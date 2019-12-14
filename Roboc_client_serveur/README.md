<h1>Instructions</h1>

<p>Votre mission est de reprendre le code du labyrinthe d&eacute;velopp&eacute; &agrave; la partie pr&eacute;c&eacute;dente : <em>Roboc</em>. Vous devrez y ajouter les fonctionnalit&eacute;s suivantes :</p>
<ul>
<li>On ne doit plus jouer au jeu en console. &Agrave; la place, le jeu doit &ecirc;tre une <strong>application serveur</strong>. Il faut &eacute;galement cr&eacute;er <strong>les applications clients</strong> pour <strong>jouer &agrave; plusieurs</strong> au labyrinthe. Chaque joueur aura son propre robot. Au lieu de le placer &agrave; un endroit pr&eacute;cis sur la carte, il appara&icirc;tra <strong>al&eacute;atoirement</strong> ;</li>
<li>Le jeu multi-joueurs se jouera au <strong>tour par tour</strong>, chaque robot faisant un seul mouvement par tour. Le joueur pourra toujours demander au robot d'aller trois fois vers l'est, par exemple, mais le jeu ne fera bouger le robot qu'une fois avant de demander le coup de l'autre joueur ;</li>
<li>Le jeu doit inclure une <strong>s&eacute;rie de tests unitaires</strong> qui permettront de valider son fonctionnement. Les tests doivent v&eacute;rifier la constitution d'un labyrinthe standard, la cr&eacute;ation d'un labyrinthe depuis une cha&icirc;ne et les fonctionnalit&eacute;s du jeu multi-joueurs ;</li>
<li>Les robots peuvent maintenant <strong>murer des portes</strong> (changer une porte en mur) ou <strong>percer une porte</strong> dans un mur. Pour ces deux fonctionnalit&eacute;s, il faudra cr&eacute;er deux nouvelles commandes, voir le d&eacute;tail plus bas.</li>
</ul>
<h3>&nbsp;</h3>
<h3>Contr&ocirc;le du robot</h3>
<p>Le syst&egrave;me est un peu plus compliqu&eacute; en interne, mais en pratique c'est la m&ecirc;me chose : <strong>le client peut envoyer des commandes au serveur pour d&eacute;placer le robot</strong>. Les commandes sont identiques pour se d&eacute;placer. On ajoute &eacute;galement :</p>
<ul>
<li>La commande <em>m</em> pour <strong>murer une porte</strong> suivie de la lettre repr&eacute;sentant la direction. Par exemple, la commande <em>me</em> demandra au robot de murer la porte qui se trouve juste &agrave; c&ocirc;t&eacute; &agrave; l'est. <em>Murer</em> transforme tout simplement une porte en mur, pi&eacute;gant le robot adverse dans la pi&egrave;ce, temporairement du moins ;</li>
<li>La commande <em>p</em> pour <strong>percer une porte</strong> dans un mur. Cette commande est &eacute;galement suivie de la lettre repr&eacute;sentant la direction. Par exemple <em>pn</em> cr&eacute;e une porte dans le mur se trouvant juste au nord.</li>
</ul>
<h3>&nbsp;</h3>
<h3>Affichage du labyrinthe</h3>
<p>L'affichage doit &ecirc;tre identique. Cette fois, c'est le serveur qui g&egrave;re r&eacute;ellement les d&eacute;placements et commandes et qui envoie le nouveau labyrinthe au client apr&egrave;s avoir jou&eacute;. <strong>Le serveur doit envoyer le nouveau labyrinthe &agrave; tous les clients</strong> pour que chacun voie les coups des adversaires. Vous pourrez voir un extrait de console (du serveur et d'un client) plus bas.</p>
<p>Notez cependant qu'il y a une diff&eacute;rence, puisque plusieurs robots doivent &ecirc;tre visibles dans le labyrinthe. Il vous faut trouver un moyen de <strong>diff&eacute;rencier son propre robot de ceux des adversaires</strong>.</p>
<h3>&nbsp;</h3>
<h3>Fonctionnalit&eacute;s du jeu</h3>
<p>Les fonctionnalit&eacute;s du jeu sont identiques &agrave; celles propos&eacute;es dans la version pr&eacute;c&eacute;dente, hormis les modifications indiqu&eacute;es. Notez cependant que, cette fois-ci, <strong>il n'est pas utile d'enregistrer les parties</strong> : les rejouer demandrait que tous les clients se reconnectent et ce serait un peu difficile &agrave; g&eacute;rer.</p>
<h3>&nbsp;</h3>
<h3>Au lancement du programme</h3>
<p>On doit <strong>lancer le serveur en premier</strong>. On doit <strong>pr&eacute;ciser la carte</strong> (comme on le faisait auparavant) dans le serveur. Une fois la carte choisie,<strong> les clients peuvent se connecter</strong>.</p>
<p>Le ou les client(s) doi(ven)t &ecirc;tre lanc&eacute;(s) une fois la carte s&eacute;lectionn&eacute;e. Un nouveau robot sera cr&eacute;&eacute; automatiquement et plac&eacute; dans le labyrinthe pour chaque client qui se connecte <strong>tant que la partie n'a pas commenc&eacute;</strong>. Notez que des cartes ind&eacute;pendantes pourront &ecirc;tre propos&eacute;es par la suite, mais ce n'est pas dans la liste de vos objectifs actuels.</p>
<p><strong>Chaque robot sera plac&eacute; al&eacute;atoirement sur la carte</strong> : pour ce faire, le plus simple est de s&eacute;lectionner al&eacute;atoirement une case vide (sans obstacle ni autre robot d&eacute;j&agrave; plac&eacute;). Notez que cela pourra donner des parties assez courtes, si un robot est plac&eacute; al&eacute;atoirement tout pr&egrave;s d'une sortie. L&agrave; encore, il pourra &ecirc;tre utile par la suite de faire en sorte que le placement soit relativement &eacute;quilibr&eacute;, mais ce n'est pas n&eacute;cessaire pour l'heure.</p>
<p>Enfin, quand suffisamment&nbsp;de clients se sont connect&eacute;s, n'importe quel client pourra <strong>entrer la commande <em>c</em> pour <em>commencer</em> la partie</strong>. Cette commande ne pourra &ecirc;tre utilis&eacute;e qu'<strong>une fois</strong>. Une fois la partie commenc&eacute;e, de nouveaux clients ne pourront pas s'y joindre.</p>
<h3>&nbsp;</h3>
<h3>Petite pr&eacute;cision c&ocirc;t&eacute; client</h3>
<p>Le client est un peu plus difficile &agrave; mettre en place dans le sens o&ugrave; il doit &agrave; la fois <strong>demander au joueur d'entrer des commandes et &eacute;couter le serveur pour des r&eacute;ponses</strong>. En th&eacute;orie, il est possible de ne demander des commandes &agrave; l'utilisateur que quand son tour est venu de jouer. En pratique, cela est peu souhaitable et vous pourriez &agrave; terme mettre en place des commandes sp&eacute;cifiques (par exemple pour&nbsp;parler &agrave; tous les joueurs de la partie). Ce type de commande n'a pas besoin d'attendre le tour du joueur.</p>
<p>Pour attendre &agrave; la fois des commandes de l'utilisateur et &eacute;couter les r&eacute;ponses du serveur, il peut &ecirc;tre utile d'<strong>utiliser la programmation parall&egrave;le</strong>. Ce n'est pas la seule solution mais c'est celle qui reste la plus expliqu&eacute;e dans ce cours. Libre &agrave; vous d'impl&eacute;menter cette fonctionnalit&eacute; autrement si vous le d&eacute;sirez.</p>
<h3>&nbsp;</h3>
<h3>Vous serez not&eacute;s sur</h3>
<ul>
<li>Le fait d'arriver &agrave; <strong>d&eacute;velopper les fonctionnalit&eacute;s de l'exercice</strong> : si l'on peut lancer vos programmes (serveur et client) et qu'ils tournent sans modification, vous aurez la note maximale, peu importe le code source derri&egrave;re ;</li>
<li>La <strong>lisibilit&eacute; du code</strong> : votre code source doit &ecirc;tre aussi agr&eacute;able &agrave; lire que possible. Les noms de vos variables, fonctions, classes, modules doivent &ecirc;tre coh&eacute;rents. La pr&eacute;sentation de votre code source ne suit pas une r&egrave;gle sp&eacute;cifique, mais elle doit &ecirc;tre coh&eacute;rente (si vous faites un choix de nommage dans un module, faites le m&ecirc;me choix dans un autre) ;</li>
<li>Le <strong>d&eacute;coupage de votre projet</strong> : essayez de bien r&eacute;fl&eacute;chir &agrave; la fa&ccedil;on dont vous d&eacute;couperez votre projet. Les fonctions, classes, modules et &eacute;ventuellement packages formeront la structure de votre projet. Puisque votre code supportera deux applications, veillez &agrave; bien r&eacute;fl&eacute;chir aux fonctionnalit&eacute;s qui seront partag&eacute;es par les deux ;</li>
<li>La <strong>documentation de votre code</strong> : indiquez de loin en loin des commentaires et documentations (sous forme de docstring, pour vos classes et fonctions), afin de rendre votre code plus compr&eacute;hensible pour quelqu'un qui le regarde ;</li>
<li>La <strong>pertinence des tests</strong> : vos tests doivent &ecirc;tre fonctionnels et utiles. Il ne faut pas seulement qu'ils fonctionnent, il faut qu'ils prouvent que le programme peut tourner correctement ;</li>
<li>L'<strong>ouverture &agrave; l'am&eacute;lioration</strong> : ce dernier point est donn&eacute; quand votre code est aussi s&eacute;par&eacute; que possible et permettrait sans difficult&eacute; des modifications, comme l'ajout d'autres obstacles dans le labyrinthe, l'utilisation de cartes 3D avec des escaliers pour circuler de niveau en niveau, l'utilisation d'un affichage graphique avec l'une des biblioth&egrave;ques existantes, l'int&eacute;gration de caract&eacute;ristiques (la vie et le mouvement) aux robots, la cr&eacute;ation de nouvelles commandes, la cr&eacute;ation d'outils, etc. Si votre code est bien hi&eacute;rarchis&eacute;, l'am&eacute;lioration est g&eacute;n&eacute;ralement plus simple. <strong>Notez bien que vous n'avez pas &agrave; coder ces fonctionnalit&eacute;s, juste &agrave; garder en t&ecirc;te que votre programme pourrait &eacute;voluer par la suite.</strong></li>
</ul>
<p>&nbsp;</p>
<h3>Exemples de retour</h3>
<p>Vous trouverez ci-dessous&nbsp;ce qu'on pourrait voir en ex&eacute;cutant le programme. Notez que :</p>
<ul>
<li>Les symboles utilis&eacute;s sont O pour un mur, . pour une porte (sur laquelle le robot peut passer), U pour la sortie et X pour le robot lui-m&ecirc;me ;</li>
<li>Dans l'exemple ci-dessous, on lance le serveur puis deux clients. Les diff&eacute;rents retours sont clairement identifi&eacute;s ;</li>
<li>Quand le robot passe une porte, elle devient invisible et s'affiche de nouveau quand le robot est pass&eacute; ;</li>
<li>Le robot ne peut pas passer &agrave; travers les murs ;</li>
<li>Les robots adverses sont not&eacute;s en minuscule <em>x</em> ;</li>
<li>L'exemple ci-dessous est un exemple de la carte <em>facile</em>.</li>
</ul>
<p>&nbsp;</p>
<p><strong>C&ocirc;t&eacute; serveur</strong></p>
<pre>python serveur.py
Labyrinthes existants :
  1 - facile.
  2 - prison.
Entrez un num&eacute;ro de labyrinthe pour commencer &agrave; jouer : 1
On attend les clients.
</pre>
<p><strong>Connexion du client 1</strong></p>
<pre>On tente de se connecter au serveur...
Connexion &eacute;tablie avec le serveur.
Bienvenue, joueur 2.<br />
OOOOOOOOOO
O O    O O
O . OO   O
O O O x XO
O OOOO O.O
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO


Entrez C pour commencer &agrave; jouer :
c
La partie commence !<br />
OOOOOOOOOO
O O    O O
O . OO   O
O O O X xO
O OOOO O.O
O O O    U
O OOOOOO.O
O O      O
O O OOOOOO
O . O    O
OOOOOOOOOO

</pre>
<p><strong>Le <em>joueur 1</em> peut ensuite jouer (un message l'informe que c'est son tour) et entrer les commandes comme il le faisait auparavant. Quand le jeu est fini (l'un des robots a atteint la sortie), les clients sont d&eacute;connect&eacute;s.</strong></p>
<p>&nbsp;</p>
<h3>&Agrave; inclure dans votre correction</h3>
<p>Vous devrez proposer en correction un fichier <em>zip</em> qui devra contenir :</p>
<ul>
<li><strong>L'ensemble de votre code source</strong>. L'application serveur (&agrave; ex&eacute;cuter en premier) doit s'appeler <em>serveur.py</em> et doit se trouver &agrave; la racine de votre code source. L'application client (&agrave; ex&eacute;cuter apr&egrave;s, autant de fois que de client &agrave; connecter) doit s'appeler <em>client.py</em> et se trouver au m&ecirc;me endroit ;</li>
<li><strong>Une liste des cartes</strong> propos&eacute;es par le programme. Le plus simple reste de cr&eacute;er un dossier <em>cartes</em> dans lequel se trouve les cartes. L&agrave; encore, le programme fourni doit &ecirc;tre capable de les trouver sans modification du code ;</li>
<li><strong>Les tests unitaires</strong>, pr&eacute;sents dans un sous-dossier <em>test</em>. Notez qu'il doit &ecirc;tre possible de lancer tous les tests unitaires en entrant simplement <em>python -m unittest</em> &agrave; la racine du projet.</li>
</ul>
<p>&nbsp;&Agrave; vous de jouer !&nbsp;</p>
