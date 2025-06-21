import os
import sys
import yaml
import zipfile
import shutil
from wasteDetection.utils.main_utils import read_yaml_file
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import ModelTrainerConfig
from wasteDetection.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            zip_file = "data.zip"
            if os.path.exists(zip_file):
                with zipfile.ZipFile(zip_file, 'r') as zf:
                    zf.extractall(".") 
                os.remove(zip_file)  
            else:
                raise FileNotFoundError(f"{zip_file} not found!")

            if not os.path.exists("data.yaml"):
                raise FileNotFoundError("data.yaml not found after extracting data.zip!")

            with open("data.yaml", "r") as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config["nc"] = int(num_classes)

            with open(f"yolov5/models/custom_{model_config_file_name}.yaml", "w") as f:
                yaml.dump(config, f)

            os.system(
                f"cd yolov5 && python train.py --img 416 --batch {self.model_trainer_config.batch_size} "
                f"--epochs {self.model_trainer_config.no_epochs} "
                f"--data ../data.yaml --cfg ./models/custom_{model_config_file_name}.yaml "
                f"--weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache"
            )

            trained_model_dir = "yolov5/runs/train/yolov5s_results/weights/best.pt"
            final_dir = self.model_trainer_config.model_trainer_dir
            os.makedirs(final_dir, exist_ok=True)

            shutil.copy(trained_model_dir, final_dir)

            for item in ["yolov5/runs", "train", "valid", "data.yaml"]:
                if os.path.exists(item):
                    if os.path.isfile(item):
                        os.remove(item)
                    else:
                        shutil.rmtree(item)

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=os.path.join(final_dir, "best.pt")
            )
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)

