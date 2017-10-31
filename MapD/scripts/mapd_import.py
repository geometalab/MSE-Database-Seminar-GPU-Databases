import os
import glob
import argparse
import pandas as pd
import csv
import numpy as np


def run(args):
    os.chdir(args.source)
    for file in glob.glob("green.csv"):
        # for file in glob.glob("green_tripdata_2014-06.csv"):
        # for file in glob.glob("green_*.csv"):
        df = pd.read_csv(file, usecols=range(0, 19),names=['VendorID','lpep_pickup_datetime','Lpep_dropoff_datetime','Store_and_fwd_flag','RateCodeID','Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude','Passenger_count','Trip_distance','Fare_amount','Extra','MTA_tax','Tip_amount','Tolls_amount','Ehail_fee','Total_amount','Payment_type','Trip_type'])
        df = rename_green(file)

        df = df.fillna(0.0)
        print(list(df.columns.values))
        print(df['pickup_datetime'])
        '''
        os.chdir(args.source)
        filename = 'tmp.csv'
        df.to_csv(filename, encoding='utf-8', index=False)
        command = r"""echo "COPY {0} FROM '{1}{2}'  WITH (header='true');" | /mapd/bin/mapdql mapd -u {3} -p {4}"""
        command = command.format('trips', args.source, filename, args.user, args.password)
        os.system(command)
        '''


def rename_green(file):
    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    cols = ['Passenger_count', 'lpep_pickup_datetime', 'Lpep_dropoff_datetime', 'Pickup_longitude',
            'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude', 'Trip_distance', 'Fare_amount', 'Total_amount']
    #  'Total_amount']
    df = pd.read_csv(file, date_parser=dateparse, parse_dates=['lpep_pickup_datetime', 'Lpep_dropoff_datetime'], header=0, index_col=None, usecols=cols)
    # df = pd.read_csv(file, comment=' ')
    # df['cab_type_id'] = 2

    print(df['lpep_pickup_datetime'])
    # df = df[['cab_type_id', 'Passenger_count', 'lpep_pickup_datetime', 'Lpep_dropoff_datetime', 'Pickup_longitude',
    #         'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude', 'Trip_distance', 'Fare_amount',
    #         'Total_amount']]
    df = df.rename(columns={'lpep_pickup_datetime': 'pickup_datetime', 'Lpep_dropoff_datetime': 'dropoff_datetime',
                            'Passenger_count': 'passenger_count', 'Pickup_longitude': 'pickup_longitude',
                            'Pickup_latitude': 'pickup_latitude', 'Dropoff_longitude': 'dropoff_longitude',
                            'Dropoff_latitude': 'dropoff_latitude', 'Trip_distance': 'trip_distance',
                            'Fare_amount': 'fare_amount', 'Total_amount': 'total_amount'})
    # df[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'trip_distance',
    #    'fare_amount', 'total_amount']] = df[
    #    ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'trip_distance',
    #     'fare_amount', 'total_amount']].astype(float)
    # df[['pickup_datetime', 'dropoff_datetime']] = df[['pickup_datetime', 'dropoff_datetime']].astype(
    #    'datetime64[ns]')
    return df[
        ['cab_type_id', 'passenger_count', 'pickup_datetime', 'dropoff_datetime', 'pickup_longitude', 'pickup_latitude',
         'dropoff_longitude', 'dropoff_latitude', 'trip_distance', 'fare_amount', 'total_amount']]


def main_function():
    parser = argparse.ArgumentParser(description='Import NYC Taxi data into MapD', )
    parser.add_argument('-p', '--password', dest='password', help='MapD password')
    parser.add_argument('-u', '--user', dest='user', help='MapD user')
    parser.add_argument('-d', '--database', dest='dbname', help='MapD database')
    parser.add_argument('-l', '--host', dest='host', help='MapD host')
    parser.add_argument('-s', '--source', dest='source', help='Data directory')
    parser.set_defaults(user="mapd", password="HyperInteractive", host="localhost", dbname="mapd",
                        source="/data/nyc-taxi-data/data/")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main_function()
