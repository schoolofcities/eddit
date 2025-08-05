<script>

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/high-point-title.png";
	import kilbyImage from "./assets/Kilby_hotel.png";
	import ymcaImage from "./assets/YMCA.png";
	import washstImage from "./assets/img-koonts-mcghee-drug-store.png"
	import congdonImage from "./assets/congdonyards.png"

	import { CompareImage } from "svelte-compare-image";

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

    const fns = ['Kevin M Leyden, “Social Capital and the Built Environment: The Importance of Walkable Neighborhoods,” *American Journal of Public Health*, 93, 9, (2003):1546-1551, [URL](https://pmc.ncbi.nlm.nih.gov/articles/PMC1448008/#sec10).',
    	'High Point Convention & Visitors Bureau, “African American Heritage Guide,” [URL](https://visithighpoint.com/wp-content/uploads/HPCVB_AAHG-low-res-final.pdf).',
		'Jon C. Teaford, “Urban Renewal and Its Aftermath,” *Housing Policy Debate*, 11, 2 (2000): 443-465, [URL](https://doi.org/10.1080/10511482.2000.9521373).',
		'City of High Point, “Washington Street: African American Business and Cultural Center,” *City of High Point Blog*, [URL](https://www.highpointnc.gov/Blog.aspx?IID=136#:~:text=Washington%20Street%20east%20of%20Centennial,Gerran%2C%20and%20Willis%20Hinton%27s%20hotel).',
		'T. William Lester, “Economic Analysis of the High Point Market in High Point, NC,” *The High Point Market Authority*, 2019, [URL](https://www.highpointmarket.org/images/pages/economicImpact/documents/High-Point-Market-Economic-Impact-Report-2018.pdf).',
		'V. Biaett & J. Lukow, “The High Point Furniture Market: A Dilemma of Eventful Placemaking,” in *Exhibitions, Trade Fairs and Industrial Events*, eds. W. Frost and J. Laing (New York: Routledge, 2018), 39-50, [URL](https://www.academia.edu/35624640/The_High_Point_Furniture_Market_A_Dilemma_of_Eventful_Placemaking).',
		'Aggregated mobility data are provided by Cuebiq, a location intelligence platform. Data are collected from anonymized users who have opted in to provide access to their location data anonymously, through a CCPA- and GDPR-compliant framework. Through its Social Impact program, Cuebiq provides mobility insights for academic research and humanitarian initiatives. The Cuebiq responsible data sharing framework enables research partners to query anonymized and privacy-enhanced data, by providing access to an auditable, on-premise Data Cleanroom environment. All final outputs provided to partners are aggregated in order to preserve privacy.',
		'Josh Bloom, “The Future of Retail: Creative Approaches to Place-Based Entrepreneurship,” *Main Street America*, 2020, [URL](https://mainstreet.org/resources/knowledge-hub/publication/the-future-of-retail-creative-appr).',
		'BMO Financial Group, “Revitalizing Bronzeville: Growing resilient Black small businesses,” *About BMO*, [URL](https://about-us.bmo.com/revitalizing-bronzeville-growing-resilient-black-small-businesses/).',
		'Mariko Lin Chang, *Shortchanged: Why Women Have Less Wealth and What Can be Done About It* (New York: Oxford University Press, 2010).',
		'Andre M. Perry and Carl Romer, “To expand the economy, invest in Black businesses,” *Brookings*, 2020, [URL](https://www.brookings.edu/articles/to-expand-the-economy-invest-in-black-businesses/).',
		'Michael Barr, “Minority and women entrepreneurs: Building capital, networks, and skills,” *Brookings*, 2015, [URL](https://www.brookings.edu/articles/minority-and-women-entrepreneurs-building-capital-networks-and-skills/).',
		'Vincenzo Quadrini, “Entrepreneurship, Saving, and Social Mobility,” *Review of Economic Dynamics*, 3, 1 (2000): 1-40, [URL](https://doi.org/10.1006/redy.1999.0077).',
		'John Haltiwanger, Ron S. Jarmin, and Javier Miranda, “Who Creates Jobs? Small versus Large versus Young,” *The Review of Economics and Statistics*, 95, 2 (2013): 347-361, [URL](https://ideas.repec.org/a/tpr/restat/v95y2013i2p347-361.html#:~:text=Javier%20Miranda-,Abstract,businesses%20in%20U.S.%20job%20creation).',
		'Michael A. Stoll, Steven Raphael, and Harry J. Holzer, “Why Are Black Employers More Likely than White Employers to Hire Blacks?,” *Institute for Research on Poverty Discussion Paper*, no. 1236-01 (2001), [URL](https://www.irp.wisc.edu/publications/dps/pdfs/dp123601.pdf).'
    ];

