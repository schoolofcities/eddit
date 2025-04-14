<script>

	import "../assets/global-styles.css"
	import uniLogos from "../assets/university-logos.svg"
	import edditLogo from "../assets/eddit-logo.svg"

</script>


<div class="footer">

	<div class="footer-content">

		<img src={edditLogo} alt="EDDIT Logo" class="logo-eddit"/>

		<p>
			Credits....
		</p>
		<p>
			Links to other pages ...
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
	font-size: 14px;
	padding-left: 20px;
	padding-right: 20px;
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