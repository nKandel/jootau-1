import tweetpony
from .models import Event, GeneralUser


def send_tweet(event_id):
    CONSUMER_KEY = "vbu0rPw39tCEtIEDfZK5g"
    CONSUMER_SECRET = "gB235sqx1GrJZKHde5y4ZaNyVawQ0oaGolQTRVEz0"
    ACCESS_TOKEN = "137592952-RGzgPZu4lRUegsMZEHv6DzXQGOuXtZ8SCqLRUS3m"
    ACCESS_TOKEN_SECRET = "RX51tm1UihA889TtW4rARKROuYV4sPgoInnB3QwqxCg"

    api = tweetpony.API(consumer_key=CONSUMER_KEY,
                        consumer_secret=CONSUMER_SECRET,
                        access_token=ACCESS_TOKEN,
                        access_token_secret=ACCESS_TOKEN_SECRET
                        )

    event = Event.objects.get(id=event_id)
    
    url = "http://localhost:8000/event/"+str(event.id)

    users = GeneralUser.objects.filter(subscription__location=event.location, subscription__event_type=event.event_type)
    msg = event.title[0:60]+ " at " + event.location.name +" on " + str(event.date) + " at " + str(event.time) + "  " + url
    for usr in users:
        try:
            api.send_message(text=msg, screen_name=usr.twitter)

        except tweetpony.APIError as err:
            print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)

        else:
            print "Yay! Your tweet has been sent!"

# user = api.user
# print "Hello, @%s!" % user.screen_name
# text = "Tweet via API"
# try:
#     # api.update_status(status=text)
#     api.send_message(text="hello pandey", screen_name="errajsubit")
# except tweetpony.APIError as err:
#     print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
# else:
#     print "Yay! Your tweet has been sent!"

# # send_message': {
#       'endpoint': "direct_messages/new.json",
#       'post': True,
#       'url_params': [],
#       'required_params': ['text'],
#       'optional_params': ['user_id', 'screen_name'],
#       'model': Message,
#   },