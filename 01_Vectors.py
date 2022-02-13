class C2dVector:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"The 2-D Vector is {self.icap}i + {self.jcap}j"
    
class C3dVector(C2dVector,):
    def __init__(self,i,j,k):
    
        self.icap = i
        self.jcap = j
        self.kcap = k

    def __str__(self):
        return f"The 2-D Vector is {self.icap}i + {self.jcap}j + {self.kcap}k"

v2 = C2dVector(1,3)
v3 = C3dVector(2,7,8)
print(v2)
print(v3)

    
