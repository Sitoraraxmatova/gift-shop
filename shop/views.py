from django.shortcuts import render
from.models import Post  


def home_page(request):
    postlar=Post.objects.all()
    context={
        'postlar':postlar
    }
    return render(request,'index.html',context)

def contact(request):
    postlar=Post.objects.all()
    context={
        'postlar':postlar
    }
    return render(request,'contact.html',context)

def shop(request):
    postlar=Post.objects.all()
    context={
        'postlar':postlar
    }
    return render(request,'shop.html',context)

def testimonial(request):
    postlar=Post.objects.all()
    context={
        'postlar':postlar
    }
    return render(request,'testimonial.html',context)

def why(request):
    postlar=Post.objects.all()
    context={
        'postlar':postlar
    }
    return render(request,'why.html',context)