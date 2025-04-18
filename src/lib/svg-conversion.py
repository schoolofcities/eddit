import os
import base64
from lxml import etree
import cairosvg

INPUT_SVG_PATH = "../routes/bridgeport-ct/assets/map-asthma-360.svg"
OUTPUT_SVG_PATH = "../routes/bridgeport-ct/assets/map-asthma-360-web.svg"

FONT_MAP = {
    "Open Sans": "OpenSans",
    "OpenSans": "OpenSans",
    "Open Sans Bold": "OpenSansBold",
    "OpenSans Bold": "OpenSansBold",
    "Open Sans Italic": "OpenSansItalic",
    "OpenSans Italic": "OpenSansItalic",
    "Open Sans Bold Italic": "OpenSansBoldItalic",
    "OpenSans Bold Italic": "OpenSansBoldItalic"
}

def get_svg_pixel_dimensions(root):
    width_attr = root.get("width", "")
    height_attr = root.get("height", "")
    viewBox = root.get("viewBox")

    def parse_length(length_str):
        if length_str.endswith("px"):
            return float(length_str[:-2])
        elif length_str.endswith("pt"):
            return float(length_str[:-2]) * 1.3333
        elif length_str.endswith("mm"):
            return float(length_str[:-2]) * 3.7795
        elif length_str.endswith("cm"):
            return float(length_str[:-2]) * 37.795
        elif length_str.endswith("in"):
            return float(length_str[:-2]) * 96
        elif length_str == "":
            return None
        else:
            return float(length_str)

    width = parse_length(width_attr)
    height = parse_length(height_attr)

    if not width or not height:
        if viewBox:
            _, _, vb_width, vb_height = viewBox.strip().split()
            width, height = float(vb_width), float(vb_height)
        else:
            raise ValueError("SVG must have width/height or viewBox")

    return width, height

def apply_font_map(root, font_map, svg_ns):
    text_nodes = root.xpath(".//svg:text | .//svg:tspan", namespaces={"svg": svg_ns})
    for node in text_nodes:
        # Create a copy of all original attributes we want to preserve
        original_attrs = dict(node.attrib)
        
        # Handle style attribute separately
        style = node.get("style", "")
        style_parts = [part.strip() for part in style.split(";") if part.strip()]
        style_dict = {}
        for part in style_parts:
            if ":" in part:
                key, value = part.split(":", 1)
                style_dict[key.strip()] = value.strip()

        # Determine font properties
        font_weight = original_attrs.get("font-weight", style_dict.get("font-weight", "")).lower()
        font_style = original_attrs.get("font-style", style_dict.get("font-style", "")).lower()
        current_font = style_dict.get("font-family", original_attrs.get("font-family", ""))

        # Map to our desired font
        if "bold" in font_weight:
            if "italic" in font_style:
                final_font = "OpenSansBoldItalic"
                # Remove font-weight since we're using the actual bold font
                if "font-weight" in style_dict:
                    del style_dict["font-weight"]
            else:
                final_font = "OpenSansBold"
                # Remove font-weight since we're using the actual bold font
                if "font-weight" in style_dict:
                    del style_dict["font-weight"]
        elif "italic" in font_style:
            final_font = "OpenSansItalic"
        else:
            final_font = "OpenSans"

        # Update font family
        style_dict["font-family"] = final_font

        # Explicitly set normal weight for non-bold fonts to prevent faux-bold
        if "bold" not in final_font.lower():
            style_dict["font-weight"] = "normal"

        # Rebuild style string while preserving all other styles
        updated_style = ";".join(f"{k}:{v}" for k, v in style_dict.items())
        if updated_style:
            updated_style += ";"

        # Clear all attributes and set them back carefully
        node.attrib.clear()
        for attr, value in original_attrs.items():
            if attr not in ["font-family", "font-weight", "font-style"]:
                node.set(attr, value)
        
        # Set the updated style
        if updated_style:
            node.set("style", updated_style)
        
        # Ensure no font-weight attribute remains as an independent attribute
        if "font-weight" in node.attrib:
            del node.attrib["font-weight"]

def rasterize_non_text_elements(root, width, height, svg_ns):
    raster_root = etree.fromstring(etree.tostring(root))

    # Remove all text and tspan elements
    for elem in raster_root.xpath(".//svg:text | .//svg:tspan", namespaces={"svg": svg_ns}):
        parent = elem.getparent()
        if parent is not None:
            parent.remove(elem)

    # Handle linked raster images: embed them as base64
    for image_elem in raster_root.xpath(".//svg:image", namespaces={"svg": svg_ns}):
        href = image_elem.get("{http://www.w3.org/1999/xlink}href") or image_elem.get("href")
        if href and not href.startswith("data:"):
            image_path = os.path.join(os.path.dirname(INPUT_SVG_PATH), href)
            if os.path.exists(image_path):
                with open(image_path, "rb") as img_file:
                    img_data = img_file.read()
                mime_type = "image/png" if href.lower().endswith(".png") else "image/jpeg"
                data_uri = f"data:{mime_type};base64," + base64.b64encode(img_data).decode("utf-8")
                image_elem.set("href", data_uri)
                if "{http://www.w3.org/1999/xlink}href" in image_elem.attrib:
                    del image_elem.attrib["{http://www.w3.org/1999/xlink}href"]

    # Save and convert raster-only copy
    temp_svg_path = "temp_raster.svg"
    with open(temp_svg_path, "wb") as f:
        f.write(etree.tostring(raster_root))

    png_bytes = cairosvg.svg2png(
        url=temp_svg_path,
        output_width=int(width),
        output_height=int(height),
        dpi=96
    )
    os.remove(temp_svg_path)
    return png_bytes



