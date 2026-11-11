"""Cria a pasta de implantação do aluno a partir de `modelos/projeto/`.

A implantação nasce dos modelos, nunca de uma cópia do caso resolvido (`exemplo/`): é o que impede que partes
interessadas, resistências e mensagens do exemplo vazem para o plano de outro órgão.

Uso, da raiz deste repositório:
    python scripts/iniciar_projeto.py <pasta nova> --sistema "Nome do sistema" --orgao SIGLA
    python scripts/iniciar_projeto.py <projeto existente> --sistema "..." --orgao SIGLA --dentro

Sem `--dentro`, a pasta não pode existir com conteúdo. Com `--dentro`, a pasta é o projeto do sistema (com
`insumos/` e `especificacao/`) e só `implantacao/` é acrescentada, sem tocar no resto.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

FERRAMENTA = Path(__file__).resolve().parents[1]
MODELOS = FERRAMENTA / "modelos" / "projeto"


def iniciar(destino: Path, sistema: str | None, orgao: str | None, dentro: bool = False) -> list[Path]:
    destino = destino.resolve()
    exemplo = FERRAMENTA / "exemplo"
    if destino == exemplo or exemplo in destino.parents:
        raise SystemExit("o projeto não pode ficar dentro de exemplo/: ali está só o caso resolvido")
    if dentro:
        if not destino.is_dir():
            raise SystemExit(f"{destino} não existe; sem --dentro, a pasta é criada")
        if (destino / "implantacao").exists():
            raise SystemExit(f"{destino.name}/implantacao/ já existe; não sobrescrevo")
        shutil.copytree(MODELOS / "implantacao", destino / "implantacao")
        base = destino / "implantacao"
    else:
        if destino.exists() and any(destino.iterdir()):
            raise SystemExit(f"{destino.name}/ já existe e não está vazia; use outra pasta ou --dentro")
        shutil.copytree(MODELOS, destino, dirs_exist_ok=True)
        base = destino
    trocas = {}
    if sistema:
        trocas["{{Nome do sistema}}"] = sistema
    if orgao:
        trocas["{{Sigla do órgão}}"] = orgao
    criados = []
    for f in sorted(base.rglob("*")):
        if not f.is_file():
            continue
        criados.append(f)
        if f.suffix in {".md", ".json"} and trocas:
            texto = f.read_text(encoding="utf-8")
            for de, para in trocas.items():
                texto = texto.replace(de, para)
            f.write_text(texto, encoding="utf-8")
    return criados


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("destino", help="pasta nova do projeto, ou o projeto do sistema com --dentro")
    ap.add_argument("--sistema", help="nome do sistema, troca o marcador {{Nome do sistema}}")
    ap.add_argument("--orgao", help="sigla do órgão, troca o marcador {{Sigla do órgão}}")
    ap.add_argument("--dentro", action="store_true", help="acrescenta implantacao/ a um projeto que já existe")
    args = ap.parse_args()
    criados = iniciar(Path(args.destino), args.sistema, args.orgao, args.dentro)
    raiz = Path(args.destino).resolve()
    print(f"{len(criados)} arquivos criados em {raiz.name}/")
    for f in criados:
        print(f"  {f.relative_to(raiz).as_posix()}")
    print("\nPróximos passos:")
    print("  1. Preencha implantacao/README.md (sistema, patrocinador, S0, insumos).")
    print("  2. Escreva os documentos 01 a 07 na ordem do roteiro (docs/metodologia/ROTEIRO_IMPLANTACAO.md).")
    print(f"  3. Confira: python scripts/conferir_implantacao.py --projeto {args.destino}")


if __name__ == "__main__":
    main()
