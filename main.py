from image_recognition_api import extractNameTags, makeImageRecognitionAPI, findInDatabase

if __name__ == "__main__":
    file_names = ['trash.txt','recyclable.txt','compost.txt','other.txt']

    '''Create tags'''

    
    # User written input
    user_tag = []

    # Image input
    user_input = input("Enter directory or url: ")
    image_location = 'https://www.wsetglobal.com/media/7108/1608x900_wine_bottles.jpg' #url or directory (path)
    image_location_mode = "remote"
    image_tags = makeImageRecognitionAPI(image_location_mode,image_location)

    #Search tags in database and print result
    search_results = findInDatabase(file_names, image_tags)
    print(search_results)
    input("\nPress enter...")