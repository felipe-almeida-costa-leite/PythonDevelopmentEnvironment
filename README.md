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
* Pytest - Para testar nosso código;
* PyBuild - Para build do nosso código;
* Pre-Commit - Para garantir que tudo seja feito antes de cada commit.
  Para facilitar a criação do ambiente, baixe o pacote [pydenv](https://pypi.org/project/pydenv/) e faça o provisionamento
  automático do ambiente.
### Estrutura Diretório
Todo projeto baseado neste "framework", terá a segunda estrutura:
```
Root
   |- .flake8
   |- .gitignore
   |- .pre-commit-config.yaml
   |- .pydocstyle.ini
   |- .pylintrc
   |- conftest.py
   |- mypy.ini
   |- LICENSE
   |- README.md
   |- requirements.txt
   |- src
   |   |-- main
   |       |-- code.py
   |   |-- test
   |       |-- code_test.py
   |- build
   |   |-- project.zip
```
### Boas práticas
A ideia é seguir boas de desenvolvimento e ter elas relatadas aqui. Uma espécie de livro de tudo isso junto e aplicado.

Como a utilização do Clean Code, Clean Architecture, SOLID, Design Patterns, TDD, JET e afins...


#### Clean Code
A ideia principal é ter um código bem escrito,
no sentido de, imaginar que a leitura e entendimento do código seja possível em até 3 minutos.
Para que isso seja possível é necessário definir algumas diretrizes para a escrita de código,
que se extende desde nome de variáveis até quando transformar uma função em classe e afins....

#### Variavéis
#### Nome Significativo
Os nomes de variavéis devem ser significativo e diretos ou seja, 
você não precisa de mais nenhum elemento fora o nome da variavel para entender o quê ela está representando.
Exemplos:
* Mau:
```python
import datetime
da = datetime.date.today().strftime("%y-%m-%d")
```
* Bom:
```python
import datetime

data_atual_formato_americano = datetime.date.today().strftime("%y-%m-%d")
data_atual_formato_brasileiro = datetime.date.today().strftime("%d/%m/%y")
```
Veja como os nomes das variaveis são claros. O primeiro exemplo tem um nome qualquer que necessita de conhecimento
do módulo datetime para entender qual será o dado que a variavel da irá guardar, porém no segundo exemplo
já não é necessário, apenas pelo nome já se sabe qual é o dado (data atual) e o formato ainda.
#### Nome Significativo
