# 🔐 File Encryptor / Decryptor

> Implementação simples de criptografia e descriptografia de arquivos em **Python**, utilizando a biblioteca `cryptography` com o algoritmo **Fernet**.  
> Desenvolvido como parte de um desafio da plataforma [Dio.me](https://www.dio.me/), com fins **educacionais** e de **estudo em segurança cibernética**.

---

## ⚠️ Aviso Importante
Este projeto é **exclusivamente para aprendizado**.  
Não deve ser usado para criptografar dados sensíveis em produção ou para fins maliciosos.  
Utilize-o para compreender os conceitos de **criptografia simétrica**, **gerenciamento de chaves** e **boas práticas de segurança**.

---

## 🚀 Funcionalidades
- **Criptografar arquivos**: lê um arquivo, criptografa e gera uma versão com extensão `.enc`.  
- **Descriptografar arquivos**: lê um arquivo `.enc` e restaura o original.  
- **Uso de chave simétrica**: ambos os scripts compartilham a mesma chave secreta (gerada via `Fernet`).  
- **Tratamento básico de erros**: valida a chave durante o processo de descriptografia.  

---

## 🧩 Pré-requisitos
- Python **3.6+**  
- Biblioteca `cryptography` instalada:
  ```bash
  pip install cryptography
📦 Instalação
bash
Copiar código
git clone https://github.com/samueldias99/projeto-dio-ransoware-.git
cd projeto-dio-ransoware-
🔑 Gerar uma Chave Secreta (opcional, mas recomendado)
No terminal Python:

python
Copiar código
from cryptography.fernet import Fernet
print(Fernet.generate_key())
Copie a chave gerada e substitua o valor da variável CHAVE nos scripts encrypter.py e decrypter.py.

⚙️ Como Usar
🔸 Criptografar um arquivo
Edite encrypter.py e adicione sua chave na variável CHAVE.

Execute o script:

bash
Copiar código
python encrypter.py
O arquivo criptografado será salvo como exemplo.txt.enc.

🔹 Descriptografar um arquivo
Edite decrypter.py com a mesma chave usada na criptografia.

Execute o script:

bash
Copiar código
python decrypter.py
O arquivo original será restaurado sem a extensão .enc.

🗂️ Estrutura do Projeto
bash
Copiar código
projeto-dio-ransoware-/
├─ encrypter.py      # Script para criptografia
├─ decrypter.py      # Script para descriptografia
├─ exemplo.txt       # Exemplo de arquivo usado nos testes
└─ README.md         # Documentação do projeto
