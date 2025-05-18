# Labyrinthe

![image](https://github.com/user-attachments/assets/4af73e75-791f-41cd-ae67-132728abe802)


# Algorithme
1) Le Robot va longer le mur de droite. 
 
2) Algorithme de Pledge, Il permet de sortir d’un labyrinthe en suivant un mur tout en gardant une direction de référence. Il utilise un compteur d’angles pour savoir quand reprendre cette direction dès que l'obstacle est contourné.

(Dans les deux cas le robot avancera dans le labyrinthe en stockant le temps et les directions dans les quelles il tourne pour les envoyés dans un payload à un second robot qui refera le même chemin avec une plus grande vitesse) 
 
=> Implémentation de l'échange avec un autre robot pas terminée par manque de temps et place dans la microbit :(

# Librairies

maprincess  https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main 
(Minifier avec https://pyminifier3.readthedocs.io/en/latest/)
 
protocole   https://gitedu.hesge.ch/info_sismondi/oc-robotique/-/tree/main/Protocole
