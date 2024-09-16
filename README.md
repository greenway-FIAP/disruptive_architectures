![Greenway_TextGray](https://github.com/greenway-FIAP/csharp_api/assets/80494196/7b3ee4f3-373d-4aed-b459-d870cc122b77)

## Índice
- [Sobre a Solução](#sobre-a-solução)
- [Recursos da Plataforma](#recursos-da-plataforma)
  - [Análise de Dados](#análise-de-dados)
  - [Sugestões Personalizadas](#sugestões-personalizadas)
  - [Monitoramento Contínuo](#monitoramento-contínuo)
  - [Certificações](#certificações)
- [Integrantes](#integrantes)

## Sobre a Solução

O **Greenway** é uma inovadora plataforma SaaS projetada para auxiliar empresas na gestão de suas operações rumo à sustentabilidade. Através de um acompanhamento detalhado dos processos de produção, a plataforma tem como objetivo promover o desenvolvimento sustentável e, ao mesmo tempo, gerar benefícios econômicos para as organizações.

### Certificações

As empresas que utilizam a plataforma recebem **certificações automáticas** em formato de badges. Essas certificações atestam o comprometimento da empresa com práticas sustentáveis, fortalecendo sua reputação no mercado e sua relação com os consumidores.

[Link da Apresentação](https://youtu.be/eGrA5A0sdb8)

## Integrantes

- **RM99513** - Rodrigo Batista Freire - Java Advanced
- **RM99562** - Kaique Santos de Andrade - Mobile Development
- **RM99466** - Marcelo Augusto de Mello Paixão - Development with .NET, DevOps & Cloud Computing e Quality Assurance
- **RM97967** - Vinicius Oliveira de Almeida - Mastering Database
- **RM98644** - Thiago Martins Bezerra - Disruptive Architectures (IA)

#

## Construir e Enviar Imagens Docker

### Imagem Docker da API
- Nome da Imagem: marceloamellopaixao/greenway-cv_api:latest
- URL do Dockerhub: greenway-cv_api

```bash
  docker build -t marceloamellopaixao/greenway-cv_api:latest .
  docker login
  docker push marceloamellopaixao/greenway-cv_api:latest
```

## Executando a Aplicação API Localmente

### 1º - Baixe a imagem mais recente da API:

```bash
  docker pull marceloamellopaixao/greenway-cv_api:latest
```

### 2º - Execute o contêiner da API:

```bash
  docker run -d -p 5000:5000 marceloamellopaixao/greenway-cv_api
```

## Executando a Aplicação Front-End Localmente

### 1º - Faça o git clone do projeto front-end:
```bash
git clone https://github.com/greenway-FIAP/disruptive_architectures.git
```

### 2º - Navegue até o diretório do projeto front-end:

```bash
  cd caminho/para/projeto-front-end
```

### 3º - Instale as dependências:

```bash
  npm i
```

### 4º - Inicie o servidor de desenvolvimento:

```bash
  npm start dev
```

### 5º - Abra no seu navegador a url: 

```bash
  localhost:5173
```

#

## Usando a Aplicação

### 1º - Abra a aplicação front-end no seu navegador.

### 2º - Faça o upload de uma imagem contendo um dos seguintes tipos:
  - Garrafas Térmicas
  - Produtos de Mercado

### 3º - A aplicação processará a imagem e categorizará o tipo.
