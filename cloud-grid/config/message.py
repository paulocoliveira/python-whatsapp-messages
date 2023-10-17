from twilio.rest import Client
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config/config.ini')

def send_whatsapp_message(test_name, result):
    account_sid = config.get('WHATSAPP', 'account_sid')
    auth_token = config.get('WHATSAPP', 'auth_token')
    notification_phone_number = config.get('WHATSAPP', 'notification_phone_number')
    my_twilio_phone_number = config.get('WHATSAPP', 'my_twilio_phone_number')

    client = Client(account_sid, auth_token)

    if result == False:
        content = f'{test_name} - FAILED'
    else:
        content = f'{test_name} - PASSED'

    client.messages.create(
        from_='whatsapp:' + my_twilio_phone_number,
        body=content,
        to='whatsapp:' + notification_phone_number
    )