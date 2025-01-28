import numpy as np
from math import sqrt


class HitRecord():
    p = np.array([0,0,0])
    normal = np.array([0,0,0])
    t = 0.0
    frontFace = None

    def SetFaceNormal(self, r, outwardNormal):
        frontFace = np.dot(r.direction, outwardNormal) < 0
        if frontFace:
            self.normal = outwardNormal
        else:   
            self.normal = -outwardNormal
    

class Sphere():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def Hit(self, r, tMin, tMax, rec):
        oc = r.origin - self.center
        a = np.dot(r.direction, r.direction)
        b = np.dot(oc, r.direction)
        c = np.dot(oc, oc) - self.radius*self.radius
        discriminant = b*b - a*c
        if (discriminant < 0):
            return False
        
        sqrtd = sqrt(discriminant)

        root = (-b - sqrtd) / a
        if (root < tMin or tMax < root):
            root = (-b + sqrtd) / a
            if (root < tMin or tMax < root):
                return False

        rec.t = root
        rec.p = r.At(rec.t)
        outwardNormal = (rec.p - self.center) / self.radius
        rec.SetFaceNormal(r, outwardNormal)

        return True
