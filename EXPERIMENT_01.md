# REA v0.1 — Experiment 01

**Stato:** PROTOCOLLO DA ESEGUIRE — NON VALIDATO  
**Versione:** 0.1  
**Data di congelamento del protocollo:** 2026-08-25  
**Progetto:** PENSAI / REA

## 1. Domanda di ricerca

Il governo ex ante di una singola interazione con l'IA produce un vantaggio misurabile che non è spiegato interamente dalla qualità del prompt engineering?

## 2. Ipotesi primaria

**H1:** a parità di problema e informazione, la condizione REA produce un risultato migliore della condizione di prompt engineering equivalente (B), almeno su una o più metriche primarie preregistrate.

**H0:** ogni differenza osservata tra REA e prompt engineering equivalente è spiegabile da contenuto informativo, struttura, lunghezza, qualità del prompt o caratteristiche del modello.

## 3. Condizioni

### A — CONTROLLO

Richiesta naturale formulata senza procedura REA esplicita e senza ottimizzazione specialistica.

### B — PROMPT ENGINEERING

Richiesta costruita da un operatore competente di prompt engineering. Deve contenere, quando necessario per il compito, le stesse informazioni sostanziali disponibili a C. Deve essere ottimizzata direttamente come prompt, senza imporre il processo REA come struttura metodologica.

### C — REA

Prima della generazione vengono esplicitamente definiti:

1. problema;
2. obiettivo;
3. vincoli;
4. criteri;
5. verifica.

Solo dopo viene costruita la richiesta al modello.

## 4. Confronto decisivo

Il confronto principale è:

**C vs B**

A serve come baseline descrittiva. Non è sufficiente dimostrare che C > A.

## 5. Campione pilota

30 problemi, distribuiti in almeno 5 categorie:

- analisi informativa;
- classificazione;
- pianificazione;
- confronto tra alternative;
- decisione vincolata.

Obiettivo successivo: replicazione su un campione più ampio dopo il pilota.

## 6. Modelli

Il protocollo richiede almeno 4 famiglie/modelli indipendenti disponibili per il test. Il modello deve essere registrato per ogni esecuzione.

L'agnosticità non richiede output identici: richiede che il governo REA possa essere mantenuto mentre cambia il modello.

## 7. Randomizzazione

L'ordine di presentazione dei problemi e delle condizioni deve essere randomizzato quando tecnicamente possibile.

Le risposte devono essere identificate con codici anonimi durante la valutazione.

## 8. Metriche primarie

Ogni risposta viene valutata separatamente su:

1. **Accuratezza** — correttezza rispetto alla soluzione o al criterio di riferimento.
2. **Completezza** — requisiti sostanziali soddisfatti.
3. **Rispetto dei vincoli** — vincoli espliciti rispettati.
4. **Verificabilità** — possibilità di stabilire, usando criteri definiti prima del test, se la risposta soddisfa l'obiettivo.
5. **Stabilità** — variazione dell'esito tra esecuzioni e modelli, dove applicabile.

L'utilità decisionale può essere registrata come metrica secondaria, ma non sostituisce le metriche primarie.

## 9. Controlli

Devono essere registrati e, ove possibile, bilanciati:

- modello e versione;
- parametri rilevanti;
- lunghezza del prompt;
- quantità di informazione fornita;
- categoria e difficoltà del problema;
- numero di run;
- eventuale uso di strumenti esterni;
- data e ora dell'esecuzione.

## 10. Test di equivalenza informativa

Per B e C deve essere verificato che non vi siano differenze sostanziali nella conoscenza messa a disposizione del modello.

Se B contiene meno informazioni di C, il confronto C > B non può essere interpretato come prova dell'autonomia di REA.

## 11. Test di equivalenza del prompt

B e C devono essere costruiti in modo da evitare che la sola superiorità stilistica o la maggiore lunghezza determini il risultato.

Quando possibile saranno prodotti anche confronti a lunghezza comparabile.

## 12. Valutazione cieca

Il valutatore non deve conoscere la condizione sperimentale né il modello che ha prodotto la risposta.

Per i compiti con risposta oggettiva si deve privilegiare una chiave di valutazione automatica o un criterio deterministico verificabile.

## 13. Criterio di interpretazione

### Supporto preliminare a REA

Si ottiene se C supera B in modo replicabile su almeno una metrica primaria preregistrata senza essere spiegabile da una differenza di informazione, lunghezza, modello o difficoltà.

### Risultato inconclusivo

Se C supera B ma il risultato è piccolo, instabile, dipendente da un singolo modello o confuso da differenze di prompt/informazione.

### Evidenza contro l'autonomia di REA

Se C non supera B dopo i controlli oppure se il vantaggio osservato è interamente spiegabile dalle variabili di controllo.

### Falsificazione forte

La teoria forte di REA è falsificata se esperimenti replicati mostrano che il governo ex ante non produce alcun effetto indipendente rispetto a prompt engineering semanticamente equivalente.

## 14. Regole anti-hindsight

Prima di raccogliere i risultati non devono essere modificati:

- ipotesi primaria;
- metriche primarie;
- criteri di esclusione;
- criteri di interpretazione.

Qualsiasi analisi successiva non prevista sarà marcata come **esplorativa**.

## 15. Registro dei risultati

Per ogni esecuzione devono essere conservati almeno:

`problem_id | condition | model | run_id | prompt | output | metrics | evaluator | timestamp`

I dati grezzi non devono essere sostituiti dalla sola sintesi statistica.

## 16. Limiti dichiarati

Questo è un **esperimento pilota**, non una validazione definitiva.

Un risultato positivo non dimostra da solo che REA sia un paradigma generale. Un risultato negativo non dimostra che ogni forma di governo ex ante sia inutile: falsifica soltanto la formulazione testata entro le condizioni dell'esperimento.

## 17. Regola fondamentale

**Non si modifica REA per ottenere un risultato positivo.**

Il risultato dell'esperimento deve determinare l'evoluzione successiva della teoria.

## 18. Sequenza

`THEORY v0.1 → EXPERIMENT 01 → DATA → ANALYSIS → VERDICT`

**VIA UNICA: REA → FALSIFICAZIONE**
