answer = 0

def on_gesture_shake():
    global answer
    answer = randint(1, 2)
    if answer == 1:
        basic.show_string("yes")
    else:
        basic.show_string("no")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
