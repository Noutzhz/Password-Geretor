import random
import string

def gerar_senhas (Tamanho): # a função gerar_senha() recebe o tamanho desejado da senha como parâmetro./функция generate_password() получает желаемую длину пароля в качестве параметра.
    caracteres_primitivos = string.ascii_letters + string.digits + string.punctuation
    senha = ''.Join(random.choice(caracteres_primitivos) for _ in range(Tamanho))
    return(senha)

Tamanho_senha = int(input("Digite o tamanho desejado para senha/Введите желаемую длину пароля:"))
senha_gerada = gerar_senhas(Tamanho_senha)
print("Senha gerada:", senha_gerada)
