import tensorflow as tf
from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="DriversLicenses")
trainer.setTrainConfig(object_names_array=["Face", "Identifier", "DlNumber"], batch_size=4,
                       num_experiments=200,)
trainer.trainModel()