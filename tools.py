import pandas as pd
import numpy as np
from datetime import datetime



def transform_values(df):
    try:
        df['user_id'] = df['user_id'].astype(int)
    except:
        df['user_id'] = df['user_id'].apply(lambda x: x.strip())

    for field in ['beer_name', 'brewery_name', 'style']:
        df[field] = df[field].apply(lambda x: x.strip())
    for column_name in ['brewery_id', 'beer_id']:
        df[column_name] = df[column_name].astype(int)
    for column_name in ['abv', 'appearance', 'aroma', 'palate', 'taste', 'overall', 'rating']:
        df[column_name] = df[column_name].astype(float)
    df['review'] = df['review'].astype(bool)

    df['date'] = df['date'].apply(lambda x: datetime.fromtimestamp(int(x)))
    return df

def read_reviews_file(file_path):

    def parse_dict(lines):
        result = {}
        for line in lines:
            key, value = line.split(':', 1)
            value = value.split('\n')[0]
            result[key] = value
        return result


    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    blank_lines_indexes = [index for index, line in enumerate(lines) if line.isspace()]

    data = []
    begin_index = 0
    for end_index in blank_lines_indexes:
        result_dict = parse_dict(lines[begin_index:end_index])
        data.append(result_dict)
        begin_index = end_index + 1

    df = pd.DataFrame(data)
    
    if not 'review' in list(df.columns):
        df['review'] = df.text.apply(lambda x: True if x else False)

    return transform_values(df)