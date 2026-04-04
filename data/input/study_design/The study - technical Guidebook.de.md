# **Menschliche Vorhersage des nächststündigen Blutzuckers auf Basis vorheriger kontinuierlicher Glukosemessung (CGM): Eine Online-Benchmarking-Studie**

**Studienprotokoll**

**Hauptuntersucherin:** Anton Kulaga \- Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA), Universitätsmedizin Rostock, Rostock, Deutschland

**Mituntersucherinnen:** Livia Zaharia (HEALES \- Healthy Life Extension Society, Brüssel, Belgien)

**Biostatistische Beratung:** Benjamin Otte, M.Sc. \- Abteilung für Biostatistik, Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA), Universitätsmedizin Rostock, Rostock, Deutschland

**Projektkontext:** Diese Studie wird im Rahmen der Sugar-Sugar Glukosegenauigkeits-Vorhersagestudie durchgeführt, gefördert von HEALES (Healthy Life Extension Society)

**Registrierungsnummer:** Ref.-Nr. A 2026-0064  
**Eingegangen bei der Ethikkommission:** 27. Februar 2026

---

## **Überblick**

**Hintergrund:**

Maschinelle Lernmodelle zur Glukoseprognose berichten über Genauigkeitsmetriken aus kontrollierten akademischen Datensätzen, doch es existiert kein Referenzwert für die menschliche Prognosegenauigkeit. CGM-Nutzer antizipieren routinemäßig künftige Glukosewerte als Teil ihres täglichen Selbstmanagements, doch die Qualität dieser Vorhersagen wurde nie systematisch bewertet.

**Ziele:**

(0) Quantifizierung der menschlichen Genauigkeit bei der Vorhersage des nächststündigen Blutzuckers anhand einer 3-stündigen CGM-Vorgeschichte;

(1) Vergleich der Prognosegenauigkeit zwischen Personen mit Diabetes (PmD) vom Typ 1 und Typ 2 und Personen ohne Diabetes, einschließlich Prä-Diabetes-, Wellness- und Nutzern ohne Vorerfahrung (nicht-DM);

(2) Vergleich der Prognosegenauigkeit zwischen CGM-Nutzern und Nicht-CGM-Nutzern. Eine Person gilt als CGM-Nutzer, wenn sie ein CGM länger als einen Monat verwendet hat.

**Design:**

Querschnittliche, beobachtende Online-Studie, bei der Nutzer gebeten werden, mindestens sechsmal Vorhersagen zu treffen, mit adaptivem zweistufigem Stichprobendesign.

**Setting:**

Webbasierte Plattform (Sugar-Sugar-Anwendung), gehostet von HEALES, mit Forschungsdaten gespeichert an der Universitätsmedizin Rostock.

**Teilnehmer:**

Ziel N≈200 Erwachsene (≥18 Jahre): ca. 100 PmD und 100 Nicht-PmD, rekrutiert über soziale Medien und Diabetesorganisationen. Das adaptive Design erlaubt eine Anpassung auf bis zu 150 pro Gruppe auf Basis einer Zwischenanalyse. Für die Nicht-DM-Gruppe gibt es Personen, die ihre CGMs zur Fitnessverfolgung, Sportverbesserung, Lifestyle-Optimierung, Biohacking usw. nutzen und vorab Interesse an einer Teilnahme bekundet haben.

Die Teilnehmer werden in vier Gruppen eingeteilt: PmD CGM-Nutzer (Gruppe „PmD CGM"), PmD ohne CGM (Gruppe „PmD ohne CGM"), Nicht-PmD CGM-Nutzer (z.B. für Wellness, Sport usw., Gruppe „nicht-PmD"), Nicht-PmD Nicht-CGM-Nutzer ohne Vorerfahrung (Gruppe „OVE")

**Verfahren:**

Teilnehmer mit CGM-Daten werden ermutigt, ihre eigenen Daten mit früheren Glukosemessungen (im Folgenden kurz: historische Daten) für die Vorhersageaufgabe hochzuladen. Die Aufgabe besteht darin, vorherzusagen, wie sich die geschätzten CGM-Glukosewerte (im Folgenden kurz: GW) bei Kenntnis der Vorwerte verändern werden. Im Fall unserer Webanwendung geschieht dies auf intuitive Weise durch Einzeichnen einer Linie in einem GW-Diagramm. Weitere Details finden sich in Abschnitt 4.2.

