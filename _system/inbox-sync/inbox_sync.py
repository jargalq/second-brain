"""D: дээрх Inbox хавтсыг Obsidian-ий 01-GTD/Inbox-той холбоно.

Хавтсанд шинээр орсон файл бүрд 01-GTD/Inbox/<файл>.md тэмдэглэл үүсгэнэ
(холбоос, хэмжээ, огноо, эхний мөрүүд). Эх файлыг зөөхгүй, устгахгүй.
Бүртгэсэн файлуудыг state.json-д хадгална. Ажиллуулах:
    python -I "D:\\Seond brain\\_system\\inbox-sync\\inbox_sync.py"
"""
import os, sys, json, re, zipfile, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.normpath(os.path.join(HERE, "..", ".."))
INBOX_NOTES = os.path.join(VAULT, "01-GTD", "Inbox")
STATE = os.path.join(HERE, "state.json")
WATCH = [r"D:\Inbox"]                       # хянах хавтсууд
SKIP = re.compile(r"^(~\$|\.|desktop\.ini$|thumbs\.db$)", re.I)


def preview(path, n=600):
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext in (".txt", ".md", ".csv"):
            with open(path, encoding="utf-8-sig", errors="replace") as f:
                return f.read(n)
        if ext == ".docx":
            x = zipfile.ZipFile(path).read("word/document.xml").decode("utf8")
            paras = ["".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)) for p in re.findall(r"<w:p[ >].*?</w:p>", x, re.S)]
            return "\n".join(p for p in paras if p.strip())[:n]
        if ext == ".pdf":
            import fitz
            d = fitz.open(path)
            t = "".join(d[i].get_text() for i in range(min(2, len(d)))).strip()
            return t[:n] if t else "(скан PDF, %d хуудас)" % len(d)
    except Exception as e:
        return "(уншиж чадсангүй: %s)" % type(e).__name__
    return ""


def size(b):
    for u in ("Б", "КБ", "МБ", "ГБ"):
        if b < 1024:
            return "%.0f %s" % (b, u)
        b /= 1024
    return "%.1f ТБ" % b


def note_path(name):
    base = re.sub(r'[\\/:*?"<>|#^\[\]]', "_", name)
    p = os.path.join(INBOX_NOTES, base + ".md"); k = 2
    while os.path.exists(p):
        p = os.path.join(INBOX_NOTES, "%s (%d).md" % (base, k)); k += 1
    return p


def main():
    os.makedirs(INBOX_NOTES, exist_ok=True)
    state = json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else {}
    new = []
    for root in WATCH:
        if not os.path.isdir(root):
            continue
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if not SKIP.match(d)]
            for fn in fns:
                if SKIP.match(fn):
                    continue
                p = os.path.join(dp, fn)
                if p in state:
                    continue
                st = os.stat(p)
                mt = datetime.datetime.fromtimestamp(st.st_mtime)
                url = "file:///" + urllib.parse.quote(p.replace("\\", "/"), safe="/:")
                pv = preview(p)
                np_ = note_path(fn)
                body = [
                    "---",
                    "төрөл: inbox",
                    "төлөв: ангилаагүй",
                    "огноо: %s" % datetime.date.today().isoformat(),
                    'эх: "%s"' % p.replace("\\", "/"),
                    "tags: [inbox, файл]",
                    "---",
                    "# %s" % fn,
                    "",
                    "- 📎 [%s](%s)" % (fn, url),
                    "- Хавтас: `%s`" % os.path.relpath(dp, root) if dp != root else "- Хавтас: `%s`" % root,
                    "- Хэмжээ: %s · Өөрчилсөн: %s" % (size(st.st_size), mt.strftime("%Y-%m-%d %H:%M")),
                ]
                if pv:
                    body += ["", "## Эхний хэсэг", "", "> " + pv.strip().replace("\n", "\n> ")]
                body += ["", "## Ангилал", "- [ ] task / төсөл / нөөц / хаях"]
                with open(np_, "w", encoding="utf-8") as f:
                    f.write("\n".join(body) + "\n")
                state[p] = {"note": os.path.relpath(np_, VAULT).replace("\\", "/"), "mtime": st.st_mtime,
                            "added": datetime.datetime.now().isoformat(timespec="seconds")}
                new.append(np_)
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1)
    if sys.stdout is None:          # pythonw (Task Scheduler): консолгүй
        return
    sys.stdout.reconfigure(encoding="utf-8")
    print("шинэ: %d" % len(new))
    for p in new:
        print(" ", os.path.relpath(p, VAULT))


if __name__ == "__main__":
    main()
