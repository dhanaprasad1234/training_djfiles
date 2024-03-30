from django.urls import path
from . import views

urlpatterns = [path('',views.home,name='home'),
                path('saveform/',views.saveform,name='saveform'),
               path('show/',views.show,name='show'),
               path('edit/<int:student_id>/',views.edit,name='edit'),
               path('update/<int:student_id>/',views.update,name='update'),
               path('delete/<int:student_id>/',views.delete,name='delete')
               ]