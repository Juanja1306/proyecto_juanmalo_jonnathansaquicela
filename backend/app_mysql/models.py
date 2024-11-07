from django.db import models

class TablaMySQL(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        app_label = 'app_mysql'
        db_table = 'tabla_mysql'
