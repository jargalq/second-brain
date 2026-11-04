---
төрөл: шийдвэр
type: session-decision
төлөв: идэвхтэй
aliases: [Vault GitHub backup]
tags: [backup, github, git, шийдвэр]
огноо: 2026-11-04
date: 2026-11-04
ai-first: true
---

# Vault-ийг GitHub-д backup хийх

**Шийдвэр:** `D:\Seond brain`-ийг git repo болгож, GitHub-ийн **private** `jargalq/second-brain` repo-д backup хийнэ.

**Хэн:** Backup хийхийг Mugi шийдсэн (2026-11-04). Repo-ийн нэр, `.gitignore`-ийн агуулгыг Claude санал болгосон.

**Яагаад:** Өмнө нь vault-ийн хуулбар байгаагүй. Компьютер эвдэрвэл бүх тэмдэглэл, төслийн материал алга болох эрсдэлтэй байсан.

| Сонголт | Утга |
|---|---|
| Хасагдсан | `04-Resources/library/*.pdf`, `*.epub` (≈80 MB, нэг файл 55.8 MB, зохиогчийн эрхтэй), `.obsidian/workspace*`, `_trash/`, `__pycache__` |
| Орсон | Бусад бүх зүйл: ≈596 файл, 23 MB. Үүнд захиалагчийн docx, pdf (Эн Си Жи Ти, ТБТ гэх мэт) багтана, тиймээс repo заавал private байна |
| Git-ийн нэр | `jargalq`, зөвхөн энэ repo-д (global биш) |
| Нэвтрэлт | Git Credential Manager-т хадгалсан `jargalq` бүртгэл |

**Төлөв (2026-11-04):** Анхны push хийгдсэн → https://github.com/jargalq/second-brain (`main`). Дараагийн backup: `git add -A; git commit -m "..."; git push`.

**Буцааж болох эсэх:** Болно. `.git` хавтсыг устгавал vault хуучин төлөвтөө орно. GitHub-ийн repo-г тусад нь устгана.
