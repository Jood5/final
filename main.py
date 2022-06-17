
basic.show_string("Jood Ahmed Alkanbashi")

def on_button_pressed_a():

   basic.show_icon(IconNames.HEART)

input.on_button_pressed(Button.A, on_button_pressed_a)
a = 90
b = 89 
def  on_button_pressed_a2():
     
    if  a>=b:
        
     basic.show_string("excellent")
    else:
     basic.show_string("good ")
input.on_button_pressed(Button.A, on_button_pressed_a2)
def on_gesture_shake():
     basic .show_number(0,9)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
    