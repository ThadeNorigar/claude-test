#!/usr/bin/env python3
"""
Matrix-Style System Monitor
Kontinuierliche Simulation von System-Operationen im Hacker-Style
"""

import random
import time
import sys
import hashlib
from datetime import datetime, timedelta


class Colors:
    """ANSI Farbcodes für Terminal-Ausgabe"""
    GREEN = '\033[0;32m'
    BRIGHT_GREEN = '\033[1;32m'
    CYAN = '\033[0;36m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    NC = '\033[0m'  # No Color
    BOLD = '\033[1m'


class MatrixMonitor:
    """Haupt-Klasse für Matrix-Style System Monitor"""

    def __init__(self):
        self.users = ["admin", "root", "operator", "sysmon", "netadmin"]
        self.files = ["kernel.sys", "auth.conf", "network.db", "security.log", "crypto.key"]
        self.algorithms = ["AES-256", "RSA-4096", "ChaCha20", "Twofish"]
        self.protocols = ["TCP", "UDP", "ICMP"]
        self.domains = ["secure.matrix.net", "auth.cyber.io", "api.quantum.dev"]

    @staticmethod
    def clear_screen():
        """Terminal löschen"""
        print("\033[2J\033[H", end="")

    @staticmethod
    def typing_effect(text, color, delay=0.01):
        """Typing-Effekt für Text"""
        for char in text:
            print(f"{color}{char}{Colors.NC}", end="", flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def random_ip():
        """Generiert zufällige IP-Adresse"""
        return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

    @staticmethod
    def random_port():
        """Generiert zufälligen Port"""
        return random.randint(1, 65535)

    @staticmethod
    def random_pid():
        """Generiert zufällige Prozess-ID"""
        return random.randint(1000, 9999)

    @staticmethod
    def random_hash():
        """Generiert zufälligen Hash-Wert"""
        random_data = str(random.random()).encode()
        return hashlib.sha256(random_data).hexdigest()

    def show_banner(self):
        """Zeigt Matrix-Banner"""
        banner = f"""{Colors.BRIGHT_GREEN}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗          ║
║   ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝          ║
║   ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝           ║
║   ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗           ║
║   ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗          ║
║   ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝          ║
║                                                               ║
║              S Y S T E M   M O N I T O R                      ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.NC}"""
        print(banner)

    def initialize(self):
        """Initialisierungs-Sequenz"""
        self.typing_effect("[INIT] Starte Systemüberwachung...", Colors.CYAN)
        time.sleep(0.5)
        self.typing_effect("[INIT] Verbinde zu Netzwerk-Matrix...", Colors.CYAN)
        time.sleep(0.5)
        self.typing_effect("[INIT] Initialisiere Sicherheitsprotokolle...", Colors.CYAN)
        time.sleep(0.5)
        print(f"{Colors.GREEN}[OK] System bereit{Colors.NC}\n")
        time.sleep(1)

    def network_scan(self):
        """Simuliert Netzwerk-Scan"""
        print(f"{Colors.BRIGHT_GREEN}[SCAN]{Colors.NC} {Colors.CYAN}Netzwerk-Scan gestartet...{Colors.NC}")
        for _ in range(5):
            ip = self.random_ip()
            port = self.random_port()
            status = random.choice(["OPEN"] * 7 + ["FILTERED"] * 3)
            color = Colors.GREEN if status == "OPEN" else Colors.RED
            print(f"  {Colors.GREEN}►{Colors.NC} Probing {ip}:{port} {color}[{status}]{Colors.NC}")
            time.sleep(0.3)

    def process_monitoring(self):
        """Simuliert Prozess-Monitoring"""
        print(f"{Colors.BRIGHT_GREEN}[PROC]{Colors.NC} {Colors.CYAN}Überwache aktive Prozesse...{Colors.NC}")
        for _ in range(4):
            pid = self.random_pid()
            cpu = random.randint(0, 100)
            mem = random.randint(0, 100)
            print(f"  {Colors.GREEN}►{Colors.NC} PID: {pid} | CPU: {cpu}% | MEM: {mem}%")
            time.sleep(0.2)

    def firewall_log(self):
        """Simuliert Firewall-Log-Analyse"""
        print(f"{Colors.BRIGHT_GREEN}[FWALL]{Colors.NC} {Colors.CYAN}Analysiere Firewall-Logs...{Colors.NC}")
        for _ in range(3):
            ip = self.random_ip()
            action = random.choice(["ACCEPT", "DROP", "REJECT"])
            color = Colors.GREEN if action == "ACCEPT" else Colors.RED
            print(f"  {Colors.GREEN}►{Colors.NC} Packet from {ip} {color}[{action}]{Colors.NC}")
            time.sleep(0.3)

    def file_integrity(self):
        """Simuliert Datei-Integritätsprüfung"""
        print(f"{Colors.BRIGHT_GREEN}[HASH]{Colors.NC} {Colors.CYAN}Prüfe Datei-Integrität...{Colors.NC}")
        file = random.choice(self.files)
        hash_value = self.random_hash()
        print(f"  {Colors.GREEN}►{Colors.NC} {file}")
        print(f"  {Colors.GREEN}►{Colors.NC} SHA256: {hash_value} {Colors.GREEN}[OK]{Colors.NC}")
        time.sleep(0.4)

    def connection_analysis(self):
        """Simuliert Verbindungsanalyse"""
        print(f"{Colors.BRIGHT_GREEN}[CONN]{Colors.NC} {Colors.CYAN}Aktive Verbindungen analysieren...{Colors.NC}")
        for _ in range(4):
            local_ip = f"192.168.1.{random.randint(0, 255)}"
            remote_ip = self.random_ip()
            local_port = self.random_port()
            remote_port = self.random_port()
            print(f"  {Colors.GREEN}►{Colors.NC} {local_ip}:{local_port} ↔ {remote_ip}:{remote_port} {Colors.GREEN}[ESTABLISHED]{Colors.NC}")
            time.sleep(0.25)

    def encryption_status(self):
        """Simuliert Verschlüsselungsstatus"""
        print(f"{Colors.BRIGHT_GREEN}[CRYPT]{Colors.NC} {Colors.CYAN}Verschlüsselungsstatus...{Colors.NC}")
        algo = random.choice(self.algorithms)
        print(f"  {Colors.GREEN}►{Colors.NC} Algorithmus: {algo}")
        print(f"  {Colors.GREEN}►{Colors.NC} Key Exchange: {Colors.GREEN}[SECURE]{Colors.NC}")
        print(f"  {Colors.GREEN}►{Colors.NC} Cipher Strength: {Colors.GREEN}[MAXIMUM]{Colors.NC}")
        time.sleep(0.5)

    def authentication_log(self):
        """Simuliert Authentifizierungs-Logs"""
        print(f"{Colors.BRIGHT_GREEN}[AUTH]{Colors.NC} {Colors.CYAN}Überprüfe Authentifizierung...{Colors.NC}")
        user = random.choice(self.users)
        ip = self.random_ip()
        success = random.randint(0, 9) < 8
        if success:
            print(f"  {Colors.GREEN}►{Colors.NC} Login: {user}@{ip} {Colors.GREEN}[SUCCESS]{Colors.NC}")
        else:
            print(f"  {Colors.GREEN}►{Colors.NC} Login: {user}@{ip} {Colors.YELLOW}[FAILED - BLOCKED]{Colors.NC}")
        time.sleep(0.4)

    def bandwidth_monitor(self):
        """Simuliert Bandbreiten-Monitoring"""
        print(f"{Colors.BRIGHT_GREEN}[BAND]{Colors.NC} {Colors.CYAN}Netzwerk-Traffic-Analyse...{Colors.NC}")
        down = random.randint(0, 1000)
        up = random.randint(0, 500)
        latency = random.randint(0, 50)
        print(f"  {Colors.GREEN}►{Colors.NC} Download: {down} MB/s")
        print(f"  {Colors.GREEN}►{Colors.NC} Upload: {up} MB/s")
        print(f"  {Colors.GREEN}►{Colors.NC} Latenz: {latency}ms {Colors.GREEN}[OPTIMAL]{Colors.NC}")
        time.sleep(0.4)

    def intrusion_detection(self):
        """Simuliert Intrusion Detection"""
        print(f"{Colors.BRIGHT_GREEN}[IDS]{Colors.NC} {Colors.CYAN}Intrusion Detection Scan...{Colors.NC}")
        threats = random.randint(0, 9) < 8
        if threats:
            print(f"  {Colors.GREEN}►{Colors.NC} Status: {Colors.GREEN}[CLEAN]{Colors.NC}")
            print(f"  {Colors.GREEN}►{Colors.NC} Bedrohungen: 0")
        else:
            ip = self.random_ip()
            print(f"  {Colors.GREEN}►{Colors.NC} Status: {Colors.YELLOW}[ANOMALIE ERKANNT]{Colors.NC}")
            print(f"  {Colors.GREEN}►{Colors.NC} Quelle: {ip} {Colors.YELLOW}[BLOCKED]{Colors.NC}")
        time.sleep(0.5)

    def database_query(self):
        """Simuliert Datenbankabfrage"""
        print(f"{Colors.BRIGHT_GREEN}[DB]{Colors.NC} {Colors.CYAN}Datenbankabfrage läuft...{Colors.NC}")
        print(f"  {Colors.GREEN}►{Colors.NC} SELECT * FROM network_events WHERE timestamp > NOW() - INTERVAL 5 MINUTE")
        rows = random.randint(0, 1000)
        query_time = random.randint(0, 999)
        print(f"  {Colors.GREEN}►{Colors.NC} {rows} Zeilen gefunden")
        print(f"  {Colors.GREEN}►{Colors.NC} Query Zeit: 0.{query_time:03d}s {Colors.GREEN}[OK]{Colors.NC}")
        time.sleep(0.5)

    def system_resources(self):
        """Simuliert System-Ressourcen Check"""
        print(f"{Colors.BRIGHT_GREEN}[SYS]{Colors.NC} {Colors.CYAN}System-Ressourcen Check...{Colors.NC}")
        cpu = random.randint(0, 100)
        memory = random.randint(0, 100)
        disk_io = random.randint(0, 100)
        network = random.randint(0, 100)
        print(f"  {Colors.GREEN}►{Colors.NC} CPU Load: {cpu}%")
        print(f"  {Colors.GREEN}►{Colors.NC} Memory: {memory}%")
        print(f"  {Colors.GREEN}►{Colors.NC} Disk I/O: {disk_io}%")
        print(f"  {Colors.GREEN}►{Colors.NC} Network: {network}% {Colors.GREEN}[HEALTHY]{Colors.NC}")
        time.sleep(0.4)

    def certificate_check(self):
        """Simuliert Zertifikats-Validierung"""
        print(f"{Colors.BRIGHT_GREEN}[CERT]{Colors.NC} {Colors.CYAN}SSL/TLS Zertifikate validieren...{Colors.NC}")
        domain = random.choice(self.domains)
        days = random.randint(30, 395)
        print(f"  {Colors.GREEN}►{Colors.NC} {domain}")
        print(f"  {Colors.GREEN}►{Colors.NC} Gültig für: {days} Tage {Colors.GREEN}[VALID]{Colors.NC}")
        time.sleep(0.4)

    def packet_analysis(self):
        """Simuliert Packet Analysis"""
        print(f"{Colors.BRIGHT_GREEN}[PKT]{Colors.NC} {Colors.CYAN}Deep Packet Inspection...{Colors.NC}")
        for _ in range(3):
            proto = random.choice(self.protocols)
            size = random.randint(64, 1564)
            ip = self.random_ip()
            print(f"  {Colors.GREEN}►{Colors.NC} {proto} | Size: {size}B | Src: {ip} {Colors.GREEN}[ANALYZED]{Colors.NC}")
            time.sleep(0.2)

    def backup_status(self):
        """Simuliert Backup-Status"""
        print(f"{Colors.BRIGHT_GREEN}[BKUP]{Colors.NC} {Colors.CYAN}Backup-Status überprüfen...{Colors.NC}")
        hours_ago = random.randint(0, 24)
        last_backup = (datetime.now() - timedelta(hours=hours_ago)).strftime('%H:%M:%S')
        size = random.randint(0, 500)
        print(f"  {Colors.GREEN}►{Colors.NC} Letzte Sicherung: {last_backup}")
        print(f"  {Colors.GREEN}►{Colors.NC} Größe: {size}GB")
        print(f"  {Colors.GREEN}►{Colors.NC} Integrität: {Colors.GREEN}[VERIFIED]{Colors.NC}")
        time.sleep(0.5)

    def security_score(self):
        """Simuliert Sicherheits-Bewertung"""
        print(f"{Colors.BRIGHT_GREEN}[SCORE]{Colors.NC} {Colors.CYAN}Sicherheits-Bewertung...{Colors.NC}")
        score = random.randint(70, 100)
        print(f"  {Colors.GREEN}►{Colors.NC} Firewall: {Colors.GREEN}[ACTIVE]{Colors.NC}")
        print(f"  {Colors.GREEN}►{Colors.NC} Encryption: {Colors.GREEN}[ENABLED]{Colors.NC}")
        print(f"  {Colors.GREEN}►{Colors.NC} Updates: {Colors.GREEN}[CURRENT]{Colors.NC}")
        print(f"  {Colors.GREEN}►{Colors.NC} Security Score: {score}/100 {Colors.GREEN}[GOOD]{Colors.NC}")
        time.sleep(0.5)

    def run(self):
        """Hauptschleife"""
        try:
            self.clear_screen()
            self.show_banner()
            time.sleep(1)
            self.initialize()

            # Liste aller Operationen
            operations = [
                self.network_scan,
                self.process_monitoring,
                self.firewall_log,
                self.file_integrity,
                self.connection_analysis,
                self.encryption_status,
                self.authentication_log,
                self.bandwidth_monitor,
                self.intrusion_detection,
                self.database_query,
                self.system_resources,
                self.certificate_check,
                self.packet_analysis,
                self.backup_status,
                self.security_score
            ]

            # Endlosschleife
            while True:
                # Zufällige Operation ausführen
                operation = random.choice(operations)
                operation()
                print()
                time.sleep(random.uniform(1, 3))

        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}[EXIT]{Colors.NC} {Colors.CYAN}System Monitor beendet{Colors.NC}")
            print(f"{Colors.GREEN}[OK] Alle Verbindungen geschlossen{Colors.NC}\n")
            sys.exit(0)


def main():
    """Main Entry Point"""
    monitor = MatrixMonitor()
    monitor.run()


if __name__ == "__main__":
    main()
