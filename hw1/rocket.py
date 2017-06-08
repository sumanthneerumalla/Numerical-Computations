#initial conditions
time = 0
timeStep = 0.1
height = 0
velocity = 0 
acceleration = 0 
position = 0 
totalForce = 0
rocketMass = 0.034
engineInitial = 0.0242
engineFinal  = 0.0094
mass = rocketMass + engineInitial

def bodyDrag(velocity):
    drag = 0
    coefficient = 0.45
    rho =  1.293
    area = 0.000506
    drag = coefficient * rho * area* ( velocity * velocity) / 2
    return drag

def finDrag(velocity):
    drag = 0
    coefficient = 0.01
    rho =  1.293
    area = 0.00496
    drag = coefficient * rho * area* ( velocity * velocity) / 2
    return drag

def forceGravity(mass):
    return mass * 9.80665

def latestForce(thrust,velocity,mass):
    result = thrust - (bodyDrag(velocity) + finDrag(velocity) + forceGravity(mass))
    return result

def getAcceleration(thrust):
    return latestForce(thrust,velocity,mass) / mass

def changeInVelocity(acceleration,timeStep):
    return acceleration * timeStep#0.1


def getVelocity(velocity,acceleration):
    return velocity + changeInVelocity(acceleration,timeStep)

def changeInDistance(velocity):
    return velocity * timeStep#0.1

def getPosition(position,velocity):
    return position + changeInDistance(velocity)

def massUpdate(mass,thrust):
    return mass - (0.0001644 * thrust)
    

forceArray = [0,5.5,12,5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,0]

time = 0 

for thrust in forceArray:
    time = time + timeStep
    acceleration = getAcceleration(thrust)
    dv = changeInVelocity(acceleration,timeStep)
    velocity = getVelocity(velocity,acceleration)
    dPosition = changeInDistance(velocity)
    position = getPosition(position,velocity)
    mass = massUpdate(mass,thrust)
    if(position< 0):
        position = 0 
        if(velocity< 0):
            velocity = 0


    print( "time: ", time)
    print( "position: ", position)
    print( "velocity: ", velocity)
    print( "acceleration: ", acceleration)
    print( "mass: ", mass)
    print()

#    if (velocity < 0):
 #       break

        #converted float decimals to ints that represent one tenth of a second
#               for i in range(0,20):
#  print("time: ",i/10)

print("********************Rocket burn finished, continuing ascent*********")

while(velocity > 0):
    time = time + timeStep
    acceleration = getAcceleration(thrust)
    dv = changeInVelocity(acceleration,timeStep)
    velocity = getVelocity(velocity,acceleration)
    dPosition = changeInDistance(velocity)
    position = getPosition(position,velocity)
    mass = massUpdate(mass,thrust)
    if(position< 0):
        position = 0 



    print( "time: ", time)
    print( "position: ", position)
    print( "velocity: ", velocity)
    print( "acceleration: ", acceleration)
    print( "mass: ", mass)
    print()
