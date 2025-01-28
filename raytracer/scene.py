
from sphere import *

class Scene():
    def __init__(self, objects):
        self.objects = objects

    def Add(self, object):
        self.objects.append(object)

    def Clear(self):
        self.objects.clear()

    def Trace(self, r, tMin, tMax, record):
        tempRec = HitRecord()
        hitAnything = False
        closesSoFar = tMax

        for object in self.objects:
            if object.Hit(r, tMin, closesSoFar, tempRec):
                hitAnything = True
                closesSoFar = tempRec.t
                record[0] = tempRec


        return hitAnything
