from computer_vision_api import extractNameTags, makeAPI, findInDatabase

if __name__ == "__main__":
    file_names = ['trash.txt','recyclable.txt','compost.txt','other.txt']

    #Create and print tags
    user_tag = []
    image_URL = 'https://www.wsetglobal.com/media/7108/1608x900_wine_bottles.jpg'
    
    image_tags = extractNameTags(makeAPI(image_URL))

    #Search tags in database and print result
    search_results = findInDatabase(file_names,image_tags)

    input("\nPress enter...")