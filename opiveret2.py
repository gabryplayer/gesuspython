









import urllib.request
import time

def hackeraggio(url):
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')

    print("\n")
    print("██████╗ ███████╗██╗   ██╗ ██████╗ ████████╗    ███████╗██╗███╗   ██╗███████╗")
    print("██╔══██╗██╔════╝██║   ██║██╔═══██╗╚══██╔══╝    ██╔════╝██║████╗  ██║██╔════╝")
    print("██████╔╝█████╗  ██║   ██║██║   ██║   ██║       █████╗  ██║██╔██╗ ██║███████╗")
    print("██╔══██╗██╔══╝  ██║   ██║██║   ██║   ██║       ██╔══╝  ██║██║╚██╗██║╚════██║")
    print("██║  ██║███████╗╚██████╔╝╚██████╔╝   ██║       ██║     ██║██║ ╚████║███████║")
    print("╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝")
    print("\n")

    print("[+] Accesso riuscito!")
    print(">> Infiltrazione in corso...")
    print(">> Sito web compromesso con successo!")

    print("\n[+] Informazioni sul sito web:")
    print("[-] URL: " + url)
    print("[-] Contenuto HTML:")
    print(content)

    print("\n[-] Contenuto CSS:")
    css_start = content.find("<style>")
    css_end = content.find("</style>")
    css_content = content[css_start + 7:css_end].strip()
    print(css_content)

    print("\n[-] Contenuto JavaScript:")
    js_start = content.find("<script>")
    js_end = content.find("</script>")
    js_content = content[js_start + 8:js_end].strip()
    print(js_content)

if __name__ == "__main__":
    print("\n██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗ ███████╗████████╗")
    print("██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗██╔════╝╚══██╔══╝")
    print("██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝█████╗     ██║")
    print("██║  ██║██╔═══╝ ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══╝     ██║")
    print("██████╔╝██║     ██║ ╚████╔╝ ███████╗██║  ██║███████╗   ██║")
    print("╚═════╝ ╚═╝     ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝")
    print("\n")

print(" _______________________________________________________________________________")     
print("¦ ---------------------------------OPIVERET2------------------------------------¦")
print("¦...............................................................................¦")
print("---------------------------------------------------------------------------------")

url = input("Inserisci l'URL del sito web: ")
confirmation = input("Sei sicuro? (y/n)")

if confirmation == "y":
    
    print("10%")
    time.sleep(3)
    print("35%")
    time.sleep(3)
    print("50%")
    time.sleep(3)
    print("88%")
    time.sleep(3)
    print("100%")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    hackeraggio(url)


    

    
