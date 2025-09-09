from dataclasses import dataclass
from typing import List, Tuple, Dict

@dataclass
class Line:
    text: str
    sfx: str
    position: Tuple[float, float, float]
    gain: float = 1.0
    loop: bool = False

# Historia base
LINES: List[Line] = [
    Line("Empiezas la noche frente al casino del barrio. La lluvia cae leve.", "rain_outside.wav", (-1.0, 0.0, 1.0), 0.6, True),
    Line("Respiras hondo. Te prometiste no apostar más, pero aquí estás.", "heartbeat_soft.wav", (0.0, 0.0, -0.5), 0.4, False),
    Line("Abres la puerta y entra el murmullo de gente y máquinas.", "door_far.wav", (0.0, 0.0, 1.0), 0.8, False),
    Line("El ambiente del salón te envuelve.", "ambience_casino.wav", (0.0, 0.0, 0.0), 0.5, True),
    Line("Un crupier ríe a tu izquierda; a la derecha, un tintinear de fichas.", "chips_clatter.wav", (1.0, 0.0, 0.0), 0.7, False),
    Line("El anuncio de una mesa te llama desde el fondo.", "crowd_murmur.wav", (0.0, 0.0, -1.0), 0.6, False),
    Line("Caminas despacio, mirando las luces y los rostros cansados.", "footsteps_right.wav", (0.8, 0.0, -0.2), 0.7, False),
    Line("Recuerdas la promesa a tu hermana: 'solo mirar'.", "whisper_behind.wav", (0.0, 0.0, 1.0), 0.5, False),
    Line("Te sientas en una mesa pequeña de cartas.", "chair_squeak.wav", (-0.4, 0.0, -0.6), 0.6, False),
    Line("El crupier baraja con precisión.", "card_flip.wav", (-0.7, 0.0, -0.5), 0.8, False),
    Line("Tus manos tiemblan un poco.", "heartbeat_soft.wav", (0.0, -0.2, -0.4), 0.3, False),
    Line("Una voz detrás susurra: 'La primera es gratis'.", "whisper_behind.wav", (0.0, 0.0, 0.6), 0.5, False),
    Line("Miras tus fichas: apenas lo justo para una mano.", "coin_spin.wav", (0.0, -0.1, -0.3), 0.7, False),
    Line("El juego empieza. Dos cartas frente a ti.", "card_flip.wav", (-0.5, 0.0, -0.6), 0.8, False),
    Line("La mesa huele a tabaco frío y a nervios.", "crowd_murmur.wav", (0.0, 0.0, -0.7), 0.4, False),
    Line("Recuerdas que viniste a buscar respuestas, no fortuna.", "ambience_casino.wav", (0.0, 0.0, 0.0), 0.4, False),
    Line("El crupier pregunta si te plantas o vas con todo.", "chips_clatter.wav", (0.3, 0.0, -0.5), 0.6, False),
    Line("Sientes un golpeteo en la sien.", "heartbeat_soft.wav", (0.0, 0.3, -0.2), 0.3, False),
    Line("Una sirena suena lejos, como recordándote el mundo afuera.", "siren_far_right.wav", (1.0, 0.0, -0.2), 0.4, False),
    Line("Tu primera decisión se acerca.", "tension_stinger.wav", (0.0, 0.0, -0.5), 0.7, False),
]

LINES_DECISION1: Dict[str, List[Line]] = {
    "1": [
        Line("Decides contenerte, respirando con calma.", "breath.wav", (0,0,-0.5), 0.5, False),
        Line("El murmullo parece lejano, como si el salón se alejara.", "crowd_murmur.wav", (0,0,-0.7), 0.4, False),
    ],
    "2": [
        Line("Te lanzas con ímpetu, el corazón se acelera.", "heartbeat_soft.wav", (0,0,-0.5), 0.7, False),
        Line("Las miradas de la mesa se clavan en ti con expectación.", "crowd_murmur.wav", (0,0,-0.7), 0.5, False),
    ]
}

LINES_DECISION2: Dict[str, List[Line]] = {
    "1": [
        Line("Confías en tu instinto, las cartas parecen hablarte.", "breath.wav", (0,0,-0.5), 0.5, False),
        Line("La tensión baja un poco; te concentras en ti mismo.", "ambience_casino.wav", (0,0,0), 0.4, False),
    ],
    "2": [
        Line("Imitas el ritmo del crupier, buscando señales en su mirada.", "chips_clatter.wav", (0.3,0,-0.5), 0.6, False),
        Line("Sientes que el destino ya está marcado por otros.", "whisper_behind.wav", (0,0,0.6), 0.5, False),
    ]
}

LINES_DECISION3: Dict[str, List[Line]] = {
    "1": [
        Line("Mantienes la calma, esperando la siguiente jugada.", "heartbeat_soft.wav", (0,0,-0.5), 0.4, False),
        Line("El tiempo se estira; cada segundo parece un alivio.", "ambience_casino.wav", (0,0,0), 0.3, False),
    ],
    "2": [
        Line("Subes la apuesta de golpe; la mesa reacciona con un murmullo.", "coin_spin.wav", (0.5,0,-0.5), 0.7, False),
        Line("El aire se espesa, todos te observan en silencio.", "crowd_murmur.wav", (0,0,-0.7), 0.5, False),
    ]
}
