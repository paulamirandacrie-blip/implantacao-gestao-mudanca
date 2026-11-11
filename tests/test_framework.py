"""Testes do framework: modelos neutros, conferidor e iniciação do projeto."""
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))

import conferir_implantacao as conf  # noqa: E402
import iniciar_projeto as ini  # noqa: E402


def erros(achados):
    return [a for a in achados if a.nivel == "erro"]


def test_exemplo_sem_erros():
    achados = conf.conferir(RAIZ / "exemplo" / "reajusta")
    assert erros(achados) == [], [f"{a.codigo} {a.arquivo}: {a.texto}" for a in erros(achados)]


def test_modelos_sem_termos_do_exemplo():
    termos = json.loads((RAIZ / "scripts" / "termos_do_exemplo.json").read_text(encoding="utf-8"))["termos"]
    for f in (RAIZ / "modelos").rglob("*.md"):
        texto = conf.sem_acento(conf.ler(f))  # comentários de orientação podem citar o caminho do exemplo
        for t in termos:
            assert conf.sem_acento(t) not in texto, f"{t} em {f}"


def test_projeto_novo_so_marcadores(tmp_path):
    ini.iniciar(tmp_path / "proj", "Sistema X", "AGX")
    achados = erros(conf.conferir(tmp_path / "proj"))
    assert achados and {a.codigo for a in achados} == {"G01"}


def test_dentro_de_projeto_existente(tmp_path):
    (tmp_path / "sis" / "especificacao").mkdir(parents=True)
    ini.iniciar(tmp_path / "sis", "Sistema X", "AGX", dentro=True)
    assert (tmp_path / "sis" / "implantacao" / "05_PLANO_COMUNICACAO.md").exists()


def _copia_exemplo(tmp_path):
    import shutil
    destino = tmp_path / "ex"
    shutil.copytree(RAIZ / "exemplo" / "reajusta", destino)
    return destino / "implantacao"


def test_g05_bloqueio_errado(tmp_path):
    impl = _copia_exemplo(tmp_path)
    p = impl / "03_DIAGNOSTICO_ADKAR.md"
    p.write_text(p.read_text(encoding="utf-8").replace("| 2 | 2 | 2 | 2 | Desejo |", "| 2 | 2 | 2 | 2 | Conhecimento |"), encoding="utf-8")
    assert "G05" in {a.codigo for a in erros(conf.conferir(impl))}


def test_g07_anuncio_antes_da_escuta(tmp_path):
    impl = _copia_exemplo(tmp_path)
    p = impl / "05_PLANO_COMUNICACAO.md"
    p.write_text(p.read_text(encoding="utf-8").replace("| Reunião geral e intranet | S-4 |", "| Reunião geral e intranet | S-7 |"), encoding="utf-8")
    assert "G07" in {a.codigo for a in erros(conf.conferir(impl))}


def test_g10_voz_sintetica_sem_aviso(tmp_path):
    impl = _copia_exemplo(tmp_path)
    p = impl / "material" / "05_ROTEIRO_VIDEO.md"
    p.write_text(p.read_text(encoding="utf-8").replace("Este vídeo tem narração gerada por inteligência artificial. ", ""), encoding="utf-8")
    assert "G10" in {a.codigo for a in erros(conf.conferir(impl))}


def test_g03_termo_do_exemplo_no_projeto(tmp_path):
    ini.iniciar(tmp_path / "proj", "Sistema X", "AGX")
    p = tmp_path / "proj" / "implantacao" / "01_IMPACTO_DA_MUDANCA.md"
    p.write_text(p.read_text(encoding="utf-8") + "\nComo no Reajusta.\n", encoding="utf-8")
    assert "G03" in {a.codigo for a in erros(conf.conferir(tmp_path / "proj"))}


def test_cli_codigo_de_saida():
    r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "conferir_implantacao.py"), "--projeto", str(RAIZ / "exemplo" / "reajusta")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout
