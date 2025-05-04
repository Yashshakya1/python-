# Q1. print the multiline and speak this lines using external module
import pyttsx3
engine = pyttsx3.init() # object creation
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine = pyttsx3.init()
engine.say('''Oh, the night is my world
City light painted girl
In the day nothing matters
It's the night time that flatters
In the night, no control
Through the wall something's breaking
Wearing white as you're walkin'
Down the street of my soul

You take my self, you take my self control
You got me livin' only for the night
Before the morning comes, the story's told
You take my self, you take my self control

Another night, another day goes by
I never stop myself to wonder why
You help me to forget to play my role
You take my self, you take my self control

I, I live among the creatures of the night
I haven't got the will to try and fight
Against a new tomorrow, so I guess I'll just believe it
That tomorrow never comes

A safe night, I'm living in the forest of my dream
I know the night is not as it would seem
I must believe in something, so I'll make myself believe it
This night will never go

Oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh
Oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh

Oh, the night is my world
City light painted girl
In the day nothing matters
It's the night time that flatters

I, I live among the creatures of the night
I haven't got the will to try and fight
Against a new tomorrow, so I guess I'll just believe it
That tomorrow never knows

A safe night, I'm living in the forest of a dream
I know the night is not as it would seem
I must believe in something, so I'll make myself believe it
This night will never go

Oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh
You take my self, you take my self control
You take my self, you take my self control
You take my self, you take my self control

      
      ''' )
engine.runAndWait()

print('''

      
Oh, the night is my world
City light painted girl
In the day nothing matters
It's the night time that flatters
In the night, no control
Through the wall something's breaking
Wearing white as you're walkin'
Down the street of my soul

You take my self, you take my self control
You got me livin' only for the night
Before the morning comes, the story's told
You take my self, you take my self control

Another night, another day goes by
I never stop myself to wonder why
You help me to forget to play my role
You take my self, you take my self control

I, I live among the creatures of the night
I haven't got the will to try and fight
Against a new tomorrow, so I guess I'll just believe it
That tomorrow never comes

A safe night, I'm living in the forest of my dream
I know the night is not as it would seem
I must believe in something, so I'll make myself believe it
This night will never go

Oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh
Oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh

Oh, the night is my world
City light painted girl
In the day nothing matters
It's the night time that flatters

I, I live among the creatures of the night
I haven't got the will to try and fight
Against a new tomorrow, so I guess I'll just believe it
That tomorrow never knows

A safe night, I'm living in the forest of a dream
I know the night is not as it would seem
I must believe in something, so I'll make myself believe it
This night will never go

Oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh, oh-oh-oh
You take my self, you take my self control
You take my self, you take my self control
You take my self, you take my self control

      
      ''') 