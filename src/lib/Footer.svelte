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
			The Equitable Development Data Insight Training (EDDIT) Initiative works with organizations in small and mid-sized cities to offer free data analysis and storytelling training. In 2023-24, the initiative helped groups working toward urban equitable development to identify and build their case, translate complex data into accessible narratives, and make compelling, evidence-based arguments to influence decision-making, build trust, and mobilize support from funders, policymakers, community members, and collaborators.
			<br><br>
			EDDIT is funded by the Robert Wood Johnson Foundation.
			<br>
			<br>
			<strong>Case studies:</strong>
		</p>

		<p class="footer-link">
			<a href="./albuquerque-nm">Albuquerque, NM</a>
		</p>
		<p class="footer-link">
			<a href="./bridgeport-ct">Bridgeport, CT - Increasing tree cover for equity and climate resilience</a>
		</p>
		<p class="footer-link">
			<a href="./albuquerque-nm">Albuquerque, NM</a>
		</p>
		<p class="footer-link">
			<a href="./champaign-il">Champaign, IL</a>
		</p>
		<p class="footer-link">
			<a href="./cook-county-il">Cook County, IL</a>
		</p>
		<p class="footer-link">
			<a href="./eau-claire-wi">Eau Claire, WI</a>
		</p>
		<p class="footer-link">
			<a href="./greensboro-nc">Greensboro, NC - Increasing the availability of healthy food</a>
		</p>
		<p class="footer-link">
			<a href="./halifax-ns">Halifax, NS</a>
		</p>
		<p class="footer-link">
			<a href="./wood-buffalo-ab">Wood Buffalo, AB</a>
		</p>
		<p class="footer-link">
			<a href="./worcester-ma">Worcester, MA</a>
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
	padding-left: 20px;
	padding-right: 20px;
	text-align: left;
	width: calc(100% - 40px);
}

p strong {
	font-family: OpenSansBold;
	font-size: 18px;
	font-weight: normal;
}

.footer-link {
	margin-bottom: -0px;
}

a {
	color: white;
	font-family: OpenSans;
	font-weight: normal;
	text-decoration: underline;
}

a:hover {
	color: var(--brandYellow);
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