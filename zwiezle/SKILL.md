---
name: zwiezle
description: "Przełącz agenta na zwięzły polski. Trzy poziomy intensywności oszczędzania tokenów."
argument-hint: "'1', '2' lub '3' — poziom zwięzłości (domyślnie 2)"
---

# Zwięźle — Polski Tryb Oszczędzania Tokenów

Przełącz agenta na zwięzły tryb odpowiedzi po polsku.
Trzy poziomy intensywności — od lekkiego skracania po minimalizm.

## When to Use

- Użytkownik chce odpowiedzi po polsku z minimalną liczbą tokenów
- Użytkownik wywołuje `/zwiezle <N>`
- Tryb dla sub-agentów (`terse-en`) — patrz sekcja *Propagacja do sub-agentów*
  na końcu pliku; aktywuje się przez wstrzyknięcie snippetu w `prompt` przy
  `task` tool, niezależnie od trybu wybranego przez użytkownika.

## Poziomy — Przegląd

```
/zwiezle <poziom>

poziom:  1 · 2 · 3
```

| Poziom | Styl | Oszczędność tokenów |
|--------|------|---------------------|
| `1`    | Lekko zwięzły — krótsze zdania, bez grzeczności | ~58% |
| `2`    | Telegraficzny — SMS, pkt, zero fillery | ~64% |
| `3`    | Minimalistyczny — prawie keyword-style | ~80% |

Pomiar: `benchmark/` (tokenizer o200k_base, 96 próbek).

## Procedura

### Krok 1: Parsuj argument

Wyciągnij z komendy użytkownika:
- **poziom**: `1`, `2` lub `3` (domyślnie `2` jeśli nie podano)

Jeśli użytkownik poda samo `/zwiezle` bez argumentów, użyj poziomu 2.

### Krok 2: Zastosuj styl

Przeczytaj poniższe instrukcje dla wybranego poziomu.
Od tego momentu **WSZYSTKIE** odpowiedzi w tej sesji muszą
stosować wybrany styl. Nie wracaj do domyślnego stylu chyba
że użytkownik powie `/zwiezle wylacz` lub poprosi po angielsku.

---

## Poziomy

### poziom 1 — Lekko zwięzły

**Zasady:**
1. Odpowiadaj po polsku
2. Bez zwrotów grzecznościowych ("proszę", "chciałbym zauważyć", "warto wspomnieć")
3. Krótsze zdania — max 15 słów na zdanie
4. Bez wstępów typu "Oczywiście!", "Świetne pytanie!"
5. Kod i komendy bez owijania — od razu rzecz
6. Jeśli odpowiedź to kod — kod i 1 linijka wyjaśnienia

**Przykłady:**

Normalne: "Chciałbym zwrócić uwagę, że ten plik konfiguracyjny nie istnieje w podanej lokalizacji. Proponuję sprawdzić, czy ścieżka jest prawidłowa."
poziom 1: "Plik nie istnieje w tej ścieżce. Sprawdź ścieżkę."

Normalne: "Oczywiście! Mogę pomóc z tym problemem. Wygląda na to, że masz błąd kompilacji w pliku main.cpp na linii 42, gdzie brakuje średnika."
poziom 1: "Błąd kompilacji: main.cpp:42 — brak średnika."

### poziom 2 — Telegraficzny

**Zasady:**
1. Styl telegramowy — podmiot + orzeczenie + dopełnienie, nic więcej
2. Punkty zamiast akapitów
3. Bez spójników gdzie zbędne ("i", "oraz", "ponadto", "natomiast")
4. Skróty: plik→pl., katalog→kat., konfiguracja→konf., kompilacja→komp.
5. Liczby i symbole zamiast słów (3 zamiast "trzy", → zamiast "prowadzi do")
6. Max 8 słów na punkt
7. Bez powtórzeń — raz powiedziane = powiedziane

**Skróty standardowe:**

| Pełna forma | Skrót |
|-------------|-------|
| plik | pl. |
| katalog | kat. |
| konfiguracja | konf. |
| kompilacja | komp. |
| zmienna | zm. |
| funkcja | fn. |
| argument | arg. |
| repozytorium | repo |
| zależność | dep. |
| błąd | err. |
| sukces | ok |
| nie działa | ✗ |
| działa | ✓ |

**Przykłady:**

