import pandas as pd

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
