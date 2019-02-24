from nltk.corpus import wordnet
from fractions import Fraction
from math import sqrt
from googletrans import Translator

capitals_dic = {
    'Afghanistan': 'Kabul',
    'Albania': 'Tirana',
    'Algeria': 'Algiers',
    'Andorra': 'Andorra la Vella',
    'Angola': 'Luanda',
    'Antigua and Barbuda': 'Saint John\'s',
    'Argentina': 'Buenos Aires',
    'Armenia': 'Yerevan',
    'Australia': 'Canberra',
    'Austria': 'Vienna',
    'Azerbaijan': 'Baku',
    'The Bahamas': 'Nassau',
    'Bahrain': 'Manama',
    'Bangladesh': 'Dhaka',
    'Barbados': 'Bridgetown',
    'Belarus': 'Minsk',
    'Belgium': 'Brussels',
    'Belize': 'Belmopan',
    'Benin': 'Porto-Novo',
    'Bhutan': 'Thimphu',
    'Bolivia': 'La Paz (administrative); Sucre (judicial)',
    'Bosnia and Herzegovina': 'Sarajevo',
    'Botswana': 'Gaborone',
    'Brazil': 'Brasilia',
    'Brunei': 'Bandar Seri Begawan',
    'Bulgaria': 'Sofia',
    'Burkina Faso': 'Ouagadougou',
    'Burundi': 'Gitega (changed from Bujumbura in December 2018)',
    'Cambodia': 'Phnom Penh',
    'Cameroon': 'Yaounde',
    'Canada': 'Ottawa',
    'Cape Verde': 'Praia',
    'Central African Republic': 'Bangui',
    'Chad': 'N\'Djamena',
    'Chile': 'Santiago',
    'China': 'Beijing',
    'Colombia': 'Bogota',
    'Comoros': 'Moroni',
    'Republic of the Congo; Congo-Republic': 'Brazzaville',
    'Democratic Republic of the Congo; Congo-Democratic Republic': 'Kinshasa',
    'Costa Rica': 'San Jose',
    'Cote d\'Ivoire': ' Yamoussoukro (official); Abidjan (de facto)',
    'Croatia': 'Zagreb',
    'Cuba': 'Havana',
    'Cyprus': 'Nicosia',
    'Czech Republic': 'Prague',
    'Denmark': 'Copenhagen',
    'Djibouti': 'Djibouti',
    'Dominica': 'Roseau',
    'Dominican Republic': 'Santo Domingo',
    'East Timor (Timor-Leste)': 'Dili',
    'Ecuador': 'Quito',
    'Egypt': 'Cairo',
    'El Salvador': 'San Salvador',
    'Equatorial Guinea': 'Malabo',
    'Eritrea': 'Asmara',
    'Estonia': 'Tallinn',
    'Ethiopia': 'Addis Ababa',
    'Fiji': 'Suva',
    'Finland': 'Helsinki',
    'France': 'Paris',
    'Gabon': 'Libreville',
    'The Gambia': 'Banjul',
    'Georgia': 'Tbilisi',
    'Germany': 'Berlin',
    'Ghana': 'Accra',
    'Greece': 'Athens',
    'Grenada': 'Saint George\'s',
    'Guatemala': 'Guatemala City',
    'Guinea': 'Conakry',
    'Guinea-Bissau': 'Bissau',
    'Guyana': 'Georgetown',
    'Haiti': 'Port-au-Prince',
    'Honduras': 'Tegucigalpa',
    'Hungary': 'Budapest',
    'Iceland': 'Reykjavik',
    'India': 'New Delhi',
    'Indonesia': 'Jakarta',
    'Iran': 'Tehran',
    'Iraq': 'Baghdad',
    'Ireland': 'Dublin',
    'Israel': 'Jerusalem',
    'Italy': 'Rome',
    'Jamaica': 'Kingston',
    'Japan': 'Tokyo',
    'Jordan': 'Amman',
    'Kazakhstan': 'Astana',
    'Kenya': 'Nairobi',
    'Kiribati': 'Tarawa Atoll',
    'Korea, North; North Korea': 'Pyongyang',
    'Korea, South; South Korea': 'Seoul',
    'Kuwait': 'Kuwait City',
    'Kyrgyzstan': 'Bishkek',
    'Laos': 'Vientiane',
    'Latvia': 'Riga',
    'Lebanon': 'Beirut',
    'Lesotho': 'Maseru',
    'Liberia': 'Monrovia',
    'Libya': 'Tripoli',
    'Liechtenstein': 'Vaduz',
    'Lithuania': 'Vilnius',
    'Luxembourg': 'Luxembourg',
    'Macedonia': 'Skopje',
    'Madagascar': 'Antananarivo',
    'Malawi': 'Lilongwe',
    'Malaysia': 'Kuala Lumpur',
    'Maldives': 'Male',
    'Mali': 'Bamako',
    'Malta': 'Valletta',
    'Marshall Islands': 'Majuro',
    'Mauritania': 'Nouakchott',
    'Mauritius': 'Port Louis',
    'Mexico': 'Mexico City',
    'Micronesia': 'Federated States of: Palikir',
    'Moldova': 'Chisinau',
    'Monaco': 'Monaco',
    'Mongolia': 'Ulaanbaatar',
    'Montenegro': 'Podgorica',
    'Morocco': 'Rabat',
    'Mozambique': 'Maputo',
    'Myanmar (Burma)': 'Rangoon (Yangon); Naypyidaw or Nay Pyi Taw (administrative)',
    'Namibia': 'Windhoek',
    'Nauru': 'no official capital; government offices in Yaren District',
    'Nepal': 'Kathmandu',
    'Netherlands': 'Amsterdam; The Hague (seat of government)',
    'New Zealand': 'Wellington',
    'Nicaragua': 'Managua',
    'Niger': 'Niamey',
    'Nigeria': 'Abuja',
    'Norway': 'Oslo',
    'Oman': 'Muscat',
    'Pakistan': 'Islamabad',
    'Palau': 'Melekeok',
    'Panama': 'Panama City',
    'Papua New Guinea': 'Port Moresby',
    'Paraguay': 'Asuncion',
    'Peru': 'Lima',
    'Philippines': 'Manila',
    'Poland': 'Warsaw',
    'Portugal': 'Lisbon',
    'Qatar': 'Doha',
    'Romania': 'Bucharest',
    'Russia': 'Moscow',
    'Rwanda': 'Kigali',
    'Saint Kitts and Nevis': 'Basseterre',
    'Saint Lucia': 'Castries',
    'Saint Vincent and the Grenadines': 'Kingstown',
    'Samoa': 'Apia',
    'San Marino': 'San Marino',
    'Sao Tome and Principe': 'Sao Tome',
    'Saudi Arabia': 'Riyadh',
    'Senegal': 'Dakar',
    'Serbia': 'Belgrade',
    'Seychelles': 'Victoria',
    'Sierra Leone': 'Freetown',
    'Singapore': 'Singapore',
    'Slovakia': 'Bratislava',
    'Slovenia': 'Ljubljana',
    'Solomon Islands': 'Honiara',
    'Somalia': 'Mogadishu',
    'South Africa': 'Pretoria (administrative); Cape Town (legislative); Bloemfontein (judiciary)',
    'South Sudan': 'Juba',
    'Spain': 'Madrid',
    'Sri Lanka': 'Colombo; Sri Jayewardenepura Kotte (legislative)',
    'Sudan': 'Khartoum',
    'Suriname': 'Paramaribo',
    'Swaziland': 'Mbabane',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Syria': 'Damascus',
    'Taiwan': 'Taipei',
    'Tajikistan': 'Dushanbe',
    'Tanzania': 'Dar es Salaam; Dodoma (legislative)',
    'Thailand': 'Bangkok',
    'Togo': 'Lome',
    'Tonga': 'Nuku\'alofa',
    'Trinidad and Tobago': 'Port-of-Spain,',
    'Tunisia': 'Tunis',
    'Turkey': 'Ankara',
    'Turkmenistan': 'Ashgabat',
    'Tuvalu': 'Vaiaku village, Funafuti province',
    'Uganda': 'Kampala',
    'Ukraine': 'Kyiv',
    'United Arab Emirates': 'Abu Dhabi',
    'United Kingdom': 'London',
    'United States of America': 'Washington, D.C.',
    'Uruguay': 'Montevideo',
    'Uzbekistan': 'Tashkent',
    'Vanuatu': 'Port-Vila',
    'Vatican City (Holy See)': 'Vatican City',
    'Venezuela': 'Caracas',
    'Vietnam': 'Hanoi',
    'Yemen': 'Sanaa',
    'Zambia': 'Lusaka',
    'Zimbabwe': 'Harare',
}

