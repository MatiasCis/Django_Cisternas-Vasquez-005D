from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Cliente

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields=['idProducto','nombre','marca','fechaFabricacion','imagen']
        labels ={
            'idProducto': 'ID del Producto', 
            'nombre': 'Nombre del producto', 
            'marca': 'Marca', 
            'fechaFabricacion': 'Fecha de fabricacion',
            'imagen': 'Imagen'
        }
        widgets={
            'idProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la id del producto', 
                    'id': 'idProducto'
                }
            ),
            
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del producto', 
                    'id': 'nombre'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'fechaFabricacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la fecha de fabricacion del producto', 
                    'id': 'fechaFabricacion',
                }
            ),   
        }



class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields=['rut','nombre','apellido','email']
        labels ={
            'rut': 'Rut del cliente', 
            'nombre': 'Nombre del cliente', 
            'apellido': 'Apellido del cliente', 
            'email': 'Email del cliente',
        }
        widgets={
            'rut': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el rut del cliente', 
                    'id': 'rut'
                }
            ),
            
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del cliente', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el apellido del cliente', 
                    'id': 'apellido'
                }
            ), 
            'email': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el email del cliente', 
                    'id': 'email',
                }
            )

        }