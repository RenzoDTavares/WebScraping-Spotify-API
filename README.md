<h1>WebScraping with Spotify API 🎵</h1>

Este repositório utiliza a interação entre APIs usando o pacote BeautifulSoup para obter as 100 melhores músicas de uma data específica no site https://www.billboard.com/charts/hot-100 e criar uma playlist particular no Spotify com as mesmas 100 músicas que o usuário solicitou.

Então, vamos começar. Eu recomendo que você verifique primeiro estes links para entender o que precisaremos para que este código funcione e a documentação que precisamos consultar:

- https://www.youtube.com/watch?v=yAXoOolPvjU&t=1254s -> Este youtuber me ajudou a entender quais informações padrão precisamos obter. Ele usa Node.js, mas se você assistir, entenderá a API do Spotify.
- https://developer.spotify.com/documentation/general/guides/ -> Esta é a documentação da API do Spotify.
- https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user -> Isso facilita tudo ao usar a API do Spotify.
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/ -> Documentação do BeautifulSoup, usamos isso para obter todos os nomes das músicas do site Billboard.

Executando o código, a primeira mensagem no prompt de comando nos pedirá para inserir uma data que o usuário deseja obter as 100 melhores músicas, usando o formato padrão YYYY-MM-DD, porque usaremos requests para obter a página da Billboard com a data exata.

Depois disso, o navegador será iniciado e mostrará uma página do Spotify para autorizar o código a obter as informações, como ID e Secret Key. Algo assim :)

<p align="center">
<img src="https://user-images.githubusercontent.com/43189736/151885934-0082cebf-fe0a-4afd-96a7-4cfdbad28c52.png">
</p>

Então, depois de clicar em aceitar, será enviado para outra página, que configuramos no início seguindo os tutoriais, certo? Copiaremos a URL e a colaremos no prompt de comando para responder à pergunta do código.

![image](https://user-images.githubusercontent.com/43189736/151886853-d4a2aaf9-ad77-4b74-9013-240b32c0dd1e.png)

Um arquivo chamado token.txt foi criado e agora temos a chave de autenticação para proceder com as informações. Depois disso, não precisamos obter a URL novamente, porque temos a chave Token, mas atenção, este token tem um tempo de expiração, então se você obter um erro de autenticação, talvez seja necessário deletar o arquivo e criar um novo como fizemos na primeira vez. Você pode melhorar essa parte do código, talvez tentar eliminar essa parte e obter este Token conforme ele expira, é um grande desafio.

Para finalizar este repositório, podemos verificar no nosso Spotify e veremos a playlist do dia que escolhemos, com as mesmas músicas do site da Billboard.
<p align="center">
<img src="https://user-images.githubusercontent.com/43189736/151887875-1676219c-8d6c-47fb-91fd-12ded09d90d6.png">
</p>

