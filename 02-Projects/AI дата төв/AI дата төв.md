---
төрөл: төсөл
төлөв: судалгаа
date: 2026-11-12
updated: 2026-11-13
type: project
status: planning
project-type: research
area: 
business: internal
scope: mine
accountable: Mugi
responsible: Project agent
context: 
start: 2026-11-12
due: 
income: << энгийн орлого, тоо. Дэлгэрэнгүйг доорх finance жагсаалтаар өг >>
expenses: << энгийн зарлага, тоо >>
finance:
  << Санхүүгийн бичилт бүр: type (invoice|payment|expense|contract) · label · amount (тоо) · status (invoice: sent|paid|overdue; contract: draft|signed) · date · doc ([[файл руу холбоос]], заавал биш). Command Center-ийн Санхүү хэсэгт статустай харагдана. Жишээ: >>
  - type: invoice
    label: << нэхэмжлэхийн нэр >>
    amount: 0
    status: sent
    date: << YYYY-MM-DD >>
    doc:
goal: "Монголд нүүрсний уурхайн хажууд AI дата төв барих боломжийг судалж, судалгааны төлөвлөгөө гаргах"
milestones:
  - label: 8 чиглэлийн урьдчилсан судалгаа
    date: 2026-11-13
    done: true
  - label: Газрын асуудлыг тодруулах (Mugi)
    date:
    done: false
  - label: Бөөрөлжүүтийн эзэдтэй анхны уулзалт
    date:
    done: false
risks:
  - risk: Засгийн газрын бодлого AI дата төвийг сэргээгдэх эрчим хүчтэй, нүүрсийг крипто төвтэй холбож байна
    level: high
    mitigation: Нар, салхи, батарей хосолсон эх үүсвэр; бодлогын хэлэлцүүлэгт оролцох
  - risk: АНУ-ын GPU экспортын лиценз авах зам тодорхойгүй
    level: high
    mitigation: Казахстаны Firebird-ийн жишгийг судлах; colocation загвараар GPU-г түнш авчрах
  - risk: Нүүрсний станцаас ~0.9 сая т CO₂/жил (100 МВт), ESG шаардлагатай үйлчлүүлэгч татгалзах
    level: high
    mitigation: ESG шаардлага багатай үйлчлүүлэгч, нүүрсийг сэргээгдэх эх үүсвэрээр хэсэгчлэн орлуулах
  - risk: Бөөрөлжүүтийн хөрөнгө оруулалтын гэрээ дахин хэлэлцэгдэж байна
    level: med
    mitigation: Гэрээний өөрчлөлтөд дата төвийн хэрэгцээг эрт оруулах
open-questions:
  - Уурхайн тусгай зөвшөөрлийн талбайд дата төвийн газар олгож болох уу? (Mugi)
  - Бөөрөлжүүтийн 3–4-р блокоос дата төвд цахилгаан хуваарилах боломж бий юу?
  - Монголд АНУ-ын GPU-ийн экспортын лиценз авах зам ямар вэ?
  - Зангуу түрээслэгч хэн байж болох вэ?
  - Өгөгдлийн тухай хууль хэзээ, ямар агуулгаар батлагдах вэ?
parent:
subprojects:
related:
tags:
  - project
  - дата-төв
aliases: [AI data center]
ai-first: true
anti-goal:
---

# AI дата төв

> 📋 Ажлын гарын авлага: [[_BRAIN]]

## 📂 Төслийн файлууд (Inbox → Баримт → Output)

> Энэ төслийн хавтасны файлууд шатаар: 📥 Inbox (орж ирсэн), 📄 Баримт (brief, spec, plan), 📤 Output (гаралт). Бүх төслийн нэгдсэн харагдац: [[02-Projects/Project Files.base]].

