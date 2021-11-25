from library.sms.mellipayamak import Api
from django.conf import settings

class Sms():
    def __init__(self):
        self.username = settings.SMS_USERNAME
        self.password = settings.SMS_PASSWORD
        self.number = settings.SMS_NUMBER

    def sendsms(self, message=[] , mobileNumbers=[]):
        api = Api(self.username, self.password)
        sms = api.sms('soap')
        to = mobileNumbers
        _from = self.number
        text = message
        response = sms.send(to, text, _from)
        return response

    def send_template(self):
        api = Api(self.username, self.password)
        sms = api.sms('soap')
        to = '09190661327'
        _from = self.number
        text = '2050'
        bodyId = 66350
        response = sms.send_by_base_number(text, to, bodyId)
        return response