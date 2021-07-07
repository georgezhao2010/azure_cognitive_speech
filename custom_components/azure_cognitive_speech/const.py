DOMAIN = "azure_cognitive_speech"
OPT_VOICE = "voice"
OPT_STYLE = "style"
OPT_ROLE = "role"
OPT_SPEED = "speed"
CONF_DEFAULT_VOICE = "default_voice"
DEFAULT_LANGUAGE = "zh-CN"
DEFAULT_VOICE = "Xiaoxiao"
ENDPOINT_URI = "https://{}.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
TTS_URL = "https://{}.tts.speech.microsoft.com/cognitiveservices/v1"
TOKEN_OUTDATE = 720
SUPPORT_LANGUAGES = [
    "ar-EG",
    "ar-SA",
    "bg-BG",
    "ca-ES",
    "cs-CZ",
    "cy-GB",
    "da-DK",
    "de-AT",
    "de-CH",
    "de-DE",
    "el-GR",
    "en-AU",
    "en-CA",
    "en-GB",
    "en-HK",
    "en-IE",
    "en-IN",
    "en-NZ",
    "en-PH",
    "en-SG",
    "en-US",
    "en-ZA",
    "es-AR",
    "es-CO",
    "es-ES",
    "es-MX",
    "es-US",
    "et-EE",
    "fi-FI",
    "fr-BE",
    "fr-CA",
    "fr-CH",
    "fr-FR",
    "ga-IE",
    "gu-IN",
    "he-IL",
    "hi-IN",
    "hr-HR",
    "hu-HU",
    "id-ID",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "lt-LT",
    "lv-LV",
    "mr-IN",
    "ms-MY",
    "mt-MT",
    "nb-NO",
    "nl-BE",
    "nl-NL",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "sk-SK",
    "sl-SI",
    "sv-SE",
    "sw-KE",
    "ta-IN",
    "te-IN",
    "th-TH",
    "tr-TR",
    "uk-UA",
    "ur-PK",
    "vi-VN",
    "zh-CN",
    "zh-HK",
    "zh-TW"
]

