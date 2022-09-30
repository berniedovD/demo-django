docker run -td  --name guni --mount type=bind,source=/home/ubuntu/demo-django/scripts,target=/scripts2 gunicorn python /scripts2/py2.py
