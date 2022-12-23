# On the quest for beerfection

## Alestract:
Our goal is to determine objetively the completely bias-proof question of which beer tastes best. One of the central topics revolves around detecting different trends in preferences and possible biases from beer consumers in different regions, as everyone but us is clearly compromised. Finally, we'll provide you with the best beer ever, for everyone, no matter their "individual tastes".

## Methods

We use SVD for the recommendation system, otherwise we rely on basic extraction and visualisation techniques, the dataset being rich enough for us to not need more complex mathematics.

### It's a lager world out there

So, first off, on top of all the reviews being written by biased folk, there's participation bias too, which is bad.

![Internet and beer access rarely match](/adapassets/brewerybycountries.png)

As we can see, some very internet starved countries have a lot of reviews, and others have the opposite problem, we also notice that the US scores top in both. Oh well, at least breweries randomly distributed their beers, otherwise we'd be in trouble.

![Number of beers doesn't correlate to anything](/adapassets/beersperbrewery.png)

Anyways, we've looked at the planet and we see that a lot of people think a lot of things, now let's be judgy about individual biases.

### Everyone is steeping but me

So, let's keep going with the lighthearted theme of jingoism!

![People like whatever beer's at home](/adapassets/jingoism.png)

As you can hardly see on that graph, the average beer reviewer has some light nationalistic tendencies, as such the dataset is completely corrupted by 20th century propaganda,but since we all are we can simply chug along and pretend this is normal.

### Fermenting attributes

With a bit of malt, linear regression, water, and dataframes we can extract the correlation between individual attribute rating and total ratings:

![If beer tastes better it tastes better, whodathunkit](/adapassets/correlations.png)

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
