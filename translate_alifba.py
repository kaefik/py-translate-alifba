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
    common_turic_alifbasi_to_cyrilic_tatar[l[0]]=l[1]
    cyrilic_tatar_to_common_turic_alifbasi[l[1]]=l[0]

print(common_turic_alifbasi_to_cyrilic_tatar)
print()
print(cyrilic_tatar_to_common_turic_alifbasi)
    
original_text = "әйбет"
translate_text = ""
for i in original_text:
    translate_text+=cyrilic_tatar_to_common_turic_alifbasi[i]
print(translate_text)
