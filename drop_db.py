import os

if os.path.exists("biblioteca.db"):
    os.remove("biblioteca.db")
    print("✅ biblioteca.db eliminado.")
else:
    print("⚠️ biblioteca.db no existe.")
