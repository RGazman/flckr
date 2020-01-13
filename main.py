from bs4 import BeautifulSoup
import os #Module for directory (create/delete)
import requests
import re


def CheckList():
    path = os.getcwd()      #Get path for main.py. FOR TESTING
    print (path)

    fotog_for_open = path + "\Fotolist.txt"      #Generate new path for fotograph list
    #print (fotog_for_open) 
    #check = open('.\check.html','w+')

    links_fotograph = open(fotog_for_open, "r")  #Open file for reading
    for read_links in links_fotograph:           #Read link from file; by line
        print (read_links) 
        #check.writelines(str(requests.get(read_links.strip()).content))    #Open link without '\n' and write html in file
        #print (requests.get(read_links.strip()).content)                   #Open link without '\n'
        
        #reg_Ex = '("title" content=")+[\s\w\d]{1,30}'                                  #Regular expression
        soup = str(requests.get(read_links.strip()).content)                            #Get response in memory
        find_reg = str(re.findall(r'("title" content=")+([\s\w\d]{1,30})', soup))       #Parse response until [('"title" content="', 'DDG XIE')]    //including "[()]"
        find_reg = str(re.findall(r"'[\s\w\d]{1,30}'", find_reg))                       #Parse response until ["'DDG XIE'"]
        find_reg = find_reg.strip('["\'\'"]')                                           #Parse response until LoginName / without quotes
        print (find_reg)
        #############
        
        #check.writelines("\n")
        #check.truncate(0)                              #Erase the file

        
        access_right = 0o755                            #Define the access rights
        new_path = "\\"+find_reg                        #Define the new name for new dir
        print (new_path)
        try:
            os.mkdir(path + new_path, access_right)     #Create dir with new_path and access_ringt
        except OSError:
            print ("Cration of the dir %s failed" % path)
        else:
            print ("OKSuccessfully created")
        

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
