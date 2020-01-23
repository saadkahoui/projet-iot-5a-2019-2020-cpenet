# Projet IoT
## Équipe

Dylan Synault (Chef de projet)<br />
Nicolas BOSIA<br />
Jérémy ROQUIN<br />
Saad KAHOUI<br />
Mehdi LARIBI<br />

## Description du Projet

Le projet de l'équipe CPE-NET est la création d'un système IOT pour la detection et l'anticipation des incendies. Ce projet utilise plusieurs capteurs 'click' ainsi qu'un Arduino Mega et un RaspberryPi.<br />
<br />
Notre idée originale était d'utiliser une communication GSM entre l'arduino et le Raspberry, en y implémentant OpenBTS.<br />
Par manque de temps et à cause de problèmes techniques, nous n'avons pas reussi à faire fonctionner cette liaison.<br />
Ainsi, et afin d'avoir une chaine de transmission complète, nous avons pour l'instant connecté le Raspberry et l'arduino par une liaison série.<br />
<br />
Voici ci-dessous un schéma de fonctionnement du projet. <br />
<br />

![alt text](https://github.com/CPELyon/projet-iot-5a-2019-2020-cpenet/blob/master/images/iot.png)

### Capteurs

Nous utilisons un capteur 'météo' qui relève des données d'humidité, de température, de pression et d'altitude, ainsi qu'un detecteur de flamme.<br />

### Cas d'utilisation

L'idée serait de placer l'arduino équipé des capteurs dans une forêt (sur un arbre par exemple) et alimenté d'une batterie.
Ainsi, le système enverrait des données au raspberry,qui est connecté à internet, et qui transmets les données à la plateforme qui les récolte : Ubidots.
Ce système a pour vocation de détecter les incendies et les conditions favorables à un départ d'incendie afin d'agir de facon proactive.
Si le système détecte une température trop elevée ainsi qu'une humidité très faible, il est capable de prévenir, via l'interface ou un mail d'alerte, qu'il y a potentiellement des risques d'incendie dans la zone du capteur.

## Répartition des tâches

### Suivi journalier

## Procédure de mise en place de votre chaîne IoT

## Conclusions et recommandations
