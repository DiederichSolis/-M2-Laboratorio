
prencendencia = {'+': 1, '.': 2, '*': 3}


def is_operator(c: str) -> bool:
    return c in prencendencia

def is_operand(c: str) -> bool:
    return c.isalnum() or c == '_'

def insert_concatenation_operators(infix: str) -> str:
    result = [] 
    length = len(infix)  
   
    for i in range(length):
        result.append(infix[i])  
        if i < length - 1:
        # El carácter actual es '*' y el siguiente es un operando o un paréntesis abierto
            if (is_operand(infix[i]) and (is_operand(infix[i+1]) or infix[i+1] == '(')) or \
               (infix[i] == ')' and (is_operand(infix[i+1]) or infix[i+1] == '(')) or \
               (infix[i] == '*' and (is_operand(infix[i+1]) or infix[i+1] == '(')):
                result.append('.')  

    return ''.join(result)


def toPostFix(infixExpression: str) -> str:
    
    infixExpression = insert_concatenation_operators(infixExpression)

    output = []
    operador = []  

    i = 0
   
    while i < len(infixExpression):
        c = infixExpression[i]

        if is_operand(c):  
            output.append(c)
        elif c == '(': 
            operador.append(c)
        elif c == ')':  
            while operador and operador[-1] != '(':
                output.append(operador.pop()) 
            operador.pop()  
        elif is_operator(c):  
            
            while (operador and operador[-1] != '(' and
                   prencendencia[operador[-1]] >= prencendencia[c]):
                output.append(operador.pop())
            
            operador.append(c)
        i += 1

  
    while operador:
        output.append(operador.pop())
    
 
    return ''.join(output)

if __name__ == "__main__":
    infix = "(0+1)*11(0+1)*"
    postfix = toPostFix(infix)
    print(f"Infijo: {infix}")  
    print(f"Postfijo: {postfix}") 
