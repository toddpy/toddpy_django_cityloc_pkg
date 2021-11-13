from django.shortcuts import render

# Create your views here.
def loc_nyc(request):
    """ 
    Display the content for the NYC location 
    
    """

    return render(request, 'citylocations/loc_nyc.html', {})

