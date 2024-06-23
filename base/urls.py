from django.urls import path


from base import views

urlspatterns =[
    path("create/", views.create_note, name="create")
]