Teilnehmer ohne CGM-Daten oder die lieber keine hochladen möchten, können Drittanbieter-Daten aus öffentlichen anonymisierten Datensätzen verwenden, die kostenlos heruntergeladen werden können. Wir haben die Liste der Datensätze unter [https://github.com/GlucoseDAO/glucose\_data\_processing/blob/main/docs/datasets.csv](https://github.com/GlucoseDAO/glucose_data_processing/blob/main/docs/datasets.csv) zusammengestellt, wobei Datensätze mit einer „Downloader"-Spalte vollständig öffentlich zugänglich sind.

Jeder Teilnehmer wird 6 bis 12 Vorhersageaufgaben absolvieren. Bei jeder Aufgabe sagen sie vorher, was in der nächsten Stunde passieren wird, indem sie Punkte in einem Diagramm einer Webanwendung einzeichnen. Konkret sagen sie 12 Datenpunkte vorher – einen für jedes 5-Minuten-Intervall im 60-Minuten-Zeitraum. Um diese Vorhersagen zu treffen, werden den Teilnehmern die vorherigen 3 Stunden Daten als Kontext gezeigt.

Mehrere Vorhersageversuche pro Teilnehmer sind notwendig, um zuverlässige Genauigkeitsschätzungen auf individueller Ebene und ausreichende statistische Power zu erhalten.

**Messungsreproduzierbarkeit:** Ein einziger Vorhersageversuch liefert aufgrund zufälliger Variation (z.B. Schwierigkeit des Segments, momentane Aufmerksamkeitslücken) eine unzuverlässige Schätzung der individuellen Fähigkeit. Durch Mittelwertbildung über 6–12 Versuche werden stabile, reproduzierbare Genauigkeitsmetriken durch Reduktion des Messfehlers erzielt.

**Statistische Power:** Das Messwiederholungsdesign erhöht die statistische Power erheblich im Vergleich zu Einzelversuchsdesigns. Mit 200 Teilnehmern, die jeweils 10 Versuche absolvieren, nähert sich die effektive Stichprobengröße für Innersubjekt-Analysen 2.000 Beobachtungen, was die Erkennung kleiner bis mittlerer Effektgrößen (Cohen's d ≥ 0,3) ermöglicht, die in Einzelversuchsdesigns unrealistisch große Stichprobengrößen erfordern würden.

**Kontextuelle Variabilität:** Mehrere Versuche ermöglichen das Sampling über unterschiedliche Glukosedynamiken (Tageszeit, Trendrichtung, Ereigniskontexte) hinweg, was sicherstellt, dass Genauigkeitsschätzungen die Leistung über repräsentative Szenarien hinweg widerspiegeln und nicht nur einen einzelnen atypischen Fall.

**Durchführbarkeit:** Der Bereich von 6–12 Versuchen balanciert Messpräzision mit Teilnehmerbelastung. Pilottests zeigten anhaltende Beteiligung über 15–20 Minuten (ca. 10–12 Segmente), danach können Ermüdungseffekte die Datenqualität beeinträchtigen.

Dieser Ansatz folgt der Standard-Psychometrie-Praxis zur Etablierung zuverlässiger individueller Unterschiede in kognitiven Aufgaben und entspricht Messwiederholungsdesigns, die häufig in Benchmarking-Studien zur menschlichen Leistung eingesetzt werden.

**Primäre Ergebnismaße:**

Wir messen die Prognosegenauigkeit anhand zweier Standardmetriken: Mittlerer absoluter Fehler (MAE) und Wurzel des mittleren quadratischen Fehlers (RMSE), beide gemessen in mg/dL. Diese Metriken zeigen, wie weit die Vorhersagen von den tatsächlichen Glukosewerten abweichen. Diese Metriken werden sowohl für maschinelle Lernmodelle als auch für die Vorhersagen der menschlichen Teilnehmer berechnet.

**Statistische Analyse:**

Gruppenvergleich von MAE/RMSE pro Person zwischen PmD und Nicht-DM; Vergleich menschlicher Vorhersagen mit Basismodellen (Persistenz, lineare Extrapolation). Sekundäre Analysen untersuchen Zusammenhänge zwischen Erfahrung und Genauigkeit. Die Analyse berücksichtigt die Messwiederholungsstruktur.

**Ethik und Verbreitung:**

Positives Votum der Ethikkommission, Universitätsmedizin Rostock erhalten. Nicht-interventionelle Studie nur mit historischen Daten. Ergebnisse sollen in begutachteten Fachzeitschriften veröffentlicht werden.

---

## **1\. Hintergrund und Begründung**

### **1.1 Kontext: CGM-Nutzer und Selbstvorhersage**

Kontinuierliche Glukosemessgeräte (CGM) \[5\] liefern alle 5 Minuten Blutzuckermessungen und erzeugen detaillierte 24-Stunden-Glukoseprofile. CGM-Technologie wird von mehreren Bevölkerungsgruppen verwendet:

**Personen mit Diabetes (PmD):**

* Nutzen CGM-Daten für eigene Insulindosierung, Mahlzeitenplanung und Aktivitätsentscheidungen
* Entwickeln durch tägliche Erfahrung mit ihren Glukosetrends intuitive Mustererkennung
* Treffen Selbstmanagementent­scheidungen auf Basis antizipierter Glukoseverläufe

**Gesundheitsbewusste Personen (Wellness-Nutzer):**

* Prädiabetiker, die Glukose für die Lebensstiloptimierung überwachen
* Nicht-Diabetiker mit Interesse an metabolischer Gesundheit und Langlebigkeit
* Sportler und Biohacker, die Glukosereaktionen auf Ernährung und Sport verfolgen

In allen Fällen treffen Nutzer ihre eigenen Vorhersagen über künftige Glukosewerte als Teil des täglichen Selbstmanagements – diese Studie quantifiziert diese Vorhersagefähigkeit.

### **1.2 Das fehlende Referenzwert-Problem**

Aktuelle maschinelle Lernmodelle für Glukosevorhersagen berichten technische Metriken (RMSE, MAE), die jedoch aus **kontrollierten akademischen Datensätzen** stammen. Laut GlucoBench \[1\] erreichen modernste Modelle:

* **30-Minuten-Vorhersagen:** RMSE 8–12 mg/dL, MAE 6–10 mg/dL
* **60-Minuten-Vorhersagen:** RMSE 10–16 mg/dL, MAE 9–13 mg/dL

Diese Metriken haben jedoch wichtige Einschränkungen:

1. **Kontrollierte vs. reale Leistung:** Akademische Referenzwerte verwenden kuratierte Datensätze mit konsistenter Datenqualität. Reale CGM-Nutzer haben Lücken, Sensorfehler und inkonsistente Ereignisprotokollierung.
2. **Kein menschlicher Vergleich:** Wir wissen nicht, wie diese ML-Metriken im Vergleich zur Vorhersagefähigkeit abschneiden, die erfahrene CGM-Nutzer durch tägliche Nutzung entwickeln.
3. **Bevölkerungsvielfalt:** Akademische Datensätze konzentrieren sich oft auf spezifische Diabetestypen; reale Nutzer umfassen diabetische, prädiabetische und Wellness-Bevölkerungsgruppen mit unterschiedlichen Vorhersagekontexten.

**Diese Studie schließt diese Lücke**, indem sie ermittelt, wie gut tatsächliche CGM-Nutzer ihren eigenen Blutzucker unter realistischen Bedingungen vorhersagen.
Weitere Details finden sich im Referenzabschnitt.

### **1.3 Forschungslücke und Innovation**

Nach unserem Wissen hat **keine frühere Studie systematisch die menschliche Genauigkeit bei der Vorhersage stündlicher Glukoseverläufe quantifiziert**. Diese Studie schließt diese kritische Lücke durch:

1. Etablierung einer Baseline für die menschliche Selbstvorhersagegenauigkeit über verschiedene Nutzergruppen hinweg
2. Vergleich der Leistung zwischen den vier oben genannten Personengruppen: PmD CGM, PmD ohne CGM, nicht-PmD CGM und OVE
3. Untersuchung von Faktoren, die mit der Prognosegenauigkeit assoziiert sind (Diabetesdauer, CGM-Erfahrung)
4. Erstellung eines realen Referenzwerts, der laborgewonnene ML-Metriken ergänzt

### **1.4 Studienbegründung**

Diese Forschung ist notwendig, weil:

* **Kein menschlicher Referenzwert existiert:** Wir wissen nicht, wie gut erfahrene CGM-Nutzer ihren eigenen Blutzucker vorhersagen
* **Akademische Referenzwerte sind zu optimistisch:** ML-Metriken aus kuratierten Datensätzen spiegeln keine realen Leistungsbedingungen wider
* **Diverse Nutzergruppen:** Diabetische, prädiabetische und Wellness-CGM-Nutzer können unterschiedliche Vorhersagefähigkeiten haben
* **Selbstmanagement-Kontext:** Das Verständnis menschlicher Vorhersagefähigkeit informiert realistische Erwartungen an KI-gestützte Werkzeuge

---

## **2\. Studienziele und Hypothesen**

### **2.1 Primäre Ziele**

**Ziel 0:**

Quantifizierung, wie präzise Menschen Glukosewerte für die nächste Stunde vorhersagen können, nachdem sie die vorherigen 3 Stunden Glukosedaten gesehen haben, unabhängig davon, ob sie CGM verwenden oder Diabetes haben.

**Ziel 1:**

Quantifizierung und Vergleich, wie präzise Personen mit Diabetes (PmD) im Vergleich zu Personen ohne Diabetes (nicht-PmD) Glukosewerte für die nächste Stunde vorhersagen können, nachdem sie die vorherigen 3 Stunden Glukosedaten gesehen haben, unabhängig davon, ob sie CGM verwenden (CGM- und Nicht-CGM-Gruppe paarweise nach Diabetesstatus kombiniert).

**Ziel 2:**

Quantifizierung und Vergleich der Genauigkeit von Personen, die bereits kontinuierliche Glukosemessgeräte verwenden, gegenüber Personen, die kein CGM verwenden, bei der Vorhersage von Glukosewerten für die nächste Stunde nach Kenntnis der vorherigen 3 Stunden Daten, unabhängig von ihrem Diabetesstatus (PmD- und nicht-PmD-Gruppen paarweise nach CGM-Erfahrung kombiniert)

### **2.2 Sekundäre Ziele**

**Ziel 3:** Prüfung, ob längere Diabetesdauer mit besserer Prognosegenauigkeit assoziiert ist.

**Ziel 4:** Prüfung, ob längere CGM-Erfahrung mit besserer Genauigkeit assoziiert ist.

**Ziel 5:** Vergleich der Genauigkeit, wenn Teilnehmer generische anonymisierte Daten gegenüber eigenen CGM-Daten vorhersagen (Innersubjekt-Vergleich).

### **2.3 Formale Hypothesen** Dieser Abschnitt präsentiert nur die Hypothesen – für statistische Testmethoden siehe Abschnitt 7\.

#### **Primäre Hypothesen**

**H1 (Gruppenunterschied – Diabetes mellitus als Unterscheidungsmerkmal):**

* Nullhypothese (H1.1): Mittlerer MAE von Personen mit Diabetes \= Mittlerer MAE von Personen ohne Diabetes
* Alternativhypothese (H1.2): Mittlerer MAE von Personen mit Diabetes ≠ Mittlerer MAE von Personen ohne Diabetes – Richtung durch Vergleich zu bestimmen

*Begründung:* Personen mit Diabetes haben direkte Lebenserfahrung im Umgang mit Glukosevariabilität und können durch tägliche CGM-Nutzung intuitive Mustererkennung entwickeln. Niedrigerer MAE zeigt bessere Prognosegenauigkeit an.

**H2 (Gruppenunterschied – CGM-Nutzer als Unterscheidungsmerkmal):**

* Nullhypothese (H2.1): Mittlerer MAE von Personen mit CGM \= Mittlerer MAE von Personen ohne CGM
* Alternativhypothese (H2.2): Mittlerer MAE von Personen mit CGM ≠ Mittlerer MAE von Personen ohne CGM – Richtung durch Vergleich zu bestimmen

*Begründung:* GlucoBench \[1\] und verwandte Studien liefern Referenzpunkte: Für 60-Minuten-Vorhersagen erreichen einfache Modelle MAE ~12–20 mg/dL, während Deep-Learning-Modelle (Transformer, Gluformer) MAE ~11–17 mg/dL erreichen, abhängig von Datensatz und Bedingungen. Wir erwarten, dass die menschliche Leistung irgendwo in diesem Bereich liegt. Dieser Vergleich zeigt, wo menschliche Intuition im Verhältnis zu algorithmischen Ansätzen steht.

#### **Sekundäre Hypothesen**

**H3 (Dauerwirkung):**

* Nullhypothese (H3.0): Es gibt keinen Zusammenhang zwischen Diabetesdauer und MAE (ρ \= 0)
* Alternativhypothese (H3.1): Es gibt einen negativen Zusammenhang zwischen Diabetesdauer und MAE (ρ \< 0), mit den stärksten Effekten in den ersten 5 Jahren

Längere Diabetesdauer ist mit einer höheren Anzahl beobachteter Glukosewerte verbunden, die mit Ergebnissen gepaart sind, was wiederum zu niedrigerem MAE (besserer Genauigkeit) führt. Diese erstrecken sich nicht nur aus CGM-Messungen, sondern auch aus zuvor durch Blutuntersuchungen und Beobachtungen bei Ereignissen wie Essen, Injizieren, Sport und körperlicher Aktivität angesammelter Erfahrung. All diese Ereignisse würden einen älteren Diabetiker zu einem genaueren Vorhersager von Glukoseschwankungen machen.

*Begründung:* Menschen, die länger mit Diabetes gelebt haben, haben mehr Erfahrung darin gesammelt zu beobachten, wie ihr Blutzucker auf Mahlzeiten, Insulin, Sport, Stress und andere Faktoren reagiert. Diese erweiterte Exposition bietet mehr Möglichkeiten, Muster zu erkennen und intuitive Vorhersagefähigkeiten zu entwickeln.

Wichtiger Hinweis – die Dauer korreliert in unserem Fall nur mit der Zeit mit Diabetes, nicht mit dem allgemeinen Alter des Teilnehmers – daher werden wir Nutzer nicht nach ihrem Alter, sondern nach der tatsächlichen Zeit mit dieser Erkrankung gruppieren. Dies wird auch nicht mit der Anzahl der Teilnehmer abgeglichen (z.B. unter der Annahme, dass ältere Menschen mehr Erfahrung mit ihrer Erkrankung haben, aber weniger am Studium teilnehmen – das würde zu Unsicherheit führen – wir kümmern uns nur darum, wie die Dauer der Erkrankung die Vorhersagegenauigkeit der Teilnehmenden widerspiegelt).

**H4 (CGM-Erfahrungseffekt):**

* Nullhypothese (H4.0): Es gibt keinen Zusammenhang zwischen CGM-Erfahrungsdauer und MAE (ρ \= 0)
* Alternativhypothese (H4.1): Es gibt einen negativen Zusammenhang zwischen CGM-Erfahrungsdauer und MAE (ρ \< 0), mit den stärksten Effekten in den ersten 2 Jahren

Längere CGM-Erfahrung ist mit niedrigerem MAE (besserer Genauigkeit) assoziiert.

*Begründung:* CGM-Nutzer treffen täglich Entscheidungen auf Basis ihrer Glukosetrends – Anpassung von Insulindosen, Mahlzeitenplanung und Modifikation von Aktivitäten. Diese kontinuierliche Feedbackschleife schafft eine natürliche Lernumgebung, in der Nutzer durch wiederholte Entscheidungsfindung und Ergebnisbeobachtung Mustererkennungsfähigkeiten entwickeln. Nutzer, die CGM länger tragen, hatten mehr Möglichkeiten, ihre persönliche Glukosedynamik kennenzulernen.

**H5 (Eigene vs. generische Daten):**

* Nullhypothese (H5.1): Mittlerer MAE von Personen mit eigenen Daten \= Mittlerer MAE von Personen mit generischen Daten
* Alternativhypothese (H5.2): Mittlerer MAE von Personen mit eigenen Daten ≠ Mittlerer MAE von Personen mit generischen Daten – Richtung durch Vergleich zu bestimmen

Teilnehmer haben niedrigeren MAE (bessere Genauigkeit), wenn sie ihre eigenen Glukosemuster im Vergleich zu generischen Daten vorhersagen. Dies wird gemessen, indem den Teilnehmern erlaubt wird, auf zwei Weisen zu testen – entweder durch Verwenden eines generischen Datensatzes oder durch Hochladen ihrer eigenen Daten zur Vorhersage. Im zweiten Fall werden die Daten für den Nutzer anonymisiert (kein Datum wird angezeigt – nur die Uhrzeit, um Rückerinnerung an genaue Daten zu vermeiden) und grafisch genau wie im vorherigen Fall dargestellt.

*Begründung:* Teilnehmer sind mit ihren eigenen Glukosemustern, Lebensstil und typischen Reaktionen auf Mahlzeiten und Aktivitäten vertraut. Dieses persönliche Wissen sollte einen Vorteil bieten, wenn sie ihre eigenen Daten im Vergleich zu unbekannten generischen Profilen vorhersagen.

**H6 (Mensch vs. Basismodelle):**
Wir stellen die Hypothese auf, dass die menschliche Prognosegenauigkeit (MAE) zwischen einfachen Basismodellen und modernsten KI-Ansätzen liegen wird.

Basismodelle sind die einfachstmöglichen Vorhersagemethoden – sie erfordern kein Training oder komplexe Algorithmen. Unsere Basiswerte umfassen: (1) Persistenzmodell – angenommen, Glukose bleibt auf dem aktuellen Messwert gleich, (2) lineare Extrapolation – eine Gerade durch aktuelle Messungen ziehen und vorwärts verlängern, und (3) ARIMA – eine Standard-Statistikmethode für Zeitreihendaten.

Wir erwarten die Leistungshierarchie: einfache Basiswerte < menschliche Vorhersagen < Deep-Learning-Modelle (z.B. LSTMs, Transformer). Wir werden testen, ob Menschen Basiswerte signifikant übertreffen und ob Deep Learning Menschen signifikant übertrifft.

Diese Hypothese wird für die Fortsetzung der Studie aufbewahrt, wenn ein gut definiertes Modell vorliegt – Im Moment ist kein Modell in der Studie involviert.

*Begründung:* GlucoBench und verwandte Studien liefern Referenzpunkte: Für 60-Minuten-Vorhersagen erreichen einfache Modelle MAE ~12–20 mg/dL, während Deep-Learning-Modelle (Transformer, Gluformer \[2,7,8\]) MAE ~11–17 mg/dL erreichen, abhängig von Datensatz und Bedingungen. Wir erwarten, dass die menschliche Leistung irgendwo in diesem Bereich liegt. Dieser Vergleich zeigt, wo menschliche Intuition im Verhältnis zu algorithmischen Ansätzen steht.

---

## **3\. Studiendesign**

### **3.1 Studientyp**

**Design:** Beobachtend, querschnittlich mit wiederholten Vorhersageaufgaben. Weitere Details siehe Abschnitt 4.2  
**Datenerhebung:** Webbasierte Online-Plattform  
**Follow-up:** Keines (einmalige Teilnahme)

### **3.2 Regulatorische Klassifizierung**

Diese Studie ist eine **nicht-interventionelle, beobachtende Studie**, die keine ärztliche Aufsicht oder medizinische Geräteregelung erfordert.

#### **3.2.1 Nur historische Daten**

* Alle CGM-Daten, die den Teilnehmern gezeigt werden, sind **historische, vorab aufgezeichnete Daten** – entweder aus einem zusammengeführten anonymen Datensatz oder aus den eigenen zuvor exportierten CGM-Dateien des Teilnehmers
* **Keine Echtzeit-Glukoseüberwachung** wird während der Studie durchgeführt
* **Keine Verbindung zu aktiven CGM-Geräten** – Teilnehmer müssen keine Überwachungsgeräte für diese Studie tragen oder verwenden
* Die Studie analysiert Prognosegenauigkeit auf vergangenen Datensegmenten, nicht auf dem aktuellen Gesundheitsstatus

#### **3.2.2 Keine medizinischen Entscheidungen oder Diagnosen**

Diese Studie tut ausdrücklich **NICHT**:

* Stellt keine medizinische Diagnose oder Prognose
* Trifft keine therapeutischen oder Behandlungsempfehlungen
* Beeinflusst keine klinischen Entscheidungen oder medizinischen Behandlungspläne
* Bietet keine personalisierten Gesundheitsratschläge oder -anleitungen
* Erzeugt keine Ausgaben für klinischen Einsatz

**Ergebnisse dienen ausschließlich Forschungs-Benchmarking-Zwecken** – Genauigkeitswerte zeigen nur Vorhersageleistung an und haben keine diagnostische oder therapeutische Bedeutung.

#### **3.2.3 Keine ärztliche Aufsicht erforderlich**

Ärztliche Aufsicht ist für diese Studie nicht erforderlich, weil:

* **Keine medizinische Intervention** durchgeführt wird
* **Keine diagnostischen Tests** durchgeführt werden
* **Keine Gesundheitsergebnisse** von Teilnahme oder Ergebnissen abhängen
* **Keine Behandlungsentscheidungen** durch die Studie informiert werden
* Die Aktivität dem **Ausfüllen einer Online-kognitiven Aufgabe oder Umfrage** entspricht

### **3.3 Studienpopulation**

#### **Einschlusskriterien**

**Allgemeine Bevölkerung (beide Gruppen):**

* Alter 18 Jahre oder älter
* Fähigkeit zur informierten Einwilligung
* Internetzugang und grundlegende Computer-/Mobilliteralität
* Bereitschaft zur Durchführung von Vorhersageaufgaben

**Zusätzlich für Personen mit Diabetes (PmD):**

* Selbst berichtete Diabetes-Diagnose (Typ 1, Typ 2 oder andere)
* Aktuelle oder frühere CGM-Nutzung (jedes Gerät)

---

## **4\. Teilnehmer-Workflow und Verfahren**

### **4.1 Rekrutierungsstrategie**

**Rekrutierungskanäle:**

1. Ankündigungen in sozialen Medien (Twitter/X, LinkedIn, Facebook-Diabetesgruppen)
2. Diabetes-Patientenorganisationen und Interessenvertretungen
3. Netzwerke wissenschaftlicher Beiräte
4. Community-Kanäle (Projektwebsite, Telegram)
5. Wissenschaftliche Konferenzen (Präsentationen bei Longevity-/Diabetes-Treffen)

Spezifische Rekrutierungsmaterialien werden nach Erhalt der Ethikfreigabe entwickelt.

### **4.2 Studienverfahren**

#### **Phase 1: Einwilligung und Baseline-Informationen**

Teilnehmer greifen über eine URL (Webadresse) auf die Sugar-Sugar-Webanwendung zu und absolvieren:

**1\. Elektronische informierte Einwilligung**

* Studieninformationsblatt
* Datenschutzinformationen (DSGVO-konform)
* Checkbox-Einwilligung für Studienteilnahme und Datenverarbeitung
* Optionale Einwilligungen für: Hochladen eigener CGM-Daten, zukünftige Kontaktaufnahme falls der Nutzer mehr Details über die Studienergebnisse erfahren möchte, Werbemitteilungen

**2\. Basis-Fragebogen**
**(wird vom Teilnehmer genau auf Basis seines Wissens ausgefüllt)**

* E-Mail (zur eindeutigen Identifizierung; für Anonymisierung gehasht)
* Alter (Jahre)
* Geschlecht
* Wohnland
* Diabetesstatus (Ja/Nein)
  * Falls Ja: Diabetestyp, Jahre seit Diagnose
* CGM-Nutzung (Ja/Nein)
  * Falls Ja: Jahre der Nutzung
* Optionales Gewicht (kg) und Größe (cm)

**Datenschutzhinweis:** E-Mails werden unmittelbar nach der Übermittlung gehasht für eine eindeutige Identifizierung ohne Speicherung persönlicher Bezeichner. Teilnehmer können sich separat für Wiederholungskontakt-Mitteilungen anmelden.

#### **Phase 2: Übungsversuche**

2 optionale Übungsversuche zur Vertrautmachung mit der Benutzeroberfläche (Nutzer haben die Möglichkeit, für die ersten 2 Versuche nicht einzureichen). Übungsversuchsdaten werden von der Analyse ausgeschlossen.

#### **Phase 3: Generische Daten-Vorhersageaufgabe**

**Aufgabenstruktur:**

* **Anzahl der Versuche:** 6–12 Vorhersagesegmente pro Teilnehmer
* **Jedes Segment:** Teilnehmer zeichnet 12 Vorhersagepunkte (5-Minuten-Intervalle über 60 Minuten)
* **Gezeigtes Kontextfenster:** 3 Stunden CGM-Daten (36 Punkte bei 5-Minuten-Auflösung)
* **Datenquelle:** De-identifizierte CGM-Daten aus dem kuratierten Datensatz der Studie

Segmente werden ausgewählt, um eine ausgewogene Mischung verschiedener Tageszeiten, Glukosetrends und Ereigniskontexte bereitzustellen. Die Reihenfolge wird über Teilnehmer hinweg randomisiert.

**Interface-Funktionen:**

* Interaktives Diagramm mit 5-Minuten-Zeitgitter
* Teilnehmer klicken/zeichnen, um Vorhersagekurve zu erstellen
* Anzeige von Ereignismarkierungen (Mahlzeit-/Insulin-/Sport-Zeitstempel)
* Editierbare Vorhersagen vor der Einreichung

*Unten ist die Hauptoberfläche für den Nutzer nach dem Ausfüllen der Daten- und Einwilligungsformulare.*
*\-blaue Linie und Punkt stellen die aufgezeichneten historischen Daten dar, die für den Test aufgezeichnet wurden*

*\-rote Linie sind vom Nutzer vorhergesagte Daten*

*\-es gibt die Möglichkeit, Messeinheiten zu ändern – je nach den dem Teilnehmer am vertrautesten*

*\-es gibt Informationen darüber, welche Runde von den 12 dies ist*

*\-der Nutzer hat jederzeit während des Tests zwei Optionen – einreichen oder einfach beenden*

*Nach jeder Runde erhält der Nutzer folgende Bildschirmanzeige:*

*\-es gibt Informationen darüber, welche Runde es war*

*\-es gibt Vergleich der Daten – blaue Linie wird vollständig gezeigt*

*\-es gibt die numerischen Bearbeitungsergebnisse*

*\-sowie das statistische Ergebnis pro Runde*

*\-der Nutzer hat wieder die Möglichkeit zu beenden oder mit der nächsten Runde fortzufahren*

*Am Ende des Versuchs (max. 12 Runden) erhält der Nutzer diesen Bildschirm, auf dem alle Daten für den gesamten Versuch zusammengestellt sind. Unten sind zwei Beispiele – eines, bei dem der Nutzer nur eine Runde absolviert hat, und eines, bei dem der Nutzer mehrere Runden absolviert hat. Wie zu sehen ist, enthält er:*
*\-Genauigkeitsmetriken*

*\-Einheiten, in denen es durchgeführt wurde*

*\-Werte pro Runde*

*\-Ranking![][image1]*

![][image2]

#### **Phase 4: Eigene Daten hochladen und Aufgabe (Optional)**

**Berechtigung:** Teilnehmer, die ihre Bereitschaft zum Hochladen von CGM-Daten angegeben haben

**Daten-Upload-Prozess:**

1. CGM-Exportdatei hochladen (CSV- oder JSON-Format von unterstützten Geräten oder Nightscout-Export)
2. Automatisierte Qualitätsprüfungen (mindestens 5 aufeinanderfolgende Tage, Datenvalidierung)
3. Datenverarbeitung, bei der wir vom unterstützten Geräteformat in das einheitliche Format für Datenausgabe konvertieren
4. Datenpseudonymisierung und sichere Speicherung

**Eigene Daten-Vorhersageaufgabe:**

* 6–12 Segmente aus eigenen CGM-Daten des Teilnehmers entnommen
* Segmente anonymisiert (keine Daten/Zeiten angezeigt)
* Ermöglicht Innersubjekt-Vergleich der Genauigkeit bei eigenen vs. generischen Daten

#### **Phase 5: Abschluss und Feedback**

**Kurzer Sicherheitshinweis (nur bei erster Ansicht):**

Bei der ersten Teilnahme wird vor den Ergebnissen ein kurzer Hinweis angezeigt:

**Nur für Forschungszwecke** – Diese Werte messen die Mustererkennungsleistung, nicht die medizinische Fähigkeit. Befolgen Sie weiterhin die Anweisungen Ihres Gesundheitsdienstleisters.

Dieser Hinweis wird einem Nutzer einmal angezeigt; zurückkehrende Nutzer sehen die Ergebnisse direkt.

**Ergebnisanzeige (standardmäßig angezeigt):**

* Persönliche Genauigkeitszusammenfassung (MAE in mg/dL)
* Perzentil-Ranking im Vergleich zu anderen Teilnehmern basierend auf aktuellem Datenbankspeicher zum Zeitpunkt der Teilnahme des Nutzers. Kurz gesagt haben wir einen separaten Ranking-Speicher – wir benötigen nur eine anonymisierte Nutzer-ID und ein Ranking – von dort aus erfahren Sie die Gesamtzahl der Teilnehmer und ihre Leistung
* Visueller Vergleich von Vorhersagen vs. tatsächlichen Verläufen
* Option „Überspringen und beenden" verfügbar, aber nicht prominent

**Teilbares Ergebniskärtchen (Nutzer-kontrollierter Inhalt):**

Nutzer können ein Ergebniskärtchen mit anpassbarem Inhalt erstellen und teilen:

* **Immer enthalten:** „Ich habe an der Sugar-Sugar-Glukosevorhersagestudie teilgenommen"
* **Nutzer kann wählen, ob er einbezogen:** Genauigkeitsperzentil, MAE-Wert, Anzahl der abgeschlossenen Segmente, Vergleich mit anderen Teilnehmern
* **Nutzer kontrolliert, was geteilt wird** – Gamification ist ein wichtiges Engagement-Merkmal
* Nutzer werden darüber informiert, dass das Teilen ihr Interesse an Glukose-/Diabetesthemen preisgeben kann

**Kein medizinischer Rat:** Ergebnisse werden als Spiel-/Forschungsleistungsmetriken präsentiert, nicht als Gesundheitsbewertungen.

---

## **5\. Datenerhebung und -management**

### **5.1 Datenkategorien**

**Basisdaten:** Demografische und Nutzerdaten wie:

* E-Mail (zur eindeutigen Identifizierung; für Anonymisierung gehasht)
* Alter (Jahre)
* Geschlecht
* Wohnland
* Diabetesstatus (Ja/Nein)
  * Falls Ja: Diabetestyp, Jahre seit Diagnose
* CGM-Nutzung (Ja/Nein)
  * Falls Ja: Jahre der Nutzung
* Optionales Gewicht (kg) und Größe (cm)

**Einwilligungspräferenzen:**

* für Studienteilnahme und Datenverarbeitung
* für: Hochladen eigener CGM-Daten, zukünftige Kontaktaufnahme falls der Nutzer mehr Details über die abgeschlossenen Studienergebnisse erfahren möchte, Werbemitteilungen

**Diagrammdaten:**

6–12 Segmente pro Teilnehmer, jeweils enthaltend

**Vorhersagedaten:** 12 Vorhersagepunkte (einschließlich Glukosewert und Zeitstempel),

**Grundwahrheitsdaten:** 12 tatsächliche CGM-Werte zur Auswertung (den Teilnehmern erst nach Einreichung gezeigt, einschließlich Glukosewert und Zeitstempel)

**Ergebnisdaten:**

MAE, MSI, RSME, MAPE-Werte

### **5.2 Datenschutz und DSGVO-Konformität**

#### **5.2.1 Datenverantwortlicher, Auftragsverarbeiter und Architektur**

**Datenverantwortlicher:** Das Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA) an der Universitätsmedizin Rostock (UMR) ist der Datenverantwortliche für diese Studie.

**Implikationen dieser Vereinbarung:**

* IBIMA/UMR trägt die volle Verantwortung für DSGVO-Konformität und Teilnehmerrechte
* Alle Betroffenenanfragen (Zugang, Löschung, Widerruf) werden vom Studienteam bei IBIMA bearbeitet

**Auftragsverarbeiter:** HEALES (Healthy Life Extension Society) wird die Sugar-Sugar-Webanwendung als Auftragsverarbeiter unter einem Auftragsverarbeitungsvertrag (AVV) mit UMR betreiben.

**Technische Architektur: Pull-Modell**

Die Studie verwendet eine sicherheitsfokussierte „Pull-Modell"-Architektur:

\[Teilnehmer\] → \[Sugar-Sugar App (HEALES-Server)\] ← \[UMR-Datenkollektor\]

                         ↓                                    ↑

                   \[Temporärer Cache\] ──────────────────→ \[Forschungsdatenbank (UMR)\]

**Funktionsweise:**

1. Teilnehmer interagiert mit der Sugar-Sugar-App auf HEALES-Servern
2. Abgeschlossene Sitzungsdaten werden verschlüsselt und vorübergehend auf HEALES-Servern zwischengespeichert
3. Das UMR-Datenerfassungssystem **zieht** Daten periodisch (alle 2 Stunden) von HEALES und entschlüsselt sie
4. Nach erfolgreichem Transfer wird Cache bei HEALES gelöscht
5. Alle dauerhaften Forschungsdaten werden ausschließlich auf UMR-Servern gespeichert
6. Auf der HEALES-Seite existiert keine Entschlüsselungsfähigkeit, was den temporären Cache sichert

**Sicherheitsvorteile:**

* UMR-Forschungsdatenbank hat keinen eingehenden Zugriff von externen Systemen
* HEALES kann keine Daten an UMR „pushen" – UMR initiiert alle Datenübertragungen, Datenfluss ist konstruktionsbedingt unidirektional
* Vorübergehende Speicherung verschlüsselter Daten im Cache ohne Entschlüsselungsschlüssel auf HEALES-Seite mindert Risiken unbefugten Cache-Zugriffs
* Reduzierte Angriffsfläche auf Forschungsdateninfrastruktur
* Klare Trennung zwischen Anwendungsschicht (HEALES) und Datenspeicherung (UMR)

**Temporärer Cache auf HEALES-Servern:**

* Enthält nur abgeschlossene Sitzungsdaten, die auf Übertragung warten, in verschlüsselter Form
* Maximale Aufbewahrung: 7 Tage (automatisch gelöscht, wenn Pull fehlschlägt)
* Verschlüsselt im Ruhezustand
* Kein direkter Zugriff auf Cache außer durch automatisiertes Pull-System
* Cache ist transiente Verarbeitung, keine dauerhafte Speicherung

**Auftragsverarbeitungsvertrag (AVV) legt fest:**

* HEALES verarbeitet Daten nur auf Anweisung von UMR
* Keine dauerhafte Speicherung von Forschungsdaten auf HEALES-Servern
* Keine unverschlüsselte Speicherung von Forschungsdaten auf HEALES-Servern
* Cache wird unmittelbar nach erfolgreichem Pull zu UMR gelöscht
* Automatische Cache-Löschung nach 7 Tagen unabhängig vom Pull-Status
* Sicherheitsmaßnahmen für temporären Cache (Verschlüsselung, Zugriffskontrollen)
* Auditrechte für UMR
* HEALES-Mitarbeiterzugriff beschränkt auf technische Wartung

**Keine anderen externen Auftragsverarbeiter:**

* Keine externen Analysen, CDN oder Drittanbieter-Dienste verarbeiten Teilnehmerdaten
* HEALES-Community-Mitglieder (außer aufgelistetem Studienteam) haben keinen Zugriff auf Teilnehmerdaten

#### **5.2.2 Identifizierung und Pseudonymisierung**

**Was gespeichert wird und warum:**

1. **E-Mail-Adresse (Klartext, verschlüsselt im Ruhezustand):** Separat von Forschungsdaten gespeichert, nur für zwei Zwecke:
   * Ermöglichung von Widerrufsanfragen (Teilnehmer kontaktiert uns, wir finden und löschen seine Daten)
   * Optionale erneute Kontaktaufnahme für Studienergebnisse (nur wenn Teilnehmer zugestimmt hat)
2. **Studien-ID:** Zufälliger alphanumerischer Bezeichner, durch Hashing zugewiesen (z.B. f5afc4cf-9881-467d-88a1-325eb9558baa), bei der Registrierung vergeben
3. **Verknüpfungstabelle:** Eine separate verschlüsselte Datei, die Studien-ID ↔ E-Mail-Adresse zuordnet
   * Auf separaten verschlüsselten Laufwerk von Forschungsdaten gespeichert
   * Zugriff beschränkt auf PI (Anton Kulaga) und Ko-PI
   * Zweck: Widerruf und optionale erneute Kontaktaufnahme ermöglichen
4. **Forschungsdaten:** Alle Vorhersagedaten, CGM-Uploads, Fragebogenantworten nur mit Studien-ID pseudonymisiert gespeichert (keine E-Mail, kein Name)

**Hash-Klarstellung:** Wir verlassen uns NICHT auf E-Mail-Hashing zur Pseudonymisierung. Der Hash wird nur zur Duplikaterkennung bei der Registrierung verwendet (verhindert, dass dieselbe Person zweimal registriert). Die Verknüpfungstabelle enthält die eigentliche E-Mail für Widerruf-/erneute Kontaktzwecke.

#### **5.2.3 Aufbewahrungs- und Löschrichtlinie**

| Datentyp | Aufbewahrungsdauer | Auslöser für Löschung |
| :---- | :---- | :---- |
| E-Mail-Adressen | Bis Studienabschluss + 12 Monate | Verknüpfungstabelle nach Übergangsfrist vernichtet |
| Verknüpfungstabelle | Studienabschluss + 12 Monate | Vernichtet, sodass Daten vollständig anonym werden |
| Forschungsdaten (pseudonymisiert) | 10 Jahre gemäß deutschen Forschungsstandards | Entfällt – für Reproduzierbarkeit aufbewahrt |
| Hochgeladene CGM-Dateien | Sofort verarbeitet, Rohdateien innerhalb von 30 Tagen gelöscht | Automatisch nach Segmentextraktion |

#### **5.2.4 Widerrufsbeschränkungen (Wichtig)**

**Widerruf ist jederzeit möglich BIS die Verknüpfungstabelle vernichtet wird** (ca. 12 Monate nach Studienabschluss). Danach:

* Forschungsdaten werden vollständig anonym (keine erneute Identifizierung möglich)
* Widerrufsanfragen können nicht erfüllt werden, da wir nicht identifizieren können, welche Daten dem Antragsteller gehören
* Diese Einschränkung ist klar im Einwilligungsformular angegeben

**Widerrufsprozess:**

1. Teilnehmer schreibt Studienkoordinator mit Widerrufswunsch
2. Wir finden ihre Studien-ID über die Verknüpfungstabelle
3. Alle mit dieser Studien-ID verbundenen Forschungsdaten werden dauerhaft gelöscht
4. Bestätigung wird an Teilnehmer gesendet

#### **5.2.5 Grenzüberschreitende Datenübertragungen**

**Keine Daten verlassen die Europäische Union.**

* **UMR-Forschungsdatenbank:** In Deutschland (EU) gelegen
* **HEALES verwaltetes Cloud-Konto:** In der EU gelegen (nur temporärer Cache, max. 24 Stunden)
* Keine Drittanbieter-Dienste, die Daten außerhalb der EU übertragen
* Kein CDN, keine externen Analysen oder Cloud-Dienste mit nicht-EU-Rechenzentren
* E-Mail-Kommunikation verwendet Standard-EU-basierte E-Mail-Anbieter

Teilnehmer außerhalb der EU können teilnehmen, aber ihre Daten werden ausschließlich innerhalb der EU unter DSGVO-Schutz verarbeitet und gespeichert.

#### **5.2.6 Datenspeichersicherheit**

* **Standort der UMR-Forschungsdatenbank:** Deutschland (EU)
* **Standort des HEALES-temporären Cache:** EU
* **Verschlüsselung während der Übertragung:** TLS 1.3 (sowohl App-zu-Nutzer als auch UMR-zu-HEALES-Pull)
* **Verschlüsselung im Ruhezustand:** AES-256 (sowohl UMR-Datenbank als auch HEALES-Cache)
* **Zugriffskontrollen:** Rollenbasiert; Forschungsdaten für Studienteam zugänglich; Verknüpfungstabelle nur für PIs zugänglich
* **Backup:** Verschlüsselte tägliche Backups innerhalb der EU (nur UMR; HEALES-Cache ist transient)
* **Audit-Protokollierung:** Alle Datenzugriffe protokolliert

---

## **6\. Ergebnismaße und Genauigkeitsmetriken**

### **6.1 Primäre Metriken**

Wir verwenden Standardmetriken aus der Glukosevorhersageliteratur \[1,9,10\], die direkten Vergleich mit veröffentlichten ML-Modell-Benchmarks ermöglichen (z.B. GlucoBench – weitere Details im Referenzabschnitt).

**Mittlerer absoluter Fehler (MAE):** Durchschnitt der absoluten Differenz zwischen vorhergesagten und tatsächlichen Glukosewerten (in mg/dL). Niedrigere Werte zeigen bessere Genauigkeit an.

 MAE \= (1 / n) × Σ |vorhergesagt − tatsächlich|

* Misst die typische Größe von Vorhersagefehlern
* Alle Fehler werden gleich gewichtet
* Gleiche Einheiten wie die Zielvariable

**Wurzel des mittleren quadratischen Fehlers (RMSE):** Quadratwurzel der durchschnittlichen quadratischen Differenzen. Bestraft größere Fehler stärker als MAE. Ebenfalls in mg/dL angegeben.

 RMSE \= sqrt(MSE)

* Gleiche Einheit wie die Zielvariable
* Bestraft große Fehler wie MSE
* Leichter zu interpretieren als MSE

**Mittlerer quadratischer Fehler (MSE):** Durchschnitt der quadratischen Differenzen zwischen vorhergesagten und tatsächlichen Werten.

 MSE \= (1 / n) × Σ (vorhergesagt − tatsächlich)²

* Bestraft große Fehler stärker
* Empfindlich gegenüber Ausreißern
* Einheiten sind quadratisch, was direkte Interpretation erschwert

**Mittlerer absoluter prozentualer Fehler (MAPE):** Der durchschnittliche absolute Fehler ausgedrückt als Prozentsatz des tatsächlichen Wertes.

 MAPE \= (100 / n) × Σ |(vorhergesagt − tatsächlich) / tatsächlich|

* Misst relativen Fehler
* Skalenunabhängig
* Kann irreführend sein, wenn tatsächliche Werte nahe null sind

Diese Metriken werden berechnet:

* Pro Versuch (über die 12 Vorhersagepunkte)
* Pro Teilnehmer (gemittelt über ihre 6–12 Versuche)
* Pro Gruppe (für Gruppenvergleiche)

### **6.2 Basismodell-Vergleiche**

Um die menschliche Leistung zu kontextualisieren, vergleichen wir mit einfachen Basismodellen unter Verwendung derselben Testsegmente:

* **Persistenzmodell:** Vorhersage, dass Glukose am letzten beobachteten Wert konstant bleibt
* **Lineare Extrapolation:** Den Trend der letzten 30 Minuten vorwärts projizieren

Dies wird nach der Datenerhebung durchgeführt, um einen Ausgangspunkt für den zukünftigen Teil der Studie zu setzen, in dem wir ML-Modelle integrieren werden. Es wird die Datenerhebung in dieser Studienphase nicht beeinflussen. Weitere Details finden sich in H6.

---

## **7\. Statistischer Analyseplan**

### **7.1 Überblick**

Die Studie erhebt **mehrere Messungen pro Teilnehmer** (jeweils 6–12 Vorhersagesegmente mit 12 Punkten pro Segment). Die Analyse berücksichtigt diese Messwiederholungsstruktur. Sie liefert einen genaueren Überblick über die Teilnehmer-Vorhersagefähigkeit als eine einmalige Messung.

### **7.2 Analysepopulationen**

* **Primäranalyse:** Alle Teilnehmer, die mindestens 6 analysierbare generische Datensegmente abschließen
* **Eigene Daten-Analyse:** Teilnehmer, die mindestens 6 eigene Datensegmente abschließen
  Die Anzahl der vorgeschlagenen Datensegmente ist auf die erwartete Variabilität in den Genauigkeitsmetriken (MAE/RMSE) zurückzuführen. Basierend auf GlucoBench-Daten liegt die Standardabweichung für Prognosegenauigkeit bei etwa 0,18–0,22 auf einer Skala von 0–1. Wenn es nur 2–3 Messungen pro Person gäbe, hätte die Schätzung ihrer Fähigkeit große Konfidenzintervalle.

## **7.3 Primäre Analysen**

### **H1 (Gruppenunterschied – Diabetesstatus)**

**Ziel**: Vergleich der Prognosegenauigkeit zwischen Personen mit Diabetes (PmD) und Personen ohne Diabetes (nicht-PmD).

**Datenzusammenfassung**: Jeder Teilnehmer sagt Glukosewerte für mehrere Zeitpunkte über verschiedene Glukoseverlaufspräsentationen voraus. Wir berechnen einen MAE-Wert pro Teilnehmer durch Mittelwertbildung der Vorhersagefehler über alle ihre Vorhersagen. Dies gibt uns einen zusammenfassenden Genauigkeitswert pro Person.

**Statistische Methode**:

1. **Normalitätsprüfung**: Wir prüfen zunächst, ob MAE-Werte innerhalb jeder Gruppe normalverteilt sind, mithilfe des Shapiro-Wilk-Tests (p > 0,05 zeigt Normalverteilung an).
2. **Gruppenvergleich**:
   * **Wenn Daten normalverteilt sind** (Shapiro-Wilk p > 0,05): Wir verwenden einen **Zwei-Stichproben-t-Test**. Dieser Test vergleicht den durchschnittlichen MAE zwischen zwei Gruppen unter Berücksichtigung der Variabilität innerhalb jeder Gruppe und der Stichprobengrößen. Der t-Test berechnet, ob die beobachtete Differenz der Mittelwerte größer ist als durch Zufall allein zu erwarten wäre.
   * **Wenn Daten nicht normalverteilt sind** (Shapiro-Wilk p < 0,05): Wir verwenden den **Mann-Whitney-U-Test**. Dieser nicht-parametrische Test vergleicht Gruppen, indem alle MAE-Werte vom besten zum schlechtesten gereiht werden (unabhängig von der Gruppe), dann wird getestet, ob eine Gruppe tendenziell bessere Ränge hat als die andere. Dieser Ansatz ist robust gegenüber Ausreißern und schiefen Verteilungen.
3. **Signifikanzniveau**: α \= 0,05 (zweiseitig)
4. **Effektgröße**: Wir berichten Cohen's d (für t-Test) oder rangbiseriale Korrelation (für Mann-Whitney), um das Ausmaß der Differenz zu quantifizieren.

**Warum dieser Ansatz**: Wir verwenden Zusammenfassungsstatistiken pro Person (ein MAE pro Teilnehmer) anstatt Tausende einzelner Vorhersagen zu analysieren, weil einzelne Vorhersagen derselben Person nicht unabhängig sind – sie werden durch die konsistente Vorhersagestrategie dieser Person beeinflusst. Zusammenfassung auf einen Wert pro Person stellt sicher, dass unsere statistischen Tests die Annahme unabhängiger Beobachtungen erfüllen.

---

### **H2 (Gruppenunterschied – CGM-Erfahrung)**

**Ziel**: Vergleich der Prognosegenauigkeit zwischen Personen, die aktuell CGM verwenden, und Personen, die noch nie CGM verwendet haben.

**Datenzusammenfassung**: Wie bei H1 – ein MAE-Wert pro Teilnehmer, gemittelt über alle ihre Vorhersagen.

**Statistische Methode**: Identischer Ansatz zu H1:

1. Shapiro-Wilk-Test zur Normalitätsbewertung
2. Zwei-Stichproben-t-Test (wenn normal) oder Mann-Whitney-U-Test (wenn nicht normal)
3. Signifikanzniveau α \= 0,05 (zweiseitig)
4. Entsprechende Effektgröße berichten

**Begründung**: Gleiche Logik wie H1 – wir vergleichen zwei unabhängige Gruppen an einer einzelnen Genauigkeitsmessung pro Person.

---

## **7.4 Sekundäre Analysen**

### **H3 (Dauerwirkung – Diabetes)**

**Ziel**: Prüfung, ob längere Diabetesdauer mit besserer Prognosegenauigkeit assoziiert ist.

**Datenzusammenfassung**: Für jeden Teilnehmer mit Diabetes haben wir:

* **Prädiktorvariable**: Diabetesdauer in Jahren (kontinuierliche Variable)
* **Ergebnisvariable**: MAE (ein Wert pro Person, berechnet wie in H1)

**Statistische Methode**:

1. **Normalitäts- und Linearitätsprüfung**:
   * Streudiagramm von Diabetesdauer (x-Achse) vs. MAE (y-Achse) erstellen, um die Beziehung visuell zu inspizieren
   * Shapiro-Wilk-Test verwenden, um zu prüfen, ob MAE-Werte normalverteilt sind
   * Streudiagramm auf Linearität vs. Kurvenverläufe untersuchen
2. **Korrelationsanalyse**:
   * **Wenn MAE normalverteilt ist UND Beziehung linear erscheint**: **Pearson-Korrelationskoeffizient (r)** verwenden. Dieser misst die Stärke und Richtung einer linearen Beziehung zwischen zwei kontinuierlichen Variablen. Werte reichen von -1 (perfekte negative Beziehung) bis +1 (perfekte positive Beziehung). Wir erwarten negative Korrelation (längere Dauer → niedrigerer MAE).
   * **Wenn MAE nicht normalverteilt ist ODER Beziehung nicht linear erscheint**: **Spearmans Rangkorrelation (ρ)** verwenden. Diese funktioniert wie Pearsons, verwendet aber Ränge statt tatsächlicher Werte, was sie robust gegenüber Ausreißern macht und monotone Beziehungen erkennen kann, auch wenn sie nicht perfekt linear sind.
3. **Signifikanzniveau**: α \= 0,05 (zweiseitig)
4. **Explorative Analyse**: Da wir erwarten, dass die Beziehung ein Plateau erreichen kann (große Verbesserung in frühen Jahren, minimale Verbesserung nach 5+ Jahren), werden wir zusätzlich:
   * Ein logarithmisches Modell anpassen: MAE \= β₀ \+ β₁·log(Dauer \+ 1)
   * Linearen vs. logarithmischen Fit mit R²-Werten vergleichen
   * Eine Visualisierung erstellen, die zeigt, wie sich MAE über Dauerkategorien verändert (<1 Jahr, 1–5 Jahre, 5–10 Jahre, >10 Jahre)

**Warum dieser Ansatz**: Korrelationsanalyse ist angemessen, wenn die Beziehung zwischen zwei kontinuierlichen Variablen untersucht wird. Wir verwenden Spearmans als Backup, da Lernkurven oft abnehmende Erträge zeigen (nicht-lineare Muster), und Spearman kann diese Beziehungen erkennen, auch wenn sie keine perfekten geraden Linien sind.

---

### **H4 (CGM-Erfahrungseffekt)**

**Ziel**: Prüfung, ob längere CGM-Erfahrung mit besserer Prognosegenauigkeit unter CGM-Nutzern assoziiert ist.

**Datenzusammenfassung**:

* **Prädiktorvariable**: CGM-Erfahrung in Jahren (kontinuierliche Variable, nur für CGM-Nutzer)
* **Ergebnisvariable**: MAE (ein Wert pro CGM-Nutzer)

**Statistische Methode**: Identischer Ansatz zu H3:

1. Streudiagramm-Visualisierung und Normalitätsprüfung (Shapiro-Wilk)
2. Pearsons Korrelation (wenn normal/linear) oder Spearmans Korrelation (wenn nicht normal/nicht linear)
3. Explorative logarithmische Modellierung zum Testen auf Plateaueffekte
4. Signifikanzniveau α \= 0,05

**Begründung**: Gleiche Logik wie H3 – wir erwarten, dass CGM-Nutzer anfangs schnelle Verbesserungen zeigen, mit Lernplateau, nachdem sie häufige Glukosemuster verinnerlicht haben.

---

### **H5 (Eigene vs. Generische Daten)**

**Ziel**: Prüfung, ob Teilnehmer genauer vorhersagen, wenn sie ihre eigenen Glukosedaten im Vergleich zu generischen anonymisierten Daten betrachten.

**Datenzusammenfassung**: Dies ist ein **Innersubjekt-Vergleich**. Teilnehmer, die beide Bedingungen abschließen, haben:

* **Eigene Daten MAE**: Durchschnittsfehler über alle Vorhersagen auf eigenen Glukoseverläufen
* **Generische Daten MAE**: Durchschnittsfehler über alle Vorhersagen auf anonymisierten Verläufen
* **Differenzscore**: Generischer MAE − Eigener MAE (positive Werte zeigen bessere Leistung bei eigenen Daten an)

**Statistische Methode**:

1. **Warum gepaarte Analyse**: Wir verwenden „gepaarte" Tests, weil wir **zwei Messungen von derselben Person** haben (Eigene-Daten-Genauigkeit vs. generische Daten-Genauigkeit). Dies unterscheidet sich grundlegend von H1–H2, wo wir verschiedene Personen vergleichen. Gepaarte Tests berücksichtigen, dass dieselbe Person in beiden Bedingungen erscheint, und kontrollieren personenspezifische Faktoren wie allgemeine Vorhersagefähigkeit, Aufmerksamkeit, Motivation usw.
2. **Normalitätsprüfung**: Shapiro-Wilk-Test auf **Differenzscores** (nicht auf den rohen MAE-Werten)
3. **Vergleich**:
   * **Wenn Differenzscores normalverteilt sind**: **Gepaarter Stichproben-t-Test** verwenden. Dies testet, ob die durchschnittliche Differenz zwischen Bedingungen signifikant von null verschieden ist, unter Berücksichtigung der Innersubjekt-Korrelation.
   * **Wenn Differenzscores nicht normalverteilt sind**: **Wilcoxon-Vorzeichenrangtest** verwenden. Dies ist das nicht-parametrische Äquivalent des gepaarten t-Tests – er rangiert die absoluten Differenzen und testet, ob positive Differenzen (bessere Leistung bei eigenen Daten) häufiger sind als negative.
4. **Signifikanzniveau**: α \= 0,05 (zweiseitig)
5. **Effektgröße**: Cohen's d für gepaarte Design berichten

**Warum dieser Ansatz**: Gepaarte Tests sind leistungsfähiger als unabhängige Tests, weil sie Variabilität aufgrund individueller Unterschiede entfernen. Wenn Person A einfach natürlich besser in Vorhersageaufgaben ist als Person B, spielt das keine Rolle – uns interessiert nur, ob jede Person über die zwei Datentypen unterschiedlich abschneidet.

---

### **H6 (Mensch vs. Basismodelle)**

**Hinweis**: Diese Hypothese wird auf zukünftige Arbeit verschoben, wenn Basismodelle implementiert sind. Bei der Analyse werden wir ähnliche gepaarte Vergleichsansätze verwenden und den MAE jedes Teilnehmers mit dem MAE der Berechnungsmodelle auf denselben Glukoseverläufen vergleichen.

---

## **Zusammenfassungstabelle der statistischen Methoden**

| Hypothese | Vergleichstyp | Primärer Test | Alternativer Test | Wenn Alternative verwenden |
| ----- | ----- | ----- | ----- | ----- |
| H1 | Unabhängige Gruppen (PmD vs. nicht-PmD) | Unabhängiger t-Test | Mann-Whitney U | Shapiro-Wilk p < 0,05 |
| H2 | Unabhängige Gruppen (CGM vs. nicht-CGM) | Unabhängiger t-Test | Mann-Whitney U | Shapiro-Wilk p < 0,05 |
| H3 | Korrelation (Dauer vs. MAE) | Pearsons r | Spearmans ρ | Nicht normal oder nicht linear |
| H4 | Korrelation (CGM-Erfahrung vs. MAE) | Pearsons r | Spearmans ρ | Nicht normal oder nicht linear |
| H5 | Gepaarter Vergleich (eigen vs. generisch) | Gepaarter t-Test | Wilcoxon-Vorzeichenrang | Differenzscores nicht normal |

**Alle Tests verwenden α \= 0,05 Signifikanzniveau. Effektgrößen werden für alle Analysen berichtet.**

### **7.5 Erwartete Effektgrößen**

Basierend auf GlucoBench und verwandter Glukosevorhersageliteratur für **60-Minuten-Vorhersagezeiträume**:

**Modellleistung aus veröffentlichten Benchmarks (MAE in mg/dL):**

Die Leistung variiert erheblich über Datensätze und Bedingungen. Repräsentative Bereiche aus der Literatur:

* **Lineare Regression / ARIMA \[7,8\]:** MAE ~12–20 mg/dL (GlucoBench ID-Daten), RMSE ~23–27 mg/dL (andere Studien)
* **Deep Learning (Transformer, Gluformer \[2,7,8\]):** MAE ~11–17 mg/dL je nach Datensatz
* **Modernste personalisierte Modelle:** MAE ~15–17 mg/dL (neueste LLM-basierte Ansätze \[3\])

Hinweis: Werte variieren erheblich nach Datensatzgröße, Populationsmerkmalen und ob die Auswertung in-distribution (ID) oder out-of-distribution (OD) ist. GlucoBench berichtet, dass Deep-Learning-Modelle erheblich besser als einfache Baselines auf OD-Daten verallgemeinern.

**Erwartete Effektgrößen für Studienhypothesen:**

Angesichts dieser Variabilität verwenden wir konservative Annahmen:

* **H1 (PmD vs. nicht-DM):** Ausgehend von SD ~8–12 mg/dL über Teilnehmer und einem bedeutsamen Unterschied von ~3–5 mg/dL zwischen Gruppen entspricht dies Cohen's d ~0,3–0,5 (kleiner bis mittlerer Effekt).
* **H2 (Mensch vs. Baselines):** Die Lücke zwischen einfachen und fortgeschrittenen Modellen beträgt typischerweise ~5–10 mg/dL. Wir erwarten, dass Menschen in diesem Bereich liegen. Weitere Beschreibung der erwarteten menschlichen Verteilung finden sich in der Stichprobengröße.
* **H3, H4 (Dauer/CGM-Korrelationen):** Wir erwarten Korrelationen von r ~0,15–0,30 zwischen Erfahrung und Genauigkeit, basierend auf Lernkurvenannahmen.
* **H5 (Eigen vs. generisch):** Wir erwarten eine Verbesserung von ~2–4 mg/dL bei Vorhersage eigener Daten (gepaarter Effekt). Dies ist wichtig, da es die erwartete Differenz zwischen dem tatsächlichen Blutzuckerwert und dem geschätzten Glukosewert (EGV) abdeckt, den CGMs liefern.

**Wichtiger Vorbehalt:** Diese Effektgrößenschätzungen sind aus der Variabilität zwischen ML-Modellen abgeleitet, nicht aus früheren Studien zur menschlichen Vorhersage (die nicht existieren). Die tatsächliche menschliche Leistungsverteilung ist unbekannt und wird durch diese Studie etabliert. Wir betonen, dass diese Zahlen auf Basis der im Referenzabschnitt genannten Papiere geschätzt werden, insbesondere des GlucoBench-Papiers.

---

## **8\. Stichprobengröße**

### **8.1 Ziel-Einschreibung**

**Ziel:** Ca. 200 Teilnehmer insgesamt

* Ca. 100 Personen mit Diabetes (PmD)
* Ca. 100 Personen ohne Diabetes (nicht-DM)
* Unter PmD: Ziel für 70–90 Teilnehmer, die eigene Daten hochladen

**Minimum viable:** Ca. 150 Teilnehmer (75 pro Gruppe)

### **8.2 Begründung**

Stichprobengrößenziele basieren auf Effektgrößenschätzungen aus ML-Modell-Benchmarks, mit Anerkennung der Unsicherheit:

**Umgang mit Messwiederholungen:** Jeder Teilnehmer trifft 6–12 Vorhersagen, was bedeutet, dass unsere Daten eine Messwiederholungsstruktur haben. Wir berücksichtigen dies auf zwei Weisen: (1) Unsere primären Analysen verwenden Mittelwerte pro Person (ein MAE-Wert pro Teilnehmer), was die Unabhängigkeitsannahme für t-Tests und Korrelationen erfüllt, und (2) für detailliertere Analysen verwenden wir gemischte Modelle, die die Korrelation zwischen Wiederholungsmessungen derselben Person explizit modellieren.

**Bedeutungsvolle Unterschiede:** Wir halten einen Unterschied von 3–4 mg/dL im MAE für klinisch bedeutsam, weil er etwa der Hälfte des Messfehlers der CGM-Geräte selbst entspricht (die eine mittlere absolute Relatifabweichung von 8–10% vom Blutzucker haben, oder etwa 7–9 mg/dL bei typischen Glukosespiegeln). Eine Korrelation von r=0,25 erklärt etwa 6% der Varianz, was, obwohl bescheiden, es wert wäre zu verstehen für zukünftiges Interventionsdesign.

**H1 (Diabetes vs. Nicht-Diabetes-Gruppenvergleich):** Um einen Unterschied von 4 mg/dL im mittleren absoluten Fehler (MAE) zwischen Gruppen zu erkennen, unter Annahme einer Standardabweichung von 10 mg/dL (Cohen's d ≈ 0,4), benötigen wir 80–100 Teilnehmer pro Gruppe. Wir verwendeten einen einseitigen Test mit α=0,025 hier, weil frühere Literatur andeutet, dass Personen mit Diabetes möglicherweise besser vorhersagen, obwohl die Richtung nicht sicher ist. Diese Bonferroni-Anpassung berücksichtigt das Testen zweier primärer Vergleiche (H1 und H2).

**H2 (CGM-Nutzer vs. Nicht-Nutzer):** Gleiche Berechnung wie H1 – wir erwarten ähnliche Effektgrößen und benötigen ca. 80–100 pro Gruppe. Der gepaarte Charakter einiger Vergleiche innerhalb von Teilnehmern (wo dieselbe Person mehrere Vorhersagen trifft) gibt uns tatsächlich zusätzliche statistische Power, aber wir sind konservativ in unseren Schätzungen.

**H3 und H4 (Korrelationsanalysen):** Um eine Korrelation von r=0,25 zwischen Erfahrungsdauer und Prognosegenauigkeit mit 80% Power zu erkennen, benötigen wir 100–120 Teilnehmer. Der Bereich (100–120) spiegelt Unsicherheit in der wahren Korrelationsstärke wider – wenn die tatsächliche Korrelation schwächer als r=0,25 ist, bräuchten wir das höhere Ende des Bereichs. Wir wählten r=0,25 als Ziel, weil kleinere Korrelationen von begrenzter praktischer Bedeutung wären.

**H5 (Eigene Daten vs. generische Daten-Vergleich):** Dies ist ein Innersubjekt-Vergleich, sodass wir mehr statistische Power haben. Um einen Unterschied von 3 mg/dL in gepaarten Messungen zu erkennen (unter Annahme eines gepaarten SD von 6 mg/dL), benötigen wir ca. 70 Teilnehmer, die beide Aufgaben abschließen. Das gepaarte Design ist effizienter, weil jede Person als ihre eigene Kontrollperson dient.

**Wichtiger Vorbehalt:** Unsicherheit der Stichprobengröße

Unsere Stichprobengrößenberechnungen basieren auf ML-Modellleistung, aber menschliches Verhalten kann abweichen:

Warum das wichtig ist:

* ML-Modelle sind konsistent → vorhersagbare Variabilität (SD ~10 mg/dL)
* Menschen sind variabel → individuelle Unterschiede, Lerneffekte, Erschöpfung
* Risiko: Wenn die tatsächliche menschliche SD von den Annahmen abweicht, ändert sich die Power drastisch

Beispiele:

| Szenario | Angenommene SD | Tatsächliche SD | Geplante N pro Gruppe | Tatsächliche Power | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Optimistisch | 10 mg/dL | 8 mg/dL | 100 | ~95% | Überpowert |
| Basisfall | 10 mg/dL | 10 mg/dL | 100 | 80% | Angemessen |
| Konservativ | 10 mg/dL | 12 mg/dL | 100 | ~65% | Unterpowert |
| Pessimistisch | 10 mg/dL | 15 mg/dL | 100 | ~45% | Stark unterpowert |

**Ergebnis:** Studie könnte unterpowert sein, um echte Effekte zu erkennen, oder Ressourcen mit unnötiger Einschreibung verschwenden.

---

**Vorgeschlagene Lösung:** Adaptives Zweistufendesign

**Stufe 1 –** Zwischenanalyse (N=60–75 pro Gruppe)

* Beobachtete SDs und Effektgrößen aus echten menschlichen Daten berechnen
* Erforderliche Stichprobengröße mit empirischen Schätzungen neu berechnen
* Rekrutierungsziel anpassen, um 80% Power beizubehalten

**Stufe 2 –** Angepasste Rekrutierung

* Einschreibung auf überarbeitetes Ziel basierend auf Zwischenergebnissen fortsetzen
* Vorher festgelegte Entscheidungsregeln:
  * *„Wenn beobachtete SD \= 8 mg/dL → bei 100 pro Gruppe stoppen (bereits überpowert)"*
  * *„Wenn beobachtete SD \= 12 mg/dL → auf 130 pro Gruppe erhöhen"*
  * *„Wenn beobachtete SD >15 mg/dL → auf maximal 150 pro Gruppe erhöhen"*
* Maximale Obergrenze: 150 pro Gruppe

Vorteile:

* Stellt angemessene Power mit realen Daten sicher
* Vermeidet Überrekrutierung, wenn Variabilität niedriger als erwartet
* Verhindert schwere Unterpowerung, wenn Variabilität höher ist

**8.3 Erwartetes Ergebnis**

Mit unserer Zieleinschreibung (100 pro Gruppe, möglicherweise auf 150 erweiterbar) sollten wir ausreichende Power für alle geplanten Analysen haben, wenn unsere Variabilitätsschätzungen ungefähr stimmen. Aber der eigentliche Wert dieser Studie ist nicht nur das Testen unserer spezifischen Hypothesen – es ist die Etablierung der ersten empirischen Benchmarks für menschliche Glukosevorhersagegenauigkeit.

Selbst wenn wir entdecken, dass Menschen viel variabler als ML-Modelle sind, ist das ein veröffentlichenswertes Ergebnis. Es würde uns sagen, dass menschliche Vorhersagefähigkeit grundsätzlich weniger konsistent als algorithmische Ansätze ist, was Implikationen für das Design und die Bewertung klinischer Entscheidungsunterstützungswerkzeuge hat.

**Fehlende Daten und Ausschlüsse:** Wir verwenden Complete-Case-Analyse für die primären Ergebnisse (Teilnehmer, die mindestens 6 gültige Vorhersagesegmente abschließen). Wenn fehlende Daten 10% der rekrutierten Teilnehmer überschreiten, führen wir Sensitivitätsanalysen durch, die Kompletteure vs. Nicht-Kompletteure auf Baseline-Merkmale vergleichen. Wir erwarten keine wesentlichen fehlenden Daten, weil die Aufgabe online ist und nur 15–20 Minuten dauert.

**Multiplizität:** Wir haben zwei primäre Hypothesen (H1 und H2) mit Bonferroni-Korrektur (α=0,025 pro Test). Sekundäre Hypothesen (H3, H4, H5) sind explorativ und werden mit nominalen p-Werten ohne Anpassung berichtet, klar als explorative Analysen gekennzeichnet.

**Wer die Analyse durchführt:** Primäre statistische Analysen werden von Anton Kulaga (PI) mit Anleitung von Benjamin Otte (biostatistischer Berater) durchgeführt. Alle Analysen werden in Python mit Standardpaketen durchgeführt. Analysecode wird neben den veröffentlichten Ergebnissen öffentlich zugänglich gemacht.

**Störfaktoren:** Das Querschnittsdesign der Studie begrenzt unsere Fähigkeit, Störfaktoren zu kontrollieren. Wir erheben und berichten Schlüsselvariablen (Alter, Diabetesdauer, CGM-Erfahrung) und führen stratifizierte Analysen durch, wo die Stichprobengröße es erlaubt. Die primären Vergleiche (PmD vs. nicht-PmD, CGM vs. nicht-CGM) sind beschreibend statt kausal, sodass Störfaktoren weniger problematisch sind als bei interventionellen Studien.

**Bestätigend vs. explorativ:** H1 und H2 sind bestätigende Hypothesen mit Bonferroni-angepassten Signifikanzniveaus. H3, H4 und H5 sind explorativ und werden als solche berichtet, mit Konfidenzintervallen und Effektgrößen statt alleiniger Abhängigkeit von p-Werten.

---

## **9\. Datenqualitätskontrolle**

### **9.1 Automatisierte Prüfungen**

* E-Mail-Eindeutigkeitsvalidierung
* Altersbereichsvalidierung
* Vervollständigungszeit-Prüfungen
* Vorhersagepunkt-Validierung (alle 12 Punkte erforderlich)
* CGM-Datenqualitätsprüfungen für Uploads

### **9.2 Ausschlusskriterien für die Analyse**

* Segmente mit unvollständigen Vorhersagen (weniger als 12 Punkte)
* Segmente mit übermäßig fehlenden CGM-Kontextdaten
* Teilnehmer mit weniger als 5 gültigen Segmenten

---

## **10\. Risiko-Nutzen-Analyse**

### **10.1 Risiken für Teilnehmer**

#### **10.1.1 Physische Risiken**

**Keine.** Dies ist eine Online-Beobachtungsstudie ohne physische Interventionen:

* Keine medizinischen Verfahren
* Keine Medikamentengabe
* Keine persönlichen Besuche erforderlich
* **Keine Echtzeit-Gesundheitsüberwachung** – alle Daten sind historisch
* **Keine Verbindung zu aktiven medizinischen Geräten** – Teilnehmer müssen keine Geräte tragen

#### **10.1.2 Psychologische Risiken**

**Minimal:**

* Mögliche Frustration mit Vorhersageaufgaben (gemildert durch klare Anweisungen, Übungsversuche)
* Leichte Leistungsangst (gemildert durch Betonung des Forschungszwecks)
* Datenschutzbedenken bezüglich der Weitergabe von CGM-Daten (gemildert durch optionale Teilnahme, vollständige Datenschutzerklärung)

**Gesamtbewertung:** Risiken vergleichbar mit dem Ausfüllen eines Online-Tests oder einer Umfrage.

### **10.2 Vorteile**

**Direkte Vorteile für Teilnehmer:** Keine (nur Forschungsstudie). Ergebnisse stellen keinen medizinischen Rat dar.

**Wichtige Haftungsausschlüsse, die Teilnehmern mitgeteilt werden:**

* Genauigkeitswerte messen nur Vorhersageleistung – sie haben keine diagnostische oder therapeutische Bedeutung
* Ergebnisse sollten nicht zur Anpassung von Insulindosierungen, Ernährungsentscheidungen oder medizinischen Entscheidungen verwendet werden
* Teilnehmer sollten weiterhin unabhängig die Anleitung ihres Gesundheitsdienstleisters befolgen

**Indirekte Vorteile:**

* Beitrag zum wissenschaftlichen Wissen
* Persönliche Einblicke in die eigene Vorhersagefähigkeit
* Unterstützung der Entwicklung besserer Glukosevorhersage-Werkzeuge

---

## **11\. Teilnehmerschutz und Ethik**

### **11.1 Informierte Einwilligung**

Wichtiger Hinweis – alle Einwilligungen werden durch Klicken auf entsprechende Checkboxen in der Online-Oberfläche gegeben und digital gespeichert. Wenn die Pflichteinwilligung nicht gegeben wird, darf der Teilnehmer nicht weiter fortfahren, was jede Teilnahme ohne Einwilligung verhindert.

**Altersverifikations-Gate:**

Bevor auf Studieninhalte zugegriffen wird, müssen Teilnehmer bestätigen, dass sie 18 Jahre oder älter sind:

* Erster Bildschirm zeigt: „Diese Studie steht Erwachsenen ab 18 Jahren offen. Bitte bestätigen Sie Ihr Alter, um fortzufahren."
* Zwei Schaltflächen: „Ich bin 18 Jahre oder älter" (geht zur Einwilligung über) / „Ich bin unter 18" (zeigt Meldung: „Vielen Dank für Ihr Interesse, aber diese Studie steht nur Erwachsenen offen. Bitte schließen Sie diese Seite.")
* Wenn „unter 18" ausgewählt wird: Keine Daten werden gesammelt, Sitzung endet sofort, keine Cookies oder Bezeichner gespeichert
* Dieses Altersgate erscheint vor jeder persönlichen Datenerhebung

**Zweisprachiger Einwilligungsprozess:**

Die Studie stellt Einwilligungsmaterialien in Englisch und Deutsch bereit. Teilnehmer wählen ihre bevorzugte Sprache zu Beginn:

* **Sprachauswahl:** Teilnehmer wählen „English" oder „Deutsch" auf der Startseite
* **Vollständige Materialien:** Alle Einwilligungsinformationen, Studienanweisungen und Rückmeldungen werden in der gewählten Sprache angezeigt
* **Gleichwertiger Inhalt:** Beide Sprachversionen enthalten identische Informationen und gewährleisten gleiches Verständnis unabhängig von der Sprachpräferenz

**Elektronisches Einwilligungsformular umfasst:**

* Klare Studieninformationen in nicht-technischer Sprache
* Betonung der freiwilligen Teilnahme
* Datenschutz- und DSGVO-Rechtserklärung
* Widerrufsprozeduren und -einschränkungen (Widerruf bis zur Datenanonymisierung möglich)
* Kontaktinformationen

**Einwilligungscheckboxen (Pflicht):**

* Ich bestätige, dass ich 18 Jahre oder älter bin, die Studieninformationen gelesen und verstanden habe und freiwillig zustimme, teilzunehmen
* Ich stimme der Datenverarbeitung für Forschungszwecke zu und verstehe, dass ich bis zur Datenanonymisierung widerrufen kann (DSGVO Art. 6(1)(a), 9(2)(a))

**Optionale Einwilligungscheckboxen (klar getrennt von Studieneinwilligung):**

* Ich stimme zu, meine eigenen CGM-Daten für die optionale eigene Datenaufgabe hochzuladen
* Ich stimme zu, für Studienergebnisse erneut kontaktiert zu werden (E-Mail nur für diesen Zweck gespeichert)

**Werbemitteilungen (Getrennt von Studieneinwilligung):**

Jede Opt-in für Werbemitteilungen über HEALES oder verwandte Projekte ist:

* Auf einer SEPARATEN Seite NACH Studienabschluss präsentiert (nicht während der Einwilligung)
* Klar als unrelated zur Studienteilnahme gekennzeichnet
* Hat keinen Einfluss auf Studienteilnahme oder Datenhandhabung
* Kann ohne Konsequenzen abgelehnt werden

### **11.2 Vergütung**

Keine monetäre Vergütung. Nicht-monetäre Anreize umfassen personalisiertes Genauigkeitsfeedback und teilbares Ergebniskärtchen.

### **11.3 Versicherung**

Keine studiespezifische Versicherung erforderlich aufgrund minimalen Risikos (Online-Umfrage-äquivalent).

---

## **12\. Zeitplan**

Der Studienzeitplan ist flexibel und wird basierend auf dem Rekrutierungsfortschritt und operativen Bedürfnissen angepasst. Allgemeine Phasen umfassen:

1. **Vorbereitung:** Ethikantrag, Plattformfinalisierung, Rekrutierungsmaterialvorbereitung
2. **Pilottesting:** Kleinmaßstäbliches Testen mit Feedback-Erhebung
3. **Rekrutierung und Datenerhebung:** Fortlaufend bis Ziel-Einschreibung erreicht
4. **Analyse:** Datenverarbeitung, statistische Analyse
5. **Verbreitung:** Manuskriptvorbereitung, Veröffentlichung, Teilnehmerkommunikation

Spezifische Zeitpläne werden basierend auf Ethik-Genehmigungsdatum und Rekrutierungserfolg festgelegt.

---

## **13\. Einschränkungen**

### **13.1 Selektionsbias**

Teilnehmer sind selbst ausgewählte Freiwillige, die möglicherweise nicht die allgemeine CGM-Nutzerpopulation repräsentieren.

### **13.2 Akademische vs. Reale Referenzwerte**

Während diese Studie realistischere Bedingungen als kontrollierte akademische Datensätze verwendet, können Online-Teilnehmer immer noch von typischen CGM-Nutzern abweichen.

### **13.3 Einzelsitzungsdesign**

Kein longitudinales Follow-up; Lerneffekte über die Zeit können nicht bewertet werden.

---

## **14\. Kontaktinformationen**

**Hauptuntersucherin:**

 Anton Kulaga  
 Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA)  
 Universitätsmedizin Rostock  
 E-Mail: anton.kulaga@uni-rostock.de

**Mituntersucherinnen:**

Livia Zaharia, MSc  
 HEALES \- Healthy Life Extension Society  
 E-Mail: [liviazaharia2020@gmail.com](mailto:liviazaharia2020@gmail.com)

**Biostatistischer Berater:**

Benjamin Otte, MSc  
 Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA)  
 Universitätsmedizin Rostock  
 E-Mail: benjamin.otte@uni-rostock.de

**Datenmanager:**  
 Nikolay Usanov, MSc  
 HEALES \- Healthy Life Extension Society  
 ML-Ingenieur und Bioinformatiker

**Beirat:**

* Prof. Georg Fullen \- Universitätsmedizin Rostock
* Irina Gaynanova, PhD (Statistische Beraterin) \- Texas A\&M University
* Renat Sergazinov, PhD (Technischer Berater) \- GlucoBench-Autor

## Referenzen:

\[1\] Sergazinov, R., Chun, E., Rogovchenko, V., Fernandes, N., Kasman, N., & Gaynanova, I. (2024). GlucoBench: Curated List of Continuous Glucose Monitoring Datasets with Prediction Benchmarks. International Conference on Learning Representations (ICLR). https://doi.org/10.48550/arXiv.2410.05780

\[2\] Sergazinov, R., Armandpour, M., & Gaynanova, I. (2023). Gluformer: Transformer-Based Personalized Glucose Forecasting with Uncertainty Quantification. IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP). https://doi.org/10.48550/arXiv.2209.04526

