sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
# sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo gunicorn -c /home/box/web/etc/gunicorn-hello.conf hello:wcgi_app
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
sudo /etc/init.d/gunicorn restart
# sudo /etc/inid.d/mysql start