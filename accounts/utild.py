from email.policy import default

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import  get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from pyexpat.errors import messages
from django.core.mail import EmailMessage

def detectUser(user):
    if user.role == 1:
        redirecturl = 'vendorDashboard'
        return redirecturl
    elif user.role == 2:
        redirecturl = 'custDashboard'
        return redirecturl
    elif user.role == None and user.is_superadmin:
        redirecturl = '/admin'
        return redirecturl



def send_verification_email(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Please Activate your account'
    messages = render_to_string('accounts/emails_verification_email.html',
   {'user': user,
    'domain': current_site,
    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    'token': default_token_generator.make_token(user),


    })
    to_email = user.email
    mail = EmailMessage(mail_subject, messages, to=[to_email])
    mail.send()

