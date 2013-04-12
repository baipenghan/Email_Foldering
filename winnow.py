import numpy as np
import parse

def ww_train(msgs):
    
    



if __name__ == "__main__":
    root_path = '../maildir'
    user_array = parse.get_msg_info(root_path)
    usr = user_array[0]
    slot_size = len(usr) * 0.1
    ww_train(usr[0: slot_size - 1])

