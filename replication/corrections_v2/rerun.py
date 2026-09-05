"""Run an existing cached-data evaluator, redirecting result writes to audit outputs."""
import builtins, os, runpy, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent/"recomputed"
os.chdir(ROOT);sys.path.insert(0,str(ROOT))
real_open=builtins.open
def safe_open(file,mode='r',*args,**kwargs):
    if isinstance(file,(str,bytes,os.PathLike)) and any(x in mode for x in ('w','a','x','+')):
        p=Path(file).resolve()
        if p.is_relative_to(ROOT) and p.relative_to(ROOT).parts[0].startswith('results'):
            p=OUT/p.relative_to(ROOT);p.parent.mkdir(parents=True,exist_ok=True);file=p
        else:raise RuntimeError('Unexpected write: '+str(p))
    return real_open(file,mode,*args,**kwargs)
builtins.open=safe_open
runpy.run_path(str(ROOT/sys.argv[1]),run_name='__main__')
