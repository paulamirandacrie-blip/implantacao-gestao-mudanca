# 05. Plano e material de comunicação

O plano de comunicação diz **quem fica sabendo do quê, por qual canal, quando e por quem**. O material de
comunicação são as peças prontas que o plano pede. A IA faz as duas coisas; uma pessoa revisa antes de qualquer envio.

## 1. Plano de comunicação (`05_PLANO_COMUNICACAO.md`)

Uma linha `CM-nn` por comunicação:

| Coluna | O que vai |
|---|---|
| Público | `PI-` (uma ou mais) ou "Todos" |
| Tipo | **Escuta**, **Anúncio**, **Capacitação**, **Orientação** ou **Reforço** |
| Objetivo | O elemento ADKAR que a comunicação move |
| Mensagem-chave | Uma frase, na linguagem do público |
| Canal | Reunião presencial, reunião on-line, e-mail, intranet, ofício, vídeo, sistema |
| Momento | `S-n`, `S0`, `S+n` |
| Responsável | Função. O patrocinador assina ao menos o primeiro **Anúncio** |
| Peça | `PC-` que a comunicação usa, ou "—" |

Regras:

- **Escuta antes do Anúncio.** Toda `PI-` Resistente tem uma **Escuta** em momento anterior ao primeiro **Anúncio**
  (o conferidor verifica). A escuta é conversa, não apresentação: o objetivo é ajustar o plano.
- **Canal pelo quadrante.** Gerenciar de perto: conversa direta. Manter satisfeito: reunião curta e resumo de uma
  página. Manter informado: canais coletivos e peças. Monitorar: intranet e comunicado.
- **Sequência:** escuta (S-4 a S-3) → anúncio pelo patrocinador (S-2) → orientação e capacitação (S-1 a S0) → reforço
  (S+1 em diante).
- **Regulados à parte.** Se o sistema muda o que o regulado envia, a comunicação a ele é formal (ofício ou ato), com
  antecedência e com o contrato de dados.

## 2. As peças (`implantacao/material/`)

| Peça | Público típico | Pronto quando |
|---|---|---|
| Guia rápido (1 página) | Quem opera o sistema | Uma pessoa de fora da equipe faz a tarefa principal só com o guia |
| Manual do usuário com telas | Quem opera e o multiplicador | Cada tarefa do perfil com passo a passo e tela real |
| Perguntas frequentes | Todos que usam | Responde as dúvidas da escuta e do plantão |
| Apresentação para a diretoria (5 slides) | Patrocinador, diretoria | Problema, o que muda, o que continua humano, riscos, indicadores |
| Roteiro de vídeo (2 min) | Quem opera | Uma tarefa por vídeo, com as telas; aviso de IA se a narração for sintética |
| Comunicado aos regulados | Regulados | O que muda para eles, o que enviar, a partir de quando, onde tirar dúvida |

Cada peça começa pela tabela de cabeçalho do modelo, com `PC-`, a `CM-` que a pede, o público e a versão.

## 3. Peças a partir do próprio sistema

**Manual e vídeos: use o kit-manual-usuario da aula 7.** Se o projeto já tem o kit (roteiros YAML por tarefa, matriz
perfil × tarefa, manual em PDF por perfil e vídeos narrados com legenda), as peças "manual" e "vídeo" do plano
**apontam para as saídas do kit**, sem reescrever: o cabeçalho da peça cita o caminho do manual ou do roteiro, e a
matriz do kit serve de base para a capacitação (`CAP-`). Este framework cuida do que o kit não faz: **por que** e
**para quem** comunicar, em que ordem, e as peças fora do sistema (anúncio, apresentação para a diretoria, comunicado
aos regulados, perguntas frequentes nascidas das resistências).

Sem o kit, a IA consegue gerar o material a partir do repositório e do sistema publicado:

- **Manual e guia:** ler `especificacao/11_TELAS.md` e os casos de uso; navegar no ambiente de validação; capturar as
  telas (com dados fictícios); escrever o passo a passo por tarefa.
- **Vídeo:** roteiro cena a cena com a tela de cada passo; gravar a navegação; narração e legenda. Se a narração for
  voz sintética, o aviso é a primeira coisa do vídeo.
- **Apresentação:** a partir do 01 (problema e metas) e dos indicadores da linha de base.

## 4. IA, transparência e acessibilidade

- **Aviso de IA** no início de toda peça com voz, imagem ou avatar sintéticos (o conferidor verifica no roteiro de
  vídeo). Texto revisado por uma pessoa não precisa de aviso.
- **Acessibilidade:** legenda e transcrição em todo vídeo; texto alternativo em toda imagem; documento com texto
  selecionável, não imagem de texto; contraste e fonte legíveis.
- **Dado pessoal:** captura de tela só com dados fictícios ou anonimizados.

## 5. Pronto quando

- Toda `PI-` aparece em pelo menos uma comunicação.
- Toda Resistente tem Escuta antes do primeiro Anúncio.
- Toda peça aponta a `CM-` que a pede, e toda `CM-` com peça aponta uma peça que existe.
- As peças passaram pela PARADA G3: patrocinador e um usuário real.
