# **Prédiction Humaine de la Glycémie de la Prochaine Heure à partir du Contexte Préalable du Capteur de Glucose en Continu (CGM) : Une Étude de Référence en Ligne**

**Protocole de l'étude**

**Investigateur Principal :** Anton Kulaga \- Institut de Biostatistique et d'Informatique en Médecine et Recherche sur le Vieillissement (IBIMA), Centre Médical Universitaire de Rostock, Rostock, Allemagne

**Co-investigateurs :** Livia Zaharia (HEALES \- Healthy Life Extension Society, Bruxelles, Belgique)

**Conseil biostatistique :** Benjamin Otte, M.Sc. \- Département de Biostatistique, Institut de Biostatistique et d'Informatique en Médecine et Recherche sur le Vieillissement (IBIMA), Centre Médical Universitaire de Rostock, Rostock, Allemagne

**Contexte du projet :** Cette étude est menée dans le cadre de l'Étude de Prédiction de Précision de la Glycémie Sugar-Sugar, soutenue par HEALES (Healthy Life Extension Society)

**Numéro d'enregistrement :** Réf. A 2026-0064  
**Reçu par le Comité d'Éthique :** 27 février 2026

---

## **Aperçu**

**Contexte :**

Les modèles d'apprentissage automatique pour la prédiction de la glycémie rapportent des métriques de précision dérivées de jeux de données académiques contrôlés, mais aucune référence n'existe pour la précision de prédiction humaine. Les utilisateurs de CGM anticipent régulièrement les niveaux futurs de glycémie dans le cadre de leur autogestion quotidienne, pourtant la qualité de cette prédiction n'a jamais été évaluée de manière systématique.

**Objectifs :**

(0) Quantifier la précision humaine dans la prédiction de la glycémie de la prochaine heure à partir de 3 heures d'historique CGM ;

(1) Comparer la précision de prédiction entre les personnes atteintes de diabète (PAD) de type 1 et type 2 et les personnes sans diabète, y compris les personnes en prédiabète, les utilisateurs bien-être et les utilisateurs sans expérience préalable (non-DM) ;

(2) Comparer la précision de prédiction entre les utilisateurs de CGM et les non-utilisateurs de CGM. Une personne est considérée comme utilisateur de CGM si elle en a utilisé un pendant plus d'un mois.

**Conception :**

Étude en ligne observationnelle transversale où les utilisateurs sont invités à faire des prédictions six fois ou plus, avec un plan d'échantillonnage adaptatif à deux étapes.

**Cadre :**

Plateforme basée sur le web (application Sugar-Sugar) hébergée par HEALES avec les données de recherche stockées au Centre Médical Universitaire de Rostock.

**Participants :**

N cible ≈200 adultes (≥18 ans) : environ 100 PAD et 100 non-PAD, recrutés via les réseaux sociaux et les organisations diabétiques. Le plan adaptatif permet un ajustement jusqu'à 150 par groupe sur la base d'une analyse intermédiaire. Pour le groupe non-DM, il y a des personnes qui utilisent leurs CGM pour le suivi de la condition physique, l'amélioration sportive, l'amélioration du style de vie, le biohacking, etc. qui ont montré un intérêt préliminaire à participer.

Les participants sont répartis en quatre groupes : Utilisateurs PAD CGM (groupe « PAD CGM »), PAD sans CGM (groupe « PAD sans-CGM »), Utilisateurs non-PAD CGM (p. ex., pour le bien-être, les sports, etc., groupe « non-PAD »), Utilisateurs non-PAD sans-CGM sans expérience préalable (groupe « SEP »)

**Procédures :**

Les participants disposant de données CGM sont encouragés à télécharger leurs propres données avec des mesures de glycémie antérieures (ci-après, données historiques pour être bref) pour la tâche de prédiction. La tâche consiste à prédire comment les valeurs de glycémie estimées par le CGM (ci-après, VG) évolueront en connaissant les valeurs précédentes. Dans le cas de notre application web, cela se fait de manière intuitive, en traçant la ligne sur un graphique VG. Pour plus de détails, consultez la section 4.2.

Les participants sans données CGM ou qui préfèrent ne pas en télécharger peuvent utiliser des données tierces provenant de jeux de données publics anonymisés disponibles gratuitement. Nous avons compilé la liste des jeux de données sur [https://github.com/GlucoseDAO/glucose\_data\_processing/blob/main/docs/datasets.csv](https://github.com/GlucoseDAO/glucose_data_processing/blob/main/docs/datasets.csv) où les jeux de données avec une colonne « Downloader » sont entièrement publics.

Chaque participant effectuera de 6 à 12 tâches de prédiction. Dans chaque tâche, il prédit ce qui se passera au cours de la prochaine heure en traçant des points sur un graphique affiché dans une application web. Concrètement, il prédit 12 points de données — un pour chaque intervalle de 5 minutes sur la période de 60 minutes. Pour les aider à faire ces prédictions, les participants se verront présenter les 3 heures précédentes de données comme contexte.

Plusieurs tentatives de prédiction par participant sont nécessaires pour obtenir des estimations fiables de précision au niveau individuel et une puissance statistique adéquate.

**Fiabilité de la mesure :** Une seule tentative de prédiction fournit une estimation peu fiable de la capacité individuelle en raison de la variation aléatoire (p. ex., difficulté du segment, moments d'inattention). La moyenne sur 6 à 12 tentatives produit des métriques de précision stables et reproductibles en réduisant l'erreur de mesure.

**Puissance statistique :** Le plan à mesures répétées augmente substantiellement la puissance statistique par rapport aux plans à tentative unique. Avec 200 participants réalisant chacun 10 tentatives, la taille d'échantillon effective pour les analyses intra-sujet approche 2 000 observations, permettant la détection de tailles d'effet petites à modérées (d de Cohen ≥ 0,3) qui nécessiteraient des tailles d'échantillon irréalisables dans les plans à tentative unique.

**Variabilité contextuelle :** Plusieurs tentatives permettent d'échantillonner à travers diverses dynamiques glycémiques (heure de la journée, direction de la tendance, contextes d'événements), assurant que les estimations de précision reflètent les performances dans des scénarios représentatifs plutôt qu'un cas atypique unique.

**Faisabilité :** La plage de 6 à 12 tentatives équilibre la précision de mesure avec la charge du participant. Les tests pilotes ont indiqué une participation soutenue pendant 15 à 20 minutes (environ 10 à 12 segments), après quoi les effets de fatigue peuvent compromettre la qualité des données.

Cette approche suit la pratique psychométrique standard pour établir des différences individuelles fiables dans les tâches cognitives et s'aligne avec les plans à mesures répétées couramment utilisés dans les études de référence sur les performances humaines.

**Mesures de résultats principaux :**

Nous mesurerons la précision des prédictions à l'aide de deux métriques standard : l'Erreur Absolue Moyenne (MAE) et la Racine de l'Erreur Quadratique Moyenne (RMSE), toutes deux mesurées en mg/dL. Ces métriques montreront dans quelle mesure les prédictions s'écartent des valeurs réelles de glycémie. Nous calculerons ces métriques à la fois pour les modèles d'apprentissage automatique et les prédictions des participants humains.

**Analyse statistique :**

Comparaison de groupe du MAE/RMSE par personne entre les PAD et les non-DM ; comparaison des prédictions humaines par rapport aux modèles de référence (persistance, extrapolation linéaire). Les analyses secondaires examinent les associations entre l'expérience et la précision. L'analyse prend en compte la structure des mesures répétées.

**Éthique et diffusion :**

Soumis au Comité d'Éthique, Centre Médical Universitaire de Rostock. Étude non interventionnelle utilisant uniquement des données historiques. Les résultats seront publiés dans des revues à comité de lecture.

---

## **1\. Contexte et Justification**

### **1.1 Contexte : Utilisateurs de CGM et Autoprédiction**

Les dispositifs de Surveillance Continue de la Glycémie (CGM) \[5\] fournissent des mesures de glycémie toutes les 5 minutes, générant des profils glycémiques détaillés sur 24 heures. La technologie CGM est utilisée par plusieurs populations :

**Personnes Atteintes de Diabète (PAD) :**

* Utilisent les données CGM pour informer leur propre dosage d'insuline, le calendrier des repas et les décisions d'activité
* Développent une reconnaissance intuitive des patterns grâce à l'expérience quotidienne avec leurs tendances glycémiques
* Prennent des décisions d'autogestion basées sur les trajectoires glycémiques anticipées

**Personnes Conscientes de leur Santé (Utilisateurs Bien-être) :**

* Personnes prédiabétiques qui surveillent leur glycémie pour l'optimisation du mode de vie
* Utilisateurs non diabétiques intéressés par la santé métabolique et la longévité
* Athlètes et biohackers qui suivent la réponse glycémique à l'alimentation et à l'exercice

Dans tous les cas, les utilisateurs font leurs propres prédictions sur les niveaux futurs de glycémie dans le cadre de leur autogestion quotidienne — cette étude quantifie cette capacité de prédiction.

### **1.2 Le Problème du Repère Manquant**

Les modèles d'apprentissage automatique actuels pour la prédiction glycémique rapportent des métriques techniques (RMSE, MAE) mais celles-ci sont dérivées de **jeux de données académiques contrôlés**. Selon GlucoBench \[1\], les modèles de pointe atteignent :

* **Prédictions à 30 minutes :** RMSE 8–12 mg/dL, MAE 6–10 mg/dL
* **Prédictions à 60 minutes :** RMSE 10–16 mg/dL, MAE 9–13 mg/dL

Cependant, ces métriques ont des limites importantes :

1. **Performance contrôlée vs. réelle :** Les références académiques utilisent des jeux de données organisés avec une qualité de données cohérente. Les vrais utilisateurs de CGM ont des lacunes, des erreurs de capteurs et un enregistrement d'événements incohérent.
2. **Pas de comparaison humaine :** Nous ne savons pas comment ces métriques ML se comparent à la capacité de prédiction que les utilisateurs expérimentés de CGM développent par une utilisation quotidienne.
3. **Diversité de la population :** Les jeux de données académiques se concentrent souvent sur des types spécifiques de diabète ; les vrais utilisateurs comprennent des populations diabétiques, prédiabétiques et bien-être avec différents contextes de prédiction.

**Cette étude comble l'écart** en établissant dans quelle mesure les vrais utilisateurs de CGM prédisent leur propre glycémie dans des conditions réalistes.
Veuillez consulter la section références pour plus de détails.

### **1.3 Lacune de Recherche et Innovation**

À notre connaissance, **aucune étude précédente n'a systématiquement quantifié la précision humaine dans la prédiction des trajectoires glycémiques de la prochaine heure**. Cette étude comble cette lacune critique en :

1. Établissant la précision de base d'autoprédiction humaine dans différentes populations d'utilisateurs
2. Comparant les performances entre les quatre groupes mentionnés ci-dessus : PAD CGM, PAD sans-CGM, non-PAD CGM et SEP
3. Examinant les facteurs associés à la précision de prédiction (durée du diabète, expérience CGM)
4. Créant un repère du monde réel qui complète les métriques ML dérivées en laboratoire

### **1.4 Justification de l'Étude**

Cette recherche est nécessaire parce que :

* **Aucune référence humaine n'existe :** Nous ne savons pas dans quelle mesure les utilisateurs expérimentés de CGM prédisent leur propre glycémie
* **Les références académiques sont trop optimistes :** Les métriques ML de jeux de données organisés ne reflètent pas les conditions de performance du monde réel
* **Populations d'utilisateurs diverses :** Les utilisateurs diabétiques, prédiabétiques et bien-être de CGM peuvent avoir différentes capacités de prédiction
* **Contexte d'autogestion :** Comprendre la capacité de prédiction humaine informe les attentes réalistes pour les outils assistés par IA

---

## **2\. Objectifs et Hypothèses de l'Étude**

### **2.1 Objectifs Primaires**

**Objectif 0 :**

Quantifier avec quelle précision les humains peuvent prédire les niveaux de glycémie pour la prochaine heure après avoir vu les 3 heures précédentes de données glycémiques, indépendamment de l'utilisation d'un CGM ou de la présence d'un diabète.

**Objectif 1 :**

Quantifier et comparer avec quelle précision les personnes atteintes de diabète (PAD) par rapport aux personnes sans diabète (non-PAD) peuvent prédire les niveaux de glycémie pour la prochaine heure après avoir vu les 3 heures précédentes de données glycémiques, indépendamment de l'utilisation d'un CGM (groupes CGM et non-CGM combinés par paires selon le statut diabétique).

**Objectif 2 :**

Quantifier et comparer la précision des personnes qui utilisent déjà des capteurs de glucose en continu par rapport aux personnes qui n'utilisent pas de CGM dans la prédiction des niveaux de glycémie pour la prochaine heure après avoir vu les 3 heures précédentes de données glycémiques, indépendamment de leur statut diabétique (groupes PAD et non-PAD combinés par paires selon l'expérience CGM)

