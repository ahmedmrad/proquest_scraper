import pandas as pd


def create_df(path_toFiles, list_dict, publication, query, start_date, end_date):

'''
'''

    df = pd.DataFrame.from_dict(list_dict)
    df.to_csv('%s\\%s_%s_%s_%s.csv' %
              (path_toFiles, publication, query, start_date, end_date), index=False)
