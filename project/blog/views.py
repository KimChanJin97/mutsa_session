from django.http import QueryDict
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

# READ
def read_all_function(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs":blogs})

# READ
def read_one_function(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, "detail.html", {"blog":blog})

# CREATE 를 위한 리소스 띄우기
def new_function(request):
    return render(request, "new.html")

# CREATE
def create_function(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        create_blog = form.save(commit=False)
        create_blog.writer = request.user # 안쓰면 개고생한다
        create_blog.save()
        return redirect('blog:read_one', create_blog.id)
    return render(request, "new.html", {'form':form})

# UPDATE 를 위한 리소스 띄우기
def edit_function(request, id):
    edit_blog = get_object_or_404(Blog, pk=id)
    return render(request, "edit.html", {"edit_blog":edit_blog})

# UPDATE
def update_function(request, id):
    update_blog_old = get_object_or_404(Blog, pk=id)
    form = BlogForm(request.POST, instance=update_blog_old)

    if request.method == "POST":
        # make_error = QueryDict.copy(request.POST)
        # make_error["title"] = ""
        # form = BlogForm(make_error, instance=update_blog_old)
        if form.is_valid():
            update_blog_new = form.save(commit=False)
            update_blog_new.save()
            return redirect("blog:read_one", update_blog_new.id)

    return render(request, "new.html", {"form":form, "update_blog_old":update_blog_old})

# DELETE
def delete_function(request, id):
    delete_blog = get_object_or_404(Blog, pk=id)
    delete_blog.delete()
    return redirect("blog:read_all")