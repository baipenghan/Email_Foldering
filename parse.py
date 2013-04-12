import email
from datetime import datetime
import os
import filter
from collections import namedtuple

# root path
root_path = '../maildir'

#def comparator(msg1, msg2):
#    t = datetime.datetime.strptime(msg1, "%a, %d %b %Y %H:%M:%S %Z")

class Msg:
    def __init__(self, date_info, from_info, folder_info, header_info, body_info):
        self.date_info = date_info
        self.from_info = from_info
        self.folder_info = folder_info
        self.header_info = header_info
        self.body_info = body_info
        self.dict_info = []

# check if time is legal, only for testing
def check_time(time_list):
    if time_list[3] < 0 or time_list[3] > 23:
        print('Illegal hour: ' + time_list[3])
        
    if time_list[1] == 1 or time_list[1] == 3 or time_list[1] == 5 or time_list[1] == 7 or time_list[1] == 8 or time_list[1] == 10 or time_list[1] == 12:
        if time_list[2] < 1 or time_list[2] > 31:
            print('Illegal month and date: ' + time_tuple[1] + ' ' + time_tuple[2])
    elif time_list[1] == 4 or time_list[1] == 6 or time_list[1] == 9 or time_list[1] == 11:
        if time_list[2] < 1 or time_list[2] > 30:
            print('Illegal month and date: ' + time_tuple[1] + ' ' + time_tuple[2])
    elif time_list[1] == 2:
        if time_list[0] % 4 == 0 and time_list[0] % 100 != 0 or time_list[0] % 400 == 0:
            if time_list[2] < 1 or time_list[2] > 29:
                print('Illegal year, month and date: ' + time_list[0] + ' ' + time_list[1] + ' ' + time_list[2])
        else :
            if time_list[2] < 1 or time_list[2] > 28:
                print('Illegal year, month and date: ' + time_list[0] + ' ' + time_list[1] + ' ' + time_list[2])
    else:
        print('Illegal month: ' + time_list[1])

# given a 10-tuple representing time, change PDT to PST
def pdt_to_pst (time_tuple):
    if (time_tuple[-1] == '-25200'):
        if (time_tuple[3] > 0):
            time_tuple[3] = time_tuple[3] - 1
        else:
            time_tuple[3] = 23
            if (time_tuple[2] > 1):
                time_tuple[2] = time_tuple[2] - 1
            else:
                time_tuple[1] = time_tuple[1] - 1
                if time_tuple[1] == 4 or time_tuple[1] == 6 or time_tuple[1] == 8 or time_tuple[1] == 9:
                    time_tuple[2] = 31
                elif time_tuple[1] == 5 or time_tuple[1] == 7 or time_tuple[1] == 10:
                    time_tuple[2] = 30

# get date, from, header, folder and body from msgs of one user.
def get_msg_info_user (root):
    msg_array = []
    
    for folder in os.listdir(root):
        folder_path = os.path.join(root, folder)
        for msg in os.listdir(folder_path):
            file_path = os.path.join(folder_path, msg)
            f = open(file_path, 'r')
            
            content = f.read()
            msg = email.message_from_string(content)

            date = msg['Date'][5:][:-6]
            time_list = list(email.utils.parsedate_tz(date))
            pdt_to_pst(time_list)
            time_list = time_list[:-4]
            m = Msg(time_list, msg['From'], msg['Subject'], msg['X-Folder'], msg.get_payload())
            msg_array.append(m)

    return msg_array

# compare two msgs by timestamp
def compare(msg1, msg2):
    return compare_time(msg1.date_info, msg2.date_info)

# compare two timestamps represented by time list
def compare_time(time_list1, time_list2):
    if time_list1[0] < time_list2[0]:
        return -1
    elif time_list1[0] > time_list2[0]:
        return 1
    else:
        if time_list1[1] < time_list2[1]:
            return -1
        elif time_list1[1] > time_list2[1]:
            return 1
        else:
            if time_list1[2] < time_list2[2]:
                return -1
            elif time_list1[2] > time_list2[2]:
                return 1
            else:
                if time_list1[3] < time_list2[3]:
                    return -1
                elif time_list1[3] > time_list2[3]:
                    return 1
                else:
                    if time_list1[4] < time_list2[4]:
                        return -1
                    elif time_list1[4] > time_list2[4]:
                        return 1
                    else:
                        if time_list1[5] < time_list2[5]:
                            return -1
                        elif time_list1[5] > time_list2[5]:
                            return 1
                        else:
                            return 0

# driver
def get_msg_info (root_path):
    user_array = []
    
    for user in os.listdir(root_path):
        if (user == 'farmer_d'):
            user_path = os.path.join(root_path, user)
            msg_array = get_msg_info_user(user_path)

            sorted_msg_array = sorted(msg_array, cmp = compare)

            for msg in sorted_msg_array:
                msg.dict_info = filter.filter(msg.header_info + msg.body_info)
                print(msg.dict_info.items())
            user_array.append(msg_array)
    return user_array

get_msg_info(root_path)


