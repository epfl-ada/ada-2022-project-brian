# On the quest for beerfection

## Alestract:
Our goal is to determine objetively the completely bias-proof question of which beer tastes best. One of the central topics revolves around detecting different trends in preferences and possible biases from beer consumers in different regions, as everyone but us is clearly compromised. Finally, we'll provide you with the best beer ever, for everyone, no matter their "individual tastes".

## Methods

We use SVD for the recommendation system, otherwise we rely on basic extraction and visualisation techniques, the dataset being rich enough for us to not need more complex mathematics.

### It's a lager world out there

So, first off, on top of all the reviews being written by biased folk, there's participation bias too, which is bad.

![Internet and beer access rarely match](/adapassets/brewerybycountries.png)

As we can see, some very internat starved countries have a lot of reviews, and others have the opposite problem, we also notice that the US scores top in both.

### Everyone is steeping but me
Here, firstly, some metrics will be put in place in order to relate the users' reviews history with their personal preferences regarding beer style and/or beer country. They are initially thought to be intimately related to the scores the user gives on average for each beer style and each beer country, as well as the frequency that the user makes a review in each of these categories. Therefore, different variables can be generated for each user, regarding statistical metrics of both the *frequency* and *scores* of his/her reviews history, being related to its personal preferences in terms of beer style and country of origin.
Then, using appropriate statistical tests, the relationship of these generated markers for individual preferences can be tested against other variables of interest. For example, to test whether individuals prefer beers from their own country, we can perform a statistical test between the individuals' metrics of "favorite beer country" against the individuals' own country of origin, to identify possible correlations not explainable by the null hypothesis.
Finally, here we want to investigate whether the individuals' reviews of beers are affected by possible confounding factors, such as, whether there are reviewers in locations with limited access of various beer types/origins, which could possibly present a "distorted" view on the individual's preferences. Here, an initial idea is to compare the different metrics against themselves. E.g. to answer the question: *"Do individuals prefer beers from their own country because these are the ones they have access to?"*, we can confront the origin of the beers which are most frequently tested by the given individual with the origin of the beers which are most highly rated by the same individual. If they are not equal, this could indicate that the meaningful answer to the question above would be *"no"*.

### Fermenting attributes

The data provided by one of the beer reviews website offers individual ratings for each of the following beer attribute: appearance, aroma, palate, taste. What we want to do here is to analyse if any of these attributes has a particularly stronger influence over the rating of the beer, and whether it varies over beer style or country. Here we must differentiate the overall rating which for the two dataset is the calculated based on the different attribute rating and the finale rating which is a rating of the beer provided by the user independently from all the other attributes rating. This why it is intersting to investigate the relation between the attribute rating and the final rating.

In the notebook linear regression was made where teh four attributes are the features and the final rating is the outcome. We can see that a correlation exists for the general case (i.e. comparing all the beer styles and ratings). Analysis over a beer style basis also show a correlation and we can divide beer style to diffrent group. Finally analysis according the country/region of origin of the reviewer show a correlation and some insight was made concerning particular country.

Indeed by analysing the coefficient of the regression anylsis of each attributes (i.e, beer attributes) and ploting it we can gain some insight regarding the impact of this correlation.

### Beercommendation system

After doing all our analysis the goal would be to implement a recommender system to conclude our story.

What is even a recommender system ?

According to Wikipedia : "A recommender system, or a recommendation system (sometimes replacing 'system' with a synonym such as platform or engine), is a subclass of information filtering system that provide suggestions for items that are most pertinent to a particular user." https://en.wikipedia.org/wiki/Recommender_system

So the goal is here would be to recommend a beer for a user giving his past review, i.e., his "taste".

Singular Value Decomposition (SVD) is a matrix factorization technique that is often used in the field of recommendation systems to predict the ratings that users would give to items they have not yet rated.

In collaborative filtering, we try to predict the ratings that a user would give to an item based on the ratings that similar users have given to that item. One way to do this is to use SVD to decompose the ratings matrix into the product of three matrices: a user matrix, a singular matrix, and an item matrix.

The user matrix and the item matrix both contain latent factors that represent the preferences of the users and the characteristics of the items, respectively. These latent factors are derived from the ratings matrix through the SVD process.

To make a prediction for a given user and item, we can take the dot product of the latent factors for that user and item. This dot product gives us a predicted rating for the user-item pair.

The SVD method can be used to handle missing values in the ratings matrix, which is common in real-world recommendation systems where many users have not rated many items. By decomposing the ratings matrix into latent factors, we can fill in the missing values and make predictions for all the user-item pairs, even those that have not been rated.

### Conclusion

~~Cider tastes better actually~~

### Special thanks

We would especially like to thank for their contribution:

-[Ninkasi](https://en.wikipedia.org/wiki/Ninkasi) for giving us beer during the making of man.

-Robert west for giving us a chance to work on such a "unique" dataset.

-Budweiser for reminding us that anything can be beer if we believe hard enough. 
