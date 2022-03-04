# Image classification service using Django and Keras
An image classifier application where the Django server receives an image as input and after it is loaded, the CNN-based image classifier classifies the image. 
After that, the program saves the path to the image and the result of the image classifier in PostgreSQL DB.

Project made by:
- Dias Kamza
- Yerkebulan Zhigerbayev
- Erasyl Usenov

## Installation
- Install dependencies:

```shell
$ pip install -r requirements.txt
```

- Or install libraries manually:

```shell
$ pip install django
$ pip install tensorflow-cpu
$ pip install keras
$ pip install psycopg2 
$ pip install Pillow
$ pip install django-heroku
$ pip install gunicorn
$ pip install ipykernel
$ pip install jupyterlab
$ pip install notebook
```

## Usage

- Follow the link if you just want to use our services

```shell 
https://imageclassificationapp.herokuapp.com/
```
- Or run the server locally

```shell
$ python manage.py runserver  
```

## Examples

- Run the server locally or go to the link

```python
https://imageclassificationapp.herokuapp.com/

http://127.0.0.1:8000/
```
After launching the service, upload an image with a specific object and click the submit button. 
The classification result and the path where the file was saved will appear on the screen.
The path to the image and the result of the image classifier will be saved in PostgreSQL

![image](https://user-images.githubusercontent.com/68639981/156689733-cedd5110-653b-4314-a007-b88615a83b54.png)

