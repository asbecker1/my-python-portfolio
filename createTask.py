#Ap computer science

import random #This imports the random library

from PIL import Image #This is a code that we learned in class to open images
import requests
from io import BytesIO

#Some of the data was cut off due to the size of the pdf, so I included a spreedsheet:
#https://docs.google.com/spreadsheets/d/132mLn4ET5rwVRC4qXJJDhyLo9O1I5rwuZi-xOuIf46A/edit?gid=0#gid=0
foodList = ["burrata","cheeseboard","avocado_toast","fruit_salad",
            "bagel","caprese_sandwich","chicken_alfredo","grilled_cheese",
            "crepes","tacos","gnocci","salad","gelato","brownies","cookies"]
meal = ["snack","snack","breakfast","snack","breakfast","lunch","dinner","lunch","breakfast","dinner","dinner","lunch","dessert","dessert","dessert"] #This is a list of the different meals
links = ["https://i2.wp.com/yestoyolks.com/wp-content/uploads/2020/06/IMG_9109-2.jpg?resize=682%2C1024&ssl=1","https://data.thefeedfeed.com/static/2019/10/29/15723712545db87b368e766.webp","https://californiaavocado.com/wp-content/uploads/2020/07/California-Avocado-Toast-Three-Ways.jpeg","https://kathrynskitchenblog.com/wp-content/uploads/2021/02/Berry-Salad-4-scaled.jpg","https://images.squarespace-cdn.com/content/v1/5f564f33b94bfb4447810a47/e25b0355-8a4e-46a7-b9f7-ef41e9e3d4de/bagel%2Bcc.png?format=2500w","http://www.simplyscratch.com/wp-content/uploads/2013/05/Caprese-Panini-www.SimplyScratch.com_-620x415.jpg","https://www.recipetineats.com/tachyon/2017/03/One-Pot-Chicken-Alfredo-2.jpg?resize=1200%2C1680&zoom=0.67","https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1000w,f_auto,q_auto:best/newscms/2020_07/3230981/200214-stock-grilled-cheese-ew-108p.jpg","https://theinspiredhome.com/wp-content/uploads/2022/12/Crepe-Brunch-14.jpg","https://danosseasoning.com/wp-content/uploads/2022/03/Beef-Tacos-1024x767.jpg","https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_auto,w_728,h_546/k%2FPhoto%2FRecipes%2F2020-10-How-to-Make-the-Easiest-Gnocchi-from-Scratch%20%2FHT-Gnocchi-From-Scratch-479","https://www.seriouseats.com/thmb/9TnG8tGrg-1V65xKR6Y8hJu8YJ4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/the-best-caesar-salad-recipe-06-40e70f549ba2489db09355abd62f79a9.jpg","https://blog.italotreno.com/wp-content/uploads/2024/08/gelato.jpg","https://www.kingarthurbaking.com/sites/default/files/styles/featured_image/public/recipe_legacy/1228-3-large.jpg?itok=ADPr9QfO","https://img.taste.com.au/FH2xb58L/taste/2010/01/choc-chip-cookies-image1-197537-1.jpg"]#This is a list of links
filteredList = [] #Food from foodList are added to this when filtered
randomFood = 0 #This is a variable that determines which food is given

def open_image(url): #This is a function that we learned in class to open an image
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def type(answer):
    print("Welcome, I will be giving you an idea for some food to eat!")
    while True:
        if answer == "snack":
            for i in range(len(meal)):
                if answer == meal[i]:
                    filteredList.append(foodList[i])
                    randomFood = random.randint(0,2)
                    if randomFood == 0:
                        open_image(links[0])
                        print("this is a picture of burrata! it is delicious!")
                    elif randomFood == 1:
                        open_image(links[1])
                        print("this is a picture of a cheeseboard! it has a lot of variety!")
                    elif randomFood == 2:
                        open_image(links[3])
                        print("this is a picture of a fruit salad! it is sweet!")
                    answer = input("Do you want another snack or quit?")
        elif answer == "breakfast":
            for i in range(len(meal)):
                if answer == meal[i]:
                    filteredList.append(foodList[i])
                    randomFood = random.randint(0,2)
                    if randomFood == 0:
                        open_image(links[2])
                        print("this is a picture of avacado toast! it is delicious!")
                    elif randomFood == 1:
                        open_image(links[4])
                        print("this is a picture of a bagel! it has a lot of variety of cream cheese!")
                    elif randomFood == 2:
                        open_image(links[8])
                        print("this is a picture of crepes! they can be sweet or salty!")
                    answer = input("Do you want another breakfast or quit?")
        elif answer == "lunch":
            for i in range(len(meal)):
                if answer == meal[i]:
                    filteredList.append(foodList[i])
                    randomFood = random.randint(0,2)
                    if randomFood == 0:
                        open_image(links[5])
                        print("this is a picture of a caprese sandwich! it is delicious!")
                    elif randomFood == 1:
                        open_image(links[7])
                        print("this is a picture of a grilled cheese sandwich! it is a comfort food!")
                    elif randomFood == 2:
                        open_image(links[11])
                        print("this is a picture of a salad! it is healthy and yummy!")
                    answer = input("Do you want another lunch or quit?")
        elif answer == "dinner":
            for i in range(len(meal)):
                if answer == meal[i]:
                    filteredList.append(foodList[i])
                    randomFood = random.randint(0,2)
                    if randomFood == 0:
                        open_image(links[6])
                        print("this is a picture of chicken alfredo! it is delicious!")
                    elif randomFood == 1:
                        open_image(links[9])
                        print("this is a picture of a tacos! it has a lot of variety!")
                    elif randomFood == 2:
                        open_image(links[10])
                        print("this is a picture of a gnocci! it is super yummy!")
                    answer = input("Do you want another dinner or quit?")
        elif answer == "dessert":
            for i in range(len(meal)):
                if answer == meal[i]:
                    filteredList.append(foodList[i])
                    randomFood = random.randint(0,2)
                    if randomFood == 0:
                        open_image(links[12])
                        print("this is a picture of gelato! it is delicious!")
                    elif randomFood == 1:
                        open_image(links[13])
                        print("this is a picture of a brownies! they melt in your mouth!")
                    elif randomFood == 2:
                        open_image(links[14])
                        print("this is a picture of cookies! they are sweet!")
                    answer = input("Do you want another dessert or quit?")
        else:
            print("Thank you so much for playing, we hope you enjoy your meal!")
            break

