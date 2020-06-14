# Used car price prediction 
Example of ML model deployed on Django Rest Framework 

## Building
```sh
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

## Data
Data in `CARS.csv` from Kaggle

ML model was build in the notebook `model.ipynb`