\[3\] Yang, F., Wang, X., Liu, Y., et al. (2024). From Glucose Patterns to Health Outcomes: A Generalizable Foundation Model for Continuous Glucose Monitor Data Analysis. arXiv. https://doi.org/10.48550/arXiv.2408.11876

\[4\] Battelino, T., Danne, T., Bergenstal, R. M., et al. (2019). Clinical Targets for Continuous Glucose Monitoring Data Interpretation: Recommendations from the International Consensus on Time in Range. Diabetes Care, 42(8), 1593-1603. https://doi.org/10.2337/dci19-0028

\[5\] Rodbard, D. (2016). Continuous Glucose Monitoring: A Review of Successes, Challenges, and Opportunities. Diabetes Technology & Therapeutics, 18(S2), S2-3-S2-13. https://doi.org/10.1089/dia.2015.0417

\[6\] Hall, H., Perelman, D., Breschi, A., et al. (2018). Glucotypes reveal new patterns of glucose dysregulation. PLOS Biology, 16(7), e2005143. https://doi.org/10.1371/journal.pbio.2005143

\[7\] Jaloli, M., & Cescon, M. (2022). Long-term Prediction of Blood Glucose Levels in Type 1 Diabetes Using a CNN-LSTM-Based Deep Neural Network. Journal of Diabetes Science and Technology, 17(6), 1590-1601. https://doi.org/10.1177/19322968221092785

