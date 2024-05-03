from django.urls import path

from . import views

app_name = "noteit"
urlpatterns = [
    # ex: noteit/add --> create new note (TODO: not working yet)
    # path("notes/add/", views.NewNoteView.as_view(), name="new_note"),

    # path("notes/login/", views.LoginView.as_view(), name="login"),

    path("notes/folder/<str:folder>/", views.FolderIndexView.as_view(),
         name="folder_index"),

    path("notes/tag/<str:tag>/", views.TagIndexView.as_view(),
         name="folder_index"),

    # ex: noteit/notes/5/ --> edit note version (working)
    path("notes/<int:pk>/", views.DetailView.as_view(), name="detail"),

    # ex: noteit/5/results/ --> view note version (working)
    path("notes/<int:pk>/results/", views.ResultsView.as_view(),
         name="results"),

    # ex: noteit/5/submit/ --> submit edits to note (working)
    path("notes/<int:pk>/submit/", views.submit, name="submit"),

    # ex: noteit/notes --> index/homepage (working)
    path("notes/", views.IndexView.as_view(), name="index"),

    # ex: noteit/message --> javascript test (working)
    path("notes/message", views.MessageView, name="message"),
]
