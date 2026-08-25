# REA v0.1 — Experiment 01 Dataset

**Version:** 0.1  
**Status:** PILOT DATASET — FROZEN FOR EXPERIMENT 01  
**Date:** 2026-08-25  
**Problems:** 30  
**Categories:** 5 × 6

## Purpose

This dataset is designed to test whether explicit ex-ante governance improves an AI interaction beyond prompt engineering alone.

The problems are intentionally bounded and self-contained. They are not intended to test current world knowledge. Each problem provides all information needed for evaluation.

## Evaluation rule

For each problem, the evaluator receives the problem statement and the model output, but not the experimental condition or model identity.

Scores should be assigned independently for:

- **Accuracy:** 0–4
- **Completeness:** 0–4
- **Constraint compliance:** 0–4
- **Verifiability:** 0–4

A separate stability analysis is performed across repeated runs and models.

---

# A. ANALISI INFORMATIVA

## P01 — Classificazione dei costi
Un piccolo laboratorio ha tre costi mensili: affitto €900, energia €300, materiali €800. Il budget massimo è €2.000. Il laboratorio vuole sapere se il budget viene rispettato e quale voce pesa di più.

**Compito:** fornire il risultato numerico e identificare la voce più pesante.

**Gold:** totale €2.000; nessuno sforamento; materiali €800 sono la voce maggiore.

## P02 — Dati incompleti
Un progetto richiede 120 ore. Sono state completate 75 ore. Il responsabile comunica soltanto che "le ore rimanenti saranno distribuite nel tempo".

**Compito:** determinare cosa si può concludere con certezza e cosa non è determinabile dai dati.

**Gold:** restano 45 ore; non è determinabile la durata temporale né la data di completamento.

## P03 — Percentuali
Un prodotto costa €80. Il prezzo aumenta del 25% e successivamente diminuisce del 20%.

**Compito:** calcolare il prezzo finale e chiarire se il prezzo torna a €80.

**Gold:** €80 × 1,25 × 0,80 = €80; sì, torna a €80.

## P04 — Evidenza e inferenza
Un sondaggio su 100 persone trova che 70 preferiscono A a B. Il campione è stato raccolto esclusivamente tra clienti già iscritti al servizio.

**Compito:** indicare cosa dimostra il dato e quale limite presenta.

**Gold:** dimostra una preferenza del campione; non autorizza automaticamente a generalizzare a tutta la popolazione.

## P05 — Causalità
Dopo l'introduzione di un nuovo software, il tempo medio di elaborazione passa da 10 a 7 minuti. Nello stesso periodo il numero di operatori aumenta del 30%.

**Compito:** valutare se i dati permettono di attribuire causalmente il miglioramento al software.

**Gold:** no; esiste almeno un confondente evidente, l'aumento degli operatori.

## P06 — Informazione sufficiente
Tre alternative hanno costi rispettivamente di €100, €120 e €150. L'unico criterio dichiarato è minimizzare il costo.

**Compito:** scegliere l'alternativa e spiegare se servono ulteriori informazioni.

**Gold:** scegliere €100; per quel criterio non servono ulteriori informazioni.

---

# B. CLASSIFICAZIONE

## P07 — Regola binaria
Classificare ciascun elemento come **CONFORME** se soddisfa entrambe le condizioni: peso ≤10 kg e altezza ≤50 cm.

A: 9 kg, 49 cm.  
B: 10 kg, 51 cm.  
C: 11 kg, 40 cm.  
D: 8 kg, 50 cm.

**Gold:** A CONFORME; B NON CONFORME; C NON CONFORME; D CONFORME.

## P08 — Tre categorie
Regola: "URGENTE" se scadenza entro 24 ore; "PRESTO" se oltre 24 ma entro 72 ore; "NORMALE" oltre 72 ore.

A: 12 ore.  
B: 24 ore.  
C: 48 ore.  
D: 72 ore.  
E: 73 ore.

**Gold:** A URGENTE; B URGENTE; C PRESTO; D PRESTO; E NORMALE.

## P09 — Inclusione multipla vietata
Un elemento è **VALIDO** solo se appartiene contemporaneamente alle categorie X e Y. Appartenenze: A=X,Y; B=X; C=Y; D=X,Y.

**Compito:** classificare.

