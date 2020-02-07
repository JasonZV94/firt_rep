frutas = ["Manzana","Pera","Banano","Uva"]

matrix = [["A","B","C","D"], ["E","F","G","H"], ["I","J","K","L"] , ["M","N","O","P"], ["Q","R","S","T"] ]

respuesta = ""

for row in matrix:
    print(respuesta)
    respuesta = ""
    for colum in row:
        respuesta = respuesta + " " + colum



for fruta in frutas:
    if fruta == "Pera":
        print("Si hay coincidencias")