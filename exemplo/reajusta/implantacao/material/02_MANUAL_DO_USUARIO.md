# Manual do usuário: Reajusta (analistas e gestor do cadastro)

| Item | Conteúdo |
|---|---|
| Peça | PC-02 |
| Plano | CM-07 |
| Público | PI-ANA, PI-GCA |
| Versão | 0.1 (rascunho; capturas pendentes até a publicação da homologação) |
| Revisado por | Equipe do projeto |

## 1. O que é o sistema

O Reajusta recebe o pleito da concessionária no layout, valida na entrada, recalcula o índice e o total com as regras
do contrato e gera a memória de cálculo e a minuta do parecer técnico. **O parecer continua sendo seu:** você confere,
ajusta e assina.

## 2. Acesso

Endereço do ambiente de homologação, informado na oficina (CAP-01). O perfil de acesso é pedido à TI.

## 3. Conferir o resultado da validação de um pleito (UC-02)

1. Abra o ciclo no painel (TL-01) e entre no detalhe (TL-02).
2. Abra **Resultado da validação** (TL-04). Cada regra, de V01 a V12, aparece como ok, aviso ou erro, com o número que
   falhou e o que fazer.

   ![Tela de resultado da validação, com as regras V01 a V12 e a situação de cada uma](telas/TL-04_resultado_validacao.png)

3. Se houver erro, confirme a devolução com pendências (UC-04). O ofício de complementação sai por modelo.

## 4. Conferir a memória de cálculo (UC-05)

1. No detalhe do ciclo, abra **Memória de cálculo** (TL-05). Cada número mostra a sua origem: série, mês e fonte.

   ![Tela de memória de cálculo, com os termos ponderados, o índice e a origem de cada número](telas/TL-05_memoria_calculo.png)

2. Na operação assistida, compare com a sua conta pelo método atual. Divergência sem causa vai para a chefia
   (IND-AD-03).

## 5. Cadastrar uma versão contratual (UC-06, gestor do cadastro)

1. Abra o contrato (TL-06) e crie a versão a partir do ato (termo aditivo ou deliberação).
2. Para cada parâmetro, cole o trecho literal da fonte. A versão nova guarda só o que mudou.

## 6. Mensagens e o que fazer

| Mensagem | O que significa | O que fazer |
|---|---|---|
| Erro em V01 a V12 | O pleito não atende a uma regra de entrada | Confirmar a devolução com pendências |
| Aviso de série | Uma série da fonte pública não confere com a do pleito | Ver a origem na memória e registrar a causa |

## 7. Onde tirar dúvida

Multiplicador da CAPET (SUP-02); plantão diário (SUP-03); erro do sistema, chamado à equipe (SUP-04).
