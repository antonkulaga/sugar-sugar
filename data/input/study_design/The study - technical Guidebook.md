# **Human Prediction of Next-Hour Glucose from Prior Continuous Glucose Monitor (CGM) Context: An Online Benchmarking Study**

**Study protocol**

**Principal Investigator:** Anton Kulaga \- Institute for Biostatistics and Informatics in Medicine and Ageing (IBIMA), University Medical Center Rostock, Rostock, Germany

**Co-Investigators:** Livia Zaharia (HEALES \- Healthy Life Extension Society, Bruselles, Belgium)

**Biostatistical advice:** Benjamin Otte, M.Sc. \- Department of Biostatistics, Institute for Biostatistics and Informatics in Medicine and Ageing (IBIMA), University Medical Center Rostock, Rostock, Germany

**Project Context:** This study is conducted as part of the Sugar-Sugar Glucose Accuracy Prediction Study, supported by HEALES (Healthy Life Extension Society)

**Registration Number:** Ref. number A 2026-0064  
**Received by the Ethics Committee:** February 27, 2026

---

## **Overview**

**Background:** 

Machine learning models for glucose prediction report accuracy metrics derived from controlled academic datasets, but no benchmark exists for human prediction accuracy. CGM users routinely anticipate future glucose levels as part of their daily self-management, yet the quality of the prediction has never been systematically assessed.

**Objectives:**

(0) Quantify human accuracy in predicting next-hour glucose from 3-hour CGM history; 

(1) Compare prediction accuracy between people with diabetes (PwD) of both type 1 and type 2 and people without diabetes, including pre-diabetes, wellness and non-prior-experience users (non-DM); 

(2) Compare prediction accuracy between CGM users and non-CGM users. A person is considered a CGM user if they have used a CGM for more than one month.

**Design:** 

Cross-sectional, observational online study where users are asked to make predictions six or more times and adaptive two-stage sample size design.

**Setting:** 

Web-based platform (Sugar-Sugar application) hosted by HEALES with research data stored at University Medical Center Rostock.

**Participants:** 

Target N≈200 adults (≥18 years): approximately 100 PwD and 100 non-Pwd, recruited via social media and diabetes organizations. Adaptive design allows adjustment up to 150 per group based on interim analysis. For a non-DM group, there are people that use their CGMs in fitness tracking, sport enhancement, lifestyle improvement, biohacking, etc that showed preliminary interest in participating.

Participants are partitioned into four groups: PwD CGM-Users (“PwD CGM” group), PwD without CGM (“PwD no-CGM” group), non-PwD CGM Users (eg. for wellness, sports etc, “non-PwD” group), non-PwD non-CGM Users no-prior-experience group (“NPE” group)

**Procedures:** 

Participants with CGM data are encouraged to upload their own data with previous glucose values measurements (further, historical data for brevity) for the prediction task. The task is to predict how CGM estimated glucose values (further, GV) will change knowing prior values. In the case of our web application this is done in an intuitive way, by drawing the line on a GV graph. For more details check section 4.2.

Participants without CGM data or who prefer not to upload, can use third-party data from public anonymized datasets that are free to download. We have collected the list of the datasets at [https://github.com/GlucoseDAO/glucose\_data\_processing/blob/main/docs/datasets.csv](https://github.com/GlucoseDAO/glucose_data_processing/blob/main/docs/datasets.csv) where datasets that have a “Downloader” column are fully public. 

Each participant will complete 6 to 12 prediction tasks. In each task, they will predict what will happen over the next hour by drawing points on a graph displayed in a web application. Specifically, they will predict 12 data points—one for every 5-minute interval across the 60-minute period. To help them make these predictions, participants will be shown the previous 3 hours of data as context.

Multiple prediction trials per participant are necessary to obtain reliable individual-level accuracy estimates and adequate statistical power.

**Measurement Reliability:** A single prediction trial provides an unreliable estimate of individual ability due to random variation (e.g., segment difficulty, momentary attention lapses). Averaging across 6-12 trials yields stable, reproducible accuracy metrics by reducing measurement error.

**Statistical Power:** The repeated-measures design substantially increases statistical power compared to single-trial designs. With 200 participants completing 10 trials each, the effective sample size for within-person analyses approaches 2,000 observations, enabling detection of small-to-moderate effect sizes (Cohen's d ≥ 0.3) that would require unfeasibly large sample sizes in single-trial designs.

**Contextual Variability:** Multiple trials allow sampling across diverse glucose dynamics (time of day, trend direction, event contexts), ensuring accuracy estimates reflect performance across representative scenarios rather than a single atypical case.

**Feasibility:** The 6-12 trial range balances measurement precision with participant burden. Pilot testing indicated sustained engagement through 15-20 minutes (approximately 10-12 segments), after which fatigue effects may compromise data quality.

This approach follows standard psychometric practice for establishing reliable individual differences in cognitive tasks and aligns with repeated-measures designs commonly used in human performance benchmarking studies.

**Main Outcome Measures:** 

We will measure how accurate the predictions are using two standard metrics: Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), both measured in mg/dL. These metrics will show how far off the predictions are from the actual glucose values. We'll calculate these metrics for both the machine learning models and the human participants' predictions.

**Statistical Analysis:** 

Group comparison of per-person MAE/RMSE between PwD and non-DM; comparison of human predictions vs. baseline models (persistence, linear extrapolation). Secondary analyses examine associations between experience and accuracy. Analysis accounts for repeated-measures structure.

**Ethics and Dissemination:** 

Submitted to Ethikkommission, Universitätsmedizin Rostock. Non-interventional study using historical data only. Results to be published in peer-reviewed journals.

---

## **1\. Background and Rationale**

### **1.1 Context: CGM Users and Self-Prediction**

Continuous Glucose Monitoring (CGM) devices \[5\] provide blood glucose measurements every 5 minutes, generating detailed 24-hour glucose profiles. CGM technology is used by several populations:

**People with Diabetes (PwD):**

* Use CGM data to inform their own insulin dosing, meal timing, and activity decisions  
* Develop intuitive pattern recognition through daily experience with their glucose trends  
* Make self-management decisions based on anticipated glucose trajectories

**Health-Conscious Individuals (Wellness Users):**

* Pre-diabetic individuals monitoring glucose for lifestyle optimization  
* Non-diabetic users interested in metabolic health and longevity  
* Athletes and biohackers tracking glucose response to diet and exercise

In all cases, users make their own predictions about future glucose levels as part of daily self-management \- this study quantifies that prediction ability.

### **1.2 The Missing Benchmark Problem**

Current machine learning models for glucose forecasting report technical metrics (RMSE, MAE) but these are derived from **controlled academic datasets**. According to GlucoBench \[1\], state-of-the-art models achieve:

* **30-minute predictions:** RMSE 8-12 mg/dL, MAE 6-10 mg/dL  
* **60-minute predictions:** RMSE 10-16 mg/dL, MAE 9-13 mg/dL

However, these metrics have important limitations:

1. **Controlled vs. Real-World Performance:** Academic benchmarks use curated datasets with consistent data quality. Real CGM users have gaps, sensor errors, and inconsistent event logging.  
2. **No Human Comparison:** We don't know how these ML metrics compare to the prediction ability that experienced CGM users develop through daily use.  
3. **Population Diversity:** Academic datasets often focus on specific diabetes types; real-world users include diabetic, pre-diabetic, and wellness populations with different prediction contexts.

**This study fills the gap** by establishing how well actual CGM users predict their own glucose in realistic conditions.  
Please consult the reference section for more details.

### **1.3 Research Gap and Innovation**

To our knowledge, **no prior study has systematically quantified human accuracy in predicting next-hour glucose trajectories**. This study addresses this critical gap by:

1. Establishing baseline human self-prediction accuracy across different user populations  
2. Comparing performance between four groups of people mentioned above: PwD CGM, PwD no-CGM, non-PwD CGM, and NPE.  
3. Examining factors associated with prediction accuracy (diabetes duration, CGM experience)  
4. Creating a real-world benchmark that complements laboratory-derived ML metrics

### **1.4 Study Justification**

This research is necessary because:

* **No human baseline exists:** We don't know how well experienced CGM users predict their own glucose  
* **Academic benchmarks are overoptimistic:** ML metrics from curated datasets don't reflect real-world performance conditions  
* **Diverse user populations:** Diabetic, pre-diabetic, and wellness CGM users may have different prediction abilities  
* **Self-management context:** Understanding human prediction ability informs realistic expectations for AI-assisted tools

---

## **2\. Study Objectives and Hypotheses**

### **2.1 Primary Objectives**

**Objective 0:**

Quantify how precisely humans can predict glucose levels for the next hour after seeing the previous 3 hours of glucose data, regardless of whether they use CGM or have diabetes.

**Objective 1:**

Quantify and compare how precisely people with diabetes (PwD) versus people without diabetes (non-Pwd) can predict glucose levels for the next hour after seeing the previous 3 hours of glucose data, regardless of whether they use CGM (CGM and non-CGM group combined pairwise by diabetes status vs each other).

**Objective 2:**

Quantify and compare accuracy of people who already use continuous glucose monitors versus people who don't use CGM can predict glucose levels for the next hour after seeing the previous 3 hours of glucose data, regardless of their diabetes status (PwD and non-PwD groups combined pairwise by CGM-experience)

### **2.2 Secondary Objectives**

**Objective 3:** Test whether longer diabetes duration is associated with better prediction accuracy.

**Objective 4:** Test whether longer CGM experience is associated with better accuracy.

**Objective 5:** Compare accuracy when participants predict using generic anonymized data versus their own CGM data (within-person comparison).

### 

### **2.3 Formal Hypotheses**  This section only presents the hypotheses- for statistical testing methods please check Section 7\.

#### **Primary Hypotheses**

**H1 (Group Difference- Diabetes Mellitus differentiator):**

* Null hypothesis (H1.1): Mean MAE of people with diabetes \= Mean MAE of people without diabetes  
* Alternative hypothesis (H1.2): Mean MAE of people with diabetes ≠ Mean MAE of people without diabetes- to have direction established by comparison

*Rationale:* People with diabetes have direct lived experience managing glucose variability and may develop intuitive pattern recognition through daily CGM use. Lower MAE indicates better prediction accuracy.

**H2 (Group Difference- CGM user differentiator):**

* Null hypothesis (H2.1): Mean MAE of people with CGM \= Mean MAE of people without CGM  
* Alternative hypothesis (H2.2): Mean MAE of people with CGM  ≠ Mean MAE of people without CGM- to have direction established by comparison

*Rationale:* GlucoBench \[1\] and related studies provide reference points: for 60-minute predictions, simple models achieve MAE \~12-20 mg/dL while deep learning models (Transformer, Gluformer) achieve MAE \~11-17 mg/dL depending on dataset and conditions. We expect human performance to fall somewhere in this range. This comparison establishes where human intuition sits relative to algorithmic approaches.

#### 

#### **Secondary Hypotheses**

**H3 (Duration Effect):**

* Null hypothesis (H3.0): There is no relationship between diabetes duration and MAE (ρ \= 0\)  
* Alternative hypothesis (H3.1): There is a negative relationship between diabetes duration and MAE (ρ \< 0), with the strongest effects occurring in the first 5 years

Longer diabetes duration is associated with a higher number of glucose values observations, paired with the outcomes, which in turn results in lower MAE (better accuracy). These span not only from CGM readings but also from experience cumulated previously via blood testing and observation on events such as eating, injecting, sports and physical activity. All these events would render an older diabetic into a more accurate predictor of glucose variation.

*Rationale:* People who have lived with diabetes longer have accumulated more experience observing how their glucose responds to meals, insulin, exercise, stress, and other factors. This extended exposure provides more opportunities to recognize patterns and develop intuitive prediction skills.

Important mention- duration in our case will only correlate with time with diabetes, not generic age of participant- as such we shall not group users according to their age but rather actual time with this condition. This will as well not be checked against the number of participants (ex: assuming that older people have more experience in their condition but less overall participation in the study- that would lead to uncertainty- we only care how duration of condition reflects accuracy in prediction out of those that participated) 

**H4 (CGM Experience Effect):**

* Null hypothesis (H4.0): There is no relationship between CGM experience duration and MAE (ρ \= 0\)  
* Alternative hypothesis (H4.1): There is a negative relationship between CGM experience duration and MAE (ρ \< 0), with the strongest effects occurring in the first 2 years

 Longer CGM experience is associated with lower MAE (better accuracy).

*Rationale:* CGM users make daily decisions based on their glucose trends \- adjusting insulin doses, timing meals, and modifying activities. This continuous feedback loop creates a natural learning environment where users develop pattern recognition skills through repeated decision-making and outcome observation. Users who have worn CGM longer have had more opportunities to learn their personal glucose dynamics.

**H5 (Own vs Generic Data):**

* Null hypothesis (H5.1): Mean MAE of people using own data \= Mean MAE of people using generic data  
* Alternative hypothesis (H5.2): Mean MAE of people using own data  ≠ Mean MAE of people using generic data- to have direction established by comparison

Participants have lower MAE (better accuracy) when predicting their own glucose patterns versus generic data.This will be measured by allowing the participants to test in two ways- either by using a generic dataset or by uploading their own data to predict upon. In the second case data will be anonymized from the user (no date will be shown- only time- to avoid recollection of exact date) and it will be represented exactly as in the previous case graphically.

*Rationale:* Participants are familiar with their own glucose patterns, lifestyle, and typical responses to meals and activities. This personal knowledge should provide an advantage when predicting their own data compared to unfamiliar generic profiles.

**H6 (Human vs Baseline Models):**  
We hypothesize that human prediction accuracy (MAE) will fall between simple baseline models and state-of-the-art AI approaches. 

Baseline models are the simplest possible prediction methods \- they require no training or complex algorithms. Our baselines include: (1) persistence model \- assuming glucose stays the same as the current reading, (2) linear extrapolation \- drawing a straight line through recent readings and extending it forward, and (3) ARIMA \- a standard statistical method for time-series data. 

We expect the performance hierarchy: simple baselines \< human predictions \< deep learning models (e.g., LSTMs, Transformers). We will test whether humans significantly outperform baselines and whether deep learning significantly outperforms humans.

This hypothesis will be left for the continuation of the study at the moment when we will have a well defined model- At the moment no model is involved in the study.

*Rationale:* GlucoBench and related studies provide reference points: for 60-minute predictions, simple models achieve MAE \~12-20 mg/dL while deep learning models (Transformer, Gluformer \[2,7,8\]) achieve MAE \~11-17 mg/dL depending on dataset and conditions. We expect human performance to fall somewhere in this range. This comparison establishes where human intuition sits relative to algorithmic approaches.

---

## **3\. Study Design**

### **3.1 Study Type**

**Design:** Observational, cross-sectional with repeated prediction tasks. For more details please check Section 4.2  
**Data Collection:** Web-based, online platform  
**Follow-up:** None (single-session participation)

### **3.2 Regulatory Classification**

This study is  a **non-interventional, observational study** that does not require physician supervision or medical device regulation.

#### **3.2.1 Historical Data Only**

* All CGM data shown to participants is **historical, pre-recorded data** \- either from a pooled anonymous dataset or from the participant's own previously-exported CGM files  
* **No real-time glucose monitoring** is performed during the study  
* **No connection to active CGM devices** \- participants do not need to wear or use any monitoring equipment for this study  
* The study analyzes prediction accuracy on past data segments, not current health status

#### **3.2.2 No Medical Decisions or Diagnoses**

This study explicitly does **NOT**:

* Provide any medical diagnosis or prognosis  
* Make any therapeutic or treatment recommendations  
* Influence any clinical decisions or medical treatment plans  
* Offer personalized health advice or guidance  
* Generate outputs intended for clinical use

**Results are purely for research benchmarking purposes** \- accuracy scores indicate prediction performance only and have no diagnostic or therapeutic meaning.

#### **3.2.3 No Physician Supervision Required**

Physician oversight is not required for this study because:

* **No medical intervention** is administered  
* **No diagnostic testing** is performed  
* **No health outcomes** depend on participation or results  
* **No treatment decisions** are informed by the study  
* The activity is equivalent to **completing an online cognitive task or survey**

### **3.3 Study Population**

#### **Inclusion Criteria**

**General Population (Both Groups):**

* Age 18 years or older  
* Able to provide informed consent  
* Internet access and basic computer/mobile literacy  
* Willing to complete prediction tasks

**Additional for People with Diabetes (PwD):**

* Self-reported diagnosis of diabetes (Type 1, Type 2, or other)  
* Current or past CGM use (any device)

---

## **4\. Participant Workflow and Procedures**

### **4.1 Recruitment Strategy**

**Recruitment Channels:**

1. Social media announcements (Twitter/X, LinkedIn, Facebook diabetes groups)  
2. Diabetes patient organizations and advocacy groups  
3. Scientific advisory board networks  
4. Community channels (project website, Telegram)  
5. Academic conferences (presentations at longevity/diabetes meetings)

Specific recruitment materials will be developed after ethics clearance is obtained.

### **4.2 Study procedures**

#### **Phase 1: Consent and Baseline Information**

Participants access the Sugar-Sugar web application via an URL(web address) and complete:

**1\. Electronic Informed Consent**

* Study information sheet  
* Data protection information (GDPR-compliant)  
* Checkbox consent for study participation and data processing  
* Optional consents for: uploading own CGM data, future re-contact in case the user would like to know more details about the results of the study when completed, promotional communications

**2\. Baseline Questionnaire**  
**(will be filled in by participant, accurately, based on their knowledge)**

* Email (for unique identification; hashed for anonymization)  
* Age (years)  
* Sex/gender  
* Country of residence  
* Diabetes status (Yes/No)  
  * If Yes: Diabetes type, years since diagnosis  
* CGM use  (Yes/No)  
  * If Yes: years of use  
* Optional weight (kg) and height (cm) 

**Data Protection Note:** Emails are hashed immediately upon submission for unique identification without storing personal identifiers. Participants can opt-in separately for re-contact communications.

#### **Phase 2: Practice Trials**

2 optional practice trials provided to familiarize participants with the interface (users have an option not to submit for the first 2 trials). Practice trial data is excluded from analysis.

#### **Phase 3: Generic Data Prediction Task** 

**Task Structure:**

* **Number of trials:** 6-12 prediction segments per participant  
* **Each segment:** Participant draws 12 prediction points (5-min intervals over 60 minutes)  
* **Context window shown:** 3 hours of CGM data (36 points at 5-min resolution)  
* **Data source:** De-identified CGM data from the study's curated dataset

Segments are selected to provide a balanced mix of different times of day, glucose trends, and event contexts. Order is randomized across participants.

**Interface Features:**

* Interactive graph with 5-minute time grid  
* Participants click/draw to create prediction curve  
* Display of event markers (meal/insulin/exercise timestamps)  
* Editable predictions before submission

*Here below there is the main interface for the user after filling in the data and consent forms.*   
*\-blue line and point represent the charted historical data plotted for the test*

*\-red line is predicted data by the user*

*\-there is the option to change measurements units- depending on the ones the participant is most accustomed to*

*\-there is information regarding which round out of the 12 this is*

*\-user has two options at any stage during the test- submit or just exit*

*After each round user receives a screen as follows:*

*\-there is information regarding what round it was*

*\-there is comparison of the data- blue line is being shown completely*

*\-there is the numerical editing results*

*\-as well as the statistical result per this round*

*\-user again has option to exit or to continue to next round*

*At the end of the trial (max 12 rounds) user receives this screen where all the data is compiled per the whole trial. Below are two examples- one in which the user has done only one round and one in which the user has done multiple rounds. As can be seen it contains:*  
*\-accuracy metrics*

*\-units in which it was run*

*\-values per each round*

*\-ranking![][image1]*

![][image2]

#### **Phase 4: Own-Data Upload and Task (Optional)**

**Eligibility:** Participants who indicated willingness to upload CGM data

**Data Upload Process:**

1. Upload CGM export file (CSV or JSON format from supported devices)  
2. Automated quality checks (minimum 5 consecutive days, data validation)  
3. Data processing in which we convert from the supported device format to the uniform format we use for data output.  
4. Data pseudonymization and secure storage

**Own-Data Prediction Task:**

* 6-12 segments sampled from participant's own CGM data  
* Segments anonymized (no dates/times displayed)  
* Allows within-person comparison of accuracy on own vs generic data

#### **Phase 5: Completion and Feedback** 

**Brief Safety Reminder (First View Only):**

On first participation, a brief notice is displayed before results:

**Research purposes only** \- These scores measure pattern recognition performance, not medical ability. Continue following your healthcare provider's guidance.

This notice is shown once per user; returning users see results directly.

**Results Display (shown by default):**

* Personal accuracy summary (MAE in mg/dL)  
* Percentile rank compared to other participants based on current database storage at the moment of the user’s participation. Simply put we have a separate storage of ranking- we only need an anonymized user ID and rank- from there you find out total number of participants and their performance  
* Visual comparison of predictions vs actual trajectories  
* Option to "Skip and finish" available but not prominent

**Shareable Result Card (User-Controlled Content):**

Users can create and share a result card with customizable content:

* **Always included:** "I participated in the Sugar-Sugar glucose prediction study"  
* **User can choose to include:** accuracy percentile, MAE score, number of segments completed, comparison to other participants  
* **User controls what to share** \- gamification is a key engagement feature  
* Users are informed that sharing may reveal their interest in glucose/diabetes topics

**No Medical Advice:** Results are presented as game/research performance metrics, not health assessments.

---

## **5\. Data Collection and Management**

### **5.1 Data Categories**

**Baseline Data:** Demographics and user data such as:

* Email (for unique identification; hashed for anonymization)  
* Age (years)  
* Sex/gender  
* Country of residence  
* Diabetes status (Yes/No)  
  * If Yes: Diabetes type, years since diagnosis  
* CGM use  (Yes/No)  
  * If Yes: years of use  
* Optional weight (kg) and height (cm) 

**Consent preferences:**

* for study participation and data processing  
* for: uploading own CGM data, future re-contact in case the user would like to know more details about the results of the study when completed, promotional communications

**Graph Data:**

6-12 segments per participant, each containing

**Prediction Data:** 12 prediction points (including glucose value and timestamp), 

**Ground Truth Data:** 12 actual CGM values for evaluation (not shown to participants until after submission, including glucose value and timestamp)

**Result Data:**

MAE, MSI, RSME, MAPE values

### **5.2 Data Protection and GDPR Compliance**

#### **5.2.1 Data Controller, Processor, and Architecture**

**Data Controller:** The Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA) at Universitätsmedizin Rostock (UMR) is the data controller for this study.

