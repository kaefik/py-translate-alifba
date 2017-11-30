import configparser

namefile_cfg = "cfg-alifba.cfg"



def get_alifbasi(namefile_cfg):
    """ наполнение словарей перевода одних букв в другие """
    with open(namefile_cfg,"r") as f:
        lines = f.readlines()

    
    common_turic_alifbasi_to_cyrilic_tatar = dict() # из общетюркского алфавита в кирилический татарский
    cyrilic_tatar_to_common_turic_alifbasi = dict() # из  кирилического татарского в общетюркский алфавит
    for line in lines:
        line = line.replace("\n","")
        l = line.split("=")
        turk = l[0]
        cyrilic = l[1]
        if turk in common_turic_alifbasi_to_cyrilic_tatar:
            common_turic_alifbasi_to_cyrilic_tatar[turk]=common_turic_alifbasi_to_cyrilic_tatar[turk]+"*"+cyrilic
        else:
            common_turic_alifbasi_to_cyrilic_tatar[turk]=cyrilic
        if cyrilic in cyrilic_tatar_to_common_turic_alifbasi:
            cyrilic_tatar_to_common_turic_alifbasi[cyrilic]=cyrilic_tatar_to_common_turic_alifbasi[cyrilic]+"*"+turk
        else:
            cyrilic_tatar_to_common_turic_alifbasi[cyrilic]=turk
    return cyrilic_tatar_to_common_turic_alifbasi, cyrilic_tatar_to_common_turic_alifbasi
    # END наполнение словарей перевода одних букв в другие 

# перевод из кирилицы в общетюркский алфавит
def translate_cyrilic_to_cta(original_text,cyrilic_tatar_to_common_turic_alifbasi):
    """ перевод из кирилицы в общетюркский алфавит
            original_text - текст который нужно перевести
            cyrilic_tatar_to_common_turic_alifbasi - 
     """

    translate_text = "" # перевод текста
    # TODO: сначала надо отсканировать все сочетания символов которые по два или более символа.
    # TODO: надо научиться помечать/обрабатывать смволы у которых может быть два варианта.
    for i in original_text:  
        try:       
            if i.isupper():
                sim = i.lower()
                translate_text+=(cyrilic_tatar_to_common_turic_alifbasi[sim]).upper()
            else:
                translate_text+=cyrilic_tatar_to_common_turic_alifbasi[i]
        except KeyError:
            translate_text+=i
    return translate_text
# END перевод из кирилицы в общетюркский алфавит


#     
# original_text = "әйбЕт"
#original_text = "Казань"
original_text = "Татар телен укытудан баш тартмаган Шмаков мәхкәмәдә прокуратура ялганын"
print(original_text)
cyr2cta, cta2cyr = get_alifbasi(namefile_cfg)

text = translate_cyrilic_to_cta(original_text,cyr2cta)
print(text)


