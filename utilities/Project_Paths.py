from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
HMPSAC_DATA_DIR = DATA_DIR / "HMPSAC_breakdown"
HMPSAC_RESULTS_DIR = RESULTS_DIR / "HMPSAC"


def ensure_dir(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


def ensure_parent(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)