**Implications of this arrangement:**

* IBIMA/UMR bears full responsibility for GDPR compliance and participant rights  
* All data subject requests (access, deletion, withdrawal) are handled by the study team at IBIMA

**Data Processor:** HEALES (Healthy Life Extension Society) will operate the Sugar-Sugar web application as a data processor under a Data Processing Agreement (DPA) with UMR.

**Technical Architecture: Pull Model**

The study uses a security-focused "pull model" architecture:

\[Participant\] → \[Sugar-Sugar App (HEALES servers)\] ← \[UMR Data Collector\]

                         ↓                                    ↑

                   \[Temporary Cache\] ──────────────────→ \[Research Database (UMR)\]

**How it works:**

1. Participant interacts with Sugar-Sugar app hosted on HEALES servers  
2. Completed session data is encrypted and temporarily cached on HEALES servers  
3. UMR data collection system **pulls** data from HEALES periodically (every 2 hours) and decrypts it.  
4. After successful transfer, cache on HEALES is cleared  
5. All persistent research data is stored exclusively on UMR servers  
6. No decryption capability exists on HEALES side, securing temporary cache

**Security advantages:**

* UMR research database has no incoming access from external systems  
* HEALES cannot "push" data to UMR \- UMR initiates all data transfers, data flow is unidirectional by design.  
* Temporary storage of encrypted data in cache without decryption keys on HEALES side mitigates risks of unauthorized cache access.  
* Reduced attack surface on research data infrastructure  
* Clear separation between application layer (HEALES) and data storage (UMR)

**Temporary cache on HEALES servers:**

* Contains only completed session data awaiting transfer, in encrypted form.  
* Maximum retention: 7 days (auto-deleted if pull fails)  
* Encrypted at rest  
* No direct access to cache except by automated pull system  
* Cache is transient processing, not persistent storage

**Data Processing Agreement (DPA) specifies:**

* HEALES processes data only as instructed by UMR  
* No persistent storage of research data on HEALES servers  
* No unencrypted storage of research data on HEALES servers  
* Cache cleared immediately after successful pull to UMR  
* Automatic cache deletion after 7 days regardless of pull status  
* Security measures for temporary cache (encryption, access controls)  
* Audit rights for UMR  
* HEALES staff access limited to technical maintenance only

**No other external processors:**

* No external analytics, CDN, or third-party services process participant data  
* HEALES community members (other than listed study team) have no access to participant data

#### **5.2.2 Identification and Pseudonymization**

**What is stored and why:**

1. **Email address (plain text, encrypted at rest):** Stored separately from research data for two purposes only:  
   * Enabling withdrawal requests (participant contacts us, we locate and delete their data)  
   * Optional re-contact for study results (only if participant opted in)  
2. **Study ID:** Random alphanumeric identifier assigned by hashing			 (e.g., f5afc4cf-9881-467d-88a1-325eb9558baa) assigned at registration  
3. **Linking table:** A separate, encrypted file mapping Study ID ↔ Email address  
   * Stored on separate encrypted drive from research data  
   * Access restricted to PI (Anton Kulaga) and co-PI only  
   * Purpose: Enable withdrawal and optional re-contact  
4. **Research data:** All prediction data, CGM uploads, questionnaire responses stored pseudonymised with Study ID only (no email, no name)

**Hash clarification:** We do NOT rely on email hashing for pseudonymization. The hash is used only for duplicate detection during registration (preventing same person registering twice). The linking table contains the actual email for withdrawal/re-contact purposes.

#### **5.2.3 Retention and Deletion Policy**

| Data Type | Retention Period | Deletion Trigger |
| :---- | :---- | :---- |
| Email addresses | Until study completion \+ 12 months | Linking table destroyed after grace period |
| Linking table | Study completion \+ 12 months | Destroyed, rendering data fully anonymous |
| Research data (pseudonymized) | 10 years per German research standards | N/A \- retained for reproducibility |
| Uploaded CGM files | Processed immediately, raw files deleted within 30 days | Automatic after segment extraction |

#### **5.2.4 Withdrawal Limitations (Important)**

**Withdrawal is possible at any time UNTIL the linking table is destroyed** (approximately 12 months after study completion). After this point:

* Research data becomes fully anonymous (no re-identification possible)  
* Withdrawal requests cannot be fulfilled as we cannot identify which data belongs to the requester  
* This limitation is clearly stated in the consent form

