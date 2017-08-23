from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Post

from .forms import Postform
# Create your views here.
def post_list(request):
    queryset_list = Post.objects.all()


    query= request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(title__icontains=query)


    paginator = Paginator(queryset_list, 4)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)


        0
    context = {
        "object_list": queryset,
        "title" : "List"
    }
    return render(request,"post_list.html",context)


def post_create(request):

    form = Postform(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "Succesfully created" , extra_tags='some-tag')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Failed")


    context = {
        "form": form,
    }


    return render(request,"post_form.html",context)



def post_detail(request, id=None):

    #instance = get_object_or_404(Post, title="joys")
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, "detail.html", context)



def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = Postform(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Succesfully updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Updation failed!")

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }

    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Succesfully Deleted")
    return redirect('lists')





