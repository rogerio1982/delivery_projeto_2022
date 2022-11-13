from django.shortcuts import render,redirect
from loja.models import Produtos, Carrinho,Clientes, Empresa
from .forms import ProdutosForm, EmpresaForm
from django.core.files.storage import FileSystemStorage

from random import choice
import string
from django.http import HttpResponseRedirect
from django.db.models import Sum, Min
from django.utils.formats import localize

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

from django.conf import settings
from django.core.files.storage import FileSystemStorage


def register(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)
        login(request, user)
        #criar empresa
        emp = Empresa()
        emp.nome = username
        emp.image = "logo.jpg"
        emp.save()
        return redirect('logar_usuario')
    else:
      form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def logar_usuario(request):
 if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    usuario = authenticate(request, username=username, password=password)
    if usuario is not None:
      login(request, usuario)   
      context = {
      'msg':'Seja bem vindo'
      }
      return render(request, 'inicial.html', context)
      #return redirect('home')
    else:
      form_login = AuthenticationForm()
 else:
    form_login = AuthenticationForm()
 return render(request, 'login.html', {'form_login': form_login})
 #return render(request, 'lojas.html', {'form_login': form_login})


def deslogar_usuario(request):
 logout(request)
 context = {
 'msg':''
 }
 return redirect('home')
 #return render(request, '/', context)



@login_required(login_url='/logar_usuario')
def ini(request):
 
 produtos = Produtos.objects.filter(promocao=0)
 
 pk = request.session['empresa']
 produtos = Produtos.objects.filter(empresa=pk)
 
 cha = request.session['chave']
 total = Carrinho.objects.filter(chave=cha).count()

 empresa = Empresa.objects.filter(id=pk)
 emp=""
 imagem=""
 for x in empresa:
   emp=x.nome
   imagem=x.image

 context = {
 'emp': emp,
 'total':total, 
 'imagem':imagem,
 'msg':'Inserido com sucesso!',
 'produtos': produtos,
 'empresa': pk,
 }
 return render(request, 'index.html', context)

#@login_required(login_url='/logar_usuario')
def home(request):
  context = {
  }
  return redirect('lojas')
  #return render(request, 'lojas.html', context)

def home2(request,pk):
 #
 if pk != request.session.get('empresa'):
   string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
   string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
   tam = 10
   valores = string.ascii_lowercase + string.ascii_uppercase
   chave = ''
   for i in range(10):
     chave += choice(valores)
   request.session['chave'] = chave
   request.session['empresa'] = pk
   produtos = Produtos.objects.filter(empresa=pk)
   empresa = Empresa.objects.filter(id=pk)
   emp=""
   imagem=""
   for x in empresa:
     emp=x.nome
     imagem=x.image

 if not request.session.get('chave'):
   string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
   string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
   tam = 10
   valores = string.ascii_lowercase + string.ascii_uppercase
   chave = ''
   for i in range(10):
     chave += choice(valores)
   request.session['chave'] = chave
   request.session['empresa'] = pk
   produtos = Produtos.objects.filter(empresa=pk)
   empresa = Empresa.objects.filter(id=pk)
   emp=""
   imagem=""
   for x in empresa:
     emp=x.nome
     imagem=x.image
 else:
   pk = request.session['empresa']
   produtos = Produtos.objects.filter(empresa=pk)
   empresa = Empresa.objects.filter(id=pk)
   emp=""
   imagem=""
   for x in empresa:
     emp=x.nome
     imagem=x.image
 cha = request.session['chave']  
 total = Carrinho.objects.filter(chave=cha).count()
 chave = request.session['chave']    
 print("teste@@",chave)
 context = {
 'chave' :chave,
 'total':total,
 'produtos': produtos,
 'emp': emp,
 'imagem': imagem,
 }
 
 return render(request, 'index.html', context)
 

def chamaini(request):

 pk = request.session['empresa']
 produtos = Produtos.objects.filter(empresa=pk)
 
 cha = request.session['chave']
 total = Carrinho.objects.filter(chave=cha).count()

 empresa = Empresa.objects.filter(id=pk)
 emp=""

 imagem=""
 for x in empresa:
   emp=x.nome
   imagem=x.image

 context = {
 'emp': emp,
 'imagem': imagem,
 'total':total, 
 'msg':'Inserido com sucesso!',
 'produtos': produtos,
 'empresa': pk,
 }
 return render(request, 'index.html', context)


def addCart(request,pk):
 carrinho = Carrinho()
 produtos = Produtos.objects.get(pk=pk)
 carrinho.chave = request.session['chave']
 carrinho.pedido = produtos.nome
 carrinho.valor = produtos.valor
 carrinho.qtd = 1
 carrinho.save()

 pk = request.session['empresa']
 produtos = Produtos.objects.filter(empresa=pk)
 
 cha = request.session['chave']
 total = Carrinho.objects.filter(chave=cha).count()

 empresa = Empresa.objects.filter(id=pk)
 emp=""

 imagem=""
 for x in empresa:
   emp=x.nome
   imagem=x.image

 context = {
 'emp': emp,
 'imagem': imagem,
 'total':total, 
 'msg':'Inserido com sucesso!',
 'produtos': produtos,
 'empresa': pk,
 }
 return render(request, 'index.html', context)#return redirect('home')#




