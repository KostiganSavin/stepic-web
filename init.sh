sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo gunicorn -b 0.0.0.0:8080 --workers=2 hello:app
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql restart
#source web/myvenv/bin/activate
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:app &
gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application &
