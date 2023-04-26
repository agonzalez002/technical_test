# technical_test

Dans le fichier XPath_response.txt se trouve les réponse pour la première partie

Pour la seconde partie, l'application django se trouve dans le dossier my_django_project

Pour lancer l'application:

```
cd my_django_project
python3 manage.py runserver
```

Pour que l'application fonction il faut créer une base de données `person`

```
createdb -O [USERNAME] -E UTF8 person
```


L'endpoint de visualisation des personne est : 127.0.0.1:8000/api/person en GET

L'endpoint pour l'ajout d'un personne est : 127.0.0.1:8000/api/person en POST en passage les valeurs pour lastname, firstname et birthday
