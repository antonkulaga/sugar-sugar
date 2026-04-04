# **Predicția Umană a Glicemiei din Ora Următoare pe Baza Contextului Anterior al Monitorului Continuu de Glucoză (MCG): Un Studiu de Referință Online**

**Protocolul studiului**

**Investigator Principal:** Anton Kulaga \- Institutul de Biostatistică și Informatică în Medicină și Cercetarea Îmbătrânirii (IBIMA), Centrul Medical Universitar Rostock, Rostock, Germania

**Co-investigatori:** Livia Zaharia (HEALES \- Healthy Life Extension Society, Bruxelles, Belgia)

**Consiliere biostatistică:** Benjamin Otte, M.Sc. \- Departamentul de Biostatistică, Institutul de Biostatistică și Informatică în Medicină și Cercetarea Îmbătrânirii (IBIMA), Centrul Medical Universitar Rostock, Rostock, Germania

**Contextul proiectului:** Acest studiu este realizat ca parte a Studiului de Predicție a Preciziei Glicemice Sugar-Sugar, susținut de HEALES (Healthy Life Extension Society)

**Număr de înregistrare:** Ref. A 2026-0064  
**Primit de Comitetul de Etică:** 27 februarie 2026

---

## **Prezentare Generală**

**Fundal:**

Modelele de învățare automată pentru predicția glicemiei raportează metrici de precizie derivate din seturi de date academice controlate, dar nu există nicio referință pentru precizia predicției umane. Utilizatorii MCG anticipează în mod regulat nivelurile viitoare de glucoză ca parte a autogestionării zilnice, totuși calitatea predicției nu a fost niciodată evaluată sistematic.

**Obiective:**

(0) Cuantificarea preciziei umane în predicția glicemiei din ora următoare pe baza a 3 ore de istoric MCG;

(1) Compararea preciziei de predicție între persoanele cu diabet (PcD) de tip 1 și tip 2 și persoanele fără diabet, inclusiv prediabet, utilizatori wellness și utilizatori fără experiență anterioară (non-DZ);

(2) Compararea preciziei de predicție între utilizatorii MCG și non-utilizatorii MCG. O persoană este considerată utilizator MCG dacă a folosit unul mai mult de o lună.

**Design:**

Studiu online observațional transversal în care utilizatorilor li se cere să facă predicții de șase sau mai multe ori și design adaptiv de dimensionare a eșantionului în două etape.

**Cadru:**

Platformă bazată pe web (aplicația Sugar-Sugar) găzduită de HEALES cu date de cercetare stocate la Centrul Medical Universitar Rostock.

**Participanți:**

N țintă ≈200 adulți (≥18 ani): aproximativ 100 PcD și 100 non-PcD, recrutați prin rețele sociale și organizații de diabet. Designul adaptiv permite ajustarea până la 150 pe grup pe baza analizei interimare. Pentru grupul non-DZ, există persoane care își folosesc MCG-urile pentru monitorizarea condiției fizice, îmbunătățirea sportivă, îmbunătățirea stilului de viață, biohacking etc. care au arătat interes preliminar de participare.

Participanții sunt împărțiți în patru grupuri: Utilizatori PcD MCG (grupul „PcD MCG"), PcD fără MCG (grupul „PcD fără-MCG"), Utilizatori non-PcD MCG (ex., pentru wellness, sport etc., grupul „non-PcD"), Utilizatori non-PcD fără-MCG fără experiență anterioară (grupul „FEA")

**Proceduri:**

Participanții cu date MCG sunt încurajați să încarce propriile date cu măsurători anterioare de glucoză (în continuare, date istorice pe scurt) pentru sarcina de predicție. Sarcina este de a prezice cum se vor schimba valorile de glucoză estimate de MCG (în continuare, VG) cunoscând valorile anterioare. În cazul aplicației noastre web, acest lucru se face în mod intuitiv, prin trasarea liniei pe un grafic VG. Pentru mai multe detalii, verificați secțiunea 4.2.