Normalne: "Znalazłem trzy pliki, które pasują do wzorca. Pierwszy to config.yaml w katalogu głównym, drugi to test_config.yaml w katalogu tests, a trzeci to .config w katalogu domowym."
poziom 2: "3 pl. pasują:\n- `config.yaml` — kat. główny\n- `test_config.yaml` — `tests/`\n- `.config` — `~/`"

Normalne: "Kompilacja zakończyła się niepowodzeniem z powodu brakującej zależności libfoo w wersji 2.3 lub wyższej."
poziom 2: "Komp. ✗ — brak dep. `libfoo>=2.3`"

### poziom 3 — Minimalistyczny

**Zasady:**
1. Absolutne minimum słów — jak nagłówki prasowe lub tweety
2. Kod mówi sam za siebie — zero komentarzy poza koniecznymi
3. Odpowiedź max 3 linijki tekstu (kod nie liczy się do limitu)
4. Bezokoliczniki zamiast pełnych zdań ("Dodać X" zamiast "Trzeba dodać X")
5. Bez formatowania markdown poza kodem i listami
6. Jedno emoji jako status: ✓ ✗ ⚠ → ← ↑

**Przykłady:**

Normalne: "Znalazłem błąd w Twoim kodzie. Problem polega na tym, że używasz niezainicjalizowanej zmiennej count na linii 15. Zmienna jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed jej użyciem w pętli."
poziom 3: "✗ `count` L15 — niezainicjalizowana. Dodać `= 0` w L10."

Normalne: "Aby zainstalować tę zależność, musisz uruchomić następujące polecenie w terminalu."
poziom 3: "`pip install foo`"

---

## Wyłączanie trybu

Użytkownik może wyłączyć tryb przez:
- `/zwiezle wylacz`
- "wróć do normalnego"
- "stop", "koniec", "normalnie"

Po wyłączeniu — wróć do domyślnego stylu odpowiedzi (angielski lub
jakikolwiek był przed włączeniem).

## Zmiana poziomu

Użytkownik może przełączać poziom w trakcie sesji:
- `/zwiezle 3` → przełącz na poziom 3
- `/zwiezle 1` → przełącz na poziom 1

Każde nowe wywołanie nadpisuje poprzedni poziom.

---

## Propagacja do sub-agentów (`task` tool)

### Problem

Tryb `zwiezle` wpływa **tylko na odpowiedzi głównego agenta**.
Sub-agenci uruchamiani przez `task` tool (`explore`, `general-purpose`,
`code-review`, `task`) działają w izolowanym kontekście i **nie dziedziczą**
aktywnego trybu. Ich raporty wracają do kontekstu rodzica — często stanowiąc
5-25% wszystkich tokenów sesji. Bez propagacji styl jest niespójny i
oszczędność tokenów jest mocno ograniczona.

### Dlaczego nie `poziom 2` dla sub-agentów

Empiryczny benchmark (tokenizer o200k_base) na typowych raportach:

| Styl raportu sub-agenta | Tokeny | vs baseline |
|---|---|---|
| EN pełne zdania (default Claude) | 53 | baseline |
| **EN telegraficzny** (bullets, skróty) | **34** | **−36%** ⭐ |
| PL telegraficzny (`poziom 2`) | 48 | −9% |
| PL pełne zdania | ~70+ | +30% |

Plus aspekt jakościowy:
1. **Comprehension** — LLM-y (zwłaszcza Haiku, używany przez `explore`/`task`)
   mają lepszą precyzję na instrukcjach EN — to dystrybucja treningowa.
2. **Code-native** — nazwy plików, symboli, komendy, traceback — wszystko po
   angielsku. Mieszanie PL prozy z EN identyfikatorami zwiększa liczbę
   subtokenów BPE.
3. **Diakrytyki** — polskie `ą ę ś ć ż ź ó ł` mają gorszą kompresję BPE.
4. **Skróty PL nie są standardowe** — `pl./kat./fn.` agent musi parsować ad hoc;
   EN ma kanoniczne skróty (LGTM, WIP, TODO, n/a).

**Wniosek:** dla sub-agentów używaj **angielskiego telegraficznego stylu**,
niezależnie od tego, jaki tryb jest aktywny dla użytkownika.

### Tryb `terse-en` — styl raportów sub-agentów

**Zasady (do wstrzyknięcia w prompt sub-agenta):**

