from django.shortcuts import render,HttpResponse

def home_page(request):
    return render(request,'home.html')
def book_page(request):
    return render(request,'book.html')
def picture_page(request):
    return render(request,'picture.html')
def program_page(request):
    return render(request,'program.html')

