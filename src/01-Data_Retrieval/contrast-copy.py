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
    
    print("We are going inside of " + catName)

    os.chdir("/data/u/oguzhancan/ships/") 
       
    for filename in os.listdir(catName):

        try:
            os.chdir("/data/u/oguzhancan/ships/"+catName) 
            im = Image.open(filename)
            name = im.format
            
            if (name=='JPEG'):
                img = cv2.imread(filename)
                rows,cols,ch = img.shape
                cimg = (img*(0.4)).astype(np.uint8) + 20

                os.chdir("/data/u/oguzhancan/contrast-original/")

                if not os.path.exists("contrast_" + catName):
                    os.makedirs("contrast_" + catName)
		
                os.chdir("/data/u/oguzhancan/contrast-original/contrast_"+catName)
		
                tag = "contrast_" + filename
		
                cv2.imwrite(tag, cimg)
                os.chdir("/data/u/oguzhancan/ships/") 
            
            else:
                #uncomment if you need to see which files are broken
                #print ("opened" + str(i+1)+", but now deleting it")
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
