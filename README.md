# Tic-Tac
Jeu de tic-tac avec arnold. Il s'agit du premier projet d'une serie qui va du 18/11/2018 au 30/11/2018.
La description du jeu sera donnée dans la suite.

Il s'agit d'une version du jeu de tic tac mais avec 9 tableaux de jeux, chaque tableau ayant 3x3 cases.
Le jeu se termine lorsque un des joueurs a reussi à aligner 3 de ses pions que ça soit en diagonale ou en lignes, ou meme en colonne dans le cas contraire,il d'agit d'un match nul.

Ce qu'il faut faire en vrac:
<ul>
  <li> Le jeu doit pouvoir se jouer human-human, human-machine, machine-machine</li>
  <li> concevoir une IA pour jouer selon minmax</li>
  <li> Gerer des niveaux de difficultés</li>
  <li> faire une version graphique et reseau</li>
  <li> gerer un BD des joueurs</li>
</ul>
Pour ce faire, nous avons choisi d'implementer d'abord un tic tac 3x3 comme brique de base du tic tac 9x9.
  En particulier pour ce qui est de L'IA, nous alons ecrire un algorithme selon minimax qui sera chargé de jouer le coup le meilleur en fonction de l'evalution de l'etat de la partie courante.    
  
