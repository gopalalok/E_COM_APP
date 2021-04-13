from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        if request.user.is_authenticated  and returnUrl =="/login/":
            return redirect("/")

        response = get_response(request)

        return response

    return middleware