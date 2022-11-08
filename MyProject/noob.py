#! /usr/bin/env python3

import csv
import pandas as pd


writer = csv.writer(open('oops.csv', 'w', newline=''), delimiter=',')


def test_clueless():
    writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def test_spam():
    df = pd.read_csv('oops.csv')
    print(df)
    print(dir(writer))


def main():
    test_clueless()
    test_spam()


if __name__ == "__main__":
    main()
