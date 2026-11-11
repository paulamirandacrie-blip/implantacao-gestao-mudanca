# 02. Impacto da mudança e partes interessadas

Antes de planejar qualquer comunicação, é preciso saber **o que muda e para quem**. O impacto vem da especificação; as
partes interessadas vêm dos perfis e de quem é afetado sem usar o sistema.

## 1. Impacto da mudança (`01_IMPACTO_DA_MUDANCA.md`)

Para cada mudança relevante, uma linha `IMP-nn`:

| Coluna | O que vai |
|---|---|
| Mudança | O que passa a ser diferente, em uma frase, na linguagem de quem trabalha ("o cálculo deixa de ser feito na planilha") |
| Dimensão | Processo, Papel, Ferramenta, Competência, Decisão ou Relação externa |
| Partes afetadas | `PI-` afetadas |
| Intensidade | Alta, Média ou Baixa, pelo critério abaixo |
| Origem | O item da especificação ou do mapeamento que gera a mudança (`MOD-`, `UC-`, `TL-`, `PER-`, `M-`) |

Critério de intensidade:

- **Alta:** muda o que a pessoa decide, o que ela responde ou como é avaliada; ou elimina uma tarefa que dava a ela
  domínio e reconhecimento.
- **Média:** muda a ferramenta e a sequência do trabalho, mas não a responsabilidade.
- **Baixa:** muda a tela ou o formato, sem mudar a tarefa.

Atenção às mudanças de **Papel** e **Decisão**: são as que mais geram resistência e as que a especificação menos
explicita. Pergunte para cada perfil: "o que esta pessoa deixa de fazer? quem passa a ver o trabalho dela?"

## 2. Partes interessadas (`02_PARTES_INTERESSADAS.md`)

Uma linha `PI-SIG` por **grupo**, nunca por pessoa. As fontes, nesta ordem:

1. Cada perfil da especificação (`PER-`) que usa o sistema.
2. As chefias desses perfis, em especial a **chefia intermediária**, que não usa o sistema mas cobra o trabalho.
3. Quem é afetado sem usar o sistema: regulados que passam a enviar dado novo, controle interno, ouvidoria, TI que
   vai sustentar, jurídico que vai defender o uso no processo sancionador.
4. O **patrocinador**: uma função de direção com autoridade sobre as áreas afetadas.

| Coluna | O que vai |
|---|---|
| Parte interessada | Nome do grupo, pela função |
| Perfil | `PER-` da especificação, ou "não usa o sistema" |
| Poder | Alto ou Baixo: consegue acelerar, travar ou desfazer a implantação? |
| Interesse | Alto ou Baixo: o quanto a mudança mexe no trabalho ou nos resultados dele |
| Quadrante | Gerenciar de perto (alto, alto), Manter satisfeito (alto, baixo), Manter informado (baixo, alto), Monitorar (baixo, baixo) |
| Posição | Apoiador, Neutro, Resistente ou Desconhecida |
| Evidência | De onde vem a posição: entrevista do mapeamento, fala registrada, histórico. Sem evidência: `[A CONFIRMAR]` |

## 3. Resistência não é defeito

Resistência é informação: diz o que a pessoa acha que vai perder. As perdas mais comuns em sistemas de fiscalização:

- **Domínio:** "eu era quem sabia fazer a conta".
- **Discricionariedade:** "a máquina vai decidir por mim" (resposta: a camada 7, revisão humana, fica com o fiscal).
- **Exposição:** "agora todo mundo vê meu prazo".
- **Volume:** "100% da população vai gerar alerta demais".
- **Segurança jurídica:** "posso ser questionado por usar um alerta de máquina no auto".

Por isso a regra: **quem resiste é ouvido antes do anúncio geral.** Ouvir antes transforma objeção em ajuste do plano;
ouvir depois transforma objeção em oposição pública.

## 4. Pronto quando

- Todo perfil da especificação aparece como parte interessada, ou há justificativa.
- Chefia intermediária, patrocinador e afetados que não usam o sistema estão na lista.
- Toda parte interessada aparece em pelo menos um impacto.
- Toda posição tem evidência ou `[A CONFIRMAR]`.
