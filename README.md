# Mandat client — imagerie satellite historique

## Contexte

Vous reprenez ce mandat après le départ précipité du développeur qui s'en occupait.
Il ne laisse que `legacy_code.py` : un script qui permet tout juste d'ouvrir le fichier
du client, sans structure, sans tests, sans documentation.

Le client dispose d'un jeu de données provenant d'un ancien satellite (années 1960).
La résolution des pixels est faible et les données sont enregistrées dans un format
propriétaire peu documenté (`data/raw/image_spuk.grd`).

**Ne modifiez jamais le contenu de `data/raw/`.**

## Structure des fichiers `.grd`

Les fichiers `.grd` du client sont normalement des fichiers binaires : leur
contenu ne doit pas être interprété comme du texte sans connaître le format de
stockage et le mécanisme de déchiffrement utilisés.

Votre collègue explique que :

- les premières lignes commencent par `#` et décrivent les métadonnées ;
- l'en-tête indique notamment la largeur (`WIDTH`), la hauteur (`HEIGHT`), le
  type des valeurs (`DATATYPE`) et le nombre de bandes (`BANDS`) ;
- les lignes suivantes contiennent les valeurs des pixels sous forme de nombres
  séparés par des espaces ;
- il semble que chaque ligne contient des groupes de valeurs séparés par
  `|` et des espaces (possiblement les pixels de l'image, organisés en lignes, colonnes et bandes).

> Notes générales sur les images de télédétection : une image est généralement organisée sous la forme de bandes (rouge, vert, bleu, proche-infrarouge, ...). Chaque bande contient une grille (ou matrice) de pixels. Une matrice a un nombre de lignes et de colonnes. Les valeurs des pixels sont généralement un nombre.

## Ce que vous héritez

- `legacy_code.py` — le seul code fonctionnel existant. Étudiez-le attentivement :
  il vous permet d'ouvrir le fichier, mais il ne respecte pas toutes les contraintes
  du client (voir plus bas).
- `data/raw/image_spuk.grd` — le fichier de données à traiter.


## Contraintes du client (rappel — voir l'énoncé complet du TD sur Moodle)

- Le script final doit pouvoir tourner sur un ordinateur embarqué très léger : le code
  exécuté en production (tout sauf les tests) ne doit contenir **aucun `import`**.
  Regardez attentivement ce que fait `legacy_code.py` à ce sujet.
- Le script doit fonctionner avec ce fichier, mais aussi avec d'autres fichiers du
  même format, sans modification du code.

## Votre travail

Reprendre ce projet sur des bases saines : structure, documentation, tests, et les
fonctionnalités attendues par le client. Voir l'énoncé complet du TD#1 sur Moodle
pour le détail des livrables et le barème.

## Environnement

Choisissez l'une des deux méthodes suivantes selon les outils disponibles sur
votre machine.

### Avec Conda

```bash
conda create -n gmq710_td1 python=3.11
conda activate gmq710_td1
```

### Avec l'environnement virtuel Python (`venv`)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Sous Windows, activez l'environnement avec `.\.venv\Scripts\activate`.

## Exécuter le projet

Le fichier à exécuter principalement est `main.py`, situé à la racine du
projet. Il doit servir de point d'entrée et appeler les fonctionnalités
développées dans `src/`.

Dans VS Code :

1. Ouvrez `main.py`.
2. Cliquez sur le bouton **Exécuter le fichier Python** en haut à droite, ou
  faites un clic droit dans le fichier puis choisissez **Run Python File**.
3. Vérifiez le résultat dans le terminal intégré de VS Code.

L'exécution doit notamment permettre de vérifier que le lecteur fonctionne avec
un fichier `.grd` et qu'il produit le résultat attendu, sans devoir modifier le
code entre deux fichiers de données.

## Démarrer un projet à partir de ce template

Ce dépôt peut servir de point de départ pour un nouveau projet de lecture
d'images `.grd`.

### Depuis GitHub

1. Ouvrez ce dépôt sur GitHub et cliquez sur **Use this template** puis
  **Create a new repository**.
2. Donnez un nom au nouveau dépôt et choisissez sa visibilité.
3. Clonez votre nouveau dépôt, puis placez-vous dans son dossier :

  ```bash
  git clone https://github.com/<utilisateur>/<nouveau-depot>.git
  cd <nouveau-depot>
  ```

4. Créez et activez l'environnement du projet avec la méthode de votre choix :

  ```bash
  conda create -n <nom-environnement> python=3.11
  conda activate <nom-environnement>
  ```

  Ou, avec `venv` :

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

5. Remplacez les données d'exemple dans `data/raw/` par vos propres fichiers
  `.grd`, sans modifier les données originales si elles doivent être
  conservées.

### Depuis une copie locale (PRO)

```bash
git clone https://github.com/<utilisateur>/geo_imagereader.git <nouveau-projet>
cd <nouveau-projet>
git remote rename origin template
git remote add origin https://github.com/<utilisateur>/<nouveau-depot>.git
```

Après la création du projet, adaptez le nom du projet, la documentation et les
tests à votre cas d'usage avant de commencer les développements.

## Bases de Git et partage du projet

Le dépôt GitHub doit être utilisé comme espace de suivi du travail. Les
opérations courantes peuvent être réalisées directement dans VS Code, sans
utiliser le terminal.

### Ouvrir le projet

1. Ouvrez le dossier du projet dans VS Code.
2. Cliquez sur l'icône **Contrôle de code source** dans la barre latérale
  gauche.
3. Connectez-vous à GitHub lorsque VS Code le demande.

### Enregistrer une étape de travail

Après avoir modifié le code ou ajouté des tests :

1. Consultez la liste **Modifications** dans le panneau **Contrôle de code
  source**.
2. Vérifiez les fichiers concernés en cliquant dessus. Ne sélectionnez pas les
  données originales de `data/raw/`.
3. Cliquez sur le `+` à côté des fichiers à conserver dans le prochain commit.
4. Écrivez un message court et précis, par exemple `Ajouter le lecteur GRD`.
5. Cliquez sur **Valider** ou **Commit**.

Faites un commit après chaque étape importante. Un commit doit correspondre à
un changement compréhensible : fonctionnalité, correction, test ou
documentation. Évitez les messages vagues comme `changements` ou `travail
final`.

### Envoyer et récupérer les changements

Après un commit, cliquez sur **Synchroniser les modifications** dans le panneau
**Contrôle de code source**. Cette action envoie vos commits vers GitHub et
récupère les éventuelles modifications déjà présentes en ligne.

Avant de rendre le projet, vérifiez sur la page GitHub que les derniers fichiers
et commits sont bien visibles.

### Donner accès au code

Le dépôt doit être accessible à l'enseignant ou au correcteur. Sur GitHub :

1. Ouvrez le dépôt du projet et allez dans **Settings**.
2. Ouvrez **Collaborators** ou **Collaborators and teams** dans la rubrique
  **Access**.
3. Cliquez sur **Add people** et recherchez le nom d'utilisateur GitHub ou
  l'adresse associée au compte de l'enseignant.
4. Envoyez l'invitation et vérifiez que la personne apparaît dans la liste des
  collaborateurs.

Ne partagez jamais votre mot de passe, votre jeton d'accès ou une clé privée.
Si le dépôt est privé, l'ajout comme collaborateur est nécessaire pour que le
correcteur puisse consulter le code et l'historique des commits.
