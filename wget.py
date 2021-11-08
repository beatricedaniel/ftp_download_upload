# Modules par défaut à importer
import subprocess
import logging
import os
import json

# Modules à installer avant l'import
import wget

# Lecture de la configuration du serveur SFTP avec le compte en lecture
def read_config_lecture(path_in):
    print("--- Lancement de la lecture de la configuration du serveur en lecture")
    with open(path_in) as f:
        dict_ret = json.load(f)
    L_ret = dict_ret["sftp_lecture"]
    param_config = {}
    for param in L_ret:
        param_config = param.copy()
    print("- Lecture de la configuration en lecture " + path_in + ".")
    return param_config

# Commande à exécuter

## Téléchargement d'un fichier depuis le SFTP vers un emplacement local
def execute_download(username="username", password="password", sftp_host="sftp_host"):
    print('--- Lancement de la commande wget')
    dst = "/"
    username = username
    password = password
    sftp_host = sftp_host
    filepath = "doctolib/2021-11-03-doctolib-rdv.csv"
    cmd = 'wget --directory-prefix='+dst+' --user="'+username+'" --password="'+password+'"  ftp://'+sftp_host+'/'+filepath+' --progress=bar'
    subprocess.run(cmd, shell=True)
    print(' - Commande "'+cmd+'" exécutée')

param_config = read_config_lecture("test_config.json")
execute_download(username=param_config["username"], password=param_config["password"], sftp_host=param_config["sftp_host"])
