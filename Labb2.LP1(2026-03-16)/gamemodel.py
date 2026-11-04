from math import sin,cos,radians
import random



class Game:
    def __init__(self, cannonSize, ballSize):
        self.cannonSize = cannonSize    
        self.ballSize = ballSize
        self.players = [Player(self, False, -90, "blue"), Player(self, True, 90, "red")]
        self.turn = False #används för att kika vems tur det är
        self.currentWind = random.random() * 20 - 10
        

    def getPlayers(self):
        return self.players 
    
    def getCannonSize(self):
        return self.cannonSize 

    def getBallSize(self):
        return self.ballSize 

    def getCurrentPlayer(self):
        return self.players[self.turn]
        

    def getOtherPlayer(self):
        return self.players[not self.turn]

      
    
    def getCurrentPlayerNumber(self):
        return int(self.turn)    
    
    def nextPlayer(self):
        if self.turn == False:
            self.turn = True
        else:
            self.turn = False
        return self.turn 

    def setCurrentWind(self, wind):
        self.currentWind = wind

    
    def getCurrentWind(self):
        return self.currentWind
        

    def newRound(self):
        self.currentWind = random.random() * 20 - 10
        

class Player:
    def __init__(self, game, isReversed, x, color):
        self.isReversed = isReversed
        self.x = x
        self.color = color
        self.game = game 

        self.score = 0 
        self.angle = 45
        self.velocity = 40

    
    def fire(self, angle, velocity):
        self.velocity = velocity
        self.angle = angle

        wind = self.game.getCurrentWind() 
        xPos = self.x 
        yPos = (self.game.getCannonSize()/2)
        
        if self.isReversed == True:
            angle = 180 - angle
        
        return Projectile(angle, velocity, wind, xPos, yPos, -110, 110) # behöve inte spara projectilen då den enbart används en gång
        
            
        
       

    def projectileDistance(self, proj):
        cannon_posX = self.getX()
        projectile_posX = proj.getX()

        cannonSize = self.game.getCannonSize()
        ballSize = self.game.getBallSize()

        distance = projectile_posX - cannon_posX
        center_distance = cannonSize / 2 + ballSize  

        if distance > center_distance:
            return distance - center_distance

        elif distance < -center_distance:
            return distance + center_distance


        else:
            return 0



    def getScore(self):
        return self.score 

    def increaseScore(self):
        self.score += 1 

    def getColor(self):
        return self.color 

    def getX(self):
        return self.x 

    def getAim(self):
        return self.angle, self.velocity 



class Projectile:
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind


    
    def update(self, time):
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        self.yPos = max(self.yPos, 0)
        
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        self.yvel = yvel1
        self.xvel = xvel1
        
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
