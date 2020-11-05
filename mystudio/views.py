from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View

from .forms import LoginForm

from django.views.generic import ListView
from .models import PostedSong


# Create your views here.
def testfunc(request):
    return render(request,'test.html',{})

def testfunc2(request):
    return render(request,'test2.html',{})

class PostedSong(ListView):
    template_name = 'mystudio.html'
    model = PostedSong

class LoginView(AuthLoginView):
    def post(self,request,*arg,**kwargs):
        pass

    def get(self,request,*arg,**kwargs):
        form = UserCreateForm(request.POST)
        render(request,'login.html',{'form':form})


#for signup
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from . forms import UserCreateForm
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'create.html', {'form': form,})











''' write again under below'''

#class LoginView(View):
#    def get(self,request,*args,**kwargs):
#        '''method for GET request'''
#        context = {'form':LoginForm(),
#        }
        #rendering empty form for login-screen-template
#        return render(request,'accounts/login.html',context)

#    def post(self,request,*arg,**kwargs):
#        '''method for POST request'''
#        form = LoginForm(request.Post)
#        if not form.is_valid():
#            return render(request,'login.html',{'form':form})
        #get user-object from form
#        user = form.get_user()

        #Login
#        auth_login(request,user)

        #redirect another screen
#        return redirect(reverse('shop:index'))

#login = LoginView.as_view()






















#