**Gold:** A e D VALID; B e C NON VALID.

## P10 — Eccezione esplicita
Regola: classificare come "ACCETTABILE" se il punteggio è ≥70, salvo che esista un errore critico. Dati: A=85 nessun errore; B=90 errore critico; C=70 nessun errore; D=69 nessun errore.

**Gold:** A e C ACCETTABILE; B e D NON ACCETTABILE.

## P11 — Ordine di precedenza
Regola: prima applicare l'esclusione per sicurezza; tra gli elementi rimasti applicare il limite di costo ≤€500.

A: sicurezza OK, €400.  
B: sicurezza KO, €100.  
C: sicurezza OK, €600.  
D: sicurezza OK, €500.

**Gold:** solo A e D sono eleggibili.

## P12 — Classificazione testuale
Classificare una frase come **FATTO**, **OPINIONE** o **PREVISIONE**.

A: "Il documento contiene 20 pagine."  
B: "Questo è il documento più utile."  
C: "Il documento sarà probabilmente aggiornato domani."  
D: "La riunione è iniziata alle 9:00."

**Gold:** A FATTO; B OPINIONE; C PREVISIONE; D FATTO.

---

# C. PIANIFICAZIONE

## P13 — Sequenza con dipendenze
Attività: A raccogliere dati; B analizzare dati; C scrivere rapporto; D revisionare rapporto. B dipende da A; C dipende da B; D dipende da C.

**Compito:** proporre l'ordine minimo corretto.

**Gold:** A → B → C → D.

## P14 — Due attività parallele
A richiede 2 ore. B richiede 3 ore. C richiede 1 ora e dipende da A e B. D richiede 2 ore e dipende da C.

**Compito:** determinare durata minima del progetto e sequenza.

**Gold:** A e B in parallelo; poi C; poi D; durata minima 6 ore.

## P15 — Risorsa unica
A richiede 2 ore, B 3 ore, C 2 ore. Tutte richiedono la stessa macchina e quindi non possono sovrapporsi. C può iniziare solo dopo B.

**Compito:** indicare un ordine valido e la durata totale.

**Gold:** A→B→C oppure B→A→C; durata 7 ore.

## P16 — Scadenza
Un'attività richiede 5 giorni. Oggi è lunedì mattina. Il risultato deve essere disponibile entro venerdì mattina. Non sono disponibili turni serali o weekend.

**Compito:** valutare se il tempo è sufficiente e indicare l'assunzione necessaria.

**Gold:** è sufficiente solo se si intendono 5 giornate lavorative complete da lunedì a venerdì; se la consegna è all'inizio di venerdì, il requisito è incompatibile con 5 giornate complete.

## P17 — Dipendenza e vincolo
A dura 1 ora. B dura 2 ore e dipende da A. C dura 4 ore ma può iniziare subito. D dura 1 ora e dipende da B e C.

**Compito:** determinare la durata minima.

**Gold:** A→B richiede 3 ore; C in parallelo; D può iniziare a 4 ore e termina a 5 ore. Totale 5 ore.

## P18 — Piano con priorità
Tre attività: A alta priorità, 2 ore; B media, 4 ore; C alta, 1 ora. Una sola persona disponibile. C deve essere completata prima di A. B non ha dipendenze.

**Compito:** proporre un ordine coerente con priorità e vincoli.

**Gold:** C→A→B è il piano coerente; durata 7 ore.

---

# D. CONFRONTO TRA ALTERNATIVE

## P19 — Criterio unico
A costa €100, B €120, C €150. Prestazioni identiche.

**Obiettivo:** minimizzare il costo.

**Gold:** A.

## P20 — Costo e tempo non compensabili
A costa €100 e richiede 10 giorni. B costa €120 e richiede 5 giorni. Il vincolo è: costo ≤€110 e tempo ≤7 giorni.

**Compito:** determinare l'alternativa eleggibile.

**Gold:** nessuna. A fallisce il tempo; B fallisce il costo.

## P21 — Tre criteri con priorità lessicografica
Priorità: prima sicurezza, poi costo. A sicurezza 9/10, costo €100; B sicurezza 8/10, costo €50; C sicurezza 10/10, costo €200.

**Compito:** scegliere secondo la regola indicata.

**Gold:** C, perché la sicurezza viene valutata prima del costo.

