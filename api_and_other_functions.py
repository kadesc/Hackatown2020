from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time


def extractNameTags(image_tags):
    image_name_tags = []
    for tag in image_tags:
        image_name_tags.append(tag[0])
    return image_name_tags

def sortingTags(image_tags):
    for i in range(len(image_tags)):
            for j in range(len(image_tags)):
                if image_tags[i][1] > image_tags[j][1]:
                    image_tags[i],image_tags[j] = image_tags[j],image_tags[i]
    return image_tags

def findInDatabase(file_names, tags):
    output = []
    for tag in tags:
        for file_name in file_names:
            f = open(file_name, "r")
            lines = f.readlines()
            for line in lines:
                if tag == line.strip():
                    output.append([tag, file_name[:-4]])
            f.close()
    return output



# Basé sur le code : https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/python-sdk
# et sur le code : https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ComputerVisionQuickstart.py

'''API functions'''
def authenticateAndCreateClient():
    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    else:
        print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()
    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
    else:
        print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    return computervision_client


def addCaptionTags(description_result, image_tags, minimal_confidence):
    for caption in description_result.captions:
        if ((caption.confidence * 100) >= minimal_confidence):
            image_tags.append([caption.text, caption.confidence * 100])
    return image_tags

def addCategoryTags(categorize_result, image_tags, minimal_confidence):
    for category in categorize_result.categories:
        if ((category.score * 100) >= minimal_confidence):
            image_tags.append([category.name, category.score * 100])
    return image_tags

def addOtherTags(tags_results, image_tags, minimal_confidence):
    for tag in tags_results.tags:
            if ((tag.confidence * 100) >= minimal_confidence):
                image_tags.append([tag.name, tag.confidence * 100])
    return image_tags



def makeImageRecognitionAPI(imageLocationMode, imageLocation):
    MINIMAL_CONFIDENCE = 70
    image_tags = []
    image_features = ["categories"]

    '''Authenticates credentials and creates a client'''
    computervision_client = authenticateAndCreateClient()


    if (imageLocationMode == "local"):
        imageLocation = open(imageLocation, "rb")
        description_results = computervision_client.describe_image_in_stream(imageLocation)
        categorize_results = computervision_client.analyze_image_in_stream(imageLocation, image_features)
        tags_results = computervision_client.tag_image_in_stream(imageLocation)

    elif (imageLocationMode == "remote"):
        description_results = computervision_client.describe_image(imageLocation)
        categorize_results = computervision_client.analyze_image(imageLocation , image_features)
        tags_results = computervision_client.tag_image(imageLocation )  
    

    '''Describes the contents using API's tag types with the confidence score'''   
    image_tags = addCaptionTags(description_results, image_tags, MINIMAL_CONFIDENCE)
    image_tags = addCategoryTags(categorize_results, image_tags, MINIMAL_CONFIDENCE)
    image_tags = addOtherTags(tags_results, image_tags, MINIMAL_CONFIDENCE)

    image_tags = sortingTags(image_tags)

    return image_tags