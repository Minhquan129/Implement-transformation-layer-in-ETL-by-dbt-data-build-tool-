devices_schema = """
    device_id INT NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    velocity FLOAT,
    speed FLOAT,
    temperature FLOAT,
    pressure FLOAT,
    humidity FLOAT
"""

yellow_taxi_schema = """
    VendorID INT NOT NULL,
    tpep_pickup_datetime TIMESTAMP NOT NULL,
    tpep_dropoff_datetime TIMESTAMP NOT NULL,
    passenger_count FLOAT,
    trip_distance FLOAT,
    RatecodeID FLOAT,
    store_and_fwd_flag CHAR(1),
    PULocationID INT,
    DOLocationID INT,
    payment_type INT,
    fare_amount FLOAT,
    extra FLOAT,
    mta_tax FLOAT,
    tip_amount FLOAT,
    tolls_amount FLOAT,
    improvement_surcharge FLOAT,
    total_amount FLOAT,
    congestion_surcharge FLOAT,
    airport_fee FLOAT
"""
