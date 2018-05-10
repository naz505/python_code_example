# CSCI 203
# Final Project
# Nazmnul Hossain
# Harrsion Brakewood

from visual import *
from trends import *
from data import *
from datetime import datetime
from geo import us_states, geo_distance, make_position, longitude, latitude
from string import ascii_letters
from ucb import main, trace, interact, log_current_line


def windowSetup():   
    """" Sets up the VPython window "scene"
         See http://www.vpython.org/webdoc/visual/display.html"""
    
    scene.autoscale = false        # Don't auto rescale
    scene.background = (1.00,0.76,0.80)
    scene.foreground = color.black
    scene.height = 1200            # height of graphic window in pixels
    scene.width = 1200             # width of graphic window in pixels
    scene.x = 100                  # x offset of upper left corner in pixels
    scene.y = 100                  # y offset of upper left corner in pixels
    scene.title = 'Twitter Sentiment Trends'

    

def CreateDictionary(term):
    ''' Creates a dictionary for the given term, of the average sentiment throughout the US States. This is an extra
function that is not being used in the main function, but this function allows for the user to see the numerical
average sentiment vavlue for each state.

    Doctest: CreateDictionary('USA')'''

    tweets = load_tweets(make_tweet, term)
    sortedTweet= group_tweets_by_state(tweets)
    print(sortedTweet, "\n")
    state_sentiments = average_sentiments(sortedTweet)
    return state_sentiments

def case1(stateCode, term):
    """ Used in processing the color for the states, actual fucntion used in main function for visualization."""
    average = average_sentiments(group_tweets_by_state(load_tweets(make_tweet, term)))
    if stateCode in average.keys():
        return (average[stateCode])
    else:
        average[stateCode] = [100]
        return average[stateCode]


def sentiment2Color(sentiment):
    ''' Returns a VPython color tuple depending on sentiment.
           Input: sentiment a float from -1.0 to 1.0. -1 being most negative sentiment, 1 being most positive and 0 being neutral

    Values for colors from http://en.wikipedia.org/wiki/List_of_colors:_Aâ€“F
    '''
    
    if -1.0 <= sentiment < -0.80:
        return (0.69, 0.75, 0.10) #Acid Green
    elif -0.80 <= sentiment < -0.60:
        return (0.79, 1.00, .90) #Aero Blue
    elif -0.60 <= sentiment < -0.40:
        return (0.89, 0.15, 0.21) #Red Crimson
    elif -0.40 <= sentiment < -0.20:
        return (0.23, 0.48, 0.34) #Amazon
    elif -0.20 <= sentiment < 0.00:
        return (1.0, 1.0, 1.0)    #White
    elif 0.00 <= sentiment < 0.20:
        return (0.0, 0.50, 0.0) #Green
    elif 0.20 <= sentiment < 0.40:
        return (0.0, 1.00, 1.00) #Aqua
    elif 0.40 <= sentiment <= 0.60:
        return (0.0, 0.50, 1.00)   #Azure Blue
    elif 0.60 <= sentiment <= 0.80:
        return (1.00,0.57,0.69) #Baker Miller Pink
    elif 0.80 <= sentiment <=1.0:
        return (0.80,0.60,0.40) #Brown Yellow
    
    return (0, 0.0, 0.0)        #Black for error
              


