# NationalCrisis

## Data Sources
* Gun Violence Set –– https://www.kaggle.com/jameslko/gun-violence-data/version/1 
* State Populations ––  2018 Census Estimation (Annual Estimates of the Resident Population for the United States, Regions, States, and Puerto Rico: April 1, 2010 to July 1, 2018) — https://www.census.gov/data/tables/time-series/demo/popest/2010s-state-total.html#par_textimage_1574439295)
* Registered weapons – https://www.atf.gov/resource-center/docs/undefined/firearmscommercestatisticalupdate20185087-24-18pdf/download page 15 Exhibit 8. National Firearms Act Registered Weapons by State (Feb 2018) 
* Background Checks 2018 (number of people applying for weapons), used to generate rates of people applying for weapons per state, page 2/Year 2018 used – https://www.fbi.gov/file-repository/nics_firearm_checks_-_month_year_by_state.pdf/view?fbclid=IwAR3ESf6EprOikRfqxa69fzsWF1MA4j4Zud3wI_1YQKpA99zx7MCM3yKRAhE
* 2016 Presidential Election Data –– https://www.nytimes.com/elections/2016/results/president
* States that did or did not expand Medicaid –– https://familiesusa.org/product/50-state-look-medicaid-expansion
* Household Income Data: 2016 ACS median household income (dollars) estimates –– https://www.census.gov/content/dam/Census/library/publications/2017/acs/acsbr16-02.pdf
## Takeaways
* Between 2016 and 2017, 42.86% of states that expanded Medicaid saw a decrease in rates of gun suicides while 30.77% of states that did not expand Medicaid saw a decrease in rates of gun suicides.

## Inspiration
Gun violence is a major issue in our country, and it's only getting worse. We cannot attempt to address or solve the problem until we understand better what the relevant factors are. Finding the potential causes can lead to solutions – this is the heart and inspiration of this project. Where is gun violence the worst, and how can understanding these regional differences lead to better policy?

## What it does
NationalCrisis provides choropleth map visualizations of data relating to gun violence. Factors such as gun registrations, background checks, and political leanings in different regions as expressed by the 2016 election are also visualized in an attempt to find correlations between gun violence and potential related factors. Additionally, maps are provided for each year from 2013 to 2018 depicting the rate of suicide by gun deaths and their potential influence by Medicaid expansion is explored.

## How I built it
Plotly, Bootstrap, lots and lots of searching for data

## Challenges I ran into
Gun data in America is very hard to find! Factors that I thought would be easy to compare to gun violence deaths were actually really difficult if not impossible to find. I also had some issues with the statistics I did find not being as relevant of factors that I thought the would be –– for instance, background checks should indicate the applicants for gun purchases, but areas with high density of gun deaths did not necessarily relate to areas with high background check rates. Also, outliers in choropleth maps are difficult to deal with! The coloring has to be specifically and deliberately done to show any deviation in all states other than the major outlier (looking at you, Kentucky background checks).

## Accomplishments that I'm proud of
I did this project all by myself, was able to find some interesting information relating to suicide and Medicaid, and finished a project that I'm pretty proud of.

## What I learned
So much about plotly, data visualization, finding data and working with data and files, and some interesting insights about gun suicide rates in the US in recent years.

## What's next for NationalCrisis
I want to continue to implement maps for topics that I am interested in seeing potential correlation to gun violence statistics. There are numerous different things that I'd like to see, including mental health data, that I doubt I'll end up being to implement by the time we have to stop coding!

