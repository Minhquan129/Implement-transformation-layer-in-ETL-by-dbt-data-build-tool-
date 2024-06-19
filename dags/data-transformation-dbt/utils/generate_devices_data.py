import argparse
import os
import random
from datetime import datetime

import pandas as pd

# Define features to generate in random
FEATURES = ["velocity", "speed", "temperature", "pressure", "humidity"]


def main(args):
    data = []

    for _ in range(args.num_records):
        record = {}
        record["device_id"] = random.randint(0, args.num_devices)
        record["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for feature in FEATURES:
            record[feature] = random.random()

        data.append(record)

    data = pd.DataFrame(data, columns=["device_id", "updated_at"] + FEATURES)

    # Save the data in parquet format
    data.to_parquet(os.path.join(args.output, "data.parquet"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--output",
        default="./data",
        help="Directory to save the data file in parquet format.",
    )
    parser.add_argument(
        "-n",
        "--num_devices",
        default=10,
        type=int,
        help="Number of IoT devices in the database.",
    )
    parser.add_argument(
        "-r",
        "--num_records",
        default=10000,
        type=int,
        help="Number of records in the database.",
    )
    args = parser.parse_args()
    main(args)
