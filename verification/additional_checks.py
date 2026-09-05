"""Seed-clustered fidelity and displayed-figure checks from raw records."""
import json, itertools
from pathlib import Path
import numpy as np
OUT=Path(__file__).resolve().parent; ROOT=OUT.parent
def load(p):return json.loads((ROOT/p).read_text())
def stats(x):
    x=np.array(x);ci=np.percentile(np.random.RandomState(0).choice(x,(5000,len(x))).mean(1),[2.5,97.5])
    return dict(n=len(x),mean=float(x.mean()),ci=ci.tolist(),wins=int((x>0).sum()),per_seed=x.tolist())
def train(s):return np.sort(np.random.RandomState(s).permutation(64)[16:])
out={}
for folder,base,seeds in [('results_v3_confirm2','results_v3_confirm',range(10,30)),('results_replicate','results_replicate',range(100,120))]:
    vals=[]
    for s in seeds:
        d=[]
        for sel,fr in itertools.product(('random','success','hard'),('accumulate','rewrite')):
            v={}
            for rd,fd in [('sender',base),('both',folder)]:
                slot='fixed' if sel=='random' else 'dynamic'
                j=load(f'{fd}/small__sel-{sel}_slots-{slot}_fresh-{fr}_cap-19_noise-0.0_rd-{rd}_seed{s}.json')
                E=[r for r in j['log'] if 'per_obj_acc' in r]
                v[rd]=np.mean([np.mean([child['language'][o]==m for o,m,_ in p['record']]) for p,child in zip(E,E[1:])])
            d.append(v['both']-v['sender'])
        vals.append(np.mean(d))
    out[folder+'_K8_seed_clustered']=stats(vals)

vals={'fresh':[],'stale':[]}
for file in ('results_v3/probe44_raw.json','results_v3_confirm2/k17_raw.json','results_replicate/k14_k17_power_raw.json'):
    j=load(file);P=None
    if isinstance(j[0],dict):P,j=j
    r={(s,a,i):np.array(l) for s,a,i,l in j if a in vals}
    for s in sorted({s for s,a,i in r}):
        if P:
            v=P[str(s)];p=np.array(v[1] if len(v)==2 else v[0])
        else:
            f=next((ROOT/('results_v3' if s<10 else 'results_v3_confirm')).glob(f'small__generations_seed{s}.json'))
            p=np.array([x for x in json.loads(f.read_text())['log'] if x['gen']==0][-1]['language'])
        obj=np.sort(np.random.RandomState(3000+s).choice(train(s),19,replace=False))
        for a in vals: vals[a].append(np.mean([np.all(r[s,a,i][obj]==p[obj],axis=1).mean() for i in (1,2)]))
out['Figure4d']={k:{'n_seeds':len(v),'mean':float(np.mean(v))} for k,v in vals.items()}
OUT.joinpath('additional_results.json').write_text(json.dumps(out,indent=2)+'\n')
for k,v in out.items():print(k,{a:b for a,b in v.items() if a!='per_seed'})