def position() :
    '''Places the dots corresponding to their sentiment value in the US map in the right state '''

    term = str(input('input term to visualize sentiment: '))
    tgaImage = materials.loadTGA("USA (9)")   # load tga image

    tex = materials.texture(data=tgaImage, mapping="sign", interpolate=False)
    
    box(length=1, height=6, width=12,  # size of box
    axis=(0,0,1), # the side to place the image
    material=tex) # places the texture tex on the side
        
    WI = sphere(pos=(1.1,1.8,1), radius=0.15,color = (sentiment2Color(case1('WI',term)[0])))
    WI_label = label(pos=(1.15,1.5,1),text='WI', height = 12, color=color.black,opacity =0, box= False)

    MN = sphere(pos=(.1,2.2,1), radius=0.15,color = (sentiment2Color(case1('MN',term)[0])))
    MN_label = label(pos=(.15,2.,1),text='MN', height = 12, color=color.black,opacity =0, box= False)

    ND = sphere(pos=(-1,2.4,1), radius=0.15,color = (sentiment2Color(case1('ND',term)[0])))
    ND_label = label(pos=(-.7,2.4,1),text='ND', height = 12, color=color.black,opacity =0, box= False)

    SD = sphere(pos=(-1,1.6,1), radius=0.15,color = (sentiment2Color(case1('SD',term)[0])))
    SD_label = label(pos=(-.7,1.6,1),text='SD', height = 12, color=color.black,opacity =0, box= False)

    IL = sphere(pos=(1.3,.8,1), radius=0.15,color = (sentiment2Color(case1('IL',term)[0])))
    IL_label = label(pos=(1.3,1.1,1),text='IL', height = 12, color=color.black,opacity =0, box= False)

    IA = sphere(pos=(.5,1,1), radius=0.15,color = (sentiment2Color(case1('IA',term)[0])))
    IA_label = label(pos=(.5,1.3,1),text='IA', height = 12, color=color.black,opacity =0, box= False)

    NE = sphere(pos=(-.85,1,1), radius=0.15,color = (sentiment2Color(case1('NE',term)[0])))
    NE_label = label(pos=(-.57,1,1),text='NE', height = 12, color=color.black,opacity =0, box= False)

    KS = sphere(pos=(-.75,.45, 1), radius=0.15,color = (sentiment2Color(case1('KS',term)[0])))
    KS_label = label(pos=(-.45,.45, 1),text='KS', height = 12, color=color.black,opacity =0, box= False)

    MO = sphere(pos=(.5,.45,1), radius=0.15,color = (sentiment2Color(case1('MO',term)[0])))
    MO_label = label(pos=(.75,.45,1),text='MO', height = 12, color=color.black,opacity =0, box= False)

    AR = sphere(pos=(.5,-.35,1), radius=0.15,color = (sentiment2Color(case1('AR',term)[0])))
    AR_label = label(pos=(.75,-.35,1),text='AR', height = 12, color=color.black,opacity =0, box= False)

    OK = sphere(pos=(-.2,-.35,1), radius=0.15,color = (sentiment2Color(case1('OK',term)[0])))
    OK_label = label(pos=(-.2,-.15,1),text='OK', height = 12, color=color.black,opacity =0, box= False)

    TX = sphere(pos=(-1,-1,1), radius=0.15,color = (sentiment2Color(case1('TX',term)[0])))
    TX_label = label(pos=(-.73,-1,1),text='TX', height = 12, color=color.black,opacity =0, box= False)

    NM = sphere(pos=(-1.8,-.6,1), radius=0.15,color = (sentiment2Color(case1('NM',term)[0])))
    NM_label = label(pos=(-2.1,-.6,1),text='NM', height = 12, color=color.black,opacity =0, box= False)

    AZ = sphere(pos=(-2.9,-.6,1), radius=0.15,color = (sentiment2Color(case1('AZ',term)[0])))
    AZ_label = label(pos=(-3.3,-.6,1),text='AZ', height = 12, color=color.black,opacity =0, box= False)

    UT = sphere(pos=(-2.9,.45,1), radius=0.15,color = (sentiment2Color(case1('UT',term)[0])))
    UT_label = label(pos=(-3.3,.45,1),text='UT', height = 12, color=color.black,opacity =0, box= False)

    CO = sphere(pos=(-1.8,.45,1), radius=0.15,color = (sentiment2Color(case1('CO',term)[0])))
    CO_label = label(pos=(-2.1,.45,1),text='CO', height = 12, color=color.black,opacity =0, box= False)

    WY = sphere(pos=(-2.3,1.3,1), radius=0.15,color = (sentiment2Color(case1('WY',term)[0])))
    WY_label = label(pos=(-2.3,1.5,1),text='WY', height = 12, color=color.black,opacity =0, box= False)

    MT = sphere(pos=(-2.3,2.3,1), radius=0.15,color = (sentiment2Color(case1('MT',term)[0])))
    MT_label = label(pos=(-2.3,1.95,1),text='MT', height = 12, color=color.black,opacity =0, box= False)

    ID = sphere(pos=(-3.3,1.4,1), radius=0.15,color = (sentiment2Color(case1('ID',term)[0])))
    ID_label = label(pos=(-3.55,1.4,1),text='ID', height = 12, color=color.black,opacity =0, box= False)

    OR = sphere(pos=(-4.5,1.5,1), radius=0.15,color = (sentiment2Color(case1('OR',term)[0])))
    OR_label = label(pos=(-4.85,1.5,1),text='OR', height = 12, color=color.black,opacity =0, box= False)

    WA = sphere(pos=(-4.5,2.5,1), radius=0.15,color = (sentiment2Color(case1('WA',term)[0])))
    WA_label = label(pos=(-4.85,2.5,1),text='WA', height = 12, color=color.black,opacity =0, box= False)

    CA = sphere(pos=(-5,.4,1), radius=0.15,color = (sentiment2Color(case1('CA',term)[0])))
    CA_label = label(pos=(-5,.65,1),text='CA', height = 12, color=color.black,opacity =0, box= False)

    NV = sphere(pos=(-4,.4,1), radius=0.15,color = (sentiment2Color(case1('NV',term)[0])))
    NV_label = label(pos=(-4,.65,1),text='NV', height = 12, color=color.black,opacity =0, box= False)

    AK = sphere(pos=(-5,-2,1), radius=0.15,color = (sentiment2Color(case1('AK',term)[0])))
    AK_label = label(pos=(-4.7,-1.8,1),text='AK', height = 12, color=color.black,opacity =0, box= False)

    HI = sphere(pos=(-2.1,-2.3,1), radius=0.15,color = (sentiment2Color(case1('HI',term)[0])))
    HI_label = label(pos=(-2.1,-2.05,1),text='HI', height = 12, color=color.black,opacity =0, box= False)

    LA = sphere(pos=(.62,-1,1), radius=0.15,color = (sentiment2Color(case1('LA',term)[0])))
    LA_label = label(pos=(0.62,-1.2,1),text='LA', height = 12, color=color.black,opacity =0, box= False)

    MI = sphere(pos=(1.2,-.9,1), radius=0.15,color = (sentiment2Color(case1('MI',term)[0])))
    MI_label = label(pos=(1.2,-.6,1),text='MI', height = 12, color=color.black,opacity =0, box= False)

    AL = sphere(pos=(1.7,-.9,1), radius=0.15,color = (sentiment2Color(case1('AL',term)[0])))
    AL_label = label(pos=(1.7,-.6,1),text='AL', height = 12, color=color.black,opacity =0, box= False)

    GA = sphere(pos=(2.5,-.9,1), radius=0.15,color = (sentiment2Color(case1('GA',term)[0])))
    GA_label = label(pos=(2.4,-.6,1),text='GA', height = 12, color=color.black,opacity =0, box= False)

    FL = sphere(pos=(2.7,-1.5,1), radius=0.15,color = (sentiment2Color(case1('FL',term)[0])))
    FL_label = label(pos=(2.8,-1.73,1),text='FL', height = 12, color=color.black,opacity =0, box= False)

    SC = sphere(pos=(3.1,-.6,1), radius=0.15,color = (sentiment2Color(case1('SC',term)[0])))
    SC_label = label(pos=(2.9,-.5,1),text='SC', height = 12, color=color.black,opacity =0, box= False)

    NC = sphere(pos=(3.4,-.2,1), radius=0.15,color = (sentiment2Color(case1('NC',term)[0])))
    NC_label = label(pos=(3.16,-.2,1),text='NC', height = 12, color=color.black,opacity =0, box= False)

    VA = sphere(pos=(3.5,.3,1), radius=0.15,color = (sentiment2Color(case1('VA',term)[0])))
    VA_label = label(pos=(3.35,.18,1),text='VA', height = 12, color=color.black,opacity =0, box= False)

    WV = sphere(pos=(2.9,.3,1), radius=0.15,color = (sentiment2Color(case1('WV',term)[0])))
    WV_label = label(pos=(3.1,.44,1),text='WV', height = 12, color=color.black,opacity =0, box= False)

    KY = sphere(pos=(2.2,.3,1), radius=0.15,color = (sentiment2Color(case1('KY',term)[0])))
    KY_label = label(pos=(2,.12,1),text='KY', height = 12, color=color.black,opacity =0, box= False)

    TN = sphere(pos=(2.2,-.2,1), radius=0.15,color = (sentiment2Color(case1('TN',term)[0])))
    TN_label = label(pos=(1.94,-.2,1),text='TN', height = 12, color=color.black,opacity =0, box= False)

    IN = sphere(pos=(1.9,.8,1), radius=0.15,color = (sentiment2Color(case1('IN',term)[0])))
    IN_label = label(pos=(1.9,.55,1),text='IN', height = 12, color=color.black,opacity =0, box= False)

    OH = sphere(pos=(2.5,.8,1), radius=0.15,color = (sentiment2Color(case1('OH',term)[0])))
    OH_label = label(pos=(2.5,.55,1),text='OH', height = 12, color=color.black,opacity =0, box= False)

    MI = sphere(pos=(2.2,1.3,1), radius=0.15,color = (sentiment2Color(case1('MI',term)[0])))
    MI_label = label(pos=(2.1,1.55,1),text='MI', height = 12, color=color.black,opacity =0, box= False)

    PA = sphere(pos=(3.5,.8,1), radius=0.15,color = (sentiment2Color(case1('PA',term)[0])))
    PA_label = label(pos=(3.75,.8,1),text='PA', height = 12, color=color.black,opacity =0, box= False)

    NY = sphere(pos=(3.8,1.3,1), radius=0.15,color = (sentiment2Color(case1('NY',term)[0])))
    NY_label = label(pos=(4.1,1.3,1),text='NY', height = 12, color=color.black,opacity =0, box= False)

    ME = sphere(pos=(5.2,2,1), radius=0.15,color = (sentiment2Color(case1('ME',term)[0])))
    ME_label = label(pos=(5.1,1.8,1),text='ME', height = 12, color=color.black,opacity =0, box= False)

    VT = sphere(pos=(4.4,2.5,1), radius=0.15,color = (sentiment2Color(case1('VT',term)[0])))
    VT_label = label(pos=(4.15,2.5,1),text='VT', height = 12, color=color.black,opacity =0, box= False)

    NH = sphere(pos=(4.4,2.1,1), radius=0.15,color = (sentiment2Color(case1('NH',term)[0])))
    NH_label = label(pos=(4.15,2.1,1),text='NH', height = 12, color=color.black,opacity =0, box= False)

    MA = sphere(pos=(5.2,.6,1), radius=0.15,color = (sentiment2Color(case1('MA',term)[0])))
    MA_label = label(pos=(4.8,.6,1),text='MA', height = 12, color=color.black,opacity =0, box= False)

    RI = sphere(pos=(5.2,.2,1), radius=0.15,color = (sentiment2Color(case1('RI',term)[0])))
    RI_label = label(pos=(4.8,.2,1),text='RI', height = 12, color=color.black,opacity =0, box= False)

    CT = sphere(pos=(5.2,-.2,1), radius=0.15,color = (sentiment2Color(case1('CT',term)[0])))
    CT_label = label(pos=(4.8,-.2,1),text='CT', height = 12, color=color.black,opacity =0, box= False)

    NJ = sphere(pos=(5.2,-.6,1), radius=0.15,color = (sentiment2Color(case1('NJ',term)[0])))
    NJ_label = label(pos=(4.8,-.6,1),text='NJ', height = 12, color=color.black,opacity =0, box= False)

    DE = sphere(pos=(5.2,-1,1), radius=0.15,color = (sentiment2Color(case1('DE',term)[0])))
    DE_label = label(pos=(4.8,-1,1),text='DE', height = 12, color=color.black,opacity =0, box= False)

    MD = sphere(pos=(5.2,-1.4,1), radius=0.15,color = (sentiment2Color(case1('MD',term)[0])))
    MD_label = label(pos=(4.8,-1.4,1),text='MD', height = 12, color=color.black,opacity =0, box= False)



    
def main():
    windowSetup()
    position()

    ''' This is the function that incoportes the windowSetup() nad Position() to visualize the average sentuiment for
for all the tweets containing the the term inpot decided by the user depending on the frequency of the time it can
take 30seconds to a minute to visualize

doctest1 : main()
           input term to visualize sentiment: politics

doctest2 : main()
           input term to visualize sentiment : USA

doctest3 : main()
           input term to visualize sentiment: Feeling good

          after this a window should pop up containing US map that would show the average sentiment for all the states
        for all the tweet containing that term, the colors would correspond to the colors defined in sentiment2Color(sentiment)
         function.'''
    
   
