# a = {'eden': "White wine", "Dean": "Red wine"}
# # open("data","w").write(str(a))
# # b = open("data","r").read()
# # print(type(b))
# # print(b)
# # print(b['eden'])
# # import pickle
# # a_file = open("data.pkl", "wb")
# #
# # pickle.dump(a, a_file)
# #
# # a_file.close()
# #
# #
# # a_file = open("data.pkl", "rb")
# #
# # output = pickle.load(a_file)
# #
# # print(output)
# # print(type(output))
# import json
# a_file = open("data.json", "w")
#
# json.dump(a, a_file)
#
# a_file.close()
#
#
# a_file = open("data.json", "r")
#
# output = a_file.read()
# print(output)
# print(type(output))
# final = json.loads(output)
# print(final)
# print(type(final))
#
# import configparser
# config = configparser.ConfigParser()
# config.read("config.ini")
# print(config.sections())
# for section in config.sections():
#     print(section, config.items(section))
import yaml
import json
data = {'mylist': [1,2,3], 'mystr': "String", "Mydict": {'Eden': 24, 'Dean': 28}}
outfile= open('data.yml', 'w')
yaml.dump(data, outfile, default_flow_style=False)
a_file = open("data.json", "w")
json.dump(fp=a_file, obj=data, indent=4)
a_file.close()