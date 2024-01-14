# This file contains the code to read the data from the source and split the data into train and test data
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

"""Initialize the data ingestion configuration"""
@dataclass
class DataIngestionConfig:
    train_data_path =  os.path.join("artifacts", "data", "train.csv")
    test_data_path = os.path.join("artifacts", "data", "test.csv")
    raw_data_path = os.path.join("artifacts", "data", "raw_data.csv")


"""Create a data ingestion class to read the data from the source and 
split the data into train and test data"""
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")
        try:
            # Read the raw data from the source
            df = pd.read_csv(os.path.join("notebooks/data", "gemstone.csv"))
            logging.info("Data read from the source successfully")
            
            # Create the artifacts folder if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save the train and test data into the artifacts folder
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Data saved into the artifacts folder successfully")
            
            # Split the data into train and test data
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=0)
            logging.info("Data split into train and test data successfully")
            
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and Test data saved into the artifacts folder successfully")
            logging.info("Data ingestion completed successfully")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        
        except Exception as e:
            logging.error("Error while initiating data ingestion")
            raise CustomException("Error while initiating data ingestion", e)
        