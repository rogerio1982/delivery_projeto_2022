from django import forms
from loja.models import Produtos,Empresa

# creating a form
class ProdutosForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(ProdutosForm, self).__init__(*args, **kwargs)
    self.fields['empresa'].widget.attrs['readonly'] = True
    self.fields['valor'].widget.attrs['type'] = 'NumberInput'

  class Meta:
    # specify model to be used
    model = Produtos
    fields = ['empresa','nome', 'descricao', 'valor','image']
    #fields = '__all__'  
    #fields = ['empresa', 'nome', 'descricao', 'qtd', 'valor','promocao','image']


# creating a form
class EmpresaForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(EmpresaForm, self).__init__(*args, **kwargs)
    self.fields['nome'].widget.attrs['readonly'] = True
    
  class Meta:
    # specify model to be used
    model = Empresa
    fields = ['nome','telefone','endereco','image'] 



