import subprocess as sub
import pandas as pd
import sys
import time
import os
import io
import os.path
import datetime


def tace_execution(execution_path, i, query, date_start, process):
    '''
    Method to profile the execution of our scraper and the output.
    :param execution_path:
    :param i: page number
    :param query: query we are looking at
    :param date_start: when the instance of the scraper was started
    :param process: process number
    '''
    query_searching = 'We are collecting data for : %s' % (' '.join(query))
    begining = 'The data collection started at %s' % date_start
    process_tracing = 'We successfully finished process: %s' % str(process)
    number_of_pages = 'We are in page: %s' % i
    with open('%s\\trace_execution_%s.txt' % (execution_path, i), 'w') as file:
        file.write('{1}{0}{2}{0}{3}{0}{4}'.format(
            '\n', query_searching, begining, process_tracing, number_of_pages))
    file.close()


def main():
    current_path = os.getcwd()
    log_filePath = '%s\\log_files' % current_path
    execution_path = '%s\\execution_files' % current_path
    os.makedirs(log_filePath, exist_ok=True)
    os.makedirs(execution_path, exist_ok=True)
    publication = pd.read_excel('publication.xlsx')  # You might want to specify the name of the publication
    argument_list = publication.values.tolist()
    i = 1
    for elem in argument_list:
        date_start = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time_start = time.time()
        file_name = '%s\\log_%s.txt' % (log_filePath, i)
        with io.open(file_name, 'w') as writer:
            process = sub.Popen([sys.executable, 'get_proquest.py'] +
                                elem, stdout=writer, stderr=sub.STDOUT, bufsize=1, universal_newlines=True, shell=True)
        writer.close()
        process.wait()
        tace_execution(execution_path, i, elem, date_start, process)
        i += 1
        time.sleep(10)
        process.kill()


if __name__ == '__main__':
    main()
