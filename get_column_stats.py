import sys
import math
import argparse


def initialize():
    """Initialize the code by taking arguments from the command line

    Parameters
    ----------
    There are no parameters passed to this function

    Returns
    -------
    args : type: argparse namespace

    """
    parser = argparse.ArgumentParser(
        description=' This program takes an input file and column number from '
                    'the user and returns the mean and standard deviation of '
                    'the numbers in that column.',
        prog='get_column_stats'
    )

    parser.add_argument('-f',
                        '--file_name',
                        type=str,
                        help='The file name of the input file, which should be'
                        ' a tab-separated file of integers.',
                        required=True)

    parser.add_argument('-c',
                        '--column_number',
                        type=str,
                        help='The column number',
                        required=True)

    args = parser.parse_args()

    return args


def column_stats(data):
    """Returns the mean and the standard deviation given a list of data.

    Parameters
    ----------
    data : list
        The list of data

    Returns
    -------
    mean : float
        The mean of the given list of data
    std : float
        The standard deviation of the given list of data

    """
    mean = sum(data)/len(data)
    std = math.sqrt(sum([(mean-x)**2 for x in data]) / len(data))

    return mean, std


def main():
    args = initialize()

    file_name = args.file_name

    # Make sure that the column number is an integer
    col_num = None
    try:
        col_num = int(args.column_number)
    except ValueError:
        print('The column number should be an integer.')
        sys.exit(1)

    # Open the file if it can be opened, or raise an error.
    f = None
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('The file', file_name, 'does not exist.')
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    # Make sure that the column number is an integer
    col = None
    try:
        col = int(args.column_number)
    except ValueError:
        print('The column number should be an integer.')
        sys.exit(1)

    # Create a list of data and check if the column number is valid
    V = []

    for l in f:
        A = [int(x) for x in l.split()]
        try:
            V.append(A[col_num])
        except IndexError:
            print('The column number is not valid.')
            sys.exit(1)

    [mean, std] = column_stats(V)

    print('mean:', mean)
    print('stdev:', std)


if __name__ == '__main__':
    main()
