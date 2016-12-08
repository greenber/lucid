from django.shortcuts import render
from .models import Story, Character, CharacterAtt, PlotPoint
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def index(request):
	print "uyoiyuoyiy"
	latest_story_list = Story.objects.order_by('-pub_date')
	context = {'latest_story_list': latest_story_list}
	return render(request, 'lucid/index.html', context)

def addStory(request):
	print "Hljlfjasldfjsld"
	newStory = Story(storyName = request.POST['storName'], pub_date=timezone.now())
	newStory.save()
	return HttpResponseRedirect(reverse('index'))


#Attributes 
def detail(request, story_id):
    p = Story.objects.get(pk=story_id)
   # print p
    c = p.character_set.get(characterName = request.POST['charAtt'])
   # print c
   # print c.characteratt_set.all
    c.characteratt_set.create(attrib = request.POST['charName'])
    #print request.POST['charAtt']
    c.save()
    return HttpResponseRedirect(reverse('playGame', args=(story_id,)))

def results(request, story_id):
    p = Story.objects.get(pk=story_id)
    p.character_set.create(characterName = request.POST['charName'])
    p.save()
    return HttpResponseRedirect(reverse('playGame', args=(story_id,)))

#PlotPoints
def vote(request, story_id):
	p = Story.objects.get(pk=story_id)

	#print "things and stuff"
	#print request.POST
	#print request.POST['Plot Point']
	p.plotpoint_set.create(point = request.POST['Plot Point'])
	p.save()
	return HttpResponseRedirect(reverse('playGame', args=(story_id,)))

#Delete a plot point
def delPoint(request, story_id):
	print "hehejejejejeejej"
	p = Story.objects.get(pk=story_id)
	
	#print request.POST['plotPoint']
	postRequest = request.POST.get('plotPoint', False)
	print postRequest

	c=p.plotpoint_set.get(point = postRequest)
	c.delete()
	p.save()
	return HttpResponseRedirect(reverse('playGame', args=(story_id,)))

def playGame(request,story_id):
	currentStory = Story.objects.get(pk=story_id)
	storyCharacters = currentStory.character_set.all()
	plotPoints = currentStory.plotpoint_set.all()
	#storyCharactersAtt = storyCharacters.characteratt_set.all()
	context = {'currentStory' : currentStory, 'storyCharacters' : storyCharacters, 
				'plotPoints' : plotPoints}
	return render(request, 'lucid/playGame.html', context)









