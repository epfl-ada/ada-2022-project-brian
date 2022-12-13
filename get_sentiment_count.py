import pandas as pd
import numpy as np
import requests
import string
import json
from langdetect import detect as lang_detect


positive_words = set(requests.get('https://ptrckprry.com/course/ssd/data/positive-words.txt').text.split('\n')[35:])
negative_words = set(requests.get('https://ptrckprry.com/course/ssd/data/negative-words.txt').text.split('\n')[35:])
punctuation_toberemoved = string.punctuation.translate({ord(i) : None for i in '+-'})

convertion_dict = {
    'virgin islands (british)' : {
        'country': 'england',
        'state': 'virgin islands'
    },
    'virgin islands (u.s.)' : {
        'country': 'united states',
        'state': 'virgin islands'
    },
    'utah' : {
        'country': 'united states',
        'state': 'utah'
    },
    'illinois' : {
        'country': 'united states',
        'state': 'illinois'
    },
    'new york' : {
        'country': 'united states',
        'state': 'new york'
    }
}
def get_state_str(x):
    if x in convertion_dict.keys():
        return convertion_dict[x]['state']
    splitted = str(x).lower().strip().split(',')
    if len(splitted) > 1:
        return splitted[-1]
    return np.nan

def get_country_str(x):
    if x in convertion_dict.keys():
        return convertion_dict[x]['country']
    return str(x).lower().strip().split(',')[0]

def remove_links(x:str):
    token = '</a>'
    if token in x:
        return x.split(token)[0]
    return x

def regularize_locations(df):
    df['state'] = df['location'].apply(lambda x: get_state_str(x))
    df['location'] = df['location'].apply(lambda x: get_country_str(remove_links(str(x))))
    return df

def sentiment_count(sentence, type):
    words = list(sentence.lower().translate(str.maketrans('', '', punctuation_toberemoved)).split(' '))
    if type == 'positive':
        return len([w for w in words if w in positive_words])
    elif type == 'negative':
        return len([w for w in words if w in negative_words])


def get_rating_text_with_list_of_dicts(file_path:str, user_list:set, breweries_list:set):
    rating = None
    text = ''
    user_in_list = False
    same_country = 0
    reviews_list = []
    with open(file_path, 'r', encoding="utf8") as r_file:
        for line in r_file:
            if line.split(':')[0] == 'user_id':
                if line.split(':')[1].strip() in user_list:
                    user_in_list = True
                    continue
            if line.split(':')[0] == 'brewery_id':
                if line.split(':')[1].strip() in breweries_list:
                    same_country = 1
                    continue
            if line.split(':')[0] == 'rating':
                rating = line.split(':')[1].strip()
                continue
            elif line.split(':')[0] == 'text':
                text = line.split(':')[1].strip()
                continue
            elif line == '\n':
                if rating and text and user_in_list:
                    d = {
                        'positive': sentiment_count(sentence=text, type='positive'),
                        'negative': sentiment_count(sentence=text, type='negative'),
                        'rating':rating,
                        'same_country': same_country
                    }
                    reviews_list.append(d)
                rating = None
                text = ''
                user_in_list = False
                same_country = 0
    return reviews_list

DATA_SOURCE = 'RateBeer'

reviews_file = f'/home/gabriel/OneDrive/Classes/ADA/Project-draft/datasets/{DATA_SOURCE}/reviews.txt'
users_file = f'/home/gabriel/OneDrive/Classes/ADA/Project-draft/datasets/{DATA_SOURCE}/users.csv'
breweries_file = f'/home/gabriel/OneDrive/Classes/ADA/Project-draft/datasets/{DATA_SOURCE}/breweries.csv'

df_users = regularize_locations(pd.read_csv(users_file))
df_users['user_id'] = df_users['user_id'].astype(str)
us_users = set(df_users[df_users.location == 'united states'].user_id)
print('Users file read')

df_breweries = regularize_locations(pd.read_csv(breweries_file))
df_breweries['id'] = df_breweries['id'].astype(str)
us_breweries = set(df_breweries[df_breweries.location == 'united states'].id)
print('Breweries file read')

print(f'Reading reviews file: {reviews_file}')

data = get_rating_text_with_list_of_dicts(file_path = reviews_file, user_list=us_users, breweries_list=us_breweries)

with open(f'datasets/sentiment_analysis/us_sentiment_count_{DATA_SOURCE}.json', 'w') as fp:
    json.dump(data, fp)