elements_dic = {
    'H': 'Hydrogen',
    'He': 'Helium',
    'Li': 'Lithium',
    'Be': 'Beryllium',
    'B': 'Boron',
    'C': 'Carbon',
    'N': 'Nitrogen',
    'O': 'Oxygen',
    'F': 'Fluorine',
    'Ne': 'Neon',
    'Na': 'Sodium',
    'Mg': 'Magnesium',
    'Al': 'Aluminum',
    'Si': 'Silicon',
    'P': 'Phosphorus',
    'S': 'Sulfur',
    'Cl': 'Chlorine',
    'Ar': 'Argon',
    'K': 'Potassium',
    'Ca': 'Calcium',
    'Sc': 'Scandium',
    'Ti': 'Titanium',
    'V': 'Vanadium',
    'Cr': 'Chromium',
    'Mn': 'Manganese',
    'Fe': 'Iron',
    'Co': 'Cobalt',
    'Ni': 'Nickel',
    'Cu': 'Copper',
    'Zn': 'Zinc',
    'Ga': 'Gallium',
    'Ge': 'Germanium',
    'As': 'Arsenic',
    'Se': 'Selenium',
    'Br': 'Bromine',
    'Kr': 'Krypton',
    'Rb': 'Rubidium',
    'Sr': 'Strontium',
    'Y': 'Yttrium',
    'Zr': 'Zirconium',
    'Nb': 'Niobium',
    'Mo': 'Molybdenum',
    'Tc': 'Technetium',
    'Ru': 'Ruthenium',
    'Rh': 'Rhodium',
    'Pd': 'Palladium',
    'Ag': 'Silver',
    'Cd': 'Cadmium',
    'In': 'Indium',
    'Sn': 'Tin',
    'Sb': 'Antimony',
    'Te': 'Tellurium',
    'I': 'Iodine',
    'Cs': 'Cesium',
    'Ba': 'Barium',
    'La': 'Lanthanum',
    'Ce': 'Cerium',
    'Pr': 'Praseodymium',
    'Nd': 'Neodymium',
    'Pm': 'Promethium',
    'Sm': 'Samarium',
    'Eu': 'Europium',
    'Gd': 'Gadolinium',
    'Tb': 'Terbium',
    'Dy': 'Dysprosium',
    'Ho': 'Holmium',
    'Er': 'Erbium',
    'Tm': 'Thulium',
    'Yb': 'Ytterbium',
    'Lu': 'Lutetium',
    'Hf': 'Hafnium',
    'Ta': 'Tantalum',
    'W': 'Tungsten',
    'Re': 'Rhenium',
    'Os': 'Osmium',
    'Ir': 'Iridium',
    'Pt': 'Platinum',
    'Au': 'Gold',
    'Hg': 'Mercury',
    'Tl': 'Thallium',
    'Pb': 'Lead',
    'Bi': 'Bismuth',
    'Po': 'Polonium',
    'At': 'Astatine',
    'Rn': 'Radon',
    'Fr': 'Francium',
    'Ra': 'Radium',
    'Ac': 'Actinium',
    'Th': 'Thorium',
    'Pa': 'Protactinium',
    'U': 'Uranium',
    'Np': 'Neptunium',
    'Pu': 'Plutonium',
    'Am': 'Americium',
    'Cm': 'Curium',
    'Bk': 'Berkelium',
    'Cf': 'Californium',
    'Es': 'Einsteinium',
    'Fm': 'Fermium',
    'Md': 'Mendelevium',
    'No': 'Nobelium',
    'Lr': 'Lawrencium',
    'Rf': 'Rutherfordium',
    'Db': 'Dubnium',
    'Sg': 'Seaborgium',
    'Bh': 'Bohrium',
    'Hs': 'Hassium',
    'Mt': 'Meitnerium',
    'Ds': 'Darmstadtium',
    'Rg': 'Roentgenium',
    'Cn': 'Copernicium',
    'Nh': 'Nihonium',
    'Fl': 'Flerovium',
    'Mc': 'Moscovium',
    'Lv': 'Livermorium',
    'Ts': 'Tennessine',
    'Og': 'Oganesson'
}

