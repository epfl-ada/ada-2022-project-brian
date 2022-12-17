import pandas as pd
import numpy as np
import json
import math

##################################################
############## NECESSARY VALUES ##################

REVIEWS_FILE = '../datasets/BeerAdvocate/reviews_sample.txt' # replace this is the location of the complete reviews.txt in your computer (not in Github)

REQUESTED_FIELDS = ['user_id', 'style', 'brewery_id', 'beer_id', 'rating']

FILE_TO_CREATE = f'part_2_BeerAdvocate.json'

NUMBER_OF_PARTS = 3

##################################################
##################################################

def get_ratings_json(reviews_file:str, requested_fields:list, terminator:list):
    start, end = terminator
    line_index = 0
    with open(reviews_file, 'r', encoding="utf8") as r_file:
        reviews_list = []
        parsed_dict = {}
        for line in r_file:
            if line_index >= start and line_index <= end:
                field = line.split(':')[0].strip()
                if field in requested_fields:
                    parsed_dict[field] = line.split(':')[1].strip()
                    continue
                elif line == '\n':
                    reviews_list.append(parsed_dict)
                    parsed_dict = {}
            line_index += 1
    return reviews_list

def count_lines(file):
    def blocks(files, size=65536):
        while True:
            b = files.read(size)
            if not b: break
            yield b

    with open(file, "r", encoding="utf-8", errors='ignore') as f:
        return sum(bl.count("\n") for bl in blocks(f))

def get_block_terminators(numlines, numparts):
    div = math.floor(numlines/numparts)
    terminators_list = []
    for i in range(numparts):
        start = i * div
        if i == (numparts - 1):
            end = numlines - 1
        else: 
            end = ((i+1) * div ) - 1
        terminators_list.append([start, end])
    return terminators_list


print(f'Reading reviews file: {REVIEWS_FILE}')
print(f'and parsing the following fields: {REQUESTED_FIELDS}')
print()
print('...')
print(f'After that, results will be written to: n_{FILE_TO_CREATE} (where n is the number of parts)')

numlines = count_lines(file=REVIEWS_FILE)
block_terminators = get_block_terminators(numlines, NUMBER_OF_PARTS)

for n, terminator in enumerate(block_terminators):

    data = get_ratings_json(reviews_file=REVIEWS_FILE, requested_fields=REQUESTED_FIELDS, terminator=terminator)

    with open(f'{n}_{FILE_TO_CREATE}', 'w') as fp:
        json.dump(data, fp)