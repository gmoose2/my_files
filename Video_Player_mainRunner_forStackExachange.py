# Video_Player_mainRunner

#%% imports
from PyQt5 import uic

from PyQt5.QtCore import Qt

from PyQt5 import QtGui

# from browse_pushBtn_callback_file import browse_pushBtn_callback_func


#%% load ui main windows
window = uic.loadUi("Video_Player.ui")

window.setWindowFlag(Qt.WindowMinimizeButtonHint , True)
window.setWindowFlag(Qt.WindowMaximizeButtonHint , True)

window.show()



