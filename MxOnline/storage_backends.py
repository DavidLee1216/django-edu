from storages.backends.s3boto3 import S3Boto3Storage
from MxOnline.settings import MEDIAFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = MEDIAFILES_LOCATION
    file_overwrite = False