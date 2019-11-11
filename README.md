# Simple Web Application Prototype

Run locally from virtual environment:
```bash
$ gunicorn -w 1 -b 0.0.0.0:8081 wsgi:app
```

Run locally from container
```bash
$ docker run -it -p 0.0.0.0:8081:8081 <image>
```
