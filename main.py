def on_received_string(receivedString):
    global angle
    if receivedString == "Open":
        if angle > 0:
            angle += -1
            maqueen.servo_run(maqueen.Servos.S1, angle)
            strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif receivedString == "Close":
        if angle < 180:
            angle += 1
            maqueen.servo_run(maqueen.Servos.S1, angle)
            strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif receivedString == "LEDL":
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    elif receivedString == "LEDR":
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    elif receivedString == "F":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    elif receivedString == "B":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    elif receivedString == "L":
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 107)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 107)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    elif receivedString == "R":
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 107)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 107)
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    else:
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        maqueen.motor_stop(maqueen.Motors.ALL)
radio.on_received_string(on_received_string)

strip: neopixel.Strip = None
angle = 0
basic.show_string("RX4")
basic.show_icon(IconNames.STICK_FIGURE)
radio.set_group(1)
angle = 0
maqueen.servo_run(maqueen.Servos.S1, angle)
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB_RGB)