def verCar(request):
 cha = request.session['chave']
 #carrinhos = Carrinho.objects.all()
 carrinhos = Carrinho.objects.filter(chave=cha)
 somar =  Carrinho.objects.filter(chave=cha).aggregate(Sum('valor'))
 somar = somar.get('valor__sum')

 #contar carrinho
 total = Carrinho.objects.filter(chave=cha).count()
 pk = request.session['empresa']

 empresa = Empresa.objects.filter(id=pk)
 emp=""
 imagem=""
 for x in empresa:
   emp=x.nome
   imagem=x.image

 context = {
 'chave': cha,   
 'emp': emp,
 'total':total, 
 'imagem':imagem,
 'msg':'Inserido com sucesso!',
 'empresa': pk,
 'carrinho': carrinhos,
 'somar':somar,
 'total':total
 }
 return render(request, 'carrinho.html', context)


def detail(request,pk):
 produtos = Produtos.objects.get(pk=pk)
    #contar carrinho
 cha = request.session['chave']
 total = Carrinho.objects.filter(chave=cha).count()
 pk = request.session['empresa']

 empresa = Empresa.objects.filter(id=pk)
 emp=""
 imagem=""
 for x in empresa:
   emp=x.nome
   imagem=x.image

 context = {
 'produtos': produtos,
 'emp': emp,
 'imagem':imagem,
 'total':total 

 }
 return render(request, 'detalhes.html', context)


def cadcli(request):
  #cad clientes
  cli = Clientes()
  chave = request.session['chave']

  pedido =  chave
  nome =  request.POST['your_name']
  pagamento =  request.POST['pagamento']
  endereco =  request.POST['endereco']
  cli.nome = nome
  cli.pedido = pedido
  cli.pagamento = pagamento
  cli.endereco=endereco
  cli.save()
  pk = request.session['empresa']
  empresa = Empresa.objects.filter(id=pk)
  
  emp=""
  imagem=""
  for x in empresa:
    emp=x.nome
    imagem=x.image
  
  cha = request.session['chave']
  carrinhos = Carrinho.objects.filter(chave=cha)
  total = Carrinho.objects.filter(chave=cha).count()
  context = {
  'total': total,
  'emp': emp,
  'msg':' ',
  'imagem':imagem

  }


  return render(request, 'cadcliconfirmar.html', context)


def cadclichama(request):
     #contar carrinho

  pk = request.session['empresa']
  empresa = Empresa.objects.filter(id=pk)
  emp=""
  imagem=""
  for x in empresa:

    emp=x.nome
    imagem=x.image
  cha = request.session['chave']
 #carrinhos = Carrinho.objects.all()
  carrinhos = Carrinho.objects.filter(chave=cha)
 #contar carrinho
  total = Carrinho.objects.filter(chave=cha).count()
  context = {
  'total': total,
  'emp': emp,
  'msg':' ',
  'imagem':imagem

  }
  return render(request, 'cadcli.html', context)


def excpedido(request,pk):
  carrinho = Carrinho.objects.get(pk=pk).delete()
  cha = request.session['chave']
 #carrinhos = Carrinho.objects.all()
  carrinhos = Carrinho.objects.filter(chave=cha)
 #contar carrinho
  total = Carrinho.objects.filter(chave=cha).count()
  somar =  Carrinho.objects.filter(chave=cha).aggregate(Sum('valor'))
  somar = somar.get('valor__sum')
  pk = request.session['empresa']
  empresa = Empresa.objects.filter(id=pk)
  emp=""
  imagem=""
  for x in empresa:
    emp=x.nome
    imagem=x.image

  context = {
   'chave' :cha,
   'emp': emp,
   'imagem': imagem,
   'carrinho': carrinhos,
   'total': total,
   'somar':somar
   }
  return render(request, 'carrinho.html', context)



def enviar(request):
  #enviar pedido
  cha = request.session['chave']
  carrinhos = Carrinho.objects.filter(chave=cha)
  clientes = Clientes.objects.filter(pedido=cha)

  somar =  Carrinho.objects.filter(chave=cha).aggregate(Sum('valor'))
  somar = str(somar.get('valor__sum'))
   ##serialize
  output=[]
 
  output.append("Pedido: "+cha)
  for cli in clientes:
      output.append("Nome: "+cli.nome)
      output.append("endereço: "+cli.endereco)
  
  output.append("produtos: " )

#empresa
  pk = request.session['empresa']#request.user
  print("nome: ", pk)
  empresa = Empresa.objects.filter(id=pk)
  emp=""
  tel=""
  for x in empresa:
    tel=x.telefone
  print ("tel"+tel)
