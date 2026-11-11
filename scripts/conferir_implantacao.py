"""Confere a forma e a rastreabilidade do plano de implantação do aluno.

Uso, da raiz deste repositório:
    python scripts/conferir_implantacao.py --projeto <pasta do projeto>

A pasta é o projeto (com `implantacao/` dentro) ou a própria pasta `implantacao/`. Sai com código 1 se houver erro.

Códigos:
    G01 erro   marcador {{...}} ainda não preenchido
    G02 erro   identificador citado que não está definido
    G03 erro   termo do caso resolvido no projeto do aluno
    G04 erro   impacto sem origem; aviso: parte interessada sem impacto
    G05 erro   parte interessada sem linha ADKAR, nota fora de 1 a 5 ou ponto de bloqueio que não confere
    G06 erro   ponto de bloqueio sem ação no elemento
    G07 erro   parte resistente sem escuta antes do primeiro anúncio geral
    G08 aviso  parte interessada que não recebe nenhuma comunicação
    G09 erro   peça sem cabeçalho ou sem linha do plano; aviso: peça que o plano não pede
    G10 erro   peça com voz sintética sem aviso de IA
    G11 aviso  parte resistente sem perda percebida registrada
    G12 aviso  indicadores sem uso ou sem resultado; meta sem "(proposto)"
    G13 aviso  perfil que usa o sistema sem capacitação ou sem suporte
    G14 erro   sustentação sem dono da solução, pessoa de reserva ou desligamento do método antigo
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

FERRAMENTA = Path(__file__).resolve().parents[1]
ELEMENTOS = ["Consciência", "Desejo", "Conhecimento", "Habilidade", "Reforço"]
PADRAO_ID = re.compile(r"(?<![A-Za-z0-9-])(IND-AD-\d+|IMP-\d+|PI-[A-Z0-9]+|AC-\d+|CM-\d+|CAP-\d+|SUP-\d+|PC-\d+|DEC-\d+)\b")
COMENTARIO = re.compile(r"<!--.*?-->", re.S)
MARCADOR = re.compile(r"\{\{.*?\}\}")
MOMENTO = re.compile(r"S\s*([+-−]\s*\d+|0)")

DOCS = {
    "imp": "01_IMPACTO_DA_MUDANCA.md",
    "pi": "02_PARTES_INTERESSADAS.md",
    "adkar": "03_DIAGNOSTICO_ADKAR.md",
    "plano": "04_PLANO_GESTAO_MUDANCA.md",
    "cm": "05_PLANO_COMUNICACAO.md",
    "cap": "06_CAPACITACAO_E_SUPORTE.md",
    "ind": "07_INDICADORES_DE_ADOCAO.md",
}


@dataclass
class Achado:
    codigo: str
    nivel: str  # "erro" ou "aviso"
    arquivo: str
    texto: str


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower().strip()


def ler(p: Path) -> str:
    return COMENTARIO.sub("", p.read_text(encoding="utf-8")) if p.exists() else ""


def tabelas(md: str) -> list[tuple[list[str], list[dict[str, str]]]]:
    """Tabelas em pipe: cabeçalho e linhas como dicionários (chave sem acento, minúscula)."""
    saida, linhas = [], md.splitlines()
    i = 0
    while i < len(linhas):
        l = linhas[i].strip()
        if l.startswith("|") and i + 1 < len(linhas) and re.match(r"^\|\s*:?-{3,}", linhas[i + 1].strip()):
            cab = [c.strip().strip("*") for c in l.strip("|").split("|")]
            chaves = [sem_acento(c) for c in cab]
            corpo, i = [], i + 2
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                cel = [c.strip() for c in linhas[i].strip().strip("|").split("|")]
                cel += [""] * (len(chaves) - len(cel))
                corpo.append(dict(zip(chaves, cel)))
                i += 1
            saida.append((chaves, corpo))
        else:
            i += 1
    return saida


def tabela_com(md: str, *colunas: str) -> list[dict[str, str]]:
    alvo = [sem_acento(c) for c in colunas]
    for chaves, corpo in tabelas(md):
        if all(c in chaves for c in alvo):
            return [r for r in corpo if not MARCADOR.search(" ".join(r.values()))]
    return []


def ids_em(texto: str) -> list[str]:
    return PADRAO_ID.findall(texto or "")


def momento(texto: str) -> int | None:
    m = MOMENTO.search(texto or "")
    if not m:
        return None
    return int(m.group(1).replace("−", "-").replace(" ", ""))


def elemento(texto: str) -> str | None:
    t = sem_acento(texto)
    for e in ELEMENTOS:
        if sem_acento(e) in t:
            return e
    if "nenhum" in t:
        return "Nenhum"
    return None


def conferir(projeto: Path) -> list[Achado]:
    impl = projeto / "implantacao" if (projeto / "implantacao").is_dir() else projeto
    achados: list[Achado] = []

    def a(codigo: str, nivel: str, arquivo: str, texto: str) -> None:
        achados.append(Achado(codigo, nivel, arquivo, texto))

    conf = {}
    if (impl / "conferencia.json").exists():
        conf = json.loads((impl / "conferencia.json").read_text(encoding="utf-8"))
    arquivos = sorted(p for p in impl.rglob("*.md") if p.name != "LEIA-ME.md")
    textos = {p.relative_to(impl).as_posix(): ler(p) for p in arquivos}

    # G01 marcadores
    for nome, t in textos.items():
        n = len(MARCADOR.findall(t))
        if n:
            a("G01", "erro", nome, f"{n} marcador(es) {{{{...}}}} a preencher")

    # G03 termos do exemplo
    if not conf.get("exemplo"):
        termos = json.loads((FERRAMENTA / "scripts" / "termos_do_exemplo.json").read_text(encoding="utf-8"))["termos"]
        permitidos = {sem_acento(t["termo"] if isinstance(t, dict) else t) for t in conf.get("termos_permitidos", [])}
        for nome, t in textos.items():
            baixo = sem_acento(t)
            for termo in termos:
                st = sem_acento(termo)
                if st not in permitidos and re.search(r"(?<![a-z0-9])" + re.escape(st) + r"(?![a-z0-9])", baixo):
                    a("G03", "erro", nome, f"termo do caso resolvido: \"{termo}\"")

    d = {k: textos.get(v, "") for k, v in DOCS.items()}
    imp = tabela_com(d["imp"], "ID", "Origem")
    pis = tabela_com(d["pi"], "ID", "Posição")
    adk = tabela_com(d["adkar"], "Parte", "Ponto de bloqueio")
    acs = tabela_com(d["plano"], "ID", "Elemento ADKAR")
    res = tabela_com(d["plano"], "Parte", "Perda percebida")
    cms = tabela_com(d["cm"], "ID", "Tipo", "Momento")
    caps = tabela_com(d["cap"], "ID", "Capacitação")
    sups = tabela_com(d["cap"], "ID", "Suporte")
    inds = tabela_com(d["ind"], "ID", "Tipo", "Meta")
    decs = tabela_com(textos.get("README.md", ""), "ID", "Decisão")

    pecas: dict[str, tuple[str, dict[str, str], str]] = {}
    for nome, t in textos.items():
        if not nome.startswith("material/"):
            continue
        cab = {sem_acento(r.get("item", "")): r.get("conteudo", "") for r in tabela_com(t, "Item", "Conteúdo")}
        if not cab.get("peca") and MARCADOR.search(t) is None:
            a("G09", "erro", nome, "peça sem a tabela de cabeçalho (Peça, Plano, Público, Versão)")
            continue
        pid = (ids_em(cab.get("peca", "")) or [None])[0]
        if pid:
            pecas[pid] = (nome, cab, t)

    definidos = set()
    for linhas in (imp, pis, acs, cms, caps, sups, inds, decs):
        definidos |= {ids_em(r.get("id", ""))[0] for r in linhas if ids_em(r.get("id", ""))}
    definidos |= set(pecas)

    # G02 referências
    for nome, t in textos.items():
        limpo = "\n".join(l for l in t.splitlines() if not MARCADOR.search(l))
        for ref in sorted(set(ids_em(limpo)) - definidos):
            a("G02", "erro", nome, f"{ref} citado, mas não definido")

    pi_ids = [ids_em(r["id"])[0] for r in pis if ids_em(r["id"])]
    posicao = {ids_em(r["id"])[0]: sem_acento(r.get("posicao", "")) for r in pis if ids_em(r["id"])}
    perfil = {ids_em(r["id"])[0]: r.get("perfil", "") for r in pis if ids_em(r["id"])}

    def cobre(celula: str, pi: str) -> bool:
        return pi in ids_em(celula) or "todos" in sem_acento(celula)

    # G04 impacto
    for r in imp:
        o = r.get("origem", "").strip()
        if o in {"", "—", "-"}:
            a("G04", "erro", DOCS["imp"], f"{r.get('id')} sem origem")
    for pi in pi_ids:
        if imp and not any(cobre(r.get("partes afetadas", ""), pi) for r in imp):
            a("G04", "aviso", DOCS["imp"], f"{pi} não aparece em nenhum impacto")

    # G05 ADKAR
    bloqueio: dict[str, str] = {}
    linhas_adk = {ids_em(r.get("parte", ""))[0]: r for r in adk if ids_em(r.get("parte", ""))}
    for pi in pi_ids:
        r = linhas_adk.get(pi)
        if not r:
            if d["adkar"]:
                a("G05", "erro", DOCS["adkar"], f"{pi} sem linha no diagnóstico ADKAR")
            continue
        notas = []
        for e in ELEMENTOS:
            m = re.search(r"\d", r.get(sem_acento(e), ""))
            v = int(m.group()) if m else None
            if v is None or not 1 <= v <= 5:
                a("G05", "erro", DOCS["adkar"], f"{pi}: nota de {e} fora de 1 a 5")
            notas.append(v or 0)
        esperado = next((e for e, v in zip(ELEMENTOS, notas) if v <= 3), "Nenhum")
        declarado = elemento(r.get("ponto de bloqueio", ""))
        if declarado != esperado:
            a("G05", "erro", DOCS["adkar"], f"{pi}: ponto de bloqueio declarado {declarado}, pelas notas é {esperado}")
        bloqueio[pi] = esperado

    # G06 ação no ponto de bloqueio
    for pi, e in bloqueio.items():
        if e == "Nenhum" or not d["plano"]:
            continue
        if not any(cobre(r.get("partes", ""), pi) and elemento(r.get("elemento adkar", "")) == e for r in acs):
            a("G06", "erro", DOCS["plano"], f"{pi} trava em {e}, mas nenhuma ação AC- trata {e} para essa parte")

    # G07 escuta antes do anúncio
    anuncios = [momento(r.get("momento", "")) for r in cms if "anuncio" in sem_acento(r.get("tipo", ""))]
    anuncios = [m for m in anuncios if m is not None]
    primeiro = min(anuncios) if anuncios else None
    for pi in pi_ids:
        if "resistente" not in posicao.get(pi, "") or not d["cm"]:
            continue
        if primeiro is None:
            a("G07", "aviso", DOCS["cm"], "o plano não tem nenhum Anúncio")
            break
        escutas = [momento(r.get("momento", "")) for r in cms
                   if "escuta" in sem_acento(r.get("tipo", "")) and pi in ids_em(r.get("publico", ""))]
        if not any(m is not None and m < primeiro for m in escutas):
            a("G07", "erro", DOCS["cm"], f"{pi} é Resistente e não tem Escuta antes do primeiro Anúncio (S{primeiro:+d})")

    # G08 toda parte comunicada
    for pi in pi_ids:
        if cms and not any(cobre(r.get("publico", ""), pi) for r in cms):
            a("G08", "aviso", DOCS["cm"], f"{pi} não recebe nenhuma comunicação")

    # G09 peças e plano
    pedidas = {p for r in cms for p in ids_em(r.get("peca", ""))}
    for pid, (nome, cab, t) in pecas.items():
        if MARCADOR.search(t):
            continue
        if not ids_em(cab.get("plano", "")):
            a("G09", "erro", nome, f"{pid} sem a linha CM- do plano que a pede")
        elif cms and pid not in pedidas:
            a("G09", "aviso", nome, f"{pid} existe, mas nenhuma linha do plano de comunicação a usa")

    # G10 aviso de IA
    for pid, (nome, cab, t) in pecas.items():
        if "sintetic" in sem_acento(cab.get("voz", "")):
            corpo = t.split("| Duração", 1)[-1]
            if "inteligencia artificial" not in sem_acento(corpo):
                a("G10", "erro", nome, f"{pid} tem voz sintética e não avisa no início que a narração é gerada por inteligência artificial")

    # G11 resistências registradas
    com_perda = {p for r in res for p in ids_em(r.get("parte", ""))}
    for pi in pi_ids:
        if "resistente" in posicao.get(pi, "") and d["plano"] and pi not in com_perda:
            a("G11", "aviso", DOCS["plano"], f"{pi} é Resistente e não tem perda percebida registrada")

    # G12 indicadores
    if inds:
        tipos = {sem_acento(r.get("tipo", "")) for r in inds}
        if not any("uso" in t for t in tipos):
            a("G12", "aviso", DOCS["ind"], "nenhum indicador de Uso")
        if not any("resultado" in t for t in tipos):
            a("G12", "aviso", DOCS["ind"], "nenhum indicador de Resultado")
        for r in inds:
            if "proposto" not in sem_acento(r.get("meta", "")):
                a("G12", "aviso", DOCS["ind"], f"{r.get('id')}: meta sem \"(proposto)\"")

    # G13 capacitação e suporte para quem usa o sistema
    if d["cap"]:
        for pi in pi_ids:
            if "PER-" not in perfil.get(pi, ""):
                continue
            if not any(cobre(r.get("partes", ""), pi) for r in caps):
                a("G13", "aviso", DOCS["cap"], f"{pi} usa o sistema e não tem capacitação")
            if not any(cobre(r.get("partes", ""), pi) for r in sups):
                a("G13", "aviso", DOCS["cap"], f"{pi} usa o sistema e não tem suporte")

    # G14 sustentação depois do projeto
    if d["plano"] and not MARCADOR.search(d["plano"]):
        sust = {sem_acento(r.get("item", "")): r.get("resposta", "").strip() for r in tabela_com(d["plano"], "Item", "Resposta")}
        for item in ("Dono da solução", "Pessoa de reserva", "Desligamento do método antigo"):
            if sust.get(sem_acento(item), "") in {"", "—", "-"}:
                a("G14", "erro", DOCS["plano"], f"sustentação: \"{item}\" não preenchido")

    return achados


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--projeto", required=True, help="pasta do projeto ou a própria pasta implantacao/")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    args = ap.parse_args()
    achados = conferir(Path(args.projeto).resolve())
    erros = [x for x in achados if x.nivel == "erro"]
    if args.json:
        print(json.dumps([x.__dict__ for x in achados], ensure_ascii=False, indent=2))
    else:
        for x in sorted(achados, key=lambda x: (x.nivel != "erro", x.codigo, x.arquivo)):
            print(f"{x.codigo} {x.nivel:5} {x.arquivo}: {x.texto}")
        avisos = len(achados) - len(erros)
        print(f"\n{len(erros)} erro(s), {avisos} aviso(s).", "Corrija os erros antes de seguir." if erros else "Sem erros.")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
