import configparser

namefile_cfg = "cfg-alifba.cfg"

with open(namefile_cfg,"r") as f:
    lines = f.readlines()

# print(lines)

common_turic_alifbasi_to_cyrilic_tatar = dict()
cyrilic_tatar_to_common_turic_alifbasi = dict()
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
    

# print(common_turic_alifbasi_to_cyrilic_tatar)
# print()
# print(cyrilic_tatar_to_common_turic_alifbasi)
    
# original_text = "әйбЕт"
#original_text = "Казань"
original_text = "Объявлениясы һава.!"
print(original_text)
translate_text = "" # перевод тес\кста
# TODO: сначала надо отсканировать все сочетания символов которые по два или более символа.
# TODO: надо научиться помечать/обрабатывать смволы у которых моңет бытҗ два варианта.
for i in original_text:  
    try:       
        if i.isupper():
            sim = i.lower()
            translate_text+=(cyrilic_tatar_to_common_turic_alifbasi[sim]).upper()
        else:
            translate_text+=cyrilic_tatar_to_common_turic_alifbasi[i]
    except KeyError:
        translate_text+=i
print(translate_text)
