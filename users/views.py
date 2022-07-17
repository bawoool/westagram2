import json, re
import bcrypt

from django.http import JsonResponse
from django.views import View

from .models import User

# Create your views here.

class SignUpView(View):
    def post(self, request): 
        try: 
            data     = json.loads(request.body)
            name     = data['name']
            email    = data['email']
            password = data['password']
            phone    = data['phone']

            email_check = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            password_check = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"

            if not re.match(email_check, email): 
                return JsonResponse({'message' : 'invalid_email'}, status=400)

            if not re.match(password_check, password): 
                return JsonResponse({'message' : 'invalid_password'}, status=400)

            if User.objects.filter(email=email).exists(): 
                return JsonResponse({'message' : 'existent_email'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name     = name,
                email    = email,
                password = hashed_password,
                phone    = phone,
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
        except KeyError: 
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
            
            

