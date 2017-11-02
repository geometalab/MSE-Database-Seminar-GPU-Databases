import os
import glob
import argparse
import pandas as pd


def run(args):
    os.chdir(args.source)
    #for file in glob.glob("green.csv"):
    for file in glob.glob("green_tripdata_2016-10.csv"):
        # for file in glob.glob("green_*.csv"):
        df = pd.read_csv(file,
                         names=['VendorID', 'lpep_pickup_datetime', 'Lpep_dropoff_datetime', 'Store_and_fwd_flag',
                                'RateCodeID', 'Pickup_longitude', 'Pickup_latitude', 'Dropoff_longitude',
                                'Dropoff_latitude', 'Passenger_count', 'Trip_distance', 'Fare_amount', 'Extra',
                                'MTA_tax', 'Tip_amount', 'Tolls_amount', 'Ehail_fee', 'Total_amount',
                                'Payment_type',
                                'Trip_type'])
        df = df.iloc[1:]
        df = rename_green(df)
        df = df.fillna(0.0)
        os.chdir(args.source)
        filename = 'tmp.csv'
        df.to_csv(filename, encoding='utf-8', index=False)
        command = r"""echo "COPY {0} FROM '{1}{2}'  WITH (header='true');" | /mapd/bin/mapdql mapd -u {3} -p {4}"""
        command = command.format('trips', args.source, filename, args.user, args.password)
        os.system(command)

def rename_green(df):
    df['cab_type_id'] = 2
    df = df.rename(columns={'lpep_pickup_datetime': 'pickup_datetime', 'Lpep_dropoff_datetime': 'dropoff_datetime',
                            'Passenger_count': 'passenger_count', 'Pickup_longitude': 'pickup_longitude',
                            'Pickup_latitude': 'pickup_latitude', 'Dropoff_longitude': 'dropoff_longitude',
                            'Dropoff_latitude': 'dropoff_latitude', 'Trip_distance': 'trip_distance',
                            'Fare_amount': 'fare_amount', 'Total_amount': 'total_amount'})
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
