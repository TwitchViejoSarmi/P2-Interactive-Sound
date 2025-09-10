import os
import random
from typing import Optional, Tuple
from .audio_engine import AudioEngine
from .story import LINES, LINES_DECISION1, LINES_DECISION2, LINES_DECISION3, Line

ASSETS_SFX = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "assets", "sfx")
ASSETS_MUSIC = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "assets", "music")

def sfx_path(name: str) -> str:
    p = os.path.abspath(os.path.join(ASSETS_SFX, name))
    if os.path.exists(p):
        return p
    return os.path.abspath(os.path.join(ASSETS_MUSIC, name))

class Game:
    def __init__(self) -> None:
        self.audio = AudioEngine()
        self.decision1: Optional[str] = None
        self.decision2: Optional[str] = None
        self.decision3: Optional[str] = None
        self.decision4: Optional[str] = None
        self.luck: float = 0.0
    
    def _print_intro(self) -> None:
        print("""==========================================
    BETTING ECHOES — NOVELA SONORA
==========================================
Controles: Presiona ENTER para avanzar.
En decisiones, escribe 1 o 2 y ENTER.
Aviso: Historia ficticia sobre apuestas.
        """)
    
    def _play_line(self, line: Line) -> None:
        self.audio.play(
            filepath=sfx_path(line.sfx),
            position=line.position,
            gain=line.gain,
            loop=line.loop,
            background=True
        )
        input()

    def run(self) -> None:
        try:
            self._print_intro()
            for idx, line in enumerate(LINES):
                if idx == 3 or idx == 8 or idx == 19:
                    self.audio.stop_all()
                print(line.text)
                self._play_line(line)
            self.decision1 = self._decision_one()
            for l in LINES_DECISION1[self.decision1]:
                print(l.text)
                self._play_line(l)
            self.decision2 = self._decision_two()
            for l in LINES_DECISION2[self.decision2]:
                print(l.text)
                self._play_line(l)
            self.decision3 = self._decision_three()
            for l in LINES_DECISION3[self.decision3]:
                print(l.text)
                self._play_line(l)
            self.decision4 = self._decision_four()
            self._resolution()
        finally:
            self.audio.close()
    
    def _decision_one(self) -> str:
        print("""DECISIÓN 1:
                1) Plantarte de inmediato, aunque apenas empieza.
                2) Ir con todo desde la primera mano.
                Elige (1/2):""")
        while True:
            ans = input().strip()
            if ans in ("1","2"):
                if ans == "1":
                    self.luck += round(random.uniform(0.05, 0.1), 2)
                else:
                    self.luck += round(random.uniform(0.0, 0.25), 2)
                self.audio.stop_all()
                return ans
            print("Por favor, escribe 1 o 2 y presiona ENTER.")
    
    def _decision_two(self) -> str:
        print("""DECISIÓN 2:
                1) Confiar en tu instinto y leer las cartas a tu manera.
                2) Observar al crupier y seguir su ritmo.
                Elige (1/2):""")
        while True:
            ans = input().strip()
            if ans in ("1", "2"):
                if ans == "1":
                    self.luck += round(random.uniform(0.0, 0.25), 2)
                else:
                    self.luck += round(random.uniform(0.05, 0.1), 2)
                self.audio.stop_all()
                return ans
            print("Por favor, escribe 1 o 2 y presiona ENTER.")

    def _decision_three(self) -> str:
        print("""DECISIÓN 3:
                1) Mantener la calma, esperar la siguiente ronda.
                2) Subir la apuesta antes de tiempo.
                Elige (1/2):""")
        while True:
            ans = input().strip()
            if ans in ("1","2"):
                if ans == "1":
                    self.luck += round(random.uniform(0.05, 0.1), 2)
                else:
                    self.luck += round(random.uniform(0.0, 0.25), 2)
                self.audio.stop_all()
                return ans
            print("Por favor, escribe 1 o 2 y presiona ENTER.")

    def _decision_four(self) -> str:
        print("""DECISIÓN 4 (final):
                1) Levantarte y salir con lo que queda de ti.
                2) Apostarlo todo en la última mano.
                Elige (1/2):""")
        while True:
            ans = input().strip()
            if ans in ("1","2"):
                if ans == "2":
                    self.luck += round(random.uniform(0.0, 0.25), 2)
                self.audio.stop_all()
                return ans
            print("Por favor, escribe 1 o 2 y presiona ENTER.")

    def _resolution(self) -> None:
        print("\n================= DESENLACE =================\n")
        result = random.random() < self.luck
        if self.decision4 == "1":
            self._ending_calm()
        else:
            if result:
                self._ending_risk()
            else:
                self._bad_ending()

    def _ending_calm(self) -> None:
        texts = [
            "Te levantas despacio. La silla se queja apenas.",
            "El crupier asiente, como si entendiera.",
            "Dejas una última ficha sobre la mesa: una despedida.",
            "Caminas hacia la salida; el murmullo se apaga detrás.",
            "La puerta se abre al aire húmedo de la noche.",
            "La lluvia te recibe, fría pero limpia.",
            "Respiras hondo. Esta vez te eliges a ti.",
            "No ganaste dinero, pero recuperas el pulso.",
            "Prometes avisar a tu hermana: estás bien.",
            "Te alejas entre charcos. La ciudad sigue, y tú también.",
            "FIN A: La elección de detenerse."
        ]
        sfxs = [
            ("chair_squeak.wav", (-0.3, 0.0, -0.4)),
            ("table_tap.wav", (0.0, 0.0, -0.6)),
            ("coin_spin.wav", (-0.6, 0.0, -0.4)),
            ("footsteps_right.wav", (0.7, 0.0, -0.2)),
            ("door_far.wav", (0.0, 0.0, 0.8)),
            ("rain_outside.wav", (-0.8, 0.0, 0.8)),
            ("breathe.wav", (0.0, 0.2, -0.2)),
            ("heartbeat_soft.wav", (0.0, 0.2, -0.2)),
            ("whisper_behind.wav", (0.0, 0.0, 0.6)),
            ("footsteps_right.wav", (0.9, 0.0, 0.0)),
            ("ambience_casino.wav", (0.0, 0.0, 0.0)),
        ]
        for t, (s, p) in zip(texts, sfxs):
            print(t)
            if s == "door_far.wav" or s == "ambience_casino.wav":
                self.audio.stop_all()
            self.audio.play(sfx_path(s), position=p, gain=0.6, loop=False, background=True)
            input()
        self.audio.stop_all()

    def _ending_risk(self) -> None:
        texts = [
            "Te quedas. Sientes el calor de la mesa en las palmas.",
            "Las cartas vuelan; el mundo es una chispa contenida.",
            "Miras al crupier y asientes. Va.",
            "La ficha cae y rueda hasta tu destino.",
            "El salón guarda silencio: un segundo eterno.",
            "La última carta voltea como una moneda en el aire.",
            "Ganas, pero entiendes que también podrías haber perdido.",
            "Recoges las fichas con manos tranquilas.",
            "Te pones de pie. El murmullo vuelve: te disuelve.",
            "Camino a la salida, la lluvia te golpea como un bautizo.",
            "FIN B: La apuesta final no fue contra el azar, sino contigo."
        ]
        sfxs = [
            ("heavy_breathe.wav", (0.0, 0.0, -0.5)),
            ("card_flip.wav", (-0.6, 0.0, -0.4)),
            ("table_tap.wav", (0.0, 0.0, -0.6)),
            ("coin_spin.wav", (0.0, -0.1, -0.3)),
            ("crowd_murmur.wav", (0.0, 0.0, -0.8)),
            ("card_flip.wav", (-0.5, 0.0, -0.5)),
            ("cash_register.wav", (-0.3, 0.0, -0.4)),
            ("chips_clatter.wav", (0.3, 0.0, -0.4)),
            ("crowd_murmur.wav", (0.0, 0.0, -0.7)),
            ("rain_outside.wav", (-0.8, 0.0, 0.8)),
            ("ambience_casino.wav", (0.0, 0.0, 0.0)),
        ]
        for t, (s, p) in zip(texts, sfxs):
            print(t)
            if s == "rain_outside.wav" or s == "ambience_casino.wav":
                self.audio.stop_all()
            self.audio.play(sfx_path(s), position=p, gain=0.6, loop=False, background=True)
            input()
        self.audio.stop_all()

    def _bad_ending(self) -> None:
        texts = [
            "Te quedas. Sientes el calor de la mesa en las palmas.",
            "Las cartas vuelan; el mundo es una chispa contenida.",
            "Miras al crupier y asientes. Va.",
            "La ficha cae y rueda hasta tu destino.",
            "El salón guarda silencio: un segundo eterno.",
            "La última carta voltea como una moneda en el aire.",
            "Perdiste, tu obsesión por la victoria te jugó una mala pasada.",
            "Ves cómo el crupier recoge todas y cada una de tus fichas.",
            "Te pones de pie. El murmullo vuelve: te disuelve.",
            "Caminas hacia la salida; el murmullo se apaga detrás.",
            "La puerta se abre al aire húmedo de la noche.",
            "La lluvia te recibe, el frío te recuerda lo débil que fuiste.",
            "Debes avisarle a tu hermana: ¿Cómo se lo vas a decir?",
            "Te alejas entre charcos. La ciudad sigue... ¿tú también?",
            "FIN C: 'Cuando puedes parar no quieres, y cuando quieres parar no puedes.' Luke Davies"
        ]
        sfxs = [
            ("heavy_breathe.wav", (0.0, 0.0, -0.5)),
            ("card_flip.wav", (-0.6, 0.0, -0.4)),
            ("table_tap.wav", (0.0, 0.0, -0.6)),
            ("coin_spin.wav", (0.0, -0.1, -0.3)),
            ("crowd_murmur.wav", (0.0, 0.0, -0.8)),
            ("card_flip.wav", (-0.5, 0.0, -0.5)),
            ("table_tap.wav", (-0.3, 0.0, -0.4)),
            ("chips_clatter.wav", (0.3, 0.0, 0.4)),
            ("crowd_murmur.wav", (0.0, 0.0, -0.7)),
            ("footsteps_right.wav", (0.7, 0.0, -0.2)),
            ("door_far.wav", (0.0, 0.0, 0.8)),
            ("rain_outside.wav", (-0.8, 0.0, 0.8)),
            ("whisper_behind.wav", (0.0, 0.0, 0.6)),
            ("footsteps_right.wav", (0.9, 0.0, 0.0)),
            ("ambience_casino.wav", (0.0, 0.0, 0.0)),
        ]
        for t, (s, p) in zip(texts, sfxs):
            print(t)
            if s == "door_far.wav" or s == "ambience_casino.wav":
                self.audio.stop_all()
            self.audio.play(sfx_path(s), position=p, gain=0.6, loop=False, background=True)
            input()
        self.audio.stop_all()