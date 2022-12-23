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

This is a general trend though, when divided by country it changes a lot:

![Beer appreciation is culturally dependent, but mine's best](/adapassets/correlations.png)

Palate and taste clearly come out ahead(it'd be clearer if we kept the same x-axis scale everywhere) But even then, that swings rather wildly and we're likely to see this variability pop up again if we divide countries in demographic/cultural subgroups, but we'll just assume your contry of origin predict exactly how you like your beer.

### Beercommendation system

After doing all our analysis the goal would be to implement a recommender system to conclude our story.

Well, what are you doing here?

It's in the notebook, go play with it, it was a lot of work.
### Conclusion

~~Cider tastes better actually~~

### Special thanks

We would especially like to thank for their contribution:

-[Ninkasi](https://en.wikipedia.org/wiki/Ninkasi) for giving us beer during the making of man.

-Robert west for giving us a chance to work on such a "unique" dataset.

-Budweiser for reminding us that anything can be beer if we believe hard enough. 
