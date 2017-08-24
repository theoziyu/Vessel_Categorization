#needed libraries

from PIL import Image
import os
import cv2

#we define a list for current folders
category_types= [ "millitary"]

#for each category we go through the list
for category in category_types:


    #we now initiate the category name as another string
    catName = category

    #we change our current path to the category directory
    #user should provide path to the directory where category directories belong
    #os.chdir("/data/u/oguzhancan/check-delete/" + catName )
    
    print("We are now going inside " + catName)

    #we get the total number of files
    # -2 is for non jpeg files
    os.chdir("/data/u/oguzhancan/learn-tasks/task2/")

    #another loop for opening the images
    #if program cannot open the image, then just pass
    #in the except part we increase failure number and then delete the so called picture
    for filename in os.listdir(catName):
        try:
	    os.chdir("/data/u/oguzhancan/learn-tasks/task2/" + catName )
            im = Image.open(filename)
            name = im.format
            
            if (name=='JPEG'):
                img = cv2.imread(filename)
                grImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                rsImg = cv2.resize(grImg, (160,120))
                #ourName = catName + str(i+1) + '.jpg'
                #niceNumber += 1
                cv2.imwrite(filename, rsImg)
            
            else:
                #uncomment if you need to see which files are broken
                #print ("opened" + str(i+1)+", but now deleting it")
                #comment if you don't want to delete the files
                #os.remove(catName + str(i+1) + '.jpg')
		pass
            
        except Exception as e:
            print (filename+" cannot be opened!")
            #uncomment if you need to see which files are broken
            #print (i+1)
            #comment if you don't want to delete the files
            #os.remove(catName + str(i+1) + '.jpg')
