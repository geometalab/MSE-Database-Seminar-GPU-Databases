import glob, os
import argparse
import pyarrow as pa
import pandas as pd
from pymapd import connect


def run(args):
    connection = connect(user=args.user, password=args.password, host=args.host, dbname=args.dbname)
    print(connection.get_tables(), len(connection.get_tables()))
    import_data(connection=connection, directory=args.source)


def import_data(connection, directory):
    df = pd.DataFrame(
        {"VendorID": [2], "lpep_pickup_datetime": ["2014-06-01 00:00:00"],
         "Lpep_dropoff_datetime": ["2014-06-01 07:40:36"],
         "Store_and_fwd_flag": ["N"],
         "RateCodeID": [1], "Pickup_longitude": [0], "Pickup_latitude": [0], "Dropoff_longitude": [-73.865570068359375],
         "Dropoff_latitude": [40.770862579345703], "Passenger_count": [1], "Trip_distance": [8.00],
         "Fare_amount": [24.5],
         "Extra": [0], "MTA_tax": [0.5], "Tip_amount": [0], "Tolls_amount": [7.5], "Ehail_fee": [0],
         "Total_amount": [32.5],
         "Payment_type": [1], "Trip_type": [1]})

    os.chdir(directory)
    # for file in glob.glob("green_*.csv"):
    for file in glob.glob("green_tripdata_2014-06.csv"):
        # df = pd.read_csv(file)
        df['cab_type_id'] = 2
        df = df[['cab_type_id', 'Passenger_count', 'lpep_pickup_datetime', 'Lpep_dropoff_datetime', 'Pickup_longitude',
                 'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude', 'Trip_distance', 'Fare_amount',
                 'Total_amount']]
        df = df.rename(columns={'lpep_pickup_datetime': 'pickup_datetime', 'Lpep_dropoff_datetime': 'dropoff_datetime',
                                'Passenger_count': 'passenger_count', 'Pickup_longitude': 'pickup_longitude',
                                'Pickup_latitude': 'pickup_latitude', 'Dropoff_longitude': 'dropoff_longitude',
                                'Dropoff_latitude': 'dropoff_latitude', 'Trip_distance': 'trip_distance',
                                'Fare_amount': 'fare_amount', 'Total_amount': 'total_amount'})
        df[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'trip_distance',
            'fare_amount', 'total_amount']] = df[
            ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'trip_distance',
             'fare_amount', 'total_amount']].astype(float)
        df[['pickup_datetime', 'dropoff_datetime']] = df[['pickup_datetime', 'dropoff_datetime']].astype(
            'datetime64[ns]')
        df = df.drop('pickup_datetime', 1)
        df = df.drop('dropoff_datetime', 1)
        df = df.fillna(0.0)
        print('Number of dataframe columns:', len(df.columns))
        print(df.dtypes)
        print(df)
        # table = pa.Table.from_pandas(df)
        # connection.load_table_arrow("trips", table)
        connection.load_table("trips", df)


def main_function():
    parser = argparse.ArgumentParser(description='Import NYC Taxi data into MapD', )
    parser.add_argument('-p', '--password', dest='password', help='MapD password')
    parser.add_argument('-u', '--user', dest='user', help='MapD user')
    parser.add_argument('-d', '--database', dest='dbname', help='MapD database')
    parser.add_argument('-l', '--host', dest='host', help='MapD host')
    parser.add_argument('-s', '--source', dest='source', help='Data directory')
    parser.set_defaults(user="mapd", password="HyperInteractive", host="localhost", dbname="mapd",
                        source="/data/dbseminar/nyc-taxi-data/data/")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main_function()
