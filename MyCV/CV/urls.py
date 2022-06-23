from django.urls import path
from .import views
urlpatterns = [
    path('person/<int:person_id>',views.person_by_id, name='person_by_id'),
]