**Withdrawal process:**

1. Participant emails study coordinator requesting withdrawal  
2. We locate their Study ID via the linking table  
3. All research data associated with that Study ID is permanently deleted  
4. Confirmation sent to participant

#### **5.2.5 Cross-Border Data Transfers**

**No data leaves the European Union.**

* **UMR research database:** Located in Germany (EU)  
* **HEALES managed cloud account:** Located in EU (temporary cache only, max 24 hours)  
* No third-party services that transfer data outside EU  
* No CDN, external analytics, or cloud services with non-EU data centers  
* Email communications use standard EU-based email providers

Participants outside the EU may participate, but their data is processed and stored exclusively within the EU under GDPR protections.

#### **5.2.6 Data Storage Security**

* **UMR research database location:** Germany (EU)  
* **HEALES temporary cache location:** EU  
* **Encryption in transit:** TLS 1.3 (both app-to-user and UMR-to-HEALES pull)  
* **Encryption at rest:** AES-256 (both UMR database and HEALES cache)  
* **Access controls:** Role-based; research data accessible to study team; linking table accessible to PIs only  
* **Backup:** Encrypted daily backups within EU (UMR only; HEALES cache is transient)  
* **Audit logging:** All data access logged

---

## **6\. Outcome Measures and Accuracy Metrics**

### **6.1 Primary Metrics**

We use standard metrics from the glucose prediction literature \[1,9,10\], enabling direct comparison with published ML model benchmarks (e.g., GlucoBench \-for more details see Reference section).

**Mean Absolute Error (MAE):** Average of the absolute difference between predicted and actual glucose values (in mg/dL). Lower values indicate better accuracy.

 MAE \= (1 / n) × Σ |predicted − actual|

* Measures the typical size of prediction errors

* All errors are weighted equally

* Same units as the target variable

**Root Mean Squared Error (RMSE):** Square root of the average squared differences. Penalizes larger errors more heavily than MAE. Also reported in mg/dL.

 RMSE \= sqrt(MSE)

* Same unit as the target variable

* Penalizes large errors like MSE

* Easier to interpret than MSE

**Mean Squared Error (MSE):** The average of the squared differences between predicted and actual values.

 MSE \= (1 / n) × Σ (predicted − actual)²

* Penalizes large errors more heavily

* Sensitive to outliers

* Units are squared, making it harder to interpret directly


**Mean Absolute Percentage Error (MAPE):** The average absolute error expressed as a percentage of the actual value.

 MAPE \= (100 / n) × Σ |(predicted − actual) / actual|

* Measures relative error

* Scale-independent

* Can be misleading when actual values are close to zero

These metrics are computed:

* Per trial (across the 12 prediction points)  
* Per participant (averaged across their 6-12 trials)  
* Per group (for group comparisons)


### **6.2 Baseline Model Comparisons**

To contextualize human performance, we compare against simple baseline models using the same test segments:

* **Persistence model:** Predict glucose remains constant at last observed value  
* **Linear extrapolation:** Project the last 30 minutes trend forward

This will be done after the gathering of data to set a start point for the future part of the study where we will integrate ML models. It will not affect the gathering of data in this stage of the study. Please refer to H6 for more details.

---

## **7\. Statistical Analysis Plan**

### **7.1 Overview**

The study collects **multiple measurements per participant** (6-12 prediction segments each, with 12 points per segment). Analysis accounts for this repeated-measures structure. It gives a more accurate overview of the participant prediction skill than just a one time measurement.

### **7.2 Analysis Populations**

* **Primary analysis:** All participants completing at least 6 analyzable generic data segments  
* **Own-data analysis:** Participants completing at least 6 own-data segments  
  The number of data segments proposed are due to the expected variability in the accuracy metrics (MAE/RMSE). Based on what we see in GlucoBench data, the standard deviation for prediction accuracy is around 0.18-0.22 on a 0-1 scale. If there would only be 2-3 measurements per person, the estimate of their ability would have large confidence intervals.

## **7.3 Primary Analyses**

### **H1 (Group Difference \- Diabetes Status)**

**Objective**: Compare prediction accuracy between people with diabetes (PwD) and people without diabetes (non-PwD).

**Data Summarization**: Each participant will predict glucose values for multiple time points across different glucose trace presentations. We will calculate one MAE value per participant by averaging their prediction errors across all their predictions. This gives us one summary accuracy score per person.

**Statistical Method**:

1. **Normality Check**: We will first test whether MAE values are normally distributed within each group using the Shapiro-Wilk test (p \> 0.05 indicates normal distribution).  
2. **Group Comparison**:  
   * **If data is normally distributed** (Shapiro-Wilk p \> 0.05): We will use an **independent samples t-test**. This test compares the average MAE between two groups while accounting for the variability within each group and sample sizes. The t-test calculates whether the observed difference in averages is larger than would be expected by random chance alone.  
   * **If data is non-normal** (Shapiro-Wilk p \< 0.05): We will use the **Mann-Whitney U test**. This non-parametric test compares groups by ranking all MAE scores from best to worst (regardless of group), then testing whether one group tends to have better ranks than the other. This approach is robust to outliers and skewed distributions.  
3. **Significance Level**: α \= 0.05 (two-tailed)  
4. **Effect Size**: We will report Cohen's d (for t-test) or rank-biserial correlation (for Mann-Whitney) to quantify the magnitude of difference.

**Why this approach**: We use per-person summary statistics (one MAE per participant) rather than analyzing thousands of individual predictions because individual predictions from the same person are not independent \- they're influenced by that person's consistent prediction strategy. Summarizing to one value per person ensures our statistical tests meet the assumption of independent observations.

---

### **H2 (Group Difference \- CGM Experience)**

**Objective**: Compare prediction accuracy between people who currently use CGM and people who have never used CGM.

**Data Summarization**: Same as H1 \- one MAE value per participant, averaged across all their predictions.

**Statistical Method**: Identical approach to H1:

1. Shapiro-Wilk test to assess normality  
2. Independent samples t-test (if normal) or Mann-Whitney U test (if non-normal)  
3. Significance level α \= 0.05 (two-tailed)  
4. Report appropriate effect size

**Rationale**: Same logic as H1 \- we're comparing two independent groups on a single accuracy measure per person.

---

## **7.4 Secondary Analyses**

### **H3 (Duration Effect \- Diabetes)**

**Objective**: Test whether longer diabetes duration is associated with better prediction accuracy.

**Data Summarization**: For each participant with diabetes, we have:

* **Predictor variable**: Diabetes duration in years (continuous variable)  
* **Outcome variable**: MAE (one value per person, calculated as in H1)

**Statistical Method**:

1. **Normality and Linearity Check**:  
   * Create a scatterplot of diabetes duration (x-axis) vs MAE (y-axis) to visually inspect the relationship  
   * Use Shapiro-Wilk test to check if MAE values are normally distributed  
   * Examine scatterplot for linearity vs curved patterns  
2. **Correlation Analysis**:  
   * **If MAE is normally distributed AND relationship appears linear**: Use **Pearson's correlation coefficient (r)**. This measures the strength and direction of a linear relationship between two continuous variables. Values range from \-1 (perfect negative relationship) to \+1 (perfect positive relationship). We expect negative correlation (longer duration → lower MAE).  
   * **If MAE is non-normal OR relationship appears non-linear**: Use **Spearman's rank correlation (ρ)**. This works like Pearson's but uses ranks instead of actual values, making it robust to outliers and able to detect monotonic (consistently increasing or decreasing) relationships even if they're not perfectly linear.  
3. **Significance Level**: α \= 0.05 (two-tailed)  
4. **Exploratory Analysis**: Because we anticipate the relationship may plateau (large improvement in early years, minimal improvement after 5+ years), we will additionally:  
   * Fit a logarithmic model: MAE \= β₀ \+ β₁·log(duration \+ 1\)  
   * Compare linear vs logarithmic fit using R² values  
   * Create a visualization showing how MAE changes across duration categories (\<1 year, 1-5 years, 5-10 years, \>10 years)

**Why this approach**: Correlation analysis is appropriate when examining the relationship between two continuous variables. We use Spearman's as a backup because learning curves often show diminishing returns (non-linear patterns), and Spearman's can detect these relationships even when they're not perfectly straight lines.

---

### **H4 (CGM Experience Effect)**

**Objective**: Test whether longer CGM experience is associated with better prediction accuracy among CGM users.

**Data Summarization**:

* **Predictor variable**: CGM experience in years (continuous variable, only for CGM users)  
* **Outcome variable**: MAE (one value per CGM user)

**Statistical Method**: Identical approach to H3:

1. Scatterplot visualization and normality check (Shapiro-Wilk)  
2. Pearson's correlation (if normal/linear) or Spearman's correlation (if non-normal/non-linear)  
3. Exploratory logarithmic modeling to test for plateau effects  
4. Significance level α \= 0.05

**Rationale**: Same logic as H3 \- we expect CGM users may show rapid improvement initially, with learning plateauing after they've internalized common glucose patterns.

---

### **H5 (Own vs Generic Data)**

**Objective**: Test whether participants predict more accurately when viewing their own glucose data compared to generic anonymized data.

**Data Summarization**: This is a **within-person comparison**. Participants who complete both conditions will have:

* **Own-data MAE**: Average error across all predictions on their personal glucose traces  
* **Generic-data MAE**: Average error across all predictions on anonymized traces  
* **Difference score**: Generic MAE \- Own MAE (positive values indicate better performance on own data)

**Statistical Method**:

1. **Why paired analysis**: We use "paired" tests because we have **two measurements from the same person** (own-data accuracy vs generic-data accuracy). This is fundamentally different from H1-H2 where we compare different people. Paired tests account for the fact that the same individual appears in both conditions, controlling for person-specific factors like general prediction ability, attention, motivation, etc.  
2. **Normality Check**: Shapiro-Wilk test on the **difference scores** (not the raw MAE values)  
3. **Comparison**:  
   * **If difference scores are normally distributed**: Use **paired samples t-test**. This tests whether the average difference between conditions is significantly different from zero, while accounting for within-person correlation.  
   * **If difference scores are non-normal**: Use **Wilcoxon signed-rank test**. This is the non-parametric equivalent of the paired t-test \- it ranks the absolute differences and tests whether positive differences (better on own data) are more common than negative differences.  
4. **Significance Level**: α \= 0.05 (two-tailed)  
5. **Effect Size**: Report Cohen's d for paired design

**Why this approach**: Paired tests are more powerful than independent tests because they remove variability due to individual differences. If Person A is just naturally better at prediction tasks than Person B, that doesn't matter \- we only care whether each person performs differently across the two data types.

---

### **H6 (Human vs Baseline Models)**

**Note**: This hypothesis is deferred to future work when baseline models are implemented. When analyzed, we will use similar paired comparison approaches, comparing each participant's MAE to the MAE achieved by computational models on the same glucose traces.

---

## **Summary Table of Statistical Methods**

| Hypothesis | Comparison Type | Primary Test | Alternative Test | When to Use Alternative |
| ----- | ----- | ----- | ----- | ----- |
| H1 | Independent groups (PwD vs non-PwD) | Independent t-test | Mann-Whitney U | Shapiro-Wilk p \< 0.05 |
| H2 | Independent groups (CGM vs non-CGM) | Independent t-test | Mann-Whitney U | Shapiro-Wilk p \< 0.05 |
| H3 | Correlation (duration vs MAE) | Pearson's r | Spearman's ρ | Non-normal or non-linear |
| H4 | Correlation (CGM experience vs MAE) | Pearson's r | Spearman's ρ | Non-normal or non-linear |
| H5 | Paired comparison (own vs generic) | Paired t-test | Wilcoxon signed-rank | Difference scores non-normal |

**All tests use α \= 0.05 significance level. Effect sizes will be reported for all analyses.**

### **7.5 Effect Size Expectations**

Based on GlucoBench and related glucose prediction literature for **60-minute prediction horizons**:

**Model Performance from Published Benchmarks (MAE in mg/dL):**

Performance varies considerably across datasets and conditions. Representative ranges from the literature:

* **Linear regression / ARIMA \[7,8\]:** MAE \~12-20 mg/dL (GlucoBench ID data), RMSE \~23-27 mg/dL (other studies)  
* **Deep learning (Transformer, Gluformer \[2,7,8\]):** MAE \~11-17 mg/dL depending on dataset  
* **State-of-the-art personalized models:** MAE \~15-17 mg/dL (recent LLM-based approaches \[3\])

Note: Values vary substantially by dataset size, population characteristics, and whether evaluation is in-distribution (ID) vs out-of-distribution (OD). GlucoBench reports that deep learning models generalize considerably better than simple baselines on OD data.

**Expected Effect Sizes for Study Hypotheses:**

Given this variability, we use conservative assumptions:

* **H1 (PwD vs non-DM):** Assuming SD \~8-12 mg/dL across participants and a meaningful difference of \~3-5 mg/dL between groups, this represents Cohen's d \~0.3-0.5 (small to medium effect).  
* **H2 (Human vs baselines):** The gap between simple and advanced models is typically \~5-10 mg/dL. We expect humans to fall within this range. For more description of human expected distribution check the sample size distribution.  
* **H3, H4 (Duration/CGM correlations):** We expect correlations of r \~0.15-0.30 between experience and accuracy, based on learning curve assumptions.  
* **H5 (Own vs generic):** We expect \~2-4 mg/dL improvement when predicting own data (paired effect). This is important since it covers the expected difference between the actual glucose value measured by blood and estimated glucose value (EGV) that CGMs provide.

