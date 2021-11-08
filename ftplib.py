# coding: utf-8

# Modules par défaut à importer
import re
import os
import ntpath
import sys
import time
import json
from tqdm import tqdm
from glob import glob

# Modules à installer avant la publication
import ftplib
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, ProgressBar, ReverseBar, RotatingMarker, SimpleProgress, Timer, UnknownLength

# Lecture de la configuration du serveur SFTP avec le compte en écriture
def read_config_ecriture(path_in):
    print("--- Lancement de la lecture de la configuration du serveur en écriture")
    with open(path_in) as f:
        dict_ret = json.load(f)
    L_ret = dict_ret["sftp_ecriture"]
    param_config = {}
    for param in L_ret:
        param_config = param.copy()
    print("Lecture de la configuration en écriture "+ path_in + ".")
    return param_config

# Commande à exécuter

global ftp

## Publication d'un fichier local sur le SFTP
def execute_upload(username="username", password="password", sftp_host="sftp_host"):
    print('--- Lancement de la publication via ftplib')
    username = username
    password = password
    sftp_host = sftp_host
    ftp = ftplib.FTP(sftp_host, username, password)
    local_file = '2021-11-03-doctolib-rdv.csv'
    size_local_file = os.path.getsize(local_file)
    file_to_transfer = open(local_file, 'rb')
    with tqdm(unit = 'blocks', unit_scale = True, leave = True, miniters = 1, desc = 'Uploading......', total = size_local_file) as tqdm_instance:
        ftp.storbinary('STOR ' + local_file, file_to_transfer, 2048, callback = lambda sent: tqdm_instance.update(len(sent)))
        file_to_transfer.close()
    #with open(local_file, 'rb') as file_to_transfer:
        #ftp.storbinary(f"STOR {local_file}", file_to_transfer)
    ftp.quit()
    ftp = None
    print(' - Publication exécutée')

param_config = read_config_ecriture("test_config.json")
execute_upload(username=param_config["username"], password=param_config["password"], sftp_host=param_config["sftp_host"])
