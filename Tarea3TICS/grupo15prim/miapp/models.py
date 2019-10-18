from django.db import models

class cliente(models.Model):
	nombre=models.CharField(max_lenght=30)
	rut=models.CharField(max_lenght=10)
	correo=models.EmailField(max_lenght=40)


class Reserva(models.Model):
	Fecha=DateField()
	Horario=CharField(max_lenght=30)
	cliente=models.ForeingKey(cliente,on_delete=models.CASCADE)
	Mesa=models.ForeingKey(Mesa,on_delete=models.CASCADE)


class Mesa(models.Model):
	nmesas=CharField(max_lenght=50)	
# Create your models here.
