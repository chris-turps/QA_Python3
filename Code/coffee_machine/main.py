'''
SR: to run the machine
'''
from initialise import *
from state_machine import *

while cm_state != CM_state.OFF:
    cm_state = state_machine(cm_state)