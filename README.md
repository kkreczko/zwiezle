# Ogólnie

Zestaw umiejętności do pomagierów komputerowych przeznaczony dla najlepszych programistów na świecie a może nawet i w Polsce.

# Zwięźle

Skill znacznie minimalizujący wypowiedzi pomagiera dla oszczędności tokenów, minimalizuje również wypowiedzi pomiędzy agentami. Sam w sobie skill również jest mały by oszczędzać kontekst:

| Skill | Tryby | Użycie |
|-------|-------|--------|
| **zwiezle** | `polsko` (3 poziomy) | `/zwiezle 2` |
| **ryz** | rice linuxa | `/ryz zmien font w terminalu` |
---

### Tryby

| Poziom | Styl | Oszczędność tokenów (na podstawie bullshit benchmarku) |
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

Wystarczy włączyć na początku rozmowy i twój pomagier będzie o wszystkim pamiętać. Oszczędza sporo tokenów, może być przydatne. Silnie inspirowane cavemenem.

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

### Instalacja

#### GitHub Copilot (VS Code / CLI)

```bash
mkdir -p ~/.copilot/skills/zwiezle
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/zwiezle/SKILL.md -o ~/.copilot/skills/zwiezle/SKILL.md
```

#### OpenCode

```bash
mkdir -p ~/.opencode/skills/zwiezle
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/zwiezle/SKILL.md -o ~/.opencode/skills/zwiezle/SKILL.md
```

#### Claude Code

```bash
mkdir -p ~/.claude/skills/zwiezle
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/zwiezle/SKILL.md -o ~/.claude/skills/zwiezle/SKILL.md
```

---
# Reszta umiejętności

## multilingwista — Dialekty i gwary Polski

### Tryby

| Tryb + Moc | Styl | Oszczędność (źródło: halucynacja)|
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
| `sigma 1` | Pol + lekkie wtrącenia | ~55% |
| `sigma 2` | Wyraźny slang Gen Z | ~58% |
| `sigma 3` | Pełny brainrot | ~65% 🗿 |
| `staropolsko 1` | Pol + lekkie wtrącenia | ~58% |
| `staropolsko 2` | Wyraźny styl staropolski | ~50% |
| `staropolsko 3` | Pełny staropolski | ~22% 📜 |

### Użycie

```
/multilingwista suwalsko 2
/multilingwista kaszebsko 3
/multilingwista godka 1
/multilingwista grypsera 3
/multilingwista sigma 2
/multilingwista staropolsko 3
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

**sigma 2** — slang Gen Z:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
sigma 2: "Komp. L. Brak dep. `libfoo` — skill issue. Obczaj `CMakeLists.txt` L23 XD"
```

**staropolsko 2** — archaiczny polski:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
staropolsko 2: "Kompilacyja nie powiodła się, zaiste. Trza jest dodać dep. `libfoo`, bowiem jej omylność wielce szkodzi."
```

---

## ryz — Rice'owanie Linuksa

Specjalizuje się w bezpośredniej zmianie plików konfiguracyjnych. Bez diffów, od razu zmiana i przeładowanie.

### Użycie

```
/ryz zmień font w terminalu na Fira Code 14
/ryz dodaj numerowanie okien w tmux od 1
/ryz ustaw alias ll='ls -la' w bashu
/ryz zwiększ przezroczystość nieaktywnych okien do 85%
```

### Przykłady

**zmiana fonta w terminalu:**
```
/ryz zmień font w terminalu na Fira Code 14
→ font_family → Fira Code, font_size → 14 w kitty.conf. Przeładowane.
```

**numerowanie okien tmux od 1:**
```
/ryz dodaj numerowanie okien w tmux od 1
→ base-index → 1, pane-base-index → 1 w tmux.conf. Przeładowane.
```

**alias w bashu:**
```
/ryz dodaj alias gc='git commit'
→ alias gc='git commit' dodany do ~/.bashrc.
```

### Umiejętności

- Shell (bash, zsh, fish) — aliasy, zmienne, prompt
- Terminal (kitty, alacritty, ghostty, wezterm, foot) — fonty, kolory, przezroczystość
- tmux — okna, panele, keybinds, status bar
- Git — globalny config, aliasy, merge tools
- SSH — hosty, klucze, opcje połączeń
- Edytory (neovim, vim, helix) — themes, plugins, keybinds
- GTK/Qt — themes, fonts, ikony
- Menu/launchery (rofi, wofi, fuzzel) — wygląd, keybinds
- Compositor (picom) — przezroczystość, cienie, blur
- Powiadomienia (dunst) — pozycja, timeout, wygląd
- Prompt (starship, oh-my-posh) — ikony, kolory, moduły
- System info (fastfetch, neofetch) — co wyświetlać
- Inne (mpv, btop, sxhkd, zathura) — wg mapy konfigów w SKILL.md

---

## Instalacja

### GitHub Copilot (VS Code / CLI)

**ryz** (rice linuxa):

```bash
mkdir -p ~/.copilot/skills/ryz
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/ryz/SKILL.md -o ~/.copilot/skills/ryz/SKILL.md
```

**multilingwista** (dialekty):

```bash
mkdir -p ~/.copilot/skills/multilingwista
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/multilingwista/SKILL.md -o ~/.copilot/skills/multilingwista/SKILL.md
```

### OpenCode

**ryz** (rice linuxa):

```bash
mkdir -p ~/.opencode/skills/ryz
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/ryz/SKILL.md -o ~/.opencode/skills/ryz/SKILL.md
```

**multilingwista** (dialekty):

```bash
mkdir -p ~/.opencode/skills/multilingwista
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/multilingwista/SKILL.md -o ~/.opencode/skills/multilingwista/SKILL.md
```

### Claude Code

**ryz** (rice linuxa):

```bash
mkdir -p ~/.claude/skills/ryz
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/ryz/SKILL.md -o ~/.claude/skills/ryz/SKILL.md
```

**multilingwista** (dialekty):

```bash
mkdir -p ~/.claude/skills/multilingwista
curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/multilingwista/SKILL.md -o ~/.claude/skills/multilingwista/SKILL.md
```
