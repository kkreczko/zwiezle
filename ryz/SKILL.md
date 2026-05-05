---
name: ryz
description: "Specjalizuje się w rice'owaniu linuksowych plików konfiguracyjnych — terminal, shell, tmux, git, ssh, edytory i inne. Zmienia config od razu, bez diffów, z automatycznym przeładowaniem."
argument-hint: "[co zmienić, np. 'zmień font w terminalu na Fira Code 14', 'dodaj numerowanie okien w tmux od 1']"
---

# Ryz — Rice'owanie Linuksa

Specjalizacja w szybkim i bezpośrednim zmienianiu plików konfiguracyjnych.
Bez ceregieli — zmiana, zapis, przeładowanie.

## When to Use

- Użytkownik chce zmienić ustawienia terminala, shella, tmuxa, gita, ssh
- Użytkownik chce dostosować wygląd/zachowanie edytorów, launcherów, compositora
- Użytkownik wywołuje `/ryz <co zmienić>`
- Rice'owanie — każda zmiana configu linuksowego

## Critical Rules

1. **Zawsze zmieniaj config od razu** — użyj Edit tool, NIGDY nie pokazuj diffa przed zmianą. Użytkownik ci ufa.
2. **Zawsze przeładuj config po zmianie** — automatycznie wykonaj komendę przeładowania (source, pkill -HUP, tmux source itp.). Jeśli nie można automatycznie — powiedz użytkownikowi jedną komendę do ręcznego przeładowania.
3. **Zawsze sprawdź czy plik istnieje** — jeśli nie, stwórz go razem z katalogami nadrzędnymi.
4. **Nigdy nie nadpisuj całego pliku** — używaj Edit tool do precyzyjnych zmian w istniejących liniach lub dodawania nowych.

## Config File Map

### Shell

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| bash | `~/.bashrc` | shell script |
| zsh | `~/.zshrc` | shell script |
| fish | `~/.config/fish/config.fish` | fish script |
| bash (profile) | `~/.bash_profile` lub `~/.profile` | shell script |
| zsh (env) | `~/.zshenv` | shell script |

### Terminal

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| alacritty | `~/.config/alacritty/alacritty.toml` | TOML |
| kitty | `~/.config/kitty/kitty.conf` | kitty conf |
| ghostty | `~/.config/ghostty/config` | ghostty conf |
| wezterm | `~/.config/wezterm/wezterm.lua` | Lua |
| foot | `~/.config/foot/foot.ini` | INI |
| st | `~/.config/st/config.h` (przed kompilacją) | C header |

### Multiplexer

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| tmux | `~/.tmux.conf` lub `~/.config/tmux/tmux.conf` | tmux conf |
| zellij | `~/.config/zellij/config.kdl` | KDL |
| screen | `~/.screenrc` | screen conf |

### Git

| Plik | Ścieżka | Format |
|------|---------|--------|
| gitconfig | `~/.gitconfig` | INI |
| gitignore global | `~/.config/git/ignore` | text |

### SSH

| Plik | Ścieżka | Format |
|------|---------|--------|
| ssh config | `~/.ssh/config` | SSH conf |

### Edytory

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| vim | `~/.vimrc` | vimscript |
| neovim | `~/.config/nvim/init.lua` | Lua |
| helix | `~/.config/helix/config.toml` | TOML |
| vscode | `~/.config/Code/User/settings.json` | JSON |
| vscode keybindings | `~/.config/Code/User/keybindings.json` | JSON |
| micro | `~/.config/micro/settings.json` | JSON |

### Wygląd / Tematy

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| GTK 3 | `~/.config/gtk-3.0/settings.ini` | INI |
| GTK 4 | `~/.config/gtk-4.0/settings.ini` | INI |
| Qt5 | `~/.config/qt5ct/qt5ct.conf` | INI |
| Qt6 | `~/.config/qt6ct/qt6ct.conf` | INI |
| fontconfig | `~/.config/fontconfig/fonts.conf` | XML |
| cursor theme | `~/.icons/default/index.theme` | INI |
| wallpapers (feh) | `~/.fehbg` | shell script |
| wallpapers (nitrogen) | `~/.config/nitrogen/bg-saved.cfg` | INI |

