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
				<a href="./albuquerque-nm">Albuquerque, NM</a> |
				<a href="./bridgeport-ct">Bridgeport, CT</a> | 
				<a href="./champaign-il">Champaign, IL</a> |
				<a href="./cook-county-il">Cook County, IL</a> |
				<a href="./greensboro-nc">Greensboro, NC</a> |
				<a href="./high-point-nc">High Point, NC</a> |
				<a href="./wood-buffalo-ab">Wood Buffalo, AB</a> | 
				<a href="./worcester-ma">Worcester, MA</a> 
			<br>
		</p>


		<p style="max-width: 720px; margin: 0 auto;">
			<br>
			Credits: Hello World, Names List 
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
	max-width: 720px;
	margin: 0 auto;
}

p {
	color: white;
	font-family: OpenSans;
	font-size: 15px;
	line-height: 20px;
	padding-left: 20px;
	padding-right: 20px;
}

a {
	color: white;
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