</script>




<!-- <Password/> -->

<Title
	title={"Revitalizing historic main streets through entrepreneurship"}
	subtitle={"A case study of High Point, North Carolina"}
	image={titleImage}
	imageCaption={"Washington Street mural, '...and still I rise.'"}
	imageSource={"Photo by Michelle Zhang, 2023"}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='' target='_blank'>Sarah A. Smith</a> & <a href='' target='_blank'>Kathryn Exon Smith</a>"}
			graphics={"<a href='' target='_blank'>Jeff Allen</a> & <a href='' target='_blank'>Isabeaux Graham</a>"}
			date={"August 2025"}
		/>

		<p>
			Local main streets are vital community hubs and contribute to the culture and economy of entire cities. Walkable, mixed-use areas with a rich mix of businesses and cultural institutions enable vibrant gathering spaces that encourage shopping, socializing, and civic engagement. These environments not only yield economic benefits, but also strengthen community bonds and trust through increased social interaction and local participation.<Footnote id={addFootnote(fns[0])} /> The historic Washington Street neighbourhood in High Point, North Carolina has been a <strong>Black Main Street</strong> since the 1860s, known for its dense concentration of Black-owned businesses and role as a cultural hub for the African American community.<Footnote id={addFootnote(fns[1])} /> However, like many main streets, Washington Street has experienced a decline over the last few decades, and now needs strategic interventions to bring it back to life.
		</p>

	</div>

	<GraphicSingle
		svg720={"./high-point-nc/web-svg/highpoint-contextmap-720.svg"}
		svg360={"./high-point-nc/web-svg/highpoint-contextmap-360.svg"}
	/>


	<div class="text">

		<div class="callout">

			<p>
				Business High Point (BHP) launched <a href="https://www.bhpchamber.org/professionals/development/thrivehp/" target="_blank">Thrive High Point</a> in 2021 as a citywide program that provides Black- and women-owned businesses with training, business mentoring services, and access to financing and micro-grants. Since its inception, Thrive High Point has been a beacon for equitable economic development in High Point by supporting hundreds of local entrepreneurs and small businesses. Shop on Washington Street is an initiative of BHP that takes similar principles and ties them to revitalization efforts in the historic district of Washington Street.
			</p>

		</div>

		<p>
			One such intervention is Shop on Washington Street, an initiative run by <a href="https://www.bhpchamber.org/" target="_blank">Business High Point (BHP)</a>, the chamber of commerce for the city, and <a href="https://changeoftenllc.com/home" target="_blank">Change Often</a>, a local social innovation firm. This program aims to equitably redevelop the historic Washington Street business district by facilitating the placement of Black- and women-owned businesses into new and existing brick-and-mortar spaces along this historic commercial corridor. This case study highlights how these organizations worked with the <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT data storytelling team</a> to share the legacy of Washington Street through data.* It demonstrates that revitalizing this historic district presents a valuable opportunity that has the potential to stimulate local economic growth while advancing social equity and representation.
		</p>
		<p>
			Renowned as the “Furniture Capital of the World,” and home to one of the fastest-growing universities in the American South, High Point has experienced significant economic development in recent years. However, the growth has not been evenly distributed, exacerbating disparities in access to economic opportunities, amenities, and high-quality infrastructure in the city’s less wealthy neighbourhoods. These disparities are especially visible along the Washington Street corridor, which has been left behind in the city’s broader revitalization despite its location between two of High Point's bustling commercial hubs: the High Point Market downtown, and High Point University.
		</p>

	</div>

	<GraphicSingle
		svg720={"./high-point-nc/web-svg/high-point-map-720.svg"}
		svg360={"./high-point-nc/web-svg/high-point-map-360.svg"}
	/>

	<div class="text">

		<p>
			Bringing more shoppers to Washington Street can help to ensure that the corridor shares in the city’s growth. The Shop on Washington Street initiative emphasizes the street’s historical significance, filling vacant storefronts along the main street with Black- and women-owned businesses, which promotes economic inclusion and diversity, fosters entrepreneurship, creates jobs, and builds wealth. The revitalization of Washington Street has the potential to not only be part of High Point’s economic success story, but a model of equitable development for historic main streets across the country.
		</p>

		<h2>Growth and decline on Washington Street</h2>
		<p>
			Historical images can be a powerful tool in storytelling, as they can contextualize change, evoke emotion, and support narratives about places and the people that inhabit them. They can often be found at local museum websites or historical societies with large and searchable databases, offering a local perspective. The Historical Society at the <a href="https://www.highpointnc.gov/3078/Museum" target="_blank">High Point Museum</a> has many images of Washington Street in its collection, including photos of buildings and social gatherings. These types of images connect the legacy of Washington Street entrepreneurship to the current efforts of the Shop on Washington Street program. 
		</p>

		<p>
			Jim Crow racial segregation throughout the American South gave rise to the development of vibrant African American centres in cities across the U.S., showcasing the economic ingenuity and resilience of African American communities during an era of racial segregation and systemic exclusion. Business districts and commercial corridors became known as “Black Wall Streets,” with Greenwood Avenue in Tulsa, Oklahoma being the most iconic. More broadly, Black Main Streets emerged as widespread corridors that served the daily needs of African American communities, providing essential goods, services, financial institutions, lodging, places of worship, and cultural spaces. Black Wall Streets and Black Main Streets both surfaced in response to exclusion from white-owned businesses and played an important role in fostering economic independence, cultural pride, and community cohesion.
		</p>
		<p>
			As one of several historic concentrations of Black-owned businesses that grew in the United States during this era, Washington Street has long been a centre for entrepreneurship and community in High Point and was once known as the city’s “Black Wall Street.” The corridor boasted 18 Black-owned businesses by 1910 and over 50 by 1940, most of which were clustered along a few blocks. These included law offices, a public library, and accommodations such as The Kilby Hotel, The Henley Hotel, and The Hinton Hotel. Unlike many others in the area, these hotels all primarily served Black guests, who would otherwise have difficulty finding affordable places to stay in the area. 
		</p>
		<h3>The Kilby Hotel, 1981</h3>
	</div>

	<ImageSingle
		imageURL={kilbyImage}
		source="Image credit: High Point Historical Society, High Point, North Carolina. Photograph by Roy Shipman."
		maxWidth="{680}px"
		link="Yes"
	/>

	<div class="text">

		<p>
			<i><a href="https://www.highpointdiscovered.org/stories/a-legacy-that-still-stands-the-kilby-hotel-and-arcade/" target="_blank">The Kilby Hotel</a> opened in 1910, and was named after Nannie and John Kilby, who came to High Point to start their lives together in the 1890s. The couple were early investors in High Point real estate, as they built the hotel and High Point’s recreation hall for African Americans, as the city was then operating under Jim Crow laws. Shops were on the first floor, and the nightclub next to the hotel hosted jazz performers, with Nat King Cole and Ella Fitzgerald making appearances. The hotel was demolished in 2014 due to structural damage.</i>
		</p>

		<p>
			As a Black Main Street, the corridor was also a source of community networks that fostered local culture. The community of Washington Street grew to include private schools that provided quality education for the city’s African American children, at a time when public education was not available to them. Spaces such as the Young Men's Community Club, Odd Fellows Hall, and churches allowed the African American community to host events, social clubs, and civic and religious gatherings, and the neighbourhood’s theatres became bustling entertainment centres. In spite of broader racial and economic inequalities, Washington Street became a vibrant centre for the African American community in High Point, and the entrepreneurial success of its residents built wealth for the Black population and city as a whole. 
		</p>

		<h3>Women reading booklets at the Washington Street Carl Chavis YMCA, 1951</h3>
	</div>

	<ImageSingle
		imageURL={ymcaImage}
		source="Image credit: High Point Historical Society, High Point, North Carolina; Chamber of Commerce Collection."
		maxWidth="{680}px"
		link="Yes"
	/>


	<div class="text">
		<p>
			<i><a href="https://www.hpymca.org/main/our-history/" target="_blank">The YMCA of High Point</a> was established in 1923 on Washington Street, led by Edgar Hartley, with youth-centred programs like sports and Sunday school. It expanded during WWII to serve servicemen and later emphasized teen programs like Hi-Y. The Carl Chavis Branch opened in 1944 for African American youth. It was named after an African American soldier from High Point who sacrificed his life in the war.</i>
		</p>

		<p>
			However, the second half of the 20th century brought several challenges for Black Main Streets. Urban renewal programs across the country destroyed neighbourhoods with high concentrations of low-income and Black residents to make way for redevelopment, usually contributing to urban decline despite the intended efforts of “improving” the built environment.<Footnote id={addFootnote(fns[2])} /> In High Point, a new highway bisected Washington Street, and schools, cultural centres, and small businesses in the area closed down as many people moved out to the suburbs in search of more opportunities.<Footnote id={addFootnote(fns[3])} /> Many of the original buildings have been demolished due to structural damage over the years. To show the effects of these changes, the data storytelling team created interactive sliders comparing aerial views of the neighbourhood, highlighting the impacts of urban renewal over a 60-year period. 
		</p>

		<h3>Aerial view of Washington Street in 1958 and 2023</h3>

	</div>

	<div style="max-width: 680px; margin: 0 auto;">
		<CompareImage
			imageLeftSrc="/eddit/high-point/imagery-1958.png"
			imageLeftAlt="left"
			imageRightSrc="/eddit/high-point/imagery-today.png"
			imageRightAlt="right"
			--handle-size="40px"
			--slider-color="#fff"
			--slider-width="5px"
		/>
	</div>

	<div class="text">

		<p>
			While the area around Washington Street hollowed out, the rest of the city grew. Downtown High Point, located just over a kilometre from Washington Street, became a national centre for the furniture industry. By the end of World War II, <a href="https://www.highpointnc.gov/841/Furniture-History" target="_blank">60 percent of all furniture</a> in America was made within 240 kilometres (150 miles) of High Point. The furniture industry became, and continues to be, the backbone of the city's economy. In 1921, the <a href="https://www.highpointmarket.org/2025/Fall/RegistrationOpen" target="_blank">High Point Market</a> trade show attracted buyers from over 100 cities across America. Today, it is the largest home furnishings industry trade show in the world, with over 11 million square feet and 2,000 exhibitors in 180 buildings. The market holds two major shows each year, in April and October, attracting between 70,000 and 80,000 attendees and contributing US$6.73 billion to the area's economy.<Footnote id={addFootnote(fns[4])} />
		</p>

		<p>
			The cyclical nature of trade shows and the dominance of the furniture industry reshaped High Point’s downtown, and Washington Street suffered along with many other businesses as downtown economic diversity rapidly declined.<Footnote id={addFootnote(fns[5])} /> Small businesses moved to the suburbs, and the number of retail shops, personal services, and “third places” such as cafes, pool halls, and community clubs — many of which were Black-owned — decreased by 80 percent.
		</p>

		<h3>500 Washington Street, 1954 and 2023</h3>
	
	</div>

	<ImageSingle
		imageURL={washstImage}
		source={"Image credit: High Point Historical Society, High Point, North Carolina; High Point Enterprise Negative Collection"}
		maxWidth={"680px"}
	/>


	<div class="text">

		<p>
			Despite these challenges, the neighbourhood continues to evolve. The building at <a href="http://itstime2dup.com/brick" target="_blank">500 Washington Street</a>, shown in the interactive slider above, was a two-story brick commercial structure notable for its evolving architectural features and diverse tenants. Initially hosting professionals like hairdressers and insurance agents on the second floor, it was home to successive grocery stores on the first floor throughout the 1920s and 1930s. By the mid-20th century, it housed medical offices and small businesses, including the practices of Dr. J.C. Morgan, a prominent Jamaican-born dentist and civic leader. Over time, the building’s appearance changed, including a rear extension built in 1924. The building slowly fell out of use, resulting in it being demolished in early 2025. 

		</p>
		<p>
			The block it sat on is now being reimagined as a new community centre. It will house a S.T.E.M., Gym, and Arts Complex that is being designed not only to serve the current needs of the community but also to honour the neighbourhood’s rich heritage. For example, more than <a href="http://itstime2dup.com/brick" target="_blank">2,000 bricks</a> from the original building have been carefully reclaimed and will be incorporated into the new construction, ensuring that the spirit and history of Washington Street remain a visible and meaningful part of its future.
		</p>

		<h2>Centring Washington Street in High Point’s growth</h2>

		<p>
			In the 21st century, High Point has experienced a period of change and revitalization. The downtown core has grown, particularly through redevelopment efforts around the High Point Market, including the live-work-play redevelopment at <a href="https://www.congdonyards.com/" target="_blank">Congdon Yards</a>, a historic factory space. The private High Point University has also seen significant investment and growth in its campus footprint and student population, and some retail and services — typically catering to students — have been built in the surrounding area. This economic growth has not yet reached Washington Street, but there is an opportunity to create a better-connected High Point by investing in the historic and centrally located neighbourhood.
		</p>

		<h3>Congdon Yards, The Commons</h3>

	</div>

	<ImageSingle
		imageURL={congdonImage}
		source={"Image credit: Michelle Zhang (2023)"}
		maxWidth={"400px"}
	/>

	<div class="text">
		<p>
			To determine the impact of future investment, it is useful to know where people are currently spending time in the city. One way to look at this is through measuring the amount of human activity occurring in different parts of the city, showing where residents and visitors go to shop, eat, work, and play, indicating existing centres. Business Improvement Areas (BIAs), Business Improvement Districts (BIDs), and chambers of commerce often use spending or survey data for this purpose. This study’s academic research team used data from Cuebiq, an organization that provides anonymized and aggregated data collected from mobile devices.<Footnote id={addFootnote(fns[6])} /> These data show where people are spending time in the city, a useful tool to identify areas that foot traffic can be drawn from. While location intelligence data tools like this require a subscription, many non-profit and academic institutions have access to them to study mobility patterns, health, and commercial activity.
		</p>
	</div>

	<GraphicSingle
		svg720={"./high-point-nc/web-svg/highpoint-footfall-720A.svg"}
		svg360={"./high-point-nc/web-svg/highpoint-footfall-360A.svg"}
	/>

	<div class="text">

		<p>
			The above map, which shows footfall in High Point using these cell phone mobility data, reveals that there is significant activity around High Point University and the downtown area within the High Point Market. Given that both of these areas are within 800m (a half mile) of Washington Street, there is potential for it to attract residents and visitors who are already spending time nearby. By connecting, sharing in, and contributing to economic activity, a revitalized Washington Street could contribute to the growing success of the city overall.
		</p>
		<h2>Investing in entrepreneurship</h2>
		<p>
			Reviving Black Main Streets, which have suffered from decline since the 1950s, requires a multifaceted approach which focuses not only on historical preservation, but investing in opportunities for Black businesses to thrive. Main streets can act as a launchpad for entrepreneurs by offering more than just physical space: they provide a built-in community, steady foot traffic, and a strong sense of place that helps new businesses gain visibility and traction.<Footnote id={addFootnote(fns[7])} /> For example, in Chicago, organizations have been working hard to bring new life to the roaring hub of Black culture and business in the Bronzeville neighbourhood, with a focus on historical preservation and economic development. From these efforts, there has been a resurgence of Black-owned businesses, many supported by organizations such as the <a href="https://www.bronzevillechamber.com/orginial-home" target="_blank">Bronzeville Chamber of Commerce</a> and the <a href="https://chiul.org/" target="_blank">Chicago Urban League</a>.<Footnote id={addFootnote(fns[8])} /> With access to local support networks such as these, entrepreneurs are empowered to experiment, collaborate, and thrive, which fosters a culture of innovation and contributes to a resilient local economy.
		</p>
		<p>
			In a similar fashion, BHP and their Shop on Washington Street initiative is centred on establishing Black- and women-owned businesses and supporting them with training, business mentoring services, and grants. Facilitating the success of Black and female entrepreneurs is essential not only for equity but also for building community wealth. Yet these underrepresented groups face significant barriers, including limited access to capital, networks, and skill-building programs.<Footnote id={addFootnote(fns[9])} /> As the U.S. becomes more diverse, empowering these entrepreneurs is crucial for increasing overall business ownership, creating jobs, and fostering a more inclusive and resilient economy.
		</p>
		<p>
			Using an analytic framework created by <a href="https://www.brookings.edu/articles/who-is-driving-black-business-growth-insights-from-the-latest-data-on-black-owned-businesses/" target="_blank">Brookings Metro</a>, our team looked at business ownership rates across various demographics in the Greensboro-High Point metropolitan region. The graph below shows that women and Black individuals are underrepresented among business owners in the region, while white people are overrepresented. The underrepresentation of Black- and women-owned businesses limits the ability of these demographic groups to build wealth and represents unrealized revenue for the region overall.<Footnote id={addFootnote(fns[10])} /> Addressing this underrepresentation is not just a matter of equity, it’s an economic imperative with wide-reaching benefits.
		</p>

	</div>

	<GraphicSingle
		svg720={"./high-point-nc/web-svg/high-point_employer-parity-720.svg"}
		svg360={"./high-point-nc/web-svg/high-point_employer-parity-360.svg"}
	/>

	<div class="text">

		<p>
			Business ownership serves as a powerful engine for social mobility, particularly for Black populations and women, underscoring the role that inclusive main streets play in creating economic opportunity for these underrepresented groups. Research suggests that increasing entrepreneurship among Black individuals and women in the U.S. can lower income inequality and boost social mobility, helping to reduce racial wealth disparities and close the gender wealth gap.<Footnote id={addFootnote(fns[11])} /> Black entrepreneurs who start businesses are more likely to move into higher income brackets than those who do not, and are just as likely to experience upward income mobility as white entrepreneurs.<Footnote id={addFootnote(fns[12])} /> 
		</p>
		<p>
			Supporting Black and female entrepreneurs not only promotes economic equity and mobility for these underrepresented groups, but also has important benefits for their employees and the broader economy. Small and new businesses are key drivers of economic growth and innovation, generating 63 percent of net new jobs in the U.S. between 1993 and 2013 and producing more patents per employee than larger firms.<Footnote id={addFootnote(fns[13])} /> Black-owned businesses also tend to hire more Black employees than non-Black-owned businesses, which directly addresses racial disparities in employment.<Footnote id={addFootnote(fns[14])} /> Targeted investment and support for Black and female entrepreneurs in main street corridors could have wide-reaching impacts.
		</p>
		<h2>Building the bridge to success</h2>
		<p>
			Washington Street was officially recognized as a National Historic District in 2010, thanks to active efforts by the community. Today, residents consider it an essential place of heritage within High Point. Across the country, corridors like these have long served as anchors for Black communities, contributing significantly to local economies and cultural identity. As cities seek to build more inclusive economies, revitalizing historic corridors through entrepreneur-led initiatives offers a tangible way to connect economic development with community identity and well-being, ensuring that prosperity is shared across all neighbourhoods.
		</p>
		<p>
			With historical images that connect the revitalization of Washington Street with its profound legacy, and maps and data charts that show the state of business equity and areas of opportunity, this case study highlights the potential of historic main streets. Programs like Shop on Washington Street are continuing a trailblazing legacy by working to bring more Black- and women-owned businesses back into this community, promoting entrepreneurship and job creation. Initiatives like these highlight the broader economic value of supporting historically underrepresented communities in business, which not only promotes social equity but also fuels local and regional growth.
		</p>

	</div>

	<Footnotes footnotes={footnotes} />

	<div class="details">

		<h2>Additional resources</h2>

		<p>
			<a href="https://www.itstime2dup.com/about" target="_blank">About D-UP Inc.</a>
			<br><br>
			<a href="https://changeoftenllc.com/home" target="_blank">Change Often</a>
			<br><br>
			<a href="https://www.congdonyards.com/" target="_blank">Congdon Yards</a>
			<br><br>
			<a href="https://www.bhpchamber.org/" target="_blank">High Point Chamber of Commerce</a>
			<br><br>
			<a href="https://www.highpointmarket.org/2025/Fall/RegistrationOpen" target="_blank">High Point Market</a>
			<br><br>
			<a href="https://www.highpointnc.gov/3078/Museum" target="_blank">Muesum | High Point, NC</a>
			<br><br>
			<a href="https://www.bhpchamber.org/professionals/development/thrivehp/" target="_blank">Thrive High Point 2.0 | Business High Point</a>
			<br><br>
			<a href="https://www.brookings.edu/articles/who-is-driving-black-business-growth-insights-from-the-latest-data-on-black-owned-businesses/" target="_blank">Who is driving Black business growth? Insights from the latest data on Black-owned businesses</a>

		</p>

	</div>


</main>

<Footer/>