def keep_only_text_elements(root, svg_ns):
    # First, make a copy of the root to work with
    new_root = etree.Element(root.tag, root.attrib)
    
    # Find all text and tspan elements
    text_elements = root.xpath(".//svg:text | .//svg:tspan", namespaces={"svg": svg_ns})
    
    # For each text element, we need to preserve its entire ancestor chain
    for text_elem in text_elements:
        # Build the ancestor chain
        ancestors = []
        current = text_elem
        while current is not None and current != root:
            ancestors.append(current)
            current = current.getparent()
        
        # Now rebuild the hierarchy in our new root
        current_parent = new_root
        for ancestor in reversed(ancestors):
            # Check if this ancestor already exists in our new tree
            existing = None
            if 'id' in ancestor.attrib:
                existing = current_parent.xpath(f"./*[@id='{ancestor.attrib['id']}']")
            
            if existing:
                current_parent = existing[0]
            else:
                # Create a new element with all original attributes
                new_elem = etree.Element(ancestor.tag, ancestor.attrib)
                current_parent.append(new_elem)
                current_parent = new_elem
        
        # Finally, add the text element itself with all its attributes
        current_parent.append(etree.Element(text_elem.tag, text_elem.attrib))
        if text_elem.text:
            current_parent[-1].text = text_elem.text
    
    # Replace the original root's content with our new content
    root.clear()
    for attr, value in new_root.attrib.items():
        root.set(attr, value)
    for child in new_root:
        root.append(child)

def embed_png_as_background(root, png_bytes, width, height, svg_ns):
    png_base64 = base64.b64encode(png_bytes).decode("utf-8")
    data_uri = f"data:image/png;base64,{png_base64}"

    viewBox = root.get("viewBox")
    if viewBox:
        x, y, vb_width, vb_height = map(float, viewBox.strip().split())
    else:
        x, y = 0, 0
        vb_width, vb_height = width, height

    # Create a group for the background image (behind everything)
    bg_group = etree.Element(f"{{{svg_ns}}}g", {"id": "background"})
    
    # Create image element with plain href (no namespace prefix)
    image_attrs = {
        "x": str(x),
        "y": str(y),
        "width": str(vb_width),
        "height": str(vb_height),
        "preserveAspectRatio": "xMidYMid meet",
        "href": data_uri  # Using plain href without namespace
    }
    image_elem = etree.Element(f"{{{svg_ns}}}image", image_attrs)
    
    bg_group.append(image_elem)
    
    # Move all existing elements (text) to a foreground group
    fg_group = etree.Element(f"{{{svg_ns}}}g", {"id": "foreground"})
    for child in root[:]:
        fg_group.append(child)
    
    # Add groups to root (background first, then foreground)
    root.append(bg_group)
    root.append(fg_group)

def process_svg(input_svg_path, output_svg_path, font_map):
    parser = etree.XMLParser(remove_comments=True, remove_blank_text=True)
    with open(input_svg_path, 'rb') as f:
        svg_data = f.read()
    root = etree.fromstring(svg_data, parser)

    nsmap = root.nsmap.copy()
    svg_ns = nsmap.get(None, "http://www.w3.org/2000/svg")

    width_px, height_px = get_svg_pixel_dimensions(root)

    # First create a copy for rasterization (before font mapping)
    raster_root = etree.fromstring(etree.tostring(root))
    png_bytes = rasterize_non_text_elements(raster_root, width_px, height_px, svg_ns)

    # Now process the original
    apply_font_map(root, font_map, svg_ns)
    keep_only_text_elements(root, svg_ns)
    embed_png_as_background(root, png_bytes, width_px, height_px, svg_ns)

    # Write the final output with clean XML
    with open(output_svg_path, 'wb') as f:
        svg_string = etree.tostring(
            root, 
            pretty_print=True, 
            xml_declaration=True, 
            encoding="UTF-8"
        )
        # Clean up any unwanted namespace prefixes
        svg_string = svg_string.replace(b'ns0:', b'').replace(b'ns1:', b'')
        f.write(svg_string)

    print(f"✅ Final output written to {output_svg_path}")

if __name__ == "__main__":
    process_svg(INPUT_SVG_PATH, OUTPUT_SVG_PATH, FONT_MAP)