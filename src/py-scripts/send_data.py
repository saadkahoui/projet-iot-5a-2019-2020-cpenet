#!/usr/bin/python3

import time
import requests
import math
import random
import json
import sys
import datetime
from time import gmtime, strftime


TOKEN = "BBFF-zU1sDkpDi5bSt0ncLOOBDGQyCoaUWn"  # Put your TOKEN here
DEVICE_LABEL = "cpenet"  # Put your device label here 
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here
VARIABLE_LABEL_2 = "altitude"  # Put your second variable label here
VARIABLE_LABEL_3 = "pression"  # Put your second variable label here
VARIABLE_LABEL_4 = "humidite"
VARIABLE_LABEL_5 = "feu"
filename = 'log.txt'

def build_payload(variable_1, variable_2, variable_3,variable_4,variable_5):
    
    # On recupere les donnees passees en argument
    data = sys.argv

    # On separe chaque donnee
    temperature = data[1]
    altitude = data[2]
    pression = data[3]
    humidite = data[4]
    feu = data[5]


    # on cree le paquet de donnees a envoyer
    payload = {variable_1: temperature,
               variable_2: altitude,
               variable_3: pression,
               variable_4: humidite,
               variable_5: feu}

    return payload


def post_request(payload):
    # Cree l'entete pour la requette HTTP
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Fais la requette HTTP
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, data=json.dumps(payload))
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Si erreur
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] Requette correcte, les informations sont mises à jour")
    return True

def write_log(temperature,pression,altitude,humidite,feu):

    # On garde un historique en écrivant les donnees et l'heure dans un fichier de logs
    date_temps =str(datetime.datetime.now()).split('.')
    # print(type(temperature))
    temp = format(float(temperature),'.2f')
    alti= format(float(altitude),'.2f')
    humi = format(float(humidite),'.2f')
    press = format(float(pression),'.2f')
    

    string_log =  date_temps[0] + '\tTemperature ' + temp + '\t| Altitude : '+ alti +'\t| Pression : '+ press + '\t| Humidite : '+ humi + '\t| Feu : '+ str(feu)+ '\n'
    log = open(filename,'a')
    # Ecriture dans le fichier
    log.write(string_log)
    # Fermeture du fichier
    log.close()

def main():

    payload = build_payload(
        VARIABLE_LABEL_1,VARIABLE_LABEL_2,VARIABLE_LABEL_3,VARIABLE_LABEL_4,VARIABLE_LABEL_5)
#    print (payload)
    print("[INFO] Envoi des donnees")
    post_request(payload)
    print("[INFO] Fin")
    # On log les actions effectuees
    write_log(payload['temperature'],payload['altitude'],payload['pression'],payload['humidite'],payload['feu'])
    

if __name__ == '__main__':
#    while (True):
    main()


