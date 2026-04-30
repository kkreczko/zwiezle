# Zwięźle

Twój Klaudiusz używa zbyt dużo tokenów? Chcesz by mówił w twoim ojczystym języku i był tańszy (lepszy) w użyciu? Ta umiejętność jest idealna dla ciebie.
Zaprzęgnij swojego blaszaka (clankera) do ciężkiej pracy używając /zwiezle i już nie martw się kosztami. Wystarczy użyć skilla na początku rozmowy i twój ~niewo~ asystent będzie o tym pamiętać.

## Tryby

Klaudiusz może pracować w kilku trybach.

| Tryb | Styl | Oszczędność tokenów |
|------|------|---------------------|
| `polsko 1` | Lekko zwięzłyi | ~20% |
| `polsko 2` | Telegraficzny | ~40% |
| `polsko 3` | Minimalistyczny | ~60% |
| `suwalsko 1` | Polski + lekkie wtrącenia z gwary | ~10% |
| `suwalsko 2` | Wyraźna gwara — dialekt w połowie słów | ~15% |
| `suwalsko 3` | Pełna gwara suwalska — autentyczny dialekt | vibes 🍺 |

## Użycie

```
/zwiezle polsko 2
/zwiezle suwalsko 3
/zwiezle off
```

## Instalacja

### GitHub Copilot CLI

```bash
mkdir -p ~/.copilot/skills/zwiezle && curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/zwiezle/SKILL.md -o ~/.copilot/skills/zwiezle/SKILL.md
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/zwiezle && curl -fsSL https://raw.githubusercontent.com/kkreczko/zwiezle/main/zwiezle/SKILL.md -o ~/.claude/skills/zwiezle/SKILL.md
```

## Przykłady

**polsko 2:**
```
Normalne: "Kompilacja zakończyła się niepowodzeniem z powodu brakującej zależności libfoo w wersji 2.3 lub wyższej."
polsko 2: "Komp. ✗ — brak dep. `libfoo>=2.3`"
```

**suwalsko 3:**
```
Normalne: "Znalazłem problem. Funkcja na linii 42 zwraca null zamiast pustej tablicy."
suwalsko 3: "Nu, kuknij — bieda na L42. Óna zwraca `null` a trza `[]`."
```
