from django.http import JsonResponse

# Create your views here.


def get_api_info(request):
    return JsonResponse({
        "api": {
            "version": "0.0.1",
            "status": "active",
        }
    })


def page_list(request):
    return JsonResponse({
        "/api": {
            "description": "Main endpoint for api",
            "status": "IN_PROGRESS",
        }
    })