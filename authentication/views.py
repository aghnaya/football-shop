from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

    import json

    # default: ambil dari POST biasa
    username = request.POST.get('username')
    password1 = request.POST.get('password1') or request.POST.get('password')
    password2 = request.POST.get('password2') or request.POST.get('password')

    # kalau POST kosong, coba baca JSON
    if not username:
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password1 = data.get('password1') or data.get('password')
            password2 = data.get('password2') or data.get('password')
        except:
            pass

    if not username or not password1 or not password2:
        return JsonResponse({'status': 'error', 'message': 'username/password required'}, status=400)

    if password1 != password2:
        return JsonResponse({'status': 'error', 'message': 'Passwords do not match.'}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'status': 'error', 'message': 'Username already exists.'}, status=400)

    user = User.objects.create_user(username=username, password=password1)
    return JsonResponse({'status': 'success', 'username': user.username}, status=201)

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        # mendukung form-data dan JSON
        try:
            data = request.POST
            username = data.get('username') or (request.body and __import__('json').loads(request.body).get('username'))
            password = data.get('password') or (request.body and __import__('json').loads(request.body).get('password'))
        except Exception:
            return JsonResponse({'status': 'error', 'message': 'Invalid payload'}, status=400)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({'status': True, 'username': user.username, 'message': 'Login successful!'}, status=200)
            return JsonResponse({'status': False, 'message': 'Account disabled'}, status=403)
        return JsonResponse({'status': False, 'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


@csrf_exempt
def logout_api(request):
    if request.method == 'POST':
        auth_logout(request)
        return JsonResponse({'status': 'success', 'message': 'Logout successful!'}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