VOICES_LIST = {
    "Salma": {
        "ShortName": "ar-EG-SalmaNeural",
        "Gender": "Female",
        "Locale": "ar-EG"
    },
    "Shakir": {
        "ShortName": "ar-EG-ShakirNeural",
        "Gender": "Male",
        "Locale": "ar-EG"
    },
    "Hoda": {
        "ShortName": "ar-EG-Hoda",
        "Gender": "Female",
        "Locale": "ar-EG"
    },
    "Hamed": {
        "ShortName": "ar-SA-HamedNeural",
        "Gender": "Male",
        "Locale": "ar-SA"
    },
    "Zariyah": {
        "ShortName": "ar-SA-ZariyahNeural",
        "Gender": "Female",
        "Locale": "ar-SA"
    },
    "Naayf": {
        "ShortName": "ar-SA-Naayf",
        "Gender": "Male",
        "Locale": "ar-SA"
    },
    "Borislav": {
        "ShortName": "bg-BG-BorislavNeural",
        "Gender": "Male",
        "Locale": "bg-BG"
    },
    "Kalina": {
        "ShortName": "bg-BG-KalinaNeural",
        "Gender": "Female",
        "Locale": "bg-BG"
    },
    "Ivan": {
        "ShortName": "bg-BG-Ivan",
        "Gender": "Male",
        "Locale": "bg-BG"
    },
    "Joana": {
        "ShortName": "ca-ES-JoanaNeural",
        "Gender": "Female",
        "Locale": "ca-ES"
    },
    "Alba": {
        "ShortName": "ca-ES-AlbaNeural",
        "Gender": "Female",
        "Locale": "ca-ES"
    },
    "Enric": {
        "ShortName": "ca-ES-EnricNeural",
        "Gender": "Male",
        "Locale": "ca-ES"
    },
    "Herena": {
        "ShortName": "ca-ES-HerenaRUS",
        "Gender": "Female",
        "Locale": "ca-ES"
    },
    "Antonin": {
        "ShortName": "cs-CZ-AntoninNeural",
        "Gender": "Male",
        "Locale": "cs-CZ"
    },
    "Vlasta": {
        "ShortName": "cs-CZ-VlastaNeural",
        "Gender": "Female",
        "Locale": "cs-CZ"
    },
    "Jakub": {
        "ShortName": "cs-CZ-Jakub",
        "Gender": "Male",
        "Locale": "cs-CZ"
    },
    "Aled": {
        "ShortName": "cy-GB-AledNeural",
        "Gender": "Male",
        "Locale": "cy-GB"
    },
    "Nia": {
        "ShortName": "cy-GB-NiaNeural",
        "Gender": "Female",
        "Locale": "cy-GB"
    },
    "Christel": {
        "ShortName": "da-DK-ChristelNeural",
        "Gender": "Female",
        "Locale": "da-DK"
    },
    "Jeppe": {
        "ShortName": "da-DK-JeppeNeural",
        "Gender": "Male",
        "Locale": "da-DK"
    },
    "Helle": {
        "ShortName": "da-DK-HelleRUS",
        "Gender": "Female",
        "Locale": "da-DK"
    },
    "Ingrid": {
        "ShortName": "de-AT-IngridNeural",
        "Gender": "Female",
        "Locale": "de-AT"
    },
    "Jonas": {
        "ShortName": "de-AT-JonasNeural",
        "Gender": "Male",
        "Locale": "de-AT"
    },
    "Michael": {
        "ShortName": "de-AT-Michael",
        "Gender": "Male",
        "Locale": "de-AT"
    },
    "Jan": {
        "ShortName": "de-CH-JanNeural",
        "Gender": "Male",
        "Locale": "de-CH"
    },
    "Leni": {
        "ShortName": "de-CH-LeniNeural",
        "Gender": "Female",
        "Locale": "de-CH"
    },
    "Karsten": {
        "ShortName": "de-CH-Karsten",
        "Gender": "Male",
        "Locale": "de-CH"
    },
    "Katja": {
        "ShortName": "de-DE-KatjaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
    "Conrad": {
        "ShortName": "de-DE-ConradNeural",
        "Gender": "Male",
        "Locale": "de-DE"
    },
    "Hedda": {
        "ShortName": "de-DE-HeddaRUS",
        "Gender": "Female",
        "Locale": "de-DE"
    },
    "Stefan": {
        "ShortName": "de-DE-Stefan",
        "Gender": "Male",
        "Locale": "de-DE"
    },
    "Athina": {
        "ShortName": "el-GR-AthinaNeural",
        "Gender": "Female",
        "Locale": "el-GR"
    },
    "Nestoras": {
        "ShortName": "el-GR-NestorasNeural",
        "Gender": "Male",
        "Locale": "el-GR"
    },
    "Stefanos": {
        "ShortName": "el-GR-Stefanos",
        "Gender": "Male",
        "Locale": "el-GR"
    },
    "Natasha": {
        "ShortName": "en-AU-NatashaNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "William": {
        "ShortName": "en-AU-WilliamNeural",
        "Gender": "Male",
        "Locale": "en-AU"
    },
    "Catherine": {
        "ShortName": "en-AU-Catherine",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Hayley": {
        "ShortName": "en-AU-HayleyRUS",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Clara": {
        "ShortName": "en-CA-ClaraNeural",
        "Gender": "Female",
        "Locale": "en-CA"
    },
    "Liam": {
        "ShortName": "en-CA-LiamNeural",
        "Gender": "Male",
        "Locale": "en-CA"
    },
    "Heather": {
        "ShortName": "en-CA-HeatherRUS",
        "Gender": "Female",
        "Locale": "en-CA"
    },
    "Linda": {
        "ShortName": "en-CA-Linda",
        "Gender": "Female",
        "Locale": "en-CA"
    },
    "Libby": {
        "ShortName": "en-GB-LibbyNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Mia": {
        "ShortName": "en-GB-MiaNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Ryan": {
        "ShortName": "en-GB-RyanNeural",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "George": {
        "ShortName": "en-GB-George",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "Hazel": {
        "ShortName": "en-GB-HazelRUS",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Susan": {
        "ShortName": "en-GB-Susan",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Sam": {
        "ShortName": "en-HK-SamNeural",
        "Gender": "Male",
        "Locale": "en-HK"
    },
    "Yan": {
        "ShortName": "en-HK-YanNeural",
        "Gender": "Female",
        "Locale": "en-HK"
    },
    "Connor": {
        "ShortName": "en-IE-ConnorNeural",
        "Gender": "Male",
        "Locale": "en-IE"
    },
    "Emily": {
        "ShortName": "en-IE-EmilyNeural",
        "Gender": "Female",
        "Locale": "en-IE"
    },
    "Sean": {
        "ShortName": "en-IE-Sean",
        "Gender": "Male",
        "Locale": "en-IE"
    },
    "Neerja": {
        "ShortName": "en-IN-NeerjaNeural",
        "Gender": "Female",
        "Locale": "en-IN"
    },
    "Prabhat": {
        "ShortName": "en-IN-PrabhatNeural",
        "Gender": "Male",
        "Locale": "en-IN"
    },
    "Heera": {
        "ShortName": "en-IN-Heera",
        "Gender": "Female",
        "Locale": "en-IN"
    },
    "Priya": {
        "ShortName": "en-IN-PriyaRUS",
        "Gender": "Female",
        "Locale": "en-IN"
    },
    "Ravi": {
        "ShortName": "en-IN-Ravi",
        "Gender": "Male",
        "Locale": "en-IN"
    },
    "Mitchell": {
        "ShortName": "en-NZ-MitchellNeural",
        "Gender": "Male",
        "Locale": "en-NZ"
    },
    "Molly": {
        "ShortName": "en-NZ-MollyNeural",
        "Gender": "Female",
        "Locale": "en-NZ"
    },
    "James": {
        "ShortName": "en-PH-JamesNeural",
        "Gender": "Male",
        "Locale": "en-PH"
    },
    "Rosa": {
        "ShortName": "en-PH-RosaNeural",
        "Gender": "Female",
        "Locale": "en-PH"
    },
    "Luna": {
        "ShortName": "en-SG-LunaNeural",
        "Gender": "Female",
        "Locale": "en-SG"
    },
    "Wayne": {
        "ShortName": "en-SG-WayneNeural",
        "Gender": "Male",
        "Locale": "en-SG"
    },
    "Jenny": {
        "ShortName": "en-US-JennyNeural",
        "Gender": "Female",
        "Locale": "en-US",
        "StyleList": [
            "assistant",
            "chat",
            "customerservice",
            "newscast"
        ]
    },
    "Jenny Multilingual": {
        "ShortName": "en-US-JennyMultilingualNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Guy": {
        "ShortName": "en-US-GuyRUS",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Aria": {
        "ShortName": "en-US-AriaRUS",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Amber": {
        "ShortName": "en-US-AmberNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Ana": {
        "ShortName": "en-US-AnaNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Ashley": {
        "ShortName": "en-US-AshleyNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Brandon": {
        "ShortName": "en-US-BrandonNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Christopher": {
        "ShortName": "en-US-ChristopherNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Cora": {
        "ShortName": "en-US-CoraNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Elizabeth": {
        "ShortName": "en-US-ElizabethNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Eric": {
        "ShortName": "en-US-EricNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Jacob": {
        "ShortName": "en-US-JacobNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Michelle": {
        "ShortName": "en-US-MichelleNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Monica": {
        "ShortName": "en-US-MonicaNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Benjamin": {
        "ShortName": "en-US-BenjaminRUS",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Zira": {
        "ShortName": "en-US-ZiraRUS",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Leah": {
        "ShortName": "en-ZA-LeahNeural",
        "Gender": "Female",
        "Locale": "en-ZA"
    },
    "Luke": {
        "ShortName": "en-ZA-LukeNeural",
        "Gender": "Male",
        "Locale": "en-ZA"
    },
    "Elena": {
        "ShortName": "es-AR-ElenaNeural",
        "Gender": "Female",
        "Locale": "es-AR"
    },
    "Tomas": {
        "ShortName": "es-AR-TomasNeural",
        "Gender": "Male",
        "Locale": "es-AR"
    },
    "Gonzalo": {
        "ShortName": "es-CO-GonzaloNeural",
        "Gender": "Male",
        "Locale": "es-CO"
    },
    "Salome": {
        "ShortName": "es-CO-SalomeNeural",
        "Gender": "Female",
        "Locale": "es-CO"
    },
    "Alvaro": {
        "ShortName": "es-ES-AlvaroNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Elvira": {
        "ShortName": "es-ES-ElviraNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Helena": {
        "ShortName": "es-ES-HelenaRUS",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Laura": {
        "ShortName": "es-ES-Laura",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Pablo": {
        "ShortName": "es-ES-Pablo",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Dalia": {
        "ShortName": "es-MX-DaliaNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Jorge": {
        "ShortName": "es-MX-JorgeNeural",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Hilda": {
        "ShortName": "es-MX-HildaRUS",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Raul": {
        "ShortName": "es-MX-Raul",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Alonso": {
        "ShortName": "es-US-AlonsoNeural",
        "Gender": "Male",
        "Locale": "es-US"
    },
    "Paloma": {
        "ShortName": "es-US-PalomaNeural",
        "Gender": "Female",
        "Locale": "es-US"
    },
    "Anu": {
        "ShortName": "et-EE-AnuNeural",
        "Gender": "Female",
        "Locale": "et-EE"
    },
    "Kert": {
        "ShortName": "et-EE-KertNeural",
        "Gender": "Male",
        "Locale": "et-EE"
    },
    "Selma": {
        "ShortName": "fi-FI-SelmaNeural",
        "Gender": "Female",
        "Locale": "fi-FI"
    },
    "Harri": {
        "ShortName": "fi-FI-HarriNeural",
        "Gender": "Male",
        "Locale": "fi-FI"
    },
    "Noora": {
        "ShortName": "fi-FI-NooraNeural",
        "Gender": "Female",
        "Locale": "fi-FI"
    },
    "Heidi": {
        "ShortName": "fi-FI-HeidiRUS",
        "Gender": "Female",
        "Locale": "fi-FI"
    },
    "Charline": {
        "ShortName": "fr-BE-CharlineNeural",
        "Gender": "Female",
        "Locale": "fr-BE"
    },
    "Gerard": {
        "ShortName": "fr-BE-GerardNeural",
        "Gender": "Male",
        "Locale": "fr-BE"
    },
    "Sylvie": {
        "ShortName": "fr-CA-SylvieNeural",
        "Gender": "Female",
        "Locale": "fr-CA"
    },
    "Antoine": {
        "ShortName": "fr-CA-AntoineNeural",
        "Gender": "Male",
        "Locale": "fr-CA"
    },
    "Jean": {
        "ShortName": "fr-CA-JeanNeural",
        "Gender": "Male",
        "Locale": "fr-CA"
    },
    "Caroline": {
        "ShortName": "fr-CA-Caroline",
        "Gender": "Female",
        "Locale": "fr-CA"
    },
    "Harmonie": {
        "ShortName": "fr-CA-HarmonieRUS",
        "Gender": "Female",
        "Locale": "fr-CA"
    },
    "Ariane": {
        "ShortName": "fr-CH-ArianeNeural",
        "Gender": "Female",
        "Locale": "fr-CH"
    },
    "Fabrice": {
        "ShortName": "fr-CH-FabriceNeural",
        "Gender": "Male",
        "Locale": "fr-CH"
    },
    "Guillaume": {
        "ShortName": "fr-CH-Guillaume",
        "Gender": "Male",
        "Locale": "fr-CH"
    },
    "Denise": {
        "ShortName": "fr-FR-DeniseNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Henri": {
        "ShortName": "fr-FR-HenriNeural",
        "Gender": "Male",
        "Locale": "fr-FR"
    },
    "Hortense": {
        "ShortName": "fr-FR-HortenseRUS",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Julie": {
        "ShortName": "fr-FR-Julie",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Paul": {
        "ShortName": "fr-FR-Paul",
        "Gender": "Male",
        "Locale": "fr-FR"
    },
    "Colm": {
        "ShortName": "ga-IE-ColmNeural",
        "Gender": "Male",
        "Locale": "ga-IE"
    },
    "Orla": {
        "ShortName": "ga-IE-OrlaNeural",
        "Gender": "Female",
        "Locale": "ga-IE"
    },
    "Dhwani": {
        "ShortName": "gu-IN-DhwaniNeural",
        "Gender": "Female",
        "Locale": "gu-IN"
    },
    "Niranjan": {
        "ShortName": "gu-IN-NiranjanNeural",
        "Gender": "Male",
        "Locale": "gu-IN"
    },
    "Avri": {
        "ShortName": "he-IL-AvriNeural",
        "Gender": "Male",
        "Locale": "he-IL"
    },
    "Hila": {
        "ShortName": "he-IL-HilaNeural",
        "Gender": "Male",
        "Locale": "he-IL"
    },
    "Asaf": {
        "ShortName": "he-IL-Asaf",
        "Gender": "Male",
        "Locale": "he-IL"
    },
    "Madhur": {
        "ShortName": "hi-IN-MadhurNeural",
        "Gender": "Male",
        "Locale": "hi-IN"
    },
    "Swara": {
        "ShortName": "hi-IN-SwaraNeural",
        "Gender": "Female",
        "Locale": "hi-IN"
    },
    "Hemant": {
        "ShortName": "hi-IN-Hemant",
        "Gender": "Male",
        "Locale": "hi-IN"
    },
    "Kalpana": {
        "ShortName": "hi-IN-Kalpana",
        "Gender": "Female",
        "Locale": "hi-IN"
    },
    "Gabrijela": {
        "ShortName": "hr-HR-GabrijelaNeural",
        "Gender": "Female",
        "Locale": "hr-HR"
    },
    "Srecko": {
        "ShortName": "hr-HR-SreckoNeural",
        "Gender": "Male",
        "Locale": "hr-HR"
    },
    "Matej": {
        "ShortName": "hr-HR-Matej",
        "Gender": "Male",
        "Locale": "hr-HR"
    },
    "Noemi": {
        "ShortName": "hu-HU-NoemiNeural",
        "Gender": "Female",
        "Locale": "hu-HU"
    },
    "Tamas": {
        "ShortName": "hu-HU-TamasNeural",
        "Gender": "Male",
        "Locale": "hu-HU"
    },
    "Szabolcs": {
        "ShortName": "hu-HU-Szabolcs",
        "Gender": "Male",
        "Locale": "hu-HU"
    },
    "Ardi": {
        "ShortName": "id-ID-ArdiNeural",
        "Gender": "Male",
        "Locale": "id-ID"
    },
    "Gadis": {
        "ShortName": "id-ID-GadisNeural",
        "Gender": "Female",
        "Locale": "id-ID"
    },
    "Andika": {
        "ShortName": "id-ID-Andika",
        "Gender": "Male",
        "Locale": "id-ID"
    },
    "Isabella": {
        "ShortName": "it-IT-IsabellaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Diego": {
        "ShortName": "it-IT-DiegoNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Elsa": {
        "ShortName": "it-IT-ElsaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Cosimo": {
        "ShortName": "it-IT-Cosimo",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Lucia": {
        "ShortName": "it-IT-LuciaRUS",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Nanami": {
        "ShortName": "ja-JP-NanamiNeural",
        "Gender": "Female",
        "Locale": "ja-JP"
    },
    "Keita": {
        "ShortName": "ja-JP-KeitaNeural",
        "Gender": "Male",
        "Locale": "ja-JP"
    },
    "Ayumi": {
        "ShortName": "ja-JP-Ayumi",
        "Gender": "Female",
        "Locale": "ja-JP"
    },
    "Haruka": {
        "ShortName": "ja-JP-HarukaRUS",
        "Gender": "Female",
        "Locale": "ja-JP"
    },
    "Ichiro": {
        "ShortName": "ja-JP-Ichiro",
        "Gender": "Male",
        "Locale": "ja-JP"
    },
    "Sun-Hi": {
        "ShortName": "ko-KR-SunHiNeural",
        "Gender": "Female",
        "Locale": "ko-KR"
    },
    "InJoon": {
        "ShortName": "ko-KR-InJoonNeural",
        "Gender": "Male",
        "Locale": "ko-KR"
    },
    "Heami": {
        "ShortName": "ko-KR-HeamiRUS",
        "Gender": "Female",
        "Locale": "ko-KR"
    },
    "Leonas": {
        "ShortName": "lt-LT-LeonasNeural",
        "Gender": "Male",
        "Locale": "lt-LT"
    },
    "Ona": {
        "ShortName": "lt-LT-OnaNeural",
        "Gender": "Female",
        "Locale": "lt-LT"
    },
    "Everita": {
        "ShortName": "lv-LV-EveritaNeural",
        "Gender": "Female",
        "Locale": "lv-LV"
    },
    "Nils": {
        "ShortName": "lv-LV-NilsNeural",
        "Gender": "Male",
        "Locale": "lv-LV"
    },
    "Aarohi": {
        "ShortName": "mr-IN-AarohiNeural",
        "Gender": "Female",
        "Locale": "mr-IN"
    },
    "Manohar": {
        "ShortName": "mr-IN-ManoharNeural",
        "Gender": "Male",
        "Locale": "mr-IN"
    },
    "Osman": {
        "ShortName": "ms-MY-OsmanNeural",
        "Gender": "Male",
        "Locale": "ms-MY"
    },
    "Yasmin": {
        "ShortName": "ms-MY-YasminNeural",
        "Gender": "Female",
        "Locale": "ms-MY"
    },
    "Rizwan": {
        "ShortName": "ms-MY-Rizwan",
        "Gender": "Male",
        "Locale": "ms-MY"
    },
    "Grace": {
        "ShortName": "mt-MT-GraceNeural",
        "Gender": "Female",
        "Locale": "mt-MT"
    },
    "Joseph": {
        "ShortName": "mt-MT-JosephNeural",
        "Gender": "Male",
        "Locale": "mt-MT"
    },
    "Pernille": {
        "ShortName": "nb-NO-PernilleNeural",
        "Gender": "Female",
        "Locale": "nb-NO"
    },
    "Finn": {
        "ShortName": "nb-NO-FinnNeural",
        "Gender": "Male",
        "Locale": "nb-NO"
    },
    "Iselin": {
        "ShortName": "nb-NO-IselinNeural",
        "Gender": "Female",
        "Locale": "nb-NO"
    },
    "Hulda": {
        "ShortName": "nb-NO-HuldaRUS",
        "Gender": "Female",
        "Locale": "nb-NO"
    },
    "Arnaud": {
        "ShortName": "nl-BE-ArnaudNeural",
        "Gender": "Male",
        "Locale": "nl-BE"
    },
    "Dena": {
        "ShortName": "nl-BE-DenaNeural",
        "Gender": "Female",
        "Locale": "nl-BE"
    },
    "Colette": {
        "ShortName": "nl-NL-ColetteNeural",
        "Gender": "Female",
        "Locale": "nl-NL"
    },
    "Fenna": {
        "ShortName": "nl-NL-FennaNeural",
        "Gender": "Female",
        "Locale": "nl-NL"
    },
    "Maarten": {
        "ShortName": "nl-NL-MaartenNeural",
        "Gender": "Male",
        "Locale": "nl-NL"
    },
    "Hanna": {
        "ShortName": "nl-NL-HannaRUS",
        "Gender": "Female",
        "Locale": "nl-NL"
    },
    "Agnieszka": {
        "ShortName": "pl-PL-AgnieszkaNeural",
        "Gender": "Female",
        "Locale": "pl-PL"
    },
    "Marek": {
        "ShortName": "pl-PL-MarekNeural",
        "Gender": "Male",
        "Locale": "pl-PL"
    },
    "Zofia": {
        "ShortName": "pl-PL-ZofiaNeural",
        "Gender": "Female",
        "Locale": "pl-PL"
    },
    "Paulina": {
        "ShortName": "pl-PL-PaulinaRUS",
        "Gender": "Female",
        "Locale": "pl-PL"
    },
    "Francisca": {
        "ShortName": "pt-BR-FranciscaNeural",
        "Gender": "Female",
        "Locale": "pt-BR",
        "StyleList": [
            "calm"
        ]
    },
    "Antonio": {
        "ShortName": "pt-BR-AntonioNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Daniel": {
        "ShortName": "pt-BR-Daniel",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Heloisa": {
        "ShortName": "pt-BR-HeloisaRUS",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Duarte": {
        "ShortName": "pt-PT-DuarteNeural",
        "Gender": "Male",
        "Locale": "pt-PT"
    },
    "Fernanda": {
        "ShortName": "pt-PT-FernandaNeural",
        "Gender": "Female",
        "Locale": "pt-PT"
    },
    "Raquel": {
        "ShortName": "pt-PT-RaquelNeural",
        "Gender": "Female",
        "Locale": "pt-PT"
    },
    "Helia": {
        "ShortName": "pt-PT-HeliaRUS",
        "Gender": "Female",
        "Locale": "pt-PT"
    },
    "Alina": {
        "ShortName": "ro-RO-AlinaNeural",
        "Gender": "Female",
        "Locale": "ro-RO"
    },
    "Emil": {
        "ShortName": "ro-RO-EmilNeural",
        "Gender": "Male",
        "Locale": "ro-RO"
    },
    "Andrei": {
        "ShortName": "ro-RO-Andrei",
        "Gender": "Male",
        "Locale": "ro-RO"
    },
    "Svetlana": {
        "ShortName": "ru-RU-SvetlanaNeural",
        "Gender": "Female",
        "Locale": "ru-RU"
    },
    "Dariya": {
        "ShortName": "ru-RU-DariyaNeural",
        "Gender": "Female",
        "Locale": "ru-RU"
    },
    "Dmitry": {
        "ShortName": "ru-RU-DmitryNeural",
        "Gender": "Male",
        "Locale": "ru-RU"
    },
    "Ekaterina": {
        "ShortName": "ru-RU-EkaterinaRUS",
        "Gender": "Female",
        "Locale": "ru-RU"
    },
    "Irina": {
        "ShortName": "ru-RU-Irina",
        "Gender": "Female",
        "Locale": "ru-RU"
    },
    "Pavel": {
        "ShortName": "ru-RU-Pavel",
        "Gender": "Male",
        "Locale": "ru-RU"
    },
    "Lukas": {
        "ShortName": "sk-SK-LukasNeural",
        "Gender": "Male",
        "Locale": "sk-SK"
    },
    "Viktoria": {
        "ShortName": "sk-SK-ViktoriaNeural",
        "Gender": "Female",
        "Locale": "sk-SK"
    },
    "Filip": {
        "ShortName": "sk-SK-Filip",
        "Gender": "Male",
        "Locale": "sk-SK"
    },
    "Petra": {
        "ShortName": "sl-SI-PetraNeural",
        "Gender": "Female",
        "Locale": "sl-SI"
    },
    "Rok": {
        "ShortName": "sl-SI-RokNeural",
        "Gender": "Male",
        "Locale": "sl-SI"
    },
    "Lado": {
        "ShortName": "sl-SI-Lado",
        "Gender": "Male",
        "Locale": "sl-SI"
    },
    "Sofie": {
        "ShortName": "sv-SE-SofieNeural",
        "Gender": "Female",
        "Locale": "sv-SE"
    },
    "Hillevi": {
        "ShortName": "sv-SE-HilleviNeural",
        "Gender": "Female",
        "Locale": "sv-SE"
    },
    "Mattias": {
        "ShortName": "sv-SE-MattiasNeural",
        "Gender": "Male",
        "Locale": "sv-SE"
    },
    "Hedvig": {
        "ShortName": "sv-SE-HedvigRUS",
        "Gender": "Female",
        "Locale": "sv-SE"
    },
    "Rafiki": {
        "ShortName": "sw-KE-RafikiNeural",
        "Gender": "Male",
        "Locale": "sw-KE"
    },
    "Zuri": {
        "ShortName": "sw-KE-ZuriNeural",
        "Gender": "Female",
        "Locale": "sw-KE"
    },
    "Pallavi": {
        "ShortName": "ta-IN-PallaviNeural",
        "Gender": "Female",
        "Locale": "ta-IN"
    },
    "Valluvar": {
        "ShortName": "ta-IN-Valluvar",
        "Gender": "Male",
        "Locale": "ta-IN"
    },
    "Mohan": {
        "ShortName": "te-IN-MohanNeural",
        "Gender": "Male",
        "Locale": "te-IN"
    },
    "Shruti": {
        "ShortName": "te-IN-ShrutiNeural",
        "Gender": "Female",
        "Locale": "te-IN"
    },
    "Chitra": {
        "ShortName": "te-IN-Chitra",
        "Gender": "Female",
        "Locale": "te-IN"
    },
    "Premwadee": {
        "ShortName": "th-TH-PremwadeeNeural",
        "Gender": "Female",
        "Locale": "th-TH"
    },
    "Achara": {
        "ShortName": "th-TH-AcharaNeural",
        "Gender": "Female",
        "Locale": "th-TH"
    },
    "Niwat": {
        "ShortName": "th-TH-NiwatNeural",
        "Gender": "Male",
        "Locale": "th-TH"
    },
    "Pattara": {
        "ShortName": "th-TH-Pattara",
        "Gender": "Male",
        "Locale": "th-TH"
    },
    "Ahmet": {
        "ShortName": "tr-TR-AhmetNeural",
        "Gender": "Male",
        "Locale": "tr-TR"
    },
    "Emel": {
        "ShortName": "tr-TR-EmelNeural",
        "Gender": "Female",
        "Locale": "tr-TR"
    },
    "Seda": {
        "ShortName": "tr-TR-SedaRUS",
        "Gender": "Female",
        "Locale": "tr-TR"
    },
    "Ostap": {
        "ShortName": "uk-UA-OstapNeural",
        "Gender": "Male",
        "Locale": "uk-UA"
    },
    "Polina": {
        "ShortName": "uk-UA-PolinaNeural",
        "Gender": "Female",
        "Locale": "uk-UA"
    },
    "Asad": {
        "ShortName": "ur-PK-AsadNeural",
        "Gender": "Male",
        "Locale": "ur-PK"
    },
    "Uzma": {
        "ShortName": "ur-PK-UzmaNeural",
        "Gender": "Female",
        "Locale": "ur-PK"
    },
    "HoaiMy": {
        "ShortName": "vi-VN-HoaiMyNeural",
        "Gender": "Female",
        "Locale": "vi-VN"
    },
    "NamMinh": {
        "ShortName": "vi-VN-NamMinhNeural",
        "Gender": "Male",
        "Locale": "vi-VN"
    },
    "An": {
        "ShortName": "vi-VN-An",
        "Gender": "Male",
        "Locale": "vi-VN"
    },
    "Xiaoxiao": {
        "ShortName": "zh-CN-XiaoxiaoNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "assistant",
            "chat",
            "customerservice",
            "newscast",
            "affectionate",
            "angry",
            "calm",
            "cheerful",
            "disgruntled",
            "fearful",
            "gentle",
            "lyrical",
            "sad",
            "serious"
        ]
    },
    "Yunyang": {
        "ShortName": "zh-CN-YunyangNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "customerservice",
            "narration"
        ]
    },
    "Xiaohan": {
        "ShortName": "zh-CN-XiaohanNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "calm",
            "fearful",
            "cheerful",
            "disgruntled",
            "serious",
            "angry",
            "sad",
            "gentle",
            "affectionate",
            "embarrassed"
        ]
    },
    "Xiaomo": {
        "ShortName": "zh-CN-XiaomoNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "calm",
            "fearful",
            "cheerful",
            "disgruntled",
            "serious",
            "angry",
            "gentle",
            "depressed"
        ],
        "RolePlayList": [
            "YoungAdultFemale",
            "YoungAdultMale",
            "OlderAdultFemale",
            "OlderAdultMale",
            "SeniorFemale",
            "SeniorMale",
            "Girl",
            "Boy"
        ]
    },
    "Xiaorui": {
        "ShortName": "zh-CN-XiaoruiNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "calm",
            "fearful",
            "angry",
            "sad"
        ]
    },
    "Xiaoxuan": {
        "ShortName": "zh-CN-XiaoxuanNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "calm",
            "fearful",
            "cheerful",
            "disgruntled",
            "serious",
            "angry",
            "gentle",
            "depressed"
        ],
        "RolePlayList": [
            "YoungAdultFemale",
            "YoungAdultMale",
            "OlderAdultFemale",
            "OlderAdultMale",
            "SeniorFemale",
            "SeniorMale",
            "Girl",
            "Boy"
        ]
    },
    "Xiaoyou": {
        "ShortName": "zh-CN-XiaoyouNeural",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "Yunxi": {
        "ShortName": "zh-CN-YunxiNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "assistant",
            "calm",
            "fearful",
            "cheerful",
            "disgruntled",
            "serious",
            "angry",
            "sad",
            "depressed",
            "embarrassed"
        ]
    },
    "Yunye": {
        "ShortName": "zh-CN-YunyeNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "calm",
            "fearful",
            "cheerful",
            "disgruntled",
            "serious",
            "angry",
            "sad"
        ]
    },
    "Huihui": {
        "ShortName": "zh-CN-HuihuiRUS",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "Kangkang": {
        "ShortName": "zh-CN-Kangkang",
        "Gender": "Male",
        "Locale": "zh-CN"
    },
    "Yaoyao": {
        "ShortName": "zh-CN-Yaoyao",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "HiuMaan": {
        "ShortName": "zh-HK-HiuMaanNeural",
        "Gender": "Female",
        "Locale": "zh-HK"
    },
    "HiuGaai": {
        "ShortName": "zh-HK-HiuGaaiNeural",
        "Gender": "Female",
        "Locale": "zh-HK"
    },
    "WanLung": {
        "ShortName": "zh-HK-WanLungNeural",
        "Gender": "Male",
        "Locale": "zh-HK"
    },
    "Danny": {
        "ShortName": "zh-HK-Danny",
        "Gender": "Male",
        "Locale": "zh-HK"
    },
    "Tracy": {
        "ShortName": "zh-HK-TracyRUS",
        "Gender": "Female",
        "Locale": "zh-HK"
    },
    "HsiaoChen": {
        "ShortName": "zh-TW-HsiaoChenNeural",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "HsiaoYu": {
        "ShortName": "zh-TW-HsiaoYuNeural",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "YunJhe": {
        "ShortName": "zh-TW-YunJheNeural",
        "Gender": "Male",
        "Locale": "zh-TW"
    },
    "HanHan": {
        "ShortName": "zh-TW-HanHanRUS",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "Yating": {
        "ShortName": "zh-TW-Yating",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "Zhiwei": {
        "ShortName": "zh-TW-Zhiwei",
        "Gender": "Male",
        "Locale": "zh-TW"
    }
}
