from computer_vision_api import extractNameTags, makeImageRecognitionAPI, findInDatabase

if __name__ == "__main__":
    file_names = ['trash.txt','recyclable.txt','compost.txt','other.txt']

    '''Create tags'''
    # User written input
    user_tag = []

    # Image input
    image_location = 'https://www.wsetglobal.com/media/7108/1608x900_wine_bottles.jpg' #url or directory (path)
    image_location_mode = "remote"
    image_tags = extractNameTags(makeImageRecognitionAPI(image_location_mode,image_location))

    #Search tags in database and print result
    search_results = findInDatabase(file_names, image_tags)

    input("\nPress enter...")