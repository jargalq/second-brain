"""Second Brain самбарын өгөгдлийг vault-аас үүсгэнэ.

Ажиллуулах:  py -3 -I "_system/dashboard/second_brain_dashboard.py"
Гаралт:      _system/dashboard/data/{tasks,projects,inbox,activity,para}.json
Шийдвэр:     04-Resources/Atomic/decisions/2026-11-05 - Second Brain самбарыг өдөр бүр 07-00-д шинэчлэх.md
Самбар:      https://claude.ai/artifact/A9nkgRwgBD86wsTJ77EPu6 (scheduled task файлуудыг upload хийнэ)

Зөвхөн уншина; vault-д data/ хавтаснаас өөр юу ч бичихгүй.
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parents[2]
OUT = VAULT / "_system" / "dashboard" / "data"
DONE = "хийсэн"
ACTIVITY_DAYS = 30

DONE_ALIASES = {"хийсэн", "completed", "done", "дууссан"}
SKIP_TASK = {"cancelled", "цуцалсан"}
SKIP_FILES = {"README.md", "Tasks.md", "Inbox.md"}


def front(path):
    """Frontmatter-ийг dict болгож буцаана (алдаатай бол хоосон)."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    try:
        data = yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        # Эвдэрхий YAML: энгийн «түлхүүр: утга» мөрөөр уншина
        data = {}
        for line in text[3:end].splitlines():
            m = re.match(r"^([^\s#:][^:]*):\s*(.*)$", line)
            if m:
                data[m.group(1).strip()] = m.group(2).strip().strip("'\"")
    return data if isinstance(data, dict) else {}


def s(v):
    """Утгыг цэвэр текст болгоно: огноо, жагсаалт, [[холбоос]]."""
    if v is None:
        return ""
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()[:10]
    if isinstance(v, list):
        v = v[0] if v else ""
        return s(v)
    v = str(v).strip()
    m = re.search(r"\[\[([^\]|#]+)", v)
    if m:
        v = m.group(1).rsplit("/", 1)[-1]
    return v


def area_of(fm):
    a = s(fm.get("хүрээ") or fm.get("areas") or fm.get("area") or fm.get("context"))
    a = a.split("/")[0].strip()
    if a in ("README", ""):
        return "—"
    return {"work": "Ажил", "personal": "Хувийн"}.get(a, a)


def file_date(path):
    m = re.match(r"(\d{4}-\d{2}-\d{2})", path.name)
    return m.group(1) if m else ""


def tasks():
    rows = []
    for p in sorted((VAULT / "01-GTD" / "Tasks").glob("*.md")):
        if p.name in SKIP_FILES:
            continue
        fm = front(p)
        status = s(fm.get("төлөв") or fm.get("status")) or "—"
        if status in SKIP_TASK:
            continue
        if status in DONE_ALIASES:
            status = DONE
        created = s(fm.get("огноо") or fm.get("date")) or file_date(p)
        due = s(fm.get("due") or fm.get("хугацаа"))
        if not due and fm.get("огноо") and status != DONE and "цаг" in fm:
            due = created
        name = re.sub(r"^\d{4}-\d{2}-\d{2} - ", "", p.stem)
        rows.append({"task": name, "created": created[:10], "status": status,
                     "due": due[:10], "area": area_of(fm)})
    return rows


def projects():
    rows = []
    root = VAULT / "02-Projects"
    for p in sorted(root.rglob("*.md")):
        if p.name.startswith("_") or p.name in SKIP_FILES:
            continue
        fm = front(p)
        if s(fm.get("type")) != "project" and s(fm.get("төрөл")) not in ("төсөл", "project"):
            continue
        rel = p.relative_to(root).parts
        group = rel[0] if len(rel) > 1 else "(үндсэн)"
        start, end = s(fm.get("эхлэх") or fm.get("start")), s(fm.get("дуусах") or fm.get("due"))
        period = f"{start[:7]} → {end[:7]}" if start and end else ""
        rows.append({"project": p.stem, "group": group,
                     "status": s(fm.get("төлөв") or fm.get("status")) or "—",
                     "area": area_of(fm), "period": period})
    return rows


def inbox():
    d = VAULT / "01-GTD" / "Inbox"
    return [{"item": p.stem} for p in sorted(d.iterdir())
            if p.is_file() and p.name not in SKIP_FILES and not p.name.startswith(".")]


def activity():
    since = (dt.date.today() - dt.timedelta(days=ACTIVITY_DAYS - 1)).isoformat()
    sources = [("Шийдвэр", VAULT / "04-Resources" / "Atomic" / "decisions"),
               ("Мэдлэг", VAULT / "04-Resources" / "Atomic" / "knowledge"),
               ("Өдрийн тэмдэглэл", VAULT / "01-GTD" / "Daily")]
    counts = {}
    for kind, folder in sources:
        for p in folder.glob("*.md"):
            day = file_date(p)
            if day and day >= since:
                counts[(day, kind)] = counts.get((day, kind), 0) + 1
    return [{"day": d, "kind": k, "n": n} for (d, k), n in sorted(counts.items())]


def para():
    folders = ["01-GTD/Inbox", "01-GTD/Tasks", "01-GTD/Daily", "02-Projects",
               "03-Areas", "04-Resources", "99-Archive"]
    return [{"folder": f, "notes": sum(1 for _ in (VAULT / f).rglob("*.md"))} for f in folders]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    data = {"tasks": tasks(), "projects": projects(), "inbox": inbox(),
            "activity": activity(), "para": para()}
    for name, rows in data.items():
        (OUT / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=0),
                                         encoding="utf-8")
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (OUT / "_meta.json").write_text(json.dumps({"generated_at": stamp,
                                                "counts": {k: len(v) for k, v in data.items()}},
                                               ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"generated_at": stamp, **{k: len(v) for k, v in data.items()}},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
