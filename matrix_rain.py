#!/usr/bin/env python3
"""
Matrix Digital Rain Effect
Klassischer Matrix-Style mit fallenden grünen Zeichen
"""

import curses
import random
import time
from collections import deque


class MatrixRain:
    """Matrix Digital Rain Effekt"""

    # Zeichen für den Matrix-Effekt (Katakana, Zahlen, Symbole)
    CHARS = (
        "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ"
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ".:=*+-<>¦|╌"
        "ｦｧｨｩｪｫｬｭｮｯｰ"
    )

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.drops = []

        # Curses Setup
        curses.curs_set(0)  # Cursor verstecken
        curses.start_color()
        curses.use_default_colors()

        # Farben definieren (verschiedene Grüntöne)
        curses.init_pair(1, 255, -1)  # Weiß (hellster Punkt)
        curses.init_pair(2, 10, -1)   # Sehr helles Grün
        curses.init_pair(3, 46, -1)   # Helles Grün
        curses.init_pair(4, 40, -1)   # Mittleres Grün
        curses.init_pair(5, 34, -1)   # Dunkles Grün
        curses.init_pair(6, 28, -1)   # Sehr dunkles Grün

        self.stdscr.timeout(50)  # Non-blocking input mit 50ms timeout

        # Initialisiere Tropfen für jede Spalte
        self.init_drops()

    def init_drops(self):
        """Initialisiere fallende Zeichen-Tropfen"""
        for x in range(self.width):
            # Zufällige Start-Position und Geschwindigkeit
            drop = {
                'x': x,
                'y': random.randint(-self.height, 0),
                'speed': random.uniform(0.3, 1.5),
                'length': random.randint(5, 25),
                'chars': deque(maxlen=30),
                'counter': 0.0
            }
            self.drops.append(drop)

    def get_random_char(self):
        """Gibt ein zufälliges Matrix-Zeichen zurück"""
        return random.choice(self.CHARS)

    def draw_drop(self, drop):
        """Zeichnet einen einzelnen fallenden Tropfen"""
        length = len(drop['chars'])

        for i, (char, y_pos) in enumerate(drop['chars']):
            if 0 <= y_pos < self.height - 1 and 0 <= drop['x'] < self.width:
                # Farbintensität basierend auf Position im Tropfen
                if i == length - 1:
                    # Hellster Punkt (Kopf des Tropfens)
                    color = curses.color_pair(1) | curses.A_BOLD
                elif i == length - 2:
                    color = curses.color_pair(2) | curses.A_BOLD
                elif i == length - 3:
                    color = curses.color_pair(3) | curses.A_BOLD
                elif i > length - 6:
                    color = curses.color_pair(4)
                elif i > length - 10:
                    color = curses.color_pair(5)
                else:
                    color = curses.color_pair(6)

                try:
                    self.stdscr.addstr(y_pos, drop['x'], char, color)
                except curses.error:
                    pass  # Ignoriere Fehler am Rand des Bildschirms

    def update_drop(self, drop):
        """Aktualisiert einen Tropfen"""
        drop['counter'] += drop['speed']

        if drop['counter'] >= 1.0:
            drop['counter'] = 0.0
            drop['y'] += 1

            # Neues Zeichen am Kopf hinzufügen
            drop['chars'].append((self.get_random_char(), drop['y']))

            # Manchmal Zeichen zufällig ändern (flackern)
            if random.random() < 0.05 and len(drop['chars']) > 0:
                idx = random.randint(0, len(drop['chars']) - 1)
                old_char, y_pos = drop['chars'][idx]
                drop['chars'][idx] = (self.get_random_char(), y_pos)

        # Reset wenn Tropfen aus dem Bildschirm ist
        if drop['y'] > self.height + drop['length']:
            drop['y'] = random.randint(-20, -5)
            drop['speed'] = random.uniform(0.3, 1.5)
            drop['length'] = random.randint(5, 25)
            drop['chars'].clear()

    def draw_banner(self):
        """Zeigt den Matrix-Banner in der Mitte"""
        banner = [
            "╔═══════════════════════════════════════╗",
            "║     M  A  T  R  I  X     R  A  I  N  ║",
            "╚═══════════════════════════════════════╝"
        ]

        start_y = self.height // 2 - 2
        for i, line in enumerate(banner):
            x = max(0, (self.width - len(line)) // 2)
            try:
                self.stdscr.addstr(start_y + i, x, line,
                                 curses.color_pair(2) | curses.A_BOLD)
            except curses.error:
                pass

    def show_intro(self):
        """Zeigt Intro-Animation"""
        intro_text = [
            "WAKE UP, NEO...",
            "",
            "THE MATRIX HAS YOU",
            "",
            "FOLLOW THE WHITE RABBIT",
            "",
            "Press any key to enter the Matrix...",
        ]

        self.stdscr.clear()
        start_y = self.height // 2 - len(intro_text) // 2

        for i, line in enumerate(intro_text):
            x = max(0, (self.width - len(line)) // 2)
            try:
                self.stdscr.addstr(start_y + i, x, line,
                                 curses.color_pair(2) | curses.A_BOLD)
            except curses.error:
                pass

        self.stdscr.refresh()
        self.stdscr.timeout(-1)  # Blocking input
        self.stdscr.getch()
        self.stdscr.timeout(50)  # Zurück zu non-blocking

    def run(self):
        """Hauptschleife"""
        try:
            # Zeige Intro
            self.show_intro()

            show_banner_until = time.time() + 3  # Banner für 3 Sekunden

            while True:
                # Check für Tastendruck (ESC oder q zum Beenden)
                key = self.stdscr.getch()
                if key in (27, ord('q'), ord('Q')):  # ESC oder q
                    break

                # Bildschirm leicht dimmen (Spur-Effekt)
                self.stdscr.clear()

                # Aktualisiere und zeichne alle Tropfen
                for drop in self.drops:
                    self.update_drop(drop)
                    self.draw_drop(drop)

                # Zeige Banner am Anfang
                if time.time() < show_banner_until:
                    self.draw_banner()

                # Zeige Tastenkombination zum Beenden
                try:
                    exit_text = "Press 'q' or ESC to exit"
                    self.stdscr.addstr(self.height - 1,
                                     max(0, self.width - len(exit_text) - 2),
                                     exit_text,
                                     curses.color_pair(5))
                except curses.error:
                    pass

                self.stdscr.refresh()
                time.sleep(0.03)  # ~30 FPS

        except KeyboardInterrupt:
            pass


def main(stdscr):
    """Main Entry Point für curses"""
    matrix = MatrixRain(stdscr)
    matrix.run()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass

    print("\n\033[0;32mDisconnecting from the Matrix...\033[0m")
    print("\033[1;32mGoodbye, Neo.\033[0m\n")
