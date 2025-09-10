import threading
import time
from typing import Tuple, List
from openal import oalInit, oalQuit, oalOpen, Listener, alDistanceModel

Vector3 = Tuple[float, float, float]

class AudioEngine:
    def __init__(self) -> None:
        self._ctx = oalInit()
        self._sources : List[Tuple[object, threading.Event]] = []
        self.listener = Listener()
        self.listener.set_position((0.0,0.0,0.0))
        self.listener.set_orientation((0.0,0.0,-1.0,0.0,1.0,0.0))
        self._lock = threading.Lock()
    
    def play(self, filepath: str, position: Vector3 = (0.0, 0.0, -1.0), gain: float = 1.0, loop: bool = False, background: bool = True):
        stop_src_ev = threading.Event()
        def _runner():
            src = oalOpen(filepath)
            if not src:
                return
            src.set_position(position)
            src.set_gain(gain)
            src.set_looping(loop)
            with self._lock:
                self._sources.append((src, stop_src_ev))
            src.play()
            try:
                while src.get_state() == 4114 and not stop_src_ev.is_set():
                    time.sleep(0.1)
            finally:
                with self._lock:
                    try:
                        self._sources.remove((src, stop_src_ev))
                    except ValueError:
                        pass
                    try:
                        src.stop()
                    except Exception:
                        pass
                    try:
                        src.destroy()
                    except Exception:
                        pass

        if background:
            t = threading.Thread(target=_runner, daemon=True)
            t.start()
        else:
            _runner()

    def stop_all(self) -> None:
        with self._lock:
            for s, ev in list(self._sources):
                try:
                    ev.set()
                except Exception:
                    pass
                try:
                    s.set_looping(False)
                except Exception:
                    pass
                try:
                    s.stop()
                except Exception:
                    pass

    def close(self) -> None:
        self._stop_all()
        oalQuit()