## P22 — Informazione insufficiente
A costa €100 con affidabilità sconosciuta. B costa €120 con affidabilità 99%. L'obiettivo è massimizzare affidabilità, ma non esistono dati sull'affidabilità di A.

**Compito:** decidere se è possibile una scelta definitiva.

**Gold:** no; A non è valutabile rispetto al criterio principale.

## P23 — Dominanza
A: costo €100, tempo 5 giorni. B: €120, 7 giorni. C: €100, 4 giorni. L'obiettivo è minimizzare costo e tempo simultaneamente.

**Compito:** individuare l'alternativa dominata e l'alternativa non dominata più forte.

**Gold:** B è dominata da C; C è migliore di A su tempo e uguale sul costo.

## P24 — Vincolo eliminatorio
Budget massimo €500. A costa €450 e ha affidabilità 80%; B €550 e affidabilità 95%; C €480 e affidabilità 85%.

**Compito:** applicare prima il vincolo di budget e poi scegliere l'affidabilità maggiore.

**Gold:** C.

---

# E. DECISIONE VINCOLATA

## P25 — Stop rule
Regola: scegliere la prima alternativa che soddisfa tutti i requisiti; non confrontare alternative successive se una è già conforme.

A: requisiti 4/5.  
B: 5/5.  
C: 5/5.

**Compito:** decidere secondo la regola.

**Gold:** B.

## P26 — Peggior caso eliminatorio
Un'opzione è ammissibile solo se il suo scenario peggiore non presenta un esito critico.

A: peggiore non critico.  
B: peggiore critico.  
C: peggiore non critico.

**Compito:** classificare le opzioni.

**Gold:** A e C ammissibili; B esclusa.

## P27 — Decisione con dati mancanti
Per scegliere tra A e B servono due dati: costo e tempo. Sono noti per A (€100, 4 giorni), ma per B è noto solo il costo (€80).

Vincoli: costo ≤€100 e tempo ≤5 giorni.

**Compito:** determinare cosa può essere deciso.

**Gold:** A è sicuramente ammissibile; B non è classificabile definitivamente perché manca il tempo.

## P28 — Contraddizione nei requisiti
Obiettivo: completare un progetto in massimo 3 giorni. Vincolo operativo: ogni attività richiede almeno 2 giorni e ci sono due attività obbligatorie sequenziali.

**Compito:** stabilire se esiste una soluzione compatibile.

**Gold:** no; minimo 4 giorni.

## P29 — Trade-off esplicito
A ha qualità 9 e costo 9. B qualità 8 e costo 5. C qualità 6 e costo 3. Il criterio dichiarato è: massimizzare qualità senza superare costo 6.

**Compito:** scegliere l'alternativa eleggibile con qualità maggiore.

**Gold:** B.

## P30 — Decisione con verifica
Un responsabile deve scegliere un piano. Requisiti: costo ≤€1.000, durata ≤10 giorni, almeno 90% di copertura. A: €900, 9 giorni, 88%. B: €950, 10 giorni, 92%. C: €1.100, 8 giorni, 95%.

**Compito:** scegliere il piano conforme e indicare quali alternative sono escluse e perché.

**Gold:** B; A esclusa per copertura insufficiente; C esclusa per costo eccessivo.

---

# Regole di integrità del dataset

1. I problemi sono congelati per Experiment 01.
2. Le condizioni A/B/C devono ricevere lo stesso problema P01–P30.
3. Il testo del problema non deve essere modificato tra le condizioni.
4. Il gold non deve essere incluso nel prompt inviato al modello.
5. Il gold deve essere usato esclusivamente per la valutazione.
6. Se un problema presenta ambiguità scoperta **prima** dell'esecuzione, deve essere registrata e il problema marcato `EXCLUDED_BEFORE_RUN`; non deve essere corretto silenziosamente.
7. Se l'ambiguità viene scoperta dopo l'esecuzione, il problema non viene retroattivamente modificato: viene marcato `EXCLUDED_POST_RUN` e l'analisi primaria resta invariata.
8. Qualsiasi modifica futura deve creare `DATASET_02`, senza sovrascrivere questo file.

## Stato

**DATASET_01 = FROZEN**

`30 problemi × 3 condizioni × più modelli/run → dati → analisi → verdetto`
