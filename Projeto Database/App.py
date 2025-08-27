import pandas as pd
import plotly.express as px
import streamlit as st

#Definição do título e ícone da página
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="💰",
    layout='wide',
)

df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

#Barra lateral
st.sidebar.header('Filtros')

#Filtra para os anos
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect('Ano', anos_disponiveis, default=anos_disponiveis)

#Filtra para as senioridades
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect('Senioridade', senioridades_disponiveis, default=senioridades_disponiveis)

#Filtra para os contratos
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect('Contrato', contratos_disponiveis, default=contratos_disponiveis)

#Filtra para os cargos
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_disponiveis = st.sidebar.multiselect('Tamanho da Empresa', tamanhos_disponiveis, default=tamanhos_disponiveis)


#O dataframe será filtrado conforme as escolhas feitas na barra lateral
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_disponiveis))
]

#Header do Dashboard
st.title('Dashboard de Análise salarial na Área de Dados')
st.markdown('Explore os dados de salários na área de dados, filtrando por ano, senioridade, contrato e tamanho da empresa.')

#Subheader
st.subheader("Métricas Gerais (Salário anual em USD)")

if not df_filtrado.empty:   #Verifica se o DataFrame filtrado não está vazio
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
else:
    salario_medio = 0
    salario_maximo = 0
    total_registros = 0
    cargo_mais_frequente = ""

#Indicadores importantes
col1, col2, col3, col4 = st.columns(4)
col1.metric('Salário Médio', f"${salario_medio:.2f}")
col2.metric('Salário Máximo', f"${salario_maximo:.2f}")
col3.metric('Total de registros', total_registros)
col4.metric('Cargo mais frequente', cargo_mais_frequente)

col_graf1, col_graf2 = st.columns(2)

# criação dos gráficos
with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title='Cargos com maiores salários',
            labels={'usd': 'Salário Anual (USD)' , 'cargo': 'Cargo'},
        )
        # Atualiza o layout do gráfico
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para exibir o gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title='Distribuição de salários anuais',
            labels={'usd': 'Salário Anual (USD)', 'Count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para exibir o gráfico de distribuição de salários.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho (Remoto/Presencial)',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para exibir o gráfico de tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(
            media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Média Salarial de Cientitas de Dados por País',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
        )
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de países.')

# Dados detalhados
st.subheader('Dados Detalhados')
st.dataframe(df_filtrado)