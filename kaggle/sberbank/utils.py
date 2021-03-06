"""
This is a set of helper scripts used to organize the EDA and modeling for the SBER Bank dataset
"""

"""
Some of the modeling is perfomred in SAS in which the naming convention proved to be either too long or had 
numerical charachters in which prompted exceptions when modeling in SAS. Therefore here are the new column names. 
"""
sas_col_rename = {
    'preschool_education_centers_raion':'prek_raison',
    'school_education_centers_top_20_raion': 'school_top20_raison',
    'raion_build_count_with_builddate_info': 'raison_build_count_info',
    'public_transport_station_min_walk':'public_transport_minwalk',
    '0_6_all':'under6_all',
    '0_6_male':'under6_m',
    '0_6_female':'under6_f',
    '7_14_all':'seven_14_all',
    '7_14_male':'seven_14_m',
    '7_14_female':'seven_14_f',
    '0_17_all':'under17_all',
    '0_17_male':"under17m",
    '0_17_female':'under17f',
    '16_29_all':'sixteen_29_all',
    '16_29_male':'sixteen_29m',
    '16_29_female':'six_29f',
    '0_13_all':'under13_all',
    '0_13_male':'under13_m',
    '0_13_female':"under13_f"
}


districts = {
 'Nagatinskij Zaton':'south',
 "Tekstil'shhiki":'south_east',
 'Mitino':'north_west',
 'Basmannoe':'central',
 'Nizhegorodskoe':'south_east',
 "Sokol'niki":'east',
 'Koptevo':"north",
 'Kuncevo':'west',
 'Kosino-Uhtomskoe': 'east',
 'Zapadnoe Degunino': 'north',
 'Presnenskoe':'central',
 'Lefortovo': 'south_east',
 "Mar'ino":'south_east',
 "Kuz'minki": 'south_east',
 'Nagornoe': 'south',
 "Gol'janovo": 'east',
 'Vnukovo': 'west',
 'Juzhnoe Tushino': 'north_west',
 'Severnoe Tushino': 'north_west',
 "Chertanovo Central'noe":"south",
 'Otradnoe':'north_east',
 'Novo-Peredelkino':'west',
 'Bogorodskoe': 'east',
 'Strogino':'north_west',
 'Hovrino':'north',
 "Moskvorech'e-Saburovo":'south',
 'Ljublino':'south_east',
 'Caricyno':'south',
 'Veshnjaki':'north_east',
 'Danilovskoe':'south',
 'Preobrazhenskoe':'east',
 "Kon'kovo":'south_west',
 'Brateevo':'south',
 'Vostochnoe Izmajlovo':'east',
 'Jaroslavskoe':'north_east',
 'Vyhino-Zhulebino':'south_east',
 'Donskoe':'south',
 'Novogireevo':'east',
 'Juzhnoe Butovo':'south',
 'Sokol':'north',
 'Kurkino':'north_west',
 'Izmajlovo':'east',
 'Severnoe Medvedkovo':'north_east',
 'Rostokino':'north_east',
 'Orehovo-Borisovo Severnoe':'south',
 'Taganskoe':'central',
 'Dmitrovskoe':'north',
 'Orehovo-Borisovo Juzhnoe':'south',
 'Teplyj Stan':'south',
 'Babushkinskoe':'north_east',
 'Staroe Krjukovo':'north',
 'Pokrovskoe Streshnevo':"north_west",
 'Obruchevskoe':'south_west',
 'Filevskij Park':'west',
 'Troparevo-Nikulino':'west',
 'Severnoe Butovo':'south_west',
 'Hamovniki':'central',
 'Solncevo':'west',
 'Lianozovo':'north_west',
 'Pechatniki':'south_east',
 'Krjukovo':'north',
 'Jasenevo':'south_west',
 'Chertanovo Severnoe':'south',
 'Rjazanskij':'south_east',
 'Ochakovo-Matveevskoe':'west',
 'Ivanovskoe':'east',
 'Novokosino':'east',
 'Nagatino-Sadovniki':'south',
 'Birjulevo Vostochnoe':'south',
 'Sokolinaja Gora':'east',
 'Vostochnoe Degunino':'north',
 'Prospekt Vernadskogo':'west',
 'Savelki':'north',
 'Ajeroport':'north',
 'Vojkovskoe':'north_east',
 'Beskudnikovskoe': 'south_west',
 'Krylatskoe':'west',
 'Perovo':'east',
 'Akademicheskoe':'south_west',
 'Horoshevo-Mnevniki':'north_west',
 'Shhukino':'north_west',
 'Kapotnja':'south_east',
 'Fili Davydkovo':'west',
 'Horoshevskoe':'south_west',
 'Marfino':'north_east',
 'Juzhnoportovoe':'east',
 'Chertanovo Juzhnoe': 'south',
 'Silino':'north_west',
 'Savelovskoe':'north',
 'Severnoe Izmajlovo':'east',
 'Birjulevo Zapadnoe':'south',
 'Cheremushki':'south_west',
 'Alekseevskoe':'north_east',
 "Krasnosel'skoe":'central',
 'Kotlovka':'south_west',
 'Ostankinskoe':'north_east',
 'Tverskoe':'south',
 'Losinoostrovskoe': 'north_east',
 'Butyrskoe': 'north_east',
 'Matushkino':'north_west',
 'Metrogorodok': 'east',
 'Juzhnoe Medvedkovo':'north_east',
 'Zjuzino':'south_west',
 'Lomonosovskoe':'south_west',
 'Jakimanka':'central',
 'Mozhajskoe':'west',
 'Levoberezhnoe':'north',
 'Sviblovo':'north_east',
 "Mar'ina Roshha":'north_east',
 'Timirjazevskoe':'north',
 'Nekrasovka':'south_east',
 'Dorogomilovo':'west',
 'Gagarinskoe':'south_west',
 'Golovinskoe':'north',
 "Altuf'evskoe":'central',
 'Ramenki':'west',
 'Zjablikovo':'south',
 'Meshhanskoe':'central',
 'Severnoe':'north',
 'Begovoe':'north',
 'Arbat':'central',
 "Zamoskvorech'e":'central',
 'Poselenie Sosenskoe':'Poselenie',
 'Poselenie Moskovskij':'Poselenie',
 'Poselenie Pervomajskoe':'Poselenie',
 'Poselenie Desjonovskoe':'Poselenie',
 'Poselenie Voskresenskoe':'Poselenie',
 'Troickij okrug':'east',
 'Poselenie Shherbinka':'Poselenie',
 'Poselenie Filimonkovskoe':'Poselenie',
 'Poselenie Vnukovskoe':'Poselenie',
 'Poselenie Marushkinskoe':'Poselenie',
 'Poselenie Shhapovskoe':'Poselenie',
 'Poselenie Mosrentgen':'Poselenie',
 'Poselenie Rjazanovskoe':'Poselenie',
 'Poselenie Kokoshkino':'Poselenie',
 'Vostochnoe':'north',
 'Poselenie Krasnopahorskoe':'Poselenie',
 'Poselenie Novofedorovskoe':'Poselenie',
 'Poselenie Voronovskoe':'Poselenie',
 'Poselenie Klenovskoe':'Poselenie',
 'Poselenie Rogovskoe':'Poselenie',
 'Molzhaninovskoe':'north',
 'Poselenie Mihajlovo-Jarcevskoe':'Poselenie',
 'Poselenie Kievskij':'Poselenie',
 'Bibirevo':'north_east'
}
#'Poselenie Voronovskoe':'central',
#'Poselenie Klenovskoe':'north_west',
#'Poselenie Rogovskoe':'nort_west',
#'Poselenie Novofedorovskoe':'southeast'
