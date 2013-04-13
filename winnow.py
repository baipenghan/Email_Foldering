from numpy import *
import parse

def ww_train(msgs):
    total_dict = dict()
    labels = set()
    for msg in msgs:
        labels.add(msg.folder_info)
        for pair in msg.dict_info.items():
            if pair[0] in total_dict:
                total_dict[pair[0]] += total_dict[pair[1]] 
            else:
                total_dict[pair[0]] = pair[1]
    
    # Generate final_dict
    for key in total_dict.keys():
        if total_dict[key] == 1:
            del total_dict[key]
    key_list = total_dict.keys()
    print len(key_list), len(labels)
    
    # x_array n*(m+1)
    x_array = []
    
    for msg in msgs:
        x =  [0] * len(key_list) 
        # Add the (m+1)th element in x
        x.append(1)
        for i, key in enumerate(key_list):
            if key in msg.dict_info:
                
    
    
    
    
    
    



if __name__ == "__main__":
    root_path = '../maildir'
    user_array = parse.get_msg_info(root_path)
    print len(user_array)
    usr = user_array[0]
    slot_size = len(usr) / 10
    ww_train(usr[0: slot_size - 1])

