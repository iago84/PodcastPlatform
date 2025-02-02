from django.shortcuts import render


def cookie_policy(request):
	return render(request, 'policies_app/cookie_policy.html')


def legal_advise(request):
	return render(request, 'policies_app/legal_advise.html')


def terms_and_conditions(request):
	return render(request, 'policies_app/terms_and_conditions.html')


def privacy_policy(request):
	return render(request, 'policies_app/privacy_policy.html')
