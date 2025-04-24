[![CodeFactor](https://www.codefactor.io/repository/github/redarmz/terrortrack/badge)](https://www.codefactor.io/repository/github/redarmz/terrortrack)


## Install and run

```
git clone https://github.com/redarmz/TerrorTrack.git
```

### Backend

Pour Linux 
```
cd backend
virtualenv . && source bin/activate
pip install -r requirements.txt
```
Pour Windows
```
cd backend
python -m venv venv  # Crée un environnement virtuel nommé "venv"
venv\Scripts\activate  # Active l'environnement virtuel
pip install -r requirements.txt  # Installe les dépendances
```

Run

```
cd instant_backend
python3 manage.py runserver
```

### Websockets server

Install a Centrifugo server locally:

```
cd backend/instant_backend
python manage.py installws
```

[More info](https://github.com/synw/django-instant#install-the-websockets-server).

Run the websockets server:

```
cd backend/instant_backend
python manage.py runws
```

### Frontend

```
cd frontend
npm install
# or yarn install
npm run dev
# or yarn dev
```

The frontend is available at `localhost:3000`
