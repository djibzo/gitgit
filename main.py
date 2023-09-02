import json

class Reseau:
    def __init__(self,n,m,noeud,connexions) -> None:
        self.n=n
        self.m=m
        self.noeud=noeud
        self.connexions=connexions

def loadFic(filename):
    with open(filename,"r") as f:
        contenue=f.readlines()
        contenue = [i.strip() for i in contenue if not i.startswith('#') and len(i)>1]
        met_dat=[int(i) for i in contenue[0].split(',')]
        n,m=met_dat
        del contenue[0]
        noeud_dat=None
        conn=[]
        for i in contenue:
            if i.startswith("N"):
                noeud_dat=i.split(',')
            else:
                conn.append(tuple(i.split(',')))
        conn=[(int(i[0]),int(i[1])) for i in conn]
        noeud_dat={i:v for i,v in enumerate(noeud_dat)}
        conn={i:v for i,v in enumerate(conn)}
        Reseau={}
        Reseau['n']=n
        Reseau['m']=m
        Reseau['noeud']=noeud_dat
        Reseau['conn']=conn
        f.close()
    return Reseau

reseau=loadFic("reseau.txt")

def saveNet(filename,reseau):
    with open(filename,"w") as f:
        json.dump(reseau,f)
        print("Success !")


r1= Reseau(reseau['n'],reseau['m'],reseau['noeud'],reseau['conn'])

def ifConn(n1,n2):
    for i in r1.connexions.values():
        if str(i)==str((n1, n2)) or str(i)==str((n2, n1)):
            return True
    return False

tab=[0,1,2,5,6,10]
def connect(Tab):
    for i in range(len(Tab)-1):
        if ifConn(Tab[i],Tab[i+1])==True:
            print(f"Le noeud {Tab[i]} et le noeud {Tab[i+1]} sont connectes\n")
connect(tab)