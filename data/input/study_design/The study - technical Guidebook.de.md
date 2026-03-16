# **Menschliche Vorhersage der Glukose in der nächsten Stunde anhand vorheriger CGM‑Kontexte: Eine Online‑Benchmarking‑Studie**

**Studienprotokoll (Kurzfassung)**

**Hauptprüfer (Principal Investigator):** Anton Kulaga – Institut für Biostatistik und Informatik in Medizin und Alternsforschung (IBIMA), Universitätsmedizin Rostock, Rostock, Deutschland

**Co‑Investigators:** Livia Zaharia (HEALES – Healthy Life Extension Society, Brüssel, Belgien)

**Biostatistische Beratung:** Benjamin Otte, M.Sc. – Abteilung Biostatistik, IBIMA, Universitätsmedizin Rostock

**Projektkontext:** Diese Studie ist Teil der Sugar‑Sugar Glucose Accuracy Prediction Study und wird von HEALES unterstützt.

**Registrierungsnummer:** Ref. number A 2026-0064  
**Eingegangen bei der Ethikkommission:** 27. Februar 2026

---

## **Überblick**

**Hintergrund:**  
Für Machine‑Learning‑Modelle zur Glukosevorhersage werden Genauigkeitsmetriken häufig anhand kontrollierter akademischer Datensätze berichtet. Ein vergleichbarer **Benchmark für die menschliche Vorhersagegenauigkeit** existiert bisher nicht. CGM‑Nutzende antizipieren im Alltag regelmäßig zukünftige Glukoseverläufe als Teil des Selbstmanagements – die Qualität dieser Vorhersagen wurde jedoch noch nicht systematisch untersucht.

**Ziele:**

- (0) Quantifizierung der Genauigkeit menschlicher Vorhersagen der nächsten Stunde auf Basis von 3 Stunden CGM‑Historie
- (1) Vergleich der Vorhersagegenauigkeit zwischen Menschen mit Diabetes (Typ 1 und Typ 2) und Menschen ohne Diabetes (einschließlich Prädiabetes / Wellness‑Nutzung)
- (2) Vergleich der Vorhersagegenauigkeit zwischen CGM‑Nutzenden und Nicht‑Nutzenden (CGM‑Nutzung > 1 Monat gilt als CGM‑Nutzung)

**Design:**  
Querschnittliche, beobachtende Online‑Studie. Teilnehmende geben **mindestens sechs** Vorhersagen ab; ein adaptives, zweistufiges Stichprobendesign ist vorgesehen.

**Setting:**  
Web‑Plattform (Sugar‑Sugar‑Applikation), betrieben von HEALES; Forschungsdaten werden an der Universitätsmedizin Rostock gespeichert.

**Teilnehmende:**  
Zielgröße \(N \approx 200\) Erwachsene (≥18 Jahre), ungefähr 100 mit Diabetes und 100 ohne Diabetes, Rekrutierung über soziale Medien und Diabetes‑Organisationen. Das adaptive Design erlaubt Anpassungen bis zu 150 pro Gruppe nach Zwischenanalyse. Zusätzlich können Personen ohne Diabetes teilnehmen, die CGM z. B. für Fitness, Sport, Lifestyle‑Optimierung oder Biohacking verwenden.

Die Einteilung erfolgt in vier Gruppen:

- Menschen mit Diabetes + CGM („PwD CGM“)
- Menschen mit Diabetes ohne CGM („PwD no‑CGM“)
- Menschen ohne Diabetes + CGM („non‑PwD“)
- Menschen ohne Diabetes ohne CGM‑Vorerfahrung („NPE“)

**Ablauf / Verfahren:**  
Teilnehmende mit CGM‑Daten werden ermutigt, optional eigene Daten (historische Glukosewerte) hochzuladen. Die Aufgabe ist, den Verlauf der nächsten Stunde basierend auf dem vorherigen Kontext vorherzusagen – in der Web‑Applikation durch **Zeichnen einer Linie** auf einem Glukose‑Graphen. Teilnehmende ohne eigene Daten (oder die keinen Upload möchten) nutzen anonymisierte Drittanbieter‑Datensätze.

Jede Person bearbeitet 6–12 Aufgaben. Pro Aufgabe werden 12 Punkte vorhergesagt (alle 5 Minuten für 60 Minuten), basierend auf 3 Stunden Kontext.

**Warum 6–12 Aufgaben?**

- **Reliabilität:** Eine einzelne Aufgabe ist als Fähigkeitsmaß unzuverlässig; Mittelung über 6–12 Aufgaben reduziert Messfehler.
- **Statistische Power:** Wiederholte Messungen erhöhen die Power erheblich (z. B. 200 Personen × 10 Aufgaben ≈ 2.000 Beobachtungen).
- **Variabilität:** Mehrere Aufgaben erfassen unterschiedliche Glukosedynamiken (Tageszeit, Trendrichtung, Ereigniskontexte).
- **Machbarkeit:** 6–12 Aufgaben balancieren Genauigkeit vs. Belastung (Pilot: 15–20 Minuten Engagement).

**Primäre Endpunkte:**  
Vorhersagefehler werden über **MAE** (Mean Absolute Error) und **RMSE** (Root Mean Squared Error) in mg/dL quantifiziert.

**Statistische Analyse (Kurz):**  
Vergleich der pro‑Person‑MAE/RMSE zwischen Gruppen (Diabetes vs. ohne Diabetes; CGM‑Nutzung vs. keine), Vergleich menschlicher Vorhersagen mit Baselines (Persistenz, lineare Extrapolation). Berücksichtigung der wiederholten Messstruktur.

**Ethik und Dissemination:**  
Einreichung bei der Ethikkommission, Universitätsmedizin Rostock. Nicht‑interventionelle Studie, Nutzung historischer Daten. Ergebnisse werden in Fachzeitschriften publiziert.

---

### Vollständiges Protokoll

Die ausführliche technische Anleitung ist aktuell in Englisch verfügbar:  
`data/input/study_design/The study - technical Guidebook.md`

