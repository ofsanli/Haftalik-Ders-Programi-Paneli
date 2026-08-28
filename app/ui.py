from pathlib import Path
from fastapi.responses import HTMLResponse

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"


def _read_template(template_name: str) -> str:
    template_path = TEMPLATES_DIR / template_name
    return template_path.read_text(encoding="utf-8")


def home():
    return HTMLResponse(content=_read_template("index.html"))


def panel():
    return HTMLResponse(content=_read_template("panel.html"))
