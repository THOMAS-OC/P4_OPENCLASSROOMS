import os, time, shutil
x = 1

V1 = str(os.stat("web-design.html").st_atime)


while x:
    html_meta_data = os.stat("web-design.html")
    time.sleep(2)

    if V1 != str(html_meta_data.st_atime) :
        print("Actualisation de index.html")
        #Suppression du fichier index
        os.remove("index.html")
        time.sleep(1)
        #Création d'un nouveau fichier index
        shutil.copyfile("web-design.html", "index.html")
        V1 = str(os.stat("web-design.html").st_atime)
    else :
        pass