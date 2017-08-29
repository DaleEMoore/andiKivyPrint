#! /usr/bin/python3

__version__ = "0.2" # TODO; increment this frequently!

# cd ~/PycharmProjects/andiKivyPrint
# buildozer init
# vi buildozer.spec
# buildozer android debug
# email bin/*.apk to phone
# Install apk on phone.

# But, I can't see the prints anywhere.
# https://stackoverflow.com/questions/23055696/see-output-of-print-statements-on-android-using-kivy-kivy-launcher
# https://stackoverflow.com/questions/3102443/is-there-a-way-to-print-to-the-console-in-an-android-app
# Nice printlog():
# https://stackoverflow.com/questions/26265015/how-to-get-console-output-printed-using-kivy
# https://developer.android.com/reference/android/util/Log.html

# Tried the stuff, below and can't get the Builder to do right. Move to
# complete code examples.
# dalem@QnD:~/PycharmProjects$ git clone https://github.com/kivy/kivy.git andiKivyExamples


# From: https://stackoverflow.com/questions/23055696/see-output-of-print-statements-on-android-using-kivy-kivy-launcher
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.lang import Builder
import time

Builder.load_string('''
<InfoBubble@Bubble>
    # declare our message StringProperty
    message: 'empty message'
    # let the bubble be of 200 device pixels
    # and expand as necessary on the height
    # depending on the message + 20 dp of padding.
    size_hint: None, None
    show_arrow: False
    pos_hint: {'top': 1, 'right': 1}
    size: dp(200), lbl.texture_size[1] + dp(20)
    Label:
        id: lbl
        text: root.message
        # constraint the text to be displayed within
        # the bubble width and have it be unrestricted
        # on the height.
        text_size: root.width - dp(20), None
''')
# TODO; nothing appears for this info_bubble - what's going on?
info_bubble = Factory.InfoBubble()
#info_bubble = ""
# TODO; output something that Android can see.
def bubbprint(message):
    print(message) # Normal console display output.
    message = repr(message)
    #if not info_bubble:
    #    info_bubble = Factory.InfoBubble()
    info_bubble.message = message
    # Check if bubble is not already on screen
    if not info_bubble.parent:
        Window.add_widget(info_bubble)
    # Remove bubble after X secs
    X = 200 # number of seconds to wait before removing bubble.
    Clock.schedule_once(lambda dt:
        Window.remove_widget(info_bubble), X)
#def bubbprint(self, message):
#    message = repr(message)
#    if not self.info_bubble:
#        self.info_bubble = Factory.InfoBubble()
#    self.info_bubble.message = message
#    # Check if bubble is not already on screen
#    if not self.info_bubble.parent:
#        Window.add_widget(self.info_bubble)
#    # Remove bubble after 2 secs
#    Clock.schedule_once(lambda dt:
#        Window.remove_widget(self.info_bubble), 2)

#bp = bubbprint
info_bubble = Factory.InfoBubble()
s1 = "Start andiKivyPrint version " + str(__version__)
bubbprint(s1)
X = 5
print("Sleeping " + str(X) + " seconds.")
time.sleep(X)
#s1 = """
#This will be lots and lots and lots of lines.
#lots
#    more lots
#        more and more lots
#            lots and lots and more lots
#lots
#    more lots
#        more and more lots
#            lots and lots and more lots
#lots
#    more lots
#        more and more lots
#            lots and lots and more lots
#lots
#    more lots
#        more and more lots
#            lots and lots and more lots
#lots
#    more lots
#        more and more lots
#            lots and lots and more lots
#"""
#bubbprint(s1)
s1 = "End andiKivyPrint version " + str(__version__)
bubbprint(s1)