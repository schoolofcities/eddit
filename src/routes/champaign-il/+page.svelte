<script>

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/champaign-title.jpg";
	import streetlightImage from "./assets/streetlight.jpeg";

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = ['Erin Grinshteyn and David Hemenway, “Violent death rates in the US compared to those of the other high-income countries, 2015,” *Preventive Medicine* 123 (2019): 20–26. [URL](https://pubmed.ncbi.nlm.nih.gov/30817955/)',
		'Magic M. Wade, “Not as Bad as the ‘90s”? Firearm Violence in Small, Mid-Size, and Large US Cities, 2015–2021,” *Homicide Studies* 0 (2023). [URL](https://doi.org/10.1177/10887679231163287).',
		'Wade, “Not as Bad as the ‘90s”?',
		'City of Champaign, “PL-25-19 Amendment to the Comprehensive Plan - Garden Hills Strategic Neighborhood Action Plan,” May 2025. [URL](https://engagechampaign.org/18229/widgets/57761/documents/67786).',
		'City of Champaign, “Garden Hills Strategic Neighborhood Action Plan.”',
		'Elizabeth Griffiths and Jorge M. Chavez, “Communities, street guns and homicide trajectories in Chicago, 1980–1995: Merging methods for examining homicide trends across space and time,” *Criminology* 42, no. 4 (2006): 941–978. [URL](https://doi.org/10.1111/j.1745-9125.2004.tb00541.x); Patrick Sharkey, *Uneasy Peace: The Great Crime Decline, the Renewal of City Life, and the Next War on Violence* (WW Norton & Company, 2018).',
		'David Weisburd et al., “Understanding the Mechanisms Underlying Broken Windows Policing: The Need for Evaluation Evidence,” *Journal of Research in Crime and Delinquency* 52, no. 4 (2015): 589–608. [URL](https://doi.org/10.1177/0022427815577837).',
		'Ngozi C. Kamalu and Emmanuel C. Onyeozili, "A Critical Analysis of the ‘Broken Windows’ Policing in New York City and Its Impact: Implications for the Criminal Justice System and the African American Community," *African Journal of Criminology and Justice Studies* Vol. 11: Iss. 1, Article 6 (2018). [URL](https://digitalscholarship.tsu.edu/ajcjs/vol11/iss1/6).',
		'Jane Jacobs, *The Death and Life of Great American Cities* (New York: Random House, 1961).',
		'Beth E. Molnar et al., “Neighborhood Predictors of Concealed Firearm Carrying Among Children and Adolescents: Results From the Project on Human Development in Chicago Neighborhoods,” *Archives of Pediatrics & Adolescent Medicine* 158, no. 7 (2004): 657–664. [URL](https://pubmed.ncbi.nlm.nih.gov/15237065/)',
		'Yusuf Bicer et al., “Influence of urban layout on crime incidence using UAV images,” *Spatial Information Research* 33, article 20 (2025). [URL](https://doi.org/10.1007/s41324-025-00618-z).',
		'Brandon Welsh and David P. Farrington, *The Oxford Handbook of Crime Prevention* (Oxford University Press, 2012).',
		'Robert J. Sampson, Stephen W. Raudenbush, and Felton Earls, “Neighborhoods and violent crime: A multilevel study of collective efficacy,” *Science* 277 (1997): 918–924. [URL](https://pubmed.ncbi.nlm.nih.gov/9252316/); Richard P. Taub, Garth Taylor, and Jan D. Dunham, *Paths of Neighborhood Change: Race and Crime in Urban America* (University of Chicago Press, 1984); R. B. Taylor and S. Gottfredson, “Environmental design, crime and prevention: An examination of community dynamics,” in *Communities and Crime*, eds. A. J. Reiss & M. Tonry (University of Chicago Press, 1986).',
		'Gregory Breetzke et al., “Greenspace and gun violence in Detroit, USA,” *International Journal of Criminal Justice Sciences* 15, no. 2 (2020): 248–265. [URL](https://doi.org/10.5281/zenodo.3865608).',
		'Charles C. Branas et al., “Urban blight remediation as a cost-beneficial solution to firearm violence,” *American Journal of Public Health* 106, no. 12 (2016): 2158–2164. [URL](https://pubmed.ncbi.nlm.nih.gov/27736217/).',
		'Justin E. Heinze et al., “Busy Streets Theory: The Effects of Community-engaged Greening on Violence,” *American Journal of Community Psychology* 62, no. 1–2 (2018): 101–109. [URL](https://doi.org/10.1002/ajcp.12270).',
		'Branas et al., “Urban blight remediation.”'
	];

	let title = "Building Safe Communities: Infrastructure investments for gun violence prevention"
	let subTitle = "A case study of Champaign, Illinois"

