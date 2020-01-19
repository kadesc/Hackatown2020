from image_recognition_api import makeImageRecognitionAPI, findInDatabase

'''
Test url:
https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg
https://www.wsetglobal.com/media/7108/1608x900_wine_bottles.jpg

'''

if __name__ == "__main__":
    file_names = ['trash.txt','recyclable.txt','compost.txt','other.txt']
    image_tags = []
    done = False
    while not done:
        #Create search tags
        search_mode = input("Enter corresponding number to desired search mode (x to quit):\n 1 - text, 2 - local image, 3- online image\n")
        if (search_mode == "2"):
            search_mode = "local"
            image_location = input("Enter directory: ")
            image_tags = makeImageRecognitionAPI(search_mode,image_location)
        elif (search_mode == "3"):
            search_mode = "remote"
            image_location = input("Enter url: ")
            image_tags = makeImageRecognitionAPI(search_mode,image_location)
        elif (search_mode == "1"):
            image_tags = input("Enter item: ")
            image_tags = [image_tags]
        elif (search_mode == "x"):
            done = True
        else:
            print("Not a correct number entered")

        #Search tags in database and print result
        search_results = findInDatabase(file_names, image_tags)
        if (len(search_results)!= 0):
            print(search_results)
        else:
            print("No result found\n")
