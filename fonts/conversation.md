Projeto de web scraping, analise dos dados e previsão com machine learning 07/03/2023 às 13:43
Descrição do Projeto:
Estou iniciando um projeto onde quero buscar as informações das partidas d ojogo Double da Blaze, salvar em uma banco de dados, analisar os dados em tempo real, entender os padrões atuais e indicar qual cor deve ser jogada com base nos padrões analisados.

Como os padrões mudam a todo momento, o código deve ser capaz de analisar em tempo real.

Obs: Não precisa de uma interface gráfica bonita.

---

1º

Diórgenes P.

10/03/2023 às 09:21
Olá Jeferson,

Então, basicamente o projeto seria pegar os dados do site, salvar em um banco de dados, analisar os dados em tempo real, identificar os padrões e "prever" a próxima jogada com base nos padrões identificados (utilizando algoritmos de ML).

Uma coisa que não mencionei no descritivo do projeto é que preciso que esse programa rode em uma VPS para que fique analisando 24h por dia.

A parte da interface gráfica fica a teu critério de como acha melhor a apresentação, mas pode ser o mais simples mesmo ou até mesmo enviar uma mensagem para o telegram (nesse ponto gostaria de uma opinião sua).

---

2º
Diórgenes P.

10/03/2023 às 11:49
Sobre as dúvidas:

- Os dados da partida (cor, número, data, horário);
- Eu teria preferencia por SQL, mas se você achar que outro tipo de DB seja melhor podemos conversar;
- No telegram eu gostaria de receber a cor a ser jogada na próxima partida, algo tipo assim: Jogar no preto após o vermelho número X (cor e número da última partida para ter certeza de qual momento entrar)
- Dos dados coletados, como os padrões mudam constantemente podemos continuar coletando os atuais. Não sei se para treinar o modelo com ML a gnt precisaria pegar dados antigos fazer este treino. Tem um site que armazena o histórico dos jogos da blaze.


-- repos

- https://github.com/victorratts13/radar-sport-api
- https://github.com/viniciusgdr/Blaze
- https://github.com/elizandrodantas/bot-blaze-telegram

---


Diórgenes P.

10/03/2023 às 13:41
Site com os históricos:
https://www.historicosblaze.com/br/blaze/doubles


Diórgenes P.

10/03/2023 às 13:47
é double da Blaze. Ele funciona assim:

- A roleta gira 2 vezes por minuto. a Cada 1 ou duas horas a roleta vai girar 1 vez no periodo de um minuto para ajustar o tempo.

- Você tem 3 opções de aposta: apostar no Branco, vermelho ou preto.
-- O Branco sai com menos frequência, mas paga 14x a aposta.
-- O preto e o vermelho saem o tempo todo e pagam 2x a aposta.
-- Do 1 ao 7 são da cor vermelha. Do 8 ao 14 são da cor preta.

Basicamente é isso.

## todo 

- [ ] extrair site: https://www.historicosblaze.com/br/blaze/doubles
    - login
    - dowload do excel ou extrair os dados manualmente


---

Olá Diórgenes,

Desculpe pela demora para a resposta, vamos la:

pode ser dividído em várias etapas:

1º o telegram, por hora não possui problemas, mais dependendo do input do modelo 

2º - crawling/scrapping: o site que você me enviou tem informações interessantes, até o excel para baixar, porem dependendo da necessidade, é possível é necessário mais dados, e jogar no SQL, tem bancos otimizados para isso, porem por hora, podemos continuar com MySQL, 
    - tempo médio: 3 a 5 dias, preço $400 (negociável)

3º sobre o modelo, percebi que:
    - vamos precisar de uma base de dados grande, e correlação entre os dados, (cor, data, dia)
    - È possível com machine learning, a dificuldade consitirá: 
        - limpeza de dados, e pegar o tipo de dado certo (correlação)
        - acuracia de dados, (falso positívos, interferências, ex: dados errados, que levam resultados errados)
        - tempo e treino de dados
    - se o machine learning ainda sim não ser safistatório, podemos tentar o Deep learning, que consiste treinar o modelo x vezes até o dados ajustado, como mencionado anteriomente podendo ser necessários recursos pesados e modelo alto de dados (Ex: 50g)
    - sobre o prazo percebi que, não tem como mensurar ele, pelos seguintes motivos:
        - é mais por tentativa e erro,
        - tempo de treino
    - sobre o preço, vai variar de acordo se for machine learning ou deep learning (de $800 até $4500) ou podendo fazer via mensalidade comos serviço, alem do desenvolvimento do mesmo