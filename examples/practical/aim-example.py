import json
import subprocess
import sys
import tempfile


def write_fixture(path):
    from aim import Run
    run = Run(repo=path, system_tracking_interval=None, log_system_params=False, capture_terminal_logs=False)
    run['fixture'] = 'synthetic-loss'
    for step, value in enumerate([1.0, 0.5, 0.25]):
        run.track(value, name='loss', step=step, context={'subset': 'train'})
    run.close()


def read_fixture(path):
    from aim import Run, Repo
    repo = Repo(path)
    hashes = repo.list_all_runs()
    assert len(hashes) == 1
    run = Run(hashes[0], repo=repo, system_tracking_interval=None, log_system_params=False, capture_terminal_logs=False)
    from aim.storage.context import Context
    sequence = run.get_metric('loss', Context({'subset': 'train'}))
    steps, (values, epochs, timestamps) = sequence.data.items_list()
    assert list(steps) == [0, 1, 2]
    assert list(values) == [1.0, 0.5, 0.25]
    print(json.dumps({'runs': len(hashes), 'steps': list(steps), 'loss': list(values)}))
    run.close()


if len(sys.argv) == 3 and sys.argv[1] == '--write':
    write_fixture(sys.argv[2])
elif len(sys.argv) == 3 and sys.argv[1] == '--read':
    read_fixture(sys.argv[2])
else:
    with tempfile.TemporaryDirectory(prefix='awesome-aim-') as path:
        for mode in ['--write', '--read']:
            subprocess.run([sys.executable, __file__, mode, path], check=True, timeout=60)
