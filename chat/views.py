from django.contrib.auth import authenticate, login as auth_login  # Rename login import
from django.shortcuts import render, redirect
from chat.models import CustomUser
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv
import openai
import os

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.create_user(
            username=username, email=email, password=password, fullname=fullname
        )
        auth_login(request, user)  # Use auth_login instead of login
        # Replace 'login' with your desired URL name
        return redirect('login')
    return render(request, 'signup.html')


def login_view(request):  # Rename login function
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use auth_login instead of login
                # Redirect to the chat page after successful login
                return redirect('chat')
            else:
                return redirect('loginerror')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'landing.html')


@login_required(login_url='login')
def chat(request):
    chat_response = None
    if request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"Respond like a therapist to in yoruba {user_input}",
            max_tokens=256,
            stop=".",
            temperature=0.5
        )
        print(response)

        chat_response = response["choices"][0]["text"]
    return render(request, 'message.html', {"response": chat_response})
