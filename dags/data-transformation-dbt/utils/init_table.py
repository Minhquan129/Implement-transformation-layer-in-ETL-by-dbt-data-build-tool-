import argparse
import os

import dotenv
import pandas as pd
import psycopg2
import schemas
from sqlalchemy import create_engine

dotenv.load_dotenv()


def main(args):
    # Connect to the database
    conn = psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )
    cursor = conn.cursor()

    # Get table schema based on the table name
    if args.table_name == "devices":
        schema = schemas.yellow_taxi_schema
    else:
        raise ValueError("Invalid table name!")
    create_sql = f"""CREATE TABLE {args.table_name} (
        {schema}
    )"""

    # Create the table
    try:
        cursor.execute(create_sql)
        print(f"Table {args.table_name} has been created successfully!")
        conn.commit()
    except Exception as e:
        print(f"Creation failed with error: {e}")

    # Insert data read from a parquet file to table
    df = pd.read_parquet(args.input_file)
    engine = create_engine(
        "postgresql://{}:{}@{}:{}/{}".format(
            os.getenv("POSTGRES_USER"),
            os.getenv("POSTGRES_PASSWORD"),
            os.getenv("POSTGRES_HOST"),
            os.getenv("POSTGRES_PORT"),
            os.getenv("POSTGRES_DB"),
        )
    )
    try:
        df.to_sql(args.table_name, con=engine.connect(), if_exists="replace")
        print(f"Table {args.table_name} has been inserted successfully!")
    except Exception as e:
        print(f"Insertion failed with error {e}")

    # Closing the connection
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--table_name",
        default="devices",
        help="Table name of the generated data.",
    )
    parser.add_argument(
        "-i",
        "--input_file",
        default="./data/data.parquet",
        type=str,
        help="Path to the data file in parquet format.",
    )
    args = parser.parse_args()

    main(args)
