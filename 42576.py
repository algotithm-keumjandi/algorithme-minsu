def solution(participant, completion):
    dict_marathon = {}
    for parti in participant : 
        dict_marathon[parti] = dict_marathon.get(parti,0)+1
    #print(dict_par)
    for compl in completion :
        dict_marathon[compl] -=1
    #print(dict_par)
    for di in dict_marathon :
        if dict_marathon[di] == 1:
            return di