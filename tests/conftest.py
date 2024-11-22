import sys
from pathlib import Path

# Добавляем папку `app` в пути поиска
sys.path.append(str(Path(__file__).parent.parent / "app"))
