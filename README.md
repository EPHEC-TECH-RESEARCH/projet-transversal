# ephec-rpi

Vous trouverez ici des exemples ainsi que certaines informations utiles pour les ateliers Raspberry Pi du projet Transversal (1T Ephec).

## Ressources utiles:
- Formation groupes : [lien formation groupe](https://ephec.sharepoint.com/:x:/r/sites/Projettransversal2025/_layouts/15/Doc.aspx?sourcedoc=%7B731BDD96-0292-44ED-B424-74DCF24D171E%7D&file=Projet%20transversal%202025%20Etudiants.xlsx&action=default&mobileredirect=true)
- [Teams](https://teams.microsoft.com/l/channel/19%3AApZFu9Z_XcjK-wj33KfWrv3_XhxLgSGDhwzREq3Ekdg1%40thread.tacv2/?groupId=0672944d-af5e-44ff-bfb0-c73e93ac0139&tenantId=21936fc0-be19-4e1b-ad89-4def5c23b4cb) (communications lors des séances plus communications informelles): "projet transversal" dans votre Teams
- Mail pour les communications officielles
- Détails techniques pour la [LED RGB](https://github.com/EPHEC-TECH-RESEARCH/projet-transversal/blob/main/LED%20RGB%20d%C3%A9tails%20techniques.pdf)
- Exemples de code/ résolution d'exercices (par Séance + d'autre pas classé): les dossiers 'exemples' et 'exemples_old' de ce repository
- librairie python pour utilisation des gpio: https://gpiozero.readthedocs.io/en/stable/
- Une 'Cheat Sheet' qui n'a peut etre pas été finie/imprimé, mais dont les éléments la constituant se trouvant dans le dossier 'Cheat Sheet' de ce repository.
- intro au python (vous n'aurez pas besoin de grand chose): https://wiki.python.org/moin/BeginnersGuide/Programmers
==> mais beaucoup de choses existent sur internet, n'hésitez pas à chercher

## Connection au Raspberry Pi

* Leur hostname est :  écrit sur leur carte SD et aurra la forme `pi[numero_unique]`, par exemple `pi06`
* Leur username est : `pi`
* Leur password est : `ephec` (vous pouvez le changer, mais on ne pourra pas vous aider si vous oubliez le nouveau)

Une fois votre Raspberry allumé et branché avec un câble réseau (dans votre ordi ou dans le switch), vous pouvez vous y connecter (en ssh), soit:
* En utilisant juste son hostname: ex: `ssh pi@pi10` (il se connectera en IPv6 en utilisant le protocole de *neighbours discovery*)
* Si le routeur + switchs (+ wifi ?) sont déjà en place (à partir du deuxième atelier), il y aura un serveur DHCP (avec un accès internet) et vous pourez aussi (pas obligatoire) utiliser l'IPv4 du Raspberry. Ex: `ssh pi@192.168.20.242` (note: l'ip commencera toujour par *192.168.20._ *)

==> Votre raspberry pi **ET** votre ordinateur doivent être branché sur le routeur/switch. 
Pour trouver l'adresse IP de votre Raspberry Pi, le plus simple, c'est de demander à quelqu'un d'autre (par exemple un autre groupe ? Tant qu'il est branché au switch ...), d'utiliser la méthode 1 pour vous récuperer son IP (note: pour connaitre les addresses IP sur Linux, il suffit de taper `ip a`)


> Note sur le wifi: **Si** il y a une connection wifi, elle sera probablement pas stable (car beaucoup d'interférences et pas prévue pour supporter beaucoup de connections simultanées) ==>  Evitez donc de l'utiliser autant que possible et, si vous devez l'utiliser, limitez le trafique !   Cette connection wifi peu avoir du sens pour accèder, depuis votre téléphone, à la page web que vous aurez construite ou si **vraiment** vous n'avez **absolument** pas d'autre solution pour brancher votre ordinateur avec un cable.

#### Autre Passwords
* wifi (si il y en a) : `ephecephec`


## Choses à upgrader/installer sur le raspberry pi si pas présent 
Remarque : il faut être connecté à Internet pour que cela fonctionne
```
sudo su
apt update
apt dist-upgrade -y
apt install -y python3-pip  git tmux vim bpython
pip install Flask
```

## Conseils
- [une fois tmux installé] lancez tmux dès que vous êtes connecté, ainsi si vous perdez la connection, vous pourrez, en vous reconnectant, tapper `tmux a`, et revenir là où vous étiez.
- [une fois git installé] vous pouvez faire un `git clone https://github.com/EPHEC-TECH-RESEARCH/projet-transversal.git` pour récupérer tout ce repository (ainsi que les exemples)
- les erreurs python sont vite arrivées et la coloration syntaxique est très utile: soit codez sur votre ordinateur (dans un IDE) et copiez sur votre raspberry pi (ex: avec nano) ou bien vous pouvez aussi utiliser vim
- avant d'éteindre le Raspberry, tapez la commande sudo shutdown now et attendez que la LED verte ait fini de clignoter


## Déroulement des séances
### Séance 1 (vendredi 14 février 2025)
Intro au Python, au Raspberry Pi. Allumage d'une led ainsi que l'utilisation d'un bouton poussoir.
Des exemples de code sont disponible dans le directory "exemples par scéance".
Ressource utile: https://gpiozero.readthedocs.io/en/stable/ ( + google ;)

### Séance 2 (vendredi 21 février 2025)
* (Possible: Utilisation des Microtik )
* Installation de certaines choses sur votre Rpi (tel que Flask)
* Intro à Flask: création d'un serveur Web + un peu plus de Python
* Approfondissement de l'utilisation de gpiozero + quelques notions supplémentaire sur les rpi et l'électronique


Note : Une difficultée de cette séance est de devoir gérer le serveur Web en même temps, ce qui implique que la partie 'electronique' du code ne peux pas bloquer la partie Web...


Note: il n'y a pas que la difficulté de 'faire marcher' le capteur, il y a aussi la difficulté lié à votre senario.  
Ex: une led n'est pas compliqué, mais afficher un nombre en binaire l'est plus... Un bouton n'est pas compliqué, mais une mini calculatrice l'est plus, ... 

### Séance 3 (vendredi 21 mars 2025)
* Quelques nouveaux capteurs sont introduit
    * codeur rotatif 
    * capteurs proximité 
    * servo moteur
    * buzzer 
    * capteurs température (à confirmer)
    * Et d'autres ...
* Définition et travail sur votre projet

### Séance 4 (vendredi 4 avril 2025)
- Travail sur votre projet
- Présentation / Jury


# Capteurs 
Pour la troisième séance, vous avez accès à beaucoup plus de capteur afin de réaliser votre projet.

Parmi les capteurs à disposition, je les mettrais en 3 catégories: 
1. Les "conseillés" ==> ils sont 'relativement' simple, et marchent avec gpiozero (aller voir les exemples et les montage sur le site de gpiozero!)
2. les "challenging" ==> ils sont testé, du code est a disposition, mais gpiozero ne suffira pas, il faudra utiliser 'pythonCircuit', heureusement des cartes SD avec tout installé sont dispo) 
3. les "hardcore" ==> pas de code fourni, probablement qu'ils vous faudra installer des choses supplémentaire et on ne pourra vous fournir qu'une aide limité (en fonction de la disponibilité)

J'en oublie peut-etre, mais voici les capteurs disponible par catégorie:
1. Consseilé :
- Boutton and co  ==> il y a beauchoup de capteurs qui se comportent comme des boutons et sont très simpa à utiliser (genre le tilt sensor)
- LED (notement qq RGB)
- buzzer
- Capteur de lumière
- Capteur de distance
- Capteur de mouvement
- servo moteur
- encodeur rotatif
- relay ?  (pas compliqué, mais necessite un autre appareil à controler)

2. Challenging
- Capteur de températeur et humidité
- Capteur de pression et d'altitude
- Certains autre capteurs fourni dans le boite de découverte de capteurs
- 7 segment unique

3. Hardcore
- Recepteur Infra rouge
- emeteur-recepteur 433 Mhz
- multiple 7-segment
- controleur de moteur
- ... et le reste des capteurs random dispo


## Quelques info sur les capteurs à disposition (note: info pas mise à jour et incomplete)
# Le codeur rotatif
[wikipedia] "Un codeur rotatif ou capteur rotatif est un type de capteur permettant de fournir une information d'angle, en mesurant la rotation effectuée autour d'un axe.

L'information de vitesse peut alors être déduite de la variation de la position par rapport au temps. Plus le codeur rotatif tourne lentement, plus la déduction de vitesse perd en précision."

Les codeurs rotatif disponible ont 4 pin alors que dans l'exemple de 'gpio zero' il n'y en a que 3: c'est parceque ceux-ci ont également un bouton integré: c'est la pin nommée 'sw'.  Les pins nomées 'Data' et 'Clk' peuvent être inter-changé (ça influera sur la détermination du sens de rotation concidéré comme sens positif).

# Le Servo moteur
Le fil rouge est pour le vcc (en 5v), le brun est le Ground (0v) et le jaune est le signal (celui qui doit aller sur votre GPIO)  
Note: il y en a moins disponible

# Le capteur "nivau d'eau/floteur"
Il se comporte comme un button.  Lorsque l'eau soulève le floteur le circuit est fermé.
