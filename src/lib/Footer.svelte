<script>

	import "../assets/global-styles.css"
	import uniLogos from "../assets/university-logos.svg"
	import edditLogo from "../assets/eddit-logo.svg"

</script>


<div class="footer">

	<div class="footer-content">

		<img src={edditLogo} alt="EDDIT Logo" class="logo-eddit"/>

		<p style="max-width: 720px; margin: 0 auto;  text-align: left;">
			<br><br>
			The <a href="https://www.equitabledev.org/">Equitable Development Data Insight Training (EDDIT)</a> Initiative works with organizations in small and mid-sized cities to offer free data analysis and storytelling training. In 2023-24, the initiative helped groups working toward urban equitable development to identify and build their case, translate complex data into accessible narratives, and make compelling, evidence-based arguments to influence decision-making, build trust, and mobilize support from funders, policymakers, community members, and collaborators. 
			<br><br>
			EDDIT is funded by the Robert Wood Johnson Foundation.
			<br>
			<br>
			<br>
			<strong>Case studies:</strong>
		</p>

		<p class="footer-link">
			→ <a href="./albuquerque-nm">From tracks to trail: Planning for equitable (re)development <i>- Albuquerque, NM</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./bridgeport-ct">Increasing tree cover for equity and climate resilience <i>- Bridgeport, CT</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./champaign-il">Building safe communities: Infrastructure investments for gun violence prevention <i> - Champaign, IL</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./cook-county-il">Cross-community Approaches to Climate Action: Transitioning to sustainable landscape practices <i>- Cook County, IL</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./eau-claire-wi">Connecting the Dots: Showcasing the Benefits of Public Transportation <i> - Eau Claire, WI</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./greensboro-nc">Increasing the availability of healthy food <i>- Greensboro, NC</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./halifax-ns">Becoming “Canada’s Favourite Downtown”: Encouraging investments in the core <i>- Halifax, NS</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./high-point-nc">Revitalizing historic main streets through entrepreneurship <i>- High Point, NC</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./wood-buffalo-ab">Seeking a new definition of affordability in a resource economy <i>- Wood Buffalo, AB</i></a>
		</p>
		<p class="footer-link">
			→ <a href="./worcester-ma">Investing in affordable housing to support inclusive downtowns <i>- Worcester, MA</i></a>
		</p>
		
		<p style="max-width: 720px; margin: 0 auto;  text-align: left;">
			
			<br><br><br>
		</p>

		<img src={uniLogos} alt="UofT and UCB Logos" class="logo-unis"/>

	</div>

</div>


<style>

.footer {
	width: 100%;
	background-color: var(--brandDarkBlue);
	padding-top: 50px;
	padding-bottom: 50px;
	text-align: center; 
	border-top: solid 1px var(--brandMedGreen);
}

.footer-content {
	max-width: 720px;
	margin: 0 auto;
	width: 100%;
}

p {
	color: white;
	font-family: OpenSans;
	font-weight: normal;
	font-size: 15px;
	line-height: 21px;
	padding-left: 10px;
	padding-right: 10px;
	text-align: left;
	width: calc(100% - 40px);
}

p strong {
	font-family: OpenSansBold;
	font-size: 22px;
	font-weight: normal;
}

.footer-link {
	margin-bottom: -0px;
	margin-left: 20px;
	width: calc(100% - 60px);
	margin-right: 20px;
	padding: 2px;
	padding-left: 0px;
	padding-right: 8px;
	padding-left: 1.2em;
 	text-indent: -1.2em;
	background-color: #6fc7ea1f;
}

a {
	color: white;
	font-family: OpenSansBold;
	font-weight: normal;
	text-decoration: underline;
}

.footer-link a {
	text-decoration: none;
}

a:hover {
	color: var(--brandYellow);
}

i {
	font-family: OpenSans;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}

.logo-unis {
	width: 320px;
	height: auto;
	display: block;
	margin: 0 auto;
}

.logo-eddit {
	width: 220px;
	height: auto;
	display: block;
	margin: 0 auto;
}

</style>