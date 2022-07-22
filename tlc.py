from time import sleep
from Player.core import Player
from utils.info import show_track_info
from utils.keyboard_shortcut import keyboard_shortcut_handler
from optparse import OptionParser
from rich.console import Console
from rich import print
from pynput import keybord
import os
# Default track play numbers
currentTrack = 1
allTrackSum = 1
keysCurrentlyPressed = []

def onPress(key) -> None:
    """
    Pressed keyboard keys
    If the total of pressed keys is equal to 3
    it will be sent to the keyboardShortcutHandler for handlation
    params : key : key preesed
    retrun None
    """
    if len(keysCurrentlyPressed) == 3:
        keysCurrentlyPressed.clear()

    if key not in keysCurrentlyPressed:
        keysCurrentlyPressed.append(key)

    if len(keysCurrentlyPressed) == 3:
        keyboardShortcutHandler(player, keysCurrentlyPressed)
