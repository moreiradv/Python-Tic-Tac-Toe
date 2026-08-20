Fala, pessoal! Blz? 👋

Resolvi tirar uma ideia do papel pra treinar minha lógica em Python e acabei recriando aquele clássico Jogo da Velha que todo mundo jogava no fim do caderno da escola.

Foi um projetinho bem divertido de fazer e me ajudou bastante a fixar conceitos como matrizes, condicionais e como controlar o fluxo de um jogo no terminal sem deixar o código um caos.

💻 O que tem de legal nesse código?
Montei a lógica de um jeito bem direto:

Matriz 3x3: Usei listas dentro de listas pra criar a grade do tabuleiro.

Checagem de vitória: A cada rodada o código dá uma varrida pra ver se alguém alinhou 3 símbolos (seja em linha, coluna ou diagonal).

Alternância de turnos: Ele faz a troca automática entre o jogador X e o jogador O.

Deu velha? Se bater 9 jogadas e ninguém ganhar, ele avisa que empatou e encerra numa boa.

🕹️ Como funciona na prática?
Quando você roda o jogo, ele mostra o tabuleiro com coordenadas que vão de 0 a 2:

Plaintext

         0   1   2
      0 [ ] [ ] [ ]
      1 [ ] [ ] [ ]
      2 [ ] [ ] [ ]
Aí é só escolher a linha e a coluna onde você quer jogar. Por exemplo: se quiser colocar no meio certinho, escolhe linha 1 e coluna 1.

🎯 Próximos ajustes (o que quero melhorar)
Como nenhum código nasce perfeito, já tô de olho em algumas coisas pra atualizar em breve:

Travar o programa pra não quebrar se o usuário digitar uma letra sem querer em vez de número.

Impedir que alguém jogue em um quadrado que já tá ocupado (se vacilar, hoje dá pra sobrescrever a jogada do outro haha).

Criar um bot simples pra dá pra jogar sozinho contra o PC.

Se quiser rodar aí na sua máquina, é só clonar o repositório e dar um python nome_do_arquivo.py.

Se tiver qualquer dica pra me ajudar a melhorar o código, pode mandar que vou adorar trocar uma ideia! 🚀

**Funcionamento de validação, empate e vitória.**

<img width="319" height="196" alt="image" src="https://github.com/user-attachments/assets/f5711724-d51a-4be6-a321-6cf59e1c9390" /> <img width="319" height="196" alt="image" src="https://github.com/user-attachments/assets/8b10c97a-fa34-4a67-8265-aefbed3520a4" />

