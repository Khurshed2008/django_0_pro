from django.urls import path,include
from main.views import look, kill,itemsid

app_name = 'myapp'

urlpatterns = [
    path('',look),

    path('me/',kill),
    path('me/<int:my_id>/',itemsid,name='detail')
]