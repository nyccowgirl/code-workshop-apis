"""Using Twilio, sends sms message"""

from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER

# add one of you phone numbers here with no spaces
# exampe: "+15553334444"
to_number = "+---------"

# set a variable call client to an instance of Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# lets make and send the message, add in the missing data
message = client.api.account.messages.create(
        to=to_number,
        from_=TWILIO_NUMBER,
        body="Twilio thinks you are Trang")

print "Message set. Message Id: {}".format(message.sid)
