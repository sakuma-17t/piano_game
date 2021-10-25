import pygame
import pygame.midi
import serial

pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
print("input MIDI:%d" % input_id)
midi_in = pygame.midi.Input(input_id)
print("starting")
print("full midi_events:[[[status,data1,data2,data3],timestamp]]")

loop = True
t_state = 0

ser = serial.Serial("COM6", 115200) #必要に応じて「"COM6"」の部分は書き換えてください

while loop:
    if midi_in.poll():
        midi_events = midi_in.read(10)
        print("full midi_events:" + str(midi_events))
        state = midi_events[0][0]
        t_state = midi_events[0][1]
        #移動---------------------------------------------------------------
        if (state[0] == 144) and ((state[1] == 51) or (state[1] == 21) or (state[1] == 103)):  # W
            ser.write(bytes([51]))

        if (state[0] == 128) and ((state[1] == 51) or (state[1] == 21) or (state[1] == 103)):  # W
            ser.write(bytes([51 + 88]))

        if (state[0] == 144) and ((state[1] == 52) or (state[1] == 22) or (state[1] == 104)):  # S
            ser.write(bytes([52]))

        if (state[0] == 128) and ((state[1] == 52) or (state[1] == 22) or (state[1] == 104)):  # S
            ser.write(bytes([52 + 88]))

        if (state[0] == 144) and ((state[1] == 50) or (state[1] == 23) or (state[1] == 105)):  # A
            ser.write(bytes([50]))
            
        if (state[0] == 128) and ((state[1] == 50) or (state[1] == 23) or (state[1] == 105)):  # A
            ser.write(bytes([50 + 88]))
            
        if (state[0] == 144) and ((state[1] == 53) or (state[1] == 24) or (state[1] == 106)):  # D
            ser.write(bytes([53]))

        if (state[0] == 128) and ((state[1] == 53) or (state[1] == 24) or (state[1] == 106)):  # D
            ser.write(bytes([53 + 88]))
            
        if (state[0] == 144) and ((state[1] == 47) or (state[1] == 25) or (state[1] == 107)):  # LCTRL
            ser.write(bytes([47]))

        if (state[0] == 128) and ((state[1] == 47) or (state[1] == 25) or (state[1] == 107)):  # LCTRL
            ser.write(bytes([47 + 88]))
            
        if (state[0] == 144) and ((state[1] == 55) or (state[1] == 26) or (state[1] == 108)):  # SPACE
            ser.write(bytes([55]))

        if (state[0] == 128) and ((state[1] == 55) or (state[1] == 26) or (state[1] == 108)):  # SPACE
            ser.write(bytes([55 + 88]))
            
        if (state[0] == 144) and ((state[1] == 48) or (state[1] == 27)):  # SHIFT
            ser.write(bytes([48]))

        if (state[0] == 128) and ((state[1] == 48) or (state[1] == 27)):  # SHIFT
            ser.write(bytes([48 + 88]))
        #移動---------------------------------------------------------------
        
        #武器・アビリティ----------------------------------------------------
        if (state[0] == 144) and ((state[1] == 49) or (state[1] == 28)):  # Q
            ser.write(bytes([49]))

        if (state[0] == 128) and ((state[1] == 49) or (state[1] == 28)):  # Q
            ser.write(bytes([49 + 88]))
            
        if (state[0] == 144) and ((state[1] == 45) or (state[1] == 29)):  # Z
            ser.write(bytes([45]))

        if (state[0] == 128) and ((state[1] == 45) or (state[1] == 29)):  # Z
            ser.write(bytes([45 + 88]))
            
        if (state[0] == 144) and ((state[1] == 54) or (state[1] == 30)):  # E
            ser.write(bytes([54]))

        if (state[0] == 128) and ((state[1] == 54) or (state[1] == 30)):  # E
            ser.write(bytes([54 + 88]))
            
        if (state[0] == 144) and ((state[1] == 56) or (state[1] == 31)):  # X
            ser.write(bytes([56]))

        if (state[0] == 128) and ((state[1] == 56) or (state[1] == 31)):  # X
            ser.write(bytes([56 + 88]))
            
        if (state[0] == 144) and ((state[1] == 46) or (state[1] == 32)):  # TAB
            ser.write(bytes([46]))

        if (state[0] == 128) and ((state[1] == 46) or (state[1] == 32)):  # TAB
            ser.write(bytes([46 + 88]))
            
        if (state[0] == 144) and ((state[1] == 63) or (state[1] == 33)):  # M
            ser.write(bytes([63]))

        if (state[0] == 128) and ((state[1] == 63) or (state[1] == 33)):  # M
            ser.write(bytes([63 + 88]))
            
        if (state[0] == 144) and ((state[1] == 72) or (state[1] == 34) or (state[1] == 98)):  # 左クリック
            ser.write(bytes([72]))

        if (state[0] == 128) and ((state[1] == 72) or (state[1] == 34) or (state[1] == 98)):  # 左クリック
            ser.write(bytes([72 + 88]))
            
        if (state[0] == 144) and ((state[1] == 58) or (state[1] == 35)):  # B
            ser.write(bytes([58]))

        if (state[0] == 128) and ((state[1] == 58) or (state[1] == 35)):  # B
            ser.write(bytes([58 + 88]))
            
        if (state[0] == 144) and ((state[1] == 83) or (state[1] == 36)):  # 右クリック
            ser.write(bytes([83]))

        if (state[0] == 128) and ((state[1] == 83) or (state[1] == 36)):  # 右クリック
            ser.write(bytes([83 + 88]))
            
        if (state[0] == 144) and ((state[1] == 59) or (state[1] == 37)):  # V
            ser.write(bytes([59]))

        if (state[0] == 128) and ((state[1] == 59) or (state[1] == 37)):  # V
            ser.write(bytes([59 + 88]))
            
        if (state[0] == 144) and ((state[1] == 57) or (state[1] == 38)):  # R
            ser.write(bytes([57]))

        if (state[0] == 128) and ((state[1] == 57) or (state[1] == 38)):  # R
            ser.write(bytes([57 + 88]))
            
        if (state[0] == 144) and ((state[1] == 73) or (state[1] == 65)):  # 1
            ser.write(bytes([73]))

        if (state[0] == 128) and ((state[1] == 73) or (state[1] == 65)):  # 1
            ser.write(bytes([73 + 88]))
            
        if (state[0] == 144) and ((state[1] == 82) or (state[1] == 66)):  # 2
            ser.write(bytes([82]))

        if (state[0] == 128) and ((state[1] == 82) or (state[1] == 66)):  # 2
            ser.write(bytes([82 + 88]))
            
        if (state[0] == 144) and ((state[1] == 71) or (state[1] == 67)):  # 3
            ser.write(bytes([71]))

        if (state[0] == 128) and ((state[1] == 71) or (state[1] == 67)):  # 3
            ser.write(bytes([71 + 88]))
            
        if (state[0] == 144) and ((state[1] == 60) or (state[1] == 68)):  # G
            ser.write(bytes([60]))

        if (state[0] == 128) and ((state[1] == 60) or (state[1] == 68)):  # G
            ser.write(bytes([60 + 88]))
            
        if (state[0] == 144) and ((state[1] == 61) or (state[1] == 69)):  # T
            ser.write(bytes([61]))

        if (state[0] == 128) and ((state[1] == 61) or (state[1] == 69)):  # T
            ser.write(bytes([61 + 88]))
            
        if (state[0] == 144) and ((state[1] == 44) or (state[1] == 74)):  # 4
            ser.write(bytes([44]))

        if (state[0] == 128) and ((state[1] == 44) or (state[1] == 74)): #4
            ser.write(bytes([44 + 88]))
            
        if (state[0] == 144) and ((state[1] == 43) or (state[1] == 75)):  # 5
            ser.write(bytes([43]))

        if (state[0] == 128) and ((state[1] == 43) or (state[1] == 75)):  # 5
            ser.write(bytes([43 + 88]))
            
        if (state[0] == 144) and ((state[1] == 42) or (state[1] == 80)):  # 6
            ser.write(bytes([42]))

        if (state[0] == 128) and ((state[1] == 42) or (state[1] == 80)):  # 6
            ser.write(bytes([42 + 88]))
            
        if (state[0] == 144) and ((state[1] == 41) or (state[1] == 81)):  # 7
            ser.write(bytes([41]))

        if (state[0] == 128) and ((state[1] == 41) or (state[1] == 81)):  # 7
            ser.write(bytes([41 + 88]))
            
        if (state[0] == 144) and ((state[1] == 40) or (state[1] == 84)):  # 8
            ser.write(bytes([40]))

        if (state[0] == 128) and ((state[1] == 40) or (state[1] == 84)):  # 8
            ser.write(bytes([40 + 88]))
            
        if (state[0] == 144) and ((state[1] == 39) or (state[1] == 86)):  # 9
            ser.write(bytes([39]))

        if (state[0] == 128) and ((state[1] == 39) or (state[1] == 86)):  # 9
            ser.write(bytes([39 + 88]))
            
        if (state[0] == 144) and ((state[1] == 62) or (state[1] == 87)):  # F
            ser.write(bytes([62]))

        if (state[0] == 128) and ((state[1] == 62) or (state[1] == 87)):  # F
            ser.write(bytes([62 + 88]))
            
        if (state[0] == 144) and ((state[1] == 64) or (state[1] == 97)):  # N
            ser.write(bytes([64]))

        if (state[0] == 128) and ((state[1] == 64) or (state[1] == 97)):  # N
            ser.write(bytes([64 + 88]))
        #武器・アビリティ----------------------------------------------------
        
        #通信---------------------------------------------------------------
        if (state[0] == 144) and (state[1] == 85): #J
            ser.write(bytes([85]))

        if (state[0] == 128) and (state[1] == 85): #J
            ser.write(bytes([85 + 88]))
            
        if (state[0] == 144) and (state[1] == 70): #H
            ser.write(bytes([70]))

        if (state[0] == 128) and (state[1] == 70): #H
            ser.write(bytes([70 + 88]))
            
        if (state[0] == 144) and (state[1] == 92): #U
            ser.write(bytes([92]))

        if (state[0] == 128) and (state[1] == 92): #U
            ser.write(bytes([92 + 88]))
            
        if (state[0] == 144) and (state[1] == 93): #I
            ser.write(bytes([93]))

        if (state[0] == 128) and (state[1] == 93): #I
            ser.write(bytes([93 + 88]))
            
        if (state[0] == 144) and (state[1] == 94): #O
            ser.write(bytes([94]))

        if (state[0] == 128) and (state[1] == 94): #O
            ser.write(bytes([94 + 88]))
            
        if (state[0] == 144) and (state[1] == 95): #P
            ser.write(bytes([95]))

        if (state[0] == 128) and (state[1] == 95): #P
            ser.write(bytes([95 + 88]))
            
        if (state[0] == 144) and (state[1] == 96): #K
            ser.write(bytes([96]))

        if (state[0] == 128) and (state[1] == 96): #K
            ser.write(bytes([96 + 88]))
        #通信---------------------------------------------------------------
        
        #マウス---------------------------------------------------------------
        if (state[0] == 144) and (state[1] == 76): #視点左
            ser.write(bytes([76]))

        if (state[0] == 128) and (state[1] == 76): #視点左
            ser.write(bytes([76 + 88]))
            
        if (state[0] == 144) and (state[1] == 79): #視点右
            ser.write(bytes([79]))

        if (state[0] == 128) and (state[1] == 79): #視点右
            ser.write(bytes([79 + 88]))
            
        if (state[0] == 144) and (state[1] == 78): #視点上
            ser.write(bytes([78]))

        if (state[0] == 128) and (state[1] == 78): #視点上
            ser.write(bytes([78 + 88]))
            
        if (state[0] == 144) and (state[1] == 77): #視点下
            ser.write(bytes([77]))

        if (state[0] == 128) and (state[1] == 77): #視点下
            ser.write(bytes([77 + 88]))

        if (state[0] == 144) and (state[1] == 88): #視点左弱
            ser.write(bytes([88]))

        if (state[0] == 128) and (state[1] == 88): #視点左弱
            ser.write(bytes([88 + 88]))

        if (state[0] == 144) and (state[1] == 91): #視点右弱
            ser.write(bytes([91]))

        if (state[0] == 128) and (state[1] == 91): #視点右弱
            ser.write(bytes([91 + 88]))

        if (state[0] == 144) and (state[1] == 90): #視点上弱
            ser.write(bytes([90]))

        if (state[0] == 128) and (state[1] == 90): #視点上弱
            ser.write(bytes([90 + 88]))

        if (state[0] == 144) and (state[1] == 89): #視点下弱
            ser.write(bytes([89]))

        if (state[0] == 128) and (state[1] == 89): #視点下弱
            ser.write(bytes([89 + 88]))
            
        if (state[0] == 144) and (state[1] == 99):  # 視点右強
            ser.write(bytes([99]))

        if (state[0] == 128) and (state[1] == 99):  # 視点右強
            ser.write(bytes([99 + 88]))
            
        if (state[0] == 144) and (state[1] == 100):  # 視点左強
            ser.write(bytes([100]))

        if (state[0] == 128) and (state[1] == 100):  # 視点左強
            ser.write(bytes([100 + 88]))
            
        if (state[0] == 144) and (state[1] == 101):  # 視点上強
            ser.write(bytes([101]))

        if (state[0] == 128) and (state[1] == 101):  # 視点上強
            ser.write(bytes([101 + 88]))
            
        if (state[0] == 144) and (state[1] == 102):  # 視点下強
            ser.write(bytes([102]))

        if (state[0] == 128) and (state[1] == 102):  # 視点下強
            ser.write(bytes([102 + 88]))
        #マウス---------------------------------------------------------------
ser.close()            
midi_in.close()
pygame.midi.quit()
