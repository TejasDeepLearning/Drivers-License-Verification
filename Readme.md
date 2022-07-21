# Document Verification Project ![](https://img.shields.io/badge/Tests-Pass-blue)
The aim of this project was to create a way to identify the features of a Driver's License and parse that information using seperate Machine Learning techniques such as **Object Detection** and **Optical Character Recognition**. 
The dataset I gathered contained `9000` images of drivers licenses from which I sampled out `500`, with a `90%/10%` split for training and validation.
I've placed the latest version of the project on this page while moving the previous iterations into an **Archived Releases directory** for perusal.

![Imgur](https://i.imgur.com/MMej47ml.jpg)
![Imgur](https://i.imgur.com/iPxT0Wxl.jpg)

## Table of Contents
- [How to use](#how-to-use)
- [Archived Releases](#archived-releases)
- [Roadmap](#roadmap)
- [Credits](#credits)

# How to Use
For the Object Detection phase of this project, head over to the [ImageAi Documentation](https://imageai.readthedocs.io/en/latest/) website to see how you can get started on the project. 
A couple of things to note are:
- Install anaconda and create a conda environment with `python version 3.7.6` as per the requirement
- Follow the necessary steps to install Tensorflow with gpu compatibility as it is useful for training models on datasets with a large number of images. I'll include a [video](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj15o7r9oj5AhU7TmwGHfGCCBUQwqsBegQIGBAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DhHWkvEcDBO0&usg=AOvVaw1FkucvpisZGhZohnfNqJAZ) here for reference 

For text extraction, I used [PaddleOCR](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjJ2cSM-oj5AhXMHbcAHf6YAw4QFnoECAUQAQ&url=https%3A%2F%2Fpypi.org%2Fproject%2Fpaddleocr%2F&usg=AOvVaw0W5IIWKVagVGyqU2KvLfSN) a library that I chose above Tesseract and EasyOCR due to its ease of use and no preprocessing required.

# Archived Releases
Provided here is the [link](https://github.com/Tj-dev-py/Drivers-License-Verification/tree/main/Archived%20Versions) to all of the archived versions of the project, which didn't meet the mark.

# Roadmap
I do plan to improve upon this project in the future some ideas I have in mind are finding ways to combine Object Detection and OCR in a single script, because as of right now with all the dependency conflicts, I can't place it all in one single environment to work with. 

I also want to gather a large labelled dataset for training, but this would require me manually labelling every image which takes time, and since there are no readily available, cleaned, and processed datasets around for this, it's going to be hard.

# Credits
PaddleOCR, ImageAi
