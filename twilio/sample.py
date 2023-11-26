from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

client.messages.create(
  from_='whatsapp:+19876543210',
  body='Hello! This message is automated using Twilio.',
  to='whatsapp:+1234567890'
)