**Important caveat:** These effect size estimates are derived from inter-model variability in ML benchmarks, not from prior human prediction studies (which do not exist). The actual human performance distribution is unknown and will be established by this study. We emphasize that these numbers are estimated based on the papers mentioned in the reference section, especially Glucobench paper.

---

## **8\. Sample Size**

### **8.1 Target Enrollment**

**Target:** Approximately 200 participants total

* Approximately 100 people with diabetes (PwD)  
* Approximately 100 people without diabetes (non-DM)  
* Among PwD: aim for 70-90 participants uploading own data

**Minimum viable:** Approximately 150 participants (75 per group)

### **8.2 Rationale**

Sample size targets are based on effect size estimates derived from ML model benchmarks, with acknowledgment of uncertainty:

**Handling repeated measures:** Each participant makes 6-12 predictions, which means our data has a repeated-measures structure. We account for this in two ways: (1) our primary analyses will use per-person averages (one MAE value per participant), which satisfies the independence assumption for t-tests and correlations, and (2) for more detailed analyses, we'll use mixed-effects models that explicitly model the correlation between repeated measures from the same person.

**Meaningful differences:** We consider a 3-4 mg/dL difference in MAE to be clinically meaningful because it's roughly half the measurement error of CGM devices themselves (which have a mean absolute relative difference of 8-10% from blood glucose, or about 7-9 mg/dL at typical glucose levels). A correlation of r=0.25 explains about 6% of variance, which, while modest, would be worth understanding for future intervention design.

