from cryptography.fernet import Fernet
import os

# Mesma chave usada no encrypter
CHAVE = b'sua_chave_aqui_em_base64'  # Deve ser idêntica à do encrypter

def descriptografar_arquivo(caminho_arquivo_criptografado):
    fernet = Fernet(CHAVE)
    
    with open(caminho_arquivo_criptografado, 'rb') as arquivo:
        dados_criptografados = arquivo.read()
    
    try:
        dados_descriptografados = fernet.decrypt(dados_criptografados)
        
        # Remove a extensão '.enc' para restaurar o nome original
        caminho_saida = caminho_arquivo_criptografado.replace('.enc', '')
        with open(caminho_saida, 'wb') as arquivo_saida:
            arquivo_saida.write(dados_descriptografados)
        
        print(f"Arquivo descriptografado salvo como: {caminho_saida}")
    except Exception as e:
        print(f"Erro na descriptografia: {e} (verifique se a chave está correta)")

# Exemplo de uso: descriptografar 'exemplo.txt.enc'
descriptografar_arquivo('exemplo.txt.enc')