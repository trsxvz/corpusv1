Répertoires :
- 'intranet' correspond aux documents internes publics auprès des élèves (règlement des études, maquettes pédagogiques à jour, etc)
- 'polytech.sorbonne-universite.fr' correspond au site web de Polytech sorbonne. l'agencement du répertoire suit la structure web du site pour que l'on s'y retrouve mieux, mais il faudra probablement regrouper tous les .jsonl dans un seul et même dossier pour l'embedding.
d'autres répertoires seront éventuellement ajoutés dans le futur (site Polytech global, site S-U,...)

Structure :
- La structure des répertoires essaie de s'approcher le plus possible de l'agencement réel du site, mais a parfois dû être modifiée pour éviter les redondances ou pour s'adapter aux différentes structures des pages. Toute l'information textuelle pertinente a néanmoins été conservée.

Avancement :
- La partie spécifique des filières (onglet "formations" du site polytechsorbonne) reste à traiter.
- La partie spécifique des entreprises (onglet "entreprises" du site polytechsorbonne) reste à traiter.
- Les documents de l'intranet restent à traiter.

Fichiers :
- 'readme.txt' est le présent fichier explicatif
- 'script-extraction-v1.py' est un script python utilisant la librairie beautifulsoup pour extraire les infos d'une page web. Il est pratique mais il faut tout de même gérer certaines choses manuellement, comme par exemple les metadata, la bonne répartition du texte, les url à extraire des hyperliens,...)

Courte explication de la manière dont on a stocké les données :

On a opté pour un format .jsonl (JSON Lines) où chaque ligne correspond à un fichier JSON.
L'avantage par rapport au .txt est la possibilité d'agencer le texte et d'attribuer des metadonnées.
L'avantage par rapport au .csv est la capacité à traiter correctement des textes relativement longs.
L'avantage par rapport au .pdf est une bien meilleure structuration (les pdf sont structurés graphiquement plutot que logiquement)
L'avantage par rapport au .json classique est multiple :
- réduire le nombre de fichiers puisque chaque ligne du jsonl correspond à un json
- structure jsonl particulièrement bien adaptée aux pages web divisées en plusieurs rubriques
- facilité de représentation humaine : chaque fichier correspondant à une page web, on s'y retrouve facilement

Choix des metadata :

Certaines metadonnées se révèlent peu utiles dans notre contextes :
- L'auteur d'une publication import peu puisque l'ensemble vient de toute manière de polytech
- La date de publication et d'édition n'importe pas beaucoup plus, mais peut parfois être utile :

Les metadata les plus importantes sont en réalité celles de structuration :
- datespecifique correspond à une temporalité auquel le document fait référence (et non pas est publié) et prend "NA" sinon.
   par exemple, le règlement des études 2024-2025 prendrait la valeur "2024_2025" puisqu'il concerne surtout ces années.
- category1 correspond à la source de la page (site polytech, intranet, site s-u...)
- category2 correspond à la première grande catégorie sur le site même
- category3 correspond à la première sous-catégorie sur le site
- category4 correspond à la deuxième sous-catégorie sur le site
Parfois, l'imbrication n'est pas si profonde, et dans ce cas les category non-atteintes prennent la valeur "NA".
- filierespecifique (exemple : "main_agral" ou "main") indique si le document concerne une/des filière(s) en particulier, et prend "NA" sinon.