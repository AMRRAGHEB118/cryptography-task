with open('newMessage.txt', 'r') as file: 
     content = file.read().strip()

def transposition(message): 
    key = "982751" 
    step = len(key)
    message = message.replace(" ", "")
    matrix = []
    for i in range(0, len(message), step):
        matrix.append(list(message[i:i+step])) 

    transposed_matrix = list(zip(*matrix))
    transposed_content = ''.join([''.join(row) for row in transposed_matrix])
    return transposed_content



result =  transposition(content)

with open('newMessage.txt', 'w') as file: 
     content = file.write(result)    