#carrinho 
  for dados in carrinhos:
    output.append(dados.pedido)
    output.append(dados.valor)
  output.append("Total: R$"+ somar)
  #print(output)
  #print('\n'.join(map(str, output)))
  #formata a saída sem aspas
  output='\n'.join(map(str, output))
  del request.session['chave']     
  del request.session['empresa']    
  return HttpResponseRedirect("https://api.whatsapp.com/send?phone=" + "55"+tel+ "&text=" + str(output),"_blank")


def moeda(request):
  valor = 1768 
  valor = localize(valor)
  return ('Valor: %s' % valor)


@login_required(login_url='/logar_usuario')
def emp(request):
 pk = request.user
 empresa = Empresa.objects.filter(nome=pk)
 emp=""
 id=""
 for x in empresa:
   emp=x.id
   tel=x.telefone
   end=x.endereco
 empform = EmpresaForm(initial={'nome': pk,'telefone':tel, 'endereco':end})
 empresa = Empresa.objects.filter(nome=pk)
 emp=""
 image=""
 endereco=""
 tel=""
 for x in empresa:
   emp=x.nome
   endereco=x.endereco
   image=x.image
   tel=x.telefone
 context = {
 'telefone':tel,
 'image':image,
 'empresa': emp,
 'endereco':endereco,
 'form':empform
 }
 return render(request, 'empresa.html', context)


@login_required(login_url='/logar_usuario')
def cademp(request):
 pk = request.user
 empresa = Empresa.objects.filter(nome=pk)
 emp=""
 id=""
 for x in empresa:
   emp=x.id
   tel=x.telefone
   end=x.endereco
 #empresa = Empresa.objects.get(id=emp)
  #iniciar campo no form
 empform = EmpresaForm(initial={'nome': pk,'telefone':tel, 'endereco':end})
 if request.method == "POST":
  # e = EmpresaForm(request.POST or None, request.FILES or None)
   nome =  request.POST['nome']
   telefone =  request.POST['telefone']
   endereco =  request.POST['endereco']
   image =  request.FILES['image']
 #empresa.image = image
 #empresa.telefone = telefone
   e = Empresa(nome=nome, telefone=telefone, image=image,endereco=endereco, pk=emp)
   e.save()
   #emp()


 empresa = Empresa.objects.filter(nome=pk)
 emp=""
 image=""
 endereco=""
 tel=""
 for x in empresa:
   emp=x.nome
   endereco=x.endereco
   image=x.image
   tel=x.telefone
 context = {
 'telefone':tel,
 'image':image,
 'empresa': emp,
 'endereco':endereco,
 'form':empform
 }
 return render(request, 'empresa.html', context)



def cadprod(request):
 pk = request.user
 project = Empresa.objects.filter(nome=pk)
 emp=""
 for x in project:
   emp=x.id

 prod = ProdutosForm(initial={'empresa': emp})#iniciar campo no form

 if request.method == "POST":
   prod = ProdutosForm(request.POST or None, request.FILES or None)
   if prod.is_valid():

     #prod.empresa=emp
     #prod.cleaned_data['empresa'] = emp
     #pro.promocao=promocao
     #pro.qtd=qtd
     prod.save()



 project = Produtos.objects.filter(empresa=emp)
 context = {
 'projects': project,
 'msg':'',
 'form': prod,
 }         
 return render(request, "produtos.html", context)


def atuprod(request,pk):
 #pro = Produtos()
 pro = Produtos.objects.get(id=pk)

 nome =  request.POST['nome']
 descricao =  request.POST['descricao']
 valor =  request.POST['valor']
 #imagem =  request.POST['imagem']
 #empresa = emp
 #promocao = 0
 #qtd = 0

 pro.nome = nome
 pro.descricao = descricao
 pro.valor = valor
 #pro.imagem=imagem
 #pro.empresa=empresa
 #pro.promocao=promocao
 #pro.qtd=qtd

 pro.save()

 emp = request.user
 project = Empresa.objects.filter(nome=emp)
 id=""
 for x in project:
   id=x.id
 project = Produtos.objects.filter(empresa=id)
 context = {
 'projects': project,
 'msg':'Atualizado com sucesso!'
 }
 return render(request, "produtos.html", context)


def delprod(request,pk):
 
 project = Produtos.objects.get(id=pk)
 project.delete()

 emp = request.user
 project = Empresa.objects.filter(nome=emp)
 id=""
 for x in project:
   id=x.id
 project = Produtos.objects.filter(empresa=id)
 context = {
 'id': id,
 'projects': project,
 }
 return render(request, "produtos.html", context)


def vis(request):
 pk = request.user
 project = Empresa.objects.filter(nome=pk)
 id=""
 for x in project:
   id=x.id
 context = {
 'id': id,
 }
 return render(request, "visualizar.html", context)


def lojas(request):
 pk = request.user
 project = Empresa.objects.all()
 id=""
 for x in project:
   id=x.id
 context = {
 'id': id,
 'project':project,
 }
 return render(request, "lojas.html", context)