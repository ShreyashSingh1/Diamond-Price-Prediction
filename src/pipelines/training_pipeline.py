import sys
import os
from src.components import data_transformation
from src.exception import CustomException
from src.logger import logging
import pandas as pd  
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
        # Create an instance of DataIngestion class
        data_ingestion = DataIngestion()
        data_transform = DataTransformation()
        
        # Call the initiate_data_ingestion method
        train_data_path, test_data_path, raw_data_path = data_ingestion.initiate_data_ingestion()
        print(train_data_path, test_data_path, raw_data_path)

        tarin_data, test_data, _  = data_transform.initiate_data_transformation(train_data_path, test_data_path)

        model_trainer = ModelTrainer()
        model_trainer.initate_model_training(tarin_data, test_data)

    