# Project TING (Trybe is not Google)

- O Projeto foi implementado visando simular um algorítimo de indexação de documentos semelhante ao utilizado pelo Google, o programa analisa e identifica ocorrências de termo em arquivos TXT, além de alguns testes para as funções e classes desenvolvidas.

- O Projeto desenvolvido se divide em dois módulos:
  - **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato TXT).
  - **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

---

# Tecnologias utilizadas :books:

- Python

---

# Como Utilizar a aplicação

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:matheusnff85/project-ting.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd project-ting`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  4. Após isso para utilizar a aplicação utilize o comando abaixo:

  - `python3 -m ting_word_searches.word_search`

  - Com isso duas funções são habilitadas para uso, a `search_by_word` e a `exists_word`, as duas esperam dois parâmetros, o primeiro sendo a **palavra a ser buscada** e o segundo a **instância da classe Queue**.

    - A primeira `search_by_word("programa", queue_instance)` retorna as informações obtidas de forma mais completa como exemplificado abaixo:

    ```Python
    [
      {
        "palavra": "programa", 
        "arquivo": "statics/novo_paradigma_globalizado.txt", 
        "ocorrencias": [
            {
              "linha": 6, 
              "conteudo": "Do mesmo modo, a execução dos pontos do programa [...]",
            }, 
            {
              "linha": 33, 
              "conteudo": "Por outro lado, [...] pontos do programa [...]",
            },
        ],
      },
    ]
    ```

    - Já a segunda, `exists_word("programa", queue_instance)`, retorna um relatório um pouco menos detalhado.
    
    ```Python
    [
      {
        "palavra": "programa",
        "arquivo": "statics/new_globalized_paradigm.txt",
        "ocorrencias": [
            {"linha": 6},
            {"linha": 33}
        ],
      },
    ]
    ```

---

- Desenvolvido por [Matheus Marinho](https://www.linkedin.com/in/matheus-marinhodsp/).