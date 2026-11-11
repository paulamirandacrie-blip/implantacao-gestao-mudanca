# Implantação de sistemas: gestão de mudança e comunicação

Framework para levar um sistema especificado (ou já publicado) **até as pessoas que vão usá-lo**: impacto da mudança,
partes interessadas, diagnóstico ADKAR, plano de gestão de mudança, plano de comunicação, capacitação e suporte,
indicadores de adoção e **as peças de comunicação prontas** (guia rápido, manual com telas, perguntas frequentes,
apresentação para a diretoria, roteiro de vídeo, comunicado aos regulados).

É a terceira parte do curso de processos na administração pública:

1. [mapeamento-processos-sei](https://github.com/RaulAraujoSilva/mapeamento-processos-sei): mapeia o processo, avalia
   o AS-IS, desenha o TO-BE e escolhe o que automatizar.
2. [framework-especificacao-sistemas](https://github.com/RaulAraujoSilva/framework-especificacao-sistemas): do TO-BE à
   especificação completa do sistema.
3. **Este repositório:** da especificação ao sistema adotado. Um sistema pronto não é um sistema usado.

## Como usar

O aluno traz **o seu processo e o seu sistema** (insumos do mapeamento, especificação, endereço do sistema publicado) e
indica este repositório à IA dele como referência de método e de saída. O trabalho acontece num **projeto próprio**:

```bash
python scripts/iniciar_projeto.py ../meu-sistema-implantacao --sistema "Nome do sistema" --orgao SIGLA
```

```bash
python scripts/conferir_implantacao.py --projeto ../meu-sistema-implantacao
```

Se o projeto do sistema já existe (um repositório com `insumos/` e `especificacao/`), crie a implantação **dentro
dele**: `python scripts/iniciar_projeto.py ../meu-sistema --sistema "..." --orgao SIGLA --dentro`. A pasta
`implantacao/` é acrescentada sem tocar no resto.

| Para quem | Comece por |
|---|---|
| A **IA** do aluno (Claude Code, Codex ou equivalente) | [`AGENTS.md`](AGENTS.md) |
| Quem vai **planejar a implantação** do próprio sistema | [Visão geral](docs/metodologia/00_VISAO_GERAL.md) e [roteiro](docs/metodologia/ROTEIRO_IMPLANTACAO.md) |
| Quem está **em aula**, com tempo marcado | [Modo aula](docs/metodologia/MODO_AULA.md) |
| Quem quer **ver o resultado** pronto | [`exemplo/reajusta/`](exemplo/reajusta/LEIA-ME.md) |

## Metodologia

| Capítulo | Assunto |
|---|---|
| [00 Visão geral](docs/metodologia/00_VISAO_GERAL.md) | Por que sistemas bons falham na implantação; fluxo; tipos de etapa; o que não se negocia |
| [01 Insumos](docs/metodologia/01_INSUMOS.md) | O que trazer do mapeamento, da especificação e do sistema publicado |
| [02 Impacto e partes interessadas](docs/metodologia/02_IMPACTO_E_PARTES_INTERESSADAS.md) | O que muda para quem; mapa poder × interesse; posição e evidência |
| [03 Diagnóstico ADKAR](docs/metodologia/03_DIAGNOSTICO_ADKAR.md) | Consciência, desejo, conhecimento, habilidade e reforço; o ponto de bloqueio |
| [04 Plano de gestão de mudança](docs/metodologia/04_PLANO_DE_MUDANCA.md) | Patrocínio, resistências, ações por elemento ADKAR, capacitação, suporte, indicadores de adoção |
| [05 Plano e material de comunicação](docs/metodologia/05_COMUNICACAO.md) | Público, mensagem, canal, momento, responsável; as peças; IA, acessibilidade e transparência |
| [06 Uso do caso resolvido](docs/metodologia/06_USO_DO_EXEMPLO.md) | O que aproveitar do exemplo e o que nunca copiar |
| [Roteiro](docs/metodologia/ROTEIRO_IMPLANTACAO.md) | Etapas G0 a G4 com ação, aceite, artefato e as PARADAs |
| [Modo aula](docs/metodologia/MODO_AULA.md) | Como rodar o roteiro em 30 a 40 minutos, com subagentes em paralelo |

## Mapa do repositório

| Pasta | Conteúdo |
|---|---|
| [`docs/metodologia/`](docs/metodologia/) | O método |
| [`modelos/projeto/implantacao/`](modelos/projeto/implantacao/) | Os 7 documentos do plano e as 6 peças de comunicação, com marcadores `{{...}}` e orientação de preenchimento |
| [`scripts/`](scripts/) | `iniciar_projeto.py` e `conferir_implantacao.py` (rastreabilidade, ADKAR, escuta antes do anúncio, aviso de IA, isolamento do exemplo) |
| [`exemplo/reajusta/`](exemplo/reajusta/LEIA-ME.md) | Caso resolvido: a implantação do Reajusta, o sistema especificado na parte 2 do curso. Só referência de forma |
| [`tests/`](tests/) | Testes do framework |

## Instalação

Python 3.10 ou mais novo. Os scripts usam só a biblioteca padrão; os testes usam `pytest`.

```bash
pip install -r requirements.txt
```

```bash
python -m pytest tests
```

## Regras que não se negociam

- **Nenhum impacto sem origem.** Cada mudança aponta o módulo, o caso de uso, a tela ou a melhoria de onde veio.
- **Nenhuma ação sem alvo.** Cada ação de mudança diz a quem se dirige e que elemento do ADKAR ela trata.
- **Quem resiste é ouvido antes do anúncio geral.** O conferidor barra o plano que anuncia antes de escutar.
- **Sustentação antes da entrada em uso.** Dono da solução, pessoa de reserva e data para desligar o método antigo.
- **Toda peça tem dono no plano.** Cada peça de comunicação aponta a linha do plano de comunicação que a pede.
- **Transparência sobre IA.** Voz, imagem ou avatar sintéticos levam aviso no início da peça.
- **Acessível ou não está pronto.** Vídeo com legenda e transcrição; documentos com texto, não só imagem.
- **Função, não nome.** Nenhum nome de pessoa no plano; use a função (chefe da unidade, fiscal, analista).
- **O seu caso, não o do exemplo.** O conferidor barra termos do caso resolvido.
- **Toda saída da IA é verificada por uma pessoa** antes de chegar a quem vai usar o sistema.
