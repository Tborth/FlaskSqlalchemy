sudo apt-get install virtualenv
virtualenv venv --python=python3.8
source venv/bin/activate
pip install flask
pip install sqlalchemy
postgres:-

sudo apt install postgresql postgresql-contrib
 sudo -u postgres psql
 ALTER USER postgres PASSWORD 'root';

psql -U postgres -h localhost
