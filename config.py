import os

WTF_CSRF_ENABLED = False

PROJECT_ID = 'testproject-183322'

#CLOUD SQL
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = 'nettunes2017'
CLOUDSQL_DATABASE = 'nettunes-lib'
CLOUDSQL_CONNECTION_NAME = 'testproject-183322:us-central1:nettunes-lib'

# Alternatively, you could use a local MySQL instance for testing.
LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE)

# When running on App Engine a unix socket is used to connect to the cloudsql
# instance.
LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@localhost/{database}'
    '?unix_socket=/cloudsql/{connection_name}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)

if os.environ.get('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI

