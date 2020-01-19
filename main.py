from computer_vision_api import findInDatabase, makeAPI





if __name__ == "__main__":
    #image_URL = 'https://www.wsetglobal.com/media/7108/1608x900_wine_bottles.jpg'
    #image_tags = makeAPI(image_URL)

    tags = ["bottle", "tiger", "motorcycle","paper"]
    file_names = ['trash.txt','recyclable.txt','compost.txt','other.txt']
    search_Outputs = []
    for tag in tags:
        search_Output = findInDatabase(file_names,tag)
        print(search_Output)
        input("\nPress enter...") 
        if (len(search_Output) != 0):
            search_Outputs.append(search_Output)
            print(search_Outputs)
            print("appended")
            input("\nPress enter...") 
    
    input("\nPress enter...") 