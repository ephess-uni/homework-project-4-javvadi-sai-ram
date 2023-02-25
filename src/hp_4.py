# hp_4.py
#
from datetime import datetime, timedelta
from csv import DictReader, DictWriter
from collections import defaultdict


def reformat_dates(old_dates):
    list_of_date=[]

    for each in old_dates:
        list_of_date.append(datetime.strptime(each,"%Y-%m-%d").strftime("%d,%b,%Y"))
    return list_of_date


def date_range(start, n):
    if not isinstance(start,str):
        raise TypeError
    elif not isinstance(n,int):
        raise TypeError
    else:
        list_of_date=[]
        for index in range(n):
            list_of_date.append(datetime.strptime(start,"%Y-%m-%d")  + timedelta(days=index))
            return list_of_date

def add_date_range(values, start_date):
    list_of_date=[]

    for index,value in enumerate(values):
        list_of_date.append(datetime.strptime(start_date,"%Y-%m-%d")  + timedelta(days=i))
        return list(zip(list_of_date,values))

        
def fees_report(infile, outfile):
    """Calculates late fees per patron id and writes a summary report to
    outfile."""
    pass


# The following main selection block will only run when you choose
# "Run -> Module" in IDLE.  Use this section to run test code.  The
# template code below tests the fees_report function.
#
# Use the get_data_file_path function to get the full path of any file
# under the data directory.

if __name__ == '__main__':
    
    try:
        from src.util import get_data_file_path
    except ImportError:
        from util import get_data_file_path

    # BOOK_RETURNS_PATH = get_data_file_path('book_returns.csv')
    BOOK_RETURNS_PATH = get_data_file_path('book_returns_short.csv')

    OUTFILE = 'book_fees.csv'

    fees_report(BOOK_RETURNS_PATH, OUTFILE)

    # Print the data written to the outfile
    with open(OUTFILE) as f:
        print(f.read())
