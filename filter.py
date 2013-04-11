import nltk

one_hundred = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'I', 'at', 'be', 'this', 'have', 'from', 'or', 'had', 'by', 'but', 'not', 'what', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'an', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'then', 'them', 'these', 'so', 'her', 'would', 'him', 'into', 'has', 'no', 'could', 'my', 'than', 'been', 'who', 'its', 'down', 'did', 'may']
one_hundred = set(one_hundred)
taggers = ['ABL', 'ABN', 'ABX', 'AP', 'CD', 'EX', 'FW', 'JJ', 'JJR', 'JJS', 'JJT', 'NC', 'NN', 'NN$', 'NNS', 'NNS$', 'NP', 'NP$', 'NPS', 'NPS$', 'NR', 'OD', 'PN', 'RB', 'RBR', 'RBT', 'RN', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
taggers = set(taggers)
punctuation = '.?!,#*():;\'\"'

def filter(fname):
    f = open(fname, 'r')
    
    final_tuple = []
    word_dic = dict()
    subject = ''
    tagged = []
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        if line.startswith('Subject'):
            start_index = len('Subject: ')
            subject = line[start_index:]
        if line.startswith('X-FileName'):
            break
    
    #Parse Subject
    
    subject_tokens = nltk.word_tokenize(subject)
    subject_tagged = nltk.pos_tag(subject_tokens)
    for pair in subject_tagged:
        if pair[1] in taggers and pair[0].lower() not in one_hundred:
            final_tuple.append(pair)
    
    
    #Parse Body
    body = f.readlines()
    
    for sentence in body:
        #NLTK
        tokens = nltk.word_tokenize(sentence)
        tagged += nltk.pos_tag(tokens)
    
    for pair in tagged:
        if pair[1] in taggers and pair[0].lower() not in one_hundred and pair[0] not in punctuation:
            final_tuple.append(pair)
    
    for pair in final_tuple:
        word = pair[0].lower()
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    '''
    Remove only appering once word in dictionary
    
    for key in word_dic.keys():
        if word_dic[key] == 1:
            del word_dic[key]
    
    '''
    
    print word_dic

    
filter('/Users/taurus/Documents/CPSC540/preschedule/1')
