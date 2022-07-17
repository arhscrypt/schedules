from django.urls import path
from .views import delete, index, scheduleApi, add, update

urlpatterns = [
    # api link
    path('rest',scheduleApi),
    path('rest/<int:id>',scheduleApi),
    # render link
    path('',index, name='list'),
    path('add',add, name='add'),
    path('update/<int:id_sch>',update, name='update'),
    path('delete/<int:id_sch>',delete, name='delete'),
]