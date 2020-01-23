# Configuration BeagleBone Black (BBB)

![alt Beaglebone](../images/bbb.jpg)

## 

## Lecture des données de l'Arduino

Le script read_send.py permet de lire les données envoyées depuis le port série 1 de 
l'Arduino. Lorsque le script s'exécute, les données au format JSON sont lues en permanence 
jusqu'à ce que le symbole '}' apparaisse, méthode read_until() de la classe Serial.
Lorsque que ce symbole apparaît, on a alors reçu une trame de la forme
``` { Temperature : 26.25, Altitude : 12.0 ... } ```
que l'on convertit du type bytes vers une chaîne de caractères, méthode decode().

