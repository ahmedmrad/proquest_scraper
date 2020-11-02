import pandas as pd


def create_df(path_toFiles, list_dict, publication, query, start_date, end_date):
    '''
    generate dataframes
    :param path_toFiles:
    :param list_dict:
    :param publication: name of publication
    :param query: element to look for
    :param start_date: start date of the query
    :param end_date: end date of the query
    '''
    df = pd.DataFrame.from_dict(list_dict)
    df.to_csv('%s\\%s_%s_%s_%s.csv' %
              (path_toFiles, publication, query, start_date, end_date), index=False)
