from django.db import models

# Create your models here.
class Produtos(models.Model):
 empresa = models.CharField(max_length=100)
 nome = models.CharField(max_length=100)
 descricao = models.TextField(max_length=100)
 qtd = models.IntegerField(default=0)
 valor = models.FloatField()
 promocao = models.CharField(max_length=20,default=0)
 image = models.ImageField()
 #image = models.CharField(max_length=10000)
 #image = models.FileField(upload_to ='static/',blank=True)

class Carrinho(models.Model):
  chave = models.CharField(max_length=100)
  pedido = models.TextField(max_length=100)
  valor = models.FloatField()
  qtd = models.IntegerField()
  sub_total = models.DecimalField(max_digits=10,decimal_places=2,default='0')

class Clientes(models.Model):
  pedido = models.CharField(max_length=100)
  nome = models.CharField(max_length=100)
  pagamento = models.CharField(max_length=20)
  endereco = models.CharField(max_length=20)

class Empresa(models.Model):
  nome = models.CharField(max_length=100)
  telefone = models.CharField(max_length=20)
  endereco = models.CharField(max_length=20)  
  #image = models.ImageField(upload_to ='static/',blank=True)
  image = models.ImageField()
#image = models.FileField(upload_to ='static/',blank=True)

 #image = models.CharField(max_length=10000)