### **2.2 Objectifs Secondaires**

**Objectif 3 :** Tester si une durée plus longue du diabète est associée à une meilleure précision de prédiction.

**Objectif 4 :** Tester si une expérience CGM plus longue est associée à une meilleure précision.

**Objectif 5 :** Comparer la précision lorsque les participants prédisent à l'aide de données génériques anonymisées par rapport à leurs propres données CGM (comparaison intra-sujet).

### **2.3 Hypothèses Formelles** Cette section présente uniquement les hypothèses — pour les méthodes de test statistique, veuillez consulter la Section 7\.

#### **Hypothèses Primaires**

**H1 (Différence de Groupe — Différentiateur Diabète Mellitus) :**

* Hypothèse nulle (H1.1) : MAE moyen des personnes atteintes de diabète \= MAE moyen des personnes sans diabète
* Hypothèse alternative (H1.2) : MAE moyen des personnes atteintes de diabète ≠ MAE moyen des personnes sans diabète — la direction est établie par comparaison

*Justification :* Les personnes atteintes de diabète ont une expérience vécue directe de la gestion de la variabilité glycémique et peuvent développer une reconnaissance intuitive des patterns grâce à l'utilisation quotidienne du CGM. Un MAE plus bas indique une meilleure précision de prédiction.

**H2 (Différence de Groupe — Différentiateur Utilisateur CGM) :**

* Hypothèse nulle (H2.1) : MAE moyen des personnes avec CGM \= MAE moyen des personnes sans CGM
* Hypothèse alternative (H2.2) : MAE moyen des personnes avec CGM ≠ MAE moyen des personnes sans CGM — la direction est établie par comparaison

*Justification :* GlucoBench \[1\] et les études connexes fournissent des points de référence : pour les prédictions à 60 minutes, les modèles simples atteignent un MAE ~12–20 mg/dL tandis que les modèles d'apprentissage profond (Transformer, Gluformer) atteignent un MAE ~11–17 mg/dL selon le jeu de données et les conditions. Nous nous attendons à ce que les performances humaines se situent quelque part dans cette plage. Cette comparaison établit où se situe l'intuition humaine par rapport aux approches algorithmiques.

#### **Hypothèses Secondaires**

**H3 (Effet de Durée) :**

* Hypothèse nulle (H3.0) : Il n'y a pas de relation entre la durée du diabète et le MAE (ρ \= 0)
* Hypothèse alternative (H3.1) : Il y a une relation négative entre la durée du diabète et le MAE (ρ \< 0), avec les effets les plus forts dans les 5 premières années

Une durée plus longue du diabète est associée à un plus grand nombre d'observations de valeurs glycémiques, couplées aux résultats, ce qui entraîne un MAE plus faible (meilleure précision). Celles-ci proviennent non seulement des lectures CGM mais aussi de l'expérience accumulée précédemment via les tests sanguins et l'observation d'événements tels que les repas, les injections, les sports et l'activité physique. Tous ces événements rendraient un diabétique plus ancien un prédicteur plus précis de la variation glycémique.

*Justification :* Les personnes qui vivent avec le diabète depuis plus longtemps ont accumulé plus d'expérience en observant comment leur glycémie répond aux repas, à l'insuline, à l'exercice, au stress et à d'autres facteurs. Cette exposition prolongée offre plus d'opportunités de reconnaître des patterns et de développer des compétences intuitives de prédiction.

