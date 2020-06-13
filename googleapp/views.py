from django.shortcuts import render, redirect
from .forms import GoogleForm
import re
from .models import Location


def location_view(request):
	if request.method == "POST":
		form = GoogleForm(request.POST)
		if form.is_valid():
			link = form.cleaned_data['map_url']
			url_link = re.findall(r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](!)?)*)", link)
			form = form.save(commit=False)
			form.map_url = url_link[0][0]
			form.user = request.user
			form.save()
			return redirect("/display/")
	else:
		form = GoogleForm()
		context = {"form":form}
		return render(request, "google_form.html", context)

def location_display_view(request):
	location_obj = Location.objects.get(user=request.user)
	context = {'location_obj':location_obj}
	return render(request, "google_form_display.html", context)
