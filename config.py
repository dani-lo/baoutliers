import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

class Config:
    S3_BUCKET                 = os.environ('S3_BUCKET')
    S3_KEY                    = os.environ('S3_KEY')
    S3_SECRET                 = os.environ('S3_SECRET')
    S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

    APP_DATA                  = '/var/www/outliers/testrun/data/' if os.environ('APP_ENV') == 'production' else '/home/dani/Documents/projects/outliers/testrun/data/'
    SECRET_KEY                = os.urandom(32)
    DEBUG                     = True
    PORT                      = 5000