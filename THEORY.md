# REA v0.1 — Teoria

## 1. Definizione

Il Ragionamento Ex Ante Agnostico (REA) ipotizza che il governo della singola interazione con un sistema di IA possa costituire un livello metodologico precedente alla generazione dell'output e separabile dal modello utilizzato.

Il governo ex ante definisce almeno:

- **P** — problema;
- **O** — obiettivo;
- **V** — vincoli;
- **C** — criteri di valutazione;
- **E** — procedura di verifica.

La richiesta **Q** inviata al modello è costruita come conseguenza di questi elementi.

## 2. Modello

Interazione ordinaria:

`Q → M → R`

Modello REA:

`(P,O,V,C,E) → Q → M → R → E(R)`

Dove M è il modello, R la risposta e E(R) la verifica dell'output.

## 3. Agnosticità

L'agnosticità non significa che modelli diversi debbano produrre la stessa risposta. Significa che lo stato metodologico `(P,O,V,C,E)` rimane definito mentre il modello M varia.

## 4. Tesi centrale

REA sostiene che il governo ex ante sia una variabile metodologica misurabile se il suo effetto resta osservabile dopo aver controllato qualità del prompt, contenuto informativo, lunghezza, modello e difficoltà del compito.

## 5. Ipotesi

### H1 — Effetto di governo

`Quality_REA > Quality_Control`

### H2 — Specificazione

`Ambiguity_REA < Ambiguity_Control`

### H3 — Verificabilità

`Verifiability_REA > Verifiability_Control`

### H4 — Robustezza cross-model

L'effetto REA deve essere osservabile su più famiglie di modelli.

### H5 — Stabilità

REA dovrebbe ridurre la sensibilità dell'esito a variazioni superficiali della formulazione.

### H6 — Autonomia rispetto al prompt engineering

Il test più forte richiede il confronto con un prompt non-REA semanticamente equivalente e professionalmente ottimizzato.

## 6. Ipotesi nulla

**H0:** ogni vantaggio osservato da REA è spiegabile dalla maggiore qualità, informazione, struttura o lunghezza del prompt e non dall'esistenza di un livello metodologico autonomo.

## 7. Falsificazione

La versione forte della teoria è falsificata se, dopo controlli adeguati:

1. REA non produce alcun vantaggio replicabile;
2. il vantaggio compare soltanto su un singolo modello;
3. il vantaggio scompare rispetto a un prompt semanticamente equivalente;
4. non migliora la verificabilità;
5. gli effetti sono interamente spiegabili dal prompt engineering.

## 8. Stato epistemico

Questa è una teoria candidata. Le evidenze disponibili sul prompting e sulla specificazione dei compiti sono compatibili con REA, ma non dimostrano l'esistenza di REA come livello metodologico autonomo.

**La validazione deve essere prodotta dall'esperimento, non dalla formulazione teorica.**
