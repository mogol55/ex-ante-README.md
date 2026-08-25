import json
from pathlib import Path
D=json.loads(Path('DATASET_01.json').read_text())
out=[]
for p in D['problems']:
    s=p['scenario']; o=p['objective']
    prompts={'A':f'{s} Cosa si puo concludere o quale decisione risponde all’obiettivo: {o}?','B':f'Analizza questi dati: {s} Determina {o}. Mostra i passaggi essenziali e non introdurre dati non forniti.','C':f'Problema: {s} Obiettivo: {o}. Vincoli: usare solo i dati forniti e rispettare tutte le condizioni esplicite. Criteri: risposta corretta e distinguere fatti, assunzioni e informazioni mancanti quando rilevanti. Verifica: ricontrolla dati, soglie, dipendenze e condizioni prima della risposta. Rispondi.'}
    for c in ('A','B','C'): out.append({'problem_id':p['problem_id'],'condition':c,'prompt':prompts[c]})
Path('PROMPTS_01.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in out))
