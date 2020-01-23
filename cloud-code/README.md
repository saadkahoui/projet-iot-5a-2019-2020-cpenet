# Configuration Passerelle - Cloud

Ce code est utilisé pour envoyer les données recues sur le Raspberry Pi vers Ubidots.
<br/>
Pour plus de simplicité, et pour ne pas avoir à toucher au code, il faut passer en argument de ce code les 5 variables récupérees.
Lorsque que vous créez votre espace Ubidots, il est necessaire de changer le TOKEN, présent en haut du code, par celui propre à votre compte.

Afin d'assurer une tracabilité, les donneés envoyées sont sauvegardées dans un fichier de logs : 'logs.txt', grâce à la fonction  write_log.

Ce script est ensuite appellé par le script read_send.py, qui recupere les données de l'arduino et appelle ce programme ci en passant en argument les données.

