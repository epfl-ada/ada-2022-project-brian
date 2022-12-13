import pandas as pd
import numpy as np
import json

##################################################
############## NECESSARY VALUES ##################

REVIEWS_FILE = '../reviews_files/BeerAdvocate/reviews.txt' # this is not in the GitHub repository: the file is too large

REQUESTED_FIELDS = ['user_id', 'style', 'brewery_id', 'beer_id', 'rating']

FILE_TO_CREATE = f'part_2_BeerAdvocate.json'

##################################################
##################################################

def get_ratings_json(reviews_file:str, requested_fields:list):
    with open(reviews_file, 'r', encoding="utf8") as r_file:
        reviews_list = []
        parsed_dict = {}
        for line in r_file:
            field = line.split(':')[0].strip()
            if field in requested_fields:
                parsed_dict[field] = line.split(':')[1].strip()
                continue
            elif line == '\n':
                reviews_list.append(parsed_dict)
                parsed_dict = {}
    return reviews_list


print(f'Reading reviews file: {REVIEWS_FILE}')
print(f'and parsing the following fields: {REQUESTED_FIELDS}')
print('...')
print(f'After that, results will be written to: {FILE_TO_CREATE}')

data = get_ratings_json(reviews_file=REVIEWS_FILE, requested_fields=REQUESTED_FIELDS)

with open(FILE_TO_CREATE, 'w') as fp:
    json.dump(data, fp)