</script>


<svelte:head>

	<title>{title}  | School of Cities</title>

	<meta name="description" content={subTitle} />
	<meta name="author" content="School of Cities, University of Toronto">

	<meta property="og:title" content={title} />
	<meta property="og:description" content={subTitle} />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/design-components/" />
	<meta property="og:image" content="https://raw.githubusercontent.com/schoolofcities/eddit/main/static/web-card.png" />
	<meta property="og:locale" content="en_CA">

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={subTitle} />
	<meta name="twitter:site" content="https://schoolofcities.github.io/eddit/" />
	<meta name="twitter:image" content="https://raw.githubusercontent.com/schoolofcities/eddit/main/static/web-card.png" /> 

</svelte:head>


<!-- <Password/> -->

<Title
	title={"Building Safe Communities: Infrastructure investments for gun violence prevention"}
	subtitle={"A case study of Champaign, Illinois"}
	image={titleImage}
	imageCaption={"Beginning phase of improvements in Garden Hills, 2024."}
	imageSource={"Photo by Evelyne St-Louis."}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='https://www.linkedin.com/in/sarah-a-smith-79089b2a0/' target='_blank'>Sarah A. Smith</a> & <a href='https://www.linkedin.com/in/kathrynexonsmith/' target='_blank'>Kathryn Exon Smith</a>"}
			graphics={"<a href='http://linkedin.com/in/isabeaux-graham/' target='_blank'>Isabeaux Graham</a>, <a href='https://www.linkedin.com/in/julia-greenberg-23114a130/' target='_blank'>Julia Greenberg</a>, & <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>"}
			date={"September 2025"}
		/>

		<p>
			Gun violence in the United States is a persistent and deeply entrenched public health crisis, with particularly severe impacts on young people and communities of colour. The U.S. firearm homicide rate is staggeringly high compared to other high-income nations, and Americans make up the vast majority of global gun deaths.<Footnote id={addFootnote(fns[0])} /> In response to this crisis, cities are rethinking what it means to prevent gun violence by focusing not just on law enforcement, but on the physical and social conditions that allow violent crimes to persist.
		</p>
		<p>
			Increasingly, city councils are prioritizing gun violence prevention through investments in community safety initiatives that go beyond policing. These include built environment interventions, such as improved lighting, street maintenance, and greening vacant lots, which can reduce opportunities for violence while also enhancing residents' quality of life and well-being. Such strategies are rooted in the understanding that addressing gun violence requires more than reacting to individual crimes: it demands proactive, structural solutions that make neighbourhoods safer and more livable.
		</p>
		<p>
			Gun violence in the U.S. is often associated with large cities, but small and mid-sized cities are also significantly affected. Though gun violence has been rising in cities of all sizes, between 2015 and 2023, 42 percent of gun homicides and 37 percent of non-fatal gun incidents occurred in cities with populations under 250,000.<Footnote id={addFootnote(fns[1])} /> The pandemic also exacerbated gun violence nationwide, driven by factors such as weakened community support, social isolation, and job instability. In 2020, the highest per capita death rate from gun violence in any American community was 111 per 100,000 in Selma, Alabama, which has a population of only 17,971.<Footnote id={addFootnote(fns[2])} />
		</p>
		<p>
			Black Americans are disproportionately <a href="https://publichealth.jhu.edu/2022/gun-deaths-spiked-during-the-pandemic" target="_blank">affected</a>, facing gun homicide rates nearly 14 times higher than white Americans. This disparity is evident in smaller cities like Champaign, Illinois, where gun violence is concentrated in predominantly Black and Hispanic neighbourhoods, such as Garden Hills. The Garden Hills neighbourhood was built in the 1950s as a postwar suburban subdivision, and originally had minimal physical public infrastructure.<Footnote id={addFootnote(fns[3])} /> Today, the neighbourhood is home to approximately 4,600 residents in 1,600 homes, who have repeatedly called for infrastructure and public safety improvements to address these deficits.<Footnote id={addFootnote(fns[4])} /> 
		</p>

	</div>

	<GraphicSingle
		svg720={"./champaign-il/web-svg/champaign-contextmap-720.svg"}
		svg360={"./champaign-il/web-svg/champaign-contextmap-360.svg"}
	/>

	<div class="text">

		<p>
			In response, the City of Champaign has adopted a holistic approach aimed at improving both public safety and neighbourhood well-being in Garden Hills. In early 2022, the city council approved the <a href="https://champaignil.gov/equity-and-engagement-department/community-safety-and-justice-division/blueprint/" target="_blank">Community Gun Violence Reduction Blueprint</a> (CGVRB), a strategic framework focused on addressing gun violence at its roots through promoting safety and prevention, enhancing community engagement, and ensuring data-driven decision making. Around the same time, the city began working on the <a href="https://engagechampaign.org/garden-hills-strategic-neighborhood-action-plan" target="_blank">Garden Hills Strategic Neighborhood Action Plan</a> (GH-SNAP), which focuses on infrastructure investments that improve the quality of life in the neighbourhood. This includes the installation of new street lighting, sidewalks, and stormwater basins, and the development of community parks and pathways. Some of the improvements that began in 2023 and 2024 are the focus of this case study, but investments are ongoing and are planned to continue into at least 2026.
		</p>
		<p>
			The city’s gun violence prevention efforts and the infrastructure improvement project were run by different departments, yet both were partially funded through the <a href="https://www.congress.gov/bill/117th-congress/house-bill/1319" target="_blank">American Rescue Plan Act</a> (ARPA). The city used this synergy to demonstrate a new model of community investment, which reflects a growing recognition that the built environment plays a critical role in shaping social outcomes, including public health and safety. The <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT team</a> worked with the City of Champaign to develop a data story which highlights their recent community-centred investments in infrastructure and how these relate to gun violence prevention. This case study underscores the importance of political will in sustaining these kinds of integrated strategies, ensuring they remain a priority beyond short-term funding cycles. It encourages leaders to commit to preventive, equity-focused investments that address the root causes of violence and promote long-term community resilience. 
		</p>
		<h2>Advocating for gun violence prevention</h2>
		<p>
			In response to the sharp increase in urban gun violence in the U.S. in the 1970s and 1980s, a new policing philosophy known as the “broken windows” approach gained national traction.<Footnote id={addFootnote(fns[5])} /> The theory suggested that neglecting minor forms of disorder, such as vandalism or public loitering, could create an environment that fosters more serious crime. This led to widespread adoption of aggressive policing strategies that emphasized arrests for low-level offenses as a means of deterring larger crimes.<Footnote id={addFootnote(fns[6])} /> However, this approach disproportionately targeted communities of colour, especially youth, who bore the brunt of intensified surveillance and punitive enforcement.<Footnote id={addFootnote(fns[7])} /> 
		</p>
		<p>
			Today, advocacy around gun violence prevention calls for a fundamental shift away from these reactive enforcement models and toward proactive, community-driven strategies that address the root causes of violence. Many cities have approached this through a <a href="https://www.brookings.edu/articles/a-new-community-safety-blueprint-how-the-federal-government-can-address-violence-and-harm-through-a-public-health-approach/#:~:text=Another%20promising%20model%2C%20Advance%20Peace%2C%20contributed%20to,drop%20in%20gun%20homicides%20in%20Stockton%2C%20Calif" target="_blank">public health lens</a> by creating policies and programs that are focused on stopping violence before it happens, and are structured to improve residents’ overall quality of life. These interventions have focused on economic and housing security, youth education and workforce development, and the creation of welcoming community spaces. By prioritizing prevention over punishment, cities such as <a href="https://philadelphiaskills.org/" target="_blank">Philadelphia</a>, <a href="https://www.boston.gov/departments/youth-employment-and-opportunity" target="_blank">Boston</a>, and <a href="https://www.kansascityfed.org/research/research-working-papers/the-effect-of-housing-first-programs-on-future-homelessness-and-socioeconomic-outcomes/" target="_blank">Los Angeles</a> have moved toward community investment strategies that promote healthier and safer cities.
		</p>
		<p>
			While traditional narratives around gun violence have generally focused on the crime itself and the resulting loss of life, preventative approaches to addressing gun violence frame the issue in a more hopeful and positive way by focusing on how lives can be saved and violence can be avoided altogether. For example, statistics might focus on the years of human life that could be saved if gun violence was prevented, instead of highlighting how many people have died from these incidents. This kind of data representation underscores that the goal of effective violence prevention is to invest in people’s lives and their communities.
		</p>
	</div>

	<GraphicSingle
		svg720={"./champaign-il/web-svg/Champaign_lives-lost-chart-720.svg"}
		svg360={"./champaign-il/web-svg/Champaign_lives-lost-chart-360.svg"}
	/>

	<div class="text">
		<h2>Lighting the way to safety</h2>

		<p>
			The urbanist Jane Jacobs argued that the self-regulating nature of communities — particularly the presence of “eyes on the street” — plays a vital role in maintaining safety and social order.<Footnote id={addFootnote(fns[8])} /> Social order is the idea that people feel safe walking in their neighbourhoods and engaging in their daily activities without perceiving a threat from fellow citizens.<Footnote id={addFootnote(fns[9])} /> To feel safe, especially at night, it is important that there is sufficient outdoor lighting. Street and home exterior lights become essential, not only for improving visibility, but also for encouraging informal monitoring among neighbours.
		</p>
		<p>
			Community lighting has emerged as a widely adopted intervention in efforts to improve community safety and has been shown to decrease criminal activity.<Footnote id={addFootnote(fns[10])} />  While there is mixed evidence supporting the direct correlation between street lighting and gun violence specifically, studies have found a relationship between streetlighting and reductions in overall crime rates. Well-lit communities extend the hours people spend in public spaces, which increases the “eyes on the street” and discourages crime due to the likelihood of detection.<Footnote id={addFootnote(fns[11])} /> 
		</p>
		<p>
			Infrastructure like lighting also plays a powerful role in strengthening community pride, cohesion, and responsibility. Investments in the built environment can lead residents to view their community more positively, be more proactive about protecting their neighbourhood, and be more likely to intervene in potential criminal offences.<Footnote id={addFootnote(fns[12])} /> When integrated into broader strategies for violence prevention, improved lighting can contribute to a greater sense of safety and cohesion — especially in neighbourhoods that have experienced long-term disinvestment. 
		</p>

	</div>


	<ImageSingle
		imageURL={streetlightImage}
		caption={"Streetlight improvements in Garden Hills."}
		source={"Photo credit: Julia Greenberg."}
		maxWidth={"450px"}
	/>

	<div class="text">

		<p>
			As mentioned previously, the Garden Hills community has suffered from an infrastructure deficit, including minimal streetlighting. One of the infrastructure improvements the city made in the Garden Hills neighbourhood was an extensive community lighting upgrade that aimed to improve residents’ sense of safety. The initiative involved two programs, one for installing new streetlights and one for providing exterior lights to residential homes. As of 2024, the city has installed 388 home exterior lights and 288 streetlights throughout the community. The map below shows the locations of these lights in Garden Hills. With more extensive coverage, violence is being prevented, and residents walking through the neighbourhood can feel safer.
		</p>

	</div>

	<GraphicSingle
		svg720={"./champaign-il/web-svg/Champaign_street-lighting-map-720.svg"}
		svg360={"./champaign-il/web-svg/Champaign_street-lighting-map-360.svg"}
	/>

	<div class="text">

		<h2>Turning vacant spaces into connected communities</h2>

		<p>
			Urban areas have long experienced unequal maintenance and development due to discrimination, prejudice, historical injustices, and cycles of physical and structural violence. Because disinvestment in the built environment <a href="https://www.urban.org/research/publication/engaging-communities-reducing-gun-violence-road-map-safer-communities" target="_blank">directly contributes</a> to incidents of gun violence, investing in the repair of neglected areas can have an immediate impact on reducing it. In communities that often lack public amenities, city leaders can demonstrate a long-term commitment to safety and well-being by creating or revitalizing green spaces. Transforming underutilized spaces through dedicated community engagement efforts offers residents new places to spend time and connect with one another.
		</p>
		<p>
			Parks, community gardens, and open recreational areas provide safe, accessible environments where residents can gather, build relationships, and engage in healthy activities. Research has shown that well-maintained green spaces can reduce stress, foster social cohesion, and even lower crime rates through informal community supervision.<Footnote id={addFootnote(fns[13])} /> A 2016 study found that cleaning, greening, and maintaining vacant lots led to significant reductions in gun violence.<Footnote id={addFootnote(fns[14])} /> In Flint, Michigan, neighbourhoods that cleaned and maintained vacant lots in their communities through the <a href="https://www.thelandbank.org/cleanandgreen.asp" target="_blank">Clean & Green program</a> saw 40 percent fewer violent crimes than other neighbourhoods.<Footnote id={addFootnote(fns[15])} /> 
		</p>
		<p>
			It can often be challenging to find room in municipal budgets for this kind of infrastructure maintenance, but research has indicated that these improvements can yield sufficient economic benefits to make the investment worthwhile. Urban blight remediation programs have been shown to have a return on investment between US$79 and $333 for every dollar spent in the first year, when accounting for the decrease in costs to the criminal justice system that result from reductions in firearm crimes.<Footnote id={addFootnote(fns[16])} /> These findings highlight how targeted investments in the built environment can serve as cost-effective strategies for violence prevention and broader community well-being.
		</p>
		<p>
			Building on the evidence that creating new green spaces and activating vacant areas can reduce violence and improve community well-being, the City of Champaign embraced this kind of community investment through projects like the Safe Places/Active Spaces – Hedge POP! Park. This pop-up park was intended to be temporary while land was being cleared for the Garden Hills Drainage Improvements project, serving to activate and beautify the space while final engineering work was underway. More than just a stopgap, Hedge POP! Park quickly revealed a deeper, unmet need for accessible recreational areas in the neighbourhood. The park not only provided a safe and welcoming place for residents to gather, play, and relax, but it also became a valuable touchpoint for city staff to build relationships and engage with the community. Through regular on-site interactions, staff were able to hear directly from residents about their needs, ideas, and concerns, making the park both a recreational asset and a platform for participatory planning.
		</p>
		<p>
			Hedge POP! Park demonstrates how infrastructure interventions can yield meaningful insights, build trust, and lay the groundwork for long-term investments that reflect the community’s vision for safety, equity, and connection while working to prevent gun violence. The city is planning to build a park in the same location to create a hub for the community that will include a splash pad, playground, basketball court, and seating. The map below shows that most of Garden Hills — including more than 4,000 residents — will be able to walk to the new park within 15 minutes.
		</p>

	</div>

	<GraphicSingle
		svg720={"./champaign-il/web-svg/Champaign_access-map-720.svg"}
		svg360={"./champaign-il/web-svg/Champaign_access-map-360.svg"}
	/>

	<div class="text">
		<h2>Investing in a new era of safety</h2>

		<p>
			The City of Champaign worked with the EDDIT data storytelling team to create crime data visualizations to show that there had been measurable decreases in gun violence over the period of recent community investments such as CGVRB and GH-SNAP. However, while these charts demonstrate that gun violence declined as investments increased, this relationship does not necessarily mean that these investments caused the reductions in crime. Many factors can influence gun violence trends, and without more rigorous analysis, it is difficult to conclude that the investments directly played a role in improving public safety. It’s possible that other social, economic, or policy changes played a role as well.
		</p>

	</div>

	<GraphicSingle
		svg720={"./champaign-il/web-svg/Champaign_shooting-incidents-bars-720.svg"}
		svg360={"./champaign-il/web-svg/Champaign_shooting-incidents-bars-360.svg"}
	/>

	<div class="text">

		<p>
			These clear and accessible charts and maps are tools the city can use to build public trust, validate its prevention-focused approach, and galvanize continued support for long-term investment in community-driven solutions. The City of Champaign’s experience illustrates how targeted investments can serve as a powerful tool for gun violence prevention and neighbourhood transformation, particularly in historically disinvested communities. By moving beyond traditional enforcement models and focusing instead on the physical and social environments where violence takes root, the city has embraced a holistic approach that centres equity and long-term impact. The combination of improved lighting, new green spaces, and community engagement has fostered a renewed sense of safety and connection in Garden Hills. As cities across the U.S. seek to address the complex drivers of gun violence, they can learn from Champaign’s approach to improving public safety through enhancing public infrastructure.
		</p>

		<br>
		<p style="font-size: 16px; line-height: 25px;">
			<i>The authors would like to thank Karen Chapple, Michelle Zhang, Julia Greenberg, and Evelyne St-Louis for their contributions to editing and informing this case study.</i>
		</p>
		<br>

		<Footnotes footnotes={footnotes} />

		<div class="details">

			<h2>Additional resources</h2>

			<p>
				<a href="https://www.brookings.edu/articles/a-new-community-safety-blueprint-how-the-federal-government-can-address-violence-and-harm-through-a-public-health-approach/#:~:text=Another%20promising%20model%2C%20Advance%20Peace%2C%20contributed%20to,drop%20in%20gun%20homicides%20in%20Stockton%2C%20Calif" target="_blank">A new community safety blueprint</a>
				<br><br>
				<a href="https://www.congress.gov/bill/117th-congress/house-bill/1319" target="_blank">American Rescue Plan Act (ARPA)</a>
				<br><br>
				<a href="https://champaignil.gov/equity-and-engagement-department/community-safety-and-justice-division/blueprint/" target="_blank">Community Gun Violence Reduction Blueprint, City of Champaign</a>
				<br><br>
				<a href="https://www.urban.org/research/publication/engaging-communities-reducing-gun-violence-road-map-safer-communities" target="_blank">Engaging Communities in Reducing Gun Violence: A Road Map for Safer Communities</a>
				<br><br>
				<a href="https://engagechampaign.org/garden-hills-strategic-neighborhood-action-plan" target="_blank">Garden Hills Strategic Neighborhood Action Plan</a>
			</p>

		</div>

	</div>

</main>

<Footer/>