from django.urls import path
from . import views

urlpatterns = [path('show/',views.show,name='show'),
               path('edit/<int:student_id>/',views.edit,name='edit'),
               path('update/<int:student_id>/',views.update,name='update'),
               ]