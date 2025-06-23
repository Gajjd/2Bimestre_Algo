class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class pilha:
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
          
if __name__ == "__main__":
    pilha = pilha()
    print(pilha)
    pilha.push(No(0))
    pilha.push(No(2))
    pilha.push(No(3))
    pilha.push(No(4))
    pilha.push(No(5))
    pilha.push(No(9))
    print(pilha)