from django.urls import path
from .views import eliminar_auto, galeria, home, formulario, lista_automoveis, eliminar_auto, modificar_auto,PersonCreateView, teste


urlpatterns = [
    path('', home, name='home' ),
    path('galeria/', galeria, name='galeria'),
    path('formulario/', formulario, name='formulario'),
    path('lista-autos/', lista_automoveis, name='lista_autos'),
    path('eliminar_auto/<id>/', eliminar_auto, name='eliminar_auto'),
    path('modificar_auto/<id>', modificar_auto, name="modificar_auto"),
    path('person_form/', PersonCreateView.as_view() ,name='person_form'),
    path('teste/', teste, name='teste'),

]



