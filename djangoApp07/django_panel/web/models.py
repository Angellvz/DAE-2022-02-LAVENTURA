from django.db import models


class TblAlumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=100)
    alumno_email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alumno'