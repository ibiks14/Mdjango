from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm
#from django.http import HttpResponse

def index(request):
    return render(request, 'tolls/home.html')
    #return HttpResponse('Hello, world!')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'tolls/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'tolls/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('balls:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tolls/new_topic.html', context)


# Create your views here.
