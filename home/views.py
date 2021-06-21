from django.shortcuts import render,HttpResponse
import pyrebase
firebaseConfig = {
           "apiKey": "AIzaSyDeKkMtloXQVu-ZBYwyIPjbT2-11Ph-TWQ",
           "authDomain": "instacashbot.firebaseapp.com",
           "databaseURL": "https://instacashbot-default-rtdb.asia-southeast1.firebasedatabase.app",
           "projectId": "instacashbot",
           "storageBucket": "instacashbot.appspot.com",
           "messagingSenderId": "832483698311",
           "appId": "1:832483698311:web:6333d88cf1adcffdf47a22",
          "measurementId": "G-ZR3YKJDDPH"
         }
firebase=pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
def home(request):
    #return HttpResponse("This protofili homepage")
    context = {'Navtitle':'Insta_cash_bot','course':'testcourse'}
    return render(request,'home.html',context)

def paytmcash(request):
    context = {'Navtitle':'Insta_cash_bot','course':'testcourse'}
    return render(request,'Paytm_tree.html',context)


def indiagold(request):
    context = {'Abttitle':'PaytmCash','course':'abouttest'}
    return render(request,'indiagold.html',context)
#--------------------Crypto Links-------------------
def Crypto(request):
    context = {'Abttitle':'PaytmCash','course':'abouttest'}
    return render(request,'Crypto_Maintree.html',context)

def wallet(request):
    context = {'Abttitle':'PaytmCash','course':'abouttest'}
    return render(request,'wallet.html',context)

def Telegramlink(request):
    context = {'Abttitle':'PaytmCash','course':'abouttest'}
    return render(request,'Cryptolayout.html',context)

# def contact(request):
    # channel_name = database.child('data1').child('name').get().val()
    # channel_type = database.child('data1').child('type').get().val()
    # channel_subs = database.child('data1').child('subscribe').get().val()
    # return render(request,'index.html',{
    #     "channel_name":channel_name,
    #     "channel_type":channel_type,
    #     "channel_subs":channel_subs
    # })
def fileuploaded(request):
    paytmno = request.POST.get('paytmno')
    name = request.POST.get('name')
    url = request.POST.get('url')
    
    data = {
        "paytmno":paytmno,
        "name":name,
        "url":url
    }
    database.child("paytm").child("Indiagold").push(data)
    return render(request,'create.html')