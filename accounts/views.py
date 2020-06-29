import tempfile
from django.utils.html import strip_tags
import requests
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core import files
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.models import RegularUser,OrganizationUser
from mediablog.models import MediaBlog
# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from io import BytesIO
from accounts.tokens import account_activation_token

def  CreateR(user,city,phone,fb,photo,about):
    regular=RegularUser(user_r=user)
    regular.city=city
    regular.phone=phone
    regular.about_you=about
    regular.photo=photo
    regular.fb=fb
    regular.save()
def CreateO(user,city,phone,web,address,purpose,photo,org_name):
    organization = OrganizationUser(user_o=user)
    organization.city=city
    organization.phone=phone
    organization.fb=web
    organization.address=address
    organization.purpose=purpose
    organization.photo=photo
    organization.o_name=org_name
    organization.save()

def SIgnupView(request):
    return render(request,'user/signup.html')
def LoginView(request):
    if request.user.is_authenticated:
        return redirect('Mainhome')
    else:
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            print(username,password)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Mainhome')
            else:
                messages.info(request,"Enter correct username and password")
                return redirect('login')

        else:
            return render(request, 'user/login.html')



def Logout_view(request):
    logout(request)
    return redirect('login')
def RegularView(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        comfirm_password=request.POST['comfirm_password']
        facebook=request.POST['facebook']
        city=request.POST['city']
        phone=request.POST['phone']
        about_you=request.POST['about_you']
        photo=request.FILES['photo']
        print(username,email,first_name,last_name,password,comfirm_password,city,facebook,phone,about_you,photo)
        if password==comfirm_password:
            if len(password)<8:
                messages.info(request, "password must be 8 character and strong")
                return redirect("signup")

            elif User.objects.filter(username=username).exists():
                messages.info(request, "user taken already")
                return redirect("signup")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect("signup")

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save()
                user.refresh_from_db()
                CreateR(get_object_or_404(User,username=username),city,phone,facebook,photo,about_you)
                current_site = get_current_site(request)
                mail_subject = 'Activate your  account.'
                message = render_to_string('user/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('<h1>Please confirm your email address to complete the registration and back to login</h1>')
        else:
            messages.info(request,"Password not matching")
            return redirect('signup')

    else:
        return redirect('signup')


def OrganizationView(request):
    if request.method=="POST":
        email=request.POST['org_email']
        password=request.POST['password']
        org_name=request.POST['org_name']
        comfirm_password=request.POST['comfirm_password']
        website=request.POST['website']
        city=request.POST['org_city']
        phone=request.POST['org_phone']
        address=request.POST['org_address']
        purpose = request.POST['purpose']
        photo=request.FILES['org_photo']
        if password==comfirm_password:
            if len(password)<8:
                messages.info(request, "password must be 8 character and strong")
                return redirect("signup")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect("signup")

            else:
                user = User.objects.create_user(username=email,email=email,password=password)
                user.save()
                user.refresh_from_db()
                CreateO(get_object_or_404(User,username=email),city,phone,website,address,purpose,photo,org_name)
                current_site = get_current_site(request)
                mail_subject = 'Activate your  account.'
                message = render_to_string('user/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('<h1>Please confirm your email address to complete the registration and back to login</h1>')
        else:
            messages.info(request,"Password not matching")
            return redirect('signup')

    else:
        return redirect('signup')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('<h2>Thank you for your email confirmation. Now you can login your account.</h2>')
    else:
        return HttpResponse('Activation link is invalid!')

def Dashboard(request):
    if request.user.is_authenticated:
        return render(request,'admin/index.html')
    else:
        return redirect('Mainhome')


def CreateMedia(user,title,link,des):
    video_id = link.split('v=')[+1]
    thumbnail_url = f"http://img.youtube.com/vi/{video_id}/sddefault.jpg"
    request = requests.get(thumbnail_url,stream=True)

    lf = tempfile.NamedTemporaryFile()
    for block in request.iter_content(1024*8):
        if not block:
            break
        lf.write(block)
    media = MediaBlog(author=user)
    media.title=title
    media.link=link
    media.description=des
    media.thumbnail.save("thumbnail.jpg",files.File(lf))
def PostMedia(request):
    if request.method=="POST":
        post_title = request.POST['title']
        link = request.POST['link']
        description = request.POST['editor']
        print(post_title,link,description)
        CreateMedia(get_object_or_404(User,username=request.user),post_title,link,description)
        return redirect('postmedia')
    else:
        return render(request,'user/postmedia.html')