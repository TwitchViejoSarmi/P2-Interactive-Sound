import threading
import time
from typing import Tuple
from openal import oalInit, oalQuit, oalOpen, Listener

Vector3 = Tuple[float, float, float]

class AudioEngine:
    def __init__(self) -> None:
        self._ctx = oalInit()
        self._sources = []
        self.listener = Listener()
        self.listener.set_position((0.0,0.0,0.0))
        self.listener.set_orientation((0.0,0.0,-1.0,0.0,1.0,0.0))
        self._lock = threading.Lock()
    
    def play(self, filepath: str, position: Vector3 = (0.0, 0.0, -1.0), gain: float = 1.0, loop: bool = False, background: bool = True):
        def _runner():
            src = oalOpen(filepath)
            if not src:
                return
            src.set_position(position)
            src.set_gain(gain)
            src.set_looping(loop)
            with self._lock:
                self._sources.append(src)
            src.play()
            if loop:
                while src.get_state() == 4114:
                    time.sleep(0.1)
            else:
                src.wait()
            with self._lock:
                try:
                    self._sources.remove(src)
                except ValueError:
                    pass
                src.stop()
                src.destroy()

        if background:
            t = threading.Thread(target=_runner, daemon=True)
            t.start()
        else:
            _runner()

    def _stop_all(self) -> None:
        with self._lock:
            for s in list(self._sources):
                try:
                    s.stop()
                    s.destroy()
                except Exception:
                    pass
            self._sources.clear()
    
    def close(self) -> None:
        self._stop_all()
        oalQuit()