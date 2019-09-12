#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Testing for PEP8 coding style
run pep8_style_test pycodestyle style.py
assert_no_stdout
run pep8_get_column_stats pycodestyle get_column_stats.py
assert_no_stdout

# Test if get_column_stats.py works properly with random numbers
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run column_stats_random_test python get_column_stats.py -f data.txt -c 2
assert_stdout
assert_exit_code 0
assert_in_stdout "mean:"
assert_in_stdout "stdev:"
assert_no_stderr

# Test if get_column_stats.py works properly (compare to known expected behavior)
for i in `seq 1 20`;
do
    V=$i;
    (for j in `seq 1 100`; do 
        echo -e "$V\t$V\t$V\t$V\t$V";
    done )> data.txt
    run column_stats_test python get_column_stats.py -f data.txt --c 2
    assert_stdout
    assert_exit_code 0
    assert_in_stdout mean: $V.0\nstdev: 0.0
done

# Test if the exceptions handling in get_column_stats.py works properly
run invalid_file_test python get_column_stats.py -f data1.txt -c 2
assert_in_stdout "does not exist."
assert_exit_code 1

run invalid_column_type python get_column_stats.py -f data.txt -c "test"
assert_in_stdout "The column number should be an integer."
assert_exit_code 1

run invalide_column_index python get_column_stats.py -f data.txt -c 8
assert_in_stdout "The column number is not valid."
assert_exit_code 1

