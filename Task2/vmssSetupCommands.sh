sudo apt-get update
sudo apt-get install python3 nginx
sudo apt install python3-pip
mkdir -p www/flaskapp
cd www/flaskapp
pip3 install virtualenv
python3 -m virtualenv flaskenv
chmod 755 flaskenv/
source flaskenv/bin/activate
pip install flask
nano app.py
FLASK_APP=app.py
flask run
pip install numpy
curl http://localhost:5000/numericalintegralservice/0/3.14159
source flaskenv/bin/activate
flask run --host 0.0.0.0
sudo apt install net-tools
netstat -tulpn | grep :5000
kill -9 [process_id]
sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
sudo apt install gunicorn
gunicorn --bind 0.0.0.0:5000 app:app --reload & >> /dev/null
ps -ef | grep gunicorn
kill -9 [gunicorn_process_id]
sudo rm /etc/nginx/sites-available/default
sudo nano /etc/nginx/sites-available/flaskapp
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled/
sudo systemctl reload nginx
sudo systemctl start nginx
sudo systemctl status nginx
curl localhost:80
curl -v http://localhost/numericalintegralservice/0/3.14159
sudo lsof -i :5000
