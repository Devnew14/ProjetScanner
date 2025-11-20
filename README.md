🔍 Mini Scanner de Ports en Python

Petit projet éducatif permettant de scanner des ports TCP sur une machine locale ou un hôte du réseau.
Il est conçu pour être simple à comprendre, à modifier et à utiliser.

⚠️ Utilisation légale

Ce scanner doit uniquement être utilisé sur :

vos propres machines

des machines pour lesquelles vous avez une autorisation explicite

Scanner des machines sans autorisation est illégal.

🧠 Comment ça fonctionne ?

Le script tente d’ouvrir une connexion TCP vers chaque port ciblé.

✔️ Si la connexion réussit : le port est considéré ouvert

❌ Si la connexion échoue : le port est fermé

Il utilise uniquement le module Python standard :

import socket


Ce qui rend le script compatible avec n’importe quelle installation Python.

▶️ Exemple d'utilisation

Dans un terminal :

python Scanner_ports.py


Puis entrez une IP :

IP à scanner : 127.0.0.1  (localhost)


Exemple de sortie (avec un port fictif) :

Port ouvert : 5000


Ici, 5000 est juste un exemple de port générique utilisé dans beaucoup de démonstrations.

📁 Contenu du projet
ProjetScanner/
│
├── Scanner_ports.py       → Scanner de ports principal
├── test_port_8000.py      → Petit script test (utilise un port d’exemple)
├── exemple_logs.md        → Exemple de résultats (fichier démonstration)
└── README.md              → Documentation du projet