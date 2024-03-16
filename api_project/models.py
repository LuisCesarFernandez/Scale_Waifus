from django.db import models

# Create your models here.

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name_role = models.CharField(max_length=20)

    class Meta:
        db_table = 'Role'

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre_user = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    roles = models.ManyToManyField(Role, through='User_Role')

    class Meta:
        db_table = 'User'

class User_Role(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'User_Role'

class Waifu(models.Model):
    id_waifu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    anime = models.CharField(max_length=100)
    edad = models.CharField(max_length=50)
    puntuación_total = models.DecimalField(max_digits=4, decimal_places=2)
    cant_puntuaciones = models.IntegerField()

    class Meta:
        db_table = 'Waifu'

class Waifu_raiting(models.Model):
    id_waifu_rating = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_waifu = models.ForeignKey(Waifu, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Waifu_raiting'

class Personaje(models.Model):
    id_personaje = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    verso = models.CharField(max_length=100)
    escala = models.CharField(max_length=30)
    hazañas = models.TextField

    class Meta:
        db_table = 'Personaje'

class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    comentarios = models.TextField

    class Meta:
        db_table = 'Comentario'