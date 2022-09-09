email = input("Informe seu e-mail: ")

var1, var2 = email.split("@")
var3, var4 = var1.split(".")
var5, var6, var7 = var2.split(".")

print(f"var3: {var3}\n"
      f"var4: {var4}\n"
      f"var5: {var5}\n"
      f"var6: {var6}\n"
      f"var7: {var7}\n")
