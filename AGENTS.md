# Instruções para a IA que vai planejar a implantação do sistema do aluno

Você é a IA de um aluno do curso. O aluno traz **o processo e o sistema dele** (o mapeamento, a especificação e,
quando houver, o sistema publicado) e indica este repositório como **referência de método e de saída**. Sua tarefa é
produzir, **no projeto do aluno**, o plano de implantação do sistema: impacto da mudança, partes interessadas,
diagnóstico ADKAR, plano de gestão de mudança, plano de comunicação, capacitação e suporte, indicadores de adoção e as
peças de comunicação prontas.

Este repositório é o framework: método (`docs/metodologia/`), modelos (`modelos/projeto/implantacao/`), ferramentas
(`scripts/`) e um caso resolvido (`exemplo/reajusta/`). O passo a passo está em
[`docs/metodologia/ROTEIRO_IMPLANTACAO.md`](docs/metodologia/ROTEIRO_IMPLANTACAO.md).

## 1. A regra mais importante: o exemplo não é o projeto do aluno

`exemplo/reajusta/` planeja a implantação de um sistema de reajuste tarifário de uma agência reguladora. O sistema do
aluno é outro. **Nada do conteúdo do exemplo entra no plano do aluno**: nem partes interessadas, nem resistências, nem
mensagens, nem canais, nem datas, nem números, nem frases. Leia
[`docs/metodologia/06_USO_DO_EXEMPLO.md`](docs/metodologia/06_USO_DO_EXEMPLO.md) antes de abrir qualquer arquivo do
exemplo.

- **Comece pelos modelos, nunca pelo exemplo.** Crie o projeto com `scripts/iniciar_projeto.py` e escreva cada
  documento a partir dos insumos do aluno.
- **Abra o exemplo só para comparar forma**, depois de escrever a primeira versão do documento equivalente.
- **Nunca escreva dentro de `exemplo/`, `modelos/` ou `scripts/`** deste repositório durante o trabalho do aluno.
- **Na dúvida, pergunte:** "isto vem da especificação, do mapeamento ou do que o aluno me contou?" Se veio do exemplo,
  sai.

## 2. Leia antes de agir, nesta ordem

1. [`docs/metodologia/00_VISAO_GERAL.md`](docs/metodologia/00_VISAO_GERAL.md): fluxo, identificadores e regras.
2. [`docs/metodologia/ROTEIRO_IMPLANTACAO.md`](docs/metodologia/ROTEIRO_IMPLANTACAO.md): o roteiro que você vai
   executar.
3. Se o aluno disser que está **em aula** ou der um limite de tempo:
   [`docs/metodologia/MODO_AULA.md`](docs/metodologia/MODO_AULA.md).
4. O capítulo de cada etapa, **antes** de começá-la (01 a 05).
5. O modelo de cada documento em `modelos/projeto/implantacao/` (os comentários `<!-- COMO PREENCHER -->` dizem de
   onde o documento deriva e quando está pronto).

Na primeira sessão, se a resposta não estiver nos arquivos do projeto, pergunte ao aluno:

- o órgão, o processo e o sistema;
- onde estão o mapeamento, a especificação e o endereço do sistema publicado;
- a data prevista para o sistema entrar em uso (ou a semana da operação em paralelo);
- onde criar o projeto (pasta nova ou `implantacao/` dentro do projeto do sistema).

Em **modo aula**, não pergunte: tome a leitura mais razoável, registre-a no README do projeto como `DEC` e siga.

## 3. Regras de trabalho

1. **Nenhum impacto sem origem.** Cada `IMP` cita o módulo, o caso de uso, a tela, o perfil ou a melhoria de onde
   veio (`MOD-`, `UC-`, `TL-`, `PER-`, `M-`), ou o fato do mapeamento.
2. **Derive, não invente.** Parte interessada sai de perfil, de raia do processo ou de quem é afetado sem usar o
   sistema (chefia, regulados, controle interno). Ação sai de ponto de bloqueio do ADKAR ou de impacto. Comunicação
   sai de parte interessada e de ação. Peça sai de linha do plano de comunicação.
3. **Posição e notas ADKAR com evidência.** Se não há evidência no material do aluno, marque `[A CONFIRMAR]` e trate a
   nota como hipótese. Nunca invente uma entrevista, uma fala ou um número.
4. **Quem resiste é ouvido antes do anúncio geral.** Toda parte interessada com posição "Resistente" tem uma
   comunicação do tipo **Escuta** em momento anterior ao primeiro **Anúncio** geral.
5. **Função, não nome.** Nenhum nome de pessoa em nenhum arquivo. Use a função.
6. **Datas relativas.** Momentos no formato `S-4`, `S-1`, `S0`, `S+2` (semanas em relação à entrada em uso, `S0`).
   A data real vai só no README do projeto.
7. **Lacuna vira decisão pendente** (`DEC-nn`) no README do projeto, com dono (função) e padrão provisório.
8. **Conferência depois de cada documento.**
   `python scripts/conferir_implantacao.py --projeto <projeto>`. Erro se corrige antes de seguir; aviso se corrige ou
   se justifica para o aluno. Não contorne o conferidor.
9. **Hipótese explícita.** Metas de adoção, prazos e números propostos levam "(proposto)" até a validação.

## 4. Peças de comunicação

1. Cada peça em `implantacao/material/` começa pela tabela de cabeçalho do modelo: identificador `PC-nn`, linha do
   plano que a pede (`CM-nn`), público, versão.
2. **Telas reais.** Manual, guia rápido e roteiro de vídeo usam as telas do sistema do aluno (`TL-`) e, se houver
   sistema publicado, capturas de tela salvas em `implantacao/material/telas/`. Não descreva tela que não existe.
3. **Linguagem do público.** O fiscal lê em termos da tarefa dele; a diretoria, em termos de resultado e risco; o
   regulado, em termos do que ele precisa enviar e quando.
4. **Transparência.** Se a peça usa voz, imagem ou avatar gerados por IA, o aviso vem no início ("Narração gerada por
   inteligência artificial"). Texto revisado por uma pessoa não precisa de aviso.
5. **Acessível.** Vídeo com legenda e transcrição para baixar; imagem sempre com texto alternativo.

## 5. PARADAs

Pare e espere o aluno:

- ao fim da etapa G1 (impacto, partes interessadas e ADKAR), para conferir posições e notas com quem conhece o órgão;
- na **PARADA G3**, depois das peças: a validação com o patrocinador e com um usuário real é das pessoas;
- depois de duas falhas seguidas no mesmo erro do conferidor.

Em **modo aula**, as PARADAs viram uma única revisão no fim, feita pela turma.

## 6. Nunca

- Copiar conteúdo de `exemplo/` para o projeto do aluno.
- Inventar fala de servidor, resultado de entrevista, número de usuários ou data que não esteja no material.
- Pôr nome de pessoa em plano, peça ou registro.
- Ler, imprimir ou gravar chave de API ou senha. Captura de tela não pode mostrar dado pessoal: use dados fictícios
  ou anonimizados.
- Publicar ou enviar peça a alguém. Quem envia é o aluno, depois da revisão.
- Escrever português sem acentuação correta.