class Solver:
    def __init__(self):
        pass

      
@staticmethod
    def var(string):
        if "+" in string:
            splitString = string.split("^")
            return "2A^" + splitString[2]
        elif "x" in string:
            splitString = string.split("x")
            expo = int(splitString[0][2]) + int(splitString[1][3])
            return "A^" + str(expo)
        elif "/" in string:
            splitString = string.split("x")
            expo = int(splitString[0][2]) - int(splitString[1][3])
            return "A^" + str(expo)

    @staticmethod
    def sqRoot(string):
        string = string.split("root")
        return sqrt(int(string[1]))

    @staticmethod
    def percents(string):
        string = string.split("% of ")
        perc = int(string[0])/100
        return eval(str(perc) + "*" + string[1])

   @staticmethod
    def rounded(string):
        if ".5" in string:
            string = string.split(" rounded")
            print(int(string[0][0]) + 1)
        else:
            string = string.split(" rounded")
            return round(float(string[0]))
@staticmethod
    def solve(string):
        if "A" in string:
            return Solver.var(string)
        elif "square root" in string:
            return Solver.sqRoot(string)
        elif "of" in string:
            return Solver.percents(string)
        elif "rounded" in string:
            return Solver.rounded(string)
        elif string.count('/') > 1:
            if "x" in string:
                string = string.replace('x', '*')
                myDeci = eval(string)
                return Fraction(myDeci).limit_denominator()
            elif "**" in string:
                string = string.replace('^', '**')
                myDeci = eval(string)
                return Fraction(myDeci).limit_denominator()
            elif string.count("/") > 2:
                splitFrac = string.split("/")
                ans = "(" + splitFrac[0] + "/" + splitFrac[1] + ")" + "/" + "(" + splitFrac[2] + "/" + splitFrac[3] + ")"
                myDeci = eval(ans)
                return Fraction(myDeci).limit_denominator()
            else:
                myDeci = eval(string)
                return Fraction(myDeci).limit_denominator()
        elif "x" in string:
            string = string.replace('x', '*')
            return int(eval(string))
        elif "^" in string:
            string = string.replace('^', '**')
            return int(eval(string))
        else:
            return eval(string)
            
