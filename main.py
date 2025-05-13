from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion is Completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the Data Validation")
        datavalidationartifact = data_validation.initiate_data_validation()
        logging.info("Data Initiation Completed")
        print(datavalidationartifact)
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(datavalidationartifact,data_transformation_config)
        logging.info("Initiate the Data Transformation")
        datatransformationartifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation initiated")
        print(datatransformationartifact)
        
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config
                                     ,data_transformation_artifact=datatransformationartifact)
        logging.info("Initiate the Model Training")
        modeltrainingartifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training Completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
        