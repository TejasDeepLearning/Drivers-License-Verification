from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory='DriversLicenses')
metrics = trainer.evaluateModel(model_path='DriversLicenses/models/detection_model-ex-055--loss-0016.222.h5',
                                json_path='DriversLicenses/json/detection_config.json')
print(metrics)
