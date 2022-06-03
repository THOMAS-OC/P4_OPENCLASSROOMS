import os, time, shutil
x = 1

HTML_FILE = str(os.stat("web-design.html").st_atime)
CSS_FILE = str(os.stat("style.css").st_atime)

while x:
    html_meta_data = os.stat("web-design.html")
    css_meta_data = os.stat("style.css")
    time.sleep(2)

    if HTML_FILE != str(html_meta_data.st_atime) :
        print("Actualisation de index.html")
        #Suppression du fichier index
        os.remove("index.html")
        time.sleep(1)
        #Création d'un nouveau fichier index
        shutil.copyfile("web-design.html", "index.html")
        HTML_FILE = str(os.stat("web-design.html").st_atime)
    else :
        pass

    if CSS_FILE != str(css_meta_data.st_atime) :
        print("Actualisation de style.min.css")
        os.system("css-minify -f style.css -o .")
        CSS_FILE = str(os.stat("style.css").st_atime)
    else :
        pass