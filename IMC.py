def calculador_imc(pessoa):
    imc = pessoa["peso"] / (pessoa["altura"] * pessoa["altura"])
    resultado = (f"O IMC {pessoa["nome"]} é {imc:.2f}")
    saudavel = 18.5 < imc <25

    return{
        "nome": {pessoa["nome"]},
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel
    } 

pessoa1 = {
    "nome": "José",
    "peso": 110,
    "altura": 1.75
}

pessoa = {
    "nome": input("Digite seu nome: "),
    "peso": float(input("Digite seu peso: ")),
    "altura": float(input("Digite sua altura: "))
}

print (calculador_imc(pessoa))

    





