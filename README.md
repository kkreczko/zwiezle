# Zwięźle

Twój Klaudiusz używa zbyt dużo tokenów? Chcesz by mówił w twoim ojczystym języku i był tańszy (lepszy) w użyciu? A może nie chcesz żeby gdakał jak gdaka trzy po trzy (pierdolił)? Jeżeli tak to ta umiejętność jest idealna dla ciebie.
Zaprzęgnij swojego blaszaka (clankera) do ciężkiej pracy używając /zwiezle i już nie martw się kosztami. Wystarczy użyć skilla na początku rozmowy i twój ~niewo~ asystent będzie o tym pamiętać.

## Tryby

Klaudiusz może pracować w kilku trybach.

| Tryb | Styl | Oszczędność tokenów |
|------|------|---------------------|
| `polsko 1` | Lekko zwięzły | ~58% |
| `polsko 2` | Telegraficzny | ~64% |
| `polsko 3` | Minimalistyczny | ~80% |
| `suwalsko 1` | Polski + lekkie wtrącenia z gwary | ~59% |
| `suwalsko 2` | Wyraźna gwara — dialekt w połowie słów | ~56% |
| `suwalsko 3` | Pełna gwara suwalska — autentyczny dialekt | ~42% 🍺 |
| `kaszebsko 1` | Polski + lekkie wtrącenia kaszubskie | ~58% |
| `kaszebsko 2` | Wyraźny kaszubski — kaszëbskô mòwa | ~49% |
| `kaszebsko 3` | Pełny kaszubski | ~25% 🐟 |
| `godka 1` | Polski + lekkie wtrącenia śląskie | ~58% |
| `godka 2` | Wyraźny śląski — ślōnskŏ gŏdka | ~54% |
| `godka 3` | Pełna ślōnskŏ gŏdka | ~27% 🏭 |
| `grypsera 1` | Polski + lekkie wtrącenia grypserskie | ~52% |
| `grypsera 2` | Wyraźna grypsera — slang w połowie | ~54% |
| `grypsera 3` | Pełna grypsera — kminisz? | ~64% 🔒 |

## Użycie

```
/zwiezle polsko 2
/zwiezle suwalsko 3
/zwiezle kaszebsko 1
/zwiezle godka 2
/zwiezle grypsera 3
/zwiezle wylacz
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

**polsko 1** — krótko i na temat:
```
Normalne: "Chciałbym zwrócić uwagę, że ten plik konfiguracyjny nie istnieje w podanej lokalizacji.
           Proponuję sprawdzić, czy ścieżka jest prawidłowa."
polsko 1: "Plik nie istnieje w tej ścieżce. Sprawdź ścieżkę."
```

**polsko 2** — telegraficzny:
```
Normalne: "Kompilacja zakończyła się niepowodzeniem z powodu brakującej zależności libfoo w wersji 2.3 lub wyższej."
polsko 2: "Komp. ✗ — brak dep. `libfoo>=2.3`"
```

**polsko 3** — minimalistyczny:
```
Normalne: "Aby zainstalować tę zależność, musisz uruchomić następujące polecenie w terminalu."
polsko 3: "`pip install foo`"
```

**suwalsko 2** — wyraźna gwara:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
suwalsko 2: "Komp. ni poszła. Trza dodać dep. `libfoo`. Kuknij na `CMakeLists.txt` L23."
```

**suwalsko 3** — pełna gwara suwalska:
```
Normalne: "Znalazłem problem. Funkcja na linii 42 zwraca null zamiast pustej tablicy."
suwalsko 3: "Nu, kuknij — bieda na L42. Óna zwraca `null` a trza `[]`.
             Jeno zmienić `return null` → `return []` dy będzie dobrza."
```

**kaszebsko 2** — wyraźny kaszubski:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
kaszebsko 2: "Komp. nié pòszła. Mùszi dodac dep. `libfoo`. Zdrzëj na `CMakeLists.txt` L23."
```

**kaszebsko 3** — pełny kaszëbsczi:
```
Normalne: "Znalazłem problem. Funkcja na linii 42 zwraca null zamiast pustej tablicy.
           Trzeba zmienić return null na return []."
kaszebsko 3: "Zdrzëj — fela na L42. Òna wrôcô `null` a mùszi `[]`.
              Le zmienic `return null` → `return []` ë bãdze bëlno."
```

**godka 2** — wyraźny śląski:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
godka 2: "Komp. niy poszła. Trza dodać dep. `libfoo`. Wejrzij na `CMakeLists.txt` L23."
```

**godka 3** — pełna ślōnskŏ gŏdka:
```
Normalne: "Znalazłem problem. Funkcja na linii 42 zwraca null zamiast pustej tablicy.
           Trzeba zmienić return null na return []."
godka 3: "Wejrzij — feler na L42. Łōna wrŏcŏ `null` a trza `[]`.
           Ino zmiyń `return null` → `return []` i bydzie gryfnie."
```

**grypsera 2** — wyraźna grypsera:
```
Normalne: "Kompilacja nie powiodła się. Trzeba dodać brakującą zależność libfoo."
grypsera 2: "Komp. kicha. Brak dep. `libfoo` — ogarnij. Czaj na `CMakeLists.txt` L23."
```

**grypsera 3** — pełna grypsera:
```
Normalne: "Znalazłem problem. Funkcja na linii 42 zwraca null zamiast pustej tablicy.
           Trzeba zmienić return null na return []."
grypsera 3: "Czaj — kicha na L42. Łona zwraca `null` a trza `[]`.
             Ogarnij `return null` → `return []` i gitówa."
```
