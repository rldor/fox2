#def sh():
#with open('bio.txt') as f:
#    s1 = list(f)
def cards(s):
    return s.split(';')

#r = open('rules.txt', 'r')
#rules_needed_to_red = r.readlines()
#rules=''
#for i in rules_needed_to_red:
#    rules+=i

m = ['PAIN(t)', 'ALLIGATOR', 'MIME', 'MIRROR']
s_bio = 'Abiotic environment : Абиотическая среда;Species : Вид;Anthropogenic factor : Антропогенные факторы;Immunity : Иммунитет;Zygote : Зигота;Embryo : Зародыш;Differentiation : Дифференцировка;Cell : Клетка;Biological indicators : Биоиндикаторы;Biomass : Биомасса;Biosphere : Биосфера;Biocenosis : Биоценоз;Gamete : Гамета;Generative organs : Генеративные органы;Hybridization : Гибридизация;Metabolism : Обмен веществ;Organism : Организм;Organ : Орган;Fertilization : Оплодотворение;Population : Популяция;Selection : Селекция;Symbiosis : Симбиоз;Systematics : Систематика;Cytoplasm : Цитоплазма;Evolution : Эволюция;Unicellular : Одноклеточные;Chromosomes : Хромосомы'
s_bot = 'Higher plants : Высшие растения;Lower plants : Низшие растения;Leukoplast : Лейкопласт;Gymnosperms : Голосеменные растения;Hygrophytes : Гигрофиты;Hydrophytes : Гидрофиты;Monoecious plants : Однодомные растения;Endosperm : Эндосперм;Cellulose (fiber) : Целлюлоза (клетчатка);Chloroplasts : Хлоропласты;Chromatophore : Хроматофор;Chromoplasts : Хромопласты;Angiosperms : Покрытосемянные;Photosynthesis : Фотосинтез;Annual plants : Однолетники;Same-sex flowers : Однополые цветки;Perianth : Околоцветник;Pollination : Опыление'
s_bh = 'Antibiotics : Антибиотики;Amino acid : Аминокислоты;Hormones : Гормоны;Fats : Жиры;Antioxidants : Антиоксиданты;Biochemistry : Биохимия;Proteins : Белки;Nucleic acid : Нуклеиновые кислоты;Organic matter : Органические вещества;Carbohydrates : Углеводы;Macronutrient : Макроэлемент;Micronutrient : Микроэлемент'
s_chem_easy = 'Absorption : Абсорбция;Allotropy : Аллотропия;Atomic weight : Атомный вес;Atom : Атом;Anion : Анион;Cation : Катион;Electron : Электрон;Valence : Валентность;Sublimation : Возгонка;Evaporation : Выпаривание;Autoclave : Автоклав;Analytical chemistry : Аналитическая химия;Isotopes : Изотопы;Molecule : Молекула;Monomers : Мономеры;Precipitation : Осаждение;Peroxides : Перекиси;Chemical equilibrium : Равновесие химическое;Free radicals : Радикалы свободные;Solubility : Растворимость;Filtration : Фильтрация;Chemical kinetics : Кинетика химическая;Crystallization : Кристаллизация;Carboxylic acid : Карбоновые кислоты;Hydrophilicity : Гидрофильность;Hydration : Гидратация;Hygroscopicity : Гигроскопичность;Heterogeneous system : Гетерогенные системы;Halogens : Галогены;Centrifugation : Центрифугирование;Alkalis : Щелочи;Electrolytes : Электролиты;Electrolysis : Электролиз'
s_chem_hard = 'Angstrom : Ангстрем;Adhesion : Адгезия;Viscometer : Вискозиметр;Hydrogen ph : Водородный показатель ph;Distillation : Дистилляция (перегонка);Isomerization : Изомеризация;Pyrolysis : Пиролиз;Plasma : Плазма;Polymerization : Полимеризация;Promoters : Промоторы;Rectification : Ректификация;Spectroscopy : Спектроскопия;Stereochemistry : Стереохимия;Tautomerism : Таутомерия;Chromatography : Хроматография;Esterification : Этерификация;Nuclear reaction : Ядерные реакции'
#s1=s.split(';')
#s1 = [1,2,3,345,234,3,2,6]#s.readlines()