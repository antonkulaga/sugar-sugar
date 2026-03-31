from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Final, Optional

from dash import dcc

from sugar_sugar.i18n import normalize_locale

_CONSENT_NOTICE_MD_RELATIVE_PATH: Final[Path] = Path(
    "data/input/patient_consent_form/Teilnehmerinformation_und_Einwilligungserklaerung_v2.docx.md"
)


def _project_root() -> Path:
    # sugar_sugar/consent_notice_text.py -> repo root
    return Path(__file__).resolve().parents[1]


def _consent_notice_md_path() -> Path:
    return _project_root() / _CONSENT_NOTICE_MD_RELATIVE_PATH


_CHECKBOX_GLYPHS_LINE_RE: Final[re.Pattern[str]] = re.compile(r"(?m)^\s*[☐☑]\s*")
_CHECKBOX_GLYPHS_ANYWHERE_RE: Final[re.Pattern[str]] = re.compile(r"[☐☑]\s*")
_ITTEILUNGEN_RE: Final[re.Pattern[str]] = re.compile(r"(?m)^(\*?)itteilungen\b")


def _sanitize_markdown(text: str) -> str:
    # Remove "checkbox" glyphs from the plain text/markdown (we use real UI checkboxes).
    text = _CHECKBOX_GLYPHS_LINE_RE.sub("", text)
    text = _CHECKBOX_GLYPHS_ANYWHERE_RE.sub("", text)

    # Fix a known conversion artifact present in the markdown export.
    text = _ITTEILUNGEN_RE.sub(r"\1Mitteilungen", text)

    # Minor cleanup for artifacts caused by docx->markdown conversion.
    text = text.replace("Ihnenzwei", "Ihnen zwei")
    text = text.replace("historischenDaten", "historischen Daten")
    text = text.replace("fürv", "für")
    return text.strip()


