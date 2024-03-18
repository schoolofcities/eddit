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
			<h1>Reinvesting in Washington Street</h1>
			<h3>Honoring High Point's Trailblazing Legacy</h3>
		</div>
	</div>

	<div class="text">
		<p>
			<b>Under construction! :) Please do not share without permission</b>
			<br />
			<i
				>This story map includes draft placeholder language to give you
				a sense of how this can be used. Please feel free to personalize
				or reuse language from the case guide.</i
			>
			<br />
			<br /><br />
			<br />
		</p>
		<p>
			Our city of High Point, North Carolina, is a beacon for other small
			cities because each of our unique neighborhoods is rich in
			community, history, and economic opportunities. Parts of our city
			have experienced significant economic growth in the last several
			years. Yet, for our community to truly succeed, everyone must
			succeed. That’s why High Point is redeveloping and reinvesting in
			Washington Street now as a down payment toward that future.
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
			Shortly after the City of High Point was incorporated in the mid
			1800s, Washington Street took shape as a cultural and economic hub,
			and a vibrant Main Street for High Point’s African American
			community - sometimes referred to as High Point’s “Black Wall
			Street”. The corridor boasted 18 black-owned businesses by 1910, and
			just over 50 by 1940, most of which were concentrated along a few
			blocks. Establishments along Washington Street included hotels, law
			and real estate offices, dentists, pharmacists, entertainment
			venues, meeting spaces, as well as several churches. Even in the
			face of the inequalities of the past, Washington Street was a
			vibrant center for African American community and business in High
			Point.
		</p>
		<p>
			Today, Washington Street remains a deeply valuable place in High
			Point. Although this corridor and the surrounding area faced various
			hurdles in the second half of the 20th century, including disruptive
			highway construction, the closure of a key educational institution,
			and broader disinvestment that occurred as integration took place in
			the late 1960s and 1970s, it represents to this day an essential
			part of High Point’s story. High Pointers are leading amazing work
			in this area. Committed organizations and local businesses are
			working to serve the community through youth programming and
			education, local food production, entertainment and community
			spaces, and restaurants. The people of Washington Street continue to
			anchor this district as an important place of heritage and community
			in High Point. Thanks to active efforts by community members,
			Washington Street was also officially recognized as a National
			Historic place in 2010.
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
	<p class="caption">
		<b>Key Places on Washington Street</b> (Map points are clickable)
	</p>

	<div class="text">
		<p>
			Washington Street is located between Downtown and High Point
			University, two areas of the city that have seen renewed activity,
			growth, and reinvestment in recent years. Given this strategic
			location, there is great potential for Washington Street and its
			surrounding neighborhood to be part of this ongoing revitalization.
		</p>
		<p>
			<b>Downtown:</b>
		</p>
		<p>
			Downtown’s revitalization has been underway thanks to private and
			public reinvestment, with the City’s goal being to draw both
			residents and visitors all year round. Two main projects helped
			catalyze this transformation: one is the Truist Point Stadium, which
			opened in 2019 and is home to the Rockers baseball team and the
			Carolina Core FC soccer team, and the other is Congdon Yards, an
			adaptive reuse of two former mill buildings that are now home to a
			an innovative design and business center. Congdon Yards offers a mix
			of offices, meeting rooms, coworking space, small-scale
			manufacturing/woodworking space, a café and restaurant, and other
			event spaces. These projects are the result of a highly
			collaborative effort between the local city government and multiple
			business and community leaders. Other businesses have opened in the
			area since then, such as Plank Street Tavern and Stock + Grain Food
			Hall.
		</p>
		<div class="image-small-width">
			<img
				src="/eddit/high-point/img-congdon-yards.png"
				alt="Your Image"
			/>
			<p class="caption">Image Source: www.congdonyards.com</p>
		</div>
		<p>
			<b>High Point University:</b>
		</p>
		<p>
			High Point University has grown exponentially since 2005, under the
			leadership of the current president, Dr. Qubein. The campus has
			grown from about 90 acres and 1,500 students in the 1990s, to over
			400 acres and over 5,000 students today, including new amenities
			that serve the campus and the community, such as a new arena and
			conference center.
		</p>
	</div>

	<div class="text">
		<h2>Mobility Data</h2>
		<p>
			Cell phone data can be used to track activity in a more granular way
			that other traditional datasets. By tracking the movement of
			individuals over time or across neighborhoods, we can pick up on
			trends, such as hubs of activity, or where people are coming from or
			going to.
		</p>
		<p>
			As an example, the map below shows activity around Washington
			Street. The concentration of activity around Downtown and High Point
			University shows the need and potential to attract more residents
			and visitors to Washington Street, to ensure that we have vibrant
			economic opportunities in all of our neighborhoods.
		</p>
	</div>

	<div class="map">
		<Cellular />
		<p class="caption">Mobility Data Source: Spectus</p>
	</div>

	<!-- <div class="text">
		<p>
			Insert example of event activity here :)
		</p>
	</div>

	<div class="image-mid-width">
		<img
			src="/eddit/high-point/location-12-and-i-still-rise.png"
			alt="Your Image"
		/>
		<p class="caption">Caption and source of image</p>
	</div> -->

	<div class="text">
		<h2>Thrive High Point</h2>
		<p>
			Our community has already invested deeply in local entrepreneurs and
			innovators through the Thrive High Point program, which began in
			2021 and is run by the City’s Chamber of Commerce. Through business
			coaching, networking, and financial support, diverse entrepreneurs -
			including women and entrepreneurs of color from across the city -
			have been supported in establishing or growing their business. Over
			500 entrepreneurs have participated in the Thrive High Point program
			since 2021. Some of these businesses are reaching a point where a
			brick-and-mortar space would allow them to continue growing,
			planting deeper roots and building greater economic opportunities in
			High Point. These businesses are well poised to contribute their
			strengths to the revitalization of Washington Street.
		</p>
		<h3>What are you hoping to gain by joining Thrive?</h3>
		<div class="image-small-width">
			<img
				src="/eddit/high-point/img-thrive-hope-to-gain.png"
				alt="Your Image"
			/>
		</div>
		<h3>How has Thrive helped your business?</h3>
		<div class="image-small-width">
			<img
				src="/eddit/high-point/img-thrive-how-has-helped.png"
				alt="Your Image"
			/>
		</div>
	</div>
</main>

<style>
</style>
