import os

class Config:
    S3_BUCKET                 = os.getenv('S3_BUCKET')
    S3_KEY                    = os.getenv('S3_KEY')
    S3_SECRET                 = os.getenv('S3_SECRET')
    S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

    SECRET_KEY                = os.urandom(32)
    DEBUG                     = True
    PORT                      = 5000