from django.conf import settings
import pymysql
if not settings.DEBUG:
    pymysql.install_as_MySQLdb()