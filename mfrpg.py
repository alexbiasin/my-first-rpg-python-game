# ! / b i n / p y t h o n 3
from typing import List
import io
import sys
#import aalib
#import PIL.Image
import random

# This is my first RPG Python game, based on the Raspberry-Pi begginers guide one

# EJ: print (randomString(['uno','dos','tres','cuatro']))
def randomString(stringList):
    selected = random.choice(stringList)
    return selected

def loadAscii(imagefile):
    file_object  = open(imagefile, 'r')
    return file_object.read()

def asciiArt():
    asciiWidth = 56
    asciiHeight = 28
    global hallScreen
    hallScreen = loadAscii("hall.scr")
    #hallScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"hall.png").convert('L').resize(hallScreen.virtual_size)
    #hallScreen.put_image((0, 0), aimage)
    global hall2Screen
    hall2Screen = loadAscii("hall2.scr")
    #hall2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"hall2.png").convert('L').resize(hall2Screen.virtual_size)
    #hall2Screen.put_image((0, 0), aimage)
    global kitchenScreen
    kitchenScreen = loadAscii("kitchen.scr")
    #kitchenScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"kitchen.png").convert('L').resize(kitchenScreen.virtual_size)
    #kitchenScreen.put_image((0, 0), aimage)
    global kitchen2Screen
    kitchen2Screen = loadAscii("kitchen2.scr")
    #kitchen2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"kitchen2.png").convert('L').resize(kitchen2Screen.virtual_size)
    #kitchen2Screen.put_image((0, 0), aimage)
    global basementScreen
    basementScreen = loadAscii("basement.scr")
    #basementScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"basement.png").convert('L').resize(basementScreen.virtual_size)
    #basementScreen.put_image((0, 0), aimage)
    global basement2Screen
    basement2Screen = loadAscii("basement2.scr")
    #basement2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"basement2.png").convert('L').resize(basement2Screen.virtual_size)
    #basement2Screen.put_image((0, 0), aimage)
    global diningScreen
    diningScreen = loadAscii("dining.scr")
    #diningScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"dining.png").convert('L').resize(diningScreen.virtual_size)
    #diningScreen.put_image((0, 0), aimage)
    global dining2Screen
    dining2Screen = loadAscii("dining2.scr")
    #dining2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"dining2.png").convert('L').resize(dining2Screen.virtual_size)
    #dining2Screen.put_image((0, 0), aimage)
    global uphallScreen
    uphallScreen = loadAscii("uphall.scr")
    #uphallScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"uphall.png").convert('L').resize(uphallScreen.virtual_size)
    #uphallScreen.put_image((0, 0), aimage)
    global uphall2Screen
    uphall2Screen = loadAscii("uphall2.scr")
    #uphall2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"uphall2.png").convert('L').resize(uphall2Screen.virtual_size)
    #uphall2Screen.put_image((0, 0), aimage)
    global bedroomScreen
    bedroomScreen = loadAscii("bedroom.scr")
    #bedroomScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"bedroom.png").convert('L').resize(bedroomScreen.virtual_size)
    #bedroomScreen.put_image((0, 0), aimage)
    global bedroom2Screen
    bedroom2Screen = loadAscii("bedroom2.scr")
    #bedroom2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"bedroom2.png").convert('L').resize(bedroom2Screen.virtual_size)
    #bedroom2Screen.put_image((0, 0), aimage)
    global bathroomScreen
    bathroomScreen = loadAscii("bathroom.scr")
    #bathroomScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"bathroom.png").convert('L').resize(bathroomScreen.virtual_size)
    #bathroomScreen.put_image((0, 0), aimage)
    global bathroom2Screen
    bathroom2Screen = loadAscii("bathroom2.scr")
    #bathroom2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"bathroom2.png").convert('L').resize(bathroom2Screen.virtual_size)
    #bathroom2Screen.put_image((0, 0), aimage)
    global corridorScreen
    corridorScreen = loadAscii("corridor.scr")
    #corridorScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"corridor.png").convert('L').resize(corridorScreen.virtual_size)
    #corridorScreen.put_image((0, 0), aimage)
    global corridor2Screen
    corridor2Screen = loadAscii("corridor2.scr")
    #corridor2Screen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"corridor2.png").convert('L').resize(corridor2Screen.virtual_size)
    #corridor2Screen.put_image((0, 0), aimage)
    global gardenScreen
    gardenScreen = loadAscii("garden.scr")
    #gardenScreen = aalib.AsciiScreen(width=asciiWidth, height=asciiHeight)
    #aimage = PIL.Image.open(r"garden.png").convert('L').resize(gardenScreen.virtual_size)
    #gardenScreen.put_image((0, 0), aimage)


