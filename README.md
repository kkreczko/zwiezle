# Zwięźle

Zestaw umiejętności oszczędzających tokeny przez zwięzły styl odpowiedzi po polsku.

Dwa skille:

| Skill | Tryby | Użycie |
|-------|-------|--------|
| **zwiezle** | `polsko` (3 poziomy) | `/zwiezle 2` |
| **multilingwista** | `suwalsko`, `kaszebsko`, `godka`, `grypsera` (×3) | `/multilingwista suwalsko 2` |

---

## zwiezle — Zwięzły polski

### Tryby

| Poziom | Styl | Oszczędność tokenów |
|--------|------|---------------------|
| `1` | Lekko zwięzły — krótsze zdania, bez grzeczności | ~58% |
| `2` | Telegraficzny — SMS, pkt, zero fillery | ~64% |
| `3` | Minimalistyczny — prawie keyword-style | ~80% |

### Użycie

```
/zwiezle 2
/zwiezle 3
/zwiezle wylacz
```

### Przykłady

**poziom 1** — krótko i na temat:
```
Normalne: "Chciałbym zwrócić uwagę, że ten plik konfiguracyjny nie istnieje w podanej lokalizacji.
           Proponuję sprawdzić, czy ścieżka jest prawidłowa."
poziom 1: "Plik nie istnieje w tej ścieżce. Sprawdź ścieżkę."
```

**poziom 2** — telegraficzny:
```
Normalne: "Kompilacja zakończyła się niepowodzeniem z powodu brakującej zależności libfoo."
poziom 2: "Komp. ✗ — brak dep. `libfoo>=2.3`"
```

**poziom 3** — minimalistyczny:
```
Normalne: "Aby zainstalować tę zależność, musisz uruchomić następujące polecenie w terminalu."
poziom 3: "`pip install foo`"
```

---

## multilingwista — Dialekty i gwary

### Tryby

| Tryb + Moc | Styl | Oszczędność |
|------------|------|-------------|
| `suwalsko 1` | Pol + lekkie wtrącenia | ~59% |
| `suwalsko 2` | Wyraźna gwara | ~56% |
| `suwalsko 3` | Pełna gwara suwalska | ~42% 🍺 |
| `kaszebsko 1` | Pol + lekkie wtrącenia | ~58% |
| `kaszebsko 2` | Wyraźny kaszubski | ~49% |
| `kaszebsko 3` | Pełny kaszubski | ~25% 🐟 |
| `godka 1` | Pol + lekkie wtrącenia | ~58% |
| `godka 2` | Wyraźny śląski | ~54% |
| `godka 3` | Pełna ślōnskŏ gŏdka | ~27% 🏭 |
| `grypsera 1` | Pol + lekkie wtrącenia | ~52% |
| `grypsera 2` | Wyraźna grypsera | ~54% |
| `grypsera 3` | Pełna grypsera | ~64% 🔒 |

### Użycie

```
/multilingwista suwalsko 2
/multilingwista kaszebsko 3
/multilingwista godka 1
/multilingwista grypsera 3
/multilingwista wylacz
```

### Przykłady

**suwalsko 2** — wyraźna gwara:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
suwalsko 2: "Komp. ni poszła. Trza dodać dep. `libfoo`. Kuknij na `CMakeLists.txt` L23."
```

**kaszebsko 2** — wyraźny kaszubski:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
kaszebsko 2: "Komp. nié pòszła. Mùszi dodac dep. `libfoo`. Zdrzëj na `CMakeLists.txt` L23."
```

**godka 2** — wyraźny śląski:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
godka 2: "Komp. niy poszła. Trza dodać dep. `libfoo`. Wejrzij na `CMakeLists.txt` L23."
```

**grypsera 2** — wyraźna grypsera:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
grypsera 2: "Komp. kicha. Brak dep. `libfoo` — ogarnij. Czaj na `CMakeLists.txt` L23."
```

---

## Instalacja

### GitHub Copilot CLI

```bash
# zwiezle (zwięzły polski)
mkdir -p ~/.copilot/skills/zwiezle && curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/zwiezle/SKILL.md -o ~/.copilot/skills/zwiezle/SKILL.md

# multilingwista (dialekty)
mkdir -p ~/.copilot/skills/multilingwista && curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/multilingwista/SKILL.md -o ~/.copilot/skills/multilingwista/SKILL.md
```

### Claude Code

```bash
# zwiezle (zwięzły polski)
mkdir -p ~/.claude/skills/zwiezle && curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/zwiezle/SKILL.md -o ~/.claude/skills/zwiezle/SKILL.md

# multilingwista (dialekty)
mkdir -p ~/.claude/skills/multilingwista && curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/multilingwista/SKILL.md -o ~/.claude/skills/multilingwista/SKILL.md
```
