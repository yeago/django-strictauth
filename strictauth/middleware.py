from django.contrib.auth import logout

from django.utils.deprecation import MiddlewareMixin

class StrictAuthentication(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
       if request.session.accessed and request.user.is_authenticated() and not request.user.is_active:
          logout(request)
