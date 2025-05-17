# Labyrinthe

# Algorithme
Après avoir essayé et échoué d'appliquer une méthode de résolution qui se basait sur "simplement" suivre le mur de gauche/droite, nous voulions essayé de utilisé une méthode basé sur un autre algorithme créé par Pledge. En effet, l'algorithme de Pledge est bien connu pour la résolution de labyrinthes et nous avons déjà confirmer sa faisabilité dans le labyrinthe imprimé dans le cours. 

Ce que ce code fait c'est de basiquement compter les virages/angles : + ou - quand on tourne à gauche ou à droite. Quand le compteur atteint 0, le robot suit une ligne droite jusqu'à atteindre le mur. Nous avons essayé d'implémenter ça ici. Voici la première version de teste.

# Librairies

maprincess  https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main 
(Minifier avec https://pyminifier3.readthedocs.io/en/latest/)
 
protocole   https://gitedu.hesge.ch/info_sismondi/oc-robotique/-/tree/main/Protocole
