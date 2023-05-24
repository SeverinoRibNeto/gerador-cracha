# Projeto de Geração de Crachás

Esse projeto surgiu com o intuito de facilitar a geração de crachás de uma escola estadual e assim automatizando esse processo de forma simples.
Abaixo você encontrará informações sobre o projeto, sua estrutura de código e como utilizá-lo.

## Descrição

O projeto de Geração de Crachás consiste em uma aplicação que automatiza o processo de geração de crachás para estudantes. Ele lê informações de um arquivo CSV contendo os dados dos estudantes, como matrícula, nome, fator RH, curso, data de nascimento e número SUS. Com base nessas informações, o projeto cria crachás personalizados para cada estudante, permitindo que sejam adicionadas imagens dos estudantes, se disponíveis. Os crachás gerados são salvos em uma pasta de saída especificada pelo usuário.

## Requisitos

Antes de executar o projeto, verifique se você possui os seguintes requisitos:

    Python 3.9.7 em um ambiente virtual(venv)

Você pode instalar os pacotes Python utilizando o pip. Execute o seguinte comando para instalar os pacotes necessários:
```
pip install -r requeriments.txt
```

## Estrutura do Projeto

O projeto possui a seguinte estrutura de código:

    estudante.py: Define a classe Estudante que representa as informações de um estudante.
    cracha.py: Define a classe Cracha responsável pela geração dos crachás.
    gui.py: Contém a classe GUI que implementa a interface gráfica da aplicação.
    app.py: Arquivo principal do projeto, contendo a criação da classe CrachaController que controla a lógica do projeto e interage com a GUI.
    config.txt: Arquivo de configuração que armazena as configurações da aplicação. Ele é criado automaticamente sem valores definidos.
    template.csv: Arquivo CSV de exemplo contendo os campos necessários para a geração dos crachás. Criado quando o botão de template é acidonado.
    Outros arquivos e diretórios: O projeto pode utilizar outras imagens e arquivos CSV como entrada, conforme especificado pelo usuário.

## Uso

Siga as instruções abaixo para utilizar o projeto:

    Certifique-se de ter instalado os requisitos mencionados anteriormente.
    Execute o arquivo app.py para iniciar a aplicação.
    A interface gráfica será exibida, permitindo que você configure as opções de entrada, como o caminho para o arquivo CSV com os dados dos estudantes, o diretório contendo as imagens dos estudantes (opcional) e o diretório de saída para os crachás gerados.
    Após configurar as opções de entrada, clique no botão "Salvar" para salvar as configurações.
    Você pode carregar as configurações salvas clicando no botão "Carregar".
    Para gerar os crachás, clique no botão "Gerar". Os crachás serão criados com base nos dados do arquivo CSV e salvos no diretório de saída especificado.
    Durante o processo de geração, um contador será exibido na interface gráfica para acompanhar o progresso.
    Se desejar, você pode baixar um arquivo CSV de exemplo clicando no botão "Download".

Certifique-se de que o arquivo CSV de entrada esteja no formato correto, contendo os campos necessários conforme especificado no cabeçalho do arquivo. Utilize o arquivo template.csv como referência.

## Observações

    As imagens de modelo de crachá, imagens de estudantes e a biblioteca qrcode são necessárias para o funcionamento correto do projeto. Verifique se esses arquivos estão presentes nos caminhos especificados no código.
    O projeto vai continuar em desenvolvimento e contribuições serão bem vindas
    
## Contribuição no Projeto

Se você está interessado em contribuir para o projeto de Geração de Crachás, ficaremos felizes em receber sua colaboração. Contribuições podem incluir correção de bugs, implementação de novos recursos, melhorias de desempenho, documentação e muito mais. Aqui estão algumas informações sobre como você pode contribuir:
### 1. Fork do Repositório

O primeiro passo para contribuir é fazer um fork do repositório do projeto. Isso criará uma cópia do projeto em sua própria conta do GitHub.
### 2. Clone do Repositório

Após fazer o fork, clone o repositório para sua máquina local. Isso permitirá que você faça alterações no código.
```
git clone https://github.com/SeverinoRibNeto/gerador-cracha.git
```

### 3. Faça as Alterações

Agora você pode fazer as alterações no código do projeto de acordo com a sua contribuição. Você pode adicionar novos recursos, corrigir bugs, melhorar a estrutura do código, etc.

### 4. Teste as Alterações

Antes de enviar suas alterações, é importante testá-las para garantir que tudo funcione conforme o esperado. Execute os testes existentes ou crie novos testes, se necessário, para verificar a integridade das alterações.

### 5. Commit e Push das Alterações

Após testar as alterações, faça um commit das suas alterações e faça um push para o seu repositório no GitHub.

```
git add .
git commit -m "Descrição das alterações"
git push origin master
```
Certifique-se de substituir "Descrição das alterações" por uma breve descrição das alterações que você fez.

### 6. Crie um Pull Request

Depois de ter feito o push das suas alterações para o seu repositório no GitHub, você pode criar um Pull Request (PR). Isso permitirá que você solicite a inclusão das suas alterações no repositório principal do projeto.

No GitHub, vá para a página do seu repositório e clique no botão "New Pull Request". Siga as instruções fornecidas para criar o PR. Certifique-se de fornecer uma descrição clara das suas alterações e do motivo pelo qual elas são relevantes para o projeto.

### 7. Discussão e Revisão

Após criar o PR, os mantenedores do projeto irão revisar suas alterações. Pode ser necessário discutir detalhes, fazer ajustes ou solicitar mais informações. Esteja aberto a feedback e contribua ativamente durante o processo de revisão.

### 8. Aceitação e Mesclagem

Se suas alterações forem aprovadas e consideradas adequadas para o projeto, elas serão mescladas ao repositório principal. Parabéns, você contribuiu com sucesso para o projeto!
Orientações Adicionais

    Certifique-se de seguir as diretrizes de contribuição do projeto, se houver. Verifique se existem padrões de codificação, convenções de nomenclatura ou outros requisitos específicos.
    Se estiver trabalhando em uma nova funcionalidade, discuta-a antecipadamente com os mantenedores do projeto para obter feedback e orientações.
    Ao fazer alterações no código, documente-as adequadamente para facilitar a compreensão e manutenção futura.
    Se estiver corrigindo um bug, forneça informações detalhadas sobre o problema encontrado e como ele foi resolvido.
    Contribuições de todos os níveis de habilidade são bem-vindas. Não hesite em contribuir, mesmo se você for novo na programação ou no projeto em si.

Agradecemos antecipadamente sua contribuição para o projeto de Geração de Crachás. Sua participação pode ajudar a melhorar o projeto e beneficiar a comunidade de usuários. Se você tiver alguma dúvida adicional, entre em contato conosco.
