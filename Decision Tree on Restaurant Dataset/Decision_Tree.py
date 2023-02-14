from math import log

YES = "Yes"
NO = "No"
SOME = "Some"
FULL = "Full"
NONE = "None"
CH = "$"
ME = "$$"
EX = "$$$"
F = "French"
T = "Thai"
I = "Italian"
B = "Burger"
Z_10 = "0-10"
T_60 = "30-60"
T_30 = "10-30"
M_60 = ">60"

Alt = [YES, YES, NO, YES, YES, NO, NO, NO, NO, YES, NO, YES]
Bar = [NO, NO, YES, NO, NO, YES, YES, NO, YES, YES, NO, YES]
Fri = [NO, NO, NO, YES, YES, NO, NO, NO, YES, YES, NO, YES]
Hun = [YES, YES, NO, YES, NO, YES, NO, YES, NO, YES, NO, YES]
Pat = [SOME, FULL, SOME, FULL, FULL, SOME, NONE, SOME, FULL, FULL, NONE, FULL]
Price = [EX, CH, CH, CH, EX, ME, CH, ME, CH, EX, CH, CH]
Rain = [NO, NO, NO, YES, NO, YES, YES, YES, YES, NO, NO, NO]
Res = [YES, NO, NO, NO, YES, YES, NO, YES, NO, YES, NO, NO]
Type = [F, T, B, T, F, I, B, T, B, I, T, B]
Est = [Z_10, T_60, Z_10, T_30, M_60, Z_10, Z_10, Z_10, M_60, T_30, Z_10, T_60]
WillWait = [YES, NO, YES, YES, NO, YES, NO, YES, NO, NO, NO, YES]

def Dict_Features(Features):
    Features_Dict = []
    for i in range(len(Features)):
        Dict = {}
        for j in Features[i]:
            if j not in Dict:
                Dict[j] = {"+" : 0, "-" : 0}
        Features_Dict.append(Dict)
    return Features_Dict

def Make_Dict(List, Dict):
    for i in range(len(List)):
        if List[i] != -1:
            if WillWait[i] == YES:
                Dict[List[i]]["+"] += 1
            else:
                Dict[List[i]]["-"] += 1
    return Dict

def P(List, Dict):
    Dict = Make_Dict(List, Dict)
    Probability = []
    for i in Dict:
        Sum = sum(Dict[i].values())
        if Sum != 0:
            for j in Dict[i]:
                Probability.append(Dict[i][j] / Sum)
    return Probability

def Entropy(List, Dict):
    Probabilities = P(List, Dict)
    Sum_Prev = 0
    entropy = 0
    for i in Dict:
        for j in Dict[i]:
            Sum_Prev += Dict[i][j]
    if Sum_Prev != 0:
        for i in Probabilities:
            if i != 0:
                entropy += (i) * (log(i, 10))
    return -entropy

def Make_Node(List, Dict):
    Dict = Make_Dict(List, Dict)
    for i in Dict:
        if Dict[i]["+"] == 0:
            Dict[i] = NO
        elif Dict[i]["-"] == 0:
            Dict[i] = YES
        elif (Dict[i]["+"] == 0 and Dict[i]["-"] == 0) or (Dict[i]["+"] == Dict[i]["-"]):
            Dict[i] = YES
        else:
            Dict[i] = {}
    return Dict

def Insert_Tree(Tree, Node):
    if len(Tree) == 0:
        Tree = Node
        return Tree
    for i,j in Tree.items():
        if isinstance(j, dict):
            Tree[i] = Insert_Tree(j, Node)     
    return Tree    

def Update_Features(Features, Min_Index, Node):
    To_Delete = Features[Min_Index]
    for i in Node:
        if Node[i] != None:
            for j in range(len(To_Delete)):
                if To_Delete[j] == i:
                    for k in range(len(Features)):
                        if k != Min_Index:
                            Features[k][j] = -1
    return Features

def Set_Zero(Features_Dict):
    for i in range(len(Features_Dict)):
        for j in Features_Dict[i]:
            Features_Dict[i][j]["+"] = 0
            Features_Dict[i][j]["-"] = 0
    return Features_Dict

def Update_Tree(Features, Features_Dict, Tree, Desicion):
    Min_Index = Desicion.index(min(Desicion))
    Features_Dict = Set_Zero(Features_Dict)
    Node = Make_Node(Features[Min_Index], Features_Dict[Min_Index])
    Features = Update_Features(Features, Min_Index, Node)
    Tree = Insert_Tree(Tree, Node)
    Features_Dict.pop(Desicion.index(min(Desicion)))
    Features.pop(Desicion.index(min(Desicion)))
    return Features, Features_Dict, Tree

def Find_Best_Feature(Features_Dict, Features):
    Desicion = []
    for i in range(len(Features)):
        Desicion.append(Entropy(Features[i], Features_Dict[i]))
    return Desicion

Features = [Alt, Bar, Fri, Hun, Pat, Price, Rain, Res, Type, Est]
Features_Dict = Dict_Features(Features)
Tree = {}
while len(Features) != 0:
    Desicion = Find_Best_Feature(Features_Dict, Features)
    Features, Features_Dict, Tree = Update_Tree(Features, Features_Dict, Tree, Desicion)
print(Tree)