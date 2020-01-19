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

def findInDatabase(file_names, tag):
    for file_name in file_names:
        f = open(file_name, "r")
        lines = f.readlines()
        for line in lines:
            if tag == line.strip():
                output = [tag, file_name[:-4]]     
        f.close()
    return output


def makeAPI(remote_image_url):
    MINIMAL_CONFIDENCE = 70

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


    image_tags = []
    
    '''Describes the contents of a remote image with the confidence score'''   
    description_results = computervision_client.describe_image(remote_image_url )  # Call API
    if (len(description_results.captions) == 0):
        print("No description detected.")
    else:
        for caption in description_results.captions:
            if ((caption.confidence * 100) >= MINIMAL_CONFIDENCE):
                image_tags.append([caption.text, caption.confidence * 100])


    '''Describes the category of a remote image with the confidence score'''   
    remote_image_features = ["categories"]
    categorize_results_remote = computervision_client.analyze_image(remote_image_url , remote_image_features)     # Call API with URL and features
    if (len(categorize_results_remote.categories) == 0):
        print("No categories detected.")
    else:
        for category in categorize_results_remote.categories:
            if ((category.score * 100) >= MINIMAL_CONFIDENCE):
                image_tags.append([category.name, category.score * 100])



    '''
    Returns a tag (key word) for each thing in the image.
    '''
    tags_result_remote = computervision_client.tag_image(remote_image_url )     # Call API with remote image
    if (len(tags_result_remote.tags) == 0):
        print("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            if ((tag.confidence * 100) >= MINIMAL_CONFIDENCE):
                image_tags.append([tag.name, tag.confidence * 100])
    


    for i in range(len(image_tags)):
        for j in range(len(image_tags)):
            if image_tags[i][1] > image_tags[j][1]:
                image_tags[i],image_tags[j] = image_tags[j],image_tags[i]



    return image_tags