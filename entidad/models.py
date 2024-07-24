from django.db import models
 
class EntidadModel(models.Model):
    Nit = models.BigIntegerField()
    Dv = models.SmallIntegerField()
    RazonSocial = models.CharField(max_length=150)
    TipoEntidad = models.SmallIntegerField()
    CodigoSuper = models.SmallIntegerField()
    Sigla = models.CharField(max_length=60)
    Descripcion = models.CharField(max_length=60)
    Departamento = models.CharField(max_length=30)
    Ciudad = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=20)
    Email = models.EmailField(max_length=60)
    CIIU = models.SmallIntegerField()
    RepresentanteLegal = models.CharField(max_length=60)
    Gremio = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "entidad"
        ordering = ['-created_at']