"""Compare every reported observation with the versioned reproduction contract."""
import json
from pathlib import Path


def check_result(name, observed):
    expected = json.loads(Path(__file__).with_name('expected.json').read_text())[name]
    if observed != expected:
        raise AssertionError(f'{name}: expected {expected!r}, observed {observed!r}')
    print(json.dumps(observed))