\[8\] Li, K., Daniels, J., Liu, C., Herrero, P., & Georgiou, P. (2019). Convolutional recurrent neural networks for glucose prediction. IEEE Journal of Biomedical and Health Informatics, 24(2), 603-613. https://doi.org/10.1109/JBHI.2019.2908488

\[9\] Gaynanova, I., Punjabi, N., & Crainiceanu, C. (2022). Modeling continuous glucose monitoring (CGM) data during sleep. Biostatistics, 23(1), 223-239. https://doi.org/10.1093/biostatistics/kxaa023

\[10\] Broll, S., Urbanek, J., Buchanan, D., et al. (2021). Interpreting blood glucose data with R package iglu. PLOS ONE, 16(4), e0248560. https://doi.org/10.1371/journal.pone.0248560

---

**Anwendbare Vorschriften:**

* DSGVO / BDSG (Datenschutz) \- JA
* Deutsche Forschungsethik-Richtlinien \- JA
* Medizinprodukte-Verordnung (MDR) \- NICHT anwendbar
* AMG (Arzneimittelgesetz) \- NICHT anwendbar

---

**ENDE DES DOKUMENTS**

*Bei Fragen oder Klärungsbedarf wenden Sie sich bitte an:*  
 *Anton Kulaga: anton.kulaga@uni-rostock.de*  
 *Livia Zaharia: livia.zaharia@uni-rostock.de*
