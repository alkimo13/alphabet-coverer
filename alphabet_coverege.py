from colorama import Fore
given_string = "abc"
listed = [*given_string]
alphabet = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
print(f"{Fore.GREEN}Green-----> exists")
print(f"{Fore.RED}Red-----> not exists")
sayaç = 0
for i in alphabet:
    if i in listed:
        print(f"{Fore.GREEN}{i}",end=" ")
        sayaç = sayaç+1
    else:
        print(f"{Fore.RED}{i}",end=" ")
if sayaç == 29:
    sayaç = "all(29)"
print("\n")
print(f"{Fore.CYAN}Given string covers {sayaç} letters in alphabet.")