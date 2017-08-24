#needed libraries

from PIL import Image
import os
import cv2
import numpy as np

#we define a list for current folders
category_types= ["Attack_Submarine", "Ballistic_Missile_Submarine", "fish_boat",
		  "barge", "bc_ship", "capital_ship", "cargo_ship", "Container_Boat", "destroyer_escort_ship",
		  "dredger_ship", "drednought_ship", "ferry", "fire_boat", "frigate_ship", "gmc_ship",
		  "guard_ship", "hospital_ship", "Houseboat", "hovercraft", "hydrofoil", "ice_breaker_ship",
		  "Ice_Yacht", "ironclad_ship", "lc_ship", "man_of_war_ship", "mine_layer_ship", "Nuclear_Submarine",
		  "Oil_Tanker", "passenger_ship", "patrol_ship", "p_battleship", "pilot_boat", "ps_ship", "pt_ship",
		  "Racing_Yacht", "Research_submarine", "school_ship", "Submarine_Pigboat", "Submersile", "Super_Tanker",
		  "surface_ship", "tbd_ship", "tender", "Tender_Supply", "Trawler", "Trawler_Dragger", "tug", "whaler_ship"]

os.chdir("/data/u/oguzhancan/ships/")
    

#for each category we go through the list "aircraft_ship",
for category in category_types:

    #we now initiate the category name as another string
    catName = category

    #we change our current path to the category directory
    #user should provide path to the directory where category directories belong
    
    print("We are going inside of " + catName)

    #we get the total number of files
    # -2 is for non jpeg files
    #ourLength = len(os.listdir('.'))
    
    #print("Our length is " + str(ourLength))

    #another loop for opening the images
    #if program cannot open the image, then just pass
    #in the except part we increase failure number and then delete the so called picture
    #os.chdir("/data/u/oguzhancan/ships/"+catName)
    os.chdir("/data/u/oguzhancan/ships/") 
       
    for filename in os.listdir(catName):

	try:
	    os.chdir("/data/u/oguzhancan/ships/"+catName) 
            im = Image.open(filename)
            name = im.format
            
            if (name=='JPEG'):
                img = cv2.imread(filename)
		rows,cols,ch = img.shape
		#print cols, rows
		"""
		if (cols > rows) :
		
		    x1 = (cols - rows)/2
		    x2 = x1 + rows

		    y1 = (rows - (cols/2))/2
		    y2 = y1 + (cols/2)

		else:
		    x1 = (cols-(rows/2))/2
		    x2 = x1 + rows/2

		    y1 = (rows - cols)/2
		    y2 = y1 + cols
		"""
		#print x1, x2, y1, y2
		"""
		pts1 = np.float32([[cols,0],[cols,rows],[0,0],[0, rows]])
		pts2 = np.float32([[0,0],[0,rows],[cols,0],[cols,rows]])
		M = cv2.getPerspectiveTransform(pts1,pts2)
		dst = cv2.warpPerspective(img,M,(cols,rows))
		"""
		kernel = np.ones((5,5),np.float32)/25
		dst = cv2.filter2D(img,-1,kernel)

		
		os.chdir("/data/u/oguzhancan/blur-original/")

		if not os.path.exists("blur_" + catName):
			os.makedirs("blur_" + catName)
		
		os.chdir("/data/u/oguzhancan/blur-original/blur_"+catName)
		
		tag = "blur_" + filename
		
                cv2.imwrite(tag, dst)
		os.chdir("/data/u/oguzhancan/ships/") 
            
            else:
                #uncomment if you need to see which files are broken
                print ("opened" + str(i+1)+", but now deleting it")
                #comment if you don't want to delete the files
                #os.remove(filename)
		pass
	            
        except Exception as e:
            print (filename +" cannot be opened!")
	    os.chdir("/data/u/oguzhancan/ships/") 
            #uncomment if you need to see which files are broken
            #print (i+1)
            #comment if you don't want to delete the files
            #os.remove(filename)
