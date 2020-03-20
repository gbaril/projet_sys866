# Source

Ce travail a été pris de [oscarknagg](https://github.com/oscarknagg/few-shot).

# Datasets utilisés

1. [Omniglot](https://github.com/brendenlake/omniglot/tree/master/python)
1. [MiniImageNet](https://drive.google.com/file/d/0B3Irx3uQNoBMQ1FlNXJsZUdYWEE/view)
1. [CUB200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)

# Modifications

* Ajout du fichier [prepare_cub200.py](./scripts/prepare_cub200.py) afin de préparer les images CUB200 2011 pour qu'il soit utilisable par le modèle pour l'entrainement et les tests.

* Ajout du fichier [remove_grayscale_cub200.py](./scripts/remove_grayscale_cub200.py) qui enlève les quelques images qui ont un seul canal de couleur dans les images CUB200.  
   
   Il est impossible de les traiter directement.  J'ai choisi cette façon de faire puisque regarder chaque image et modifier l'une de ces dimensions durant l'entrainement rajoute du temps qui peut être sauvé de cette façon.

* Ajout de la classe [Cub200Dataset](./few_shot/datasets.py) qui permet de charger les images CUB200 avec un Dataloader de pytorch.

   Il a aussi fallu changer la grosseur des images MiniImageNet pour qu'elles soient 64x64 au lieu de 84x84.  Sinon, je ne pouvais pas entrer les images dans la mémoire de mon GPU.

* Ajout du paramètre [cub200](./experiments/proto_nets.py) afin d'entrainer le Prototypical Network sur le dataset CUB200.

* Ajout du paramètre [cub200](./experiments/maml.py) afin d'entrainer le MAML sur le dataset CUB200.

* Creation et entrainement des modèles [MAML](./models/maml/) et [Prototypical Network](./models/proto_nets/).

* Sauvegarde des pertes et des précisions lors de l'entrainement de chaque [model](./logs/).

* Creation du [script](./graphmaker.ipynb) qui permet de générer les graphiques présents dans l'annexe du rapport.