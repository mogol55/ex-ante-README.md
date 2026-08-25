# REA v0.1 — Protocollo di falsificazione

## Obiettivo

Determinare se il governo ex ante della singola interazione con l'IA produce un effetto metodologico indipendente dalla semplice ottimizzazione del prompt.

## Disegno minimo

Tre condizioni sperimentali:

### A — Controllo

Richiesta naturale/non governata.

### B — Prompt engineering

Richiesta ottimizzata direttamente, con contenuto informativo e obiettivo comparabili.

### C — REA

1. problema;
2. obiettivo;
3. vincoli;
4. criteri;
5. verifica;
6. trasformazione finale in richiesta al modello.

Il confronto decisivo è **C vs B**, non soltanto C vs A.

## Campione

Protocollo iniziale consigliato:

- almeno 30 problemi;
- almeno 5 categorie di problema;
- almeno 4 famiglie di modelli;
- più esecuzioni per problema;
- ordine randomizzato;
- valutazione cieca.

## Categorie

1. analisi informativa;
2. classificazione;
3. pianificazione;
4. confronto tra alternative;
5. decisione vincolata.

## Variabili indipendenti

- condizione sperimentale;
- modello;
- categoria;
- difficoltà;
- lunghezza input;
- quantità di informazione disponibile.

## Variabili dipendenti

- accuratezza;
- completezza;
- rispetto dei vincoli;
- verificabilità;
- stabilità tra run;
- stabilità cross-model;
- utilità decisionale.

## Controlli

Devono essere controllati almeno:

- lunghezza del prompt;
- contenuto informativo;
- modello;
- temperatura e parametri rilevanti;
- difficoltà del problema;
- criterio di valutazione.

## Test di autonomia

Costruire un prompt B semanticamente equivalente al prompt C, mantenendo:

- stesso problema;
- stesso obiettivo;
- stessi vincoli;
- stessi criteri;
- stessa procedura di verifica;
- informazione comparabile;
- lunghezza comparabile quando tecnicamente possibile.

Se `C ≈ B` su tutte le metriche, l'ipotesi di un vantaggio autonomo di REA viene fortemente indebolita.

Se `C > B` in modo replicabile, emerge evidenza a favore dell'autonomia metodologica.

## Test cross-model

Lo stesso stato metodologico REA deve essere applicato a più modelli senza modificare sostanzialmente il significato di `(P,O,V,C,E)`.

Non è richiesto che gli output siano identici.

## Valutazione

I criteri devono essere definiti prima dell'esecuzione. I valutatori dovrebbero essere ciechi rispetto alla condizione sperimentale e al modello.

## Preregistrazione

Prima del test devono essere congelati:

- ipotesi;
- dataset;
- metriche;
- soglie;
- procedura;
- criteri di esclusione;
- analisi primaria.

Le modifiche successive devono essere dichiarate come analisi esplorative.

## Falsificazione forte

La teoria forte viene considerata falsificata se, dopo i controlli e la replicazione:

`ΔY_REA|controlli ≈ 0`

oppure se il vantaggio è interamente spiegabile da prompt engineering, quantità di informazione, lunghezza o caratteristiche del singolo modello.

## Risultato negativo

Un risultato negativo non deve essere nascosto né reinterpretato come successo. Costituisce un esito valido del programma di ricerca.

## Regola di integrità

La teoria non deve essere modificata dopo aver osservato i risultati allo scopo di evitare la falsificazione.
