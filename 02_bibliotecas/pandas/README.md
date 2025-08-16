# 📊 Pandas — Manipulação e Análise de Dados

Este diretório reúne exemplos práticos de uso do **Pandas**, biblioteca essencial para análise e manipulação de dados em Python.  
Os notebooks e scripts foram criados com o objetivo de **demonstrar domínio das principais funcionalidades da biblioteca**, aplicadas em diferentes contextos.

---

## 📂 Estrutura

pandas/  
├── 📓 fundamentos/               # Conceitos essenciais  
│   ├── 01_estruturas_basicas.ipynb  
│   └── 02_operacoes_core.ipynb  
│  
├── 🔍 analise/                   # Análise exploratória profissional  
│   ├── eda_automotivo.ipynb  
│   └── eda_financeiro.ipynb  
│   
├── ⚙️ processamento/            # Engenharia de dados  
│   ├── combinacao_dados/  
│   │   ├── merge_vs_concat.ipynb  
│   │   └── join_patterns.py  
│   │  
│   ├── tratamento/  
│   │   ├── missing_values.ipynb  
│   │   └── outliers.ipynb  
│   │
│   └── temporais/  
│       ├── datetime_advanced.ipynb  
│       └── resampling_financeiro.py  
│

---

## 📌 Conteúdo da pasta

### introducao.ipynb
Criação e manipulação de **Series** e **DataFrames**:
- Criação de Series e DataFrames a partir de listas, dicionários e arrays
- Indexação e seleção de dados
- Filtragem e ordenação
- Alteração de tipos e renomeação de colunas

### analise_exploratoria.ipynb
Análise exploratória (EDA) em dataset real:
- Estatísticas descritivas (`info()`, `describe()`)
- Contagem de valores e distribuição de dados
- Detecção de outliers e inconsistências
- Visualização inicial de dados (gráficos simples)

### casos_especiais/

#### combinando_dados.ipynb
Exemplos de como unir e mesclar datasets diferentes usando:
- `merge()`, `concat()`, `join()`
- Técnicas de alinhamento por chaves e índices
- Exemplos com datasets reais simulados

#### missing_values.ipynb
Demonstração de técnicas para lidar com valores ausentes:
- Identificação (`isnull()`, `notnull()`)
- Remoção de registros incompletos (`dropna()`)
- Preenchimento com valores estatísticos (`fillna()`)
- Estratégias mais avançadas de imputação

#### series_temporais.py
Demonstração de manipulação de dados temporais:
- Conversão de colunas para `datetime`
- Indexação por datas
- Resampling, rolling windows e agregações
- Operações comuns em séries temporais financeiras ou de sensores

### avancado/

#### performance_memoria.ipynb
Exemplos de otimização e comparação de desempenho:
- Uso de `apply` vs operações vetorizadas
- Medição de tempo e memória em DataFrames grandes
- Boas práticas para manipulação eficiente de dados

#### pipeline_limpeza.py
Exemplo de pipeline de limpeza profissional:
- Estrutura de funções reutilizáveis
- Tratamento de missing values, normalização e codificação
- Código pronto para projetos e portfólio

---

## 🔑 Habilidades demonstradas

- Criação, indexação e filtragem de **Series** e **DataFrames**
- **Limpeza e transformação** de dados
- Uso de funções como `groupby`, `merge`, `concat` e `apply`
- Análise exploratória com estatísticas descritivas (`info`, `describe`, etc.)
- Manipulação de **datas e séries temporais**
- Boas práticas de performance e construção de pipelines de dados

---

## 🎯 Objetivo desta seção

Expor meu conhecimento prático em **Pandas**, aplicando técnicas de manipulação de dados utilizadas em análises estatísticas, preparação de datasets e construção de pipelines de **Ciência de Dados**, servindo como diferencial em portfólio profissional.
