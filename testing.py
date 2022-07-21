from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("DriversLicenses/models/detection_model-ex-055--loss-0016.222.h5")
detector.setJsonPath("DriversLicenses/json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="DriversLicenses/test/images/license1132.jpg", output_image_path="license1132-detected.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])