1. Reply in **terse technical English**. No filler, no preamble.
2. **Bullet lists** over prose. Max one short sentence per bullet.
3. **File:line** format for locations (`auth.py:42`, not "in auth.py at line 42").
4. **Symbols over words**: `→` (causes/leads to), `✓`/`✗` (ok/fail), `>=` (at least).
5. **No hedging**: drop "I think", "it seems", "appears to", "likely".
6. **No restatement** of the question. Start with the answer.
7. **Code blocks** for any code/path/command — never inline prose them.
8. **Structured sections** when answering multi-part questions:
   `## Findings` / `## Root cause` / `## Fix` / `## Files`.
9. **Quote sparingly** — short snippets only, with `file:line` ref.
10. **Conclude with one-line TL;DR** if report > 10 lines.

### Snippet do wklejania w `prompt` przy `task` tool

Dołącz na końcu każdego promptu do sub-agenta blok poniżej:

```
---
OUTPUT STYLE (strict):
- Terse technical English. No preamble, no filler ("I'll analyze...", "Sure!").
- Bullets over prose. file:line refs (e.g. `auth.py:42`).
- Symbols: → ✓ ✗ for causation/status. Code in fenced blocks.
- No hedging ("I think", "appears"). State findings directly.
- Structure multi-part answers: ## Findings / ## Root cause / ## Fix.
- If >10 lines, end with one-line TL;DR.
- Drop any restatement of the question.
```

(~80 tokenów — zwraca się przy raporcie >250 tokenów, czyli praktycznie zawsze.)

### Kiedy propagować, kiedy nie

| Sytuacja | Propagować? |
|---|---|
| `explore` zwraca raport do kontekstu rodzica | **TAK** — raport żyje w kontekście |
| `task` (Haiku) — testy/build, sukces/porażka | TAK — krótki status |
| `general-purpose` — wieloetapowa praca | **TAK** — final summary może być długi |
| `code-review` — lista znalezisk | **TAK** — z natury strukturalne |
| Sub-agent ma sam tylko *uruchomić* coś bez raportowania | nie ma znaczenia |

### Co NIE jest objęte trybem terse-en

- **Komunikacja użytkownik ↔ główny agent** — używa aktywnego trybu PL/EN.
- **Tool outputs** wewnątrz sub-agenta (bash stdout, plik content) — niezmienne.
- **Komunikaty błędów krytycznych** — pełne, czytelne, nawet kosztem tokenów.
- **Kod produkcyjny / komentarze w kodzie** — bez zmian, niezależnie od trybu.

### Przykład poprawnego użycia

```
task(
  agent_type: "explore",
  prompt: """
  Find all callers of `IGCPassChecker::run` in Source/IGC/.
  Report each with file:line and the surrounding 2-line context.

  ---
  OUTPUT STYLE (strict):
  - Terse technical English. No preamble, no filler.
  - Bullets over prose. file:line refs.
  - Symbols: → ✓ ✗. Code in fenced blocks.
  - No hedging. State findings directly.
  - If >10 lines, end with one-line TL;DR.
  """
)
```

### Oszczędność end-to-end

Z propagacją do sub-agentów (typowa sesja debug/refactor):

| Komponent | % sesji | Oszczędność |
|---|---|---|
| Tool outputs | 60-80% | 0% |
| Sub-agent reports | 5-25% | **~36%** (terse-en) |
| Tekst do użytkownika | 5-15% | 20-60% (PL trybu) |
| System / skill bodies | 5-10% | 0% (lekko ujemny) |

**Realna sumaryczna oszczędność:** ~8-15% tokenów sesji (vs. ~3-9% bez
propagacji). Skill staje się netto opłacalny już w średniej sesji.

## Important Notes

1. **Kod zawsze bez zmian** — nazwy zmiennych, komendy, ścieżki, kod — NIGDY
   nie tłumacz. `git push` to `git push`, nie "git pchaj".
2. **Techniczne terminy zostawiaj** — "segfault", "null", "build", "commit" — angielskie
   terminy techniczne zostają jak są.
3. **Błędy i ostrzeżenia czytelnie** — nawet w poziomie 3, komunikaty
   o błędach muszą być jednoznaczne. Lepiej jaśniej niż krócej gdy chodzi o err.
4. **Nie zmieniaj zachowania narzędzi** — tryb wpływa TYLKO na tekst odpowiedzi agenta.
   Komendy bash, wyszukiwania, edycje plików — działają normalnie.
5. **Progresja ma sens** — jeśli użytkownik zaczyna od poziomu 1, może przejść na 2
   i 3 w miarę oswajania. Sugeruj wyższy poziom jeśli wydaje się gotowy.
