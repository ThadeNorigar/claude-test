#!/usr/bin/env python3
"""
Matrix Digital Rain Effect - Windows Compatible
Klassischer Matrix-Style mit fallenden grünen Zeichen
Funktioniert auf Windows, Linux und macOS
"""

import os
import sys
import random
import time
import shutil
from collections import deque


class Colors:
    """ANSI Farbcodes für Terminal"""
    WHITE = '\033[97m'
    BRIGHT_GREEN = '\033[92m'
    GREEN = '\033[32m'
    DARK_GREEN = '\033[38;5;28m'
    VERY_DARK_GREEN = '\033[38;5;22m'
    YELLOW = '\033[1;33m'
    NC = '\033[0m'
    BOLD = '\033[1m'


class MatrixRain:
    """Matrix Digital Rain Effekt - Windows kompatibel"""

    # Zeichen für den Matrix-Effekt (erweiterte ASCII und Katakana-ähnliche)
    CHARS = list(
        "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ"
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ".:=*+-<>¦|"
        "ｦｧｨｩｪｫｬｭｮｯｰ"
        "日月火水木金土"
    )

    def __init__(self):
        self.running = True
        self.setup_terminal()
        self.init_drops()

    def setup_terminal(self):
        """Terminal Setup"""
        # Enable ANSI colors on Windows
        if sys.platform == 'win32':
            os.system('')  # Enable ANSI escape sequences

        # Terminal Größe
        term_size = shutil.get_terminal_size()
        self.width = term_size.columns
        self.height = term_size.lines - 1  # Eine Zeile für Status

    def init_drops(self):
        """Initialisiere fallende Zeichen-Tropfen"""
        self.drops = []
        for x in range(self.width):
            drop = {
                'x': x,
                'y': random.randint(-self.height, 0),
                'speed': random.uniform(0.2, 1.0),
                'length': random.randint(8, 25),
                'chars': deque(maxlen=35),
                'counter': 0.0
            }
            self.drops.append(drop)

    def clear_screen(self):
        """Bildschirm löschen"""
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

    def hide_cursor(self):
        """Cursor verstecken"""
        print('\033[?25l', end='', flush=True)

    def show_cursor(self):
        """Cursor anzeigen"""
        print('\033[?25h', end='', flush=True)

    def move_cursor(self, x, y):
        """Cursor bewegen"""
        print(f'\033[{y};{x}H', end='', flush=True)

    def get_random_char(self):
        """Gibt ein zufälliges Matrix-Zeichen zurück"""
        return random.choice(self.CHARS)

    def get_color(self, position, length):
        """Gibt die Farbe basierend auf Position im Tropfen zurück"""
        if position == length - 1:
            return Colors.WHITE + Colors.BOLD  # Kopf: Weiß/Hell
        elif position == length - 2:
            return Colors.BRIGHT_GREEN + Colors.BOLD
        elif position > length - 5:
            return Colors.BRIGHT_GREEN
        elif position > length - 10:
            return Colors.GREEN
        elif position > length - 15:
            return Colors.DARK_GREEN
        else:
            return Colors.VERY_DARK_GREEN

    def draw_frame(self):
        """Zeichnet einen Frame"""
        # Erstelle leeres Grid
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        colors = [[Colors.NC for _ in range(self.width)] for _ in range(self.height)]

        # Zeichne alle Tropfen ins Grid
        for drop in self.drops:
            length = len(drop['chars'])
            for i, (char, y_pos) in enumerate(drop['chars']):
                if 0 <= y_pos < self.height and 0 <= drop['x'] < self.width:
                    grid[y_pos][drop['x']] = char
                    colors[y_pos][drop['x']] = self.get_color(i, length)

        # Ausgabe
        self.move_cursor(0, 0)
        output = []
        for y in range(self.height):
            line = ''
            current_color = Colors.NC
            for x in range(self.width):
                char = grid[y][x]
                color = colors[y][x]
                if color != current_color:
                    line += color
                    current_color = color
                line += char
            output.append(line + Colors.NC)

        print('\n'.join(output), flush=True)

        # Status-Zeile
        status = f"{Colors.DARK_GREEN}Press Ctrl+C to exit | Matrix Digital Rain{Colors.NC}"
        print(status.ljust(self.width), end='', flush=True)

    def update_drops(self):
        """Aktualisiert alle Tropfen"""
        for drop in self.drops:
            drop['counter'] += drop['speed']

            if drop['counter'] >= 1.0:
                drop['counter'] = 0.0
                drop['y'] += 1

                # Neues Zeichen am Kopf
                drop['chars'].append((self.get_random_char(), drop['y']))

                # Manchmal Zeichen ändern (Flackern)
                if random.random() < 0.03 and len(drop['chars']) > 2:
                    idx = random.randint(0, len(drop['chars']) - 3)
                    old_char, y_pos = drop['chars'][idx]
                    drop['chars'][idx] = (self.get_random_char(), y_pos)

            # Reset wenn komplett durch
            if drop['y'] > self.height + drop['length']:
                drop['y'] = random.randint(-30, -5)
                drop['speed'] = random.uniform(0.2, 1.0)
                drop['length'] = random.randint(8, 25)
                drop['chars'].clear()

    def show_intro(self):
        """Zeigt Intro"""
        self.clear_screen()
        self.hide_cursor()

        intro = [
            "",
            "╔═══════════════════════════════════════════════════╗",
            "║                                                   ║",
            "║     M A T R I X   D I G I T A L   R A I N        ║",
            "║                                                   ║",
            "╚═══════════════════════════════════════════════════╝",
            "",
            "",
            "           W A K E   U P ,   N E O . . .",
            "",
            "             THE MATRIX HAS YOU",
            "",
            "         FOLLOW THE WHITE RABBIT",
            "",
            "",
            "           Press ENTER to continue...",
        ]

        for line in intro:
            print(f"{Colors.BRIGHT_GREEN}{line.center(self.width)}{Colors.NC}")

        input()  # Warte auf ENTER

    def run(self):
        """Hauptschleife"""
        try:
            self.show_intro()
            self.clear_screen()
            self.hide_cursor()

            frame_count = 0
            start_time = time.time()

            while True:
                frame_start = time.time()

                # Update und Draw
                self.update_drops()
                self.draw_frame()

                # FPS Control (~20-25 FPS für flüssige Animation)
                frame_time = time.time() - frame_start
                target_frame_time = 1.0 / 25.0  # 25 FPS
                if frame_time < target_frame_time:
                    time.sleep(target_frame_time - frame_time)

                frame_count += 1

                # Terminal-Größe neu checken alle 50 Frames
                if frame_count % 50 == 0:
                    old_width, old_height = self.width, self.height
                    self.setup_terminal()
                    if old_width != self.width or old_height != self.height:
                        self.init_drops()
                        self.clear_screen()

        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()

    def cleanup(self):
        """Aufräumen"""
        self.show_cursor()
        self.clear_screen()
        print(f"\n{Colors.BRIGHT_GREEN}Disconnecting from the Matrix...{Colors.NC}")
        print(f"{Colors.GREEN}Goodbye, Neo.{Colors.NC}\n")


def main():
    """Main Entry Point"""
    # Check für Windows Terminal Features
    if sys.platform == 'win32':
        # Windows Terminal erkennen
        if 'WT_SESSION' not in os.environ:
            print(f"{Colors.YELLOW}⚠ Hinweis: Für beste Darstellung verwenden Sie Windows Terminal{Colors.NC}")
            print(f"{Colors.YELLOW}  Download: https://aka.ms/terminal{Colors.NC}\n")
            time.sleep(2)

    matrix = MatrixRain()
    matrix.run()


if __name__ == "__main__":
    main()
