# OpenClassrooms

Votre mission est de concevoir et développer un petit jeu permettant de contrôler un robot dans un labyrinthe. Ce jeu devra être développé en console pour des raisons d'accessibilité. Je l'ai appelé... Roboc.

Le jeu est un labyrinthe formé d'obstacles : des murs qui sont tout simplement là pour vous ralentir, des portes qui peuvent être traversées et au moins un point par lequel on peut quitter le labyrinthe. Si le robot arrive sur ce point, la partie est considérée comme gagnée.

 
Contrôle du robot : 

Le robot est contrôlable grâce à des commandes entrées au clavier. Il doit exister les commandes suivantes :

    Q qui doit permettre de sauvegarder et quitter la partie en cours ;
    N qui demande au robot de se déplacer vers le nord (c'est-à-dire le haut de votre écran) ;
    E qui demande au robot de se déplacer vers l'est (c'est-à-dire la droite de votre écran) ;
    S qui demande au robot de se déplacer vers le sud (c'est-à-dire le bas de votre écran) ;
    O qui demande au robot de se déplacer vers l'ouest (c'est-à-dire la gauche de votre écran) ;
    Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 pour avancer de trois cases vers l'est).

 
Affichage du labyrinthe

Le labyrinthe est vu du dessus. Un symbole représente un obstacle ou votre propre robot. Vous pouvez vous référez à l'exemple ci-dessous pour voir quelques exemples de partie.

Pour reconnaître la nature des obstacles, on doit bien évidemment représenter chaque obstacle par un symbole différent. Sans quoi, difficile de différencier les murs des portes de sorties.

 
Fonctionnalités du jeu

Le jeu doit :

    Enregistrer automatiquement chaque partie à chaque coup pour permettre de les continuer plus tard ;
    Proposer plusieurs cartes faciles à éditer. Chacune des cartes disponibles se trouvera dans un fichier avec l'extension txt dans un dossier particulier. Il sera donc facile d'ajouter, supprimer ou modifier des cartes. Vous pourrez télécharger les cartes par défaut plus bas.

 
Au lancement du programme

La première chose à faire est de trouver les cartes existantes, conservées dans nos fichiers txt, de les charger et de vérifier qu'une partie n'était pas en cours. Si une partie est en cours, proposer de rejouer cette partie (consultez l'exemple de jeu plus bas).

Choisir une carte lance la partie. La même chose se produit si vous demandez à jouer une partie déjà existante, s'il en existe une. À chaque tour, le labyrinthe est réaffiché avec la position de chaque obstacle et la position du robot.
