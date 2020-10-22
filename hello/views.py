from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import argparse
import os
import pickle
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from .picker import NBAPicker
import json

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    filename = "nba-player.csv"
    with open(os.path.join(".","staticfiles", filename), "rb") as f:
        ratings = pd.read_csv(f,names=("player","salary","team","position","team-agaisnt","ceiling","floor","points"))

    model = NBAPicker()
    team = model.pick(ratings)
    result = team.to_json()
    parsed = json.loads(result)
    return render(request, "index.html", {"result": parsed})

def pickTeam(request):
    filename = "nba-player.csv"
    with open(os.path.join(".","staticfiles", filename), "rb") as f:
        ratings = pd.read_csv(f,names=("player","salary","team","position","team-agaisnt","ceiling","floor","points"))

    model = NBAPicker()
    team = model.pick(ratings)
    result = team.to_json()
    parsed = json.loads(result)
    return HttpResponse( json.dumps( parsed ))

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
