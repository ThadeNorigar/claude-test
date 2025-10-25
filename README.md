# Matrix Programs Collection

Eine Sammlung von Matrix-Style Konsolenprogrammen in Python.

## Programme

### 1. 🖥️ Matrix Monitor (`matrix_monitor.py`)

Simuliert kontinuierliche System-Operationen im Hacker-Style.

**Features:**
- Netzwerk-Scans mit IP-Adressen und Ports
- Prozess-Monitoring (CPU/Memory)
- Firewall-Logs
- Datei-Integritätsprüfungen (SHA256)
- Verschlüsselungsstatus
- Authentifizierungs-Logs
- Bandbreiten-Monitoring
- Intrusion Detection
- Datenbankabfragen
- SSL/TLS Zertifikats-Checks
- Deep Packet Inspection
- Backup-Status
- Security Scores

**Verwendung:**
```bash
python matrix_monitor.py
```

**Kompatibilität:** Windows, Linux, macOS

---

### 2. 🌧️ Matrix Digital Rain (`matrix_rain_win.py`) ⭐ EMPFOHLEN für Windows

Klassischer Matrix Digital Rain Effekt - fallende grüne Zeichen wie im Film!

**Features:**
- Authentischer Matrix-Effekt mit fallenden Zeichen
- Katakana, Zahlen und Symbole
- Verschiedene Grüntöne (weiß → hellgrün → dunkelgrün)
- Smooth Animation (~25 FPS)
- Intro-Screen: "Wake up, Neo..."
- Zufällige Geschwindigkeiten und Längen
- Zeichen flackern während sie fallen
- **Windows-kompatibel!**

**Verwendung:**
```bash
python matrix_rain_win.py
```

**Kompatibilität:** Windows, Linux, macOS

**Empfehlung für Windows:** Verwenden Sie [Windows Terminal](https://aka.ms/terminal) für beste Darstellung.

---

### 3. 🌧️ Matrix Digital Rain (`matrix_rain.py`)

Alternative Version mit Python `curses` - nur für Linux/macOS.

**Hinweis:** Diese Version funktioniert **nicht unter Windows**, da das `curses` Modul nicht verfügbar ist.

**Verwendung (nur Linux/macOS):**
```bash
python matrix_rain.py
```

**Kompatibilität:** Linux, macOS

---

## Schnellstart

### Windows
```bash
# Matrix Monitor
python matrix_monitor.py

# Matrix Rain (empfohlen)
python matrix_rain_win.py
```

### Linux / macOS
```bash
# Matrix Monitor
python3 matrix_monitor.py

# Matrix Rain (beide Versionen funktionieren)
python3 matrix_rain_win.py
# oder
python3 matrix_rain.py
```

## Beenden

Alle Programme können mit **`Ctrl+C`** beendet werden.

Bei `matrix_rain_win.py` zusätzlich mit **`q`** oder **`ESC`** möglich.

## Voraussetzungen

- Python 3.6 oder höher
- Keine zusätzlichen Pakete erforderlich (nur Standard-Bibliothek)

## Terminal-Empfehlungen

### Windows
- **Windows Terminal** (empfohlen): https://aka.ms/terminal
- PowerShell
- CMD

### Linux
- Jedes moderne Terminal (GNOME Terminal, Konsole, xterm, etc.)

### macOS
- Terminal.app
- iTerm2

## Screenshots

### Matrix Monitor
```
╔═══════════════════════════════════════════════════════════════╗
║   ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗          ║
║   ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝           ║
╚═══════════════════════════════════════════════════════════════╝

[SCAN] Netzwerk-Scan gestartet...
  ► Probing 192.168.1.42:8080 [OPEN]
  ► Probing 10.0.0.15:443 [FILTERED]

[PROC] Überwache aktive Prozesse...
  ► PID: 4521 | CPU: 45% | MEM: 32%
```

### Matrix Digital Rain
```
Fallende grüne Zeichen von oben nach unten:

ﾊ   7   ｳ   B   5   ﾓ
ﾐ   3   ｼ   K   9   ﾆ
ﾋ   日  ﾅ   L   2   ｻ
ｰ   0   月  P   8   ﾜ
    火  4   ｵ   1   ﾂ
```

## Lizenz

Frei verfügbar für persönliche und kommerzielle Nutzung.

## Credits

Erstellt mit [Claude Code](https://claude.com/claude-code)

---

**Viel Spaß beim Eintauchen in die Matrix!** 🟢⚫🟢
