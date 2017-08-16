#needed libaries

#these libraries are for python 3 or higher, comment these if you use python 2.7
#import urllib.request
#import os

#these libraries are for python 2.7, comment these if you use python 3 or higher
import os
import urllib
import urllib2


#define a dictionary that holds the type of the ship and the URL to find its pics

dict_data = 	{
		 "bus_autobus": "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02924116",
		 "trolleybus" : "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04487081",
		 "minibus"    : "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03769881",
		 "school_bus" : "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04146614"
		}
#the dictionary can go on as much as we want

#beginning of the function

def store_raw_images(ship_data):


	for Item in dict_data.keys():

	#Number Name Details should be put in here!

		#Show the user that download has started
		print("Started downloading {0} pictures." .format(Item))

		#URL taken from image net downloads tab

		images_link = dict_data[Item]

		#read and decode the given URL

		#this line is for python 3 or higher, comment if you use python 2.7
		#images_urls = urllib.request.urlopen(images_link).read().decode()

		#this line is for python 2.7, comment if you use python 3 or higher
		images_urls = urllib2.urlopen(images_link).read().decode()

		#define a category name
		category_name = Item



		#if there is not a folder with the given name then this piece creates it for us

		if not os.path.exists(category_name):
			os.makedirs(category_name)

		#a number is defined for naming purposes
		#saved images will be named as 'category_name1, category_name2, category_name3' etc.

		number = 1

		#we read the decoded URL, we take every line as a seperate input
		for i in images_urls.split('\n'):
			try:
				#prints the URL, saves the image to folder
				 
				print(i)
				#this line is for python 3 or higher, comment if you use python 2.7
				#urllib.request.urlretrieve(i, category_name + "/" + category_name + str(number)+'.jpg')
                
				#this line is for python 2.7, comment if you use python 3 or higher
				urllib.urlretrieve(i, category_name + "/" + category_name + str(number)+'.jpg')
				number = len(os.listdir(category_name + '/')) + 1

			except Exception as e:

				#If it couldn't download the image, shows the error
				print(str(e))

		print("Finisheded downloading {0} pictures." .format(Item))

#start running the code
store_raw_images(dict_data)
