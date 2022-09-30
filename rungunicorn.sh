docker run -td  --name guni --mount type=bind,source=/home/ubuntu/demo-django/scripts,target=/scripts2 -p 8000:8000 gunicorn
