# Implantação do sistema Reajusta (AGENERSA)

O Reajusta leva o reajuste tarifário anual do protocolo ao arquivamento com cálculo conferido por máquina, prazos com
dono e minutas assistidas. Para quem trabalha no processo, muda quem faz a conta, quem vê o prazo e como as peças
nascem; a decisão de homologar continua com o Conselho-Diretor.

Plano feito pelo método do repositório implantacao-gestao-mudanca, a terceira parte do curso (mapeamento →
especificação → implantação).

## Sistema e datas

| Item | Conteúdo |
|---|---|
| Sistema | Reajusta |
| Endereço de validação | Ainda não publicado (ambiente de homologação das releases R1 e R2) |
| Patrocinador (função) | Presidência do Conselho-Diretor (DEC-01) |
| Dono do processo (função) | Chefia da CAPET |
| S0, entrada em uso | Início da operação assistida: o primeiro pleito de novembro depois do aceite da R2 (especificação, `14_OPERACAO.md` §8, etapa 3) |
| Operação em paralelo | Durante todo o ciclo do piloto: a CAPET refaz a conta pelo método atual |

## Insumos usados

| Insumo | Arquivo (no framework-especificacao-sistemas) |
|---|---|
| Escopo, módulos e perfis | `exemplo/reajusta/especificacao/01_VISAO_ESCOPO.md` |
| Perfis e jornadas | `exemplo/reajusta/especificacao/02_PERFIS_E_JORNADAS.md` |
| Releases | `exemplo/reajusta/especificacao/13_BACKLOG.md` §3 |
| Plano de implantação no piloto e medição | `exemplo/reajusta/especificacao/14_OPERACAO.md` §8 e §9 |

## Documentos

| Documento | Situação |
|---|---|
| [01 Impacto da mudança](01_IMPACTO_DA_MUDANCA.md) | conferido |
| [02 Partes interessadas](02_PARTES_INTERESSADAS.md) | conferido; posições a confirmar |
| [03 Diagnóstico ADKAR](03_DIAGNOSTICO_ADKAR.md) | conferido; notas a confirmar |
| [04 Plano de gestão de mudança](04_PLANO_GESTAO_MUDANCA.md) | conferido |
| [05 Plano de comunicação](05_PLANO_COMUNICACAO.md) | conferido |
| [06 Capacitação e suporte](06_CAPACITACAO_E_SUPORTE.md) | conferido |
| [07 Indicadores de adoção](07_INDICADORES_DE_ADOCAO.md) | conferido |
| [Peças de comunicação](material/) | rascunho, antes da PARADA G3 |

## Decisões pendentes

| ID | Decisão | Dono (função) | Padrão provisório |
|---|---|---|---|
| DEC-01 | Quem patrocina: a Presidência ou um conselheiro designado | Conselho-Diretor | Presidência do Conselho-Diretor |
| DEC-02 | Se a validação prévia passa a ser obrigatória para as concessionárias e por que ato | Conselho-Diretor, Procuradoria | Facultativa no piloto |
| DEC-03 | Se haverá narração humana nos vídeos ou voz sintética com aviso | Assessoria de comunicação | Voz sintética, com aviso no início |
