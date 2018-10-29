
# Supervisord

Setup auto-restart service

Homepage: [http://supervisord.org/](http://supervisord.org/)

Useful for CTF tasks, long-running tasks

## Steps

Installing via pip

```sh
pip install supervisor
```

Change config

```sh
sudo vim /etc/supervisor/supervisord.conf
```
Details

```ini
[supervisord]
logfile = /tmp/supervisord.log
user = deploy

[program:tcp_sudoku]
directory=/home/deploy/tcp_sudoku
command=python sudoku_service.py
stderr_logfile=sudoku.log
stdout_logfile=sudoku.log
autostart=true
autorestart=true
```