Mention importante — la durée dans notre cas ne se corrélera qu'avec le temps avec le diabète, pas avec l'âge générique du participant — à ce titre, nous ne regrouperons pas les utilisateurs selon leur âge mais plutôt selon le temps réel avec cette condition. Cela ne sera pas non plus vérifié par rapport au nombre de participants (p. ex., en supposant que les personnes âgées ont plus d'expérience avec leur condition mais moins de participation globale à l'étude — cela conduirait à l'incertitude — nous nous soucions uniquement de la façon dont la durée de la condition reflète la précision de prédiction parmi ceux qui ont participé)

**H4 (Effet d'Expérience CGM) :**

* Hypothèse nulle (H4.0) : Il n'y a pas de relation entre la durée d'expérience CGM et le MAE (ρ \= 0)
* Hypothèse alternative (H4.1) : Il y a une relation négative entre la durée d'expérience CGM et le MAE (ρ \< 0), avec les effets les plus forts dans les 2 premières années

Une expérience CGM plus longue est associée à un MAE plus faible (meilleure précision).

*Justification :* Les utilisateurs de CGM prennent des décisions quotidiennes basées sur leurs tendances glycémiques — ajustant les doses d'insuline, programmant les repas et modifiant les activités. Cette boucle de rétroaction continue crée un environnement d'apprentissage naturel où les utilisateurs développent des compétences de reconnaissance des patterns grâce à la prise de décision répétée et à l'observation des résultats. Les utilisateurs qui portent un CGM depuis plus longtemps ont eu plus d'opportunités d'apprendre leur dynamique glycémique personnelle.

**H5 (Données Propres vs. Génériques) :**

* Hypothèse nulle (H5.1) : MAE moyen des personnes utilisant leurs propres données \= MAE moyen des personnes utilisant des données génériques
* Hypothèse alternative (H5.2) : MAE moyen des personnes utilisant leurs propres données ≠ MAE moyen des personnes utilisant des données génériques — la direction est établie par comparaison

Les participants ont un MAE plus faible (meilleure précision) lors de la prédiction de leurs propres patterns glycémiques par rapport aux données génériques. Cela sera mesuré en permettant aux participants de tester de deux façons — soit en utilisant un jeu de données générique, soit en téléchargeant leurs propres données pour prédire. Dans le second cas, les données seront anonymisées pour l'utilisateur (aucune date ne sera affichée — seulement l'heure — pour éviter de se souvenir de la date exacte) et seront représentées exactement comme dans le cas précédent graphiquement.

*Justification :* Les participants sont familiers avec leurs propres patterns glycémiques, leur mode de vie et leurs réponses typiques aux repas et aux activités. Cette connaissance personnelle devrait fournir un avantage lors de la prédiction de leurs propres données par rapport à des profils génériques inconnus.

**H6 (Humain vs. Modèles de Référence) :**
Nous émettons l'hypothèse que la précision de prédiction humaine (MAE) se situera entre des modèles de référence simples et des approches IA de pointe.

Les modèles de référence sont les méthodes de prédiction les plus simples possibles — ils ne nécessitent ni entraînement ni algorithmes complexes. Nos références comprennent : (1) modèle de persistance — en supposant que la glycémie reste constante à la dernière lecture, (2) extrapolation linéaire — traçant une ligne droite à travers les lectures récentes et l'étendant vers l'avant, et (3) ARIMA — une méthode statistique standard pour les données de séries temporelles.

Nous nous attendons à la hiérarchie de performance : références simples < prédictions humaines < modèles d'apprentissage profond (p. ex., LSTMs, Transformers). Nous testerons si les humains surpassent significativement les références et si l'apprentissage profond surpasse significativement les humains.

Cette hypothèse sera laissée pour la continuation de l'étude au moment où nous aurons un modèle bien défini — Pour le moment, aucun modèle n'est impliqué dans l'étude.

*Justification :* GlucoBench et les études connexes fournissent des points de référence : pour les prédictions à 60 minutes, les modèles simples atteignent un MAE ~12–20 mg/dL tandis que les modèles d'apprentissage profond (Transformer, Gluformer \[2,7,8\]) atteignent un MAE ~11–17 mg/dL selon le jeu de données et les conditions. Nous nous attendons à ce que les performances humaines se situent quelque part dans cette plage. Cette comparaison établit où se situe l'intuition humaine par rapport aux approches algorithmiques.

---

## **3\. Conception de l'Étude**

### **3.1 Type d'Étude**

**Conception :** Observationnelle, transversale avec des tâches de prédiction répétées. Pour plus de détails, veuillez consulter la Section 4.2  
**Collecte de données :** Plateforme en ligne basée sur le web  
**Suivi :** Aucun (participation en session unique)

### **3.2 Classification Réglementaire**

Cette étude est une **étude non interventionnelle, observationnelle** qui ne nécessite pas de supervision médicale ni de réglementation sur les dispositifs médicaux.

#### **3.2.1 Données Historiques Uniquement**

* Toutes les données CGM présentées aux participants sont des **données historiques, pré-enregistrées** — soit d'un jeu de données anonyme groupé, soit des propres fichiers CGM exportés précédemment du participant
* **Aucune surveillance glycémique en temps réel** n'est effectuée pendant l'étude
* **Aucune connexion à des dispositifs CGM actifs** — les participants n'ont pas besoin de porter ou d'utiliser d'équipement de surveillance pour cette étude
* L'étude analyse la précision de prédiction sur des segments de données passées, pas sur l'état de santé actuel

#### **3.2.2 Pas de Décisions Médicales ni de Diagnostics**

Cette étude ne fait explicitement **PAS** :

* Fournir de diagnostic ou de pronostic médical
* Faire de recommandations thérapeutiques ou de traitement
* Influencer des décisions cliniques ou des plans de traitement médical
* Offrir des conseils ou des orientations de santé personnalisés
* Générer des sorties destinées à un usage clinique

**Les résultats sont purement à des fins de référence de recherche** — les scores de précision indiquent uniquement les performances de prédiction et n'ont pas de signification diagnostique ou thérapeutique.

#### **3.2.3 Aucune Supervision Médicale Requise**

La supervision médicale n'est pas requise pour cette étude car :

* **Aucune intervention médicale** n'est administrée
* **Aucun test diagnostique** n'est effectué
* **Aucun résultat de santé** ne dépend de la participation ou des résultats
* **Aucune décision de traitement** n'est informée par l'étude
* L'activité est équivalente à **compléter une tâche cognitive en ligne ou un sondage**

### **3.3 Population de l'Étude**

#### **Critères d'Inclusion**

**Population Générale (Les Deux Groupes) :**

* Âge 18 ans ou plus
* Capable de fournir un consentement éclairé
* Accès à Internet et alphabétisation de base en informatique/mobile
* Prêt à compléter les tâches de prédiction

**Supplémentaire pour les Personnes Atteintes de Diabète (PAD) :**

* Diagnostic de diabète auto-déclaré (Type 1, Type 2 ou autre)
* Utilisation actuelle ou passée de CGM (tout dispositif)

---

## **4\. Flux de Travail du Participant et Procédures**

### **4.1 Stratégie de Recrutement**

**Canaux de Recrutement :**

1. Annonces sur les réseaux sociaux (Twitter/X, LinkedIn, groupes Facebook diabète)
2. Organisations de patients diabétiques et groupes de défense
3. Réseaux du conseil scientifique consultatif
4. Canaux communautaires (site web du projet, Telegram)
5. Conférences académiques (présentations lors de réunions sur la longévité/diabète)

Les matériaux de recrutement spécifiques seront développés après l'obtention de l'approbation éthique.

### **4.2 Procédures de l'Étude**

#### **Phase 1 : Consentement et Informations de Référence**

Les participants accèdent à l'application web Sugar-Sugar via une URL (adresse web) et complètent :

**1\. Consentement Éclairé Électronique**

* Feuille d'information sur l'étude
* Informations sur la protection des données (conformes au RGPD)
* Consentement par case à cocher pour la participation à l'étude et le traitement des données
* Consentements optionnels pour : télécharger ses propres données CGM, re-contact futur au cas où l'utilisateur souhaite connaître plus de détails sur les résultats de l'étude lorsqu'elle est terminée, communications promotionnelles

**2\. Questionnaire de Référence**
**(sera rempli par le participant, avec précision, selon ses connaissances)**

* Email (pour identification unique ; haché pour l'anonymisation)
* Âge (années)
* Sexe/genre
* Pays de résidence
* Statut diabétique (Oui/Non)
  * Si Oui : Type de diabète, années depuis le diagnostic
* Utilisation du CGM (Oui/Non)
  * Si Oui : années d'utilisation
* Poids optionnel (kg) et taille (cm)

**Note de Protection des Données :** Les emails sont hachés immédiatement lors de la soumission pour une identification unique sans stocker d'identifiants personnels. Les participants peuvent s'inscrire séparément pour les communications de re-contact.

#### **Phase 2 : Essais de Pratique**

2 essais de pratique optionnels pour familiariser les participants avec l'interface (les utilisateurs ont la possibilité de ne pas soumettre pour les 2 premiers essais). Les données des essais de pratique sont exclues de l'analyse.

#### **Phase 3 : Tâche de Prédiction de Données Génériques**

**Structure de la Tâche :**

* **Nombre d'essais :** 6–12 segments de prédiction par participant
* **Chaque segment :** Le participant trace 12 points de prédiction (intervalles de 5 minutes sur 60 minutes)
* **Fenêtre de contexte affichée :** 3 heures de données CGM (36 points à résolution de 5 minutes)
* **Source de données :** Données CGM désidentifiées du jeu de données organisé de l'étude

Les segments sont sélectionnés pour fournir un mélange équilibré de différentes heures de la journée, tendances glycémiques et contextes d'événements. L'ordre est randomisé entre les participants.

**Fonctionnalités de l'Interface :**

* Graphique interactif avec grille de temps de 5 minutes
* Les participants cliquent/tracent pour créer la courbe de prédiction
* Affichage des marqueurs d'événements (horodatages repas/insuline/exercice)
* Prédictions modifiables avant soumission

*Ci-dessous se trouve l'interface principale pour l'utilisateur après avoir rempli les formulaires de données et de consentement.*
*\-la ligne et le point bleus représentent les données historiques tracées pour le test*

*\-la ligne rouge représente les données prédites par l'utilisateur*

*\-il y a l'option de changer les unités de mesure — selon celles avec lesquelles le participant est le plus habitué*

*\-il y a des informations sur quel tour parmi les 12 c'est*

*\-l'utilisateur a deux options à tout moment pendant le test — soumettre ou simplement quitter*

*Après chaque tour, l'utilisateur reçoit un écran comme suit :*

*\-il y a des informations sur quel tour c'était*

*\-il y a une comparaison des données — la ligne bleue est montrée complètement*

*\-il y a les résultats d'édition numérique*

*\-ainsi que le résultat statistique pour ce tour*

*\-l'utilisateur a à nouveau la possibilité de quitter ou de continuer au tour suivant*

*À la fin de l'essai (max. 12 tours), l'utilisateur reçoit cet écran où toutes les données sont compilées pour l'ensemble de l'essai. Ci-dessous deux exemples — un dans lequel l'utilisateur n'a fait qu'un seul tour et un dans lequel l'utilisateur a fait plusieurs tours. Comme on peut le voir, il contient :*
*\-métriques de précision*

*\-unités dans lesquelles il a été exécuté*

*\-valeurs par tour*

*\-classement ![][image1]*

![][image2]

#### **Phase 4 : Téléchargement de Données Propres et Tâche (Optionnelle)**

**Éligibilité :** Participants qui ont indiqué leur volonté de télécharger des données CGM

**Processus de Téléchargement de Données :**

1. Télécharger le fichier d'exportation CGM (format CSV ou JSON des dispositifs pris en charge, ou exportation Nightscout)
2. Vérifications de qualité automatisées (minimum 5 jours consécutifs, validation des données)
3. Traitement des données dans lequel nous convertissons du format de dispositif pris en charge au format uniforme que nous utilisons pour la sortie de données
4. Pseudonymisation des données et stockage sécurisé

**Tâche de Prédiction de Données Propres :**

* 6–12 segments échantillonnés à partir des propres données CGM du participant
* Segments anonymisés (aucune date/heure affichée)
* Permet une comparaison intra-sujet de la précision sur les données propres vs. génériques

#### **Phase 5 : Complétion et Retour d'Information**

**Bref Rappel de Sécurité (Première Vue Uniquement) :**

Lors de la première participation, un bref avis est affiché avant les résultats :

**À des fins de recherche uniquement** — Ces scores mesurent les performances de reconnaissance des patterns, pas la capacité médicale. Continuez à suivre les conseils de votre professionnel de santé.

Cet avis est affiché une fois par utilisateur ; les utilisateurs récurrents voient les résultats directement.

**Affichage des Résultats (affiché par défaut) :**

* Résumé de précision personnel (MAE en mg/dL)
* Rang percentile comparé aux autres participants sur la base du stockage actuel de la base de données au moment de la participation de l'utilisateur. En bref, nous avons un stockage de classement séparé — nous n'avons besoin que d'un ID d'utilisateur anonymisé et d'un rang — à partir de là, vous connaissez le nombre total de participants et leurs performances
* Comparaison visuelle des prédictions vs. trajectoires réelles
* Option « Passer et terminer » disponible mais pas proéminente

**Carte de Résultat Partageable (Contenu Contrôlé par l'Utilisateur) :**

Les utilisateurs peuvent créer et partager une carte de résultat avec un contenu personnalisable :

* **Toujours inclus :** « J'ai participé à l'étude de prédiction de glycémie Sugar-Sugar »
* **L'utilisateur peut choisir d'inclure :** percentile de précision, score MAE, nombre de segments complétés, comparaison avec d'autres participants
* **L'utilisateur contrôle ce qu'il partage** — la gamification est une caractéristique clé d'engagement
* Les utilisateurs sont informés que le partage peut révéler leur intérêt pour les sujets glycémie/diabète

**Pas de Conseil Médical :** Les résultats sont présentés comme des métriques de performance de jeu/recherche, pas comme des évaluations de santé.

---

## **5\. Collecte et Gestion des Données**

### **5.1 Catégories de Données**

**Données de Référence :** Données démographiques et utilisateurs telles que :

* Email (pour identification unique ; haché pour l'anonymisation)
* Âge (années)
* Sexe/genre
* Pays de résidence
* Statut diabétique (Oui/Non)
  * Si Oui : Type de diabète, années depuis le diagnostic
* Utilisation du CGM (Oui/Non)
  * Si Oui : années d'utilisation
* Poids optionnel (kg) et taille (cm)

**Préférences de Consentement :**

* pour la participation à l'étude et le traitement des données
* pour : télécharger ses propres données CGM, re-contact futur au cas où l'utilisateur souhaite connaître plus de détails sur les résultats de l'étude lorsqu'elle est terminée, communications promotionnelles

**Données du Graphique :**

6–12 segments par participant, chacun contenant

**Données de Prédiction :** 12 points de prédiction (incluant la valeur glycémique et l'horodatage),

**Données de Vérité Terrain :** 12 valeurs CGM réelles pour évaluation (non montrées aux participants jusqu'après la soumission, incluant la valeur glycémique et l'horodatage)

**Données de Résultat :**

Valeurs MAE, MSI, RSME, MAPE

### **5.2 Protection des Données et Conformité au RGPD**

#### **5.2.1 Responsable du Traitement, Sous-traitant et Architecture**

**Responsable du Traitement :** L'Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA) à l'Universitätsmedizin Rostock (UMR) est le responsable du traitement des données pour cette étude.

**Implications de cet arrangement :**

* IBIMA/UMR assume l'entière responsabilité de la conformité au RGPD et des droits des participants
* Toutes les demandes des personnes concernées (accès, suppression, retrait) sont traitées par l'équipe d'étude à l'IBIMA

**Sous-traitant :** HEALES (Healthy Life Extension Society) exploitera l'application web Sugar-Sugar en tant que sous-traitant dans le cadre d'un Accord de Traitement des Données (ATD) avec UMR.

**Architecture Technique : Modèle Pull**

L'étude utilise une architecture « modèle pull » axée sur la sécurité :

\[Participant\] → \[App Sugar-Sugar (serveurs HEALES)\] ← \[Collecteur de Données UMR\]

                         ↓                                    ↑

                   \[Cache Temporaire\] ──────────────────→ \[Base de Données de Recherche (UMR)\]

**Comment ça fonctionne :**

1. Le participant interagit avec l'app Sugar-Sugar hébergée sur les serveurs HEALES
2. Les données de session complétées sont chiffrées et temporairement mises en cache sur les serveurs HEALES
3. Le système de collecte de données UMR **extrait** les données de HEALES périodiquement (toutes les 2 heures) et les déchiffre
4. Après un transfert réussi, le cache sur HEALES est effacé
5. Toutes les données de recherche persistantes sont stockées exclusivement sur les serveurs UMR
6. Aucune capacité de déchiffrement n'existe du côté HEALES, sécurisant le cache temporaire

**Avantages de sécurité :**

* La base de données de recherche UMR n'a pas d'accès entrant de systèmes externes
* HEALES ne peut pas « pousser » des données vers UMR — UMR initie tous les transferts de données, le flux de données est unidirectionnel par conception
* Le stockage temporaire de données chiffrées en cache sans clés de déchiffrement du côté HEALES atténue les risques d'accès non autorisé au cache
* Surface d'attaque réduite sur l'infrastructure de données de recherche
* Séparation claire entre la couche application (HEALES) et le stockage des données (UMR)

**Cache temporaire sur les serveurs HEALES :**

* Contient uniquement les données de session complétées en attente de transfert, sous forme chiffrée
* Rétention maximale : 7 jours (supprimé automatiquement si l'extraction échoue)
* Chiffré au repos
* Pas d'accès direct au cache sauf par le système d'extraction automatisé
* Le cache est un traitement transitoire, pas un stockage persistant

**L'Accord de Traitement des Données (ATD) spécifie :**

* HEALES traite les données uniquement selon les instructions d'UMR
* Pas de stockage persistant des données de recherche sur les serveurs HEALES
* Pas de stockage non chiffré des données de recherche sur les serveurs HEALES
* Cache effacé immédiatement après une extraction réussie vers UMR
* Suppression automatique du cache après 7 jours indépendamment du statut d'extraction
* Mesures de sécurité pour le cache temporaire (chiffrement, contrôles d'accès)
* Droits d'audit pour UMR
* Accès du personnel HEALES limité à la maintenance technique uniquement

**Pas d'autres sous-traitants externes :**

* Aucun service externe d'analyse, CDN ou tiers ne traite les données des participants
* Les membres de la communauté HEALES (autres que l'équipe d'étude listée) n'ont pas accès aux données des participants

#### **5.2.2 Identification et Pseudonymisation**

**Ce qui est stocké et pourquoi :**

1. **Adresse email (texte clair, chiffré au repos) :** Stockée séparément des données de recherche uniquement à deux fins :
   * Permettre les demandes de retrait (le participant nous contacte, nous localisons et supprimons ses données)
   * Re-contact optionnel pour les résultats de l'étude (uniquement si le participant a opté pour cela)
2. **ID d'Étude :** Identifiant alphanumérique aléatoire assigné par hachage (p. ex., f5afc4cf-9881-467d-88a1-325eb9558baa) assigné à l'inscription
3. **Table de liaison :** Un fichier chiffré séparé mappant l'ID d'Étude ↔ Adresse email
   * Stocké sur une unité chiffrée séparée des données de recherche
   * Accès restreint à l'IP (Anton Kulaga) et co-IP uniquement
   * Objectif : Permettre le retrait et le re-contact optionnel
4. **Données de recherche :** Toutes les données de prédiction, téléchargements CGM, réponses aux questionnaires stockées pseudonymisées uniquement avec l'ID d'Étude (pas d'email, pas de nom)

**Clarification du Hachage :** Nous ne nous appuyons PAS sur le hachage de l'email pour la pseudonymisation. Le hachage est utilisé uniquement pour la détection des doublons lors de l'inscription (empêchant la même personne de s'inscrire deux fois). La table de liaison contient l'email réel à des fins de retrait/re-contact.

#### **5.2.3 Politique de Conservation et de Suppression**

| Type de Données | Période de Conservation | Déclencheur de Suppression |
| :---- | :---- | :---- |
| Adresses email | Jusqu'à la fin de l'étude + 12 mois | Table de liaison détruite après la période de grâce |
| Table de liaison | Fin de l'étude + 12 mois | Détruite, rendant les données entièrement anonymes |
| Données de recherche (pseudonymisées) | 10 ans selon les normes de recherche allemandes | N/A — conservées pour la reproductibilité |
| Fichiers CGM téléchargés | Traités immédiatement, fichiers bruts supprimés dans les 30 jours | Automatique après l'extraction des segments |

#### **5.2.4 Limitations du Retrait (Important)**

**Le retrait est possible à tout moment JUSQU'À la destruction de la table de liaison** (environ 12 mois après la fin de l'étude). Après ce point :

* Les données de recherche deviennent entièrement anonymes (aucune réidentification possible)
* Les demandes de retrait ne peuvent pas être satisfaites car nous ne pouvons pas identifier quelles données appartiennent au demandeur
* Cette limitation est clairement indiquée dans le formulaire de consentement

**Processus de retrait :**

1. Le participant envoie un email au coordinateur de l'étude demandant le retrait
2. Nous localisons son ID d'Étude via la table de liaison
3. Toutes les données de recherche associées à cet ID d'Étude sont définitivement supprimées
4. Confirmation envoyée au participant

#### **5.2.5 Transferts de Données Transfrontaliers**

**Aucune donnée ne quitte l'Union Européenne.**

* **Base de données de recherche UMR :** Située en Allemagne (UE)
* **Compte cloud géré par HEALES :** Situé dans l'UE (cache temporaire uniquement, max. 24 heures)
* Aucun service tiers ne transfère des données hors de l'UE
* Pas de CDN, d'analyses externes ou de services cloud avec des centres de données non-UE
* Les communications par email utilisent des fournisseurs d'email standard basés dans l'UE

Les participants hors UE peuvent participer, mais leurs données sont traitées et stockées exclusivement au sein de l'UE sous les protections du RGPD.

#### **5.2.6 Sécurité du Stockage des Données**

* **Emplacement de la base de données de recherche UMR :** Allemagne (UE)
* **Emplacement du cache temporaire HEALES :** UE
* **Chiffrement en transit :** TLS 1.3 (à la fois app-vers-utilisateur et extraction UMR-vers-HEALES)
* **Chiffrement au repos :** AES-256 (à la fois la base de données UMR et le cache HEALES)
* **Contrôles d'accès :** Basés sur les rôles ; données de recherche accessibles à l'équipe d'étude ; table de liaison accessible uniquement aux IPs
* **Sauvegarde :** Sauvegardes chiffrées quotidiennes dans l'UE (UMR uniquement ; le cache HEALES est transitoire)
* **Journalisation d'audit :** Tous les accès aux données enregistrés

---

## **6\. Mesures de Résultats et Métriques de Précision**

### **6.1 Métriques Primaires**

Nous utilisons des métriques standard de la littérature sur la prédiction glycémique \[1,9,10\], permettant une comparaison directe avec les benchmarks de modèles ML publiés (p. ex., GlucoBench — pour plus de détails voir la section Références).

**Erreur Absolue Moyenne (MAE) :** Moyenne de la différence absolue entre les valeurs de glycémie prédites et réelles (en mg/dL). Les valeurs plus basses indiquent une meilleure précision.

 MAE \= (1 / n) × Σ |prédit − réel|

* Mesure la taille typique des erreurs de prédiction
* Toutes les erreurs sont pondérées de manière égale
* Mêmes unités que la variable cible

**Racine de l'Erreur Quadratique Moyenne (RMSE) :** Racine carrée des différences quadratiques moyennes. Pénalise les erreurs plus grandes plus fortement que le MAE. Également reportée en mg/dL.

 RMSE \= sqrt(MSE)

* Même unité que la variable cible
* Pénalise les grandes erreurs comme le MSE
* Plus facile à interpréter que le MSE

**Erreur Quadratique Moyenne (MSE) :** La moyenne des différences quadratiques entre les valeurs prédites et réelles.

 MSE \= (1 / n) × Σ (prédit − réel)²

* Pénalise les grandes erreurs plus fortement
* Sensible aux valeurs aberrantes
* Les unités sont au carré, rendant l'interprétation directe plus difficile

**Erreur Absolue Moyenne en Pourcentage (MAPE) :** L'erreur absolue moyenne exprimée en pourcentage de la valeur réelle.

 MAPE \= (100 / n) × Σ |(prédit − réel) / réel|

* Mesure l'erreur relative
* Indépendante de l'échelle
* Peut être trompeuse lorsque les valeurs réelles sont proches de zéro

Ces métriques sont calculées :

* Par essai (sur les 12 points de prédiction)
* Par participant (en moyenne sur leurs 6–12 essais)
* Par groupe (pour les comparaisons de groupes)

### **6.2 Comparaisons avec les Modèles de Référence**

Pour contextualiser les performances humaines, nous comparons avec des modèles de référence simples en utilisant les mêmes segments de test :

* **Modèle de persistance :** Prédire que la glycémie reste constante à la dernière valeur observée
* **Extrapolation linéaire :** Projeter la tendance des 30 dernières minutes vers l'avant

Cela sera fait après la collecte des données pour fixer un point de départ pour la partie future de l'étude où nous intégrerons des modèles ML. Cela n'affectera pas la collecte de données à ce stade de l'étude. Pour plus de détails, consultez H6.

---

## **7\. Plan d'Analyse Statistique**

### **7.1 Aperçu**

L'étude collecte **plusieurs mesures par participant** (6–12 segments de prédiction chacun, avec 12 points par segment). L'analyse prend en compte cette structure de mesures répétées. Elle donne une vue plus précise de la compétence de prédiction du participant qu'une seule mesure.

### **7.2 Populations d'Analyse**

* **Analyse primaire :** Tous les participants complétant au moins 6 segments de données génériques analysables
* **Analyse de données propres :** Participants complétant au moins 6 segments de données propres
  Le nombre de segments de données proposés est dû à la variabilité attendue dans les métriques de précision (MAE/RMSE). D'après les données GlucoBench, l'écart-type pour la précision de prédiction est d'environ 0,18–0,22 sur une échelle de 0–1. S'il n'y avait que 2–3 mesures par personne, l'estimation de leur capacité aurait de larges intervalles de confiance.

## **7.3 Analyses Primaires**

### **H1 (Différence de Groupe — Statut Diabétique)**

**Objectif** : Comparer la précision de prédiction entre les personnes atteintes de diabète (PAD) et les personnes sans diabète (non-PAD).

**Résumé des Données** : Chaque participant prédira des valeurs de glycémie pour plusieurs points temporels à travers différentes présentations de traces de glycémie. Nous calculerons une valeur MAE par participant en faisant la moyenne de leurs erreurs de prédiction à travers toutes leurs prédictions. Cela nous donne un score de précision résumé par personne.

**Méthode Statistique** :

1. **Vérification de Normalité** : Nous testerons d'abord si les valeurs MAE sont distribuées normalement dans chaque groupe en utilisant le test de Shapiro-Wilk (p > 0,05 indique une distribution normale).
2. **Comparaison de Groupes** :
   * **Si les données sont distribuées normalement** (Shapiro-Wilk p > 0,05) : Nous utiliserons un **test t à échantillons indépendants**. Ce test compare le MAE moyen entre deux groupes en tenant compte de la variabilité au sein de chaque groupe et des tailles d'échantillon. Le test t calcule si la différence observée dans les moyennes est plus grande que ce que l'on attendrait par hasard seul.
   * **Si les données sont non normales** (Shapiro-Wilk p < 0,05) : Nous utiliserons le **test U de Mann-Whitney**. Ce test non paramétrique compare les groupes en classant tous les scores MAE du meilleur au pire (indépendamment du groupe), puis en testant si un groupe a tendance à avoir de meilleurs rangs que l'autre. Cette approche est robuste aux valeurs aberrantes et aux distributions asymétriques.
3. **Niveau de Signification** : α \= 0,05 (bilatéral)
4. **Taille de l'Effet** : Nous rapporterons le d de Cohen (pour le test t) ou la corrélation bisériale des rangs (pour Mann-Whitney) pour quantifier l'ampleur de la différence.

**Pourquoi cette approche** : Nous utilisons des statistiques de résumé par personne (un MAE par participant) plutôt que d'analyser des milliers de prédictions individuelles parce que les prédictions individuelles de la même personne ne sont pas indépendantes — elles sont influencées par la stratégie de prédiction cohérente de cette personne. Résumer à une valeur par personne garantit que nos tests statistiques satisfont le postulat d'observations indépendantes.

---

### **H2 (Différence de Groupe — Expérience CGM)**

**Objectif** : Comparer la précision de prédiction entre les personnes qui utilisent actuellement le CGM et les personnes qui n'ont jamais utilisé de CGM.

**Résumé des Données** : Identique à H1 — une valeur MAE par participant, en moyenne sur toutes leurs prédictions.

**Méthode Statistique** : Approche identique à H1 :

1. Test de Shapiro-Wilk pour évaluer la normalité
2. Test t à échantillons indépendants (si normal) ou test U de Mann-Whitney (si non normal)
3. Niveau de signification α \= 0,05 (bilatéral)
4. Rapporter la taille d'effet appropriée

**Justification** : Même logique que H1 — nous comparons deux groupes indépendants sur une seule mesure de précision par personne.

---

## **7.4 Analyses Secondaires**

### **H3 (Effet de Durée — Diabète)**

**Objectif** : Tester si une durée plus longue du diabète est associée à une meilleure précision de prédiction.

**Résumé des Données** : Pour chaque participant atteint de diabète, nous avons :

* **Variable prédictrice** : Durée du diabète en années (variable continue)
* **Variable de résultat** : MAE (une valeur par personne, calculée comme dans H1)

**Méthode Statistique** :

1. **Vérification de Normalité et de Linéarité** :
   * Créer un nuage de points de la durée du diabète (axe x) vs. MAE (axe y) pour inspecter visuellement la relation
   * Utiliser le test de Shapiro-Wilk pour vérifier si les valeurs MAE sont distribuées normalement
   * Examiner le nuage de points pour les patterns linéaires vs. courbés
2. **Analyse de Corrélation** :
   * **Si le MAE est distribué normalement ET la relation semble linéaire** : Utiliser le **coefficient de corrélation de Pearson (r)**. Celui-ci mesure la force et la direction d'une relation linéaire entre deux variables continues. Les valeurs vont de -1 (relation négative parfaite) à +1 (relation positive parfaite). Nous nous attendons à une corrélation négative (durée plus longue → MAE plus faible).
   * **Si le MAE est non normal OU la relation semble non linéaire** : Utiliser la **corrélation de rang de Spearman (ρ)**. Celle-ci fonctionne comme Pearson mais utilise des rangs au lieu de valeurs réelles, la rendant robuste aux valeurs aberrantes et capable de détecter les relations monotones (constamment croissantes ou décroissantes) même si elles ne sont pas parfaitement linéaires.
3. **Niveau de Signification** : α \= 0,05 (bilatéral)
4. **Analyse Exploratoire** : Parce que nous anticipons que la relation peut atteindre un plateau (grande amélioration dans les premières années, amélioration minimale après 5+ ans), nous procéderons en plus à :
   * Ajuster un modèle logarithmique : MAE \= β₀ \+ β₁·log(durée \+ 1)
   * Comparer l'ajustement linéaire vs. logarithmique en utilisant les valeurs R²
   * Créer une visualisation montrant comment le MAE change à travers les catégories de durée (<1 an, 1–5 ans, 5–10 ans, >10 ans)

**Pourquoi cette approche** : L'analyse de corrélation est appropriée lors de l'examen de la relation entre deux variables continues. Nous utilisons Spearman comme sauvegarde parce que les courbes d'apprentissage montrent souvent des rendements décroissants (patterns non linéaires), et Spearman peut détecter ces relations même lorsqu'elles ne sont pas des lignes parfaitement droites.

---

### **H4 (Effet d'Expérience CGM)**

**Objectif** : Tester si une expérience CGM plus longue est associée à une meilleure précision de prédiction parmi les utilisateurs de CGM.

**Résumé des Données** :

* **Variable prédictrice** : Expérience CGM en années (variable continue, uniquement pour les utilisateurs de CGM)
* **Variable de résultat** : MAE (une valeur par utilisateur CGM)

**Méthode Statistique** : Approche identique à H3 :

1. Visualisation du nuage de points et vérification de normalité (Shapiro-Wilk)
2. Corrélation de Pearson (si normal/linéaire) ou corrélation de Spearman (si non normal/non linéaire)
3. Modélisation logarithmique exploratoire pour tester les effets de plateau
4. Niveau de signification α \= 0,05

**Justification** : Même logique que H3 — nous nous attendons à ce que les utilisateurs de CGM montrent une amélioration rapide initialement, avec un apprentissage atteignant un plateau une fois qu'ils ont intériorisé les patterns glycémiques courants.

---

### **H5 (Données Propres vs. Données Génériques)**

**Objectif** : Tester si les participants font des prédictions plus précises lorsqu'ils voient leurs propres données de glycémie par rapport aux données génériques anonymisées.

**Résumé des Données** : Il s'agit d'une **comparaison intra-sujet**. Les participants qui complètent les deux conditions auront :

* **MAE des données propres** : Erreur moyenne sur toutes les prédictions sur leurs propres traces glycémiques personnelles
* **MAE des données génériques** : Erreur moyenne sur toutes les prédictions sur les traces anonymisées
* **Score de différence** : MAE générique − MAE propre (les valeurs positives indiquent de meilleures performances sur les données propres)

**Méthode Statistique** :

1. **Pourquoi l'analyse appariée** : Nous utilisons des tests « appariés » parce que nous avons **deux mesures de la même personne** (précision sur données propres vs. précision sur données génériques). Cela est fondamentalement différent de H1–H2 où nous comparons des personnes différentes. Les tests appariés tiennent compte du fait que la même personne apparaît dans les deux conditions, contrôlant les facteurs spécifiques à la personne comme la capacité générale de prédiction, l'attention, la motivation, etc.
2. **Vérification de Normalité** : Test de Shapiro-Wilk sur les **scores de différence** (pas sur les valeurs MAE brutes)
3. **Comparaison** :
   * **Si les scores de différence sont distribués normalement** : Utiliser le **test t à échantillons appariés**. Cela teste si la différence moyenne entre les conditions est significativement différente de zéro, tout en tenant compte de la corrélation intra-sujet.
   * **Si les scores de différence sont non normaux** : Utiliser le **test des rangs signés de Wilcoxon**. Il s'agit de l'équivalent non paramétrique du test t apparié — il classe les différences absolues et teste si les différences positives (meilleures performances sur les données propres) sont plus fréquentes que les négatives.
4. **Niveau de Signification** : α \= 0,05 (bilatéral)
5. **Taille de l'Effet** : Rapporter le d de Cohen pour plan apparié

**Pourquoi cette approche** : Les tests appariés sont plus puissants que les tests indépendants parce qu'ils suppriment la variabilité due aux différences individuelles. Si la Personne A est simplement naturellement meilleure dans les tâches de prédiction que la Personne B, cela n'a pas d'importance — nous nous soucions seulement de si chaque personne performe différemment à travers les deux types de données.

---

### **H6 (Humain vs. Modèles de Référence)**

**Note** : Cette hypothèse est différée pour des travaux futurs lorsque les modèles de référence seront implémentés. Lors de l'analyse, nous utiliserons des approches de comparaison appariée similaires, comparant le MAE de chaque participant au MAE atteint par les modèles computationnels sur les mêmes traces glycémiques.

---

## **Tableau Récapitulatif des Méthodes Statistiques**

| Hypothèse | Type de Comparaison | Test Primaire | Test Alternatif | Quand Utiliser l'Alternatif |
| ----- | ----- | ----- | ----- | ----- |
| H1 | Groupes indépendants (PAD vs. non-PAD) | Test t indépendant | U de Mann-Whitney | Shapiro-Wilk p < 0,05 |
| H2 | Groupes indépendants (CGM vs. sans-CGM) | Test t indépendant | U de Mann-Whitney | Shapiro-Wilk p < 0,05 |
| H3 | Corrélation (durée vs. MAE) | r de Pearson | ρ de Spearman | Non normal ou non linéaire |
| H4 | Corrélation (expérience CGM vs. MAE) | r de Pearson | ρ de Spearman | Non normal ou non linéaire |
| H5 | Comparaison appariée (propres vs. génériques) | Test t apparié | Rangs signés de Wilcoxon | Scores de différence non normaux |

**Tous les tests utilisent le niveau de signification α \= 0,05. Les tailles d'effet seront rapportées pour toutes les analyses.**

### **7.5 Attentes de Taille d'Effet**

Basé sur GlucoBench et la littérature connexe sur la prédiction glycémique pour **les horizons de prédiction à 60 minutes** :

**Performance des Modèles issus des Benchmarks Publiés (MAE en mg/dL) :**

Les performances varient considérablement selon les jeux de données et les conditions. Plages représentatives de la littérature :

* **Régression linéaire / ARIMA \[7,8\] :** MAE ~12–20 mg/dL (données ID de GlucoBench), RMSE ~23–27 mg/dL (autres études)
* **Apprentissage profond (Transformer, Gluformer \[2,7,8\]) :** MAE ~11–17 mg/dL selon le jeu de données
* **Modèles personnalisés de pointe :** MAE ~15–17 mg/dL (approches récentes basées sur LLM \[3\])

Note : Les valeurs varient substantiellement selon la taille du jeu de données, les caractéristiques de la population et si l'évaluation est in-distribution (ID) vs. out-of-distribution (OD). GlucoBench rapporte que les modèles d'apprentissage profond généralisent considérablement mieux que les références simples sur les données OD.

**Tailles d'Effet Attendues pour les Hypothèses de l'Étude :**

Compte tenu de cette variabilité, nous utilisons des hypothèses conservatrices :

* **H1 (PAD vs. non-DM) :** En supposant un SD ~8–12 mg/dL entre participants et une différence significative de ~3–5 mg/dL entre groupes, cela représente un d de Cohen ~0,3–0,5 (effet petit à moyen).
* **H2 (Humain vs. références) :** L'écart entre les modèles simples et avancés est typiquement ~5–10 mg/dL. Nous nous attendons à ce que les humains se situent dans cette plage. Pour plus de description de la distribution humaine attendue, consultez la taille d'échantillon.
* **H3, H4 (Corrélations durée/CGM) :** Nous nous attendons à des corrélations de r ~0,15–0,30 entre l'expérience et la précision, basées sur des hypothèses de courbe d'apprentissage.
* **H5 (Propres vs. génériques) :** Nous nous attendons à une amélioration de ~2–4 mg/dL lors de la prédiction de données propres (effet apparié). C'est important car cela couvre la différence attendue entre la valeur réelle de glycémie mesurée dans le sang et la valeur de glycémie estimée (VGE) que les CGM fournissent.

**Mise en garde importante :** Ces estimations de taille d'effet sont dérivées de la variabilité entre les modèles ML dans les benchmarks, et non d'études précédentes sur la prédiction humaine (qui n'existent pas). La distribution réelle des performances humaines est inconnue et sera établie par cette étude. Nous soulignons que ces chiffres sont estimés sur la base des articles mentionnés dans la section références, en particulier l'article GlucoBench.

---

## **8\. Taille de l'Échantillon**

### **8.1 Inscription Cible**

**Cible :** Environ 200 participants au total

* Environ 100 personnes atteintes de diabète (PAD)
* Environ 100 personnes sans diabète (non-DM)
* Parmi les PAD : objectif de 70–90 participants téléchargeant leurs propres données

**Minimum viable :** Environ 150 participants (75 par groupe)

### **8.2 Justification**

Les objectifs de taille d'échantillon sont basés sur les estimations de taille d'effet dérivées des benchmarks de modèles ML, avec reconnaissance de l'incertitude :

**Gestion des mesures répétées :** Chaque participant fait 6–12 prédictions, ce qui signifie que nos données ont une structure de mesures répétées. Nous en tenons compte de deux manières : (1) nos analyses primaires utiliseront des moyennes par personne (une valeur MAE par participant), ce qui satisfait l'hypothèse d'indépendance pour les tests t et les corrélations, et (2) pour des analyses plus détaillées, nous utiliserons des modèles à effets mixtes qui modélisent explicitement la corrélation entre les mesures répétées de la même personne.

**Différences significatives :** Nous considérons une différence de 3–4 mg/dL dans le MAE comme cliniquement significative parce qu'elle représente environ la moitié de l'erreur de mesure des dispositifs CGM eux-mêmes (qui ont une différence relative absolue moyenne de 8–10% par rapport à la glycémie sanguine, soit environ 7–9 mg/dL aux niveaux glycémiques typiques). Une corrélation de r=0,25 explique environ 6% de la variance, ce qui, bien que modeste, vaudrait la peine d'être compris pour la conception future d'interventions.

**H1 (Comparaison du groupe diabète vs. non-diabète) :** Pour détecter une différence de 4 mg/dL dans l'erreur absolue moyenne (MAE) entre les groupes, en supposant un écart-type de 10 mg/dL (d de Cohen ≈ 0,4), nous avons besoin de 80–100 participants par groupe. Nous avons utilisé un test unilatéral avec α=0,025 ici parce que la littérature précédente suggère que les personnes atteintes de diabète pourraient mieux prédire, bien que la direction ne soit pas certaine. Cet ajustement de Bonferroni tient compte du test de deux comparaisons primaires (H1 et H2).

**H2 (Utilisateurs CGM vs. non-utilisateurs) :** Même calcul que H1 — nous nous attendons à des tailles d'effet similaires et avons besoin d'environ 80–100 par groupe. La nature appariée de certaines comparaisons au sein des participants (où la même personne fait plusieurs prédictions) nous donne en réalité une puissance statistique supplémentaire, mais nous sommes conservateurs dans nos estimations.

**H3 et H4 (Analyses de corrélation) :** Pour détecter une corrélation de r=0,25 entre la durée d'expérience et la précision de prédiction avec une puissance de 80%, nous avons besoin de 100–120 participants. La plage (100–120) reflète l'incertitude sur la force de corrélation réelle — si la corrélation réelle est plus faible que r=0,25, nous aurions besoin de l'extrémité supérieure de cette plage. Nous avons choisi r=0,25 comme cible parce que des corrélations plus petites auraient une importance pratique limitée.

**H5 (Comparaison données propres vs. données génériques) :** Il s'agit d'une comparaison intra-sujet, donc nous avons plus de puissance statistique. Pour détecter une différence de 3 mg/dL dans les mesures appariées (en supposant un SD apparié de 6 mg/dL), nous avons besoin d'environ 70 participants qui complètent les deux tâches. Le plan apparié est plus efficace parce que chaque personne sert de son propre contrôle.

**Mise en garde importante :** Incertitude de la Taille d'Échantillon

Nos calculs de taille d'échantillon sont basés sur les performances des modèles ML, mais le comportement humain peut différer :

Pourquoi cela importe :

* Les modèles ML sont cohérents → variabilité prévisible (SD ~10 mg/dL)
* Les humains sont variables → différences individuelles, effets d'apprentissage, fatigue
* Risque : Si le SD humain réel diffère des hypothèses, la puissance change drastiquement

Exemples :

| Scénario | SD Supposé | SD Réel | N planifié par groupe | Puissance Réelle | Statut |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Optimiste | 10 mg/dL | 8 mg/dL | 100 | ~95% | Surpuissant |
| Cas de base | 10 mg/dL | 10 mg/dL | 100 | 80% | Adéquat |
| Conservateur | 10 mg/dL | 12 mg/dL | 100 | ~65% | Sous-puissant |
| Pessimiste | 10 mg/dL | 15 mg/dL | 100 | ~45% | Sévèrement sous-puissant |

**Résultat :** L'étude pourrait être sous-puissante pour détecter de vrais effets ou gaspiller des ressources avec une inscription inutile.

---

**Solution Proposée :** Plan Adaptatif à Deux Étapes

**Étape 1 –** Analyse Intermédiaire (N=60–75 par groupe)

* Calculer les SDs et tailles d'effet observés à partir de vraies données humaines
* Recalculer la taille d'échantillon requise en utilisant des estimations empiriques
* Ajuster l'objectif de recrutement pour maintenir une puissance de 80%

**Étape 2 –** Recrutement Ajusté

* Continuer l'inscription jusqu'à l'objectif révisé basé sur les résultats intermédiaires
* Règles de décision pré-spécifiées :
  * *« Si SD observé \= 8 mg/dL → arrêter à 100 par groupe (déjà surpuissant) »*
  * *« Si SD observé \= 12 mg/dL → augmenter à 130 par groupe »*
  * *« Si SD observé >15 mg/dL → augmenter jusqu'à un maximum de 150 par groupe »*
* Plafond maximum : 150 par groupe

Avantages :

* Assure une puissance adéquate avec des données du monde réel
* Évite le sur-recrutement si la variabilité est inférieure aux attentes
* Prévient la sous-puissance sévère si la variabilité est supérieure

**8.3 Résultat Attendu**

Avec notre inscription cible (100 par groupe, potentiellement extensible à 150), nous devrions avoir une puissance adéquate pour toutes les analyses planifiées en supposant que nos estimations de variabilité sont approximativement correctes. Mais la vraie valeur de cette étude n'est pas seulement de tester nos hypothèses spécifiques — c'est d'établir les premiers benchmarks empiriques pour la précision de prédiction glycémique humaine.

Même si nous découvrons que les humains sont beaucoup plus variables que les modèles ML, c'est un résultat qui mérite d'être publié. Cela nous dirait que la capacité de prédiction humaine est fondamentalement moins cohérente que les approches algorithmiques, ce qui a des implications pour la manière dont nous concevons et évaluons les outils d'aide à la décision clinique.

**Données manquantes et exclusions :** Nous utiliserons l'analyse des cas complets pour les résultats primaires (participants qui terminent au moins 6 segments de prédiction valides). Si les données manquantes dépassent 10% des participants recrutés, nous conduirons des analyses de sensibilité comparant les compléteurs vs. non-compléteurs sur les caractéristiques de référence. Nous n'anticipons pas de données manquantes substantielles parce que la tâche est en ligne et ne prend que 15–20 minutes.

**Multiplicité :** Nous avons deux hypothèses primaires (H1 et H2) utilisant la correction de Bonferroni (α=0,025 par test). Les hypothèses secondaires (H3, H4, H5) sont exploratoires et seront rapportées avec des valeurs p nominales sans ajustement, clairement étiquetées comme analyses exploratoires.

**Qui effectue l'analyse :** Les analyses statistiques primaires seront conduites par Anton Kulaga (IP) avec l'orientation de Benjamin Otte (conseiller biostatistique). Toutes les analyses seront effectuées en Python en utilisant des packages standard. Le code d'analyse sera mis à disposition publique avec les résultats publiés.

**Facteurs de confusion :** Le plan transversal de l'étude limite notre capacité à contrôler les facteurs de confusion. Nous collecterons et rapporterons les variables clés (âge, durée du diabète, expérience CGM) et conduirons des analyses stratifiées là où la taille d'échantillon le permet. Les comparaisons primaires (PAD vs. non-PAD, CGM vs. sans-CGM) sont descriptives plutôt que causales, donc les facteurs de confusion sont moins problématiques que pour les études d'intervention.

**Confirmatoire vs. exploratoire :** H1 et H2 sont des hypothèses confirmatoires avec des niveaux de signification ajustés par Bonferroni. H3, H4 et H5 sont exploratoires et seront rapportées comme telles, avec des intervalles de confiance et des tailles d'effet plutôt que de se baser uniquement sur les valeurs p.

---

## **9\. Contrôle de la Qualité des Données**

### **9.1 Vérifications Automatisées**

* Validation de l'unicité de l'email
* Validation de la plage d'âge
* Vérifications du temps de complétion
* Validation du point de prédiction (les 12 points requis)
* Vérifications de la qualité des données CGM pour les téléchargements

### **9.2 Critères d'Exclusion pour l'Analyse**

* Segments avec des prédictions incomplètes (moins de 12 points)
* Segments avec des données de contexte CGM excessivement manquantes
* Participants avec moins de 5 segments valides

---

## **10\. Analyse Risque-Bénéfice**

### **10.1 Risques pour les Participants**

#### **10.1.1 Risques Physiques**

**Aucun.** Il s'agit d'une étude observationnelle en ligne sans interventions physiques :

* Pas de procédures médicales
* Pas d'administration de médicaments
* Aucune visite en personne requise
* **Aucune surveillance de santé en temps réel** — toutes les données sont historiques
* **Aucune connexion à des dispositifs médicaux actifs** — les participants n'ont pas besoin de porter d'équipement

#### **10.1.2 Risques Psychologiques**

**Minimes :**

* Frustration possible avec les tâches de prédiction (atténuée par des instructions claires, des essais de pratique)
* Légère anxiété de performance (atténuée en soulignant l'objectif de recherche)
* Préoccupations de confidentialité concernant le partage des données CGM (atténuées par la participation optionnelle, l'explication complète de la protection des données)

**Évaluation Globale :** Risques comparables à compléter un quiz ou sondage en ligne.

### **10.2 Bénéfices**

**Bénéfices Directs pour les Participants :** Aucun (étude de recherche uniquement). Les résultats ne constituent pas un avis médical.

**Importants Avertissements Communiqués aux Participants :**

* Les scores de précision mesurent uniquement les performances de prédiction — ils n'ont pas de signification diagnostique ou thérapeutique
* Les résultats ne doivent pas être utilisés pour ajuster les doses d'insuline, les choix alimentaires ou toute décision médicale
* Les participants doivent continuer à suivre indépendamment les conseils de leur professionnel de santé

**Bénéfices Indirects :**

* Contribuer aux connaissances scientifiques
* Perspicacité personnelle sur la capacité de prédiction
* Soutenir le développement de meilleurs outils de prédiction glycémique

---

## **11\. Protection des Participants et Éthique**

### **11.1 Consentement Éclairé**

Note importante — tout consentement sera donné en cochant les cases correspondantes dans l'interface en ligne et sera stocké numériquement. Si le consentement obligatoire n'est pas donné, le participant n'est pas autorisé à continuer, empêchant toute participation sans consentement.

**Portail de Vérification de l'Âge :**

Avant d'accéder à tout contenu de l'étude, les participants doivent confirmer qu'ils ont 18 ans ou plus :

* Le premier écran affiche : « Cette étude est ouverte aux adultes âgés de 18 ans et plus. Veuillez confirmer votre âge pour continuer. »
* Deux boutons : « J'ai 18 ans ou plus » (procède au consentement) / « J'ai moins de 18 ans » (affiche le message : « Merci pour votre intérêt, mais cette étude est réservée aux adultes. Veuillez fermer cette page. »)
* Si « moins de 18 ans » est sélectionné : Aucune donnée n'est collectée, la session se termine immédiatement, pas de cookies ni d'identifiants stockés
* Ce portail d'âge apparaît avant toute collecte de données personnelles

**Processus de Consentement Bilingue :**

L'étude fournit des matériaux de consentement éclairé en anglais et en allemand. Les participants sélectionnent leur langue préférée au début :

* **Sélection de la Langue :** Les participants choisissent « English » ou « Deutsch » sur la page d'accueil
* **Matériaux Complets :** Toutes les informations de consentement, instructions de l'étude et retours sont affichés dans la langue sélectionnée
* **Contenu Équivalent :** Les deux versions linguistiques contiennent des informations identiques, assurant une compréhension égale indépendamment de la préférence linguistique

**Le Formulaire de Consentement Électronique comprend :**

* Informations claires sur l'étude en langage non technique
* Accent sur la participation volontaire
* Explication de la protection des données et des droits RGPD
* Procédures et limitations du retrait (retrait possible jusqu'à l'anonymisation des données)
* Coordonnées

**Cases de Consentement (obligatoires) :**

* Je confirme que j'ai 18 ans ou plus, que j'ai lu et compris les informations sur l'étude, et que j'accepte volontairement de participer
* Je consens au traitement des données à des fins de recherche et je comprends que je peux me retirer jusqu'à l'anonymisation des données (RGPD Art. 6(1)(a), 9(2)(a))

**Cases de Consentement Optionnelles (clairement séparées du consentement de l'étude) :**

* J'accepte de télécharger mes propres données CGM pour la tâche optionnelle de données propres
* J'accepte d'être recontacté pour les résultats de l'étude (email stocké uniquement à cette fin)

**Communications Promotionnelles (Séparées du Consentement de l'Étude) :**

Tout opt-in pour des communications promotionnelles sur HEALES ou des projets connexes est :

* Présenté sur une page SÉPARÉE APRÈS la complétion de l'étude (pas pendant le consentement)
* Clairement étiqueté comme sans rapport avec la participation à l'étude
* Sans effet sur la participation à l'étude ou le traitement des données
* Peut être refusé sans aucune conséquence

### **11.2 Rémunération**

Pas de compensation monétaire. Les incitations non monétaires comprennent des retours personnalisés sur la précision et une carte de résultat partageable.

### **11.3 Assurance**

Aucune assurance spécifique à l'étude requise en raison du risque minimal (équivalent à un sondage en ligne).

---

## **12\. Calendrier**

Le calendrier de l'étude est flexible et sera ajusté en fonction des progrès du recrutement et des besoins opérationnels. Les phases générales comprennent :

1. **Préparation :** Soumission éthique, finalisation de la plateforme, préparation des matériaux de recrutement
2. **Tests Pilotes :** Tests à petite échelle avec collecte de retours
3. **Recrutement et Collecte de Données :** En cours jusqu'à l'inscription cible atteinte
4. **Analyse :** Traitement des données, analyse statistique
5. **Diffusion :** Préparation du manuscrit, publication, communication avec les participants

Les calendriers spécifiques seront déterminés en fonction de la date d'approbation éthique et du succès du recrutement.

---

## **13\. Limitations**

### **13.1 Biais de Sélection**

Les participants sont des volontaires auto-sélectionnés, ce qui peut ne pas représenter la population générale des utilisateurs de CGM.

### **13.2 Références Académiques vs. Réelles**

Bien que cette étude utilise des conditions plus réalistes que les jeux de données académiques contrôlés, les participants en ligne peuvent encore différer des utilisateurs typiques de CGM.

### **13.3 Plan de Session Unique**

Pas de suivi longitudinal ; les effets d'apprentissage dans le temps ne peuvent pas être évalués.

---

## **14\. Coordonnées**

**Investigateur Principal :**

 Anton Kulaga  
 Institut de Biostatistique et d'Informatique en Médecine et Recherche sur le Vieillissement (IBIMA)  
 Centre Médical Universitaire de Rostock  
 Email : anton.kulaga@uni-rostock.de

**Co-investigateurs :**

Livia Zaharia, MSc  
 HEALES \- Healthy Life Extension Society  
 Email : [liviazaharia2020@gmail.com](mailto:liviazaharia2020@gmail.com)

**Conseiller biostatistique :**

Benjamin Otte, MSc  
 Institut de Biostatistique et d'Informatique en Médecine et Recherche sur le Vieillissement (IBIMA)  
 Centre Médical Universitaire de Rostock  
 Email : benjamin.otte@uni-rostock.de

**Gestionnaire de Données :**  
 Nikolay Usanov, MSc  
 HEALES \- Healthy Life Extension Society  
 Ingénieur ML et Bioinformaticien

**Conseil Consultatif :**

* Prof. Georg Fullen \- Centre Médical Universitaire de Rostock
* Irina Gaynanova, PhD (Conseillère Statistique) \- Texas A\&M University
* Renat Sergazinov, PhD (Conseiller Technique) \- Auteur de GlucoBench

## Références :

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

**Réglementations Applicables :**

* RGPD / BDSG (protection des données) \- OUI
* Directives d'éthique de recherche allemandes \- OUI
* Réglementations sur les dispositifs médicaux (MDR) \- NON applicable
* AMG (loi pharmaceutique) \- NON applicable

---

**FIN DU DOCUMENT**

*Pour les questions ou clarifications, veuillez contacter :*  
 *Anton Kulaga : anton.kulaga@uni-rostock.de*  
 *Livia Zaharia : livia.zaharia@uni-rostock.de*
