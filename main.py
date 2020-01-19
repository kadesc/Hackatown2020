from computer_vision_api import makeAPI

if __name__ == "__main__":
    image_URL = 'https://www.wsetglobal.com/media/7108/1608x900_wine_bottles.jpg'
    image_tags = makeAPI(image_URL)
    
    liste_dechets = "liste_dechets.txt"
    