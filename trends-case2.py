#Final Project
# Nazmul Hossain
# Harrison Brakewood

'''Phase 2 of the Final Project'''

from trends import *
from visual import *

def windowSetup():   
    """" Sets up the VPython window "scene"
         See http://www.vpython.org/webdoc/visual/display.html"""
    
    scene.autoscale = false        # Don't auto rescale
    scene.background = color.white
    scene.foreground = color.black
    scene.height = 1000            # height of graphic window in pixels
    scene.width = 1000             # width of graphic window in pixels
    scene.x = 100                  # x offset of upper left corner in pixels
    scene.y = 100                  # y offset of upper left corner in pixels
    scene.title = 'Twitter Trends'

def createTask6Dictionary():
    """ createTask6Dictionary returns a dictionary of the form
        created by Task 6 of Phase 1.
        
        The 'key is the state postal code.  The 'value' is a list of two numbers -
        the first is average sentiment for the state and the second is the number
        of tweets for the state.
           Inputs: none"""
    tweets=[]
    f = open('data/soup.txt','rb')
    for line in f:
        #print(line)        #used for debugging
        text=""
        time=""
        lat=""
        lon=""
        i=1
        containslatitide=False
        for x in line:
            if chr(x)==']':
                containslatitide=True
                break
        if containslatitide:
            while(chr(line[i])!=','):
                lat+=chr(line[i])
                i+=1
            i+=2
            while(chr(line[i])!=']'):
                lon+=chr(line[i])
                i+=1
            i+=4
            
            while(chr(line[i])!='\t'):
                time+=chr(line[i])
                i+=1
            if (chr(line[i])=='\t'):
                i+=1
        while(chr(line[i])!='\n'):
            text+=chr(line[i])
            i+=1
        if containslatitide:
            tweet=make_tweet(text,time,float(lat),float(lon))
        else:
            tweet=make_tweet(text,'2011-09-03 14:06:44',0,0)
        tweets.append(tweet)
    tweets_by_state = group_tweets_by_state(tweets)
    myDict = average_sentiments(tweets_by_state)
    return myDict


       
def displaySentiments(myDict):
    """ Lists the states in order of highest sentiment to lowest.
    By choosing different file names the user can see where his state falls for
    that selected word. By choosing all_tweets the user can see where his state
    falls with overall sentiment."""

    d=sorted(myDict.items(), key=lambda x: x[1])
    
    xpos=0
    ypos=-7.5
    zpos=0
    i=1
    for state in d:
        if(i==1):
            mycolor=(0,0,0)
        elif(i>1 and i<25):
            mycolor=(.6,.4,.8)
        elif(i>=25 and i<50):
            mycolor=(0,.5,1)
        elif(i==50):
            mycolor=(0,.5,0)
        text(pos=(xpos,ypos,zpos), text=state[0], height=.15, color=mycolor, font='times')                
        

        ypos += .45  # space between states
        i+=1
    
def main():
    windowSetup()
    displaySentiments(createTask6Dictionary())