def showInstructions():
    #print a main menu and the commands
    print('''
Alex's first Python RPG Game (v1.1): Try to escape, if you can!
========
Commands:
  go [direction]
  get [item]
  use [item] with [object]
  quit ''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    
    if currentRoom == 'Hall' :
        if ('key' in inventory):
            #print (hall2Screen.render())
            print (hall2Screen)
        else:
            print (hallScreen)    
    if currentRoom == 'Kitchen' :
        if ('item' in rooms[currentRoom]['items']) and ('monster' in rooms[currentRoom]['items']['item']):
            print (kitchenScreen)
        else:
            print (kitchen2Screen)
    if currentRoom == 'Basement' :
        if ('wand' in inventory):
            print (basement2Screen)
        else:
            print (basementScreen)
    if currentRoom == 'Dining Room' :
        if ('potion' in inventory):
            print (dining2Screen)
        else:
            print (diningScreen)
    if currentRoom == 'Upstairs Hallway' :
        if ('cloak' in inventory):
            print (uphall2Screen)
        else:
            print (uphallScreen)
    if currentRoom == 'Bedroom' :
        if ('book' in inventory):
            print (bedroom2Screen)
        else:
            print (bedroomScreen)
    if currentRoom == 'Bathroom' :
        if ('spray' in inventory):
            print (bathroom2Screen)
        else:
            print (bathroomScreen)
    if currentRoom == 'Corridor' :
        if ('locked door' in rooms[currentRoom]['items']['item']):
            print (corridorScreen)
        else:
            print (corridor2Screen)
    if currentRoom == 'Garden' :
        print (gardenScreen)
    
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]['items']:
        print('You see a ' + rooms[currentRoom]['items']['item'])
    print("Possible moves: " + str(list(rooms[currentRoom]['directions'].keys()))) # se obtienen los "keys" del array
    print("---------------------------")

#an inventory, which is initially empty
inventory = [] # type: List[str]

# a dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                'directions' : {
                   'south' : 'Kitchen',
                   'east' : 'Dining Room',
                   'stairs' : 'Upstairs Hallway'
                  },
                'items' : {
                   'item' : 'key'
                  }
                },
            'Kitchen' : {
                'directions' : {
                   'north' : 'Hall'
                  },
                'items' : {
                   'item' : 'monster'
                  }
                },
            'Basement' : {
                'directions' : {
                   'east' : 'Kitchen'
                  },
                'items' : {
                   'item' : 'wand'
                  }
                },
            'Dining Room' : {
                'directions' : {
                   'west' : 'Hall',
                   'south' : 'Corridor'
                  },
                'items' : {
                   'item' : 'potion'
                  }
                },
            'Upstairs Hallway' : {
                'directions' : {
                    'east' : 'Bedroom',
                    'west' : 'Bathroom',
                    'stairs' : 'Hall'
                  },
                'items' : {
                    'item' : 'cloak'
                  }
                },
            'Bedroom' : {
                'directions' : {
                    'west' : 'Upstairs Hallway'
                  },
                'items' : {
                    'item' : 'book'
                  }
                },
            'Bathroom' : {
                'directions' : {
                    'east' : 'Upstairs Hallway'
                  },
                'items' : {
                    'item' : 'spray'
                  }
                },
            'Corridor' : {
                'directions' : {
                   'north' : 'Dining Room',
                   #'south' : 'Garden'
                  },
                'items' : {
                    'item' : 'locked door'
                    }
                },
            'Garden' : {
                'directions' : {
                   'north' : 'Corridor'
                  },
                'items' : {}
                }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

asciiArt() # cargar las imagenes como ascii

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    inputstr = ''
    while inputstr == '':
        # If you're using Python 2.7 (or anything earlier than Python 3), you need
        # to change your input(...) command to use raw_input(...)
        if sys.version_info[0] < 3:
            inputstr = raw_input('> ')
        else:
            inputstr = input('> ')
    
    print(" ")
    move = inputstr.lower().split()

    # Acciones
    if (len(move)==1) and ( (move[0] == 'quit') or (move[0] == 'exit') ): #if they want to leave
        print(randomString(['Bye bye!','Hope to see you again!','Don\'t give up next time.','We\'ll miss you...']))
        quit()
    if (move[0] == 'go') and (len(move)>1): #if they type 'go' first
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]['directions']:
            #set the current room to the new room
            currentRoom = rooms[currentRoom]['directions'][move[1]]
        #there is no door (link) to the new room
        else:
            print(randomString(['You can\'t go that way!','Really? '+move[1]+'?','Consider getting a compass','I don\'t think going that way is the right way','Danger! Going that way is demential']))
    elif move[0] == 'get' and (len(move)>1): #if they type 'get' first
        #if the room contains an item, and the item is the one they want to get
        if ("item" in rooms[currentRoom]['items']) and (move[1] in rooms[currentRoom]['items']['item']) and (move[1] == rooms[currentRoom]['items']['item']):
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(randomString([move[1] + ' got!','Yeah! You have gotten the '+move[1],'The '+move[1]+', just what you\'ve been looking for','At last, the  glorious '+move[1] ]))
            #delete the item from the room
            del rooms[currentRoom]['items']['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print(randomString(['Can\'t get ' + move[1] + '!',move[1]+' is not here','Nah!']))
    elif (move[0] == 'use') and (len(move)>3) and (move[2] == 'with'): # if they type 'use' first
        if (move[1] == 'spray') and (move[3] == 'monster'):
            if ('item' in rooms[currentRoom]['items']) and ('monster' in rooms[currentRoom]['items']['item']) and ('spray' in inventory):
                print('You have used the magic spray to kill the monster.')
                del rooms[currentRoom]['items']['item'] ## TODO: ver como eliminar solo el monster
                print('Behind tha monster there was a passage to the Basement.')
                rooms[currentRoom]['directions']['west'] = 'Basement' # agregar nueva ruta
            else:
                print(randomString(['Mmm, think again.','You are half way there, keep up!','Yeeeeah... nope!']))
        elif (currentRoom == 'Corridor') and ('key' in inventory) and (move[1] == 'key') and (move[3] == 'locked' or move[3] == 'door'): # al abrir la puerta, se crea una salida
            rooms[currentRoom]['directions']['south'] = 'Garden' # agregar nueva ruta
            rooms[currentRoom]['items']['item'] = 'opened door'
            print('You have opened the door.')
        else:
            #tell them they can't use it
            print(randomString(['Can\'t use ' + move[1] + ' with ' + move[3] + '!','I don\'t think the '+move[1]+' is meant to be used with the '+move[3],'...'+move[1]+' with '+move[3]+' does not compute.']))
    else:
        print(randomString(['What?','Think again!','Remember the three beautiful commands?','You can do better','You think?']))
        
    # player loses if they enter a room with a monster, unless they have a cloak
    if ('item' in rooms[currentRoom]['items']) and ('monster' in rooms[currentRoom]['items']['item']):
        if 'cloak' in inventory:
            print('There is a monster! Luckily you have the cloak that keeps you safe.')
            #del rooms[currentRoom]['items']['item'] ## TODO: ver como eliminar solo el monster
        else:
            print (kitchenScreen)
            print('A monster has got you... GAME OVER!')
            break
  
    # player wins if they get to the garden with a key and a potion
    if (currentRoom == 'Garden'):
        if ('wand' in inventory) and ('potion' in inventory) and ('book' in inventory):
            print('You escaped the house with all the items... YOU WIN!')
            break
        else:
            print('Before going out, you must carry your book, potion and wand!')
  