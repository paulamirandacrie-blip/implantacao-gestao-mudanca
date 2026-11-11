# 01. Insumos

O plano de implantação deriva do que já foi feito nas partes 1 e 2 do curso. Quanto mais disso estiver no projeto,
menos a IA precisa supor.

## 1. O que trazer

| Insumo | De onde vem | Para que serve aqui |
|---|---|---|
| TO-BE e melhorias (`M-`) | Mapeamento (parte 1) | O que muda no processo; impactos |
| Indicadores e linha de base | Mapeamento (parte 1) | Indicadores de resultado que a adoção deve mover |
| Escopo, módulos (`MOD-`), perfis (`PER-`), casos de uso (`UC-`), telas (`TL-`) | Especificação (parte 2), `01_VISAO_ESCOPO.md` e `02_PERFIS_E_JORNADAS.md` | Quem usa o quê; impactos por perfil; telas para o manual |
| Releases e plano de implantação | Especificação, `13_BACKLOG.md` e `14_OPERACAO.md` | Ondas de entrada em uso; operação em paralelo |
| Sistema publicado (endereço de validação) | Desenvolvimento | Capturas de tela; vídeo; teste do guia rápido |
| Data prevista de entrada em uso | Patrocinador ou dono do processo | Referência `S0` dos momentos |
| O que se sabe das pessoas | Entrevistas do mapeamento, conversa com o aluno | Posições e notas ADKAR |

## 2. O mínimo para começar

- O escopo e a lista de perfis da especificação (ou, sem especificação, as raias do TO-BE).
- Uma frase sobre o que o sistema muda no trabalho de cada perfil.
- A função de quem patrocina o projeto.

Sem isso, registre `DEC` no README do projeto e trabalhe com hipóteses marcadas.

## 3. Onde fica

Se o projeto do sistema já tem `insumos/` e `especificacao/`, a implantação fica em `implantacao/`, dentro dele, e
cita os arquivos pelo caminho relativo. Se não tem, copie o necessário para `insumos/` do projeto novo e registre em
`insumos/LEIA-ME.md` o que veio de onde.