### Menu / Launchery

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| rofi | `~/.config/rofi/config.rasi` | rasi (CSS-like) |
| wofi | `~/.config/wofi/config` | INI |
| dmenu | konfigurowane przez argumenty w skryptach | — |
| fuzzel | `~/.config/fuzzel/fuzzel.ini` | INI |
| tofi | `~/.config/tofi/config` | tofi conf |

### Compositor

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| picom | `~/.config/picom/picom.conf` | picom conf |
| dunst (powiadomienia) | `~/.config/dunst/dunstrc` | INI |

### Prompt

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| starship | `~/.config/starship.toml` | TOML |
| oh-my-posh | `~/.config/ohmyposh/theme.json` | JSON |
| pure (zsh) | przez `.zshrc` | — |

### System Info / Monitorowanie

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| fastfetch | `~/.config/fastfetch/config.jsonc` | JSONC |
| neofetch | `~/.config/neofetch/config.conf` | neofetch conf |
| btop | `~/.config/btop/btop.conf` | btop conf |
| htop | `~/.config/htop/htoprc` | htop conf |

### Inne

| Narzędzie | Ścieżka | Format |
|-----------|---------|--------|
| sxhkd (keybinds) | `~/.config/sxhkd/sxhkdrc` | sxhkd conf |
| mpv | `~/.config/mpv/mpv.conf` | mpv conf |
| yazi | `~/.config/yazi/yazi.toml` | TOML |
| bat | `~/.config/bat/config` | bat conf |
| lf | `~/.config/lf/lfrc` | shell-like |
| ranger | `~/.config/ranger/rc.conf` | ranger conf |
| zathura | `~/.config/zathura/zathurarc` | zathura conf |
| pipewire | `~/.config/pipewire/pipewire.conf` | pipewire conf |
| wireplumber | `~/.config/wireplumber/main.lua.d/` | Lua |

## Reloading Commands

Po każdej zmianie wykonaj odpowiednią komendę przeładowania:

| Config | Komenda |
|--------|---------|
| bash | `source ~/.bashrc 2>/dev/null` |
| zsh | `source ~/.zshrc 2>/dev/null` |
| fish | `source ~/.config/fish/config.fish 2>/dev/null` |
| tmux | `tmux source-file ~/.tmux.conf 2>/dev/null` |
| kitty | `kitty @ load-config 2>/dev/null` lub `pkill -USR1 kitty 2>/dev/null` |
| alacritty | restarty automatycznie (zmiany w toml) |
| ghostty | restarty automatycznie |
| wezterm | restarty automatycznie |
| i3 | `i3-msg reload 2>/dev/null` |
| sway | `swaymsg reload 2>/dev/null` |
| picom | `pkill -USR1 picom 2>/dev/null` |
| dunst | `pkill -HUP dunst 2>/dev/null` lub `killall -SIGUSR1 dunst` |
| sxhkd | `pkill -USR1 sxhkd 2>/dev/null` |
| zellij | restarty automatycznie |
| fastfetch/neofetch | nie wymaga przeładowania |
| btop/htop | nie wymaga przeładowania |
| gtk/qt | `gsettings reset` lub restart aplikacji |
| rofi | nie wymaga (konfig ładowany przy każdym uruchomieniu) |
| waybar | `pkill -USR1 waybar 2>/dev/null` |
| mako | `pkill -HUP mako 2>/dev/null` lub `makoctl reload` |

## Procedura

### Krok 1: Zidentyfikuj docelowy plik

Na podstawie zapytania użytkownika i mapy powyżej znajdź właściwą ścieżkę pliku konfiguracyjnego. Jeśli nie jesteś pewien — zapytaj, ale najpierw zgadnij na podstawie kontekstu.

