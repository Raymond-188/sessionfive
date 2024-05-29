from django.shortcuts import render
from django.http import HttpResponse
from .models import Feauture


# Create your views here.
def index(request):
    feature1 = Feauture()
    feature1.id = 0
    feature1.name = 'Our Mission'
    feature1.details = '''consectetur elit, sed do eiusmod tempor ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
    exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    '''
    feature1.images = '/static/images/why-us-1.jpg'
    feature1.boxicon = 'bx bx-book-reader'
    feature1.is_btn = True

    feature2 = Feauture()
    feature2.id = 1
    feature2.name = 'Our Plan'
    feature2.details = '''Sed ut perspiciatis unde omnis iste natus error sit
        voluptatem doloremque laudantium, totam rem aperiam, eaque ipsa
        quae ab illo inventore veritatis et quasi architecto beatae vitae
        dicta sunt explicabo.
    '''
    feature2.images = '/static/images/why-us-2.jpg'
    feature2.boxicon = 'bx bx-calendar-edit'
    feature2.is_btn = True

    feature3 = Feauture()
    feature3.id = 2
    feature3.name = 'Our Vision'
    feature3.details = '''Nemo enim ipsam voluptatem quia voluptas sit aut
    odit aut fugit, sed quia magni dolores eos qui ratione voluptatem sequi
    nesciunt Neque porro quisquam est, qui dolorem ipsum quia
    dolor sit amet.
    '''
    feature3.images = '/static/images/why-us-3.jpg'
    feature3.boxicon = 'bx bx-landscape'
    feature3.is_btn = True

    features = [feature1, feature2, feature3]

    return render(request, 'index.html', {'features': features})
