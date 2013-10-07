import urllib2
import urllib
import Event.models as ev


def send_sms(event_id):
    
    # number = '9842227969'
    event = ev.Event.objects.get(id=event_id)
    users = ev.GeneralUser.objects.filter(subscription__location=event.location)
    url = "http://localhost:8000/event/"+str(event.id)

    users = ev.GeneralUser.objects.filter(subscription__location=event.location, subscription__event_type=event.event_type)
    msg = event.title[0:60]+ " at " + event.location.name +" on " + str(event.date) + " at " + str(event.time) + " " + url
    client_id = 'apisignup'
    username = 'nkandel'
    password = 'GluZbsQl'

    from_ = '5455'
    text = urllib.quote(msg)

    for usr in users:
        api_url = 'http://api.sparrowsms.com/call_in.php?client_id=' + client_id + '&username=' + \
            username + '&password=' + password + '&from=' + \
            from_ + '&to=' + usr.phone + '&text=' + text
        request = urllib2.Request(api_url)
        response = urllib2.urlopen(request)
        page = response.read()
    print text
    return "done"

