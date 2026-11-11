# Modo aula: o roteiro em 30 a 40 minutos

Use quando o aluno disser que está em aula ou der um limite de tempo. O objetivo é **terminar dentro do tempo** com um
primeiro rascunho completo e conferido, não a melhor versão possível. A versão final sai depois, na oficina.

## Regras do modo aula

1. **Não pergunte.** Tome a leitura mais razoável dos arquivos do projeto e registre cada suposição como `DEC` no
   README da implantação.
2. **Paralelize.** Depois de criar a pasta (G0.1) e ler os insumos (G0.2), lance subagentes em paralelo, um por
   documento, cada um com o capítulo da metodologia e o modelo do documento. Use o modelo mais rápido disponível nos
   subagentes. Você, o agente principal, junta e confere.
3. **Ordem das ondas:**
   - **Onda 1 (em paralelo):** `01_IMPACTO_DA_MUDANCA.md` e `02_PARTES_INTERESSADAS.md`.
   - **Onda 2 (em paralelo, depois da 1):** `03_DIAGNOSTICO_ADKAR.md`, `06_CAPACITACAO_E_SUPORTE.md` e
     `07_INDICADORES_DE_ADOCAO.md`.
   - **Onda 3 (em paralelo, depois da 2):** `04_PLANO_GESTAO_MUDANCA.md` e `05_PLANO_COMUNICACAO.md`.
   - **Peças (em paralelo, depois da 3):** uma peça por subagente.
4. **Confira uma vez por onda** com `conferir_implantacao.py` e corrija os erros antes da onda seguinte.
5. **PARADAs viram revisão no fim.** Não pare em G1 nem em G3: termine e entregue a lista do que a pessoa precisa
   conferir.
6. **Vídeo:** em aula, entregue o roteiro com as telas; gere o vídeo só se o tempo sobrar.

## Comando de aula (para colar no agente)

```
Estou em aula e tenho 30 minutos. Use o repositório <URL deste repositório> como
referência de método (leia o AGENTS.md e o docs/metodologia/MODO_AULA.md).
Crie a implantação dentro deste projeto (pasta implantacao/) e produza os
documentos 01 a 07 a partir do mapeamento e da especificação que já estão aqui.
Não me faça perguntas: registre as suposições como DEC no README.
Lance subagentes em paralelo, um por documento, na ordem das ondas do modo aula.
Rode o conferidor ao fim de cada onda. Ao terminar, me mostre o resumo:
partes interessadas, pontos de bloqueio, as 3 ações principais e o que preciso
conferir.
```

## Comando das peças (para colar no agente)

```
Agora, com base no plano de comunicação em implantacao/05_PLANO_COMUNICACAO.md,
produza as peças pedidas, seguindo os modelos de implantacao/material/:
a apresentação de 5 slides para a diretoria (que o patrocinador usa no
anúncio), as perguntas frequentes a partir das resistências do 04, o guia
rápido e, se o plano pedir, o comunicado aos regulados.
Manual e vídeos: se o projeto já tem o kit-manual-usuario da aula 7, não
reescreva; faça a peça apontar para o manual e os roteiros do kit.
Uma peça por subagente, em paralelo. Rode o conferidor no fim.
Tempo: 40 minutos.
```

## Resultado esperado no fim da aula

- Documentos 01 a 07 sem erro no conferidor.
- Ao menos o guia rápido e o roteiro de vídeo prontos.
- Lista de `DEC` e de `[A CONFIRMAR]` para a oficina.