type(input("Do you want a snack, breakfast, lunch, dinner, dessert, or quit?"))

#Sources of images
#A picture of Burrata. Image Source: Yes to Yolks. Author: Molly.
    #Accessed via https://yestoyolks.com/8-2/.
    #Article: Burrata Brushchetta Toasts. Published: June 10, 2020.
#A picture of a Cheeseboard. Image Source: Feedfeed. Author: Meg Quinn.
    #Accessed via https://thefeedfeed.com/ainttooproudtomeg/autumn-cheese-board.
    #Article: Autumn Cheese Board.
#A picture of Avacado Toast. Image Source: California avacados.
    #Accessed via https://californiaavocado.com/recipe/california-avocado-toast-three-ways/
    #Article: California Avacado Toast Three Ways
#A picture of a Fruit Salad. Image Source: The Forked Spoon. Author: Jessica Randhawa.
    #Accessed via https://theforkedspoon.com/fruit-salad-recipe/.
    #Article: Easy Fruit Salad Recipe.
#A picture of a Bagel. Image Source: Tilly Bagel.
    #Accessed via https://tillybagelshop.com/order-online.
#A picture of a Caprese Sandwich. Image Source: Simply Scratch. Author: Laurie.
    #Accessed via https://www.simplyscratch.com/pressed-caprese-sandwich/.
    #Article: Pressed Caprese Sandwich.
#A picture of Chicken Alfredo. Image Source: Recipetineats. Author: Nagl.
    #Accessed via https://www.recipetineats.com/one-pot-chicken-alfredo-pasta/.
    #Article: One Pot Chicken Alfredo Pasta
#A picture of Grilled Cheese. Image Source: Once Upon A Chef. Author: Jennifer Segal.
    #Accessed via https://www.onceuponachef.com/recipes/grilled-cheese.html.
    #Article: Grilled Cheese.
#A picture of Crepes. Image Source: The Inspired Home. Author: Elizabeth Van Lierde.
    #Accessed via https://theinspiredhome.com/articles/these-classic-sweet-french-crepes-taste-just-like-paris/.
    #Article: These Classic Sweet French Crepes Taste Just Like Paris.
#A picture of Tacos. Image Source: Dan-O's Seasoning.
    #Accessed via https://danosseasoning.com/recipes/ground-beef-tacos/.
#A picture of Gnocci. Image Source: The Kitchen. Author: Valeria Necchio.
    #Accessed via https://www.thekitchn.com/gnocchi-recipe-23087502.
    #Article: How To Make The Absolute Best Gnocchi From Scratch.
#A picture of Salad. Image Source: Serious Eats. Author: J. Kenji Lopez-alt.
    #Accessed via https://www.seriouseats.com/the-best-caesar-salad-recipe.
    #Article: The Best Ceaser Salad.
#A picture of Gelato. Image Source: IlatoBlog.
    #Accessed via https://blog.italotreno.com/en/italian-food/italian-gelato-shops/.
    #Article: Italy's Best Gelato: A Guide To The Finest Ice Cream Shop.
#A picture of Brownies. Image Source: King Aurthor Baking. Author: Pj Hamel.
    #Accessed via https://www.kingarthurbaking.com/recipes/whole-grain-brownies-recipe.
    #Article: Brownies.
#A picture of Cookies. Image Source: Taste. Author: Alison Turner.
    #Accessed via https://www.taste.com.au/recipes/chocolate-chip-cookies-2/1bfaa0e6-13b4-489d-bbd8-1cc5caf1fa32.
    #Article: The Ultimate Chocolate Chip Cookie Recipe.

