from bs4 import BeautifulSoup
import os #Module for directory (create/delete)
import requests


def CheckList():
    path = os.getcwd()      #Get path for main.py. FOR TESTING
    #print (path)

    fotog_for_open = path + "\Fotolist.txt"      #Generate new path for fotograph list
    #print (fotog_for_open) 
    check = open('.\check.html','w+')

    links_fotograph = open(fotog_for_open, "r")  #Open file for reading
    for read_links in links_fotograph:           #Read link from file; by line
        print (read_links) 
        check.writelines(str(requests.get(read_links.strip()).content))    #Open link without '\n'   
        #print (requests.get(read_links.strip()).content) #Open link without '\n'
        cache = BeautifulSoup(check, features="lxml")
        print(cache)
        
        check.truncate(0)                        #Erase the file
        

    links_fotograph.close()                      #Close file
    check.close()                                #Close file



'''
    access_right = 0o755    #Define the access rights
    new_path = "\\test"     #Define the new name for new dir
    try:
        os.mkdir(path + new_path, access_right)     #Create dir with new_path and access_ringt
    except OSError:
        print ("Creation of the dir %s failed" % path)
    else:
        print ("OKSuccessfully created")
'''


CheckList()
