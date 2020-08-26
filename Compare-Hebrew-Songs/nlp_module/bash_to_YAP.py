import subprocess
import json

## COMANDO QUE ABRE O TERMINAL E EXECUTA O COMANDO DEFINIDO EM COMMAND
## ESSE COMANDO ACESSA O WSL E EXECUTA O PROGRAMA YAP RETORNANDO UM .TXT .lattice
def callps1(command):
    A = subprocess.Popen('wsl.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = A.communicate(command)
    print("the out", out, "and the err", err)

## every path is identifye in a unified location
def load_paths():
    with open('paths.json') as jsonfile:
        paths = json.load(jsonfile)
    return paths


def gen_command(nome):
    paths = load_paths()
    command = bytes('''
    cd 
    cd yapproj/src/yap
    ls
    ./yap hebma -raw /mnt/c/Users/Daniel/PycharmProjects/songsSimmilaritiesPython/'nlp_module'/{}/{} -out /mnt/c/Users/Daniel/PycharmProjects/songsSimmilaritiesPython/'nlp_module'/{}/{}.lattice
    '''.format(paths['inputlyrics'], nome, paths['outputlattice'], nome), encoding='utf-8')
    return command

if __name__ == "__main__":
    callps1(gen_command("oi"))
