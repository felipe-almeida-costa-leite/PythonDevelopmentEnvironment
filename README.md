# PythonDevelopmentEnvironment
A ideia deste projeto é criar um ambiente de desenvolvimento em python, que siga as boas práticas.

## Ambiente
### Sistema Operacional
Como interface de desenvolvimento, vamos utilizar o Windons, porém, com o Linux por trás, isso pode ser alcançado pelo WSL.
#### WSL
O guia de instalação completo do wsl está disponível no link [WSL](https://docs.microsoft.com/pt-br/windows/wsl/install-win10).
Processo de instalação:
1. Habilite o WSL:

    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
2. Habilite o recurso de VM:
    
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
3. Baixe o pacote do kernerl do linux:
    
    https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
4. Selecione o WSL2 como default:
    
    wsl --set-default-version 2
5. Abra a Microsoft Store e selecione uma distribuição linux.

### IDE
Para a IDE será utilizado o Pycharm versão community, por conta de ser versão community não é possível criar um projeto automático com virtualenv pelo pychamr, ou seja isso sera feito de maneira manual por nós.
[PyCharmCommunity](https://www.jetbrains.com/pt-br/pycharm/download/download-thanks.html?platform=windows&code=PCC)
#### Configuração
Vamos realizar a padronização da configuração da IDE, que consiste em:
1. Habilitar Todas as verificações PEP
2. Baixar o pacote de idioma Português.
## Desenvolvimento
### Pacotes Utilizados
Será utilizado os seguintes pacotes:
* Virtualenv - Para criar e manter o ambiente virtual;
* Pylint e Flake8 - Para padronização e verificação de código;
* Black - Para formatação correta do código;
* Pycodestyle - Validação da formatação do código;
* Pydocstyle - Para garantir que seja feito a documentação;
* MyPy - Forcar a tipagem estática do código;
* Pre-Commit - Para garantir que tudo seja feito antes de cada commit.
### Estrutura Diretório
Todo projeto baseado neste "framework", terá a segunda estrutura:
```
Root
   |- README.md
   |- .venv
   |- .flake8
   |- .gitignore
   |- .pre-commit-config.yaml
   |- .pylintrc
   |- requirements.txt
   |- src
   |   |-- main
   |       |-- code.py
   |   |-- test
   |       |-- code_test.py
   |- setup
   |   |-- setup.py
   |- build
   |   |-- project.zip
```
### Setup
Esse programa visa realizar todo processo após o clone do repositório, além de desenvolver também um pacote python que provisiona todo o ambiente quando necessário.