![[02-Projects/Project Files.base#Энэ төсөл]]

## 📚 Судалгаа ба нөөц

> Энэ төслийн явцад үүссэн судалгаа, лавлагаа, атомууд (`project:`/`projects:` = энэ төсөл), мөн өөр төслүүдээс авч ашиглаж болох судалгаа. Шинэ судалгаа бичихдээ `type: research` (эсвэл `tags: [research]`) ба `project:` холбоосыг заавал тавь → [[04-Resources/Atomic/decisions/2026-10-11 - Төслийн судалгаа нэг base-д цугларна]]

![[04-Resources/Research.base#Энэ төслийн судалгаа]]

![[04-Resources/Research.base#Өөр төслөөс авч болох]]


## 📊 Төслийн тойм

> Энэ төсөлтэй холбоотой бүх зүйл (`project:` / `projects:` = энэ төсөл) төрлөөр нь — task, атом, шийдвэр, судалгаа, лавлагаа. Хавтас биш холбоосоор цуглардаг тул нэг файл олон төсөлд харагдаж болно.

```base
filters:
  or:
    - list(project).contains(this)
    - list(projects).contains(this)
views:
  - type: table
    name: Төрлөөр
    groupBy:
      property: type
      direction: ASC
    order:
      - file.basename
      - status
      - owner
      - date
```

## 🗂 Холбоост харагдацууд

Энэ бол Notion-ы record page шиг амьд самбар. `this` = энэ тэмдэглэл. Таск, баримт, шийдвэр, дэд төсөл нэмэхэд тэдгээрийн frontmatter дахь `project` / `parent` / `projects` холбоосоор нь энд автоматаар гарна. Гараар жагсаах шаардлагагүй.

### 📋 Таскууд

```base
filters:
  and:
    - file.inFolder("01-GTD/Tasks")
    - type == "task"
    - status != "completed"
    - status != "cancelled"
    - list(project).contains(this)
views:
  - type: table
    name: Энэ төслийн таскууд
    order:
      - file.basename
      - status
      - priority
      - due
      - owner
```

### 🔬 Судалгаа

Судалгаа = төслийн эхний шат (design thinking): `04-Resources/Research/`-д Resource хэвээр үлдэж, өөрийн `project:` relation-оор энд гарна — төсөл рүү зөөхгүй.

```base
filters:
  and:
    - file.inFolder("04-Resources/Research")
    - type == "research"
    - list(project).contains(this)
views:
  - type: table
    name: Энэ төслийн судалгаа
    order:
      - file.basename
      - status
      - closed
      - date
```

### 🤝 Уулзалтууд

```base
filters:
  and:
    - type == "meeting"
    - list(project).contains(this)
views:
  - type: table
    name: Энэ төслийн уулзалтууд
    order:
      - file.basename
      - status
      - met
      - scheduled
      - company
```

### 🌿 Дэд төслүүд

```base
filters:
  and:
    - file.inFolder("02-Projects")
    - type == "project"
    - list(parent).contains(this)
views:
  - type: table
    name: Дэд төслүүд
    order:
      - file.basename
      - status
      - area
```

### 📄 Баримтууд

```base
filters:
  and:
    - file.inFolder("02-Projects")
    - type != "project"
    - type != "project-brain"
    - list(project).contains(this)
views:
  - type: table
    name: Баримтууд
    order:
      - file.basename
      - type
      - status
      - date
```

### 🔗 Төслийн мэдлэг (relation)

Notion-ы relation шиг: frontmatter-ийн ганц `related:` жагсаалт; төрөл нь холбогдсон note-ийн `type`-аас. «Яагаад»-ыг note-ийн доод «## 🔗 Холбоос — яагаад» хэсэгт мөр бүрээр. Атом/лавлагаа энэ төсөлд хамаарвал өөрийн `projects:`-д энэ төслийг нэмнэ — хуулж бичихгүй.

```base
filters:
  and:
    - or:
        - file.inFolder("04-Resources")
        - file.inFolder("04-Resources/Atomic")
    - or:
        - list(projects).contains(this)
        - list(this.related).contains(file)
views:
  - type: table
    name: Мэдлэгийн эх (ном, лавлагаа, атом)
    order:
      - file.basename
      - type
      - framework
      - date
```

```base
filters:
  and:
    - file.inFolder("02-Projects")
    - type == "project"
    - file != this
    - or:
        - list(related).contains(this)
        - list(this.related).contains(file)
views:
  - type: table
    name: Холбогдох төслүүд
    order:
      - file.basename
      - status
      - area
```

### 🔑 Шийдвэрүүд

```base
filters:
  and:
    - file.inFolder("04-Resources/Atomic")
    - type == "session-decision"
    - list(projects).contains(this)
views:
  - type: table
    name: Шийдвэрүүд
    order:
      - file.basename
      - changetype
      - status
      - date
```

### 🧠 Атомууд (ойлголт, баримт)

```base
filters:
  and:
    - file.inFolder("04-Resources/Atomic/knowledge")
    - or:
        - list(projects).contains(this)
        - list(project).contains(this)
views:
  - type: table
    name: Атомууд
    order:
      - file.basename
      - kind
      - confidence
      - date
```

### 📎 Лавлагаа ба сэдэв

```base
filters:
  and:
    - or:
        - file.inFolder("04-Resources/references")
        - file.inFolder("04-Resources/Topics")
        - file.inFolder("04-Resources/library")
    - or:
        - list(projects).contains(this)
        - list(project).contains(this)
        - file.hasLink(this.file)
views:
  - type: table
    name: Лавлагаа ба сэдэв
    order:
      - file.basename
      - type
      - date
```

## For future agent

<< Энэ төслийн амьд самбар. Дээрх дөрвөн харагдац холбоосоор автомат шинэчлэгддэг тул таск/баримт/шийдвэрийг гараар бүү жагса. Статик гарын авлага (яагаад байдаг, дуусах шалгуур, юу хийж болохгүй) [[_BRAIN]] дотор. Чиглэл, өмнөх шийдвэр, одоогийн хамрах хүрээгээ эндээс эхэлж ойлго. >>

## Тойм

Монголд нүүрсний уурхайн хажууд AI дата төв барих боломжийн судалгаа. 2026-11-13-ны байдлаар 8 чиглэлийн урьдчилсан судалгаа дууссан. Дүгнэлт: техникийн хувьд боломжтой, эдийн засгийн хувьд нөхцөлтэй, бодлого ба ESG-ийн хувьд хамгийн хэцүү. Байршлын эхний нэр дэвшигч нь Бөөрөлжүүт. Төслийн амжилт эрчим хүчнээс илүү GPU-ийн лиценз, хөрөнгө оруулалт, урт хугацааны түрээслэгчээс шалтгаална (*ажлын дүгнэлт*). Дэлгэрэнгүйг [[Судалгааны нэгдсэн тойм]]-оос үзнэ үү.

**Судалгааны note-ууд:** [[Эрх зүйн орчин - судалгаа]] · [[Эрчим хүч - судалгаа]] · [[Бөөрөлжүүт - судалгаа]] · [[Хөргөлт ба ус - судалгаа]] · [[Хөргөлт - гадны туршлага]] · [[Холболт - судалгаа]] · [[Зах зээл - судалгаа]] · [[Санхүү - судалгаа]] · [[Эрсдэл ба ESG - судалгаа]] · [[Газар ба байгаль орчин - судалгаа]]

## Гол шийдвэр

- 2026-11-13 [[04-Resources/Atomic/decisions/2026-11-13 - AI дата төвийн байршлыг Бөөрөлжүүтээр эхэлж судлах]] - байршлын эхний нэр дэвшигч Бөөрөлжүүт
- 2026-11-13 [[04-Resources/Atomic/knowledge/2026-11-13 - AI дата төвд цахилгаан орлогын 3-5 хувь]] - энэ бол GPU-ийн бизнес
- 2026-11-13 [[04-Resources/Atomic/knowledge/2026-11-13 - Монголын сүлжээнд дата төвд илүүдэл цахилгаан алга]] - өөрийн станц хэрэгтэй
- 2026-11-13 [[04-Resources/Atomic/knowledge/2026-11-13 - АНУ-ын GPU Хятадад төвтэй компанид хаана ч хориотой]] - үйлчлүүлэгчийн хязгаар
- 2026-11-13 [[04-Resources/Atomic/knowledge/2026-11-13 - Уурхайн талбайд дата төв барьж болох уу]] - нээлттэй асуулт (Mugi)
- 2026-11-13 [[04-Resources/Atomic/decisions/2026-11-13 - AI дата төвийн судалгааг дэд сешнээр хийж төсөлд нэгтгэв]] - ажлын урсгал
- 2026-11-13 [[04-Resources/Atomic/knowledge/2026-11-13 - fm_project new нь .obsidian-д CSS snippet бичдэг]] - хэрэгслийн сургамж

## Холбоосууд

- Ажлын гарын авлага: [[_BRAIN]]
- Судалгааны нэгдсэн тойм (2026-11-13): [[Судалгааны нэгдсэн тойм]]
- << бусад холбогдох тэмдэглэл, tool, хүн >>

## 🪐 Гарагууд

- Энэ төслийн task-ууд → [[01-GTD/Tasks/Tasks]] (`project:` талбараар)
- Энэ төслийн атом, шийдвэр → [[04-Resources/Atomic/Atomic]] (`projects:` талбараар)

