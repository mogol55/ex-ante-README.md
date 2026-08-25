import json
from pathlib import Path
D=json.loads(Path('DATASET_01.json').read_text())
rows=[json.loads(x) for x in Path('PROMPTS_01.jsonl').read_text().splitlines() if x.strip()]
ids={p['problem_id'] for p in D['problems']}
errors=[]
if len(rows)!=90: errors.append(f'count={len(rows)}')
if ids!={f'P{i:02d}' for i in range(1,31)}: errors.append('dataset IDs')
seen={(r.get('problem_id'),r.get('condition')) for r in rows}
expected={(f'P{i:02d}',c) for i in range(1,31) for c in 'ABC'}
if seen!=expected: errors.append('matrix mismatch')
if len(seen)!=90: errors.append('duplicates')
if any(not r.get('prompt','').strip() for r in rows): errors.append('empty prompt')
if any(r.get('problem_id') not in ids or r.get('condition') not in 'ABC' for r in rows): errors.append('invalid record')
print('90/90 PASS' if not errors else 'FAIL: '+', '.join(errors))
raise SystemExit(0 if not errors else 1)
