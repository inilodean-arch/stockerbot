from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

def send_whatsapp_message(to, message):
    from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
    
    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to='whatsapp:' + to
    )
    
    return message.sid

# Example usage
if __name__ == '__main__':
    recipient = '+1234567890'  # Replace with the recipient's number
    msg = 'Hello from Twilio WhatsApp!'  
    message_sid = send_whatsapp_message(recipient, msg)
    print('Message sent with SID:', message_sid)