from django.db import models
from django.forms import forms

from ImportNodes import api

class search_query(models.Model):
    
    def __init__(self):
        self.name = models.CharField(max_length=30)

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.coords = [x, y]

    def to_str(self):  # for debug
        return "id: " + self.id + ", coords: [" + self.coords[0] + ", " + self.coords[1] + "]"


class Way(models.Model):
    name =  models.CharField(max_length=30)
    def __init__(self, id, nodes, tags):
        self.id = id
        self.nodes = nodes  # list of Nodes
        self.tags = tags  # dictionary with random info about the way
        self.name = models.CharField(max_length=30)

    def __str__(self):
        return self.id, self.name, self.tags



