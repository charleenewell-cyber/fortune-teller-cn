let answer = 0
input.onGesture(Gesture.Shake, function () {
    answer = randint(1, 2)
    if (answer == 1) {
        answer.move(1)
        basic.showString("yes")
    } else {
        basic.showString("no")
    }
})
