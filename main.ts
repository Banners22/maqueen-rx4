radio.onReceivedString(function (receivedString) {
    if (receivedString == "Open") {
        if (angle > 0) {
            angle += -1
            maqueen.servoRun(maqueen.Servos.S1, angle)
            strip.showColor(neopixel.colors(NeoPixelColors.Orange))
        }
    } else if (receivedString == "Close") {
        if (angle < 180) {
            angle += 1
            maqueen.servoRun(maqueen.Servos.S1, angle)
            strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        }
    } else if (receivedString == "LEDL") {
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    } else if (receivedString == "LEDR") {
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    } else if (receivedString == "F") {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
    } else if (receivedString == "B") {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 255)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
    } else if (receivedString == "L") {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 107)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 107)
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
    } else if (receivedString == "R") {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 107)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 107)
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    } else {
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
        maqueen.motorStop(maqueen.Motors.All)
    }
})
let strip: neopixel.Strip = null
let angle = 0
basic.showString("RX4")
basic.showIcon(IconNames.StickFigure)
radio.setGroup(1)
angle = 0
maqueen.servoRun(maqueen.Servos.S1, angle)
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB_RGB)
