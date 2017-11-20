import os
import re
import glob
import argparse
import pandas as pd
import numpy as np

year_month_regex = "tripdata_([0-9]{4})-([0-9]{2})"


def run(args):
    os.chdir(args.source)
    for file in glob.glob("*.csv"):
        match = re.findall(year_month_regex, file)
        year = int(match[0][0])
        month = int(match[0][1])
        cab_type = 2

        if "green" in file:
            if year < 2015:
                schema = green_schema_pre_2015
            elif year == 2015 and month < 7:
                schema = green_schema_2015_h1
            elif year == 2015 or (year == 2016 and month < 7):
                schema = green_schema_2015_h2_2016_h1
            else:
                schema = green_schema_2016_h2
            execute_command(file, schema, cab_type, args)
        elif "yellow" in file:
            cab_type = 1
            if year < 2015:
                schema = yellow_schema_pre_2015
            elif year == 2015 or (year == 2016 and month < 7):
                schema = yellow_schema_2015_2016_h1
            else:
                schema = yellow_schema_2016_h2
            execute_command(file, schema, cab_type, args)


def execute_command(file, schema, cab_type, args):
    df = pd.read_csv(file, names=schema)
    df = df.iloc[1:]
    df = rename_columns(df, cab_type=cab_type)
    df = df.fillna(0.0)
    tmp_filename = 'tmp.csv'
    df.to_csv(tmp_filename, encoding='utf-8', index=False)
    command = r"""echo "COPY {0} FROM '{1}{2}'  WITH (header='true');" | /mapd/bin/mapdql mapd -u {3} -p {4}"""
    command = command.format('trips', args.source, tmp_filename, args.user, args.password)
    os.system(command)
    os.remove(tmp_filename)


def rename_columns(df, cab_type=2):
    df['cab_type_id'] = cab_type
    df = add_non_existing_columns(df)
    df = df.rename(columns={'lpep_pickup_datetime': 'pickup_datetime', 'lpep_dropoff_datetime': 'dropoff_datetime',
                            'tpep_pickup_datetime': 'pickup_datetime', 'tpep_dropoff_datetime': 'dropoff_datetime'})
    return df[
        ['cab_type_id', 'passenger_count', 'pickup_datetime', 'dropoff_datetime', 'pickup_longitude', 'pickup_latitude',
         'dropoff_longitude', 'dropoff_latitude', 'trip_distance', 'fare_amount', 'total_amount']]


def add_non_existing_columns(df):
    if 'pickup_longitude' not in df:
        df["pickup_longitude"] = np.nan
    if 'pickup_latitude' not in df:
        df["pickup_latitude"] = np.nan
    if 'pickup_longitude' not in df:
        df["pickup_longitude"] = np.nan
    if 'dropoff_longitude' not in df:
        df["dropoff_longitude"] = np.nan
    if 'dropoff_latitude' not in df:
        df["dropoff_latitude"] = np.nan
    return df


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


green_schema_pre_2015 = ['vendor_id', 'lpep_pickup_datetime', 'lpep_dropoff_datetime',
                         'store_and_fwd_flag,rate_code_id', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
                         'dropoff_latitude', 'passenger_count', 'trip_distance', 'fare_amount', 'extra', 'mta_tax',
                         'tip_amount', 'tolls_amount', 'ehail_fee', 'total_amount', 'payment_type', 'trip_type',
                         'junk1', 'junk2']
green_schema_2015_h1 = ['vendor_id', 'lpep_pickup_datetime', 'lpep_dropoff_datetime', 'store_and_fwd_flag',
                        'rate_code_id', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude',
                        'passenger_count', 'trip_distance', 'fare_amount', 'extra', 'mta_tax,tip_amount',
                        'tolls_amount,ehail_fee', 'improvement_surcharge', 'total_amount', 'payment_type', 'trip_type',
                        'junk1', 'junk2']

green_schema_2015_h2_2016_h1 = ['vendor_id', 'lpep_pickup_datetime', 'lpep_dropoff_datetime', 'store_and_fwd_flag',
                                'rate_code_id', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
                                'dropoff_latitude', 'passenger_count', 'trip_distance', 'fare_amount', 'extra,mta_tax',
                                'tip_amount', 'tolls_amount', 'ehail_fee', 'improvement_surcharge', 'total_amount',
                                'payment_type', 'trip_type']

green_schema_2016_h2 = ['vendor_id', 'lpep_pickup_datetime', 'lpep_dropoff_datetime', 'store_and_fwd_flag',
                        'rate_code_id', 'pickup_location_id', 'dropoff_location_id', 'passenger_count', 'trip_distance',
                        'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'ehail_fee',
                        'improvement_surcharge', 'total_amount', 'payment_type', 'trip_type', 'junk1', 'junk2']

yellow_schema_pre_2015 = ['vendor_id', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count',
                          'trip_distance', 'pickup_longitude', 'pickup_latitude', 'rate_code_id', 'store_and_fwd_flag',
                          'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount', 'extra,mta_tax',
                          'tip_amount', 'tolls_amount', 'total_amount']

yellow_schema_2015_2016_h1 = ['vendor_id', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count',
                              'trip_distance', 'pickup_longitude', 'pickup_latitude', 'rate_code_id',
                              'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude', 'payment_type',
                              'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
                              'total_amount']

yellow_schema_2016_h2 = ['vendor_id', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count',
                         'trip_distance', 'rate_code_id', 'store_and_fwd_flag', 'pickup_location_id',
                         'dropoff_location_id', 'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount',
                         'tolls_amount', 'improvement_surcharge', 'total_amount', 'junk1', 'junk2']

if __name__ == "__main__":
    main_function()
