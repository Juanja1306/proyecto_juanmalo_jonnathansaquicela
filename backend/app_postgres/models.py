from django.db import models

class TablaPostgres(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    class Meta:
        app_label = 'app_postgres'
        db_table = 'tabla_postgres'
