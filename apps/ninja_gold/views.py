from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    if 'total'  and 'activities' not in request.session:
        request.session['total']=0
        request.session['activities']=[]

    return render(request, 'ninja_gold/index.html')


def process_money(request, building):

    if request.method=="POST":
        if building=="farm":
            gold=random.randint(10, 20)
            request.session['total']+=gold
        if building=="cave":
            gold=random.randint(5, 10)
            request.session['total']+=gold
        if building=="house":
            gold=random.randint(2, 5)
            request.session['total']+=gold
        if building=="casino":
            gold=random.randint(-50, 50)
            request.session['total']+=gold
        return redirect('/')

def reset(request):
    if request.method=="POST":
        request.session['total']=0
        return redirect('/')

    #
    #     data=request.POST['building']
    #     print data
    #     if data=='farm':
    #         request.session['gold']+=random.randint(10, 20)
    #         print request.session['gold']
    #     elif data=='cave':
    #         request.session['gold']+=random.randint(5, 10)
    #     elif data=='house':
    #         request.session['gold']+=random.randint(2, 5)
    #     elif data=='casino':
    #         request.session['gold']+=random.randint(-50, -50)
    # return redirect('/')
