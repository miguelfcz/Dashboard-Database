Este projeto é um dashboard interativo desenvolvido como parte da Imersão de Dados da Alura. O objetivo é visualizar e analisar dados de salários de profissionais da área de Dados, permitindo uma exploração dinâmica através de filtros e gráficos interativos.

A aplicação foi construída para ser uma ferramenta intuitiva, onde os usuários podem segmentar os dados por diversos critérios e extrair insights sobre o mercado de trabalho em Dados.

✨ Funcionalidades

O dashboard oferece uma série de visualizações e filtros para uma análise completa:

    Filtros Interativos: Permite filtrar os dados por:

        Ano

        Nível de Senioridade

        Tipo de Contrato

        Tamanho da Empresa

    Métricas Gerais: Apresenta cartões com informações consolidadas, como:

        Salário Médio (em USD)

        Salário Máximo (em USD)

        Total de Registros na seleção

        Cargo Mais Frequente

    Gráficos Detalhados:

        Top 10 Cargos: Gráfico de barras com os cargos que possuem as maiores médias salariais.

        Distribuição Salarial: Histograma que mostra a frequência de diferentes faixas salariais.

        Trabalho Remoto vs. Presencial: Gráfico de pizza que ilustra a proporção entre os modelos de trabalho.

        Média Salarial por País: Mapa interativo (choropleth) com a média salarial para Cientistas de Dados em diferentes países.

    Visualização de Dados: Tabela interativa com os dados detalhados conforme os filtros aplicados.

🚀 Tecnologias Utilizadas

As seguintes ferramentas e bibliotecas foram essenciais para a construção deste projeto:

    Python: Linguagem principal do projeto.

    Streamlit: Framework utilizado para criar a interface web do dashboard de forma rápida e interativa.

    Pandas: Biblioteca para manipulação e análise dos dados.

    Plotly Express: Biblioteca para a criação dos gráficos interativos e visualmente atraentes.

⚙️ Como Executar o Projeto Localmente

Para rodar este projeto na sua máquina, siga os passos abaixo.
Clone o repositório:

    Bash
    
    git clone https://github.com/miguelfcz/dashboard-database.git

Navegue até o diretório do projeto:

    Bash
    
    cd dashboard-database/Projeto\ Database


Crie um ambiente virtual (recomendado):
    
    Bash
    
    python -m venv venv

No Windows:

    Bash

    venv\Scripts\activate

No macOS/Linux:
    
    Bash

    source venv/bin/activate

Instale as dependências:

    Bash

    pip install -r Requirements.txt

Execute a aplicação Streamlit:

    Bash

    streamlit run App.py

Após executar o último comando, o dashboard será aberto automaticamente no seu navegador padrão.
