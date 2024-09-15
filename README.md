![Greenway_TextGray](https://github.com/greenway-FIAP/disruptive_architectures/assets/80494196/8edcfcee-7c71-49c6-b0e4-96966aaf0c69)

### Sobre a solução
O Greenway é uma inovadora plataforma SaaS projetada para auxiliar empresas na gestão de suas operações rumo à sustentabilidade. 
Ao oferecer um acompanhamento minucioso dos processos de produção, nosso objetivo é fomentar o desenvolvimento sustentável, ao mesmo tempo em que impulsionamos benefícios econômicos para as organizações. 
Nossa plataforma, equipada com uma IA Generativa de ponta, tem a capacidade de analisar os dados gerados pelas empresas e fornecer insights valiosos. 
Através de sugestões personalizadas, promovemos modificações e boas práticas que contribuem para o alcance de metas sustentáveis. 
Além disso, monitoramos continuamente o progresso das empresas através da IA, garantindo que estejam no caminho certo para a sustentabilidade. 
Um dos diferenciais do Greenway é a certificação por meio de badges gerados automaticamente pela plataforma, que atestam o comprometimento das empresas com a redução dos impactos no meio ambiente. 
Essa validação não apenas reforça a reputação das empresas no mercado, mas também fortalece o relacionamento com os consumidores finais. 
Ao criar novos canais de comunicação e aumentar a transparência, lealdade, preferência e confiança também são cultivadas junto ao público-alvo.

[Link da apresentação](https://youtu.be/eGrA5A0sdb8)

##

### Integrantes

- 99513 - Rodrigo Batista Freire - Back-end

- 99562 - Kaique Santos de Andrade - Web e Mobile

- 99466 - Marcelo Augusto de Mello Paixão - DevOps e IA

- 97967 - Vinicius Oliveira de Almeida - Mastering Database

- 98644 - Thiago Martins Bezerra - Quality Assurance

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
