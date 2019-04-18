from django.http import JsonResponse

# Create your views here.
def ping(request):
    return JsonResponse({
        'message': 'Django-BaaS is running well.'
    })