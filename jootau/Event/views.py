# Create your views here.
from Event.eform import EForm, SearchForm, SubscriptionForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
import Event.models as ev
from SendTweet import *
from SendSms import *
from Event.models import Location, EventType, Event, GeneralUser


def Home(request):
    parameters = {}
    parameters.update(csrf(request))
    parameters["request"] = request
    parameters["type"] = "home"
    parameters["events"] = Event.objects.all()
    return render_to_response("index.html", parameters)


#h4gxrq mp98r2
def EntryForm(request):
    parameters = {}
    parameters.update(csrf(request))
    parameters["request"] = request
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=/event/create/')
    if len(GeneralUser.objects.filter(user=request.user)) == 0:
        return HttpResponseRedirect('/event/subscribe/?next=/event/create/')

    if request.method == 'POST':
        form = EForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.latitude = request.POST["lat"]
            event.longitude = request.POST["lon"]
            event.host = GeneralUser.objects.get(user=request.user)
            event.save()
            parameters['message'] = "Submitted successfully"
            parameters["event"] = event
            #return HttpResponseRedirect('.',)
            print "successfully posted"

    else:
        form = EForm()
        parameters['form'] = form
    return render(request, 'Event/eform.html', parameters)


def Subscription(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/login/?next=/event/subscribe/")
    parameters = {}
    parameters.update(csrf(request))
    parameters["request"] = request
    parameters.update(csrf(request))
    if request.method == 'POST':
        if len(GeneralUser.objects.filter(user=request.user)) != 0:
            form = SubscriptionForm(request.POST, instance=GeneralUser.objects.get(user=request.user))
        else:
            form = SubscriptionForm(request.POST)
        if form.is_valid():
            general_user = form.save(commit=False)
            general_user.user = request.user
            general_user.save()
            form.save_m2m()
            parameters['message'] = "Submitted successfully"

    else:
        print GeneralUser.objects.filter(user=request.user)
        try:
            form = SubscriptionForm(instance=GeneralUser.objects.get(user=request.user))
        except:
            form = SubscriptionForm()
        parameters['form'] = form
    return render_to_response('Event/subscription.html', parameters)


@csrf_exempt
def event_list(request):
    parameters = {}
    parameters.update(csrf(request))
    #There is form in search or at beginning surfing of the page
    parameters["request"] = request
    form = SearchForm()
    parameters['form'] = form
    
    if request.method != 'GET':
        parameters["events"] = Event.objects.all()
        return render_to_response('index.html', parameters)

    form = SearchForm(request.GET)
    args = {}
    kargs = {}
    args['date'] = request.GET.get('date')
    try:
        args['location'] = Location.objects.get(pk=int(request.GET.get('location')))
    except:
        pass
    try:
        args['event_type'] = EventType.objects.get(pk=int(request.GET.get('event_type')))
    except:
        pass

    for i in args:
        if args[i]:
            kargs[i] = args[i]

    events = Event.objects.filter(**kargs)
    parameters['events'] = events
    print parameters
    return render_to_response("index.html", parameters)


def event_page(request, event_id):
    '''Gives the details of the event'''
    if request.method == 'POST':
        post_type = request.POST['my_type']
        event_id = request.POST['id']
        if post_type == "tweet":
            send_tweet(event_id)
            return HttpResponse("Tweeted succesfully")

        if post_type == "sms":
            send_sms(event_id)
            return HttpResponse("SMS succesful")

    if len(ev.Event.objects.filter(id=event_id)) == 0:
        return HttpResponse("No such event id found")
    event = ev.Event.objects.get(id=event_id)
    parameters = {}
    parameters.update(csrf(request))
    parameters["request"] = request
    parameters['event'] = event
    return render(request, 'Event/event_page.html', parameters)


def profile_page(request):
    ''' Profile page of the user '''
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/login/?next=/event/subscribe/")
    user = GeneralUser.objects.get(user=request.user)
    parameters = {}
    parameters['user'] = user
    events = []
    # print user.subscription.all().location
    for subs in user.subscription.all():
        events.extend(Event.objects.filter(location=subs.location, event_type=subs.event_type))
    print events
    parameters["events"] = set(events)
    parameters["request"] = request
    return render_to_response('registration/profile_page.html', parameters)
