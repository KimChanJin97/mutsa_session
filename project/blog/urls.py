from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    # READ : list_view
    path("", read_all_function, name="read_all"),
    # READ : detail_view
    path("blog/<int:id>", read_one_function, name="read_one"),
    # Create
    path("new/", new_function, name="new"),
    path("blog/create/", create_function, name="create"),
    # Update
    path("blog/edit/<int:id>", edit_function, name="edit"),
    path("blog/update/<int:id>", update_function, name="update"),
    # DELETE
    path("blog/delete/<int:id>", delete_function, name="delete"),

]
