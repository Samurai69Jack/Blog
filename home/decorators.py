# decorators.py

from functools import wraps
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'You need to log in first.')
            return redirect('login')  # Replace with your custom login URL
        return view_func(request, *args, **kwargs)
    return wrapper
