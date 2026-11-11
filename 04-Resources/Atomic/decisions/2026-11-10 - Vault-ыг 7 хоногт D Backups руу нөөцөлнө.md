---
date: 2026-11-10
type: session-decision
status: active
tags: [decision, backup, хамгаалалт]
ai-first: true
aliases:
  - "Weekly vault backup to D:\\Backups"
areas:
  - "[[03-Areas/AI Team/ai-workers/Architect]] — скрипт, hook-ийн эзэн"
related:
  - "[[04-Resources/references/WeChat файлын PARA индекс]] — ижил өдрийн файлын цэгцлэлт"
---

# Vault-ыг 7 хоногт D:\Backups руу нөөцөлнө

## For future agent

Mugi 2026-11-10-нд хичээлийн хамгаалалтын шалгалтын Х10 (нөөц)-ийн хариуд «D:\Backups, 7 хоногт» гэж шийдэв. Vault `D:\Second brain` нь Drive-д биш, git-гүй тул энэ бол цорын ганц нөөц.

## Шийдвэр

- **Хэн:** Mugi (шийдсэн), GTD сешн (хэрэгжүүлсэн).
- **Юу:** `_system/backup/vault_backup.py` vault-ыг бүтнээр `D:\Backups\SecondBrain-YYYY-MM-DD_HHMM.zip` болгоно; сүүлийн 8-ыг үлдээнэ; `.backups/last-backup.md`-д сүүлийн нөөцийг тэмдэглэнэ.
- **Хэзээ:** Windows Task Scheduler «SecondBrain vault backup» — Ням гариг 20:00; компьютер унтраастай байсан бол дараа асмагц (StartWhenAvailable).
- **Яагаад:** vault 61 MB, нэг диск дээр, хувилбарын түүхгүй — алдагдвал сэргээх эх байхгүй.
- **Буцааж болох уу:** тийм — Task Scheduler-ээс устгах, `D:\Backups`-ийг устгахад хангалттай.

## Анхаарах

- `D:\Backups` нь vault-тай **ижил диск** дээр — диск эвдэрвэл хоёулаа алдагдана. Гадаад диск эсвэл Drive руу хуулах нь дараагийн алхам (TBD, Mugi шийднэ).
- Анхны нөөц 2026-11-10 19:19, 19:20 (туршилт) — 1 182 файл, 46 MB.
