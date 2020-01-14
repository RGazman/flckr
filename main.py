from bs4 import BeautifulSoup
import os #Module for directory (create/delete)
import requests
import re
import datetime


def CheckList():
    path = os.getcwd()      #Get path for main.py
    #print (path)           #DEBUG

    fotog_for_open = path + "\Fotolist.txt"      #Generate new path for fotograph list
    #print (fotog_for_open)                      #DEBUG

    links_fotograph = open(fotog_for_open, "r")  #Open file for reading
    for read_links in links_fotograph:           #Read link from file; by line
        #print (read_links) 
       
        #reg_Ex = '("title" content=")+[\s\w\d]{1,30}'                                  #Regular expression
        soup = str(requests.get(read_links.strip()).content)                            #Get response in memory
        find_reg = str(re.findall(r'("title" content=")+([\s\w\d]{1,30})', soup))       #Parse response until [('"title" content="', 'DDG XIE')]    //including "[()]"
        find_reg = str(re.findall(r"'[\s\w\d]{1,30}'", find_reg))                       #Parse response until ["'DDG XIE'"]
        #find_reg = find_reg.strip('[]')
        find_reg = find_reg.strip('["\'\'"]')                                           #Parse response until NickName / without qoutes            //Its worked
        find_reg = find_reg.strip(' ')
        re.purge
        user_id = re.search(r'((\d+)@(N\d+))',soup)                                     #Pasrse response for searching LoginName
        #print ("user_id " + user_id.group(0))                                          #Print
        #print ('find_reg ' +find_reg)                                                  #DEBUG
        #############

        access_right = 0o755                            #Define the access rights
        new_path = "\\"+find_reg                        #Define the new name for new dir
        #print (new_path)                               #DEBUG
        try:
            if not os.path.exists (new_path):
                os.mkdir(path + new_path, access_right)     #Create dir with new_path and access_ringt
        except OSError:
            print ("Creation of the dir %s failed" % path)
        else:
            print ("OKSuccessfully created %s " % new_path)
   
        UploadFoto (user_id,new_path)
        
    links_fotograph.close()                       #Close file


def UploadFoto(user_id,new_path):
    #Parse XML 
    #print ('test')                                                             #DEBUG
    page = 1                                                                    #First page response
    per_page = 50    
    pages = 2
    data={ #Parameters for requests
        'method' : 'flickr.people.getPhotos',                                   #Required
        'api_key' : '',                                                         #Required //Indicate your api key
        'user_id' : user_id.group(0),                                           #
        'per_page' : str(per_page),                                             #
        'page' : page,
        'extras' : 'url_o,url_k,date_upload'                                    #
    }
    resp = str(requests.get('https://api.flickr.com/services/rest?', data).content)
    pages = re.search(r'((pages=)"(\d+)")', resp).group(0)
    pages = re.search(r'(\d+)',pages).group(0)
    #print (resp)
    #print (url_k)
    #print (url_o)
    #print (dateupload)
    print ('pages ' + str(pages))


    for page in range(1, int(pages)+1):
        data={ #Parameters for requests
            'method' : 'flickr.people.getPhotos',                                   #Required
            'api_key' : '',                                                         #Required //Indicate your api key
            'user_id' : user_id.group(0),                                           #
            'per_page' : str(per_page),                                             #
            'page' : page,
            'extras' : 'url_o,url_k,date_upload'                                    #
        }

        resp = str(requests.get('https://api.flickr.com/services/rest?', data).content)
        #pages = re.search(r'((pages=)"(\d+)")', resp).group(0)
        #pages = re.search(r'(\d+)',pages).group(0)
        print (pages)

        url_k = re.findall(r'(\w+://\w+.\w+.com/\d+/\w+k.jpg)',resp)
        url_o = re.findall(r'(\w+://\w+.\w+.com/\d+/\w+o.jpg)',resp)
        dateupload = str(re.findall(r'(\w{10}=)"(\d{10})',resp))
        dateupload = re.findall(r'(\d+)',dateupload)
        #print (dateupload)
        
        print ('page ' + str(page))
        i = 0
        if url_o == [] or (len(url_o) < len(url_k)):
            print ('url_k')
            print (len(url_k))
            for i in range(0,len(url_k)): #Upload photo size 'k', 2048px                
                print ('k '+str(i))
                photo = requests.get(str(url_k[i]).strip('["\'\'"]'))
                #print (i, ' ',dateupload[i])
                dateupload_UTC = datetime.datetime.fromtimestamp(int(str(dateupload[i]).strip('["\'\'"]'))).strftime('%Y-%m-%d %H.%M.%S')   
                path = str(os.getcwd() + new_path + '\\' + dateupload_UTC + str(i)+".jpg")
                photo_upload = open(path, "wb")
                photo_upload.write (photo.content)
                photo.close()   
                dateupload_UTC = None 
        else:
            print ('url_o')
            print (len(url_o))
            for i in range(0,len(url_o)): #Upload photo size 'o', Original
                print ('o '+str(i))
                photo = requests.get(str(url_o[i]).strip('["\'\'"]'))
                #print (i, ' ',dateupload[i])
                dateupload_UTC = datetime.datetime.fromtimestamp(int(str(dateupload[i]).strip('["\'\'"]'))).strftime('%Y-%m-%d %H.%M.%S')   
                path = str(os.getcwd() + new_path + '\\' + dateupload_UTC + str(i)+".jpg")
                photo_upload = open(path, "wb")
                photo_upload.write (photo.content)
                photo.close()   
                dateupload_UTC = None 



    
 
CheckList()             #Check photographer of file and creation directory with him name
 
