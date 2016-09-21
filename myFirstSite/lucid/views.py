from django.shortcuts import render
from .models import Story, Character, CharacterAtt, PlotPoint
# Create your views here.
from django.http import HttpResponse


def index(request):
	latest_story_list = Story.objects.order_by('-pub_date')
	context = {'latest_story_list': latest_story_list}
	return render(request, 'lucid/index.html', context)

def detail(request, story_id):
    return HttpResponse("Details of story %s." % story_id)

def results(request, story_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % story_id)

def vote(request, story_id):
    return HttpResponse("You're voting on question %s." % story_id)

def playGame(request,story_id):
	currentStory = Story.objects.get(pk=story_id)
	storyCharacters = currentStory.character_set.all()
	plotPoints = currentStory.plotpoint_set.all()
	#storyCharactersAtt = storyCharacters.characteratt_set.all()
	context = {'currentStory' : currentStory, 'storyCharacters' : storyCharacters, 
				'plotPoints' : plotPoints}
	return render(request, 'lucid/playGame.html', context)