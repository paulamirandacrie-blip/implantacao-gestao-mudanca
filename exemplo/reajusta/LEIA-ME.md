# Caso resolvido: implantação do Reajusta (exemplo, não modelo)

> **Este é um exemplo de outro caso.** Serve para ver como fica cada documento do método quando está pronto. **Não
> copie conteúdo daqui para o seu plano**: partes interessadas, posições, resistências, mensagens, canais, momentos,
> metas, números ou frases. O seu plano nasce de `modelos/projeto/` (`scripts/iniciar_projeto.py`). O conferidor
> barra termos deste exemplo no seu projeto. Leia antes o capítulo [06](../../docs/metodologia/06_USO_DO_EXEMPLO.md).

O Reajusta é o sistema do reajuste tarifário anual das concessões de saneamento de uma agência reguladora estadual
(AGENERSA, RJ). A especificação completa está no
[framework-especificacao-sistemas](https://github.com/RaulAraujoSilva/framework-especificacao-sistemas/tree/main/exemplo/reajusta),
de onde este plano deriva: módulos, perfis, casos de uso, telas, releases e o plano de implantação no piloto (Águas
de Paraty).

**Limite:** o plano foi escrito só com a especificação pública, sem conversar com os servidores. Por isso posições e
notas ADKAR estão marcadas `[A CONFIRMAR]`, como deve estar todo plano antes da PARADA G1.

## Onde ver cada etapa

| Etapa | Arquivo |
|---|---|
| Sistema, patrocinador, S0 e decisões | [`implantacao/README.md`](implantacao/README.md) |
| Impacto | [`01_IMPACTO_DA_MUDANCA.md`](implantacao/01_IMPACTO_DA_MUDANCA.md) |
| Partes interessadas | [`02_PARTES_INTERESSADAS.md`](implantacao/02_PARTES_INTERESSADAS.md) |
| ADKAR | [`03_DIAGNOSTICO_ADKAR.md`](implantacao/03_DIAGNOSTICO_ADKAR.md) |
| Plano de gestão de mudança | [`04_PLANO_GESTAO_MUDANCA.md`](implantacao/04_PLANO_GESTAO_MUDANCA.md) |
| Plano de comunicação | [`05_PLANO_COMUNICACAO.md`](implantacao/05_PLANO_COMUNICACAO.md) |
| Capacitação e suporte | [`06_CAPACITACAO_E_SUPORTE.md`](implantacao/06_CAPACITACAO_E_SUPORTE.md) |
| Indicadores de adoção | [`07_INDICADORES_DE_ADOCAO.md`](implantacao/07_INDICADORES_DE_ADOCAO.md) |
| Peças | [`implantacao/material/`](implantacao/material/) |

## Comando (da raiz do repositório)

```bash
python scripts/conferir_implantacao.py --projeto exemplo/reajusta
```

O `conferencia.json` deste exemplo tem `"exemplo": true`: é o que desliga, só aqui, a barreira contra os termos do
próprio exemplo.
