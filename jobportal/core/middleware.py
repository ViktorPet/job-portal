from django.shortcuts import redirect

class RoleBasedMiddleware: 
    def __init__(self,get_response):
        self.get_response = get_response 
        
        
    def __call__(self, request):
        
        user = request.user 
        path = request.path 
        
        if path.startswith('/company') and getattr(user,'role', None) != 'employer': 
            return redirect('/') # not authorized
        
        if path.startswith('/profile') and getattr(user,'role', None) != 'employee': 
            return redirect('/') # not authorized
        
        response = self.get_response(request)
        
        
        return response
    