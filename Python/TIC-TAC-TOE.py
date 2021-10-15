"""FULLY VOICE AUTOMATED GAME OF TIC TAC TOE"""
"""This is a simple game of tic tac toe fully voice automated!"""

import speech_recognition as sr
import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
volume = engine.getProperty("volume")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

slot = [" "] * 9
turn = 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def hear_name():
    with sr.Microphone() as source:
        r = sr.Recognizer()

        r.adjust_for_ambient_noise(source)

        print("Player 1 name: ")
        speak("Speak up the name of player 1: ")
        print("Listening....")
        audio = r.listen(source)
        print("Processing....")
        player_one = r.recognize_google(audio)
        print(f"Player 1: {player_one}")
        speak(f"Player 1 name is: {player_one}")
        time.sleep(1)

        print("\n")

        print("Player 2 name: ")
        speak("Speak up the name of player 2: ")
        print("Listening....")
        audio = r.listen(source)
        print("Processing....")
        player_two = r.recognize_google(audio)
        print(f"Player 2: {player_two}")
        speak(f"Player two name is: {player_two}")
        time.sleep(1)
        print("\n")

    return (player_one, player_two)


def base_board():
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")


def main_board():
    print(f" {slot[0]} | {slot[1]} | {slot[2]} ")
    print("---|---|---")
    print(f" {slot[3]} | {slot[4]} | {slot[5]} ")
    print("---|---|---")
    print(f" {slot[6]} | {slot[7]} | {slot[8]} ")


def voice_recog(player_one, player_two):

    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)

        if turn <= 1:
            speak("Speak up the slot which you want to fill: ")
        print("Listening....")
        audio = r.listen(source)
        print("Processing....")
        print("\n")

        try:
            option = r.recognize_google(audio)
            if option == "sex":
                option = "6"

            if option == "Tu":
                option = "2"

            option = int(option)

        except:
            print("", end="")

    if option in range(1, 10):
        if slot[option - 1] == " ":
            if chance == player_one:
                slot[option - 1] = "O"
                speak(f"Filling the slot {option} with a zero")

            else:
                slot[option - 1] = "X"
                speak(f"Filling the slot {option} with a cross")

        else:
            print("This slot is already filled, choose a different one")
            speak("This slot is already filled, choose a different one")
            voice_recog(player_one, player_two)

    else:
        print("This is an invalid slot, please choose a slot between 1 to 9")
        speak("This is an invalid slot, please choose a slot between 1 to 9")
        voice_recog(player_one, player_two)


def win_situation():
    print("\n")
    print(f"{chance} is the winner!")
    speak(f"{chance} is the winner!")
    print("\n")
    print("THANK YOU FOR PLAYING")
    speak("THANK YOU FOR PLAYING")
    exit()


def win_condition():
    for n in [0, 3, 6]:  # horizontal
        if slot[n] == slot[n + 1] != " " and slot[n + 1] == slot[n + 2]:
            main_board()
            win_situation()

    for n in [0, 1, 2]:  # vertical
        if slot[n] == slot[n + 3] != " " and slot[n + 3] == slot[n + 6]:
            main_board()
            win_situation()

    for n in [0]:  # leading diagonal
        if slot[n] == slot[n + 4] != " " and slot[n + 4] == slot[n + 8]:
            main_board()
            win_situation()

    for n in [2]:  # other diagonal
        if slot[n] == slot[n + 2] != " " and slot[n + 2] == slot[n + 4]:
            main_board()
            win_situation()


if __name__ == "__main__":
    print("--------------------WELCOME TO THE GAME OF TIC-TAC-TOE--------------------")
    speak("Welcome to game of tic tac toe")
    print("   --------------------------Created by TITAN--------------------------   ")
    speak("created by TITAN")
    print("\n")
    player_one, player_two = hear_name()
    while True:

        if turn % 2 == 0:
            chance = player_one

        else:
            chance = player_two

        base_board()
        print("\n")
        main_board()

        print("\n")

        print(f"{chance}'s turn : ")
        speak(f"{chance}'s turn")

        voice_recog(player_one, player_two)

        win_condition()

        turn = turn + 1

        if turn == 9:
            print("The Game is drawn!")
            speak("The Game is drawn!")
            print("\n")
            print("THANK YOU FOR PLAYING")
            speak("THANK YOU FOR PLAYING")
            main_board()
            exit()
