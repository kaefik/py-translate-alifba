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
    return cyrilic_tatar_to_common_turic_alifbasi, common_turic_alifbasi_to_cyrilic_tatar
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


# перевод из общетюркского алфавита в кирилицу татарский
def translate_cta_to_cyrilic(original_text,cta_to_cyr_tat):
    """ перевод из кирилицы в общетюркский алфавит
            original_text - текст который нужно перевести
            cyrilic_tatar_to_common_turic_alifbasi - 
     """

    translate_text = "" # перевод текста
    # TODO: сначала надо отсканировать все сочетания символов которые по два или более символа.
    # TODO: надо научиться помечать/обрабатывать смволы у которых может быть два варианта.,
    list_two_letter =list()
    for i in cta_to_cyr_tat:
        if len(i)>1:
            list_two_letter.append(i)            

    # print(list_two_letter)
    original_text_replace = original_text
    for i in list_two_letter:
        original_text_replace=original_text_replace.replace(i,cta_to_cyr_tat[i])
    # надо научиться помечать/обрабатывать смволы у которых может быть два варианта.,
    
    # print("original_text_replace: {}".format(original_text_replace))

    for i in original_text_replace:  
        try:       
            if i.isupper():
                sim = i.lower()
                translate_text+=(cta_to_cyr_tat[sim]).upper()
            else:
                translate_text+=cta_to_cyr_tat[i]
        except KeyError:
            translate_text+=i
    return translate_text
# END перевод из общетюркского алфавита в кирилицу татарский

#     
# original_text = "әйбЕт"
#original_text = "Казань"
original_text = "Татар телен укытудан баш тартмаган Шмаков мәхкәмәдә прокуратура ялганын"
print(original_text)
cyr2cta, cta2cyr = get_alifbasi(namefile_cfg)

text = translate_cyrilic_to_cta(original_text,cyr2cta)
print(text)

org_text2 = "900 yıllarnıñ başında qullanuğa Ğäräp älifbasına nigezlängän älifba kerä. Ozaq waqıtlar Ğäräp yazuı Tatarlar tarafınnan bernindi üzgärtüsez genä qullanılıp kilä. Farsılar, üz telläreneñ ixtıyaclarınnan çığıp, Ğäräp älifbasına dürt xäref östilär (p, ç, j, g). äkrenläp bu xäreflärne Urta Aziä Törkiläre dä üzläşterä, soñraq alarnı Tatarlar da qabul itälär, älifbalar tarixında ul «İske imlä» yä isä «İske älif» iseme belän yörtelä. Läkin ul äle Tatar telenä, anıñ qanunnarına tulısınça cawap birä torğan älifba bulmıy. Mäsälän, Tatar telendäge «g» İske imlä älifbasında Ğäräp teleneñ «k», Tatarnıñ «ç» Ğäräpneñ «c», häm «p» urınında «b», «ñ» Ğäräpneñ iske “nk” xärefläre arqılı belderelgän. Borınğı Tatar qulyazmalarında başqa xäreflär yärdämendä belderü oçraqları da bar."
text2 =translate_cta_to_cyrilic(org_text2,cta2cyr)
print(text2)

