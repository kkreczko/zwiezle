"""
Hardcoded próbki odpowiedzi: normalna (verbose) vs każdy tryb zwięźle.
6 kategorii × 7 trybów = 42 pary.
"""

# Każda próbka: (category, mode, normal_text, terse_text)
# Kategorie: short_error, short_notfound, mid_explain, mid_install, long_review, long_arch

SAMPLES: list[tuple[str, str, str, str]] = [
    # =========================================================================
    # KATEGORIA 1: short_error — krótka odpowiedź o błędzie kompilacji
    # =========================================================================
    (
        "short_error",
        "polsko1",
        "Chciałbym zwrócić uwagę, że wystąpił błąd kompilacji w pliku main.cpp na linii 42. "
        "Wygląda na to, że brakuje średnika na końcu instrukcji. "
        "Proponuję dodać średnik po wyrażeniu i spróbować skompilować ponownie.",
        "Błąd kompilacji: main.cpp:42 — brak średnika. Dodaj i przekompiluj.",
    ),
    (
        "short_error",
        "polsko2",
        "Chciałbym zwrócić uwagę, że wystąpił błąd kompilacji w pliku main.cpp na linii 42. "
        "Wygląda na to, że brakuje średnika na końcu instrukcji. "
        "Proponuję dodać średnik po wyrażeniu i spróbować skompilować ponownie.",
        "Komp. ✗ `main.cpp:42` — brak `;`\n- dodać → rekomp.",
    ),
    (
        "short_error",
        "polsko3",
        "Chciałbym zwrócić uwagę, że wystąpił błąd kompilacji w pliku main.cpp na linii 42. "
        "Wygląda na to, że brakuje średnika na końcu instrukcji. "
        "Proponuję dodać średnik po wyrażeniu i spróbować skompilować ponownie.",
        "✗ `main.cpp:42` brak `;`",
    ),
    (
        "short_error",
        "suwalsko1",
        "Chciałbym zwrócić uwagę, że wystąpił błąd kompilacji w pliku main.cpp na linii 42. "
        "Wygląda na to, że brakuje średnika na końcu instrukcji. "
        "Proponuję dodać średnik po wyrażeniu i spróbować skompilować ponownie.",
        "Jo, błąd kompilacji w main.cpp:42 — ni ma średnika. Dodaj i przekompiluj.",
    ),
    (
        "short_error",
        "suwalsko2",
        "Chciałbym zwrócić uwagę, że wystąpił błąd kompilacji w pliku main.cpp na linii 42. "
        "Wygląda na to, że brakuje średnika na końcu instrukcji. "
        "Proponuję dodać średnik po wyrażeniu i spróbować skompilować ponownie.",
        "Nu, komp. ni poszła — `main.cpp:42` ni ma `;`. Trza dodać dy rekomp.",
    ),
    (
        "short_error",
        "suwalsko3",
        "Chciałbym zwrócić uwagę, że wystąpił błąd kompilacji w pliku main.cpp na linii 42. "
        "Wygląda na to, że brakuje średnika na końcu instrukcji. "
        "Proponuję dodać średnik po wyrażeniu i spróbować skompilować ponownie.",
        "Nu, kuknij — bieda na `main.cpp:42`. Ni ma `;` dy ón ni komp. Jeno dodać dy będzie dobrza.",
    ),
    (
        "short_error",
        "terse-en",
        "Chciałbym zwrócić uwagę, że wystąpił błąd kompilacji w pliku main.cpp na linii 42. "
        "Wygląda na to, że brakuje średnika na końcu instrukcji. "
        "Proponuję dodać średnik po wyrażeniu i spróbować skompilować ponownie.",
        "✗ `main.cpp:42` — missing `;`",
    ),

    # =========================================================================
    # KATEGORIA 2: short_notfound — plik nie istnieje
    # =========================================================================
    (
        "short_notfound",
        "polsko1",
        "Niestety, ten plik konfiguracyjny nie istnieje w podanej lokalizacji. "
        "Sprawdziłem katalog /etc/app/ i nie znalazłem pliku config.yaml. "
        "Możliwe, że ścieżka jest nieprawidłowa lub plik nie został jeszcze utworzony.",
        "Plik config.yaml nie istnieje w /etc/app/. Sprawdź ścieżkę lub utwórz plik.",
    ),
    (
        "short_notfound",
        "polsko2",
        "Niestety, ten plik konfiguracyjny nie istnieje w podanej lokalizacji. "
        "Sprawdziłem katalog /etc/app/ i nie znalazłem pliku config.yaml. "
        "Możliwe, że ścieżka jest nieprawidłowa lub plik nie został jeszcze utworzony.",
        "`config.yaml` ✗ w `/etc/app/`\n- zła ścieżka? lub nie utworzony",
    ),
    (
        "short_notfound",
        "polsko3",
        "Niestety, ten plik konfiguracyjny nie istnieje w podanej lokalizacji. "
        "Sprawdziłem katalog /etc/app/ i nie znalazłem pliku config.yaml. "
        "Możliwe, że ścieżka jest nieprawidłowa lub plik nie został jeszcze utworzony.",
        "✗ `/etc/app/config.yaml` nie istnieje",
    ),
    (
        "short_notfound",
        "suwalsko1",
        "Niestety, ten plik konfiguracyjny nie istnieje w podanej lokalizacji. "
        "Sprawdziłem katalog /etc/app/ i nie znalazłem pliku config.yaml. "
        "Możliwe, że ścieżka jest nieprawidłowa lub plik nie został jeszcze utworzony.",
        "Ni ma config.yaml w /etc/app/. Sprawdź ścieżkę albo utwórz go.",
    ),
    (
        "short_notfound",
        "suwalsko2",
        "Niestety, ten plik konfiguracyjny nie istnieje w podanej lokalizacji. "
        "Sprawdziłem katalog /etc/app/ i nie znalazłem pliku config.yaml. "
        "Możliwe, że ścieżka jest nieprawidłowa lub plik nie został jeszcze utworzony.",
        "Kuknij — ni ma `config.yaml` w `/etc/app/`. Abo ścieżka zła, abo ni utworzony.",
    ),
    (
        "short_notfound",
        "suwalsko3",
        "Niestety, ten plik konfiguracyjny nie istnieje w podanej lokalizacji. "
        "Sprawdziłem katalog /etc/app/ i nie znalazłem pliku config.yaml. "
        "Możliwe, że ścieżka jest nieprawidłowa lub plik nie został jeszcze utworzony.",
        "Nu, nika ni ma — `config.yaml` ni siedzi w `/etc/app/`. Abo ścieżka ni ta, abo trza dopiro zrabić.",
    ),
    (
        "short_notfound",
        "terse-en",
        "Niestety, ten plik konfiguracyjny nie istnieje w podanej lokalizacji. "
        "Sprawdziłem katalog /etc/app/ i nie znalazłem pliku config.yaml. "
        "Możliwe, że ścieżka jest nieprawidłowa lub plik nie został jeszcze utworzony.",
        "✗ `/etc/app/config.yaml` not found. Check path or create it.",
    ),

    # =========================================================================
    # KATEGORIA 3: mid_explain — wyjaśnienie problemu z kodem
    # =========================================================================
    (
        "mid_explain",
        "polsko1",
        "Znalazłem problem w Twoim kodzie. Na linii 15 pliku utils.py używasz zmiennej count, "
        "która jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed "
        "jej użyciem w pętli for. To powoduje, że Python zgłasza UnboundLocalError, ponieważ "
        "zmienna istnieje w lokalnym scope funkcji, ale nie ma przypisanej wartości. "
        "Rozwiązaniem jest dodanie inicjalizacji count = 0 przed pętlą na linii 10.",
        "Problem: utils.py:15 — count użyta bez inicjalizacji. "
        "Deklaracja na L10 bez wartości → UnboundLocalError w pętli. "
        "Rozwiązanie: dodaj count = 0 przed pętlą.",
    ),
    (
        "mid_explain",
        "polsko2",
        "Znalazłem problem w Twoim kodzie. Na linii 15 pliku utils.py używasz zmiennej count, "
        "która jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed "
        "jej użyciem w pętli for. To powoduje, że Python zgłasza UnboundLocalError, ponieważ "
        "zmienna istnieje w lokalnym scope funkcji, ale nie ma przypisanej wartości. "
        "Rozwiązaniem jest dodanie inicjalizacji count = 0 przed pętlą na linii 10.",
        "Err: `utils.py:15` — zm. `count` bez init\n"
        "- dekl. L10, brak wartości → `UnboundLocalError`\n"
        "- fix: `count = 0` przed pętlą",
    ),
    (
        "mid_explain",
        "polsko3",
        "Znalazłem problem w Twoim kodzie. Na linii 15 pliku utils.py używasz zmiennej count, "
        "która jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed "
        "jej użyciem w pętli for. To powoduje, że Python zgłasza UnboundLocalError, ponieważ "
        "zmienna istnieje w lokalnym scope funkcji, ale nie ma przypisanej wartości. "
        "Rozwiązaniem jest dodanie inicjalizacji count = 0 przed pętlą na linii 10.",
        "✗ `count` L15 — niezainicjalizowana. Dodać `= 0` w L10.",
    ),
    (
        "mid_explain",
        "suwalsko1",
        "Znalazłem problem w Twoim kodzie. Na linii 15 pliku utils.py używasz zmiennej count, "
        "która jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed "
        "jej użyciem w pętli for. To powoduje, że Python zgłasza UnboundLocalError, ponieważ "
        "zmienna istnieje w lokalnym scope funkcji, ale nie ma przypisanej wartości. "
        "Rozwiązaniem jest dodanie inicjalizacji count = 0 przed pętlą na linii 10.",
        "Problem w utils.py:15 — count ni ma wartości początkowej. "
        "Jest deklaracja na L10 ale bez init, jo i leci UnboundLocalError. "
        "Dodaj count = 0 przed pętlą.",
    ),
    (
        "mid_explain",
        "suwalsko2",
        "Znalazłem problem w Twoim kodzie. Na linii 15 pliku utils.py używasz zmiennej count, "
        "która jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed "
        "jej użyciem w pętli for. To powoduje, że Python zgłasza UnboundLocalError, ponieważ "
        "zmienna istnieje w lokalnym scope funkcji, ale nie ma przypisanej wartości. "
        "Rozwiązaniem jest dodanie inicjalizacji count = 0 przed pętlą na linii 10.",
        "Kuknij — bieda w `utils.py:15`. Zm. `count` deklarowana na L10 ale ni ma wartości, "
        "dy léci `UnboundLocalError`. Trza dopisać `count = 0` przed pętlą.",
    ),
    (
        "mid_explain",
        "suwalsko3",
        "Znalazłem problem w Twoim kodzie. Na linii 15 pliku utils.py używasz zmiennej count, "
        "która jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed "
        "jej użyciem w pętli for. To powoduje, że Python zgłasza UnboundLocalError, ponieważ "
        "zmienna istnieje w lokalnym scope funkcji, ale nie ma przypisanej wartości. "
        "Rozwiązaniem jest dodanie inicjalizacji count = 0 przed pętlą na linii 10.",
        "Nu, poźri — `utils.py:15` wielga bieda. Ón tam `count` używa a óna ni ma wartości "
        "bo na L10 jeno deklaracja bez nika. Dy léci `UnboundLocalError`. "
        "Trza jeno dopisać `count = 0` przód pętlą dy będzie dobrza.",
    ),
    (
        "mid_explain",
        "terse-en",
        "Znalazłem problem w Twoim kodzie. Na linii 15 pliku utils.py używasz zmiennej count, "
        "która jest deklarowana na linii 10, ale nigdy nie otrzymuje wartości początkowej przed "
        "jej użyciem w pętli for. To powoduje, że Python zgłasza UnboundLocalError, ponieważ "
        "zmienna istnieje w lokalnym scope funkcji, ale nie ma przypisanej wartości. "
        "Rozwiązaniem jest dodanie inicjalizacji count = 0 przed pętlą na linii 10.",
        "- `utils.py:15` — `count` used uninitialized\n"
        "- Declared L10 without value → `UnboundLocalError`\n"
        "- Fix: add `count = 0` before loop",
    ),

    # =========================================================================
    # KATEGORIA 4: mid_install — instrukcja instalacji
    # =========================================================================
    (
        "mid_install",
        "polsko1",
        "Aby zainstalować tę aplikację, musisz wykonać następujące kroki. Po pierwsze, "
        "upewnij się, że masz zainstalowany Python w wersji 3.10 lub wyższej. Następnie "
        "sklonuj repozytorium za pomocą komendy git clone. Potem przejdź do katalogu projektu "
        "i utwórz wirtualne środowisko za pomocą python -m venv .venv. Aktywuj środowisko "
        "za pomocą source .venv/bin/activate. Na końcu zainstaluj zależności komendą "
        "pip install -r requirements.txt. Po tych krokach aplikacja powinna być gotowa do uruchomienia.",
        "Wymagania: Python >= 3.10. Instalacja:\n"
        "1. git clone <repo>\n"
        "2. cd <project>\n"
        "3. python -m venv .venv\n"
        "4. source .venv/bin/activate\n"
        "5. pip install -r requirements.txt",
    ),
    (
        "mid_install",
        "polsko2",
        "Aby zainstalować tę aplikację, musisz wykonać następujące kroki. Po pierwsze, "
        "upewnij się, że masz zainstalowany Python w wersji 3.10 lub wyższej. Następnie "
        "sklonuj repozytorium za pomocą komendy git clone. Potem przejdź do katalogu projektu "
        "i utwórz wirtualne środowisko za pomocą python -m venv .venv. Aktywuj środowisko "
        "za pomocą source .venv/bin/activate. Na końcu zainstaluj zależności komendą "
        "pip install -r requirements.txt. Po tych krokach aplikacja powinna być gotowa do uruchomienia.",
        "Python>=3.10. Kroki:\n"
        "- `git clone` → `cd` proj\n"
        "- `python -m venv .venv && source .venv/bin/activate`\n"
        "- `pip install -r requirements.txt`",
    ),
    (
        "mid_install",
        "polsko3",
        "Aby zainstalować tę aplikację, musisz wykonać następujące kroki. Po pierwsze, "
        "upewnij się, że masz zainstalowany Python w wersji 3.10 lub wyższej. Następnie "
        "sklonuj repozytorium za pomocą komendy git clone. Potem przejdź do katalogu projektu "
        "i utwórz wirtualne środowisko za pomocą python -m venv .venv. Aktywuj środowisko "
        "za pomocą source .venv/bin/activate. Na końcu zainstaluj zależności komendą "
        "pip install -r requirements.txt. Po tych krokach aplikacja powinna być gotowa do uruchomienia.",
        "```bash\ngit clone <repo> && cd <proj>\n"
        "python -m venv .venv && source .venv/bin/activate\n"
        "pip install -r requirements.txt\n```",
    ),
    (
        "mid_install",
        "suwalsko1",
        "Aby zainstalować tę aplikację, musisz wykonać następujące kroki. Po pierwsze, "
        "upewnij się, że masz zainstalowany Python w wersji 3.10 lub wyższej. Następnie "
        "sklonuj repozytorium za pomocą komendy git clone. Potem przejdź do katalogu projektu "
        "i utwórz wirtualne środowisko za pomocą python -m venv .venv. Aktywuj środowisko "
        "za pomocą source .venv/bin/activate. Na końcu zainstaluj zależności komendą "
        "pip install -r requirements.txt. Po tych krokach aplikacja powinna być gotowa do uruchomienia.",
        "Trza mieć Python >= 3.10. Jo i lecim:\n"
        "1. git clone <repo>\n"
        "2. cd <project>\n"
        "3. python -m venv .venv\n"
        "4. source .venv/bin/activate\n"
        "5. pip install -r requirements.txt\n"
        "Terazy gotowe.",
    ),
    (
        "mid_install",
        "suwalsko2",
        "Aby zainstalować tę aplikację, musisz wykonać następujące kroki. Po pierwsze, "
        "upewnij się, że masz zainstalowany Python w wersji 3.10 lub wyższej. Następnie "
        "sklonuj repozytorium za pomocą komendy git clone. Potem przejdź do katalogu projektu "
        "i utwórz wirtualne środowisko za pomocą python -m venv .venv. Aktywuj środowisko "
        "za pomocą source .venv/bin/activate. Na końcu zainstaluj zależności komendą "
        "pip install -r requirements.txt. Po tych krokach aplikacja powinna być gotowa do uruchomienia.",
        "Trza Python>=3.10. Nu, lecim:\n"
        "- `git clone` dy `cd` do kat.\n"
        "- `python -m venv .venv` → `source .venv/bin/activate`\n"
        "- `pip install -r requirements.txt`\n"
        "Dobrza, gotowe.",
    ),
    (
        "mid_install",
        "suwalsko3",
        "Aby zainstalować tę aplikację, musisz wykonać następujące kroki. Po pierwsze, "
        "upewnij się, że masz zainstalowany Python w wersji 3.10 lub wyższej. Następnie "
        "sklonuj repozytorium za pomocą komendy git clone. Potem przejdź do katalogu projektu "
        "i utwórz wirtualne środowisko za pomocą python -m venv .venv. Aktywuj środowisko "
        "za pomocą source .venv/bin/activate. Na końcu zainstaluj zależności komendą "
        "pip install -r requirements.txt. Po tych krokach aplikacja powinna być gotowa do uruchomienia.",
        "Nu, pierwiéj kuknij czy Python>=3.10 siedzi. Jo? To lecim:\n"
        "- `git clone` dy pajść do kat.\n"
        "- `python -m venv .venv` — haj zrobi venv\n"
        "- `source .venv/bin/activate` dy `pip install -r requirements.txt`\n"
        "Terazy dobrza, gotowe do odpalenia.",
    ),
    (
        "mid_install",
        "terse-en",
        "Aby zainstalować tę aplikację, musisz wykonać następujące kroki. Po pierwsze, "
        "upewnij się, że masz zainstalowany Python w wersji 3.10 lub wyższej. Następnie "
        "sklonuj repozytorium za pomocą komendy git clone. Potem przejdź do katalogu projektu "
        "i utwórz wirtualne środowisko za pomocą python -m venv .venv. Aktywuj środowisko "
        "za pomocą source .venv/bin/activate. Na końcu zainstaluj zależności komendą "
        "pip install -r requirements.txt. Po tych krokach aplikacja powinna być gotowa do uruchomienia.",
        "Requires Python >=3.10.\n"
        "```bash\n"
        "git clone <repo> && cd <proj>\n"
        "python -m venv .venv && source .venv/bin/activate\n"
        "pip install -r requirements.txt\n"
        "```",
    ),

    # =========================================================================
    # KATEGORIA 5: long_review — podsumowanie code review
    # =========================================================================
    (
        "long_review",
        "polsko1",
        "Przeprowadziłem przegląd kodu w tym pull requeście i mam kilka uwag. Po pierwsze, "
        "w pliku auth.py na linii 23 tworzysz token JWT bez ustawienia czasu wygaśnięcia, "
        "co jest poważnym problemem bezpieczeństwa, ponieważ token będzie ważny w nieskończoność. "
        "Po drugie, w pliku database.py na linii 45 masz SQL query budowane przez konkatenację "
        "stringów zamiast użycia parametryzowanych zapytań, co naraża aplikację na SQL injection. "
        "Po trzecie, w pliku routes.py na linii 67 brakuje walidacji inputu od użytkownika — "
        "pole email nie jest sprawdzane pod kątem poprawności formatu. Po czwarte, testy w pliku "
        "test_auth.py pokrywają tylko happy path, brakuje testów dla błędnych danych wejściowych "
        "i edge cases. Na końcu chciałbym zauważyć, że plik config.py zawiera zahardkodowane "
        "hasło do bazy danych na linii 12, co absolutnie nie powinno znaleźć się w repozytorium. "
        "Ogólnie kod wymaga poprawek przed mergem.",
        "Przegląd PR — 5 problemów:\n\n"
        "1. auth.py:23 — JWT bez expiration. Problem bezpieczeństwa, token ważny nieskończenie.\n"
        "2. database.py:45 — SQL budowany konkatenacją. Użyj parametryzowanych zapytań (SQL injection).\n"
        "3. routes.py:67 — brak walidacji email.\n"
        "4. test_auth.py — tylko happy path, brak testów edge cases.\n"
        "5. config.py:12 — zahardkodowane hasło do bazy. Wynieś do env vars.\n\n"
        "Wymaga poprawek przed merge.",
    ),
    (
        "long_review",
        "polsko2",
        "Przeprowadziłem przegląd kodu w tym pull requeście i mam kilka uwag. Po pierwsze, "
        "w pliku auth.py na linii 23 tworzysz token JWT bez ustawienia czasu wygaśnięcia, "
        "co jest poważnym problemem bezpieczeństwa, ponieważ token będzie ważny w nieskończoność. "
        "Po drugie, w pliku database.py na linii 45 masz SQL query budowane przez konkatenację "
        "stringów zamiast użycia parametryzowanych zapytań, co naraża aplikację na SQL injection. "
        "Po trzecie, w pliku routes.py na linii 67 brakuje walidacji inputu od użytkownika — "
        "pole email nie jest sprawdzane pod kątem poprawności formatu. Po czwarte, testy w pliku "
        "test_auth.py pokrywają tylko happy path, brakuje testów dla błędnych danych wejściowych "
        "i edge cases. Na końcu chciałbym zauważyć, że plik config.py zawiera zahardkodowane "
        "hasło do bazy danych na linii 12, co absolutnie nie powinno znaleźć się w repozytorium. "
        "Ogólnie kod wymaga poprawek przed mergem.",
        "PR — 5 err:\n"
        "- `auth.py:23` JWT bez exp → token wieczny 🔓\n"
        "- `database.py:45` SQL konkatenacja → injection\n"
        "- `routes.py:67` brak walidacji email\n"
        "- `test_auth.py` jeno happy path, 0 edge cases\n"
        "- `config.py:12` hasło hardcoded 🔓\n"
        "Blokuje merge.",
    ),
    (
        "long_review",
        "polsko3",
        "Przeprowadziłem przegląd kodu w tym pull requeście i mam kilka uwag. Po pierwsze, "
        "w pliku auth.py na linii 23 tworzysz token JWT bez ustawienia czasu wygaśnięcia, "
        "co jest poważnym problemem bezpieczeństwa, ponieważ token będzie ważny w nieskończoność. "
        "Po drugie, w pliku database.py na linii 45 masz SQL query budowane przez konkatenację "
        "stringów zamiast użycia parametryzowanych zapytań, co naraża aplikację na SQL injection. "
        "Po trzecie, w pliku routes.py na linii 67 brakuje walidacji inputu od użytkownika — "
        "pole email nie jest sprawdzane pod kątem poprawności formatu. Po czwarte, testy w pliku "
        "test_auth.py pokrywają tylko happy path, brakuje testów dla błędnych danych wejściowych "
        "i edge cases. Na końcu chciałbym zauważyć, że plik config.py zawiera zahardkodowane "
        "hasło do bazy danych na linii 12, co absolutnie nie powinno znaleźć się w repozytorium. "
        "Ogólnie kod wymaga poprawek przed mergem.",
        "⚠ 5 blokerów:\n"
        "`auth.py:23` JWT no-exp | `database.py:45` SQLi | `routes.py:67` no validation | "
        "`test_auth.py` no edge | `config.py:12` secret in repo",
    ),
    (
        "long_review",
        "suwalsko1",
        "Przeprowadziłem przegląd kodu w tym pull requeście i mam kilka uwag. Po pierwsze, "
        "w pliku auth.py na linii 23 tworzysz token JWT bez ustawienia czasu wygaśnięcia, "
        "co jest poważnym problemem bezpieczeństwa, ponieważ token będzie ważny w nieskończoność. "
        "Po drugie, w pliku database.py na linii 45 masz SQL query budowane przez konkatenację "
        "stringów zamiast użycia parametryzowanych zapytań, co naraża aplikację na SQL injection. "
        "Po trzecie, w pliku routes.py na linii 67 brakuje walidacji inputu od użytkownika — "
        "pole email nie jest sprawdzane pod kątem poprawności formatu. Po czwarte, testy w pliku "
        "test_auth.py pokrywają tylko happy path, brakuje testów dla błędnych danych wejściowych "
        "i edge cases. Na końcu chciałbym zauważyć, że plik config.py zawiera zahardkodowane "
        "hasło do bazy danych na linii 12, co absolutnie nie powinno znaleźć się w repozytorium. "
        "Ogólnie kod wymaga poprawek przed mergem.",
        "Przegląd PR — jo, jest kilka problemów:\n\n"
        "1. auth.py:23 — JWT bez expiration, token wieczny. Ni dobrze z bezpieczeństwem.\n"
        "2. database.py:45 — SQL konkatenacją, groźba injection.\n"
        "3. routes.py:67 — ni ma walidacji email.\n"
        "4. test_auth.py — jeno happy path, ni ma edge cases.\n"
        "5. config.py:12 — hasło do bazy w kodzie. Wynieś do env.\n\n"
        "Trza poprawić przed merge.",
    ),
    (
        "long_review",
        "suwalsko2",
        "Przeprowadziłem przegląd kodu w tym pull requeście i mam kilka uwag. Po pierwsze, "
        "w pliku auth.py na linii 23 tworzysz token JWT bez ustawienia czasu wygaśnięcia, "
        "co jest poważnym problemem bezpieczeństwa, ponieważ token będzie ważny w nieskończoność. "
        "Po drugie, w pliku database.py na linii 45 masz SQL query budowane przez konkatenację "
        "stringów zamiast użycia parametryzowanych zapytań, co naraża aplikację na SQL injection. "
        "Po trzecie, w pliku routes.py na linii 67 brakuje walidacji inputu od użytkownika — "
        "pole email nie jest sprawdzane pod kątem poprawności formatu. Po czwarte, testy w pliku "
        "test_auth.py pokrywają tylko happy path, brakuje testów dla błędnych danych wejściowych "
        "i edge cases. Na końcu chciałbym zauważyć, że plik config.py zawiera zahardkodowane "
        "hasło do bazy danych na linii 12, co absolutnie nie powinno znaleźć się w repozytorium. "
        "Ogólnie kod wymaga poprawek przed mergem.",
        "Nu, kuknij na PR — wielga bieda:\n"
        "- `auth.py:23` JWT bez exp → token wieczny, ni dobrza 🔓\n"
        "- `database.py:45` SQL po chłopsku (konkatenacja) → injection\n"
        "- `routes.py:67` ni ma walidacji email\n"
        "- `test_auth.py` jeno happy path, nika wiécij\n"
        "- `config.py:12` hasło w repo 🔓\n"
        "Trza poprawić, ni puścim dalij.",
    ),
    (
        "long_review",
        "suwalsko3",
        "Przeprowadziłem przegląd kodu w tym pull requeście i mam kilka uwag. Po pierwsze, "
        "w pliku auth.py na linii 23 tworzysz token JWT bez ustawienia czasu wygaśnięcia, "
        "co jest poważnym problemem bezpieczeństwa, ponieważ token będzie ważny w nieskończoność. "
        "Po drugie, w pliku database.py na linii 45 masz SQL query budowane przez konkatenację "
        "stringów zamiast użycia parametryzowanych zapytań, co naraża aplikację na SQL injection. "
        "Po trzecie, w pliku routes.py na linii 67 brakuje walidacji inputu od użytkownika — "
        "pole email nie jest sprawdzane pod kątem poprawności formatu. Po czwarte, testy w pliku "
        "test_auth.py pokrywają tylko happy path, brakuje testów dla błędnych danych wejściowych "
        "i edge cases. Na końcu chciałbym zauważyć, że plik config.py zawiera zahardkodowane "
        "hasło do bazy danych na linii 12, co absolutnie nie powinno znaleźć się w repozytorium. "
        "Ogólnie kod wymaga poprawek przed mergem.",
        "Nu, poźri na to — barzo wielga bieda z tym PR:\n"
        "- `auth.py:23` — ón JWT robi bez exp, dy token wiecznie żyje. Czamu?!\n"
        "- `database.py:45` — SQL sklejany jek na chłopski rozum, ni parametryzowany. Injection gotowy.\n"
        "- `routes.py:67` — email léci bez sprawdzenia, haj waliduje!\n"
        "- `test_auth.py` — jeno radosna ścieżka, nika trudnego ni testuje\n"
        "- `config.py:12` — hasło do bazy siedzi prosto w repo, trza do env wyciągnąć\n"
        "Nika z tego ni puścim dalij, trza poprawić.",
    ),
    (
        "long_review",
        "terse-en",
        "Przeprowadziłem przegląd kodu w tym pull requeście i mam kilka uwag. Po pierwsze, "
        "w pliku auth.py na linii 23 tworzysz token JWT bez ustawienia czasu wygaśnięcia, "
        "co jest poważnym problemem bezpieczeństwa, ponieważ token będzie ważny w nieskończoność. "
        "Po drugie, w pliku database.py na linii 45 masz SQL query budowane przez konkatenację "
        "stringów zamiast użycia parametryzowanych zapytań, co naraża aplikację na SQL injection. "
        "Po trzecie, w pliku routes.py na linii 67 brakuje walidacji inputu od użytkownika — "
        "pole email nie jest sprawdzane pod kątem poprawności formatu. Po czwarte, testy w pliku "
        "test_auth.py pokrywają tylko happy path, brakuje testów dla błędnych danych wejściowych "
        "i edge cases. Na końcu chciałbym zauważyć, że plik config.py zawiera zahardkodowane "
        "hasło do bazy danych na linii 12, co absolutnie nie powinno znaleźć się w repozytorium. "
        "Ogólnie kod wymaga poprawek przed mergem.",
        "## Findings\n"
        "5 blockers:\n"
        "- `auth.py:23` — JWT without expiry → token lives forever 🔓\n"
        "- `database.py:45` — string-concat SQL → injection vector\n"
        "- `routes.py:67` — no email validation\n"
        "- `test_auth.py` — happy-path only, zero edge-case coverage\n"
        "- `config.py:12` — DB password hardcoded in source 🔓\n\n"
        "Blocks merge.",
    ),

    # =========================================================================
    # KATEGORIA 6: long_arch — wyjaśnienie architektury modułu
    # =========================================================================
    (
        "long_arch",
        "polsko1",
        "Moduł autentykacji w tej aplikacji składa się z kilku warstw. Na najwyższym poziomie "
        "mamy middleware AuthMiddleware zdefiniowany w pliku middleware/auth.py, który przechwytuje "
        "każde żądanie HTTP i sprawdza obecność tokenu w nagłówku Authorization. Token jest "
        "przekazywany do serwisu TokenService w pliku services/token.py, który weryfikuje jego "
        "ważność, sprawdza podpis i dekoduje payload. Jeśli token jest poprawny, serwis zwraca "
        "obiekt User, który jest dołączany do kontekstu żądania. W przypadku niepoprawnego tokenu "
        "middleware zwraca odpowiedź 401 Unauthorized. Warstwa persystencji znajduje się w "
        "repositories/user_repo.py i używa SQLAlchemy do komunikacji z bazą PostgreSQL. "
        "Sesje użytkowników są przechowywane w Redis z TTL równym czasowi życia tokenu. "
        "Cały flow to: Request → AuthMiddleware → TokenService → UserRepository → Redis/PostgreSQL. "
        "Konfiguracja kluczy JWT znajduje się w pliku config/auth.py i jest ładowana ze zmiennych "
        "środowiskowych przy starcie aplikacji.",
        "Moduł auth — warstwy:\n\n"
        "1. middleware/auth.py — AuthMiddleware przechwytuje requesty, sprawdza token z nagłówka Authorization.\n"
        "2. services/token.py — TokenService weryfikuje podpis, dekoduje payload, zwraca User.\n"
        "3. repositories/user_repo.py — SQLAlchemy + PostgreSQL.\n"
        "4. Sesje w Redis (TTL = czas życia tokenu).\n\n"
        "Flow: Request → AuthMiddleware → TokenService → UserRepository → Redis/PG.\n\n"
        "Klucze JWT: config/auth.py, ładowane z env vars przy starcie.\n"
        "401 Unauthorized jeśli token niepoprawny.",
    ),
    (
        "long_arch",
        "polsko2",
        "Moduł autentykacji w tej aplikacji składa się z kilku warstw. Na najwyższym poziomie "
        "mamy middleware AuthMiddleware zdefiniowany w pliku middleware/auth.py, który przechwytuje "
        "każde żądanie HTTP i sprawdza obecność tokenu w nagłówku Authorization. Token jest "
        "przekazywany do serwisu TokenService w pliku services/token.py, który weryfikuje jego "
        "ważność, sprawdza podpis i dekoduje payload. Jeśli token jest poprawny, serwis zwraca "
        "obiekt User, który jest dołączany do kontekstu żądania. W przypadku niepoprawnego tokenu "
        "middleware zwraca odpowiedź 401 Unauthorized. Warstwa persystencji znajduje się w "
        "repositories/user_repo.py i używa SQLAlchemy do komunikacji z bazą PostgreSQL. "
        "Sesje użytkowników są przechowywane w Redis z TTL równym czasowi życia tokenu. "
        "Cały flow to: Request → AuthMiddleware → TokenService → UserRepository → Redis/PostgreSQL. "
        "Konfiguracja kluczy JWT znajduje się w pliku config/auth.py i jest ładowana ze zmiennych "
        "środowiskowych przy starcie aplikacji.",
        "Auth — warstwy:\n"
        "- `middleware/auth.py` → przechwyt req, check token\n"
        "- `services/token.py` → weryfikacja, dekod, → User\n"
        "- `repositories/user_repo.py` → SQLAlchemy+PG\n"
        "- Sesje: Redis, TTL=token lifetime\n\n"
        "Flow: Req→Middleware→TokenSvc→UserRepo→Redis/PG\n"
        "Konf.: `config/auth.py` (env vars). Err: 401.",
    ),
    (
        "long_arch",
        "polsko3",
        "Moduł autentykacji w tej aplikacji składa się z kilku warstw. Na najwyższym poziomie "
        "mamy middleware AuthMiddleware zdefiniowany w pliku middleware/auth.py, który przechwytuje "
        "każde żądanie HTTP i sprawdza obecność tokenu w nagłówku Authorization. Token jest "
        "przekazywany do serwisu TokenService w pliku services/token.py, który weryfikuje jego "
        "ważność, sprawdza podpis i dekoduje payload. Jeśli token jest poprawny, serwis zwraca "
        "obiekt User, który jest dołączany do kontekstu żądania. W przypadku niepoprawnego tokenu "
        "middleware zwraca odpowiedź 401 Unauthorized. Warstwa persystencji znajduje się w "
        "repositories/user_repo.py i używa SQLAlchemy do komunikacji z bazą PostgreSQL. "
        "Sesje użytkowników są przechowywane w Redis z TTL równym czasowi życia tokenu. "
        "Cały flow to: Request → AuthMiddleware → TokenService → UserRepository → Redis/PostgreSQL. "
        "Konfiguracja kluczy JWT znajduje się w pliku config/auth.py i jest ładowana ze zmiennych "
        "środowiskowych przy starcie aplikacji.",
        "Req→`middleware/auth.py`→`services/token.py`→`repositories/user_repo.py`→Redis/PG\n"
        "Konf: `config/auth.py` (env). 401 on fail.",
    ),
    (
        "long_arch",
        "suwalsko1",
        "Moduł autentykacji w tej aplikacji składa się z kilku warstw. Na najwyższym poziomie "
        "mamy middleware AuthMiddleware zdefiniowany w pliku middleware/auth.py, który przechwytuje "
        "każde żądanie HTTP i sprawdza obecność tokenu w nagłówku Authorization. Token jest "
        "przekazywany do serwisu TokenService w pliku services/token.py, który weryfikuje jego "
        "ważność, sprawdza podpis i dekoduje payload. Jeśli token jest poprawny, serwis zwraca "
        "obiekt User, który jest dołączany do kontekstu żądania. W przypadku niepoprawnego tokenu "
        "middleware zwraca odpowiedź 401 Unauthorized. Warstwa persystencji znajduje się w "
        "repositories/user_repo.py i używa SQLAlchemy do komunikacji z bazą PostgreSQL. "
        "Sesje użytkowników są przechowywane w Redis z TTL równym czasowi życia tokenu. "
        "Cały flow to: Request → AuthMiddleware → TokenService → UserRepository → Redis/PostgreSQL. "
        "Konfiguracja kluczy JWT znajduje się w pliku config/auth.py i jest ładowana ze zmiennych "
        "środowiskowych przy starcie aplikacji.",
        "Moduł auth — jo, kilka warstw:\n\n"
        "1. middleware/auth.py — AuthMiddleware łapie requesty, sprawdza token.\n"
        "2. services/token.py — TokenService weryfikuje podpis, dekoduje, zwraca User.\n"
        "3. repositories/user_repo.py — SQLAlchemy + PostgreSQL.\n"
        "4. Sesje trzymane w Redis (TTL = życie tokenu).\n\n"
        "Flow: Request → Middleware → TokenService → UserRepo → Redis/PG.\n"
        "Klucze JWT w config/auth.py, z env vars. Jak ni pasuje token — 401.",
    ),
    (
        "long_arch",
        "suwalsko2",
        "Moduł autentykacji w tej aplikacji składa się z kilku warstw. Na najwyższym poziomie "
        "mamy middleware AuthMiddleware zdefiniowany w pliku middleware/auth.py, który przechwytuje "
        "każde żądanie HTTP i sprawdza obecność tokenu w nagłówku Authorization. Token jest "
        "przekazywany do serwisu TokenService w pliku services/token.py, który weryfikuje jego "
        "ważność, sprawdza podpis i dekoduje payload. Jeśli token jest poprawny, serwis zwraca "
        "obiekt User, który jest dołączany do kontekstu żądania. W przypadku niepoprawnego tokenu "
        "middleware zwraca odpowiedź 401 Unauthorized. Warstwa persystencji znajduje się w "
        "repositories/user_repo.py i używa SQLAlchemy do komunikacji z bazą PostgreSQL. "
        "Sesje użytkowników są przechowywane w Redis z TTL równym czasowi życia tokenu. "
        "Cały flow to: Request → AuthMiddleware → TokenService → UserRepository → Redis/PostgreSQL. "
        "Konfiguracja kluczy JWT znajduje się w pliku config/auth.py i jest ładowana ze zmiennych "
        "środowiskowych przy starcie aplikacji.",
        "Nu, kuknij jek auth léci:\n"
        "- `middleware/auth.py` — łapie req, ciągnie token z header\n"
        "- `services/token.py` — sprawdza podpis, dekoduje, daje User\n"
        "- `repositories/user_repo.py` — SQLAlchemy+PG\n"
        "- Sesje w Redis, TTL jek token żyje\n\n"
        "Flow: Req→Middleware→TokenSvc→Repo→Redis/PG\n"
        "Konf. kluczy: `config/auth.py` (z env). Ni pasuje → 401.",
    ),
    (
        "long_arch",
        "suwalsko3",
        "Moduł autentykacji w tej aplikacji składa się z kilku warstw. Na najwyższym poziomie "
        "mamy middleware AuthMiddleware zdefiniowany w pliku middleware/auth.py, który przechwytuje "
        "każde żądanie HTTP i sprawdza obecność tokenu w nagłówku Authorization. Token jest "
        "przekazywany do serwisu TokenService w pliku services/token.py, który weryfikuje jego "
        "ważność, sprawdza podpis i dekoduje payload. Jeśli token jest poprawny, serwis zwraca "
        "obiekt User, który jest dołączany do kontekstu żądania. W przypadku niepoprawnego tokenu "
        "middleware zwraca odpowiedź 401 Unauthorized. Warstwa persystencji znajduje się w "
        "repositories/user_repo.py i używa SQLAlchemy do komunikacji z bazą PostgreSQL. "
        "Sesje użytkowników są przechowywane w Redis z TTL równym czasowi życia tokenu. "
        "Cały flow to: Request → AuthMiddleware → TokenService → UserRepository → Redis/PostgreSQL. "
        "Konfiguracja kluczy JWT znajduje się w pliku config/auth.py i jest ładowana ze zmiennych "
        "środowiskowych przy starcie aplikacji.",
        "Nu, poźri jek to wszyćko léci — auth ma parę warstw:\n"
        "- `middleware/auth.py` — ón łapie każdy req dy ciągnie token z Authorization header\n"
        "- `services/token.py` — tu TokenService kuknij na podpis, dekoduje dy daje User nazad\n"
        "- `repositories/user_repo.py` — SQLAlchemy gada z PostgreSQL\n"
        "- Sesje siedzom w Redis, TTL taki jek token żyje\n\n"
        "Całe to léci: Req→Middleware→TokenSvc→UserRepo→Redis/PG\n"
        "Klucze JWT w `config/auth.py`, ciągnione z env przy starcie. "
        "Jek token ni pasuje — 401 dy koniec.",
    ),
    (
        "long_arch",
        "terse-en",
        "Moduł autentykacji w tej aplikacji składa się z kilku warstw. Na najwyższym poziomie "
        "mamy middleware AuthMiddleware zdefiniowany w pliku middleware/auth.py, który przechwytuje "
        "każde żądanie HTTP i sprawdza obecność tokenu w nagłówku Authorization. Token jest "
        "przekazywany do serwisu TokenService w pliku services/token.py, który weryfikuje jego "
        "ważność, sprawdza podpis i dekoduje payload. Jeśli token jest poprawny, serwis zwraca "
        "obiekt User, który jest dołączany do kontekstu żądania. W przypadku niepoprawnego tokenu "
        "middleware zwraca odpowiedź 401 Unauthorized. Warstwa persystencji znajduje się w "
        "repositories/user_repo.py i używa SQLAlchemy do komunikacji z bazą PostgreSQL. "
        "Sesje użytkowników są przechowywane w Redis z TTL równym czasowi życia tokenu. "
        "Cały flow to: Request → AuthMiddleware → TokenService → UserRepository → Redis/PostgreSQL. "
        "Konfiguracja kluczy JWT znajduje się w pliku config/auth.py i jest ładowana ze zmiennych "
        "środowiskowych przy starcie aplikacji.",
        "## Auth module layers\n"
        "- `middleware/auth.py` — intercepts req, extracts token from Authorization header\n"
        "- `services/token.py` — verifies sig, decodes payload → User obj\n"
        "- `repositories/user_repo.py` — SQLAlchemy + PostgreSQL\n"
        "- Sessions: Redis (TTL = token lifetime)\n\n"
        "Flow: Req→AuthMiddleware→TokenService→UserRepo→Redis/PG\n"
        "Config: `config/auth.py` (env vars at startup). Invalid token → 401.",
    ),
]
