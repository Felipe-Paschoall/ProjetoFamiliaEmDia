from werkzeug.security import generate_password_hash

senha = "Senha@123"
hash_senha = generate_password_hash(senha)
print(hash_senha) 