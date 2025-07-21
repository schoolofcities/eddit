<script>

	import "../assets/global-styles.css"
	import uniLogos from "../assets/university-logos.svg"
	import edditLogo from "../assets/eddit-logo.svg"

</script>


<div class="footer">

	<div class="footer-content">

		<img src={edditLogo} alt="EDDIT Logo" class="logo-eddit"/>

		<p>
			<br>
				<a href="./albuquerque-nm">Albuquerque, NM</a>
				<a href="./bridgeport-ct">Bridgeport, CT</a>
				<a href="./champaign-il">Champaign, IL</a>
				<a href="./cook-county-il">Cook County, IL</a>
				<a href="./high-point-nc">Eau Claire, WI</a>
				<a href="./greensboro-nc">Greensboro, NC</a>
				<a href="./high-point-nc">Halifax, NS</a>
				<a href="./high-point-nc">High Point, NC</a>
				<a href="./wood-buffalo-ab">Wood Buffalo, AB</a>
				<a href="./worcester-ma">Worcester, MA</a>
			<br>
		</p>


		<p style="max-width: 720px; margin: 0 auto;">
			<br>
			Credits:
			<br>
			A list of everyone involved in this project
			<br><br>
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
	max-width: 700px;
	margin: 0 auto;
}

p {
	color: white;
	font-family: OpenSans;
	font-weight: normal;
	font-size: 15px;
	line-height: 20px;
	padding-left: 20px;
	padding-right: 20px;
	text-align: center;
}

a {
	color: white;
	font-family: OpenSans;
	font-weight: normal;
	padding-right: 5px;
	padding-left: 5px;
	white-space: nowrap;
	text-decoration: underline;
	/* border-bottom: solid 1px white; */
}

a:hover {
	color: var(--brandYellow);
}

.logo-unis {
	width: 275px;
	height: auto;
	display: block;
	margin: 0 auto;
}

.logo-eddit {
	width: 200px;
	height: auto;
	display: block;
	margin: 0 auto;
}

</style>