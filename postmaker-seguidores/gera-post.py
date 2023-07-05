# import the modules
import os
from os import listdir
import pathlib
import sys


pathlib.Path.cwd()
# get the path/directory
#folder_dir = pathlib.Path.cwd()#"imgs"
folder_dir = "/mnt/24860678-791e-4d8d-ab99-c76390855d86/Dropbox/vamoslonge-thumbs/postmaker-seguidores/"
for images in os.listdir(folder_dir+"jpg"):
    print(images)
    # check if the image ends with png
    if (images.endswith(".jpg")):
        print(images)
        original_stdout = sys.stdout 
        #with open(images+'.svg', 'w') as f:
        replace_numero = images[0:3]
        replace_titulo = images[4:-4]
        replace_imagem = folder_dir+"jpg/"+images

        #print(numero + titulo + imagem)
        # creating a variable and storing the text
        # that we want to search
        search_numero = "TROCARKM"
        search_titulo = "TROCARTITULO"
        search_imagem = "TROCARIMAGEM"
        # creating a variable and storing the text
        # that we want to add
        #replace_text = "replaced"
          
        # Opening our text file in read only
        # mode using the open() function
        with open(folder_dir+'postmaker-seguidores-0.svg', 'r') as file:
        
            # Reading the content of the file
            # using the read() function and storing
            # them in a new variable
            data = file.read()
          
            # Searching and replacing the text
            # using the replace() function
            data = data.replace(search_numero, replace_numero)
            data = data.replace(search_titulo, replace_titulo)
            data = data.replace(search_imagem, replace_imagem)
          
        # Opening our text file in write only
        # mode to write the replaced content
        with open(folder_dir+"/"+images+'.svg', 'w') as file:
        #sys.stdout = f # Change the standard output to the file we created.
        #with open(images+'.svg', 'w') as f:
            # Writing the replaced data in our
            # text file
            file.write(data)
        
        sys.stdout = original_stdout # Reset the standard output to its original value

        #print(images)
        ##/mnt/24860678-791e-4d8d-ab99-c76390855d86/Dropbox/vamoslonge-thumbs/thumbmaker-relatos-viajados/043 Salvador.jpg