Participanții fără date MCG sau care preferă să nu încarce date pot folosi date terțe din seturi de date publice anonimizate care pot fi descărcate gratuit. Am compilat lista seturilor de date la [https://github.com/GlucoseDAO/glucose\_data\_processing/blob/main/docs/datasets.csv](https://github.com/GlucoseDAO/glucose_data_processing/blob/main/docs/datasets.csv) unde seturile de date cu coloana „Downloader" sunt complet publice.

Fiecare participant va finaliza 6 până la 12 sarcini de predicție. În fiecare sarcină, vor prezice ce se va întâmpla în ora următoare desenând puncte pe un grafic afișat într-o aplicație web. Specific, vor prezice 12 puncte de date — câte unul pentru fiecare interval de 5 minute pe parcursul perioadei de 60 de minute. Pentru a-i ajuta să facă aceste predicții, participanților li se vor arăta cele 3 ore anterioare de date ca context.

Multiple încercări de predicție pe participant sunt necesare pentru a obține estimări fiabile de precizie la nivel individual și putere statistică adecvată.

**Fiabilitatea măsurătorii:** O singură încercare de predicție oferă o estimare nesigură a capacității individuale din cauza variației aleatoare (ex., dificultatea segmentului, lapsusuri momentane de atenție). Calculând media pe 6–12 încercări se obțin metrici de precizie stabile și reproductibile prin reducerea erorii de măsurare.

**Puterea statistică:** Designul cu măsurători repetate crește substanțial puterea statistică față de designurile cu o singură încercare. Cu 200 de participanți completând câte 10 încercări, dimensiunea eficientă a eșantionului pentru analizele intra-persoană se apropie de 2.000 de observații, permițând detectarea dimensiunilor de efect mici până la moderate (Cohen's d ≥ 0,3) care ar necesita dimensiuni de eșantion nefezabile în designurile cu o singură încercare.

**Variabilitate contextuală:** Încercările multiple permit eșantionarea peste dinamici glicemice diverse (ora zilei, direcția tendinței, contextele evenimentelor), asigurând că estimările de precizie reflectă performanța în scenarii reprezentative mai degrabă decât un singur caz atipic.

**Fezabilitate:** Intervalul de 6–12 încercări echilibrează precizia de măsurare cu povara participantului. Testele pilot au indicat participare susținută timp de 15–20 de minute (aproximativ 10–12 segmente), după care efectele de oboseală pot compromite calitatea datelor.

Această abordare urmează practica psihometrică standard pentru stabilirea diferențelor individuale fiabile în sarcinile cognitive și se aliniază cu designurile de măsurători repetate utilizate frecvent în studiile de referință a performanței umane.

**Măsuri principale de rezultat:**

Vom măsura cât de precise sunt predicțiile folosind două metrici standard: Eroarea Absolută Medie (MAE) și Rădăcina Erorii Pătratice Medii (RMSE), ambele măsurate în mg/dL. Aceste metrici vor arăta cât de departe sunt predicțiile față de valorile reale de glucoză. Vom calcula aceste metrici atât pentru modelele de învățare automată, cât și pentru predicțiile participanților umani.

**Analiză statistică:**

Compararea grupului MAE/RMSE per persoană între PcD și non-DZ; compararea predicțiilor umane față de modelele de bază (persistență, extrapolare liniară). Analizele secundare examinează asocieri între experiență și precizie. Analiza ține cont de structura măsurătorilor repetate.

**Etică și diseminare:**

Depus la Comitetul de Etică, Centrul Medical Universitar Rostock. Studiu non-intervențional care utilizează doar date istorice. Rezultatele vor fi publicate în reviste cu recenzie.

---

## **1\. Fundal și Justificare**

### **1.1 Context: Utilizatorii MCG și Auto-predicția**

Dispozitivele de Monitorizare Continuă a Glucozei (MCG) \[5\] furnizează măsurători de glicemie la fiecare 5 minute, generând profiluri detaliate de glucoză pe 24 de ore. Tehnologia MCG este utilizată de mai multe populații:

**Persoane cu Diabet (PcD):**

* Folosesc datele MCG pentru a informa propria dozare a insulinei, programarea meselor și deciziile de activitate
* Dezvoltă recunoașterea intuitivă a tiparelor prin experiența zilnică cu tendințele lor glicemice
* Iau decizii de auto-gestionare bazate pe traiectoriile glicemice anticipate

**Persoane Conștiente de Sănătate (Utilizatori Wellness):**

* Persoane prediabetice care monitorizează glucoza pentru optimizarea stilului de viață
* Utilizatori non-diabetici interesați de sănătatea metabolică și longevitate
* Atleți și biohackeri care urmăresc răspunsul glucozei la dietă și exerciții

În toate cazurile, utilizatorii fac propriile predicții despre nivelurile viitoare de glucoză ca parte a auto-gestionării zilnice — acest studiu cuantifică acea capacitate de predicție.

### **1.2 Problema Referinței Lipsă**

Modelele actuale de învățare automată pentru prognoza glicemică raportează metrici tehnice (RMSE, MAE), dar acestea sunt derivate din **seturi de date academice controlate**. Conform GlucoBench \[1\], modelele de ultimă generație ating:

* **Predicții la 30 de minute:** RMSE 8–12 mg/dL, MAE 6–10 mg/dL
* **Predicții la 60 de minute:** RMSE 10–16 mg/dL, MAE 9–13 mg/dL

Cu toate acestea, aceste metrici au limitări importante:

1. **Performanță controlată vs. din lumea reală:** Referințele academice folosesc seturi de date organizate cu calitate consistentă a datelor. Utilizatorii reali MCG au lacune, erori de senzori și înregistrare inconsistentă a evenimentelor.
2. **Fără comparație umană:** Nu știm cum se compară aceste metrici ML cu capacitatea de predicție pe care utilizatorii experimentați MCG o dezvoltă prin utilizarea zilnică.
3. **Diversitate populațională:** Seturile de date academice se concentrează adesea pe tipuri specifice de diabet; utilizatorii din lumea reală includ populații diabetice, prediabetice și wellness cu contexte de predicție diferite.

**Acest studiu umple golul** stabilind cât de bine utilizatorii reali MCG își prezic propria glucoză în condiții realiste.
Consultați secțiunea de referințe pentru mai multe detalii.

### **1.3 Lacuna de Cercetare și Inovația**

Conform cunoștințelor noastre, **niciun studiu anterior nu a cuantificat sistematic precizia umană în predicția traiectoriilor glicemice din ora următoare**. Acest studiu abordează această lacună critică prin:

1. Stabilirea preciziei de bază a auto-predicției umane în diferite populații de utilizatori
2. Compararea performanței între cele patru grupuri menționate: PcD MCG, PcD fără-MCG, non-PcD MCG și FEA
3. Examinarea factorilor asociați cu precizia predicției (durata diabetului, experiența MCG)
4. Crearea unui punct de referință din lumea reală care completează metricile ML derivate în laborator

### **1.4 Justificarea Studiului**

Această cercetare este necesară deoarece:

* **Nu există nicio referință umană:** Nu știm cât de bine utilizatorii experimentați MCG își prezic propria glucoză
* **Referințele academice sunt prea optimiste:** Metricile ML din seturi de date organizate nu reflectă condițiile de performanță din lumea reală
* **Populații diverse de utilizatori:** Utilizatorii diabetici, prediabetici și wellness MCG pot avea capacități de predicție diferite
* **Contextul auto-gestionării:** Înțelegerea capacității de predicție umane informează așteptările realiste pentru instrumentele asistate de IA

---

## **2\. Obiectivele și Ipotezele Studiului**

### **2.1 Obiective Primare**

**Obiectivul 0:**

Cuantificarea cât de precis pot oamenii să prezică nivelurile de glucoză pentru ora următoare după ce au văzut cele 3 ore anterioare de date de glucoză, indiferent dacă folosesc MCG sau au diabet.

**Obiectivul 1:**

Cuantificarea și compararea cât de precis persoanele cu diabet (PcD) față de persoanele fără diabet (non-PcD) pot prezice nivelurile de glucoză pentru ora următoare după ce au văzut cele 3 ore anterioare de date de glucoză, indiferent dacă folosesc MCG (grupurile MCG și non-MCG combinate pe perechi după statul diabetic față de celălalt).

**Obiectivul 2:**

Cuantificarea și compararea preciziei persoanelor care folosesc deja monitoare continue de glucoză față de persoanele care nu folosesc MCG în prezicerea nivelurilor de glucoză pentru ora următoare după ce au văzut cele 3 ore anterioare de date de glucoză, indiferent de statul lor diabetic (grupurile PcD și non-PcD combinate pe perechi după experiența MCG)

### **2.2 Obiective Secundare**

**Obiectivul 3:** Testarea dacă o durată mai lungă a diabetului este asociată cu o precizie mai bună a predicției.

**Obiectivul 4:** Testarea dacă o experiență mai lungă cu MCG este asociată cu o precizie mai bună.

**Obiectivul 5:** Compararea preciziei când participanții prezic folosind date generice anonimizate față de propriile date MCG (comparație intra-persoană).

### **2.3 Ipoteze Formale** Această secțiune prezintă doar ipotezele — pentru metodele de testare statistică consultați Secțiunea 7\.

#### **Ipoteze Primare**

**H1 (Diferență de Grup — Diferențiator Diabet Mellitus):**

* Ipoteza nulă (H1.1): MAE mediu al persoanelor cu diabet \= MAE mediu al persoanelor fără diabet
* Ipoteza alternativă (H1.2): MAE mediu al persoanelor cu diabet ≠ MAE mediu al persoanelor fără diabet — direcția stabilită prin comparație

*Justificare:* Persoanele cu diabet au experiență de viață directă în gestionarea variabilității glicemice și pot dezvolta recunoașterea intuitivă a tiparelor prin utilizarea zilnică a MCG. MAE mai mic indică precizie de predicție mai bună.

**H2 (Diferență de Grup — Diferențiator Utilizator MCG):**

* Ipoteza nulă (H2.1): MAE mediu al persoanelor cu MCG \= MAE mediu al persoanelor fără MCG
* Ipoteza alternativă (H2.2): MAE mediu al persoanelor cu MCG ≠ MAE mediu al persoanelor fără MCG — direcția stabilită prin comparație

*Justificare:* GlucoBench \[1\] și studiile conexe oferă puncte de referință: pentru predicții la 60 de minute, modelele simple ating MAE ~12–20 mg/dL, în timp ce modelele de învățare profundă (Transformer, Gluformer) ating MAE ~11–17 mg/dL în funcție de setul de date și condiții. Ne așteptăm ca performanța umană să se încadreze undeva în acest interval. Această comparație stabilește unde se situează intuiția umană față de abordările algoritmice.

#### **Ipoteze Secundare**

**H3 (Efectul Duratei):**

* Ipoteza nulă (H3.0): Nu există nicio relație între durata diabetului și MAE (ρ \= 0)
* Ipoteza alternativă (H3.1): Există o relație negativă între durata diabetului și MAE (ρ \< 0), cu cele mai puternice efecte în primii 5 ani

O durată mai lungă a diabetului este asociată cu un număr mai mare de observații ale valorilor de glucoză, pereche cu rezultatele, ceea ce duce la un MAE mai mic (precizie mai bună). Acestea provin nu numai din citirile MCG, ci și din experiența acumulată anterior prin testarea sângelui și observarea evenimentelor cum ar fi mâncatul, injectarea, sportul și activitatea fizică. Toate aceste evenimente ar face un diabetic mai vechi un predictor mai precis al variației glicemice.

*Justificare:* Persoanele care au trăit cu diabet mai mult timp au acumulat mai multă experiență în observarea modului în care glucoza lor răspunde la mese, insulină, exerciții, stres și alți factori. Această expunere prelungită oferă mai multe oportunități de a recunoaște tipare și de a dezvolta abilități intuitive de predicție.

Mențiune importantă — durata în cazul nostru va corela numai cu timpul cu diabet, nu cu vârsta generică a participantului — ca atare, nu vom grupa utilizatorii după vârsta lor, ci mai degrabă după timpul real cu această condiție. Aceasta nu va fi verificată nici față de numărul de participanți (ex., presupunând că persoanele mai în vârstă au mai multă experiență cu starea lor, dar mai puțină participare generală la studiu — asta ar duce la incertitudine — ne pasă doar cum durata condiției reflectă precizia predicției în rândul celor care au participat)

**H4 (Efectul Experienței MCG):**

* Ipoteza nulă (H4.0): Nu există nicio relație între durata experienței MCG și MAE (ρ \= 0)
* Ipoteza alternativă (H4.1): Există o relație negativă între durata experienței MCG și MAE (ρ \< 0), cu cele mai puternice efecte în primii 2 ani

Experiența mai lungă cu MCG este asociată cu MAE mai mic (precizie mai bună).

*Justificare:* Utilizatorii MCG iau decizii zilnice bazate pe tendințele lor glicemice — ajustând dozele de insulină, programând mesele și modificând activitățile. Această buclă continuă de feedback creează un mediu de învățare natural în care utilizatorii dezvoltă abilități de recunoaștere a tiparelor prin luarea deciziilor repetate și observarea rezultatelor. Utilizatorii care poartă MCG mai mult timp au avut mai multe oportunități de a-și învăța dinamica personală a glucozei.

**H5 (Date Proprii vs. Generice):**

* Ipoteza nulă (H5.1): MAE mediu al persoanelor care folosesc date proprii \= MAE mediu al persoanelor care folosesc date generice
* Ipoteza alternativă (H5.2): MAE mediu al persoanelor care folosesc date proprii ≠ MAE mediu al persoanelor care folosesc date generice — direcția stabilită prin comparație

Participanții au MAE mai mic (precizie mai bună) când prezic propriile tipare glicemice față de date generice. Aceasta va fi măsurată permițând participanților să testeze în două moduri — fie folosind un set de date generic, fie încărcând propriile date pentru a prezice. În al doilea caz, datele vor fi anonimizate față de utilizator (nu se va afișa nicio dată — doar ora — pentru a evita reamintirea datei exacte) și vor fi reprezentate exact ca în cazul anterior grafic.

*Justificare:* Participanții sunt familiarizați cu propriile tipare glicemice, stil de viață și răspunsuri tipice la mese și activități. Această cunoaștere personală ar trebui să ofere un avantaj când prezic propriile date față de profiluri generice necunoscute.

**H6 (Uman vs. Modele de Bază):**
Formulăm ipoteza că precizia de predicție umană (MAE) se va încadra între modelele de bază simple și abordările de IA de ultimă generație.

Modelele de bază sunt cele mai simple metode posibile de predicție — nu necesită antrenament sau algoritmi complecși. Bazele noastre includ: (1) modelul de persistență — presupunând că glucoza rămâne constantă la ultima citire, (2) extrapolarea liniară — trasând o linie dreaptă prin citirile recente și extinzând-o înainte, și (3) ARIMA — o metodă statistică standard pentru datele de serii temporale.

Ne așteptăm la ierarhia de performanță: baze simple < predicții umane < modele de învățare profundă (ex., LSTM-uri, Transformer-e). Vom testa dacă oamenii depășesc semnificativ bazele și dacă învățarea profundă îi depășește semnificativ pe oameni.

Această ipoteză va fi lăsată pentru continuarea studiului în momentul când vom avea un model bine definit — În momentul de față niciun model nu este implicat în studiu.

*Justificare:* GlucoBench și studiile conexe oferă puncte de referință: pentru predicții la 60 de minute, modelele simple ating MAE ~12–20 mg/dL, în timp ce modelele de învățare profundă (Transformer, Gluformer \[2,7,8\]) ating MAE ~11–17 mg/dL în funcție de setul de date și condiții. Ne așteptăm ca performanța umană să se încadreze undeva în acest interval. Această comparație stabilește unde se situează intuiția umană față de abordările algoritmice.

---

## **3\. Designul Studiului**

### **3.1 Tipul Studiului**

**Design:** Observațional, transversal cu sarcini repetate de predicție. Pentru mai multe detalii consultați Secțiunea 4.2  
**Colectarea datelor:** Platformă online bazată pe web  
**Urmărire:** Niciuna (participare cu o singură sesiune)

### **3.2 Clasificare Reglementară**

Acest studiu este un **studiu non-intervențional, observațional** care nu necesită supraveghere medicală sau reglementare a dispozitivelor medicale.

#### **3.2.1 Doar Date Istorice**

* Toate datele MCG afișate participanților sunt **date istorice, pre-înregistrate** — fie dintr-un set de date anonim grupat, fie din propriile fișiere MCG exportate anterior ale participantului
* **Nu se efectuează nicio monitorizare glicemică în timp real** pe durata studiului
* **Nicio conexiune la dispozitive MCG active** — participanții nu trebuie să poarte sau să folosească niciun echipament de monitorizare pentru acest studiu
* Studiul analizează precizia de predicție pe segmente de date trecute, nu pe starea curentă de sănătate

#### **3.2.2 Nicio Decizie Medicală sau Diagnostic**

Acest studiu în mod explicit **NU**:

* Oferă niciun diagnostic sau prognostic medical
* Face recomandări terapeutice sau de tratament
* Influențează decizii clinice sau planuri de tratament medical
* Oferă sfaturi sau îndrumare personalizată de sănătate
* Generează rezultate destinate utilizării clinice

**Rezultatele sunt pur în scopuri de referință a cercetării** — scorurile de precizie indică doar performanța de predicție și nu au semnificație diagnostică sau terapeutică.

#### **3.2.3 Nicio Supraveghere Medicală Necesară**

Supravegherea medicală nu este necesară pentru acest studiu deoarece:

* **Nu se administrează nicio intervenție medicală**
* **Nu se efectuează niciun test diagnostic**
* **Niciun rezultat de sănătate** nu depinde de participare sau rezultate
* **Nicio decizie de tratament** nu este informată de studiu
* Activitatea este echivalentă cu **completarea unei sarcini cognitive online sau a unui sondaj**

### **3.3 Populația Studiului**

#### **Criterii de Includere**

**Populație Generală (Ambele Grupuri):**

* Vârsta 18 ani sau mai mare
* Capabil să furnizeze consimțământ informat
* Acces la internet și literație de bază computer/mobil
* Dispus să completeze sarcini de predicție

**Suplimentar pentru Persoanele cu Diabet (PcD):**

* Diagnostic de diabet auto-raportat (Tip 1, Tip 2 sau alt tip)
* Utilizare curentă sau trecută a MCG (orice dispozitiv)

---

## **4\. Fluxul de Lucru al Participantului și Proceduri**

### **4.1 Strategia de Recrutare**

**Canale de Recrutare:**

1. Anunțuri pe rețelele sociale (Twitter/X, LinkedIn, grupuri Facebook diabet)
2. Organizații de pacienți cu diabet și grupuri de advocacy
3. Rețele ale consiliului consultativ științific
4. Canale comunitare (site-ul proiectului, Telegram)
5. Conferințe academice (prezentări la întâlniri de longevitate/diabet)

Materialele specifice de recrutare vor fi dezvoltate după obținerea aprobării etice.

### **4.2 Procedurile Studiului**

#### **Faza 1: Consimțământ și Informații de Bază**

Participanții accesează aplicația web Sugar-Sugar printr-o URL (adresă web) și completează:

**1\. Consimțământ Informat Electronic**

* Fișă de informații despre studiu
* Informații de protecție a datelor (conform RGPD)
* Consimțământ prin bifarea casetei pentru participarea la studiu și prelucrarea datelor
* Consimțăminte opționale pentru: încărcarea propriilor date MCG, recontact viitor în cazul în care utilizatorul dorește să afle mai multe detalii despre rezultatele studiului la finalizare, comunicări promoționale

**2\. Chestionar de Bază**
**(va fi completat de participant, cu exactitate, pe baza cunoștințelor sale)**

* Email (pentru identificare unică; hash-uit pentru anonimizare)
* Vârstă (ani)
* Sex/gen
* Țara de reședință
* Status diabetic (Da/Nu)
  * Dacă Da: Tipul de diabet, ani de la diagnostic
* Utilizare MCG (Da/Nu)
  * Dacă Da: ani de utilizare
* Greutate opțională (kg) și înălțime (cm)

**Notă de Protecție a Datelor:** Email-urile sunt hash-uite imediat la trimitere pentru identificare unică fără stocarea identificatorilor personali. Participanții se pot înscrie separat pentru comunicații de recontact.

#### **Faza 2: Încercări de Practică**

2 încercări opționale de practică pentru familiarizarea participanților cu interfața (utilizatorii au opțiunea de a nu trimite pentru primele 2 încercări). Datele din încercările de practică sunt excluse din analiză.

#### **Faza 3: Sarcina de Predicție cu Date Generice**

**Structura Sarcinii:**

* **Numărul de încercări:** 6–12 segmente de predicție pe participant
* **Fiecare segment:** Participantul desenează 12 puncte de predicție (intervale de 5 minute pe 60 de minute)
* **Fereastra de context afișată:** 3 ore de date MCG (36 de puncte la rezoluție de 5 minute)
* **Sursa de date:** Date MCG de-identificate din setul de date organizat al studiului

Segmentele sunt selectate pentru a oferi un mix echilibrat de diferite ore ale zilei, tendințe glicemice și contexte de evenimente. Ordinea este randomizată între participanți.

**Funcționalitățile Interfeței:**

* Grafic interactiv cu grilă de timp de 5 minute
* Participanții fac clic/desenează pentru a crea curba de predicție
* Afișarea marcatorilor de evenimente (marcaje temporale masă/insulină/exercițiu)
* Predicții editabile înainte de trimitere

*Mai jos este interfața principală pentru utilizator după completarea formularelor de date și consimțământ.*
*\-linia albastră și punctul reprezintă datele istorice trasate pentru test*

*\-linia roșie reprezintă datele prezise de utilizator*

*\-există opțiunea de a schimba unitățile de măsurare — în funcție de cele cu care participantul este cel mai obișnuit*

*\-există informații despre care rundă din cele 12 este aceasta*

*\-utilizatorul are două opțiuni în orice etapă pe durata testului — trimite sau pur și simplu iese*

*După fiecare rundă utilizatorul primește un ecran după cum urmează:*

*\-există informații despre care rundă a fost*

*\-există compararea datelor — linia albastră este afișată complet*

*\-există rezultatele editării numerice*

*\-precum și rezultatul statistic pentru această rundă*

*\-utilizatorul are din nou opțiunea de a ieși sau de a continua la runda următoare*

*La sfârșitul încercării (max. 12 runde) utilizatorul primește acest ecran unde toate datele sunt compilate pentru întreaga încercare. Mai jos sunt două exemple — unul în care utilizatorul a făcut o singură rundă și unul în care utilizatorul a făcut mai multe runde. Cum se poate vedea, conține:*
*\-metrici de precizie*

*\-unitățile în care a fost rulat*

*\-valori per fiecare rundă*

*\-clasament![][image1]*

![][image2]

#### **Faza 4: Încărcarea Datelor Proprii și Sarcina (Opțional)**

**Eligibilitate:** Participanți care au indicat disponibilitatea de a încărca date MCG

**Procesul de Încărcare a Datelor:**

1. Încărcarea fișierului de export MCG (format CSV sau JSON de la dispozitivele suportate, sau export Nightscout)
2. Verificări automate de calitate (minimum 5 zile consecutive, validarea datelor)
3. Prelucrarea datelor în care convertim din formatul dispozitivului suportat în formatul uniform pe care îl folosim pentru ieșirea datelor
4. Pseudonimizarea datelor și stocarea securizată

**Sarcina de Predicție cu Date Proprii:**

* 6–12 segmente eșantionate din propriile date MCG ale participantului
* Segmente anonimizate (nicio dată/oră afișată)
* Permite comparație intra-persoană a preciziei pe date proprii vs. generice

#### **Faza 5: Finalizare și Feedback**

**Scurtă Reamintire de Siguranță (Doar la Prima Vedere):**

La prima participare, se afișează o scurtă notificare înainte de rezultate:

**Numai în scopuri de cercetare** — Aceste scoruri măsoară performanța recunoașterii tiparelor, nu capacitatea medicală. Continuați să urmați îndrumarea furnizorului dumneavoastră de asistență medicală.

Această notificare este afișată o dată per utilizator; utilizatorii care revin văd rezultatele direct.

**Afișarea Rezultatelor (afișată implicit):**

* Rezumatul preciziei personale (MAE în mg/dL)
* Rangul percentil comparat cu alți participanți pe baza stocării curente a bazei de date la momentul participării utilizatorului. Pe scurt, avem un depozit separat de clasament — avem nevoie doar de un ID de utilizator anonimizat și rang — de acolo aflați numărul total de participanți și performanța lor
* Comparație vizuală a predicțiilor vs. traiectoriile reale
* Opțiunea „Omite și finalizează" disponibilă dar nu proeminentă

**Card de Rezultat Partajabil (Conținut Controlat de Utilizator):**

Utilizatorii pot crea și partaja un card de rezultat cu conținut personalizabil:

* **Inclus întotdeauna:** „Am participat la studiul de predicție a glicemiei Sugar-Sugar"
* **Utilizatorul poate alege să includă:** percentila de precizie, scorul MAE, numărul de segmente completate, comparația cu alți participanți
* **Utilizatorul controlează ce să partajeze** — gamificarea este o caracteristică cheie de engagement
* Utilizatorii sunt informați că partajarea poate dezvălui interesul lor pentru subiecte de glucoză/diabet

**Fără Sfaturi Medicale:** Rezultatele sunt prezentate ca metrici de performanță de joc/cercetare, nu evaluări de sănătate.

---

## **5\. Colectarea și Gestionarea Datelor**

### **5.1 Categoriile de Date**

**Date de Bază:** Date demografice și utilizator cum ar fi:

* Email (pentru identificare unică; hash-uit pentru anonimizare)
* Vârstă (ani)
* Sex/gen
* Țara de reședință
* Status diabetic (Da/Nu)
  * Dacă Da: Tipul de diabet, ani de la diagnostic
* Utilizare MCG (Da/Nu)
  * Dacă Da: ani de utilizare
* Greutate opțională (kg) și înălțime (cm)

**Preferințele de Consimțământ:**

* pentru participarea la studiu și prelucrarea datelor
* pentru: încărcarea propriilor date MCG, recontact viitor în cazul în care utilizatorul dorește să afle mai multe detalii despre rezultatele studiului la finalizare, comunicări promoționale

**Date Grafice:**

6–12 segmente pe participant, fiecare conținând

**Date de Predicție:** 12 puncte de predicție (incluzând valoarea glicemică și marcajul temporal),

**Date de Adevăr Teren:** 12 valori reale MCG pentru evaluare (neafișate participanților până după trimitere, incluzând valoarea glicemică și marcajul temporal)

**Date de Rezultat:**

Valori MAE, MSI, RSME, MAPE

### **5.2 Protecția Datelor și Conformitatea cu RGPD**

#### **5.2.1 Operator de Date, Procesator și Arhitectură**

**Operator de Date:** Institutul für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA) la Universitätsmedizin Rostock (UMR) este operatorul de date pentru acest studiu.

**Implicațiile acestui aranjament:**

* IBIMA/UMR poartă responsabilitatea deplină pentru conformitatea cu RGPD și drepturile participanților
* Toate cererile persoanelor vizate (acces, ștergere, retragere) sunt gestionate de echipa de studiu la IBIMA

**Procesator de Date:** HEALES (Healthy Life Extension Society) va opera aplicația web Sugar-Sugar ca procesator de date în baza unui Acord de Prelucrare a Datelor (APD) cu UMR.

**Arhitectura Tehnică: Modelul Pull**

Studiul utilizează o arhitectură „model pull" axată pe securitate:

\[Participant\] → \[App Sugar-Sugar (servere HEALES)\] ← \[Colector de Date UMR\]

                         ↓                                    ↑

                   \[Cache Temporar\] ──────────────────→ \[Baza de Date de Cercetare (UMR)\]

**Cum funcționează:**

1. Participantul interacționează cu aplicația Sugar-Sugar găzduită pe serverele HEALES
2. Datele sesiunii completate sunt criptate și temporar stocate în cache pe serverele HEALES
3. Sistemul de colectare a datelor UMR **extrage** datele de la HEALES periodic (la fiecare 2 ore) și le decriptează
4. După un transfer reușit, cache-ul de pe HEALES este șters
5. Toate datele persistente de cercetare sunt stocate exclusiv pe serverele UMR
6. Nu există nicio capacitate de decriptare pe partea HEALES, securizând cache-ul temporar

**Avantajele de securitate:**

* Baza de date de cercetare UMR nu are acces de intrare din sisteme externe
* HEALES nu poate „împinge" date către UMR — UMR inițiază toate transferurile de date, fluxul de date este unidirecțional prin design
* Stocarea temporară a datelor criptate în cache fără chei de decriptare pe partea HEALES atenuează riscurile de acces neautorizat la cache
* Suprafață de atac redusă pe infrastructura datelor de cercetare
* Separare clară între stratul de aplicație (HEALES) și stocarea datelor (UMR)

**Cache-ul temporar pe serverele HEALES:**

* Conține doar datele sesiunii completate în așteptarea transferului, în formă criptată
* Retenție maximă: 7 zile (șters automat dacă extragerea eșuează)
* Criptat în repaus
* Fără acces direct la cache, cu excepția sistemului automatizat de extragere
* Cache-ul este procesare tranzitorie, nu stocare persistentă

**Acordul de Prelucrare a Datelor (APD) specifică:**

* HEALES prelucrează datele numai conform instrucțiunilor UMR
* Fără stocare persistentă a datelor de cercetare pe serverele HEALES
* Fără stocare necriptată a datelor de cercetare pe serverele HEALES
* Cache-ul este șters imediat după extragerea reușită la UMR
* Ștergerea automată a cache-ului după 7 zile indiferent de statusul extragerii
* Măsuri de securitate pentru cache-ul temporar (criptare, controale de acces)
* Drepturi de audit pentru UMR
* Accesul personalului HEALES limitat doar la întreținerea tehnică

**Fără alți procesatori externi:**

* Niciun serviciu extern de analiză, CDN sau terți nu prelucrează datele participanților
* Membrii comunității HEALES (alții decât echipa de studiu listată) nu au acces la datele participanților

#### **5.2.2 Identificare și Pseudonimizare**

**Ce se stochează și de ce:**

1. **Adresă email (text clar, criptat în repaus):** Stocat separat de datele de cercetare doar în două scopuri:
   * Activarea cererilor de retragere (participantul ne contactează, localizăm și ștergem datele sale)
   * Recontact opțional pentru rezultatele studiului (numai dacă participantul a optat pentru aceasta)
2. **ID Studiu:** Identificator alfanumeric aleator atribuit prin hash-uire (ex., f5afc4cf-9881-467d-88a1-325eb9558baa) atribuit la înregistrare
3. **Tabel de legătură:** Un fișier criptat separat care mapează ID Studiu ↔ Adresă email
   * Stocat pe unitate criptată separată de datele de cercetare
   * Accesul restricționat la IP (Anton Kulaga) și co-IP numai
   * Scop: Activarea retragerii și recontactului opțional
4. **Date de cercetare:** Toate datele de predicție, încărcările MCG, răspunsurile la chestionare stocate pseudonimizate numai cu ID Studiu (fără email, fără nume)

**Clarificarea Hash-ului:** Nu ne bazăm pe hash-uirea email-ului pentru pseudonimizare. Hash-ul este folosit numai pentru detectarea duplicatelor în timpul înregistrării (prevenind înregistrarea aceleiași persoane de două ori). Tabelul de legătură conține email-ul real în scopuri de retragere/recontact.

#### **5.2.3 Politica de Retenție și Ștergere**

| Tipul de Date | Perioada de Retenție | Declanșatorul Ștergerii |
| :---- | :---- | :---- |
| Adrese email | Până la finalizarea studiului + 12 luni | Tabelul de legătură distrus după perioada de grație |
| Tabel de legătură | Finalizarea studiului + 12 luni | Distrus, randând datele complet anonime |
| Date de cercetare (pseudonimizate) | 10 ani conform standardelor de cercetare germane | N/A — reținute pentru reproductibilitate |
| Fișiere MCG încărcate | Procesate imediat, fișierele brute șterse în 30 de zile | Automat după extragerea segmentelor |

#### **5.2.4 Limitările Retragerii (Important)**

**Retragerea este posibilă oricând PÂNĂ când tabelul de legătură este distrus** (aproximativ 12 luni după finalizarea studiului). După acest punct:

* Datele de cercetare devin complet anonime (nicio reidentificare posibilă)
* Cererile de retragere nu pot fi îndeplinite deoarece nu putem identifica ce date aparțin solicitantului
* Această limitare este indicată clar în formularul de consimțământ

**Procesul de retragere:**

1. Participantul trimite email coordonatorului studiului solicitând retragerea
2. Localizăm ID-ul lor de Studiu prin tabelul de legătură
3. Toate datele de cercetare asociate cu acel ID de Studiu sunt șterse permanent
4. Confirmarea este trimisă participantului

#### **5.2.5 Transferurile Transfrontaliere de Date**

**Nicio dată nu iese din Uniunea Europeană.**

* **Baza de date de cercetare UMR:** Situată în Germania (UE)
* **Contul cloud gestionat de HEALES:** Situat în UE (numai cache temporar, max. 24 de ore)
* Niciun serviciu terț nu transferă date în afara UE
* Niciun CDN, analiză externă sau servicii cloud cu centre de date non-UE
* Comunicările prin email folosesc furnizori standard de email cu sediul în UE

Participanții din afara UE pot participa, dar datele lor sunt prelucrate și stocate exclusiv în UE sub protecțiile RGPD.

#### **5.2.6 Securitatea Stocării Datelor**

* **Locația bazei de date de cercetare UMR:** Germania (UE)
* **Locația cache-ului temporar HEALES:** UE
* **Criptare în tranzit:** TLS 1.3 (atât app-la-utilizator cât și extragerea UMR-la-HEALES)
* **Criptare în repaus:** AES-256 (atât baza de date UMR cât și cache-ul HEALES)
* **Controale de acces:** Bazate pe roluri; date de cercetare accesibile echipei de studiu; tabel de legătură accesibil numai IP-urilor
* **Backup:** Backup-uri zilnice criptate în UE (numai UMR; cache-ul HEALES este tranzitoriu)
* **Jurnalizare audit:** Toate accesările datelor sunt înregistrate

---

## **6\. Măsuri de Rezultat și Metrici de Precizie**

### **6.1 Metrici Primare**

Folosim metrici standard din literatura de predicție a glucozei \[1,9,10\], permițând compararea directă cu referințele modelelor ML publicate (ex., GlucoBench — pentru mai multe detalii consultați secțiunea Referințe).

**Eroarea Absolută Medie (MAE):** Media diferenței absolute dintre valorile glicemice prezise și cele reale (în mg/dL). Valorile mai mici indică o precizie mai bună.

 MAE \= (1 / n) × Σ |prezis − real|

* Măsoară dimensiunea tipică a erorilor de predicție
* Toate erorile sunt ponderate egal
* Aceleași unități ca variabila țintă

**Rădăcina Erorii Pătratice Medii (RMSE):** Rădăcina pătrată a diferențelor pătratice medii. Penalizează erorile mai mari mai puternic decât MAE. De asemenea raportată în mg/dL.

 RMSE \= sqrt(MSE)

* Aceeași unitate ca variabila țintă
* Penalizează erorile mari ca MSE
* Mai ușor de interpretat decât MSE

**Eroarea Pătratica Medie (MSE):** Media diferențelor pătratice dintre valorile prezise și cele reale.

 MSE \= (1 / n) × Σ (prezis − real)²

* Penalizează erorile mari mai puternic
* Sensibil la valorile extreme
* Unitățile sunt pătratice, făcând interpretarea directă mai dificilă

**Eroarea Absolută Procentuală Medie (MAPE):** Eroarea absolută medie exprimată ca procent din valoarea reală.

 MAPE \= (100 / n) × Σ |(prezis − real) / real|

* Măsoară eroarea relativă
* Independentă de scară
* Poate fi înșelătoare când valorile reale sunt aproape de zero

Aceste metrici sunt calculate:

* Per încercare (pe cele 12 puncte de predicție)
* Per participant (mediat pe 6–12 încercări ale lor)
* Per grup (pentru comparații de grup)

### **6.2 Comparații cu Modelele de Bază**

Pentru a contextualiza performanța umană, comparăm cu modele de bază simple folosind aceleași segmente de test:

* **Model de persistență:** Prezicerea că glucoza rămâne constantă la ultima valoare observată
* **Extrapolare liniară:** Proiectarea tendinței din ultimele 30 de minute înainte

Aceasta va fi realizată după colectarea datelor pentru a stabili un punct de pornire pentru partea viitoare a studiului unde vom integra modele ML. Nu va afecta colectarea datelor în această etapă a studiului. Pentru mai multe detalii consultați H6.

---

## **7\. Planul de Analiză Statistică**

### **7.1 Prezentare Generală**

Studiul colectează **mai multe măsurători per participant** (6–12 segmente de predicție fiecare, cu 12 puncte per segment). Analiza ține cont de această structură de măsurători repetate. Oferă o privire mai precisă asupra abilității de predicție a participantului decât o singură măsurătoare.

### **7.2 Populațiile de Analiză**

* **Analiza primară:** Toți participanții care completează cel puțin 6 segmente de date generice analizabile
* **Analiza datelor proprii:** Participanți care completează cel puțin 6 segmente de date proprii
  Numărul de segmente de date propus se datorează variabilității așteptate în metricile de precizie (MAE/RMSE). Pe baza datelor GlucoBench, abaterea standard pentru precizia predicției este de aproximativ 0,18–0,22 pe o scală 0–1. Dacă ar fi doar 2–3 măsurători per persoană, estimarea abilității lor ar avea intervale de încredere mari.

## **7.3 Analize Primare**

### **H1 (Diferență de Grup — Statusul Diabetic)**

**Obiectiv**: Compararea preciziei de predicție între persoanele cu diabet (PcD) și persoanele fără diabet (non-PcD).

**Rezumatul Datelor**: Fiecare participant va prezice valorile de glucoză pentru mai multe puncte temporale pe diferite prezentări ale urmelor de glucoză. Vom calcula o valoare MAE per participant prin medierea erorilor lor de predicție pe toate predicțiile lor. Aceasta ne oferă un scor de precizie rezumat per persoană.

**Metoda Statistică**:

1. **Verificarea Normalității**: Mai întâi vom testa dacă valorile MAE sunt distribuite normal în cadrul fiecărui grup folosind testul Shapiro-Wilk (p > 0,05 indică distribuție normală).
2. **Compararea Grupurilor**:
   * **Dacă datele sunt distribuite normal** (Shapiro-Wilk p > 0,05): Vom folosi un **test t cu eșantioane independente**. Acest test compară MAE mediu între două grupuri ținând cont de variabilitatea din cadrul fiecărui grup și dimensiunile eșantioanelor. Testul t calculează dacă diferența observată în medii este mai mare decât ar fi de așteptat numai prin șansă.
   * **Dacă datele sunt non-normale** (Shapiro-Wilk p < 0,05): Vom folosi **testul U Mann-Whitney**. Acest test non-parametric compară grupurile clasificând toate scorurile MAE de la cel mai bun la cel mai rău (indiferent de grup), apoi testând dacă un grup tinde să aibă ranguri mai bune decât celălalt. Această abordare este robustă față de valorile extreme și distribuțiile asimetrice.
3. **Nivelul de Semnificație**: α \= 0,05 (bilateral)
4. **Dimensiunea Efectului**: Vom raporta Cohen's d (pentru testul t) sau corelația biseriala a rangurilor (pentru Mann-Whitney) pentru a cuantifica magnitudinea diferenței.

**De ce această abordare**: Folosim statistici de rezumat per persoană (un MAE per participant) în loc să analizăm mii de predicții individuale deoarece predicțiile individuale de la aceeași persoană nu sunt independente — sunt influențate de strategia consistentă de predicție a acelei persoane. Rezumarea la o valoare per persoană asigură că testele noastre statistice satisfac presupunerea observațiilor independente.

---

### **H2 (Diferență de Grup — Experiența MCG)**

**Obiectiv**: Compararea preciziei de predicție între persoanele care folosesc în prezent MCG și persoanele care nu au folosit niciodată MCG.

**Rezumatul Datelor**: La fel ca H1 — o valoare MAE per participant, mediat pe toate predicțiile lor.

**Metoda Statistică**: Abordare identică cu H1:

1. Testul Shapiro-Wilk pentru evaluarea normalității
2. Testul t cu eșantioane independente (dacă este normal) sau testul U Mann-Whitney (dacă este non-normal)
3. Nivelul de semnificație α \= 0,05 (bilateral)
4. Raportarea dimensiunii de efect adecvate

**Justificare**: Aceeași logică ca H1 — comparăm două grupuri independente pe o singură măsurătoare de precizie per persoană.

---

## **7.4 Analize Secundare**

### **H3 (Efectul Duratei — Diabet)**

**Obiectiv**: Testarea dacă o durată mai lungă a diabetului este asociată cu o precizie mai bună a predicției.

**Rezumatul Datelor**: Pentru fiecare participant cu diabet, avem:

* **Variabila predictor**: Durata diabetului în ani (variabilă continuă)
* **Variabila de rezultat**: MAE (o valoare per persoană, calculată ca în H1)

**Metoda Statistică**:

1. **Verificarea Normalității și Liniarității**:
   * Crearea unui grafic de dispersie al duratei diabetului (axa x) vs. MAE (axa y) pentru a inspecta vizual relația
   * Folosirea testului Shapiro-Wilk pentru a verifica dacă valorile MAE sunt distribuite normal
   * Examinarea graficului de dispersie pentru tipare liniare vs. curbate
2. **Analiza Corelației**:
   * **Dacă MAE este distribuit normal ȘI relația pare liniară**: Folosirea **coeficientului de corelație Pearson (r)**. Acesta măsoară forța și direcția unei relații liniare între două variabile continue. Valorile variază de la -1 (relație negativă perfectă) la +1 (relație pozitivă perfectă). Așteptăm corelație negativă (durată mai lungă → MAE mai mic).
   * **Dacă MAE este non-normal SAU relația pare non-liniară**: Folosirea **corelației de rang Spearman (ρ)**. Aceasta funcționează ca Pearson, dar folosește ranguri în loc de valori reale, făcând-o robustă față de valorile extreme și capabilă să detecteze relații monotone (constant crescătoare sau descrescătoare) chiar dacă nu sunt perfect liniare.
3. **Nivelul de Semnificație**: α \= 0,05 (bilateral)
4. **Analiza Exploratorie**: Deoarece anticipăm că relația poate atinge un platou (îmbunătățire mare în primii ani, îmbunătățire minimă după 5+ ani), vom face suplimentar:
   * Ajustarea unui model logaritmic: MAE \= β₀ \+ β₁·log(durată \+ 1)
   * Compararea ajustărilor liniare vs. logaritmice folosind valorile R²
   * Crearea unei vizualizări care arată cum se schimbă MAE pe categorii de durată (<1 an, 1–5 ani, 5–10 ani, >10 ani)

**De ce această abordare**: Analiza corelației este adecvată când se examinează relația dintre două variabile continue. Folosim Spearman ca backup deoarece curbele de învățare arată adesea randamente descrescătoare (tipare non-liniare), iar Spearman poate detecta aceste relații chiar și când nu sunt linii perfect drepte.

---

### **H4 (Efectul Experienței MCG)**

**Obiectiv**: Testarea dacă o experiență MCG mai lungă este asociată cu o precizie mai bună a predicției în rândul utilizatorilor MCG.

**Rezumatul Datelor**:

* **Variabila predictor**: Experiența MCG în ani (variabilă continuă, numai pentru utilizatorii MCG)
* **Variabila de rezultat**: MAE (o valoare per utilizator MCG)

**Metoda Statistică**: Abordare identică cu H3:

1. Vizualizarea graficului de dispersie și verificarea normalității (Shapiro-Wilk)
2. Corelația Pearson (dacă normală/liniară) sau corelația Spearman (dacă non-normală/non-liniară)
3. Modelarea logaritmică exploratorie pentru testarea efectelor de platou
4. Nivelul de semnificație α \= 0,05

**Justificare**: Aceeași logică ca H3 — așteptăm ca utilizatorii MCG să arate o îmbunătățire rapidă inițial, cu un platou de învățare după ce au interiorizat tiparele comune de glucoză.

---

### **H5 (Date Proprii vs. Date Generice)**

**Obiectiv**: Testarea dacă participanții prezic mai precis când văd propriile date de glucoză față de date generice anonimizate.

**Rezumatul Datelor**: Aceasta este o **comparație intra-persoană**. Participanții care completează ambele condiții vor avea:

* **MAE date proprii**: Eroarea medie pe toate predicțiile de pe urmele lor personale de glucoză
* **MAE date generice**: Eroarea medie pe toate predicțiile de pe urmele anonimizate
* **Scorul de diferență**: MAE generic − MAE propriu (valorile pozitive indică performanță mai bună pe date proprii)

**Metoda Statistică**:

1. **De ce analiza pereche**: Folosim teste „pereche" deoarece avem **două măsurători de la aceeași persoană** (precizie pe date proprii vs. precizie pe date generice). Aceasta este fundamental diferit de H1–H2 unde comparăm persoane diferite. Testele pereche țin cont de faptul că aceeași persoană apare în ambele condiții, controlând factorii specifici persoanei cum ar fi abilitatea generală de predicție, atenția, motivația etc.
2. **Verificarea Normalității**: Testul Shapiro-Wilk pe **scorurile de diferență** (nu pe valorile brute MAE)
3. **Comparația**:
   * **Dacă scorurile de diferență sunt distribuite normal**: Folosirea **testului t cu eșantioane pereche**. Acesta testează dacă diferența medie între condiții este semnificativ diferită de zero, ținând cont de corelația intra-persoană.
   * **Dacă scorurile de diferență sunt non-normale**: Folosirea **testului Wilcoxon cu ranguri cu semn**. Acesta este echivalentul non-parametric al testului t pereche — clasifică diferențele absolute și testează dacă diferențele pozitive (performanță mai bună pe date proprii) sunt mai frecvente decât cele negative.
4. **Nivelul de Semnificație**: α \= 0,05 (bilateral)
5. **Dimensiunea Efectului**: Raportarea Cohen's d pentru design pereche

**De ce această abordare**: Testele pereche sunt mai puternice decât testele independente deoarece elimină variabilitatea datorată diferențelor individuale. Dacă Persoana A este pur și simplu în mod natural mai bună la sarcinile de predicție decât Persoana B, asta nu contează — ne pasă doar dacă fiecare persoană performează diferit pe cele două tipuri de date.

---

### **H6 (Uman vs. Modele de Bază)**

**Notă**: Această ipoteză este amânată pentru lucrări viitoare când modelele de bază sunt implementate. Când se analizează, vom folosi abordări similare de comparare pereche, comparând MAE-ul fiecărui participant cu MAE-ul realizat de modelele computaționale pe aceleași urme de glucoză.

---

## **Tabelul Rezumat al Metodelor Statistice**

| Ipoteza | Tipul Comparației | Testul Primar | Testul Alternativ | Când să Folosești Alternativa |
| ----- | ----- | ----- | ----- | ----- |
| H1 | Grupuri independente (PcD vs. non-PcD) | Test t independent | U Mann-Whitney | Shapiro-Wilk p < 0,05 |
| H2 | Grupuri independente (MCG vs. fără-MCG) | Test t independent | U Mann-Whitney | Shapiro-Wilk p < 0,05 |
| H3 | Corelație (durată vs. MAE) | r Pearson | ρ Spearman | Non-normal sau non-liniar |
| H4 | Corelație (experiență MCG vs. MAE) | r Pearson | ρ Spearman | Non-normal sau non-liniar |
| H5 | Comparație pereche (proprii vs. generice) | Test t pereche | Ranguri cu semn Wilcoxon | Scoruri de diferență non-normale |

**Toate testele folosesc nivelul de semnificație α \= 0,05. Dimensiunile efectului vor fi raportate pentru toate analizele.**

### **7.5 Așteptările Dimensiunii Efectului**

Bazat pe GlucoBench și literatura conexă de predicție a glucozei pentru **orizonturi de predicție de 60 de minute**:

**Performanța Modelelor din Referințele Publicate (MAE în mg/dL):**

Performanța variază considerabil pe seturi de date și condiții. Intervale reprezentative din literatură:

* **Regresie liniară / ARIMA \[7,8\]:** MAE ~12–20 mg/dL (date ID GlucoBench), RMSE ~23–27 mg/dL (alte studii)
* **Învățare profundă (Transformer, Gluformer \[2,7,8\]):** MAE ~11–17 mg/dL în funcție de set de date
* **Modele personalizate de ultimă generație:** MAE ~15–17 mg/dL (abordări recente bazate pe LLM \[3\])

Notă: Valorile variază substanțial în funcție de dimensiunea setului de date, caracteristicile populației și dacă evaluarea este in-distribution (ID) vs. out-of-distribution (OD). GlucoBench raportează că modelele de învățare profundă generalizează considerabil mai bine decât bazele simple pe datele OD.

**Dimensiunile Efectului Așteptate pentru Ipotezele Studiului:**

Dată această variabilitate, folosim presupuneri conservatoare:

* **H1 (PcD vs. non-DZ):** Presupunând SD ~8–12 mg/dL în rândul participanților și o diferență semnificativă de ~3–5 mg/dL între grupuri, aceasta reprezintă Cohen's d ~0,3–0,5 (efect mic până la mediu).
* **H2 (Uman vs. baze):** Decalajul dintre modelele simple și avansate este tipic ~5–10 mg/dL. Așteptăm ca oamenii să se încadreze în acest interval. Pentru mai multe detalii despre distribuția umană așteptată consultați dimensiunea eșantionului.
* **H3, H4 (Corelații durată/MCG):** Așteptăm corelații de r ~0,15–0,30 între experiență și precizie, bazate pe presupunerile curbei de învățare.
* **H5 (Proprii vs. generice):** Așteptăm o îmbunătățire de ~2–4 mg/dL când prezic date proprii (efect pereche). Aceasta este importantă deoarece acoperă diferența așteptată dintre valoarea reală de glucoză din sânge și valoarea estimată de glucoză (VEG) pe care o furnizează MCG-urile.

**Avertisment important:** Aceste estimări ale dimensiunii efectului sunt derivate din variabilitatea inter-model în referințele ML, nu din studii anterioare de predicție umană (care nu există). Distribuția reală a performanței umane este necunoscută și va fi stabilită de acest studiu. Subliniem că aceste cifre sunt estimate pe baza articolelor menționate în secțiunea de referințe, în special articolul GlucoBench.

---

## **8\. Dimensiunea Eșantionului**

### **8.1 Înscrierea Țintă**

**Țintă:** Aproximativ 200 de participanți total

* Aproximativ 100 de persoane cu diabet (PcD)
* Aproximativ 100 de persoane fără diabet (non-DZ)
* Printre PcD: obiectiv pentru 70–90 de participanți care încarcă date proprii

**Minim viabil:** Aproximativ 150 de participanți (75 pe grup)

### **8.2 Justificare**

Obiectivele de dimensionare a eșantionului sunt bazate pe estimările dimensiunii efectului derivate din referințele modelelor ML, cu recunoașterea incertitudinii:

**Gestionarea măsurătorilor repetate:** Fiecare participant face 6–12 predicții, ceea ce înseamnă că datele noastre au o structură de măsurători repetate. Luăm în considerare acest lucru în două moduri: (1) analizele noastre primare vor folosi medii per persoană (o valoare MAE per participant), care satisface presupunerea de independență pentru testele t și corelații, și (2) pentru analize mai detaliate, vom folosi modele cu efecte mixte care modelează explicit corelația dintre măsurătorile repetate ale aceleiași persoane.

**Diferențe semnificative:** Considerăm o diferență de 3–4 mg/dL în MAE ca semnificativă clinic deoarece reprezintă aproximativ jumătate din eroarea de măsurare a dispozitivelor MCG în sine (care au o diferență relativă absolută medie de 8–10% față de glucoza din sânge, sau aproximativ 7–9 mg/dL la nivelurile tipice de glucoză). O corelație de r=0,25 explică aproximativ 6% din varianță, ceea ce, deși modest, ar merita înțeles pentru designul viitor al intervențiilor.

**H1 (Comparația grupului diabet vs. non-diabet):** Pentru a detecta o diferență de 4 mg/dL în eroarea absolută medie (MAE) între grupuri, presupunând o abatere standard de 10 mg/dL (Cohen's d ≈ 0,4), avem nevoie de 80–100 de participanți pe grup. Am folosit un test unilateral cu α=0,025 aici deoarece literatura anterioară sugerează că persoanele cu diabet ar putea prezice mai bine, deși direcția nu este certă. Această ajustare Bonferroni ține cont de testarea a două comparații primare (H1 și H2).

**H2 (Utilizatori MCG vs. non-utilizatori):** Aceeași calculare ca H1 — așteptăm dimensiuni similare ale efectului și avem nevoie de aproximativ 80–100 pe grup. Natura pereche a unor comparații în cadrul participanților (unde aceeași persoană face mai multe predicții) ne oferă de fapt putere statistică suplimentară, dar suntem conservatori în estimările noastre.

**H3 și H4 (Analize de corelație):** Pentru a detecta o corelație de r=0,25 între durata experienței și precizia predicției cu 80% putere, avem nevoie de 100–120 de participanți. Intervalul (100–120) reflectă incertitudinea în forța reală a corelației — dacă corelația reală este mai slabă decât r=0,25, ar trebui să avem capătul superior al acestui interval. Am ales r=0,25 ca țintă deoarece corelațiile mai mici ar fi de importanță practică limitată.

**H5 (Comparația date proprii vs. date generice):** Aceasta este o comparație intra-persoană, deci avem mai multă putere statistică. Pentru a detecta o diferență de 3 mg/dL în măsurătorile pereche (presupunând un SD pereche de 6 mg/dL), avem nevoie de aproximativ 70 de participanți care completează ambele sarcini. Designul pereche este mai eficient deoarece fiecare persoană servește ca propriul control.

**Avertisment Important:** Incertitudinea Dimensiunii Eșantionului

Calculele noastre de dimensionare a eșantionului sunt bazate pe performanța modelelor ML, dar comportamentul uman poate diferi:

De ce contează:

* Modelele ML sunt consistente → variabilitate previzibilă (SD ~10 mg/dL)
* Oamenii sunt variabili → diferențe individuale, efecte de învățare, oboseală
* Risc: Dacă SD-ul uman real diferă de presupuneri, puterea se schimbă drastic

Exemple:

| Scenariu | SD Presupus | SD Real | N planificat pe grup | Puterea Reală | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Optimist | 10 mg/dL | 8 mg/dL | 100 | ~95% | Suprapotent |
| Cazul de bază | 10 mg/dL | 10 mg/dL | 100 | 80% | Adecvat |
| Conservator | 10 mg/dL | 12 mg/dL | 100 | ~65% | Subpotent |
| Pesimist | 10 mg/dL | 15 mg/dL | 100 | ~45% | Sever subpotent |

**Rezultat:** Studiul ar putea fi subpotent pentru a detecta efecte reale sau a risipi resurse cu înscrierea inutilă.

---

**Soluție Propusă:** Design Adaptiv în Două Etape

**Etapa 1 –** Analiza Interimară (N=60–75 pe grup)

* Calcularea SD-urilor și dimensiunilor efectului observate din date umane reale
* Recalcularea dimensiunii eșantionului necesare folosind estimări empirice
* Ajustarea obiectivului de recrutare pentru a menține 80% putere

**Etapa 2 –** Recrutare Ajustată

* Continuarea înscrierii până la obiectivul revizuit bazat pe constatările interimare
* Reguli de decizie pre-specificate:
  * *„Dacă SD observat \= 8 mg/dL → opriți la 100 pe grup (deja suprapotent)"*
  * *„Dacă SD observat \= 12 mg/dL → creșteți la 130 pe grup"*
  * *„Dacă SD observat >15 mg/dL → creșteți la maximum 150 pe grup"*
* Limita maximă: 150 pe grup

Beneficii:

* Asigură putere adecvată cu date din lumea reală
* Evită supra-recrutarea dacă variabilitatea este mai mică decât așteptată
* Previne subpotența severă dacă variabilitatea este mai mare

**8.3 Rezultatul Așteptat**

Cu înscrierea noastră țintă (100 pe grup, potențial extensibil la 150), ar trebui să avem putere adecvată pentru toate analizele planificate presupunând că estimările noastre de variabilitate sunt aproximativ corecte. Dar adevărata valoare a acestui studiu nu este numai testarea ipotezelor noastre specifice — ci stabilirea primelor referințe empirice pentru precizia de predicție glicemică umană.

Chiar dacă descoperim că oamenii sunt mult mai variabili decât modelele ML, aceasta este o constatare demnă de publicat. Ne-ar spune că capacitatea de predicție umană este fundamental mai puțin consistentă decât abordările algoritmice, ceea ce are implicații pentru modul în care proiectăm și evaluăm instrumentele de suport al deciziei clinice.

**Date lipsă și excluderi:** Vom folosi analiza cazurilor complete pentru rezultatele primare (participanți care finalizează cel puțin 6 segmente de predicție valide). Dacă datele lipsă depășesc 10% din participanții recrutați, vom efectua analize de sensibilitate comparând completorii vs. non-completorii pe caracteristicile de bază. Nu așteptăm date lipsă substanțiale deoarece sarcina este online și durează numai 15–20 de minute.

**Multiplicitate:** Avem două ipoteze primare (H1 și H2) folosind corecția Bonferroni (α=0,025 per test). Ipotezele secundare (H3, H4, H5) sunt exploratoare și vor fi raportate cu valori p nominale fără ajustare, etichetate clar ca analize exploratoare.

**Cine face analiza:** Analizele statistice primare vor fi efectuate de Anton Kulaga (IP) cu îndrumarea lui Benjamin Otte (consilier biostatistic). Toate analizele vor fi efectuate în Python folosind pachete standard. Codul de analiză va fi pus la dispoziție publicului alături de rezultatele publicate.

**Factorii de confuzie:** Designul transversal al studiului limitează capacitatea noastră de a controla factorii de confuzie. Vom colecta și raporta variabilele cheie (vârstă, durata diabetului, experiența MCG) și vom efectua analize stratificate unde dimensiunea eșantionului o permite. Comparațiile primare (PcD vs. non-PcD, MCG vs. fără-MCG) sunt descriptive mai degrabă decât cauzale, deci factorii de confuzie sunt mai puțin problematici decât pentru studiile intervenționale.

**Confirmatoriu vs. explorator:** H1 și H2 sunt ipoteze confirmatorii cu niveluri de semnificație ajustate Bonferroni. H3, H4 și H5 sunt exploratoare și vor fi raportate ca atare, cu intervale de încredere și dimensiuni ale efectului mai degrabă decât bazându-se exclusiv pe valorile p.

---

## **9\. Controlul Calității Datelor**

### **9.1 Verificări Automate**

* Validarea unicității email-ului
* Validarea intervalului de vârstă
* Verificări ale timpului de completare
* Validarea punctului de predicție (toate cele 12 puncte necesare)
* Verificări ale calității datelor MCG pentru încărcări

### **9.2 Criterii de Excludere pentru Analiză**

* Segmente cu predicții incomplete (mai puțin de 12 puncte)
* Segmente cu date de context MCG excesiv lipsă
* Participanți cu mai puțin de 5 segmente valide

---

## **10\. Analiza Risc-Beneficiu**

### **10.1 Riscuri pentru Participanți**

#### **10.1.1 Riscuri Fizice**

**Niciunul.** Acesta este un studiu observațional online fără intervenții fizice:

* Nicio procedură medicală
* Nicio administrare de medicamente
* Nicio vizită în persoană necesară
* **Nicio monitorizare de sănătate în timp real** — toate datele sunt istorice
* **Nicio conexiune la dispozitive medicale active** — participanții nu trebuie să poarte niciun echipament

#### **10.1.2 Riscuri Psihologice**

**Minime:**

* Posibilă frustrare cu sarcinile de predicție (atenuată prin instrucțiuni clare, încercări de practică)
* Ușoară anxietate de performanță (atenuată prin sublinierea scopului de cercetare)
* Preocupări de confidențialitate cu privire la partajarea datelor MCG (atenuate prin participare opțională, explicarea completă a protecției datelor)

**Evaluare Generală:** Riscuri comparabile cu completarea unui quiz sau sondaj online.

### **10.2 Beneficii**

**Beneficii Directe pentru Participanți:** Niciunul (numai studiu de cercetare). Rezultatele nu constituie consiliere medicală.

**Disclaimer-e Importante Comunicate Participanților:**

* Scorurile de precizie măsoară numai performanța de predicție — nu au semnificație diagnostică sau terapeutică
* Rezultatele nu trebuie folosite pentru ajustarea dozelor de insulină, alegerilor dietetice sau oricărei decizii medicale
* Participanții ar trebui să continue să urmeze independent îndrumarea furnizorului lor de asistență medicală

**Beneficii Indirecte:**

* Contribuție la cunoașterea științifică
* Perspectivă personală asupra capacității de predicție
* Sprijin pentru dezvoltarea unor instrumente mai bune de predicție a glucozei

---

## **11\. Protecția Participanților și Etică**

### **11.1 Consimțământul Informat**

Notă importantă — tot consimțământul va fi dat prin clic pe casetele de bifat corespunzătoare din interfața online și va fi stocat digital. Dacă consimțământul obligatoriu nu este dat, participantului nu i se permite să continue, oprind orice participare fără consimțire.

**Poarta de Verificare a Vârstei:**

Înainte de a accesa orice conținut al studiului, participanții trebuie să confirme că au 18 ani sau mai mult:

* Primul ecran afișează: „Acest studiu este deschis adulților cu vârsta de 18 ani și peste. Vă rugăm să vă confirmați vârsta pentru a continua."
* Două butoane: „Am 18 ani sau mai mult" (trece la consimțământ) / „Am sub 18 ani" (afișează mesajul: „Vă mulțumim pentru interes, dar acest studiu este deschis numai adulților. Vă rugăm să închideți această pagină.")
* Dacă este selectat „sub 18 ani": Nu se colectează date, sesiunea se termină imediat, niciun cookie sau identificator stocat
* Această poartă de vârstă apare înainte de orice colectare de date personale

**Procesul de Consimțământ Bilingv:**

Studiul furnizează materiale de consimțământ informat atât în engleză cât și în germană. Participanții selectează limba preferată la început:

* **Selecția Limbii:** Participanții aleg „English" sau „Deutsch" pe pagina de start
* **Materiale Complete:** Toate informațiile de consimțământ, instrucțiunile studiului și feedback-ul sunt afișate în limba selectată
* **Conținut Echivalent:** Ambele versiuni lingvistice conțin informații identice, asigurând înțelegere egală indiferent de preferința lingvistică

**Formularul Electronic de Consimțământ include:**

* Informații clare despre studiu în limbaj non-tehnic
* Accentuarea participării voluntare
* Explicarea drepturilor de protecție a datelor și RGPD
* Proceduri și limitări de retragere (retragerea posibilă până la anonimizarea datelor)
* Informații de contact

**Casetele de Consimțământ (obligatorii):**

* Confirm că am 18 ani sau mai mult, am citit și înțeles informațiile studiului și sunt de acord voluntar să particip
* Consimț prelucrarea datelor în scopuri de cercetare și înțeleg că mă pot retrage până la anonimizarea datelor (RGPD Art. 6(1)(a), 9(2)(a))

**Casetele de Consimțământ Opționale (clar separate de consimțământul studiului):**

* Sunt de acord să încarc propriile mele date MCG pentru sarcina opțională cu date proprii
* Sunt de acord să fiu recontactat pentru rezultatele studiului (email stocat numai în acest scop)

**Comunicări Promoționale (Separate de Consimțământul Studiului):**

Orice opt-in pentru comunicări promoționale despre HEALES sau proiecte conexe este:

* Prezentat pe o pagină SEPARATĂ DUPĂ finalizarea studiului (nu în timpul consimțământului)
* Etichetat clar ca neconexat cu participarea la studiu
* Nu are niciun efect asupra participării la studiu sau gestionării datelor
* Poate fi refuzat fără nicio consecință

### **11.2 Compensare**

Nicio compensare monetară. Stimulentele non-monetare includ feedback personalizat de precizie și card de rezultat partajabil.

### **11.3 Asigurare**

Nicio asigurare specifică studiului necesară datorită riscului minim (echivalent cu un sondaj online).

---

## **12\. Calendarul**

Calendarul studiului este flexibil și va fi ajustat pe baza progresului recrutării și a nevoilor operaționale. Fazele generale includ:

1. **Pregătire:** Depunere etică, finalizarea platformei, pregătirea materialului de recrutare
2. **Testare Pilot:** Testare la scară mică cu colectarea feedback-ului
3. **Recrutare și Colectarea Datelor:** Continuu până la atingerea înscrierii țintă
4. **Analiză:** Prelucrarea datelor, analiza statistică
5. **Diseminare:** Pregătirea manuscrisului, publicare, comunicarea cu participanții

Calendarele specifice vor fi determinate pe baza datei de aprobare etică și a succesului recrutării.

---

## **13\. Limitări**

### **13.1 Bias de Selecție**

Participanții sunt voluntari auto-selectați, care s-ar putea să nu reprezinte populația generală a utilizatorilor MCG.

### **13.2 Referințe Academice vs. din Lumea Reală**

Deși acest studiu folosește condiții mai realiste decât seturile de date academice controlate, participanții online pot diferi în continuare de utilizatorii tipici MCG.

### **13.3 Designul cu Sesiune Unică**

Fără urmărire longitudinală; efectele de învățare în timp nu pot fi evaluate.

---

## **14\. Informații de Contact**

**Investigator Principal:**

 Anton Kulaga  
 Institutul de Biostatistică și Informatică în Medicină și Cercetarea Îmbătrânirii (IBIMA)  
 Centrul Medical Universitar Rostock  
 Email: anton.kulaga@uni-rostock.de

**Co-investigatori:**

Livia Zaharia, MSc  
 HEALES \- Healthy Life Extension Society  
 Email: [liviazaharia2020@gmail.com](mailto:liviazaharia2020@gmail.com)

**Consilier biostatistic:**

Benjamin Otte, MSc  
 Institutul de Biostatistică și Informatică în Medicină și Cercetarea Îmbătrânirii (IBIMA)  
 Centrul Medical Universitar Rostock  
 Email: benjamin.otte@uni-rostock.de

**Manager de Date:**  
 Nikolay Usanov, MSc  
 HEALES \- Healthy Life Extension Society  
 Inginer ML și Bioinformatician

**Consiliu Consultativ:**

* Prof. Georg Fullen \- Centrul Medical Universitar Rostock
* Irina Gaynanova, PhD (Consilier Statistic) \- Texas A\&M University
* Renat Sergazinov, PhD (Consilier Tehnic) \- Autorul GlucoBench

## Referințe:

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

**Reglementări Aplicabile:**

* RGPD / BDSG (protecția datelor) \- DA
* Ghiduri de etică a cercetării germane \- DA
* Reglementările privind dispozitivele medicale (MDR) \- NU aplicabil
* AMG (legislația farmaceutică) \- NU aplicabil

---

**SFÂRȘITUL DOCUMENTULUI**

*Pentru întrebări sau clarificări, vă rugăm să contactați:*  
 *Anton Kulaga: anton.kulaga@uni-rostock.de*  
 *Livia Zaharia: livia.zaharia@uni-rostock.de*
