from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
# Create your views here.

def home(request):

	# # THIS IS HOW YOU CHECK THE USER/ADMIN LOGIN
	# title = "Hello"
	# if request.user.is_authenticated():
	# 	title = 'Hello %s' %(request.user)

	# if request.method == 'POST':
	# 	print request.POST

	form = SignUpForm(request.POST or None)
	context = {
		"form":form
	}

	if form.is_valid():
		instance = form.save(commit = False)
		# # SOME STUFF REGARDING FORM DATA
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		# print instance.email
		# print instance.full_name
		instance.save()

	return render(request, "home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key, value in form.cleaned_data.iteritems():
			print key, value
		form_full_name = form.cleaned_data.get("full_name")
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")

		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, "zafarullahmahmood777@gmail.com"]

		contact_message = '%s\n%s\n%s' %(
			form_full_name, 
			form_email, 
			form_message)

		send_mail('Feedback', contact_message, from_email, to_email, fail_silently=False)

	context = {
		"form": form,
	}
	return render(request, "contact.html", context)
















