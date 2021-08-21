from profiles.models import Profile
from django.shortcuts import render

# Create your views here.

def my_recommendations_view(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profiles()
    context= {'my_recs':my_recs}
    return render(request, 'profiles/recolist.html', context)