def _read_markdown_file(path: Path) -> str:
    if not path.exists():
        return ""
    return _sanitize_markdown(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def consent_notice_markdown_de() -> str:
    return _read_markdown_file(_consent_notice_md_path())


# NOTE: These translations are derived from the German source .docx.
# They are used when the UI language is not German.
_CONSENT_NOTICE_TRANSLATIONS: Final[dict[str, list[str]]] = {
    "en": [
        "Participant information",
        "Prediction of glucose trajectories based on previous value patterns: an online benchmarking study",
        "Short title: Sugar-Sugar glucose prediction study",
        "Please read the following text carefully before making a decision. If you have questions, please contact the study leadership.",
        "Dear participant,",
        "we would like to ask whether you would like to take part in a scientific study. This study aims to systematically investigate, for the first time, how accurately humans can predict short-term glucose trajectories based on CGM data (data from a continuous glucose monitoring device). So far, there is no such benchmark. Your participation helps establish a reference value for human prediction accuracy, which can also be used in the long term to evaluate computer-based prediction models. Such prediction models are increasingly used in diabetes research and diabetes care and can be validated and compared using the data collected here.",
        "The study is conducted at IBIMA (Institute for Biostatistics and Informatics in Medicine and Ageing Research) at University Medicine Rostock, in collaboration with HEALES (Healthy Life Extension Society, Brussels), which acts as the funder of the study. The study leadership is Anton Kulaga (University Medicine Rostock) and Livia Zaharia (HEALES). At least 200 participants are planned.",
        "Participation in the study has no influence on any medical treatment. This is a purely online study without in-person appointments or medical procedures.",
        "How does the study work?",
        "Participation takes place entirely online via the Sugar-Sugar web application and takes about 15–20 minutes.",
        "First, you will fill out a short registration questionnaire (age, gender, country of residence, diabetes status, CGM usage history; optional: weight and height). You will then complete 6 to 12 prediction tasks. Each task shows three hours of historical CGM data from a publicly known, anonymized dataset. You will be shown the earlier time points of time series collected in other studies; you are asked to guess the later time points. You will draw the expected glucose trajectory for the following 60 minutes by placing 12 points in a chart. Before the scored tasks, you will be offered two optional practice rounds.",
        "After each task, the actual glucose values are displayed and accuracy metrics are calculated. At the end, you will receive a summary of your prediction accuracy (determined from the historical data) as well as a percentile rank.",
        "Prediction accuracy is compared across four groups: people with diabetes and CGM use, people with diabetes without CGM use, people without diabetes with CGM use, and people without diabetes without CGM experience; based on the data collected at the beginning you will be assigned to one of these groups.",
        "Optional upload of your own CGM data",
        "If you use a CGM device yourself, you can optionally upload an export file (CSV or JSON). Short segments are extracted from it and used for additional prediction tasks. This makes it possible to compare whether you predict your own data more accurately than the historical data. Date and time are not displayed in the user interface. The uploaded raw file is deleted within 30 days; only the extracted segments are retained in pseudonymized form.",
        "Voluntary participation",
        "Participation in this study is voluntary. You will only be included if you declare your consent. If you do not participate in the study or later wish to withdraw from it, you will not suffer any disadvantages. You can end participation at any time without giving reasons. Partial data from completed rounds are only included if at least 6 valid rounds have been completed.",
        "Who can participate?",
        "Adults aged 18 and over with internet access can participate. Both people with and without diabetes are eligible.",
        "What possible risks, discomforts, or side effects are associated with your participation?",
        "Since our study only collects data, there are no medical risks associated with participation. The accuracy values are relevant exclusively for research and have no diagnostic or clinical meaning.",
        "What possible benefits result from your participation in the study?",
        "There is no personal health benefit for you from participating. Participation contributes to a systematic benchmark of human glucose-value prediction ability. You will receive a personal accuracy summary as well as a results card. There is no monetary compensation.",
        "What rights and conditions are associated with participation?",
        "You can end your participation in the study at any time, even without giving reasons. If you do not wish to participate or wish to withdraw, you will not suffer any disadvantages.",
        "Please note that no separate insurance has been taken out for this project and the accompanying study, as it is a purely online study without medical procedures and therefore involves minimal risk.",
        "The study has been submitted to the responsible ethics committee. It raised no objections.",
        "Data protection",
        "Below we would like to inform you comprehensively about what happens to your personal data within the study and how we handle it.",
        "1. Who is responsible for data processing and storage?",
        "University Medicine Rostock is responsible for data processing and storage within the study. HEALES operates the Sugar-Sugar application as a processor within the framework of a data processing agreement (DPA) with University Medicine Rostock. You can reach the responsible institution at the following contact details:",
        "Responsible institution: University Medicine Rostock – legally capable sub-entity of the University of Rostock",
        "Schillingallee 35, 18057 Rostock",
        "www.med.uni-rostock.de",
        "2. Who can you contact with questions about the study or data protection?",
        "To best safeguard your interests, you can also contact the following persons at any time with any questions about your participation in the study or the general procedure:",
        "Study contacts:",
        "• Anton Kulaga: anton.kulaga@uni-rostock.de",
        "• Livia Zaharia: livia.zaharia@uni-rostock.de",
        "For data protection questions, the data protection officer of University Medicine Rostock is also available:",
        "Doberaner Str. 142, 18057 Rostock",
        "0381 494 5155 | datenschutz@med.uni-rostock.de",
        "If you wish to exercise your right to complain about unlawful data processing, please contact the competent supervisory authority:",
        "State Commissioner for Data Protection and Freedom of Information M-V",
        "Schloss Schwerin, Lennéstr. 1, 19053 Schwerin",
        "info@datenschutz-mv.de",
        "3. Which data do we need from you to conduct the study?",
        "The following data are collected within the study:",
        "Contact details: email address (for registration, withdrawal handling, and optional re-notification).",
        "Demographic data: age, gender, country of residence; optional: weight and height.",
        "Health-related data: diabetes status (yes/no, type, duration), CGM usage history.",
        "Study data: predicted and, if applicable, actual glucose values, accuracy metrics (MAE, MSE, RMSE, MAPE).",
        "Consent preferences: documentation of your consent decisions.",
        "Optional – own CGM data: if uploaded, only extracted segments are retained in pseudonymized form.",
        "4. Where do we obtain this data?",
        "All data are collected exclusively directly from you as a participant, through your inputs in the Sugar-Sugar web application (registration questionnaire, prediction tasks, optional CGM upload). No data are obtained from other sources. The legal basis for processing is your explicit consent pursuant to Art. 6(1)(a) GDPR and Art. 9(2)(a) GDPR.",
        "5. For what purposes do we need your data and how are they protected?",
        "The data listed above are needed exclusively for the scientific investigation of human glucose prediction ability and are used only for this purpose.",
        "Each participating person receives a random study ID during registration. All research data are linked exclusively to this ID. A separate encrypted mapping file linking the study ID to the email address is stored separately and is accessible only to the study leadership (Anton Kulaga and Livia Zaharia). This file is used exclusively to handle withdrawal requests and optional result notifications. For other study staff, it is therefore not possible to identify you.",
        "Data are encrypted during transmission and at rest. Storage takes place on servers within the European Union (GDPR-compliant hosting). Access is regulated based on roles.",
        "6. Where and for how long are the data stored?",
        "The data collected within the study are first pseudonymized. The mapping file (email – study ID) is expected to be destroyed 12 months after study completion. After that, the study data are anonymized, i.e., they no longer allow any inference about your identity.",
        "Pseudonymized research data are retained for 10 years in accordance with German research standards. Uploaded raw CGM files are deleted within 30 days.",
        "7. Who will learn about your data? Will your data be shared or published?",
        "Pseudonymized research data are accessible only to the study team at IBIMA. The mapping file is accessible only to the study leadership (Anton Kulaga and Livia Zaharia). Study results are published only in aggregated, anonymized form. It is not possible to infer individual persons from publications.",
        "8. What data protection rights do you have when participating in the study?",
        "In accordance with applicable data protection regulations (GDPR), you have the right of access to stored data, rectification of inaccurate data, erasure of data, restriction of processing, objection to unreasonable processing, and the right to data portability of the data stored about you. You also have the right to withdraw your consent. You can exercise these rights at any time with the responsible institution.",
        "Right of withdrawal",
        "In principle, you can withdraw your consent at any time without giving reasons. Please contact the study leadership (anton.kulaga@uni-rostock.de). Your withdrawal takes effect from the time you submit it. Processing of your data up to that point remains lawful. In the event of withdrawal, deletion of personal data will be initiated. Study data that have already been anonymized and can therefore no longer be linked to you will continue to be used within the study. The mapping file is expected to be destroyed 12 months after study completion; after that, an individual assignment and thus deletion are no longer possible.",
        "Legal basis: Art. 6(1)(a) GDPR and Art. 9(2)(a) GDPR.",
        "Declaration of consent for participation in the Sugar-Sugar glucose prediction study and the associated data processing",
        "Study ID of the participating person: _________________________________ (assigned at registration)",
        "The following consents are recorded electronically at the time of registration by checking the corresponding boxes.",
        "I participate in the study voluntarily. I have carefully read the participant information for the study and the included data protection notice and the associated rights.",
        "I have been informed that personal data will be collected, processed, and used within the study, in particular my health data (diabetes status, CGM usage history, prediction performance).",
        "As stated in the participant information, processing takes place in pseudonymized form by the study team at IBIMA, University Medicine Rostock. HEALES acts as a processor under a DPA.",
        "I am aware that if my data are stored anonymously, deletion at my request is no longer possible.",
        "Right of withdrawal",
        "I have been informed that I can end my participation at any time without giving reasons, without any disadvantages for me. I am also aware that I can withdraw my consent to data processing at any time with effect for the future, without affecting the lawfulness of processing carried out on the basis of consent until withdrawal. I have taken note of the information on withdrawing consent in the corresponding participant information.",
        "I hereby declare my voluntary agreement to participate in the Sugar-Sugar glucose prediction study. I understand that I can end my participation at any time without giving reasons, without any disadvantages for me.",
        "I hereby consent, including the corresponding participant information, to the processing of my personal and health data for the following purposes:",
        "☐  Collection, processing and use of my data listed in the participant information, in particular my health data (diabetes status, CGM usage history, prediction performance), in pseudonymized form for conducting the study by the study team at IBIMA, University Medicine Rostock, as well as HEALES as processor. Storage takes place on servers within the European Union. Research data are retained for up to 10 years after anonymization of the mapping file. Withdrawal is possible up to 12 months after study completion; afterwards identification is no longer possible. Legal basis: Art. 6(1)(a) GDPR and Art. 9(2)(a) GDPR.",
        "☐  The participating person confirms being 18 years of age or older.",
        "Optional consents (refusal has no influence on participation in the study):",
        "☐  I consent to uploading my own CGM data for the optional prediction task with my own data. Raw data will be deleted within 30 days; only pseudonymized extracted segments will be retained.",
        "☐  I agree to be informed by the study team via the registered email address about the study results after publication.",
        "Notifications from HEALES or related projects will be presented on a separate page after the study ends and are completely independent of participation in the study and consent.",
        "This study has been submitted to the Ethics Committee of University Medicine Rostock. Registration number: Ref. number A 2026-0064. Received by the Ethics Committee: February 27, 2026.",
        "Questions or withdrawal requests: anton.kulaga@uni-rostock.de | livia.zaharia@uni-rostock.de",
    ],
    "uk": [
        "Інформація для учасників",
        "Прогнозування перебігу глюкози на основі попередніх шаблонів значень: онлайн‑бенчмаркінг‑дослідження",
        "Коротка назва: дослідження прогнозування глюкози Sugar‑Sugar",
        "Будь ласка, уважно прочитайте наведений нижче текст, перш ніж приймати рішення. Якщо у вас є запитання, зверніться до керівництва дослідження.",
        "Шановна учаснице, шановний учаснику,",
        "ми хотіли б запитати, чи бажаєте ви взяти участь у науковому дослідженні. Метою цього дослідження є вперше систематично вивчити, наскільки точно люди можуть прогнозувати короткострокові зміни глюкози на основі даних CGM (дані безперервного моніторингу глюкози). Наразі такого еталонного порівняння не існує. Ваша участь допоможе створити референтний показник точності людського прогнозу, який у майбутньому також можна буде використовувати для оцінювання комп’ютерних моделей прогнозування. Такі моделі дедалі частіше застосовують у дослідженнях діабету та в догляді за людьми з діабетом, і їх можна валідовувати та порівнювати за допомогою даних, зібраних у цьому дослідженні.",
        "Дослідження проводиться в IBIMA (Інститут біостатистики та інформатики в медицині й дослідженнях старіння) Університетської медицини Ростока у співпраці з HEALES (Healthy Life Extension Society, Брюссель), яка виступає спонсором/фундатором дослідження. Керівництво дослідження: Антон Кулага (Університетська медицина Ростока) та Лівія Захарія (HEALES). Планується щонайменше 200 учасників.",
        "Участь у дослідженні не впливає на будь‑яке медичне лікування. Це суто онлайн‑дослідження без очних зустрічей чи медичних процедур.",
        "Як відбувається дослідження?",
        "Участь повністю онлайн через вебзастосунок Sugar‑Sugar і триває приблизно 15–20 хвилин.",
        "Спочатку ви заповните коротку реєстраційну анкету (вік, стать, країна проживання, статус діабету, історія використання CGM; опційно: вага та зріст). Потім ви виконаєте 6–12 завдань на прогноз. Кожне завдання показує три години історичних даних CGM з публічно відомого, анонімізованого набору даних. Вам буде показано ранні часові точки часових рядів, зібраних у рамках інших досліджень; пізніші точки вам потрібно вгадати. Ви намалюєте очікувану траєкторію глюкози на наступні 60 хвилин, поставивши 12 точок на діаграмі. Перед оцінюваними завданнями вам запропонують дві необов’язкові тренувальні раунди.",
        "Після кожного завдання показуються фактичні значення глюкози та обчислюються метрики точності. Наприкінці ви отримаєте підсумок своєї точності прогнозування (за історичними даними) та перцентильний ранг.",
        "Точність прогнозу порівнюється у чотирьох групах: люди з діабетом і з використанням CGM, люди з діабетом без CGM, люди без діабету з CGM та люди без діабету без досвіду CGM; на основі початкових даних вас буде віднесено до однієї з цих груп.",
        "Опційне завантаження власних CGM‑даних",
        "Якщо ви користуєтеся CGM‑пристроєм, ви можете опційно завантажити файл експорту (CSV або JSON). З нього будуть виділені короткі сегмененти та використані для додаткових завдань прогнозування. Це дозволяє порівняти, чи прогнозуєте ви власні дані точніше, ніж історичні. Дата і час у інтерфейсі не показуються. Завантажений сирий файл буде видалено протягом 30 днів; зберігатимуться лише виділені сегменти у псевдонімізованому вигляді.",
        "Добровільність участі",
        "Участь у цьому дослідженні є добровільною. Вас включать лише тоді, коли ви надасте згоду. Якщо ви не братимете участі або згодом захочете вийти з дослідження, це не матиме для вас жодних негативних наслідків. Ви можете припинити участь у будь‑який момент без пояснення причин. Часткові дані з завершених раундів враховуються лише якщо завершено щонайменше 6 валідних раундів.",
        "Хто може брати участь?",
        "Брати участь можуть повнолітні особи від 18 років з доступом до інтернету. До участі допускаються як люди з діабетом, так і без діабету.",
        "Які можливі ризики, дискомфорт чи побічні ефекти пов’язані з участю?",
        "Оскільки в рамках нашого дослідження збираються лише дані, участь не пов’язана з медичними ризиками. Показники точності мають значення виключно для науки і не мають діагностичного чи клінічного значення.",
        "Яка можлива користь від участі в дослідженні?",
        "Особистої користі для здоров’я від участі немає. Участь робить внесок у систематичний бенчмарк здатності людини прогнозувати значення глюкози. Ви отримаєте персональний підсумок точності та картку результатів. Грошової винагороди немає.",
        "Які права та умови пов’язані з участю?",
        "Ви можете припинити участь у дослідженні будь‑коли, навіть без пояснення причин. Якщо ви не хочете брати участь або бажаєте вийти, це не спричинить для вас жодних негативних наслідків.",
        "Звертаємо увагу, що для цього проєкту та супровідного дослідження не було оформлено окремого страхування, оскільки це суто онлайн‑дослідження без медичних процедур і, відповідно, з мінімальним ризиком.",
        "Дослідження подано до відповідної етичної комісії. Заперечень не висловлено.",
        "Захист даних",
        "Нижче ми хочемо детально поінформувати вас, що відбувається з вашими персональними даними в межах дослідження і як ми з ними поводимося.",
        "1. Хто відповідає за обробку та зберігання даних?",
        "Відповідальною за обробку та зберігання даних у межах дослідження є Університетська медицина Ростока. HEALES експлуатує застосунок Sugar‑Sugar як обробник даних на підставі договору про обробку даних (AVV/DPA) з Університетською медициною Ростока. З відповідальною установою можна зв’язатися за такими контактами:",
        "Відповідальна установа",
        "Університетська медицина Ростока – правоздатна підструктура Університету Ростока",
        "Schillingallee 35",
        "18057 Rostock",
        "www.med.uni-rostock.de",
        "2. До кого звертатися з питаннями щодо дослідження або захисту даних?",
        "Щоб максимально захистити ваші інтереси, ви можете будь‑коли звертатися з усіма питаннями щодо вашого супроводу в межах дослідження або загального перебігу за такими контактами:",
        "Контакти щодо дослідження",
        "Anton Kulaga: anton.kulaga@uni-rostock.de",
        "Livia Zaharia: livia.zaharia@uni-rostock.de",
        "З питань захисту даних вам також може допомогти уповноважений із захисту даних Університетської медицини Ростока:",
        "Уповноважений із захисту даних Університетської медицини Ростока",
        "Уповноважений із захисту даних",
        "Doberaner Str. 142",
        "18057 Rostock",
        "0381 494 5155 | datenschutz@med.uni-rostock.de",
        "Якщо ви хочете скористатися правом на скаргу щодо незаконної обробки даних, зверніться до компетентного наглядового органу:",
        "Компетентний наглядовий орган із захисту даних",
        "Landesbeauftragte für Datenschutz und Informationsfreiheit M‑V",
        "Schloss Schwerin, Lennéstr. 1",
        "19053 Schwerin",
        "info@datenschutz-mv.de",
        "3. Які дані ми потребуємо від вас для проведення дослідження?",
        "У межах дослідження збираються такі дані:",
        "Контактні дані: адреса електронної пошти (для реєстрації, опрацювання відкликання та опційного повторного повідомлення).",
        "Демографічні дані: вік, стать, країна проживання; опційно: вага та зріст.",
        "Дані про здоров’я: статус діабету (так/ні, тип, тривалість), історія використання CGM.",
        "Дані дослідження: спрогнозовані та, за потреби, фактичні значення глюкози, метрики точності (MAE, MSE, RMSE, MAPE).",
        "Налаштування згоди: документування ваших рішень щодо згоди.",
        "Опційно — власні CGM‑дані: у разі завантаження зберігаються лише виділені сегменти у псевдонімізованому вигляді.",
        "4. Звідки ми отримуємо ці дані?",
        "Усі дані збираються виключно безпосередньо від вас як учасника — через ваші введення у вебзастосунку Sugar‑Sugar (реєстраційна анкета, завдання прогнозування, опційне завантаження CGM). Дані з інших джерел не отримуються. Правова підстава обробки — ваша явна згода відповідно до ст. 6(1)(a) GDPR та ст. 9(2)(a) GDPR.",
        "5. Для яких цілей потрібні ваші дані та як вони захищені?",
        "Зазначені вище дані потрібні виключно для наукового дослідження здатності людини прогнозувати глюкозу і використовуються лише для цієї мети.",
        "Під час реєстрації кожному учаснику присвоюється випадковий ID дослідження. Усі наукові дані пов’язуються лише з цим ID. Окремий зашифрований файл відповідності, який зіставляє ID дослідження з адресою електронної пошти, зберігається окремо і доступний лише керівництву дослідження (Антон Кулага та Лівія Захарія). Цей файл використовується виключно для опрацювання запитів на відкликання та опційного сповіщення про результати. Для інших співробітників дослідження встановлення вашої особи неможливе.",
        "Дані шифруються під час передавання та у стані зберігання. Зберігання відбувається на серверах у межах Європейського Союзу (GDPR‑сумісний хостинг). Доступ регулюється за ролями.",
        "6. Де і як довго зберігаються дані?",
        "Дані, зібрані в межах дослідження, спочатку псевдонімізуються. Файл відповідності (email – ID дослідження) планується знищити приблизно через 12 місяців після завершення дослідження. Після цього дані дослідження стають анонімізованими, тобто не дозволяють встановити вашу особу.",
        "Псевдонімізовані наукові дані зберігаються 10 років відповідно до німецьких наукових стандартів. Завантажені сирі CGM‑файли видаляються протягом 30 днів.",
        "7. Хто матиме доступ до ваших даних? Чи передаються та публікуються дані?",
        "Псевдонімізовані наукові дані доступні лише команді дослідження в IBIMA. Файл відповідності доступний лише керівництву дослідження (Антон Кулага та Лівія Захарія). Результати дослідження публікуються лише у агрегованому, анонімізованому вигляді. З публікацій неможливо зробити висновки про окремих осіб.",
        "8. Які права на захист даних ви маєте під час участі в дослідженні?",
        "Відповідно до чинних норм захисту даних (GDPR) ви маєте право на доступ до збережених даних, виправлення неточних даних, видалення даних, обмеження обробки даних, заперечення проти неприйнятної обробки та право на перенесення даних, що зберігаються про вас. Також ви маєте право відкликати надану згоду. Ці права можна реалізувати будь‑коли щодо відповідальної установи.",
        "Право на відкликання",
        "Загалом ви можете відкликати свою згоду будь‑коли без пояснення причин. Для цього зверніться до керівництва дослідження (anton.kulaga@uni-rostock.de). Ваше відкликання діє з моменту його подання. Обробка даних до цього моменту залишається правомірною. У разі відкликання буде ініційовано видалення персональних даних. Дані дослідження, які вже були анонімізовані і тому більше не можуть бути пов’язані з вами, продовжуватимуть використовуватися в межах дослідження. Файл відповідності планується знищити приблизно через 12 місяців після завершення; після цього індивідуальне зіставлення і, відповідно, видалення стають неможливими.",
        "Правова підстава: ст. 6(1)(a) GDPR та ст. 9(2)(a) GDPR.",
        "Заява про згоду",
        "на участь у дослідженні Sugar‑Sugar з прогнозування глюкози",
        "та пов’язану з цим обробку даних",
        "ID дослідження учасника: _________________________________ (надається під час реєстрації)",
        "Наведені нижче згоди фіксуються електронно під час реєстрації шляхом позначення відповідних прапорців.",
        "Я беру участь у дослідженні добровільно. Я уважно прочитав/ла інформацію для учасників і наведені там повідомлення про захист даних та пов’язані права.",
        "Мене поінформовано, що в межах дослідження будуть збиратися, оброблятися та використовуватися мої персональні дані, зокрема дані про здоров’я (статус діабету, історія використання CGM, показники прогнозування).",
        "Як зазначено в інформації для учасників, обробка відбувається у псевдонімізованому вигляді командою дослідження в IBIMA Університетської медицини Ростока. HEALES виступає обробником за договором AVV/DPA.",
        "Я усвідомлюю, що у разі анонімізованого зберігання моїх даних їх видалення на моє прохання більше неможливе.",
        "Право на відкликання",
        "Мене поінформовано, що я можу припинити участь будь‑коли без пояснення причин і без негативних наслідків для себе. Також мені відомо, що я можу відкликати згоду на обробку даних у будь‑який момент з дією на майбутнє, не впливаючи на правомірність обробки, здійсненої до відкликання. Інформацію щодо відкликання, наведені у відповідній інформації для учасників, я прийняв/ла до відома.",
        "Я цим заявляю про добровільну згоду на участь у дослідженні Sugar‑Sugar. Я розумію, що можу припинити участь у будь‑який момент без пояснення причин і без негативних наслідків для себе.",
        "Я даю згоду (з урахуванням відповідної інформації для учасників) на обробку моїх персональних даних та даних про здоров’я з такими цілями:",
        "☐  Збір, обробка та використання моїх даних, перелічених в інформації для учасників, зокрема моїх даних про здоров’я (статус діабету, історія використання CGM, показники прогнозу), у псевдонімізованому вигляді для проведення дослідження командою IBIMA Університетської медицини Ростока, а також HEALES як обробником даних. Зберігання відбувається на серверах у межах ЄС. Наукові дані зберігаються до 10 років після анонімізації файлу відповідності. Відкликання можливе до 12 місяців після завершення; після цього ідентифікація неможлива. Правова підстава: ст. 6(1)(a) GDPR та ст. 9(2)(a) GDPR.",
        "☐  Учасник підтверджує, що йому/їй 18 років або більше.",
        "Опційні згоди (відмова не впливає на участь у дослідженні):",
        "☐  Я даю згоду завантажити власні CGM‑дані для опційного завдання прогнозування на власних даних. Сирі дані видаляються протягом 30 днів; зберігаються лише псевдонімізовані виділені сегменти.",
        "☐  Я погоджуюся, що команда дослідження повідомить мене через зареєстровану електронну пошту про результати дослідження після їх публікації.",
        "Повідомлення від HEALES або пов’язаних проєктів будуть представлені на окремій сторінці після завершення дослідження і є повністю незалежними від участі та згод у межах дослідження.",
        "Це дослідження було подано до етичної комісії Університетської медицини Ростока. Реєстраційний номер: Ref. number A 2026-0064. Отримано Комітетом з етики: 27 лютого 2026.",
        "Питання або запити на відкликання: anton.kulaga@uni-rostock.de | livia.zaharia@uni-rostock.de",
    ],
    "ro": [
        "Informații pentru participanți",
        "Predicția evoluției glucozei pe baza tiparelor anterioare ale valorilor: un studiu online de benchmarking",
        "Titlu scurt: studiul Sugar‑Sugar de predicție a glucozei",
        "Te rugăm să citești cu atenție următorul text înainte de a lua o decizie. Pentru întrebări, contactează conducerea studiului.",
        "Stimată participantă, stimate participant,",
        "dorim să te întrebăm dacă dorești să participi la un studiu științific. Prin acest studiu se urmărește investigarea sistematică, pentru prima dată, a cât de precis pot oamenii să prezică evoluțiile pe termen scurt ale glucozei pe baza datelor CGM (date de la un dispozitiv de monitorizare continuă a glucozei). Până acum nu există un astfel de reper de comparație. Participarea ta ajută la stabilirea unei valori de referință pentru acuratețea predicției umane, care pe termen lung poate fi folosită și pentru evaluarea modelelor de predicție asistate de calculator. Astfel de modele sunt utilizate tot mai des în cercetarea diabetului și în îngrijirea persoanelor cu diabet și pot fi validate și comparate pe baza datelor colectate aici.",
        "Studiul este realizat la IBIMA (Institutul de Biostatistică și Informatică în Medicină și Cercetarea Îmbătrânirii) din cadrul Universitätsmedizin Rostock, în colaborare cu HEALES (Healthy Life Extension Society, Bruxelles), care acționează ca finanțator al studiului. Conducerea studiului: Anton Kulaga (Universitätsmedizin Rostock) și Livia Zaharia (HEALES). Sunt planificați cel puțin 200 de participanți.",
        "Participarea la studiu nu are niciun impact asupra unui eventual tratament medical. Este un studiu exclusiv online, fără întâlniri în persoană sau măsuri medicale.",
        "Cum se desfășoară studiul?",
        "Participarea are loc complet online prin aplicația web Sugar‑Sugar și durează aproximativ 15–20 de minute.",
        "Mai întâi vei completa un chestionar scurt de înregistrare (vârstă, gen, țara de reședință, statutul diabetului, istoricul utilizării CGM; opțional: greutate și înălțime). Apoi vei rezolva 6 până la 12 sarcini de predicție. Fiecare sarcină prezintă trei ore de date CGM istorice dintr-un set de date public, anonim. Vei primi momentele timpurii ale seriilor temporale colectate în alte studii; momentele târzii trebuie ghicite. Vei desena evoluția așteptată a glucozei pentru următoarele 60 de minute, plasând 12 puncte într-un grafic. Înaintea sarcinilor evaluate ți se vor oferi două runde opționale de exersare.",
        "După fiecare sarcină se afișează valorile reale ale glucozei și se calculează metrici de acuratețe. La final primești un rezumat al acurateții predicției tale (determinată din datele istorice), precum și un rang percentil.",
        "Acuratețea predicției este comparată în patru grupuri: persoane cu diabet și utilizare CGM, persoane cu diabet fără utilizare CGM, persoane fără diabet cu utilizare CGM și persoane fără diabet fără experiență CGM; pe baza datelor colectate la început vei fi repartizat într-unul dintre aceste grupuri.",
        "Încărcare opțională a propriilor date CGM",
        "Dacă folosești un dispozitiv CGM, poți încărca opțional un fișier de export (CSV sau JSON). Din acesta se extrag segmente scurte și se folosesc pentru sarcini suplimentare de predicție. Astfel se poate compara dacă îți prezici propriile date mai precis decât datele istorice. Data și ora nu sunt afișate în interfața utilizatorului. Fișierul brut încărcat este șters în 30 de zile; se păstrează doar segmentele extrase în formă pseudonimizată.",
        "Participare voluntară",
        "Participarea la acest studiu este voluntară. Vei fi inclus doar dacă îți exprimi consimțământul. Dacă nu participi sau dacă ulterior dorești să te retragi, nu vei avea niciun dezavantaj. Poți încheia participarea oricând fără a oferi motive. Datele parțiale din runde finalizate sunt incluse doar dacă au fost finalizate cel puțin 6 runde valide.",
        "Cine poate participa?",
        "Pot participa persoane majore (18+) cu acces la internet. Sunt eligibile atât persoane cu diabet, cât și fără diabet.",
        "Ce riscuri, disconfort sau efecte secundare posibile sunt asociate participării?",
        "Deoarece în cadrul studiului nostru sunt colectate doar date, participarea nu implică riscuri medicale. Valorile de acuratețe sunt relevante exclusiv pentru cercetare și nu au nicio semnificație diagnostică sau clinică.",
        "Ce beneficii posibile rezultă din participarea la studiu?",
        "Nu există un beneficiu personal pentru sănătate prin participare. Participarea contribuie la un benchmark sistematic al capacității umane de a prezice valorile glucozei. Vei primi un rezumat personal al acurateții și un card al rezultatelor. Nu există compensație financiară.",
        "Ce drepturi și condiții sunt asociate participării?",
        "Poți încheia participarea la studiu oricând, chiar și fără a oferi motive. Dacă nu dorești să participi sau dorești să te retragi, nu vei avea niciun dezavantaj.",
        "Te informăm că pentru acest proiect și studiul însoțitor nu a fost încheiată o asigurare separată, deoarece este un studiu exclusiv online fără măsuri medicale și, prin urmare, cu risc minim.",
        "Studiul a fost prezentat comisiei de etică competente. Nu au fost ridicate obiecții.",
        "Protecția datelor",
        "În cele ce urmează dorim să te informăm pe larg ce se întâmplă cu datele tale personale în cadrul studiului și cum le gestionăm.",
        "1. Cine este responsabil pentru prelucrarea și stocarea datelor?",
        "Universitätsmedizin Rostock este responsabilă pentru prelucrarea și stocarea datelor în cadrul studiului. HEALES operează aplicația Sugar‑Sugar ca împuternicit (processor) în baza unui contract de împuternicire (AVV/DPA) cu Universitätsmedizin Rostock. Poți contacta instituția responsabilă la următoarele coordonate:",
        "Instituție responsabilă",
        "Universitätsmedizin Rostock – subentitate cu personalitate juridică a Universității din Rostock",
        "Schillingallee 35",
        "18057 Rostock",
        "www.med.uni-rostock.de",
        "2. Cui te poți adresa pentru întrebări despre studiu sau despre protecția datelor?",
        "Pentru a-ți proteja cât mai bine interesele, te poți adresa oricând, pentru orice întrebări privind participarea ta în cadrul studiului sau desfășurarea lui, următorilor responsabili:",
        "Contacte pentru studiu",
        "Anton Kulaga: anton.kulaga@uni-rostock.de",
        "Livia Zaharia: livia.zaharia@uni-rostock.de",
        "Pentru întrebări legate de protecția datelor, îți stă la dispoziție și responsabilul cu protecția datelor al Universitätsmedizin Rostock:",
        "Responsabil cu protecția datelor al Universitätsmedizin Rostock",
        "Responsabilul cu protecția datelor",
        "Doberaner Str. 142",
        "18057 Rostock",
        "0381 494 5155 | datenschutz@med.uni-rostock.de",
        "Dacă dorești să îți exerciți dreptul de a depune o plângere privind prelucrări ilegale de date, te rugăm să te adresezi autorității de supraveghere competente:",
        "Autoritate competentă de supraveghere în domeniul protecției datelor",
        "Der Landesbeauftragte für Datenschutz und Informationsfreiheit M‑V",
        "Schloss Schwerin, Lennéstr. 1",
        "19053 Schwerin",
        "info@datenschutz-mv.de",
        "3. Ce date avem nevoie de la tine pentru desfășurarea studiului?",
        "În cadrul studiului sunt colectate următoarele date:",
        "Date de contact: adresă de email (pentru înregistrare, gestionarea retragerii consimțământului și re-notificare opțională).",
        "Date demografice: vârstă, gen, țara de reședință; opțional: greutate și înălțime.",
        "Date legate de sănătate: statutul diabetului (da/nu, tip, durată), istoricul utilizării CGM.",
        "Date de studiu: valorile glucozei prezise și, dacă este cazul, reale, metrici de acuratețe (MAE, MSE, RMSE, MAPE).",
        "Preferințe de consimțământ: documentarea deciziilor tale de consimțământ.",
        "Opțional – propriile date CGM: dacă sunt încărcate, se păstrează doar segmentele extrase în formă pseudonimizată.",
        "4. De unde obținem aceste date?",
        "Toate datele sunt colectate exclusiv direct de la tine ca participant, prin introducerile tale în aplicația web Sugar‑Sugar (chestionar de înregistrare, sarcini de predicție, încărcare CGM opțională). Nu sunt obținute date din alte surse. Temeiul juridic al prelucrării este consimțământul tău explicit conform art. 6 alin. 1 lit. a GDPR și art. 9 alin. 2 lit. a GDPR.",
        "5. În ce scopuri sunt necesare datele tale și cum sunt protejate?",
        "Datele menționate mai sus sunt necesare exclusiv pentru investigarea științifică a capacității umane de predicție a glucozei și sunt folosite doar în acest scop.",
        "Fiecărei persoane participante i se atribuie la înregistrare un ID de studiu aleator. Toate datele de cercetare sunt asociate exclusiv cu acest ID. Un fișier separat, criptat, de corespondență care asociază ID‑ul de studiu cu adresa de email este stocat separat și este accesibil doar conducerii studiului (Anton Kulaga și Livia Zaharia). Acest fișier este folosit exclusiv pentru gestionarea cererilor de retragere și notificarea opțională a rezultatelor. Pentru ceilalți membri ai studiului nu este posibilă identificarea ta.",
        "Datele sunt criptate în timpul transferului și în repaus. Stocarea are loc pe servere din Uniunea Europeană (hosting conform GDPR). Accesul este reglementat pe bază de roluri.",
        "6. Unde și pentru cât timp sunt stocate datele?",
        "Datele colectate în cadrul studiului sunt mai întâi pseudonimizate. Fișierul de corespondență (email – ID de studiu) este de așteptat să fie distrus la 12 luni după finalizarea studiului. După aceea, datele de studiu sunt anonimizate, adică nu mai permit nicio asociere cu persoana ta.",
        "Datele de cercetare pseudonimizate sunt păstrate 10 ani conform standardelor de cercetare din Germania. Fișierele brute CGM încărcate sunt șterse în 30 de zile.",
        "7. Cine are acces la datele tale? Sunt datele transmise sau publicate?",
        "Datele de cercetare pseudonimizate sunt accesibile doar echipei de studiu de la IBIMA. Fișierul de corespondență este accesibil doar conducerii studiului (Anton Kulaga și Livia Zaharia). Rezultatele studiului sunt publicate doar în formă agregată și anonimizată. Nu este posibilă identificarea persoanelor din publicații.",
        "8. Ce drepturi privind protecția datelor ai în cadrul participării la studiu?",
        "Conform reglementărilor aplicabile (GDPR), ai dreptul de acces la datele stocate, rectificarea datelor inexacte, ștergerea datelor, restricționarea prelucrării, opoziția față de prelucrări nejustificate și dreptul la portabilitatea datelor stocate despre tine. De asemenea, ai dreptul de a-ți retrage consimțământul. Aceste drepturi pot fi exercitate oricând față de instituția responsabilă.",
        "Dreptul de retragere",
        "În principiu, îți poți retrage consimțământul oricând fără a oferi motive. Te rugăm să contactezi conducerea studiului (anton.kulaga@uni-rostock.de). Retragerea produce efecte din momentul în care o transmiți. Prelucrarea datelor până la acel moment rămâne legală. În caz de retragere, se va iniția ștergerea datelor cu caracter personal. Datele de studiu deja anonimizate și care nu mai pot fi asociate cu tine vor continua să fie folosite în cadrul studiului. Fișierul de corespondență este de așteptat să fie distrus la 12 luni după finalizarea studiului; după aceea nu mai este posibilă asocierea individuală și, implicit, ștergerea.",
        "Temei juridic: art. 6 alin. 1 lit. a GDPR și art. 9 alin. 2 lit. a GDPR.",
        "Declarație de consimțământ",
        "pentru participarea la studiul Sugar‑Sugar de predicție a glucozei",
        "și prelucrarea de date asociată",
        "ID‑ul de studiu al persoanei participante: _________________________________ (atribuit la înregistrare)",
        "Consimțămintele de mai jos sunt înregistrate electronic la momentul înregistrării prin bifarea căsuțelor corespunzătoare.",
        "Particip voluntar la studiu. Am citit cu atenție informațiile pentru participanți și notele privind protecția datelor și drepturile asociate.",
        "Am fost informat(ă) că în cadrul studiului vor fi colectate, prelucrate și utilizate date cu caracter personal despre mine, în special date de sănătate (statutul diabetului, istoricul utilizării CGM, performanța predicției).",
        "Conform informațiilor pentru participanți, prelucrarea are loc în formă pseudonimizată de către echipa de studiu de la IBIMA, Universitätsmedizin Rostock. HEALES acționează ca împuternicit (processor) în cadrul unui AVV/DPA.",
        "Sunt conștient(ă) că, în cazul în care datele mele sunt stocate anonimizat, ștergerea lor la cererea mea nu mai este posibilă.",
        "Dreptul de retragere",
        "Am fost informat(ă) că îmi pot încheia participarea oricând fără a oferi motive, fără dezavantaje pentru mine. De asemenea, știu că îmi pot retrage consimțământul pentru prelucrarea datelor oricând, cu efect pentru viitor, fără a afecta legalitatea prelucrării efectuate până la retragere. Am luat la cunoștință informațiile privind retragerea consimțământului din informațiile pentru participanți aferente.",
        "Declar prin prezenta acordul meu voluntar de a participa la studiul Sugar‑Sugar de predicție a glucozei. Sunt conștient(ă) că îmi pot încheia participarea oricând fără a oferi motive, fără dezavantaje pentru mine.",
        "Îmi dau consimțământul (incluzând informațiile pentru participanți aferente) pentru prelucrarea datelor mele personale și de sănătate în următoarele scopuri:",
        "☐  Colectarea, prelucrarea și utilizarea datelor mele enumerate în informațiile pentru participanți, în special a datelor de sănătate (statutul diabetului, istoricul utilizării CGM, performanța predicției), în formă pseudonimizată pentru desfășurarea studiului de către echipa de la IBIMA, Universitätsmedizin Rostock, precum și de către HEALES ca împuternicit. Stocarea are loc pe servere din Uniunea Europeană. Datele de cercetare sunt păstrate până la 10 ani după anonimizarea fișierului de corespondență. Retragerea este posibilă până la 12 luni după finalizarea studiului; după aceea identificarea nu mai este posibilă. Temei juridic: art. 6 alin. 1 lit. a GDPR și art. 9 alin. 2 lit. a GDPR.",
        "☐  Persoana participantă confirmă că are 18 ani sau mai mult.",
        "Consimțăminte opționale (refuzul nu influențează participarea la studiu):",
        "☐  Sunt de acord să încarc propriile date CGM pentru sarcina opțională de predicție cu datele mele. Datele brute sunt șterse în 30 de zile; se păstrează doar segmentele extrase, pseudonimizate.",
        "☐  Sunt de acord ca echipa de studiu să mă informeze, prin adresa de email înregistrată, despre rezultatele studiului după publicare.",
        "Mesajele de la HEALES sau proiecte conexe vor fi prezentate pe o pagină separată după finalizarea studiului și sunt complet independente de participarea la studiu și de consimțământ.",
        "Acest studiu a fost prezentat Comisiei de Etică a Universitätsmedizin Rostock. Număr de înregistrare: Ref. number A 2026-0064. Primit de Comisia de Etică: 27 februarie 2026.",
        "Întrebări sau cereri de retragere: anton.kulaga@uni-rostock.de | livia.zaharia@uni-rostock.de",
    ],
}


def consent_notice_paragraphs(locale: Optional[str]) -> list[str]:
    # Backwards-compatible API used by older callers.
    # We keep this so existing code can still render non-German locales,
    # even though German now comes from markdown.
    loc = normalize_locale(locale)
    if loc == "de":
        md = consent_notice_markdown_de()
        return [x.strip() for x in md.splitlines() if x.strip()]
    translated = _CONSENT_NOTICE_TRANSLATIONS.get(loc)
    if translated is None:
        md = consent_notice_markdown_de()
        return [x.strip() for x in md.splitlines() if x.strip()]
    return translated


def consent_notice_children(locale: Optional[str]) -> list[object]:
    loc = normalize_locale(locale)

    # Prefer locale-specific markdown if it exists.
    md_candidates = []
    base = _consent_notice_md_path()
    if len(base.suffixes) >= 2 and base.suffixes[-2:] == [".docx", ".md"]:
        md_candidates.append(base.with_suffix(f".{loc}.md"))
    md_candidates.append(base.with_name(f"patient_consent_form.{loc}.md"))
    md_candidates.append(base.with_name(f"patient_consent_form_{loc}.md"))

    md_text = ""
    for p in md_candidates:
        md_text = _read_markdown_file(p)
        if md_text:
            break

    if not md_text:
        if loc == "de":
            md_text = consent_notice_markdown_de()
        else:
            # Fallback: join translated paragraphs into a readable markdown block.
            translated = _CONSENT_NOTICE_TRANSLATIONS.get(loc)
            if translated:
                md_text = _sanitize_markdown("\n\n".join(translated))
            else:
                md_text = consent_notice_markdown_de()

    # Style subtitles by exact-line matching (avoid partial replacements like "Data protection officer...").
    replacements = {
        "en": {
            "Participant information": "### Participant information",
            "Data protection": "### Data protection",
            "Right of withdrawal": "### Right of withdrawal",
        },
        "uk": {
            "Інформація для учасників": "### Інформація для учасників",
            "Захист даних": "### Захист даних",
            "Право на відкликання": "### Право на відкликання",
        },
        "ro": {
            "Informații pentru participanți": "### Informații pentru participanți",
            "Protecția datelor": "### Protecția datelor",
            "Dreptul de retragere": "### Dreptul de retragere",
        },
        "de": {
            "**Teilnehmerinformation**": "### Teilnehmerinformation",
            "## Datenschutz": "### Datenschutz",
            "## Widerrufsrecht": "### Widerrufsrecht",
        },
    }
    if loc in replacements:
        for old, new in replacements[loc].items():
            escaped_old = re.escape(old)
            md_text = re.sub(rf"(?m)^{escaped_old}\s*$", new, md_text)

    # Remove accidental heading styling from data protection officer line(s).
    officer_lines = [
        "Data protection officer of University Medicine Rostock",
        "Datenschutzbeauftragter der Universitätsmedizin Rostock",
        "Уповноважений із захисту даних Університетської медицини Ростока",
    ]
    for line in officer_lines:
        md_text = re.sub(rf"(?m)^###\s*{re.escape(line)}\s*$", line, md_text)

    # Make numbered lines bold
    md_text = re.sub(r"(\d+)\. ", r"**\1.** ", md_text)

    # Indent text after numbered lines until the next numbered line or heading.
    paragraphs = md_text.split("\n\n")
    out_text = ""
    first = True
    indent = False
    after_numbered = False

    for p in paragraphs:
        stripped = p.strip()
        is_heading = stripped.startswith("###")
        is_numbered = re.match(r"\*\*\d+\.\*\*", stripped)

        if is_heading:
            if not first:
                out_text += "\n\n"
            out_text += p
            first = False
            indent = False
            after_numbered = False
            continue

        if is_numbered:
            if not first:
                out_text += "\n\n"
            out_text += p
            first = False
            indent = True
            after_numbered = True
            continue

        if indent:
            # No blank line under numbered bullets; daughter paragraphs are indented directly.
            out_text += "\n" + f'<div style="margin-left: 20px;">{p}</div>'
            after_numbered = False
            continue

        # Standard paragraph spacing
        if not first:
            out_text += "\n\n"
        out_text += p
        first = False
        after_numbered = False

    md_text = out_text

    return [
        dcc.Markdown(
            md_text,
            link_target="_blank",
            dangerously_allow_html=True,
            style={"color": "#334155", "lineHeight": "1.6"},
        )
    ]

