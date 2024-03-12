<script>
	import Top from "../../lib/TopSofC.svelte";
	import { CompareImage } from "svelte-compare-image";
	import "../../assets/global-styles.css";
	import Map from "../../lib/MapPoints.svelte";
	import Cellular from "../../lib/MapVisits.svelte";
	import topImage from "../../assets/high-point-top-image.png";
</script>

<svelte:head>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>
</svelte:head>

<!-- <Top /> -->

<main>
	<div class="top-image" style="background-image: url('{topImage}');">
		<div class="title">
			<h1>High Point Story Map Title</h1>
			<h3>A Short Subtitle</h3>
		</div>
	</div>

	<div class="text">
		<p>
			<b>Under construction! :) Please do not share without permission</b>
		</p>
		<p>
			High Point is a beacon for other small cities because each of our
			unique neighborhoods – from downtown to Washington Street – has what
			they need to succeed. We have diverse economic opportunities,
			thriving businesses, an abundance of housing, and transportation to
			support people as they move around the city. For our community to
			succeed, everyone must succeed. That’s why High Point is
			redeveloping and reinvesting in Washington Street now as a down
			payment toward that future.
		</p>
		<p>
			We as High Pointers have experienced, and invested in, tremendous
			growth across our city in the last several years. To ensure that all
			of our residents can thrive, we need to make sure this growth and
			opportunity is equitable across our city. If our Downtown is
			thriving but other parts of our city are not, we need to ask, why?
			If we don’t act now to reinvest in Washington Street, we risk
			creating a larger divide in our community and losing the opportunity
			to tap into its amazing potential. We want equitable revitalization
			across the City of High Point.
		</p>
	</div>

	<div class="image-mid-width">
		<img src="/eddit/high-point/high-point-ref-map.png" alt="Your Image" />
		<p class="caption">
			<b>Location of Washington Street in High Point, NC.</b>
		</p>
	</div>

	<div class="text">
		<p>Washington Street has a unique and rich history in High Point.</p>

		<p>
			Shortly after High Point was incorporated in the mid 1800s,
			Washington Street took shape as a cultural and business hub in High
			Point, a vibrant ‘Main Street’ or ‘Black Wall Street’ of High
			Point’s African American community. According to Visit High Point,
			Washington Street boasted 18 black-owned businesses by 1910, and
			just over 50 by 1940, most of which were concentrated along a few
			blocks. The amenities of Washington Street included churches,
			hotels, law and real estate offices, dentists, pharmacists,
			entertainment venues, and meeting spaces. “Despite the inequalities
			of the past, Washington Street became a bustling center of African
			American education, business, worship, entertainment, and
			community.”
		</p>
		<p>
			Although Washington Street has faced hurdles since the 1960s -
			including disruptive highway construction, the closure of a key
			nearby educational institution, and broader disinvestment as
			integration occurred in the late 1960s and 1970s, today, Washington
			Street remains a deeply valuable place in High Point.
		</p>
	</div>

	<div class="image-mid-width">
		<CompareImage
			imageLeftSrc="/eddit/high-point/imagery-1958.png"
			imageLeftAlt="left"
			imageRightSrc="/eddit/high-point/imagery-today.png"
			imageRightAlt="right"
			--handle-size="3rem"
			--slider-color="white"
			--slider-width="0.17rem"
		/>
		<p class="caption">
			<b>Aerial view of Washington Street in 1958 and 2023</b> / Source: City
			of High Point, ESRI
		</p>
	</div>

	<div class="image-mid-width">
		<img
			src="/eddit/high-point/img-koonts-mcghee-drug-store.png"
			alt="Your Image"
		/>
		<p class="caption">
			<b>Koonts-McGhee Drug Store Building, 1954 and 2023</b> / Source: ...
		</p>
	</div>

	<div class="text">
		<p>
			Today, High Pointers are leading amazing work in this area.
			Committed organizations and businesses are working to serve the
			community through youth programming and education, local food
			production, entertainment and community spaces, and restaurants. The
			people of Washington Street continue to anchor this district as an
			important place of heritage and community in High Point.
		</p>
	</div>

	<div class="map">
		<Map />
	</div>

	<div class="text">
		<p>
			Washington Street is strategically located between Downtown and High
			Point University, two areas of the city that have seen new
			development activity and reinvestment in recent years. Given its
			strategic location between these areas, Washington Street and its
			surrounding neighborhood has great potential to also participate in
			-- and importantly also benefit from -- this revitalization.
		</p>
		<h2>Investment</h2>
		<p>
			Vitae tortor condimentum lacinia quis vel eros donec ac odio. Mi
			quis hendrerit dolor magna eget est. Vivamus at augue eget arcu
			dictum varius. Ac placerat vestibulum lectus mauris ultrices eros in
			cursus turpis. Fusce ut placerat orci nulla. Et odio pellentesque
			diam volutpat commodo sed egestas egestas fringilla. Risus sed
			vulputate odio ut enim blandit volutpat. Enim diam vulputate ut
			pharetra sit amet aliquam id diam. Ut ornare lectus sit amet est.
			Tempor commodo ullamcorper a lacus. Diam phasellus vestibulum lorem
			sed.
		</p>
	</div>

	<div class="text">
		<h2>Mobility Data</h2>
		<p>
			Cell phone data can be used to track activity in a more granular way
			that other traditional datasets. By tracking the movement of
			individuals over time and across neighborhoods, we can pick up on
			trends, such as hubs of activity, or where people are coming from or
			going to, or more generally get a sense for how many visitors to
			other areas of the city could be directed to Washington Street for
			example.
		</p>
		<p>
			As a first example, the map below shows activity around Washington
			Street
		</p>
	</div>

	<div class="map">
		<Cellular />
		<p class="caption">Mobility Data Source: Spectus</p>
	</div>

	<div class="text">
		<p>
			Quisque id diam vel quam elementum pulvinar etiam non quam. Faucibus
			pulvinar elementum integer enim neque volutpat. Consequat nisl vel
			pretium lectus. Eleifend quam adipiscing vitae proin sagittis nisl
			rhoncus. Tincidunt dui ut ornare lectus sit amet est. Eu augue ut
			lectus arcu bibendum at varius vel pharetra. Non diam phasellus
			vestibulum lorem sed risus. Diam sollicitudin tempor id eu nisl.
			Urna nunc id cursus metus aliquam eleifend mi in nulla.
		</p>
	</div>

	<div class="text">
		<p>
			Quisque id diam vel quam elementum pulvinar etiam non quam. Faucibus
			pulvinar elementum integer enim neque volutpat. Consequat nisl vel
			pretium lectus. Eleifend quam adipiscing vitae proin sagittis nisl
			rhoncus. Tincidunt dui ut ornare lectus sit amet est. Eu augue ut
			lectus arcu bibendum at varius vel pharetra. Non diam phasellus
			vestibulum lorem sed risus. Diam sollicitudin tempor id eu nisl.
			Urna nunc id cursus metus aliquam eleifend mi in nulla.
		</p>
	</div>

	<div class="image-mid-width">
		<img
			src="/eddit/high-point/location-12-and-i-still-rise.png"
			alt="Your Image"
		/>
		<p class="caption">Caption and source of image</p>
	</div>

	<div class="text">
		<h2>TRHIVE</h2>
		<p>
			High Point has already invested deeply in local entrepreneurs,
			innovators, and makers through the Thrive High Point program, which
			is run by the City’s Chamber of Commerce. Through business coaching,
			networking, and financial support, a diverse set of local
			entrepreneurs from across the city have been able to establish
			businesses in spite of the barriers that women and people of color
			often face. Many of these businesses are reaching a point where a
			brick-and-mortar space would allow them to grow and plant roots and
			build economic opportunity in High Point. These businesses are well
			poised to contribute their strengths and innovation to the
			revitalization of Washington Street.
		</p>
		<h3>What are you hoping to gain by joining THRIVE?</h3>
		<div class="image-small-width">
			<img
				src="/eddit/high-point/img-thrive-hope-to-gain.png"
				alt="Your Image"
			/>
		</div>
		<h3>How has THRIVE helped your business?</h3>
		<div class="image-small-width">
			<img
				src="/eddit/high-point/img-thrive-how-has-helped.png"
				alt="Your Image"
			/>
		</div>
		<p>
			Vitae tortor condimentum lacinia quis vel eros donec ac odio. Mi
			quis hendrerit dolor magna eget est. Vivamus at augue eget arcu
			dictum varius. Ac placerat vestibulum lectus mauris ultrices eros in
			cursus turpis. Fusce ut placerat orci nulla. Et odio pellentesque
			diam volutpat commodo sed egestas egestas fringilla. Risus sed
			vulputate odio ut enim blandit volutpat. Enim diam vulputate ut
			pharetra sit amet aliquam id diam. Ut ornare lectus sit amet est.
			Tempor commodo ullamcorper a lacus. Diam phasellus vestibulum lorem
			sed.
		</p>
	</div>
</main>

<style>
</style>