print(Solver.solve("30% of 67"))

    @staticmethod
    def similar(w1,w2):
        try:
            w1_syn = [" ".join(i.name().split('_')) for i in wordnet.synsets(w1)[0].lemmas()]
            w2_syn = [" ".join(i.name().split('_')) for i in wordnet.synsets(w2)[0].lemmas()]
            return w1 in w2_syn or w2 in w1_syn
        except:
            return False

    @staticmethod
    def closest_synonyms(word,choices):
        c0,c1,c2,c3 = choices
        syn_list=wordnet.synsets(word)
        for i in syn_list[0].lemmas():
            s=" ".join(i.name().split('_'))
            if Solver.similar(s,c0):
                return c0
            if Solver.similar(s,c1):
                return c1
            if Solver.similar(s,c2):
                return c2
            if Solver.similar(s,c3):
                return c3
            else:
                raise ValueError('Word not found.')

    @staticmethod
    def translate_to_en(word):
        tra=Translator()
        return tra.translate(word).text

    @staticmethod
    def country_out(cap_in):
        for country, capital in capitals_dic.items():
            if str(capital).find(str(cap_in)) != -1 or str(cap_in).find(str(capital)) != -1:
                return country

    @staticmethod
    def check_answers(capout_final, answer_options):
        for answer in answer_options:
            if str(answer).find(str(capout_final)) != -1 or str(capout_final).find(str(answer)) != -1:
                return answer

    @staticmethod
    def find_capital(input, answers):
        return Solver.check_answers(Solver.country_out(input), answers)

    @staticmethod
    def symbol(symbolelement):
        for symbol, element in elements_dic.items():
            if element == symbolelement:
                return symbol

    @staticmethod
    def chem_check_answers(symbol_final, answer_options):
        for answer in answer_options:
            if answer == symbol_final:
                return answer

    @staticmethod
    def find_symbol(input, answers):
        return Solver.chem_check_answers(Solver.symbol(input), answers)
