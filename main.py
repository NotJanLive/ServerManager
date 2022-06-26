from ensurepip import version
import os, requests 
def get_version(version):
    if version == "1.8":
        download(8)
    elif version == "1.12":
        download(12)
    elif version == "1.16":
        download(16)
    elif version == "1.18":
        download(18)
    elif version == "1.19":
        download(19)
    elif version == "Bungeecord":
        download(1)      
    else:
        print("Diese Version existiert nicht!")
        exit()

def download(wanted_version):
    if wanted_version == 8:
        os.system("cls")
        print("Lade nötige Dateien herunter...")
        response = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar")
        open("server.jar", "wb").write(response.content)
    elif wanted_version == 12:
        os.system("cls")
        print("Lade nötige Dateien herunter...")
        response = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar")
        open("server.jar", "wb").write(response.content)  
    elif wanted_version == 16:
        os.system("cls")
        print("Lade nötige Dateien herunter...")
        response = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar")
        open("server.jar", "wb").write(response.content)  
    elif wanted_version == 18:
        os.system("cls")
        print("Lade nötige Dateien herunter...")
        response = requests.get("https://download.getbukkit.org/spigot/spigot-1.18.2.jar")
        open("server.jar", "wb").write(response.content)
    elif wanted_version == 19:
        os.system("cls")
        print("Lade nötige Dateien herunter...")
        response = requests.get("https://download.getbukkit.org/spigot/spigot-1.19.jar")
        open("server.jar", "wb").write(response.content)
    elif wanted_version == 1:
        os.system("cls")
        print("Lade nötige Dateien herunter...")
        response = requests.get("https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar")
        open("server.jar", "wb").write(response.content) 
        
def setup_server(ram):
    ram = int(ram) 
    os.system("cls")
    print("Setze alles für dich auf...")
    start_server(ram)
    version = get_version
    if not version == "bungeecord":
        os.system("cls")
        print("Akzeptiere die EULA für dich")
        os.remove("eula.txt")
        with open('eula.txt', 'w') as f:
            f.write('eula=true')
            f.close()
    write_start_file(ram)
    start_server(ram)

def start_server(ram):
    os.system(f"java -Xmx{ram}G -Xms{ram}G -jar server.jar nogui PAUSE")

def write_start_file(ram):
    with open('start.bat', 'w') as f:
        f.write(f'java -Xmx{ram}G -Xms{ram}G -jar server.jar nogui PAUSE')
        f.close()

def main():
    os.system("cls")
    print("\nAuf welcher Version soll dein Minecraft-Server laufen?")
    print("""
###################
#       1.8       #
#       1.12      #
#       1.16      #
#       1.18      #
#       1.19      #  
#    Bungeecord   #
################### 
""")
    version = input(">>>")
    dir = version + " Server"
    os.mkdir(dir)
    path = os.getcwd() + "\\" + version + " Server"
    os.chdir(path)
    get_version(version)
    os.system("cls")
    print("Wie viel RAM soll dein server haben? (4GB ist empfohlen)")
    print("""
#############
#  1 GB RAM #
#  2 GB RAM #
#  4 GB RAM #
#  8 GB RAM #
#############
""")
    ram = input(">>>")
    setup_server(ram)
main()