---
төрөл: tool
type: tool
төлөв: идэвхтэй
date: 2026-11-06
updated: 2026-11-06
url: "https://mail.google.com"
tags: [tool, gmail, PARA]
ai-first: true
---

# Gmail (q.munkhjargal@gmail.com)

**Энэ юу вэ:** Gmail-ийн label, filter-ийг vault-ын PARA хавтастай ижил бүтцээр цэгцэлсэн тайлбар. Шийдвэр: [[2026-11-06 - Gmail PARA label бүтэц]].

**Гол дүрэм:** label-тай мэйл бүр Inbox-ийг алгасаж label дотроо очно. Inbox-д зөвхөн label-гүй, ангилагдаагүй мэйл үлдэнэ.

## Label бүтэц

| Label | Юу орно | Vault-ын гэр |
|---|---|---|
| `02-Projects/Голден погада ХХК` | @goldenpogada.mn | [[02-Projects/Ажил/Голден погада ХХК]] |
| `02-Projects/Тодбум ХХК` | «todbum / тодбум» үгтэй мэйл | [[02-Projects/Ажил/Тодбум ХХК]] |
| `02-Projects/Төвийн бүсийн цогцолбор` | industrialcomplex.cr@gmail.com | `02-Projects/Ажил/Төвийн бүсийн ... ТӨХХК` |
| `02-Projects/Грийтвишн ХХК` | Даваа, Даваанямаа, Арьяабал, @greatvision.mn | [[02-Projects/Грийтвишн ХХК]] |
| `02-Projects/Second Brain Season 2` | way-academy-season-2, Way Academy | [[02-Projects/Second Brain Season 2]] |
| `02-Projects/Ажил` | Vault-д хавтасгүй захиалагч: Голдман, Terra Mind, Nomin Gmining, Minevision, Соёолон, Өмнөговь | [[02-Projects/Ажил]] |
| `03-Areas/Business/Tax` | Татварын газар (@mta.mn), бүх компанийн | `03-Areas/Business` |
| `03-Areas/Life/Banks` | Хаан банк, ХасБанк, MostMoney, Капитрон банк | `03-Areas/Life` |
| `03-Areas/Tools` | Нэвтрэх код, аюулгүй байдлын мэдэгдэл | `03-Areas/Tools` |
| `04-Resources/sources` | Мэдээллийн хуудас (NetPicks, academia, Wikiloc) | `04-Resources/sources` |
| `99-Archive` | Дууссан төслийн label-ийг энд зөөнө | `99-Archive` |

## Filter

Бүгд **Skip the Inbox**-тэй. Эх файл: [[gmail-filters.xml]] — Gmail → Settings → Filters → **Import filters**-ээр нэг дор оруулна.

| # | Нөхцөл | Label |
|---|---|---|
| 1 | From `@goldenpogada.mn` | Голден погада ХХК |
| 2 | Has the words `todbum OR тодбум` | Тодбум ХХК |
| 3 | From `industrialcomplex.cr@gmail.com` | Төвийн бүсийн цогцолбор |
| 4 | From `davaam4321@gmail.com OR davaanyam.gv@gmail.com OR ariyabal.gv@gmail.com OR @greatvision.mn` | Грийтвишн ХХК |
| 5 | Has the words `way-academy-season-2 OR "Way Academy"` | Second Brain Season 2 |
| 6 | From `@goldman.mn OR nyamochir.goldman@gmail.com OR terramind.2017@gmail.com OR nomingmining@gmail.com OR minevisionminingresources@gmail.com OR @soyolon.mn OR @omnogovi.gov.mn` | Ажил |
| 7 | From `ebarimt@xacbank.mn OR digitalbank@xacbank.mn` | Life/Banks |
| 8 | From `noreply-accounts@google.com OR no-reply@accounts.google.com OR no-reply@google.com OR noreply@github.com OR account-security-noreply@accountprotection.microsoft.com OR notifications@vercel.com OR security@mail.instagram.com OR no-reply@itc.gov.mn` | Tools |
| 9 | From `netpicks@mail.beehiiv.com OR updates@academia-mail.com OR noreply@wikiloc.com` | sources |
| 10 | From `temu@shop.temuemail.com OR admin@iymcompetitions.org OR team@framer.com` | (label-гүй, зөвхөн Inbox алгасна) |
| 11 | From `@mta.mn` | Business/Tax |

Gmail-д үүнээс гадна банкны хуучин 5 filter бий (noreply.ebank@khanbank.com, noreply@khanbank.com, internetbank@xacbank.mn, service@mostmoney.mn, tsakhimbank@capitronbank.mn → Skip Inbox + Banks).

## Хэрхэн хөтлөх

- **Шинэ захиалагч:** `02-Projects/<нэр>` label үүсгээд filter-т илгээгчийн домэйныг нэмнэ. Vault-д хавтас нээгдсэн бол `Ажил` filter-ээс тэр хаягийг хасна.
- **Төсөл дуусахад:** label-ийг edit хийж «Nest under: 99-Archive» болгоно (мэйл хэвээр үлдэнэ).
- **Filter өөрчлөх:** [[gmail-filters.xml]]-ийг засаад, Gmail дээрх хуучин filter-ийг устгаж, файлаа дахин импортлоно.
- **Inbox-д label-тай мэйл үлдсэн эсэх:** `in:inbox has:userlabels` гэж хайна; гарвал бүгдийг сонгоод **E** (Archive).
- **Анхаар:** `99-Archive` label ≠ Archive товч. Inbox-оос гаргахдаа Archive товч (E) ашиглана.

## Claude-ийн хязгаар

Claude-ийн Gmail коннектор хайх, унших эрхтэй ч label үүсгэх, мэйлд label оноох, архивлах (`create_label`, `label_thread` → «additional permissions» алдаа), filter унших боломжгүй (2026-11-06, дахин холбосны дараа ч). Тиймээс Gmail дээрх өөрчлөлтийг Mugi гараар хийж, Claude `list_labels`, хайлтаар шалгана.

## Түүх

- **2026-11-06:** Хуучин `Project`, `Notes`, `A Companies`, `Banks` label-ийг доторх мэйлтэй нь устгав (Trash хоосорсон). PARA label-уудыг Mugi гараар үүсгэв. Хуучин мэйлийг оноож (Грийтвишн 38, Ажил 13, Голден погада 5, Тодбум 3, Second Brain 3, Төвийн бүс 2, sources 5, Tools 12), label-тай 58 thread-ийг Inbox-оос архивлав. Анх оруулсан filter-үүд Gmail-д хадгалагдаагүй байсныг илрүүлж, xml-ээр 10 filter импортлов. Дараа нь `Business/Tax` нэмж, Tools-ийг ч Inbox-оос гаргахаар шийдэв.
