from database import salvar_pessoa


print()
print("================================")
print("       WORKGUARD AI")
print("       CADASTRO DE PESSOA")
print("================================")
print()


nome = input("👤 Nome: ")

data_nascimento = input(
    "🎂 Data de nascimento (DD/MM/AAAA): "
)

cargo = input(
    "💼 Cargo: "
)

foto = input(
    "📸 Caminho da foto: "
)


salvar_pessoa(
    nome,
    data_nascimento,
    cargo,
    foto
)


print()
print("================================")
print("✅ CADASTRO REALIZADO!")
print("================================")