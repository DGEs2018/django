from django.shortcuts import render
# Create your views here.

# from django.http import HttpResponse

# def landingpage(request):
#     return HttpResponse('<h1>Portfolio Homepage</h1>')

personaldetails = [
    {
        'name': 'Dawit G',
        'birthdate': 1988,
        'birthplace': 'Addis Ababa',
        'profession': 'striver',
        'hobby': 'learning',
    },

    {
        'name': 'Whoever',
        'birthdate': 1985,
        'birthplace': 'Stockholm',
        'profession': 'tennis champion',
        'hobby': 'jogging'
    }
]
def landingpage(request):
    return render(request, 'my_portfolio/landingpage.html')

def aboutme(request):
    context = {
        'personaldetails': personaldetails
    }
    return render(request, 'my_portfolio/about.html', context)
    # return HttpResponse('<h1> All about?</h1>')

