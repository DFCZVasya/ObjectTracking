import random

class ObjectTracking(object) :

    def __init__(self, classID):
        self.classID = classID
        self.probability = 0.1
        self.bbox = []
        self.id = 0


    def createNewID(self, bbox, allObjects):
        id = random.randint(1,9999)
        unicID = False

        while unicID != True and len(allObjects) != 0:
            for object in allObjects:
                if object.id == id:
                    id = random.randint(1,9999)
                    unicID = False
                else:
                    unicID = True

        self.id = id
        self.bbox = bbox

    def tracking(self, newbbox, allObjects):
        for object in allObjects:
            if object.id == self.id:
                oldx = range(self.bbox[0], self.bbox[2])
                oldy = range(self.bbox[1], self.bbox[3])
                newx = range(newbbox[0], newbbox[2])
                newy = range(newbbox[1], newbbox[3])
                xintersection = []
                yintersection = []

                for pixel in newx:
                    if pixel in oldx:
                        xintersection.append(pixel)

                for pixel in newy:
                    if pixel in oldx:
                        yintersection.append(pixel)
                k = 0
                if len(xintersection) != 0 and len(yintersection) != 0:
                    sqold = (self.bbox[2] - self.bbox[0]) * (self.bbox[3] - self.bbox[1])
                    xintersectionMin = min(xintersection)
                    yintersectionMin = min(yintersection)
                    xintersectionMax = max(xintersection)
                    yintersectionMax = max(yintersection)
                    sqintersection = (xintersectionMax - xintersectionMin) * (yintersectionMax - yintersectionMin)

                    k = sqintersection / sqold

                if k >= 0.01:
                    if self.probability <= 1.0:
                        self.probability += 0.1
                    self.bbox = newbbox
                    return 0
                else:
                    self.probability -= 0.1
                    if self.probability == 0 or self.probability <= 0:
                        deletObject()


    def deletObject(self):
        return self.id

    def getIntersection(self, newbbox):
        oldx = range(self.bbox[0], self.bbox[2])
        oldy = range(self.bbox[1], self.bbox[3])
        newx = range(newbbox[0], newbbox[2])
        newy = range(newbbox[1], newbbox[3])
        xintersection = []
        yintersection = []

        for pixel in newx:
            if pixel in oldx:
                xintersection.append(pixel)

        for pixel in newy:
            if pixel in oldx:
                yintersection.append(pixel)

        if len(xintersection) != 0 and len(yintersection) != 0:
            sqold = (self.bbox[2] - self.bbox[0]) * (self.bbox[3] - self.bbox[1])
            xintersectionMin = min(xintersection)
            yintersectionMin = min(yintersection)
            xintersectionMax = max(xintersection)
            yintersectionMax = max(yintersection)
            sqintersection = (xintersectionMax - xintersectionMin) * (yintersectionMax - yintersectionMin)

            k = sqintersection / sqold
            return k

        else:
            return 0
