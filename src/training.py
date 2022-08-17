from src.utils.common import read_config
from src.utils.data_mgmt import get_data
from src.utils.model import create_model
import argparse


def training(config_path):
    config=read_config(config_path)
    validation_datasize=config['params']["validation_datasize"]
    LOSS_FUNCTION=config['params']["loss_function"]
    optimizer=config['params']["optimizer"]
    METRICS=config['params']["metrics"]
    NUM_CLASSES=config['params']["num_classes"]
    EPOCHS=config['params']["epochs"]
    VALIDATION_SET=(X_valid,y_valid)
    
    (X_train,y_train),(X_valid,y_valid),(X_test,y_test)=get_data(validation_datasize)
    model=create_model(LOSS_FUNCTION,OPTIMIZER, METRICS,NUM_CLASSES)
    history=model.fit(X_train,y_train,epoch=EPOCHS,validation_data=VALIDATION_SET)









if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_arguments("--config","-c",default="config.yaml")
    parsed_args=args.parse_args()
    training(config_path=parsed_args.config)