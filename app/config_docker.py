import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	POSTGRES_USER = os.environ.get("POSTGRES_USER")
	POSTGRES_PW = os.environ.get("POSTGRES_PW")
	POSTGRES_URL = "rc1b-879g3ztam61ufn9g.mdb.yandexcloud.net"
	POSTGRES_DB = "assessment"
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB, port=12001)