**H1 (Diabetes vs non-diabetes group comparison):** To detect a 4 mg/dL difference in mean absolute error (MAE) between groups, assuming a standard deviation of 10 mg/dL (Cohen's d ≈ 0.4), we need 80-100 participants per group. We used a one-sided test with α=0.025 here because previous literature suggests people with diabetes might predict better, though the direction isn't certain. This Bonferroni adjustment accounts for testing two primary comparisons (H1 and H2).

**H2 (CGM users vs non-users):** Same calculation as H1—we expect similar effect sizes and need approximately 80-100 per group. The paired nature of some comparisons within participants (where the same person makes multiple predictions) actually gives us additional statistical power, but we're being conservative in our estimates.

**H3 and H4 (Correlation analyses):** To detect a correlation of r=0.25 between experience duration and prediction accuracy with 80% power, we need 100-120 participants. The range (100-120) reflects uncertainty in the true correlation strength—if the actual correlation is weaker than r=0.25, we'd need the higher end of that range. We picked r=0.25 as our target because smaller correlations would be of limited practical importance.

**H5 (Own data vs generic data comparison):** This is a within-person comparison, so we have more statistical power. To detect a 3 mg/dL difference in paired measurements (assuming paired SD of 6 mg/dL), we need about 70 participants who complete both tasks. The paired design is more efficient because each person serves as their own control.

**Important Caveat:** Sample Size Uncertainty

Our sample size calculations are based on ML model performance, but human behavior may differ:

Why this matters:

* ML models are consistent → predictable variability (SD \~10 mg/dL)  
* Humans are variable → individual differences, learning effects, fatigue  
* Risk: If actual human SD differs from assumptions, power changes dramatically

Examples:

| Scenario | Assumed SD | Actual SD | Planned N per group | Actual Power | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Optimistic | 10 mg/dL | 8 mg/dL | 100 | \~95% |  Overpowered |
| Base case | 10 mg/dL | 10 mg/dL | 100 | 80% | Adequate |
| Conservative | 10 mg/dL | 12 mg/dL | 100 | \~65% | Underpowered |
| Pessimistic | 10 mg/dL | 15 mg/dL | 100 | \~45% | Severely underpowered |

**Result:** Study could be underpowered to detect real effects or waste resources with unnecessary enrollment.

---

**Proposed Solution:** Adaptive Two-Stage Design

**Stage 1 \-** Interim Analysis (N=60-75 per group)

* Calculate observed SDs and effect sizes from real human data  
* Recalculate required sample size using empirical estimates  
* Adjust recruitment target to maintain 80% power

**Stage 2 \-** Adjusted Recruitment

* Continue enrollment to revised target based on interim findings  
* Pre-specified decision rules:  
  * *"If observed SD \= 8 mg/dL → stop at 100 per group (already overpowered)"*  
  * *"If observed SD \= 12 mg/dL → increase to 130 per group"*  
  * *"If observed SD \>15 mg/dL → increase to maximum 150 per group"*  
* Maximum cap: 150 per group

Benefits:

*  Ensures adequate power with real-world data  
*  Avoids over-recruitment if variability is lower than expected  
*  Prevents severe underpowering if variability is higher

**8.3 Expected result**

With our target enrollment (100 per group, potentially expanding to 150), we should have adequate power for all planned analyses assuming our variability estimates are roughly correct. But the real value of this study isn't just testing our specific hypotheses—it's establishing the first empirical benchmarks for human glucose prediction accuracy.

Even if we discover humans are far more variable than ML models, that's a finding worth publishing. It would tell us that human prediction ability is fundamentally less consistent than algorithmic approaches, which has implications for how we design and evaluate clinical decision support tools.

**Missing data and exclusions:** We'll use complete-case analysis for the primary outcomes (participants who finish at least 6 valid prediction segments). If missing data exceeds 10% of recruited participants, we'll conduct sensitivity analyses comparing completers vs non-completers on baseline characteristics. We don't expect substantial missing data because the task is online and takes only 15-20 minutes.

**Multiplicity:** We have two primary hypotheses (H1 and H2) using Bonferroni correction (α=0.025 per test). Secondary hypotheses (H3, H4, H5) are exploratory and will be reported with nominal p-values without adjustment, clearly labeled as exploratory analyses.

**Who's doing the analysis:** Primary statistical analyses will be conducted by Anton Kulaga (PI) with guidance from Benjamin Otte (biostatistical advisor). All analyses will be performed in python using standard packages. Analysis code will be made publicly available alongside the published results.

**Confounding:** The study's cross-sectional design limits our ability to control for confounders. We'll collect and report key variables (age, diabetes duration, CGM experience) and conduct stratified analyses where sample size permits. The primary comparisons (PwD vs non-PwD, CGM vs non-CGM) are descriptive rather than causal, so confounding is less of a concern than for interventional studies.

**Confirmatory vs exploratory:** H1 and H2 are confirmatory hypotheses with Bonferroni-adjusted significance levels. H3, H4, and H5 are exploratory and will be reported as such, with confidence intervals and effect sizes rather than relying solely on p-values.

---

## **9\. Data Quality Control**

### **9.1 Automated Checks**

* Email uniqueness validation  
* Age range validation  
* Completion time checks  
* Prediction point validation (all 12 points required)  
* CGM data quality checks for uploads

### **9.2 Exclusion Criteria for Analysis**

### which methods 

* Segments with incomplete predictions (fewer than 12 points)  
* Segments with excessive missing CGM context data  
* Participants with fewer than 5 valid segments

---

## **10\. Risk-Benefit Analysis**

### **10.1 Risks to Participants**

#### **10.1.1 Physical Risks**

**None.** This is an online observational study with no physical interventions:

* No medical procedures  
* No medication administration  
* No in-person visits required  
* **No real-time health monitoring** \- all data is historical  
* **No connection to active medical devices** \- participants do not need to wear any equipment

#### **10.1.2 Psychological Risks**

**Minimal:**

* Possible frustration with prediction tasks (mitigated by clear instructions, practice trials)  
* Mild performance anxiety (mitigated by emphasizing research purpose)  
* Privacy concerns about sharing CGM data (mitigated by optional participation, full data protection explanation)

**Overall Assessment:** Risks comparable to taking an online quiz or survey.

### **10.2 Benefits**

**Direct Benefits to Participants:** None (research study only). Results do not constitute medical advice.

**Important Disclaimers Communicated to Participants:**

* Accuracy scores measure prediction performance only \- they have no diagnostic or therapeutic meaning  
* Results should not be used to adjust insulin dosing, dietary choices, or any medical decisions  
* Participants should continue to follow their healthcare provider's guidance independently

**Indirect Benefits:**

* Contribute to scientific knowledge  
* Personal insight into prediction ability  
* Support development of better glucose prediction tools


---

## **11\. Participant Protection and Ethics**

### **11.1 Informed Consent**

Important note- all consent will be given via click on corresponding checkboxes in the online interface and stored digitally. If the mandatory consent is not given, the participant is not allowed to proceed further, stopping any participation without consenting.

**Age Verification Gate:**

Before accessing any study content, participants must confirm they are 18 years or older:

* First screen displays: "This study is open to adults aged 18 and over. Please confirm your age to continue."  
* Two buttons: "I am 18 or older" (proceeds to consent) / "I am under 18" (displays message: "Thank you for your interest, but this study is only open to adults. Please close this page.")  
* If "under 18" is selected: No data is collected, session ends immediately, no cookies or identifiers stored  
* This age gate appears before any personal data collection

**Bilingual Consent Process:**

The study provides informed consent materials in both English and German. Participants select their preferred language at the start:

* **Language Selection:** Participants choose "English" or "Deutsch" on the landing page  
* **Complete Materials:** All consent information, study instructions, and feedback are displayed in the selected language  
* **Equivalent Content:** Both language versions contain identical information, ensuring equal understanding regardless of language preference

**Electronic Consent Form includes:**

* Clear study information in non-technical language  
* Emphasis on voluntary participation  
* Data protection and GDPR rights explanation  
* Withdrawal procedures and limitations (withdrawal possible until data anonymization)  
* Contact information

**Consent Checkboxes (mandatory):**

* I confirm I am 18 years or older, have read and understood the study information, and voluntarily agree to participate  
* I consent to data processing for research purposes and understand I can withdraw until data anonymization (GDPR Art. 6(1)(a), 9(2)(a))

**Optional Consent Checkboxes (clearly separated from study consent):**

* I agree to upload my own CGM data for the optional own-data task  
* I agree to be re-contacted for study results (email stored for this purpose only)

**Promotional Communications (Separate from Study Consent):**

Any opt-in for promotional communications about HEALES or related projects is:

* Presented on a SEPARATE page AFTER study completion (not during consent)  
* Clearly labeled as unrelated to study participation  
* Has no effect on study participation or data handling  
* Can be declined without any consequence

### **11.2 Compensation**

No monetary compensation. Non-monetary incentives include personalized accuracy feedback and shareable result card.

### **11.3 Insurance**

No study-specific insurance required due to minimal risk (online survey-equivalent).

---

## **12\. Timeline**

The study timeline is flexible and will be adjusted based on recruitment progress and operational needs. General phases include:

1. **Preparation:** Ethics submission, platform finalization, recruitment material preparation  
2. **Pilot Testing:** Small-scale testing with feedback collection  
3. **Recruitment and Data Collection:** Ongoing until target enrollment reached  
4. **Analysis:** Data processing, statistical analysis  
5. **Dissemination:** Manuscript preparation, publication, participant communication

Specific timelines will be determined based on ethics approval date and recruitment success.

---

## **13\. Limitations**

### **13.1 Selection Bias**

Participants are self-selected volunteers, which may not represent general CGM user population.

### **13.2 Academic vs Real-World Benchmarks**

While this study uses more realistic conditions than controlled academic datasets, online participants may still differ from typical CGM users.

### **13.3 Single Session Design**

No longitudinal follow-up; cannot assess learning effects over time.

---

## **14\. Contact Information**

**Principal Investigator:**

 Anton Kulaga  
 Institute for Biostatistics and Informatics in Medicine and Ageing Research (IBIMA)  
 University Medical Center Rostock  
 Email: anton.kulaga@uni-rostock.de

**Co-Investigators:**

Livia Zaharia, MSc  
 HEALES \- Healthy Life Extension Society  
 Email: [liviazaharia2020@gmail.com](mailto:liviazaharia2020@gmail.com)

**Biostatistical advisor:**

Benjamin Otte, MSc  
 Institute for Biostatistics and Informatics in Medicine and Ageing Research (IBIMA)  
 University Medical Center Rostock  
 Email: benjamin.otte@uni-rostock.de

**Data Manager:**  
 Nikolay Usanov, MSc  
 HEALES \- Healthy Life Extension Society  
 ML Engineer and Bioinformatician

**Advisory Board:**

* Prof. Georg Fullen \- University Medical Center Rostock  
* Irina Gaynanova, PhD (Statistical Advisor) \- Texas A\&M University  
* Renat Sergazinov, PhD (Technical Advisor) \- GlucoBench author

## References:

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

**Applicable Regulations:**

* GDPR / BDSG (data protection) \- YES  
* German research ethics guidelines \- YES  
* Medical device regulations (MDR) \- NOT applicable  
* AMG (pharmaceutical law) \- NOT applicable

---

**END OF DOCUMENT**

*For questions or clarifications, please contact:*  
 *Anton Kulaga: anton.kulaga@uni-rostock.de*  
 *Livia Zaharia: livia.zaharia@uni-rostock.de*

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAADBCAIAAACYB4kUAABE1klEQVR4Xu2dB5xURbr2Z1d33Xvv3m/v3l33GogzMAwZQYwYcF1zVgQBFUEkSM5ZVFQUc1xzWCNGXHVFTKyiIGAg5zR5OoeTQ31PVc00Pd0zwzCxe/r9/16aMxVOnVNvVT2nTsxiBEEQBJHxZCUGEARBEETmQXJIEARBECSHBEEQBEFySBAEQRCM5JAgCIIgGMkhQRAEQTCSQ4JoJCzLSgwiCCKFITkkMhRXIJcVRYktNwi6rlcnh/Hl1oxt24ZhJIbWiOM4yFXD+k3TRBokwObVkIwgMhCSQyJDUbQo1GD8hEnZOZ1g7bNzFVV3oFbMsV0HUTD8x5cYk7IkVcRybNO2dNPALyJNy9ENC39g2bK5wsCyczrGpCamaggJhhSezLGlWMpfJKhIW47YDNazV++8zt1lKTHD9sSWUXRC7Ncrv5FFW3xzypHabFhmLNm3q77v2CmXr8Hmu8NLdBwo5cEtIIjMg+SQyFAgh916dG/XPmfvvgIIQyisQl1sCJFQQPxTNQN/SjnE9DFe1WJ6CeOqaLtIDIsFxsuhpmlyQUZ1697bFRIlVTASiVQkPAgS7Ny1p2NuXvcevaG1rlRQsXU8rwg5uAGWCW2WmxSTw1jpMZBX003so1uhqVhhLCW2JyE9QWQaJIdEhlJYXPQ/f/xTOMKna/H26mtvdOnaHfbmW29DNjBlhCx9sOyfHTp2QiASrF33Y9t22X899zypK5Cf7Tt24bd9doeff9koJSemScjYpm17GJa/X7O6a7cTOnTs0qpN68KiEoRccOHFiBoy9IaEbYN0Hd+qzZSp08+/4JJnn3shqmhIfMmll2NLFtx2e7fuPZ9/4SWIIsIX3n5nTodcbNsPa9dDLaUcPvrYE61at42tLTc3z+Pxbd6yo1NeFyT2Bfz+YCCvc1e5hdiAdu3atW17MD1BZCYkh0SGcuppZ57e78x4IZRzpjZtc9b8sM7j9UMnZs2ei5CcTl2Obd2u1BfsfsKJnbr26NnrxP0Hijp07LzornsxL2zdpt0pp57u8wcff+IpiJAr5ouQRixMnj6rdfsOBSWeRYuXdOraraCo8PEnnmmf3enV11+LaPofjz4mt0t31XTa5uT269cvftvcivklFK5tuw5RxcC2/e28i3I7df121fe7du9FQcFQBKX3O6O/bjhz5t6G7YlEdcghBA8Zczt1XvHZV3LH2rbJUaJGnxNP9QciCPAHfdiS7JxOWGdOh7y3lr6HeeqyZcswA47fBoLINEgOiQyl1wknjRk7QeiFvEToYE527HGtoBmWzSeFDz38KGaB0La/HNf6pVffsBmzoFK5nQ3TLS7xdu3Wq2NuF0wEoXzLP/sc+TEv7Nyl25ix4zBpk3LYs89JS99b9tmXK79f+yPkECGRqJHXuQcWNMs+rk37dT9v/Hj551+s/LZXr17xl+6279whZ6Kw9tm5a9f9jIXzzr+4cxeeVwR2ePqZ5+Tynr35w24aCTncsnVnTA4xiczt2AXRJ/Y5paTYi4VOnXoufft9XrQR1QxVymGr1u279+gdVysEkbmQHBIZysWXXNa1G1cXqIK8EUY3LMy65DJs5b+/7ZTXBQsd83p+8NG/IIewnNyuMnunTp1zc/MQCwXdsXO3nFliJjd4yI3iDGon/NmjZx/M3s46+1z8nnxKP1dMHOWJU9NiR//luL4nnYZJKuzcc89VVdWBIouioZSYVrbvmIeJKVaFSSECz7/gErnANyk377nnX8RCt159MGfdunMPdNoTCH+9cpUs2hWTWkw9//Tnv7iuq+t6mceHKeNxx7cOhaOYdGL2Kbf59//9h0653Vq3yg4GopUqiCAyDJJDIkOBErRrn3NC7xODoQjmgvgTszrIjLyohkDEHv2XY6AcHfO6f/DRx1IOMSOU2WNyiPRXXHm11xcQGsOnXJhcSk1C4l4n9I1EdUTBsH5xfpLP3mCt22Rv275b3LzDCgoKYveXQrqghbI4WEmpDyvBOuPlEGL24kuvfLp8xTnnXYg0m7fvOr5t9rZde6UcSp07+fQz3//nJ5hHYp3hcNgVt5veMmrM6DG3hiNKTA5hmmp16dyTLxFEBkNySGQoGPzfeHNp6zbtIBjQht59+sp5IeZPHTpiQta5o1A7BHbp2vNfyz+Vd5xCkAzDwiyudeu27dplIwgpH3n0ccwjkf70fmdquolZJtZgWs7+AwXHHHs81i/vYYEaYW1YgILu3rPv8iuuQjIYdHfgwIGs4h7Us8466/hWbaRQScOaVc04/4KL5MzS5dPQ7MefeAr6Km/hOenkU1HQvv35//5mFbZHpgmrxv8d32bX7r1MyC3yIiVMCLaLQl1x0hVraN2qfbu2HbBfomL4DJUgMhCSQyJD4bMi/eCjeJGoGv+nK06iyhBLXNTTdVVmM00+jQuHozDoCuTn5182hsL8KUZV10zbCoZDmsGnm7Coyu9clQ9IQAuhlLFnE13+sIfq8ot55Q85WIgUxD/2gFisUK4kokSxBkwooY7lczvxKH3saf3YsxN85YYNOYQqy1g5Q5WbIYUfc2KsB8vYo0hE3kfjkBwSGQvJIZGhQFf4/TNuuUi4lZ/nk4H4hZww/qS8GZMKzKIsy4GZQlQwddu+Y1csY3l2t/wB+fgnFLEUK0I3+UOKKERaDa+ScYXKlj9xKHLFG5BXHHlKsQq5WpTbo+cJr72+NLbS2KnReD2OrSSWiuSQyFhIDgmiXuTk5Pzyyy/ViVlz0a1bN/koYfIrbwiCqBKSQ4KoO/Ezs8oxzY9hGNgqkkOCqCUkhwRBEARBckgQBEEQJIcEcZg4NrN03fSLl9REFZO5zIjqpo6/LNUIM6YjxLIikYhH4/fNOCUOv6GGuYZrGsy2XWYqluXarMhkUVcJWQ6/P8awdVPja3RUy40wFrItTWdMY8xkNn+SEesxWTBQxu/McRDN+DPzrqPx8lhY8Yf5Q4r0zSaCqDskhwRxOLiOxbjKLd+0992P1xni/TIQK93F/yyiR22GBKzIW1bo8WhCMjtdOFKxK27ghPAxp8AXRvg5g2+xXE2zWVizIiEVqwqFDIhtwDAhb0hwIOJ8s2GrxhzN53/11Vd6nDda1/mDGVhJ33MuCvEnQPR+F93sN9n6X3aPnPNEMJqKlzAJIl0gOSSIw8F1dNc2TXbluNvOvXx8mcOuvn4WJmpBxvpfOh36t+2A56Jrx+HPu556+7QrRhWEWOfLZ5xwzjVlOoPyQTjPu3ooZnIX3jC59xWjDZVFLHbG4NHDxkwp0tnKH7ecff6IN1dsR4Lvtxa/9dWWNTuLS22TPznBnJOvnGGJxx+jKp8aKq6lqurkRYt9mKQyt9+gERBOkkOCqDMkhwRxOLiO5liK4rzz3cbx0+/32Gx3CStT2bbSyPnXLCjwsh+27rvw2jGYuo2Ydnf/gRP2erQTBszcWmKeeuEgi7+527zkurFlFut72fA+Ayd/+e2GUp2dduOUoMVmLH4OInfZ4LH/+GTL/rC53+/ujbIftuXnKxpU1La0LufczNeghn/aVqqJeabjsmmLHoP0nnXxdT7xRjeSQ4KoMySHBHFYODrj1wu3lvmDPv2nbbsL/ZHvf97sN6wSVVVsFjLZ7qJAlBnf/fhLkcF27S/4fGdw477SX/YU28wJRrwXXD3mq3V7DZt9vnFnMFL2zfota7cfMBlbuOQtiFzY8X27KR8pv1y1drfPLA6rO0r9keKQq/g/+Ha36UAxzX4XDxMvrcHEEpPR/FKTrVy7fvXOUkWJkBwSRJ0hOSSIpsAVszfTZedecGFUL3+nWowzLxkoLzQKDv1eGJI9gmhwSA4JoimQcshvPxULCSDQEK+FOySWxUWT5JAgGhySQ4JoItw4S8S1uNViXkgQRCNBckgQTYZ8QXaVr8muMpAgiKaD5JAgmoxq5VB+6beKWSNBEE1FFv8oDEEQBEFkKiSHBEEQBOHKT9PQyVKCIAgio5Hf3yY5JAiCIDIaOUEkOSSIulL+zAR/YLDqxydqTUJe8WcVd9wQBNEYuOJD2SSHBFFX4p4irKccJsBX1bBrJAiiekgOCaJhqJDF+kzmDuYlESSIJobkkCDqjuNYtm1GdSOqWxZ6E3Pc2DtH64Br6ZrC/2fMdpihq6Gw+LQhhyulm/RWNsMwYoHJsQRBHBZ0Kw1B1BknFPa1z+18xz33hVXNYSYsdt/24aKGfFDEDh1yh98yJqLpjFl9TzkjGNGhi1x5HWfZsmVFRUU4gMWyZVlfffUVlpnow664C0AuJG4jQRC1wyU5JIjDovyKHv9nQqhee/vtk88+wxMK7dmbf+wxrXM6tMUMsXV2x5yOHdq1OlZj9phhQyxHP++Soce3+vOfWiFJu1G3joPatWnXtmv3bkcf9xdoWqv2nYSyObnZOf979HEQw40/r2zdpp1m2Z+t+LhXz67z59/bPq99Tm7XqBI44/wL73toyd59hZqtdu97Srdu3S686NzjW7U3bGa4ZsLWEgRRS0gOCeLwiMmha6l+v1c1rYceedjnD2bndhbfqbByu3QNqYZhmR3atVYYu2nodQEl0ib3VN2K6qaydduOnE5djm/bTq4ntysXwhNO6udADA29fes2+wqKQ4bdvWuPY1q1DSpGx7zuqhbu3euMa4cMMEymGxGdv87N+vmXLa2zW4VN2zCM9tmtTEu+5q0+Fy8JIqMhOSSIwyN+dpid3Y7fP2PZ3br16H7CiYGopumRDnmdMUE0batbXscy2z6heze/pp554fUus+6+a6HrsrbtOnTt1ScSVTVDD6nhEaNGR/nXDy3m2h2ycxRFOb3/WflFWrucPF9Qadu+BzKqKrv6mssV1TIdlX8KylY2bdyWk9s2atiapqG02xbeFYpaJIcEUWdIDgni8IjJoRL2deyYY5o2OPXU00NBpUfPPpdceoGY7Z06ZdpUJeRv1TXv1ltGQMDOu+ymcMSX17nDtdcOym6f6/UFTjn19OuGDMakrlW79uIOHMu1neOPbWVoeofcHMVkrdu2cRznwP6iVu2PX7DgPiTokNNZd1SVXzI0t2/dwZgO6Z08eXLXbrkDrh1Cs0OCqA8khwRx2FTMDvnnCR2XTwQNw+IhXIwQwM9bRiKRUNBvIMgxMb3TbcQbiIpGVTWqiU8bMsuxx0+ZMGjwdTx92I8UkVDUsfn6bGbq0ZC4PImsjsmvCVo2PyNqmZbDw8X0lJfJ76IxDBFgWHr8dhIEUXtIDgmieTCFxDGhZ5VjCIJoBkgOCaKZUVWVFJEgmh2SQ4IgCCKjkQ/skhwSBEEQGUr8myuqkEPbFfcC8Hf0M9NiujDLZvwhX5svyOXYglxuvNgqAym2htgqAyn2kIEUW0NslYEUW0NslYEUe8jAJouV0sbfrGi7umHxu9LcpM//ylCPN3Qgv1C3+W1tulyFIyy2nBDYeLFVBlJsDbFVBlLsIQMptobYKgMptobYKgMp9pCBTRUrpQ16t2Xr9qiiVSuHmu6UlgXEBNGpsNiyfO4qfqGxY6sMpNgaYqsMpNhDBlJsDbFVBlJsDbFVBlLsIQObOhZTw0iUvy7fSZZD23VUzZY5CYIgCKKl4oiTpVu37XD5g71VXTuMKvzxXpJDgiAIogUDOYTSbdy0BQu2kzg7dGzbVKKGI95GTBBEM+HEGZE6xPuFXNMCcCyb/bJlh4UZoGORHBJECkJjbmpCctjCqKscuuIBDHn9Uc4xyZrXDvqi+u++WjaPI0s1AzV4DcS+6Jucl6y5zGHcHfLXqmqUrPAYjZMpZNIRsZGwMnWVQ4R5g5F9BcXS9heWkDWvVfii0DD4J4KqxHD4q6aR+EBRaX5xWfJKyJrFysq8Ho9H+qhKXXQcFgpFSks9+QWJecmaz4ryi0tU07LEeJgMXKmqqt/vp3EydUw6otjjt/kb8RPm9HWVQ18oqppOzDTLJWteq/CFhe5XnSLCk4WlXiTmz486LHklZM1iqqrDZUVFRVW+sBRhwWBYpLEMMzEvWXOZYpgYT4s9Xv6ZkkSncSCHgUDAtm0aJ1PNMPpJRaxMXeXwQLFHMWy+XtMmSynj/tbLv5CQgHznQnIWsuY107Y03S4q9orzaYlDq+06hUUew2TJGcma0ywdRyfyc1qWU0WPgzfLX12SnJesua2ouDTpPAzJYYszksO0M5LDtDSSw3Q2ksODBlWAZmDBdlg4oqiaIS+uYsG0nOT0aWQtXg4VVYeP4Di5gJ2NRNVQOJqcMm3MQlN0oXktTw6xR/KtV/ARPIWFYCgi/0RTRHeDYSEt3Sfk0BQfe25hcog9QueSo6J8ZzX8hRD5xhb8IlyGJOdNFyM5PGhoqYbwuitezIOOCsPYCgf7AyEIZHKWdLEWL4dyeIWzsDswhGB/4TIEJidOD2u5coj2hj4F7+AXbsKv7HTSWRhqkUAOuMl5U91arhxC6tDL5JAoj2Pgo5ib5MwBCWDJedPFSA4r2Zix44pLypbc/+AXX36Nqpk8fQZ65rTpMydMmW6nY+essBYvh9NmTEc7hqdw4HL3Pfe++uZbH328fMTNow0nbVtjy5VDqXzjxk+UL0dGd8OcY/LkyQi8994lhUVlC26789aJkzDUJudNdWu5coijFmz+5CnTSn3+7Tt23bno7lAocuvEKdjTiZOmwFTNGj5i5KRp05PzpouRHB409My/nXfB4vsfGDlm7HMvvXxMq9bX3XATaqFjx44+1SI5TF2zzDeXvoF2/MyzL+HPjp27lfhC8++4uywQsdLXay1RDuUtfGhvuq536pzXtWcv3XbQ0YJRZdMv67x+T4/OPVXFaZvdSY4x6TeYtDw5tEygmfzUi6H6jmnTJrfHCT16983O7vDWG2/uLfGt/WlDu/Y5cBbaaK9evUojUdNglpG0nnQwksODBn9ffsVVbbJz0EVfX/r28W3btcnJXXz/Q3369CnyRbzBUHKWdLEWL4ffrV7Vuk27xx5/GrsZjGrZuZ0X3HGXLxQtKPEkJk4Xa9FyaBhGh9yOrdtnqyY/0LzimgE7t230B33MZmPHTO7ao0+xNwg/pt9g0lLl0HKFHIaOPva4niee7A1GsnM6/elPR/+//z26Q17XVu1yVNMJBKO5ublB0yI55KS7HJZ5fPjFbkc0XbNs7KLuME1888oT5JeIzaQs6WItXg7xY/ALGHwYktczXDEvlL9paS1aDplwkD8cQS9TDBM9jrkG1w+TYXaIuQi6XkTjo3DySlLaWp4cYp7AHWermoGt5zN728E4b7r8kWVVVSGN2J2wamCfbdvWGSM55KS7HLriDpqwqomzNFwOYTjkwfiqmPC0S3KYombhyJXfEizFD3sqL+wbFbdHpaW1XDnkrjEM3TRiHa3MH1Aj/ogSLi0oi4RN02GK6ablYNJy5ZBfO3T4MBiKhHEEA+dFNTRD/pn4El+I39eta9hBksNy0lQOVYvxFmzy8RTLEXHzBVc+y1RtHmhy0y2YUZ4Gv66hJq8qZa0FyKGs/KjtRvlQwodR6TXuFxOHMPpBwwzDtlVH0WxFnOrRuXPFOR+5kvSwliiHYqfkgsofqeDqiCmgzV0mu6GB3udi2TIV6TgZkrielLUWJ4cY/Rwdgx6c4mIBO6iJlim6ngLlE/1KEZ6CEPI5AzfutcRVpb6RHPINhv8wqhq8Z7oYTzFo8nFTdFTZDsQozFuAKU6jiyzpM7C2CDmUHUx0RUijHbX4ACp9IYZR0RW58QXoBBYMgwsn3Kdx+RS/aaQfLVMOuVpYGnM0ZulMHmiKXsXnH7wbilkFP9bRufvgNdXWYYnrSVlrcXIIF/C+huNLm3c62bNMXfQvceAiu5U8oIHhaBUm+2by2lLcSA5t0Rv1WLfEVMOS8wlTXkaWMomZYnl6OQSn1262ADksnyJYfJruiEkefOMYqvRU+TGpNEvF/mDANfl4yjPyI1xDXvpNH6+1SDnk9e9aBowrn+hxMco7oFyOJeACwzUmeVUpaS1SDm0XE0GYmBIIv4hDT+5NS8WC6GuYSKhyqOTHrLHTAGllJIc2fK2aVtjgVwpDYU3DMY7DD3DklN/il/rFk1KuqzNmiPcvGKKVJK8qZa0FyGH5xM7S+QUnxoKKeCM5P3/jhC34SA8pUfTDsKoojIVNJxqNoq0icRB91WKhQDDEL/cz+Rxx8vpTzlqiHPIphWVGHRM+UsWt+dybJuQBeynm7ox5/PwNNWHbUkzHF4o6Fgak9NnNFieH8FckEoKnvCFNUSJhzYLvTOaix/EHQ/kVepc5GBV1xeaDSUSJhiJhj9ePPdXEK4cSV5jCRnLIz79FXVYctZ966S3dYuu3l/7t6htCaK/86SjWf+CEaXc9FUHvtdlFg0aWaSzKp4sV08c0sRYgh+VDP449Get7/pBp9z5TZjK/xfpfM6IUmqeyqXMXy+OV/ldNuu/pD3SH2RZkg5102S2v/2tNYYidfMHg064ay8cp8dqaVLcWKYf8eqE5ZcGDJ58/unf/4UWBaKFX/fjz7+C4qGn6NdejsUK/Uurz975iysmXj7p1/hJERYz0eSFUy5ND095X7DvxsjGnD5jkV6zXPvym11nXBE3eIkuLwydcMGrqXY9FGTv/ulEnXzJqV6nxyIvvjJm5yGuwoTeNxMBCcpgOY02cRYMhjKHdzrv+nhdXBsLGFZMf3VTM75FyHGftpt0Pvb6qz6W3+By2vUA/6fKZQYxMqq3ZSjpdhWohcsgNEws4S7XcfgOnF+jGqRdM3BQM7Q+YTz7/Wp+rJvo0tmXzzj0R1n/QnBDjL227Zcbd+RY7d+At+POnfaZPTEH4CQF+upVfTUwuIlWsJcqhPIc2YOjEMGPoUyFT2V7KPlizWzX5+2Y9gfB+je3hDjIxv+993o1IZjiBqJo+u9ni5NA09VXrC3Zb/JbRb3/Z/sj7a7b7McXXQ2rwggGzihQ2aMw9EZud9beryxx+eNrvwiu7njt4yOTFinhQzXL49Yt0aagkh7ais3MvGbFHZ0teXfftuu2n3bDw9AG3bNxXgmF3+wHP6ReP63nBDVBH22YnXTHd5zJNY6qjpouDpbUAOeRXAS3VsiLoln0vHzb9gTdwTHrGVfN/DLv/3u6xmdN/6Pj9AX3nvoLBE+84Z8D0MpMfwb69/LsZdy+9cth8JH5+6aY+594QFWoqLkrxW6WSC0oVa6FyiEPJ+x57Ze79S7v3H1wSCeAw5cPVuyPi6QtbNzCGFhvM0aMlqjFo/H1+l98VpfPbipNWlZrW4uQQe7Rq/b4xi58/+fxhCx5/5apx9zzz8XfFNoswll+qdDzn5oEzXyq02Gufbc27cFyRwUoCGg5i7nvl81MvGgpvhlTRktPkUiLJoV3k0zDCQufufe4LLJwzeOEpl47OD7NrBo+dc8dTF90w86yhcwKMRXSr7yUTSg0jGnUxRxE3ViWuKmWtJcihuKXN0e0vV20et/j9u596Q2dOt9OHD1u4xMcPVtz+l92Afjhz7j0bfKzP+aMLdXfI6NknXTJwbYGZe+pgD3N/PGCePXBmEMew/MMJ/B4NeZ9qilpLlEPdNDQzcMo5Fz/w3PK/DpwSsXnX+/SHbSHLOfuyIcGIWRBk+QZTDXfpR1/sD7OIaxr4040krypFrSXK4ZPPLV3ywjs4lCzDLPDySWdcNarAYGdeNGzO/Ls/WbWj/1UTAqb9ylsrLrp+Pg5LVcW88PIhGwv0AoV988ueoMavFqfLzVAkh/w5woA3UuwNFHhFG4XyYcTU+QikWcwfYgd0VqzwR1ALIiyoBdHSSQ6bw3i7wo5gAC0LsxC/ESNsOCzMHF8UbdjxhvhNNN6yQJAxXQgI5vQewyhVGeJLIoX+KCvRwobLX1tTfrI0ldtqS5RDftXdikYUtr9U5dN0O6hr0Dy+eyUqf1FNWUDBganrusGgGcJsUTzWFnWS1pOy1gLl0ISP0JUCNrOZGTYYdxw6VBnzhy2Mizr3W8hX4t9XbO4tLoPvAqrrV1hZCN7jt0ql0R3dJIf8O6uOwd+loHDHmsy1XH4vGzNdR4eE6EFVvPTLUsNhhelGCIc/qi3ukUtaVcpaC5BDfheGrWJkjPL78A2PakbUQoe7RlX50MoVEL3U1kL8Vu+woYaLdQMDU8Syowy77vCLvvxQJqJjXXTtsNGspu7PH5ExTYcPrPCJzW8vdZk3xL8LFDRcVwthyPErFrMVW4VHwxa/K1iRL75ID2uJcmhjFDSNgPisoaLDe6qpew2NBXULgufTcFgTRl8L83u90VAdT1gvfy0UeqKm8IdKU7GhVmGZI4fiKZmDlpygJVsLkMOM82Czy6G85COMvzimeoslE7dbu2KrhIPELpSfK+PL8rxZnCUXmu7WIuQw0b9JCWplh+XruJQNU3qdLDXlsNajXmJ1J4yYtbSk1VayGlImr6q6lM1sqSWHB/tGcr3VUI01RCXE1hCVbAmJa8iYnKAxjddSs8phnPH2U63F0sjBq6oaq3Y0rCpxFVEJsTVE1Wx1zlhrSyc5rLYqElxcKfawRK6S1bbyk+SwthnrbykkhxiX5cuX0VZKfUFbTLzDEUUMB/w7yy4/Sc0/uxWJqrbDQ/gpF5c/CBiIqKrJz3Da/HsUJswVb99GslBY9fnDmm7jd8fOvQgJR3hGTyBc5g8ho/yEuj8Q4i244tXP/LxAVA2G+Bv3o7oVjJa/1zsYVWShZf6A4TB+g7go1ODbY4g18I10xdvA5S/Wr6j87IGqGdgdrFPuUaw4FI2tkoGKYfpCYcNxRbl8hagTWCAYro9opZAc8l4kntw0HIwaujhvhtrzhaJh1Sgq8yEEyzIcdSL9oosXXMJxpWV+0QZ4tWBt8jlf8Rwhr0mkkfUfCkcRBQ+i5uFl7L70lDcYQRPFMgKl45AYHpFtoLTMK70Q5yC+TmwqfuXXwBN3p/GsmeTQFX0NFShdgKpD+8eC7F+oPfkrO5qsVcsU3dCwQ4YVNfmrD3h3ELmwFx6v3+AKgf1g6G7oSrKfWrwgA50UbsUCqheNHB3E5s90q6L98zVIQwPgnVH0evRcFI1fhIcUHeHoWfJbwViQ3ufJvH6fPyjHDSwgSmzGwQ+eiIbU0C9kaHI5RDvHrqH1FpeUYXewv7IS8Is/UZ/yT4NfbuAuwJ+oXqRHHcoeoYlvjKAaZW/CL2peutgW4yRivb4A6k08DBPE0KfbvDEUlHhkFleMliga3Q2VDz+iFDgaw7jselgh6iQYUiJR3eXe5GM4Vit7MTwlB1jZMDAGFpV5MAZGeV2yEi+KK29y3OOiayMvdi25NuppKSSHUvnuvm+JfPddSDV13sRdNGUpCahuqTFYhmNQR4EoKplt273fEANGIKojF36REVKianZUKfcWRBG/GEyXf/YlulAY4yZjE6bOtMTYalS0Fd6IhTTC/SgLe+mP8N6L7Sn2BlGKwdh7H32EPh/W9aBi3HLrRFk0SgyG+NMXkShvfPB6bEgdM3acXEAIGooYu/mgg11AoQh56u/PyNLxD01Sd91te/bwDasYl2XLrs9YnGJyyF/mNGr0OHhHE8/zonrzS7xoP2WBiCcY5Y8r4UhIM+F66W78Kir+DMsKQXdCvcnwigMOdA8dHvf5I4iNHTzB0Fp9YZTA1wnDMryPUkz+og3edaVTDuQXynqI9fBAUMEWYs0hZBAqm7gvjWrNJ4eL7rpHjk3CNS50TrfKZYkPoAEE8IWwwj89YfNBgQ25cTi6RmEgGDKNGfPmoHeMGD0OVR1RwsNHjNJ0BwMNOnGFCxSunSrvKfAa95FiyqPJiZOmyD4uuxXGSPwqpoPBOuZQRXfQrSM6F2ZeRJR3bUN8vlsmQLPBn+jFslsZQiaxBvRQr6+8CaHq8FtS6kmugXpZk8uhPNQeecto1IM8dtTEe5dizdgVQ41cwBgr64QrTUUlo28gKDYAusLFfOgLwfnlh4wx27xtNzIuff+fnqCKfrpn736+p7aLzZAJ4D6pi7rwHXrx2IlTSnxBf4Df8AZ3o1uhN0kvo1BRIU5Et7785jtPMBKpOAa694EHudyJ/hvrvCYfB6SgWgWFxcm1UU9LITmUOoQqkB5CQ0ejl7Wwddfe+x54FN1g9PhJQ2+8edE998MT6zds2ZNfOvSmUVt37bP4Ay6mKRQRy3fd9+DAocOmz5o/5IYR46fMEMcU2k3DR2FX33zrPXTjhx7/uzekIAql7NpfvHtf8dyFd6/4+rupM+aHVHvObXeKcl2Dv2qYbwyKKyj2Pvb350aOHf/Bx5+u/O6HUeMmIe+NN48eOXYCtvP64aMjKosYhu7a33y3HpsaiGrLP1+Jg55xk6eh6wXC2qChI/fkF/ONUdS7779/5959gUh00X33LX7g4VDUuOu+ByZNn4Wtgspu2bnnu7U/3ffQY+8s+wiBnyz/EhuAyVNypdXSUkgOzfJTZ1dedc2Kz7/+4utVqFWMep999Q32/ZEnn8Ewt+DOe1DD//x0xZr1P+4rKAwoyu78/CdfeGnLvgP/ePMdaJ5pMPSc3fsKbfEADET0jaXvo7p+3rx9xZff8NMDBg5OldeXvv3MSy89/cIrWPNtixbjF2698trrMBAXewP7i0p/3rwNlVKM/Lp1oLgMa4b4LVx0D2Y5l1w7CH0YsT/8+Ata9cuvvSnHmsR9aTxrJjlEO8GgOXn6jO/X/Xz5NYN27itA80abxC8a/JvvLrvg0istfiLHxiHmuvU/zVlwO7xw0y1jv1m97skXXoYrN2zdASdePWjo2x98hKibR4/ZsmP3fQ8+hH3ILwsX+/lEwBcKf7z8sxVff4s+8szzr3y0/AuEjho7ccToW59+4eXCEl9hmR8lzrv9LjkIYDBAG37mxX9ccsV16I84mvnq29XYHozLqI3nnn8ReaHiI0eOhPehtS+//tab77z/1LMvoBti3EWXv2LAIHSl62+6Gd5f8fU3mKdCP/79zarkGqiXNbkcYlWffPaFPO3Bz1oFwjjawP6iEpZ/uXJ/QSkq9uEn/n7v/Y/cMmYCavK7tT9GVOtfn3+NOkQvw1wCW4kegEDUDMYZHKVgYeV3a5Z98hn0csDgG25fdO/No8b5Iyr6yIatOxH48WdfQtR8/AYaBg9CONFbZ8xdsOTBx75ZvfbJZ1/ASrDa0eMnW+IXEw/4C2PgrPm349hy/sK7nnvpZTgG4+Tg62++7Y570Tcxng8ZdvO7H36CLNdcd/2s+QuhxmMmTBk7cermHXvQwCyh32PHT8FOLX3/w8IyH9TUFOd1kqulbpZCcojW+cyzz2PiPGLU2HGTphoO6/+3C+BsrPDSK6955Im/DxxyAwwuX/HVvxH++tJ39+YXTZ0558cNm+Xs/soBg5ALC5jg79iz/54lD44ZP8kXit46ccr4CVP2HyhCH/565arb77i7qMx33fXDCku90Jh3Pvjng48+UezxP/PCy9itq6+9fuGdiyFUmmX6o+HBNw7fk19U5g89+dSzb737wa59+e99+PHm7btQIlaO9NiSiy67ssQT/Puzr+zNL1BNY8Cg6+FmbDZSDh02AgUh2bARo0eOnrz03Q9Xrvr28quv+ejT5T9v2vzw40+s+/kXlGuIo2yUgn3Hxm/Ysv3p51966LEn9xeW5BeXXXXtdejkfv6VscRKq6WllhwKGz5iJBRx+Rdfo/7h0+/X/gjnohLgiAV33IXZxkefrkBFFXu8E6dOG3zDjZ6IsuDuxcNGjsYo7PehT7moFllvt4wd//W338Oni+9/6Jvvf8DRhj8ceeeDZVj4+ttVqMw77r4XboK7LXF2aPANNyH7+l82ocKxrJpOSNGRDD3husF8G/yqPmL8BDQk2d5s/rn2gRCJUDiavCONZc0khzi0H3vr+GefewH1g363deceVCyqAoZhF3U4/JYx8vD82oHXrfpuNY7W0TghivsKitFE33j7PZs//blg0NAb0S/Cqjb8llGffLYC82v4UQyOU1GlW3fu2LBx87er19517/2ff/0NzORnhh4YdvOoV998+5pBQ9BxLrtqAALREtDXIpr63Q/r1/20acCgGzE3RbIvVn6LDoLOgtrYum0HtgGjx7Rp01C67Jibtu3ENuj8PkjeGTEITJw6A6u6aeTof634ssQbGHr9jXIe2ZDW5HKIPV25ajV+4RcctGEBtVfqC6KdI+TnTVtRgTjCQ7fSxZwedY6jBNTJ2AmT0cXgERwi4PeG4SNlU0fGITcOg+vfW/bJ5VcNHDj4pt37CzZu3YGoJQ89im4CL6PPYly1RV7UbTCqrf1pA9rJP95YCleiJcCVo26dgAWkQXdGB0QybI8trjTd//Bjyz7+FMtvvbNs8PXDDxR6ZXeGdxCONnbz6FuxzbJ3Y4gecN1Q9HEsXz1w8OhxE1EKhmJ0SUgG5LABh68UksOKc2LwGq8FOIwfwWlmQYnHFpcroHyxM8i2uKohw015XkX8KZs+VgEPIRx/Yg2oUHniGy1VnGfjR4yyUVrlZ6t5oTr/mjrDIUysCFS2HEDlxUjkleMCPxXull8gwcr5vM3hGTEKW/zltjZKQNHy4iJi+Ws1+GEXXxV/x7RhGo4rTwXIT0tje/gpXNVAermPcvPQ26XSoyrsekxNUlAOg6EIWjM2DHuNSv5p4xbsoOxjfLAQVSevoaJWIxqf9GviEgKciOYHj0jf2WIg+Oe/PuNeFp0HVRrVDf5a9vIvOfOV6OKD3bH2I12PuuWHnKLXwTxeTCkN3jb452e5RoqBmF+KxrI41VP3I5LDtmaSQ6OiJ6JCZCfCLwxNUVYUrx9xQswQh7C8Zx3sL7y7IYGsNKTHEYk3GMLBpc3r2TUdhlmIkCgLPsLAKusWC5boy4q4siu7Q6yDi8ZQfg4Nx53IDm2Da+T2uC6/bCwnCvIChzTEwmLrx9rQ+7CMEPQm7A5afsMf3zS9HDr8EgxaJh+ghOChZrCz8gI8amDClOmyN8GVqMydew/IwQQ+RUpVvCc9Ii4D86FbnIUSXuaDGObcfLKo6HIIQhRSYhlZkFKOorJEWRwMpcBkX8MakBcpESJrHo6Q3sHaRDNw1IrbL2xxNVr63RJtCdkRAq/JbZNqLT1ri56e0rPD/BKvHNmTi0lpS7xXqtKNTLEb58TDpOlqKSiHDWsJu1DjHlXyb1Js3VI2vOmmgYGkBjksKCxrJDlsQEu4S1B+gQvhOKyI9ax6Gh8oKxCDTw0uqzm2IazJ5TC272YDflRAjIQ63xmnkSqKj0jituTyD0IlJWgWIzm0q+kk5X/KThvrxjVZzKlVeveg3CZFNb61ADmULji0F4TVuEdVuruSVRR06JSNZy1SDi35YW1+xcupixxW1YNUi7/3RH6+WzywX4PLGt+hLUQOeWWKZb4vibENYRVyaGq2rqXM550bUg4xX5bnJ8lSzKxwOKyqaqLDBHBzqS+YlIWs2c0yXedAEb9dKLm3YVT1eIPoqJrOzy6SpY5hSiDP7/Ezzkm48r1IFo2TKWcRzSz2+FV+ESaeusqhJR5SKSz1kqWUFZeUhUL8e0dVYomHt5JzkTWvFZWVwmxxh7OYbFQCcigVsbCoLDkvWXNZUZkvv7gsIh7pq2qM5AQD0ZLixIxkzW7wnS2eFalMXeXQJUtVq4HkxGQpaOS1dLSqEXHJiclSxCpTVzkkCKJpqL73EikPuS2dqEkO+YeqSQ4JonkhOSSIpsGy3V+2bIccOo6TJIfyZaHirT+HiRNntSc+V6plTEhZy1wsKXETZ6w9h1VEPE2fsfbUuYj65zqsjLWnzkWkacaaSSiisTPWPmUCaZqxkahbEQ2yRzVldIUcbti42RHfSa1JDsXlfKt25sQfz9YjY3KC6qzSEXRSbA1W++1MKKKxMyZURYIlp68uY3KC6qzOGWu/bTVkrKEq6mN1K6LpG3Dtrc5F1Dlj3aqizhlrX/kN1UfqnDE5QXVW+yJqyFhDVSRb3TLWvvLrbHUuopEq34mzGuUQofLd54Z422/lnDVbwhYkJ6jS6paraTImpGzejMmJq8uYHFudHVYRzZux9lbnIuqWsW65DsvqXESLzJiQspa56pyx9ikzMGPtrW5F1C1XbTLGAnmCXbv5p5CqkENXKGJRcemB/EJL3KZvVbxih4yMjIyMrAWYnCcqqrll63b5kSwIX6IcSgzDCIVCHo+vTFj8glyOLRyM9XokYiEpttq8PP3BvImxVWZJLo6XWLvieMbabmpcMrkcl7eqNR8MrFRE5bzVbFX5QnnKKvLGZakib3yWxI2pJktycYmx1edtgspPzlvb2MoVmBhbZRa5UJFFbFhSbHV5D11c9XlrGXs4LaFSbPweHfTvofMmtsBaZClfaJBNTY6Nz3KwCLl8MG/Va64IjG1Vct5qt6pScYe1R0nFHTpL+UJ8cSlX+XWNrWqPDpGFL8RXYBXqUG3eWlS+x+uHBQIBXdcdh19frOJWmnj4y3MJgiAIomXhCFz+fvhySA4JgiCIjCNB6dgh5ZAgCIIgMgGIIskhQRAEkemQHBIEQRAEh+SQIAiCyGjkbTUkhwRBEEQmErunRtM0LodhgiAIgshgLMvicmgRBEEQROZhGIZpmliQc0Q6WUoQBEEQJIcEQRAEQXJIEARBECAr+Y01BEEQBNHiKX9jm3iFKaPZIUEQBJHhkBwSBEEQBIcewycIgiAIkkOCIAiCIDkkiBShNne0xS77HzIlQRCHC8khQdQP22LMsRkznHKNMgzDtm15ZV6iKIr8tSzDdh2RjL8FwxX/qaaBJUMJq5bLHFXnETp/oTBjpmky1zKNqK6bzGFIaFqRqKJFo1EUys21ULQtVkUQRH0gOSSI+uFyWZo8fdrOvfvefOttXdfRqTRNQwxEUVVVmQoaybjyWaZtGZapWXY4HHa5iNqWY/v9/r4n9II0GsFSKYeG6VqWFQwG+S1vruH1+jVFip6JHyiiWCsvWrcZjOSQIOoJySFB1A8hh7Pnz7v9rrv37juw+oc1uXmdPvt8Rbce3TERhLXLbt+mXVsE3nPPXZC6jp1yoX9LnnwuN7fDO++9+9e//nXhHbd/v2Z17x49DWiaHjo2p2Nu9rHHtc3p1asX1tynT9+cjtkrPv/6++83tmmTl9elY163npgOLr53yeLFi3Nzc2fNu41mhwRRf0gOCaJ+CDmcMmN6RNPvWXyfYmCqxr75/jvVNEJKVLPMPx/zfzY/Kerquvrkq+8efexxgUj0mXc+ze7QHrk7d8pr27YtkuW27+iPGMxRzzj/wp3bfsKk8rRTTv1u1UrH5edCNZOZNsvJhRBax7Ruf9pZf7WEBAaC4W69+pAcEkT9ITkkiPrh2ooSuXX8OMihblhde/bAXPDj5Z+aruMgznWOa9PasMzsDjlduuQFDNY+J/uY4459+o0Pu3bvYtt2p465hYWFx7ZudeapZ9h8bfopZ5/z44/fYR7ZpzefHR7Xpv0xrY7XLLdVmy5t23a2mdOpaw+kzOvc/cGHHundp+8bb77jkhwSRL0hOSSIemFZFlQtPkTe9ilvpUmIqpLYx2WQWC4nrzAWouv82qJpmvE37MTftkMQRN0gOSSIBiBewGIPQvD7QsVNNLGQhJQxGatONWUCmTeWJpZLrp+0kCAaBJJDgiAIgiA5JAiCIAiSQ4JoXMRlRP50oGlYtms5trztRZw5Fc/RVzbD0GCMnxrlSejlMwTRZJAcEkRjIuRQ0yOmhV/+BD0U0XYdr98Xk0DXtWNmWYZp6lhg/K4Zk+SQIJoMkkOCaEyEHFq2dvsdiwzTtR2mavxp+yFDbzAsU5olXkwjTdW1iBKV00eP1++49AQFQTQRJIcE0ZiUnyy1Hn7kMSy+9tY7mPftKygecuPw7bv3RHWDP2Jv2avXrcfC5u07DhQVW4y9+c67+DO/uEQ1+StJCYJoAkgOCaIxqZBD/F/mD4VUA2pXFgjjN6SotngDqVQ+/AYi0VfffGvVmh9s8VZuS/xCERPXSRBEI0BySBCNSqU7ZeIvEyaYaZqapuk6/5aFbZcHVmQkCKLRITkkiEYl8d7R6i3hYfxKUQRBNDYH5RBdUX6DxmlWcIyMbUoMbSZkzSSGEo0GWmBiENFUSDFODCWaEDkOJ4YSjUa5DFZQaXYYCoWgRok5mhZsULNvQ4zi4mJqnU0Galu+jSwxIr1htbYaMjY6mqYpgsQIoglB/cuz5UQTIIeamPyxeDmUKeAMs8Gw5X3kWEiMqREmXsZ4+CSWUlG6WBYbI0hMVgM7duzAMJEYmvLIPY3f/bRg586dmB2mY4UnE3uIQrS3WloCNUQ1PJYg3StfVnjdhp1UQL7APTE0FSmv24MDbMVok0bDToIWsoTZoSn8wZXjcEw+I6WoeiSq2k75N9iCUU2z+J0A+IUl56rOsIbkwNqY3AzLdlXNgKY7Lr8xzxcK+3wBwym/Sc8wXWGJeauzvfsO6MZhV0izmGk5+NV0E17QbQc7G1Y1/Jb6/MmJU9BQz7t275ULybGpbOFoyGWObjheX6DUU+ILBVXTMhw0exuWnD41DS1HNqH0sqii4ReDT/koZPATvlGdP50SUvTk9CluaPwYvpLDU8c0y+RDum674olYOc7IAccbDInKN9Ko5duVBbEB5LBTXpdp02f6/MHHHn+yz4knPfLo4x8s++euffkd8rp6g5Emk0PHUE/q22f67Hk5eT3yS7ztsztojtP31NNUVe/Ru68vFC3xBlqwHMLQkd559/1HH3ui/7kX+kOqari+oAJLTpmClr5yGFUj/f969qWXXbX43iW2a+0pDpaFDMNGb7KxJ8npU9PSVA7law2efOppLGzesm3cpKmeQBgDTlg1IlraVH7M0kAOTf4larGRysDrBl18+RWr162HHN734EOeQHDn3n1iCpSpcgj/ndj35LzOXbt07Q4txO/ceQvWrf9p6LAR4sDBaDI5ZK7VOS8XZT361POjx08+7/wLLfEgVySizJy7ABvjDystWw5xpPz2O+/ddffidjl5GI69gWgoalhuHeuziS195RASOG/B3OISL5pup865m3YXBTV+1Exy2AQmt/ne++7fs3f/Zyu+wOwQh+D8PJCDvq8mp09xSxc5tGzXtNQNmzY+8fQzbbJzzr/4khtH3AxR3LZrd6bLIdaYX1BkiKbJp88OKy4pQ3M0XYY5WZPJoSHOl2J7AsFwKBTBn1EMSPxrc/zMSVS3oM0tWA6xnTB51siuMDRKJU1G5PSVQ/y4zEHTx+EIFnyhIA6TQ4qaRoOCkbZyiNaOLUez93j9Lj9fx7XQ5u8ucEgOG8PkyVI0blMO/hXviyj2ePlpKIzAtpNGLb9aObTtiqujDYalm4bO12clxlQP1+M6kpCRywMfW4Xx5fI9O4z179+/PzGoCZHbf9BEZcZM7leVlpAxcb2pyo4dO+B9XdcTI1KARF8k+CV+Of7PGl2TWEZzI++mSQxNRaquzyqspi6TomialhiUclSq/+ockZgp9SpfPjVQtRwCdIYGlcO60HAdsgFqf+/evc04Oie2sJr6diU7VLtMUfbs2aMLEiNSgERf1NpqcE1iGc1K7JbyxIhUpOr6rMJq6jKpCLygqmpiaGqR2KSr80VivpSs/Movvqgsh/KpLyJGUVFRYlDzIe+di1kN1D5lSoG5eGJQypBQpTVUb+1jU4o07fvJ7qjB0oLku//ThRZQ2wflUL4LJj6uWUiQ63og324lrY4UFBQkBjUp8bvAr8tWbm2VY+NecelWtsS1piq7d+9O2UE5oUorV2+Cm2obm1hGsyJrPmXrvzJV12dVVnmMju8jFSSuu1nB9jTcANhIJDbp6nyRmK9S4lQhoQE0pBzGWlh9Glk9W0PcJvCm7zhWfWo/VeQQfZh/Kc+Nt4QXQGNPYeXL/H6mgxZXJ9WSWHJzkFJymFA/CVUab9I7MUuq/MpuqsoviWU3B3IzUmRjYsSqqDJV12dVVqnL2LYJq+gv5SQW2azwfavfAFh/Eis7kcQmXZ0vEvPFpUwssvlwG08OQc+ePVVVTQw9HOrZGuTtAMOGDVM0NRAK2tinekzcm1sOOdJhuq7bzDnrnPPFzsBN0Yim/rjhl+zcjrBrBg0sKCl+7a03bf5sSfiHH/nH83yh4NL33r348svWrFkzYMCABx54ID8/H3Wi2/x+MGR/8pmnsa7c3NzKBTYbKSWHqOSS4sLzzjtv9Zq1hml37NjRMIyysrL3338fUeGIPxiIomUtWDDv9DNO69y9G7wQjEa69eqJHXjw4YfQ6rx+nyvuu/OHQ2FVOaP/2Zpljh13KwJz8zqhfZ511ln173ENhaz5VKp/zu23345qnzBlMurQ5u+U8O7evw+VhkEmGo0uWbLk2kEDPQH/R5/+S8YWFxcj1ufz9e/ff+TIkaefdQ7C+//tghf/8TqGAr/fG4oamsme/vvjk6ZNHzj0RnQqdIbU2WcuGvUbABsETdMuvvhiLJxwwgmoLow8AcUTiAYV3Rk+fDhqfsuWLYjtd+YZHTvnoeVfeuUVIQXB0UgkgvrfuHGjx+PBbnz6+YpXXn/tpNNOtZgbUvTd+wtKvAHVdGx+R3BK0IhyCEeWlpYyMXYnxtWa+rcGeCUYDOqmMWfeXAw6pl33z8Wljhw+9dRTy7/8jD9KGNYwCzSs4D/eeH3WvLmPPfVkv7PPOvWMfqbrnH3uXxVD9wYDUESoHUZnVOXLr72K7L1798YYsXXrVgwKdvmd6Maa9esQ1a9fv4QSm4uUkkPT0GzL2Lx582WXX3npZVcgBF192bJl7777bjDot2xNVcwLzr/0kksuWfX9t9NmzUTNo9o/+Ww5dFLVtU1bNmNPoqqyYcvmGXNmwxe3TpwwadrUPfv2Tpg0cfUPa/Yd2I+xPrHU5iM15RDjMn4//ORjtGd5DLdxKx+IP/jgg0WLFg0ZMgTHHOMmTXz48ccQO3XmjBdffFFRFBwQT5gw4Y477rj86mtt8RjApm07sWNnnHF6WDGvG3oTc83J02fcMHzkvIV38kOWuo8QDUyKyKFsBhdddNHq1atRXdggk+kPPf7w60vfRbVjJFm8eDFcg0R53bru2LO7xMvFb8SIEcj16aef4vfll19GCJr9eRddOPyWkXNvW/D8y68uWrzkkSf+7g8rGSGHDUJDtQY3zupMKshhDCljFbvDPydbS0ughqjmJaXkMHaR45AVlVzhtbSUIjXlUFJDvdUQlRArkZ1IXOiKC0/O2UykiBzGU1FR5TVWVdShK7/mlM0IyeFhkMJy2AJJUzlMoOaeX0NU85LKctiAlMuh2MvyXU0lZ6SgHLZsSA4Pg1STQ3mM1lJJQzmsor/EN7zkjDVENS8ZIoflNz3G72UqOSMl5TC+kVfR4NOamuSwxXcGgiAIgqiSSnJYOYogCIIgWibJJ0QPyiFBEARBZCCxiwUkhwRBEETmgmmiruv4zZIvM5Uv8CUIgiCIDMG27Wg0GggEIILQxSwZGveab4IgCILICCzLit3Qm0X3lBIEQRCZieM4kEMpgnTtkCAIgiBIDgmCIAiC5JAgCIIgGMkhQRAEQTCSQ4IgCIJgJIdEBkJ3U1cH1QyRyZAcEplCxTBvag6LMBYVpgqLX5DLmRYbYrxOFFSPHY2vNILIHEgOicxBt8S4327k1/83d+d/z97DbdY+bvELcjmTYo+dvPP3M4r+PG1H2xlbQzRHJDIVkkMic1Atl+1h7DezWNbd7Ndzhc0RFr8glzMp9rfztKyF7Nfz3d8vNLa5JIdEhkJySGQKFjMxOzzA2H/M0I6Yq2TNZWTlNo9lzS9fzhd1RXJIZCAkh0SmYDMTvzvR6OcwTIb4L5mwI2exI2bDHOiiV9QVySGRgZAcEpmCeE2vk89PlhpHzjaTVaEBbHbFZGseO2KOfcQs9qs5ImSBeoSMqjDEZs1CMrEZC5zfzonwlAswS7OPmpm02sa3I+fofMNmO0WirkgOiQyE5JDIFMQAb+1jmAZpyXrQICamWU7WXDtrrsNDboscOUf97XQufr+aVVkO50agnb+aFxEyiSwQTgfZuaAmrbbRbS777WyVL8yySA6JjIXkkMgUmkAOMcM7crYN43/OZf81UzlCKtxtTtbtlRPza3W2lEY5Vf3j9NB/T2W/ncmaYXZIckgQJIdE5tAEcihPk0Jdfjc78KfZhUdMD/Dzn7drv5+q/gETxDlOzLJuY/8xV8maAqVE+nDW5JI/TAhmTYog/W9myPlihSWX0uBGckgQJIdE5tAUcjiX342SNc8583HPesa+stmRI7dct5L9dg6/Lhgvh39YqN/wKTtiTADpj5pjLPqe/RRmpYz1nPpl1tQykkOCaHpIDolMoSnkcD5XryNnmzd9pK4Js6wpnsd2M42x303fsMpmuxjrPs/6h8bWquzGN7ZrLsua9uOR4532CzfsM9kRk4r/NJtBjb5n7KhZB/Yy9v+mrdnN2E8WO3p6/r837XnLz343T0kssUGM5JAgSA6JzKEJ5JDfCzOTP8XxmwXs9yPXhCz2P1PWl6GbzfIveGfPOpv1HbP96T3sz9PNrLnGMg/LmuT79fzon+7cvNFiv5ru/nH+3vU6u/5Z1mvyqnEr3PsPsF1RLpDtp234cCv7zYxg1kRfcqENYCSHBEFySGQOTSCH/NaYBeoRc+xHi9kGxr5y2f9NKd7K2ImL1nsYW62xs2f//LKP/WEB+9+Ze9cydtzMPf85O3DEbGfet3zuuJ2xVrP3/2Fa0Y+M/WHG7g636wj8HMuzi9/YzH7VeLfYkBwSBMkhkTk0hRzOV/iDE7f5fnMb+814LFhZtyhZt+ZnzWe/nmVnzSjKuoNPH397p5G1iB01J/BfC6ysWex309hRtxf8zzQna4b6uwX2b2ew/5zOfj/TwgzyN3OsrLFbj5rO/nwnO2IWz5JYYoMYySFBkBwSmUMTyOGvZrMj5phQl1/fwf5zppm1QMm6PfD/ZrP/nFN0xCKWNUM7cg77n9nsN9O0I+bokL2sqZ6s2/jTh5DJP8z3/2a2eABjnpU1EyLqy1rA/mOuh0vpreav57Ojp3kb62U6JIcEQXJIZA4xOTxyjv6ruUmSkMk2D3VSLofFsq5IDonMg+SQyBRIDqs1kkOCIDkkMgeXm7mXsaPmW1mz3URJyGSrkMNfzXFKSQuJTIXkkMgU4meHiXqQ4VYhh0ctZAU2ySGRoZAcEpmDbjITcvjHSTuOnMn+a5YWs/+Yrf1uTrUWnzLBEjImJ6jO6pyx9ttWQ0aUXil2tnrUHOOoueoxU3+UJ0sJIgMhOSQyBT7ncW3XDUeYgUHfU9nKqreElDXkSk5QnaVURj9zEVLEWBTV5IQSK44gMgOSQyJT4GcALcYMpitcGl3mxBur3hJS1pArOUF1llIZeYjL60ZnTBMfSSaIDITkkMgUbGaK0R+YfCIkbq05aIl6EWcJKWvImBxbg9Ut42FtW3UZK0eJebMIt8URA0FkJCSHRObg8B+3fNC3mB5vdvWWkLKGXMkJqrOUyugy1WaqwUxLVA9BZCYkhwRBEARBckgQBEEQJIcEQRAEwUgOCYIgCIKRHBIEQRAEIzkkCIIgCPD/AdBXqWGikhpKAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,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>