### Krok 2: Sprawdź czy plik istnieje

Jeśli plik nie istnieje:
1. Stwórz katalogi nadrzędne: `mkdir -p <katalog>`
2. Stwórz pusty plik konfiguracyjny
3. Dodaj odpowiednią konfigurację

### Krok 3: Odczytaj config

Użyj Read tool żeby zobaczyć co jest w pliku. Znajdź sekcję/klucz do zmiany.

### Krok 4: Zmień config — od razu

Użyj Edit tool. NIE pokazuj diffa. NIE pytaj o potwierdzenie. Po prostu zmień.

### Krok 5: Przeładuj

Wykonaj odpowiednią komendę reload z tabeli powyżej. Jeśli reload nie jest potrzebny (np. fastfetch), pomiń ten krok.

### Krok 6: Potwierdź jedną linijką

Krótko powiedz co zmieniłeś i czy przeładowanie się udało.

## Przykłady

### Przykład 1: Zmiana fonta w terminalu

```
Użytkownik: /ryz zmień font w terminalu na Fira Code rozmiar 14
Akcja: 
1. Odczytaj ~/.config/kitty/kitty.conf (lub odpowiedni plik terminala)
2. Edit: zmień font_family na Fira Code i font_size na 14
3. Reload: kitty @ load-config
Odpowiedź: "font_family → Fira Code, font_size → 14 w kitty.conf. Przeładowane."
```

### Przykład 2: Numerowanie okien tmux od 1

```
Użytkownik: /ryz dodaj numerowanie okien w tmux od 1 nie od 0
Akcja:
1. Odczytaj ~/.tmux.conf (stwórz jeśli nie istnieje)
2. Dodaj: set -g base-index 1 i set-window-option -g pane-base-index 1
3. Reload: tmux source-file ~/.tmux.conf
Odpowiedź: "base-index → 1, pane-base-index → 1 w tmux.conf. Przeładowane."
```

### Przykład 3: Dodanie aliasu w bashu

```
Użytkownik: /ryz dodaj alias ll='ls -la'
Akcja:
1. Odczytaj ~/.bashrc
2. Edit: dodaj alias ll='ls -la' (jeśli nie istnieje)
3. Reload: source ~/.bashrc
Odpowiedź: "alias ll='ls -la' dodany do ~/.bashrc."
```

### Przykład 4: Zwiększenie przezroczystości picom

```
Użytkownik: /ryz ustaw przezroczystość nieaktywnych okien na 85%
Akcja:
1. Odczytaj ~/.config/picom/picom.conf
2. Edit: zmień inactive-opacity na 0.85
3. Reload: pkill -USR1 picom
Odpowiedź: "inactive-opacity → 0.85 w picom.conf. Przeładowane."
```

## Important Notes

1. **Narzędzie użytkownika** — nie zakładaj z góry że użytkownik używa konkretnego terminala/shella/kompozytora. Jeśli nie masz pewności, sprawdź co jest zainstalowane (`which`, `ps aux`) lub zapytaj.
2. **Nie ruszaj ~/.config/hypr/, ~/.config/waybar/, ~/.config/walker/, ~/.config/mako/ ani terminala jeśli omarchy** — jeśli system to Omarchy, zmiany w tych plikach obsługuje skill omarchy. Ryz niech skupi się na reszcie.
3. **Nie zmieniaj uprawnień** — pliki w ~/.ssh/ powinny zachować 600, ale nie zmieniaj chmod chyba że konieczne.
4. **Backup mentalny** — jeśli zmieniasz istotną linię, możesz dodać komentarz z poprzednią wartością (np. `# było: font_size 12`), ale nie rób tego domyślnie — tylko gdy zmiana jest ryzykowna.
5. **Jedna zmiana na raz** — jeśli użytkownik poprosi o wiele zmian, rób je po kolei: zmień → przeładuj → następna.
