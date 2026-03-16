# **Predicția umană a glucozei în următoarea oră pe baza contextului CGM anterior: un studiu online de benchmarking**

**Protocol de studiu (versiune scurtă)**

**Investigator principal:** Anton Kulaga – Institute for Biostatistics and Informatics in Medicine and Ageing (IBIMA), University Medical Center Rostock, Rostock, Germania

**Co‑investigatori:** Livia Zaharia (HEALES – Healthy Life Extension Society, Bruxelles, Belgia)

**Consiliere biostatistică:** Benjamin Otte, M.Sc. – Department of Biostatistics, IBIMA, University Medical Center Rostock

**Contextul proiectului:** Studiul este realizat ca parte a Sugar‑Sugar Glucose Accuracy Prediction Study, cu sprijinul HEALES.

**Număr de înregistrare:** Ref. number A 2026-0064  
**Primit de Comisia de Etică:** 27 februarie 2026

---

## **Prezentare generală**

**Context / fundal:**  
Modelele de învățare automată pentru predicția glucozei raportează de obicei metrici de acuratețe pe seturi de date academice controlate, însă nu există un **benchmark pentru acuratețea predicției umane**. Utilizatorii CGM anticipează frecvent valorile viitoare ale glucozei ca parte a auto‑managementului zilnic, dar calitatea acestor predicții nu a fost evaluată sistematic.

**Obiective:**

- (0) Cuantificarea acurateții umane în predicția glucozei pentru următoarea oră pe baza a 3 ore de istoric CGM  
- (1) Compararea acurateții între persoane cu diabet (tip 1 și tip 2) și persoane fără diabet (inclusiv pre‑diabet / utilizatori „wellness”)  
- (2) Compararea acurateții între utilizatori CGM și non‑utilizatori (utilizator CGM = utilizare > 1 lună)

**Design:**  
Studiu observațional online, transversal (cross‑sectional). Participanții efectuează **șase sau mai multe** predicții; este planificat un design adaptiv în două etape pentru dimensiunea eșantionului.

**Cadru (setting):**  
Platformă web (aplicația Sugar‑Sugar) găzduită de HEALES; datele de cercetare sunt stocate la University Medical Center Rostock.

**Participanți:**  
Țintă \(N \approx 200\) adulți (≥18 ani): aproximativ 100 persoane cu diabet și 100 fără diabet, recrutați prin social media și organizații de diabet. Designul adaptiv permite ajustarea până la 150 per grup după o analiză intermediară. În grupul fără diabet pot exista persoane care folosesc CGM pentru fitness, sport, biohacking, optimizarea stilului de viață etc.

Participanții sunt împărțiți în patru grupuri:

- PwD utilizatori CGM („PwD CGM”)
- PwD fără CGM („PwD no‑CGM”)
- non‑PwD utilizatori CGM („non‑PwD”)
- non‑PwD fără experiență CGM („NPE”)

**Proceduri:**  
Participanții care au date CGM sunt încurajați să încarce opțional propriile date istorice. Sarcina este să prezică cum se vor modifica valorile estimate ale glucozei cunoscând valorile anterioare; în aplicația web, acest lucru se face intuitiv, prin **desenarea unei linii** pe graficul glucozei. Participanții fără date sau care preferă să nu încarce pot utiliza seturi de date publice, anonimizate.

Fiecare participant va completa 6–12 sarcini. În fiecare sarcină, participantul prezice 12 puncte (la fiecare 5 minute pe parcursul a 60 de minute) folosind ca context cele 3 ore anterioare.

**De ce 6–12 sarcini?**

- **Fiabilitate:** o singură sarcină oferă o estimare instabilă; media pe 6–12 sarcini reduce eroarea de măsurare.
- **Putere statistică:** măsurările repetate cresc puterea (de exemplu 200 participanți × 10 sarcini ≈ 2.000 observații).
- **Variabilitate contextuală:** mai multe sarcini acoperă scenarii diverse (ora din zi, direcția trendului, contexte de evenimente).
- **Fezabilitate:** intervalul 6–12 echilibrează precizia cu efortul participantului (pilot: 15–20 minute).

**Indicatori principali:**  
Acuratețea predicțiilor este cuantificată prin **MAE** (Mean Absolute Error) și **RMSE** (Root Mean Squared Error), în mg/dL.

**Analiză statistică (pe scurt):**  
Comparații ale MAE/RMSE per‑persoană între grupuri (diabet vs fără diabet; utilizatori CGM vs non‑utilizatori) și comparații cu modele de bază (persistență, extrapolare liniară). Analiza ia în considerare structura cu măsuri repetate.

**Etică și diseminare:**  
Trimis către comisia de etică (Ethikkommission), University Medical Center Rostock. Studiu ne‑intervențional, folosind doar date istorice. Rezultatele urmează să fie publicate în reviste peer‑review.

---

### Protocol complet

În prezent, ghidul tehnic complet este disponibil în engleză:  
`data/input/study_design/The study - technical Guidebook.md`

