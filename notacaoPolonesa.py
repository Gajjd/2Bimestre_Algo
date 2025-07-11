class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class Pilha:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    def push(self, no):
        no.next = self.top
        self.top = no
        self.size +=1
        print(f"Elemento {no.valor} inserido")

    def __str__(self):
        if self.top is not None:
            no = self.top
            pilha_listaem = []
            while no is not None:
                pilha_listaem.append(f"{no.valor}")
                no = no.next
            return "\n-----\n".join(pilha_listaem)
        else:
            return "A pilha está vazia"   
        
    def pop(self):
        if(self.size > 0):
            self.top = self.top.next
            self.size -= 1  
            
    def topo(self):
        if self.top is not None:
            return self.top.valor
        else:
            return "A pilha está vazia"
            
    def tamanho(self):
        return self.size              
   

if __name__ == "__main__":
    input("Insira um número ou um operacional (+,-,*,/)")
