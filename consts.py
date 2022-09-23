STOPWORDS = ["kolahtaa", "kolahtavaa", "tattista", "koniburger", "hidastavauhtia", "ukko", "mike",
             "lääkkeellisessä", "lääkkeet", "savutonttu"]

DRUG_CATEGORIES = ["kannabis", "amfetamiini", "kokaiini", "heroiini", "subutex", "ekstaasi", "laakkeet",
                   "hallusinogeenit"]

DRUGS = {
    "kannabis": ["blosse", "bubu", "budi", "budi", "cannabis", "dulla", "dänkki", "ganja", "hartsi", "hasa", "hasis",
                 "hatsi", "heinä", "hiivu", "huja", "höpöheinä", "indica", "kannabis", "kukinto", "kukka", "kukkaa",
                 "kush", "mari", "möyhy", "northern", "nuppu", "paja", "peeäl", "peruslät", "pilvi", "pl", "polttoa",
                 "qq", "ruoho", "sativa", "sauhu", "savu", "suomikuk", "trimmihei", "tötsy", "vihreetä", "yrtti"],

    "amfetamiini": ["A-vitamiini", "alakerta", "alis", "amfe", "amphetamine", "boogie", "dimetyylitryptamiini",
                    "dimitri", "dma", "kellari", "lirpakka", "meta", "metukka", "nopsa", "nopsa", "piiska", "piri",
                    "piristys", "piristävä", "pirjo", "pirkko", "pirpsakka", "pore", "porske", "pöhinä", "pörinä",
                    "spiidi", "spörre", "stimu", "sulfa", "swimba", "vauhti", "virta", "vitamiinia", "zygy"],

    "kokaiini": ["Coca-Cola", "Pepsi", "cocaine", "jeejou", "kokaiini", "kokis", "kokkeli", "koksu", "kola", "spägä",
                 "viivotin", "ylis", "yläkerta"],

    "heroiini": ["hepo", "heppa", "herksa", "heroiini", "heroin", "herska", "hevonen", "hidasta", "hitaita", "koni",
                 "kopukka", "polakka", "polle", "polska"],

    "subutex": ["8 pallo", "8-pallo", "buna", "bunalict", "bupr", "buvid", "buvidal", "kasipallo", "nors", "norspan",
                "orkki", "orkki" "subbana", "pubre", "subbari", "subo", "suboxone", "subu", "tekken", "teku", "temg",
                "temgesic", "texi", "texmex", "ässä"],

    "ekstaasi": ["eemeli", "eetä", "eksta", "ekstaasi", "empatogeen", "emppu", "esso", "mdma", "mäiske", "mämmi",
                 "mände", "mässy", "naksu", "seksimetku"],

    "laakkeet": ["2-CMC", "2-kloorimetkatinoni", "3-metoksifenmetratsiini", "4-HO-DPT", "4F-3-metyyli-α-PVP",
                 "N-etyyliheptedroni", "alfa", "alpr", "alpra", "attentin", "benjo", "bentso", "bentsyyli", "bzp",
                 "bzp", "clhorine", "deoksi", "deoksimetoksetamiini", "deoxy", "elvanse", "ethyl", "etizolam", "etyyli",
                 "fenta", "galenika", "gamma", "gamma", "gbl", "ghb", "ilokaasu", "keta", "ketku", "klona", "kloori",
                 "kloorifenyyli", "ksalol", "lakka", "levy", "lole", "loli", "lyric", "lääkk", "mcpp", "mdmb", "mephe",
                 "metadoni", "methox", "methyl", "metoksi", "metoksisopropamiini", "metyyli", "morf", "mutteri",
                 "napit", "nappeja", "oksi", "opamox", "opiaat", "opioidi", "oxy", "panac", "piperatsiini",
                 "pregabalin", "pvp", "relaks", "remima", "remimatsolaami", "rivatril", "rivoi", "telaketju", "telari",
                 "trama", "xanor"],

    "hallusinogeenit": ["LSD", "deelejä", "deeli", "hallu", "happo", "lappuja", "lsd" "lappu", "lysergi", "psilo",
                        "psykedeeli", "psyko", "psylo", "sieni", "taikasien", "tatti", "trippi"]
}
