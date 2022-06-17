basic.showString("Jood Ahmed Alkanbashi")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
let a = 90
let b = 89
input.onButtonPressed(Button.A, function on_button_pressed_a2() {
    if (a >= b) {
        basic.showString("excellent")
    } else {
        basic.showString("good ")
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showNumber(0, 9)
})
