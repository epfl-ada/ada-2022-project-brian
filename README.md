# Title: What’s the perfect beer (for me) ?

## Abstract: (up to 150 words)
The purpose of the program will be matching a person with a beer in function of his review and from biases. At the end the reader will receive the name of his “perfect beer” and some information about it like the style of the beer and the name of the brewery. The way of finding this beer is explained in the method part. However, there is a chance that this “perfect beer” doesn’t exist.

## Research questions: 
1. **General trends worldwide**
	1. Is beer appreatiated in the same form across the world?
	2. How beer production is distributed around the globe? (As a matter of countries and regions)
	3. How users are distributed across the world? 
		1. Are they uniformely correlated with the contries population and/or beer production?
	4. Are there any region where users are more actively?
		1. Can we associate them with being more beer enthusists? \
	5. Is there any metrics we can develop to indicate the users' expertise, and the degree that she/he is a beer enthusiast? 
		1. (e.g. the number of reviews in the platform, how her/his reviews deviate from the average, etc..)
		2. Is this level of beer appreatiation correlated with any specific countries/regions?
2. **Analysis of user preferences**
	1. Can we develop metrics that are associated with users' individual preferences? E.g. preferences of beers with a certain style or from a certain country/region.
	2. How are these users preferences associated with the origin of the reviewer? Does they have any biases for prefering beers / styles original from their own country?
	3. Can we distinguish the real user preferences from possible confounders? E.g. the (possibly restricted) range of offer of beers brands/types in certain regions?
3. **Analysis of beer attributes**
	In the dataset, we have information about ratings accross *attributes* (e.g. appearance, aroma, etc...). 
	1. Is any of these attributes more important for the final evaluation of the beer?
	2. Does this most important attribute varies across regions/countries and beer styles?
4. **Recommendation system**
	1. With all the knowledge gained in this analysis, can we build a recommendation system for suggesting beer products for new users?
	2. That is, can available features, e.g. nationality, favorite beer style and preffered beer attribute, be used to "predict" or "suggest" new beers for the person which is reading our datastory? 


## Methods
For each section of the project, specific steps and methods are here outlined, corresponding to the research questions that our datastory will aim at answering.

### Worldwide trends 

### Individual preferences
Here, firstly, some metrics will be put in place in order to relate the users' reviews history with their personal preferences regarding beer style and/or beer country. They are initially though to be intimately related to the the scores the user gives on avarage for each beer style and each beer country, as well as the frequency that the user makes a review in each of these categories. Therefore, different variables can be generated for each user, regarding statistical metrics of both the *frequency* and *scores* of his/her reviews history, being related to its personal preferences in therms of beer style and country of origin.
Then, using appropriate statistical tests, the relationship of these generated markers for individual preferences can be tested against other variables of interest. For example, to test whether individuals prefer beers from their own country, we can perform a statistical test between the individuals' metrics of "favorite beer country" against the individuals' own country of origin, to identify possible correlations not explainable by the null hypothesis.
Finally, here we want to investigate whether the individuals' reviews of beers are affected by possible confounding factors, such as, whether there are reviewers in locations with limited access of various beer types/origins, which could possible present a "distorted" view on the individual's preferences. Here, a initial ideia is to compare the different metrics against themselves. E.g. to answer the question: *"Do individuals prefer beers from their own country because these are the ones they have access to?* , we can confront the origin of the beers which are most frequently tasted by the given individual with the origin of the beers which are most highly rated by the same individual. If they are not equal, this could indicate that the meaningfull aswer to the question above would be *"no"*.

### Analysis of beer attributes

### Recommendation system


## Organization within the team
The organization of the research questions througout the project was made in such a way to minimize the interferance between self contained topics, while connecting in a cohesive datastory. For this reason, the topics of research are divided among the indivuduals of the group in the following form:

1. Worldwide trends:
2. Analysis of user's preferences: Gabriel
3. Analysis of beer attributes:
4. Recommendation system:

## Proposed timeline
Considering the starting date of the P3 phase as the of the P2 deadline, there are 5 weeks to be planed, which can be divided as follows:

1. Dataset merging, cleaning and preparation: week 1
2. Data analysis, target at answering the research questions from each topic, as well as generation of plots and images: week 2 and 3
3. Writting of the conclusions in the form of a datastory? week 4
4. Migration of the results and written text to a visualization platform and final review of the complete datastory: week 5  