from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# from classes_api import views
from classes_api.views import ListView, DetailView, CreateView, UpdateView, DeleteView
from classes import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('list-api/', ListView.as_view(), name ='listAPI'),
    path('detail-api/<int:class_id>/',DetailView.as_view(), name='detailAPI'),

    path('create-api/', CreateView.as_view(), name='createAPI'),
    path('update-api/<int:class_id>/', UpdateView.as_view(), name='updateAPI'),
    path('delete-api/<int:class_id>/', DeleteView.as_view(), name='deleteAPI'),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
