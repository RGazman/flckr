# flickr.com
 # English
 Upload photo with flickr.com

### Capabilities:
  + Uploads .jpg images.
  + If possible, it loads the original photo size.
  + Separates photos by photographers (the name of the folder is the photographer’s nickname).
  + You can specify any number of photographers. The main thing is to have enough disk space.
  

### Preparation:
 1. Gitclone or download .zip
 2. Install next apps (for everything: version not lower than specified):
   
     2.1. Python3.6.    
     2.2. beautifulsoup4==4.8.0     command: pip install beautifulsoup4.     
     2.3. requests==2.19.1          command: pip install requests. 
 3. Go to https://www.flickr.com/services/apps and create new app. Get api_key on this page.
 4. The received key in paragraph 3 write in lines 56 and 75
 
  ***Example:***
  ```python
   #python
   'api_key' : 'ph34tjf0k30dkfeh89',                     #Required //Indicate your api key
  ```
 5. Enter links to photographers in the list Fotolist.txt
 
 ### Run:
 In folder with this files via cmd (command line):
```cmd
//cmd
python main.py
```
 
 # Russian / Русский
 Загрузка фото с flickr.com
 
 ### Возможности:
  + Скачивает в формате .jpg
  + Если возможно, скачивает оригинал фотографий.
  + Разделяет фото по фотографам (название папки - никнейм фотографа).
  + Можно указать любое количество фотографов. Главное, чтобы хватило места на диске.
  
 ### Подготовка:
  1. Скопируйте или скачайте репозиторий.
  2. Установите (для всего: версия не ниже указанной):       
     
     2.1. Python3.6.    
     2.2. beautifulsoup4==4.8.0   команда: pip install beautifulsoup4.     
     2.3. requests==2.19.1        команда: pip install requests.
     
  3. Получите api_key на странице https://www.flickr.com/services/apps. Вам необходимо создать новое приложение.
  4. Полученный ключ из пункта 3 укажите в '' в строчках 56, 75
  
  ***Пример:***
  ```python
   #python
   'api_key' : 'ph34tjf0k30dkfeh89',                     #Required //Indicate your api key
  ```
 5. Указать ссылки на фотографов в файле Fotolist.txt

### Запуск:
Из папки с файлами в командной строке:
```cmd
//cmd
python main.py
```
