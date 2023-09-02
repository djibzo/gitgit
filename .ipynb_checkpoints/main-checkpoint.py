import json
def loadNet():
    pass

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
print(reseau)
def saveNet(filename,reseau):
    with open(filename,"w") as f:
        json.dump(reseau,f)
        print("Success !")

#saveNet("reseau_js.json",reseau)
