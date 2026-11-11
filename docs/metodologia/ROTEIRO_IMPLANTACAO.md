# Roteiro: do sistema especificado ao sistema adotado

Passo a passo para a IA do aluno (e para o aluno). Cada etapa tem ação, comando, aceite e o artefato no **projeto do
aluno**. **PARADA** é ponto em que a IA para e espera a pessoa indicada. Antes de cada etapa, leia o capítulo citado.
Com tempo marcado, siga também o [modo aula](MODO_AULA.md).

Nos comandos, `<projeto>` é a pasta do projeto do aluno e `<impl>` é `<projeto>/implantacao`.

## Etapa G0: preparação

Capítulos: [00](00_VISAO_GERAL.md), [01](01_INSUMOS.md) e [06](06_USO_DO_EXEMPLO.md).

| # | Ação | Comando | Aceite | Artefato |
|---|---|---|---|---|
| G0.1 | Criar a implantação a partir dos modelos | `python scripts/iniciar_projeto.py <projeto> --sistema "..." --orgao SIGLA` (acrescente `--dentro` se o projeto do sistema já existe) | Pasta `implantacao/` criada | `<impl>/` |
| G0.2 | Localizar os insumos | ler `insumos/` e `especificacao/` do projeto | Escopo, perfis, telas e linha de base localizados; o que falta virou `DEC` | `<impl>/README.md` §Insumos |
| G0.3 | Registrar sistema, patrocinador e data prevista | — | `S0` definido (ou `DEC`) | `<impl>/README.md` |

## Etapa G1: impacto, partes interessadas e ADKAR

Capítulos: [02](02_IMPACTO_E_PARTES_INTERESSADAS.md) e [03](03_DIAGNOSTICO_ADKAR.md).

| # | Ação | Aceite | Artefato |
|---|---|---|---|
| G1.1 | Levantar os impactos a partir dos módulos, casos de uso e perfis | Todo `IMP` com origem (G04); toda `PI` em algum impacto | `01_IMPACTO_DA_MUDANCA.md` |
| G1.2 | Listar as partes interessadas, com poder, interesse, quadrante, posição e evidência | Perfis, chefia intermediária, patrocinador e afetados que não usam o sistema presentes | `02_PARTES_INTERESSADAS.md` |
| G1.3 | Diagnóstico ADKAR por parte interessada | Toda `PI` com linha (G05); ponto de bloqueio confere (G05) | `03_DIAGNOSTICO_ADKAR.md` |
| G1.4 | Conferir | `python scripts/conferir_implantacao.py --projeto <projeto>` sem erro nos documentos 01 a 03 | — |

**PARADA G1 (aluno e quem conhece o órgão):** conferir posições, perdas percebidas e notas. O que for hipótese segue
marcado `[A CONFIRMAR]`.

## Etapa G2: plano de mudança e plano de comunicação

Capítulos: [04](04_PLANO_DE_MUDANCA.md) e [05](05_COMUNICACAO.md).

| # | Ação | Aceite | Artefato |
|---|---|---|---|
| G2.1 | Patrocínio, coalizão, resistências e ações | Todo ponto de bloqueio com ação no elemento (G06) | `04_PLANO_GESTAO_MUDANCA.md` |
| G2.2 | Plano de comunicação | Toda Resistente com Escuta antes do Anúncio (G07); toda `PI` comunicada (G08) | `05_PLANO_COMUNICACAO.md` |
| G2.3 | Capacitação e suporte | Todo perfil que usa o sistema com `CAP` e `SUP` | `06_CAPACITACAO_E_SUPORTE.md` |
| G2.4 | Indicadores de adoção | Ao menos um de uso e um de resultado; metas "(proposto)" | `07_INDICADORES_DE_ADOCAO.md` |
| G2.5 | Conferir | conferidor sem erro | — |

## Etapa G3: peças de comunicação

Capítulo: [05](05_COMUNICACAO.md) §2 a §4.

| # | Ação | Aceite | Artefato |
|---|---|---|---|
| G3.1 | Capturar as telas do sistema publicado, com dados fictícios | Uma captura por tela usada nas peças | `<impl>/material/telas/` |
| G3.2 | Escrever as peças pedidas pelo plano | Cada peça com cabeçalho `PC`/`CM` (G09); vídeo com aviso de IA se houver voz sintética (G10) | `<impl>/material/` |
| G3.3 | Conferir | conferidor sem erro | — |

**PARADA G3 (patrocinador e um usuário real):** o patrocinador aprova a apresentação e o anúncio; um usuário de fora
da equipe faz a tarefa principal só com o guia rápido. A IA prepara e para; quem envia é o aluno.

## Etapa G4: entrada em uso, suporte e medição

| # | Ação | Quem | Aceite |
|---|---|---|---|
| G4.1 | Executar as comunicações e capacitações no calendário | aluno e responsáveis | Cada `CM` com data real registrada no README |
| G4.2 | Plantão de dúvidas de S0 a S+2 | suporte | Dúvidas registradas e incorporadas às perguntas frequentes |
| G4.3 | Medir os indicadores de adoção em S+2 e S+6 | dono do processo | Tabela "antes e depois" no `07` |
| G4.4 | Decidir seguir, ajustar ou parar | patrocinador | Decisão registrada como `DEC`, com os números |
