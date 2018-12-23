# coding: utf-8

import xlrd
import os
import nltk.corpus
import pdb

import sys
reload(sys)
sys.setdefaultencoding('utf8')

PATH_1 = "D:\\git\\Dissertation\\LabPDS\\Evaluation\\Entrega_AvaliacaoProjeto1"
PATH_2 = "D:\\git\\Dissertation\\LabPDS\\Evaluation\\Entrega_AvaliacaoProjeto2"
SAMPLE_FILE_1 = "D:\\git\\Dissertation\\LabPDS\\Evaluation\\Entrega_AvaliacaoProjeto1\\WALTER RITZEL PAIX_O-CORTES_2609612_assignsubmission_file_QualityEvaluationForm_WalterRitzelPaixaoCortes_Projeto1.xlsx"
SAMPLE_FILE_2 = "D:\\git\\Dissertation\\LabPDS\\Evaluation\\Entrega_AvaliacaoProjeto2\\WALTER RITZEL PAIX_O-CORTES_2609635_assignsubmission_file_QualityEvaluationForm_P2_WalterRitzelPaixaoCortes.xlsx"
ATTRIBUTES = ["Atômico","Completo","Prioritizável","Consistente","Conciso","Estimável","Entendível","Factível","Independente","Indepentente","Negociável","Não Ambíguo","Prioritizável","Pequeno","Testável","Valioso"]

STOP_WORDS = nltk.corpus.stopwords.words('portuguese') + ["é", "pois", "sim", "etc", "uso", "caso", "cenário", "É"]
MAC_MORPHO_TAGGER = {x : y for x,y in nltk.corpus.mac_morpho.tagged_words()} #news text, with over a million words of journalistic texts extracted from ten sections of the daily newspaper Folha de Sao Paulo, 1994.
FLORESTA_TAGGER = {x : y for x,y in nltk.corpus.floresta.tagged_words()} #"Floresta Sinta(c)tica Corpus" version 7.4, available from http://www.linguateca.pt/Floresta/.

def analyze_file(path):
    folder = path.split(os.sep)[-2]
    student = path.split(os.sep)[-1].split(" ")[0]
    book = xlrd.open_workbook(path)
    for i in range(book.nsheets):
        sh = book.sheet_by_index(i)
        if "Template Blank" in sh.name:
            continue
        print "\n" + "_".join([folder, student, sh.name.replace(" ", "_")])
        for rx in range(sh.nrows):
            row_data = []
            for ry in sh.row(rx):
                if ry != xlrd.empty_cell and len(ry.value) > 0:
                    row_data.append(ry.value)
            if len(row_data) > 1 and row_data[0].encode("latin-1") in ATTRIBUTES:
                print "\t".join([row_data[0].encode("utf-8"), row_data[1].encode("utf-8")])
                
def analyze_to_file(path):
    folder = path.split(os.sep)[-2].replace("Entrega_Avaliacao","")
    student = path.split(os.sep)[-1].split(" ")[0]
    filename = "_".join([folder, student]) + ".txt"
    file = open(filename, "w")
    book = xlrd.open_workbook(path)    
    for i in range(book.nsheets):
        sh = book.sheet_by_index(i)
        if "Template Blank" in sh.name:
            continue
        file.write("\n==" + "_".join([folder, student, sh.name.replace(" ", "_")]) + "\n")
        for rx in range(sh.nrows):
            row_data = []
            for ry in sh.row(rx):
                if ry != xlrd.empty_cell and len(ry.value) > 0:
                    row_data.append(ry.value)
            if len(row_data) > 1 and row_data[0].encode("latin-1") in ATTRIBUTES:
                file.write("\t".join([row_data[0].encode("utf-8"), row_data[1].encode("utf-8")]) + "\n")
    file.close()
    #print "File created: " + filename
    return filename
    
def _sheet_type(sheet):
    lower_sheet = sheet.lower() 
    if "use_case" in lower_sheet or "uc" in lower_sheet or "caso" in lower_sheet:
        return "Use case"
    elif "capa" in lower_sheet:
        return "Misc"
    elif "definicoes" in lower_sheet or "definições" in lower_sheet:
        return "Definitions"
    elif "us" in lower_sheet or "cen" in lower_sheet or "us" in lower_sheet:
        return "BDD"
    else:
        return "?"

def _word_type(word):
    type = ""
    if word.lower() in MAC_MORPHO_TAGGER:
        type += MAC_MORPHO_TAGGER[word.lower()]
    else:
        type += "?"
    type += " / "
    if word.lower() in FLORESTA_TAGGER:
        type += FLORESTA_TAGGER[word.lower()]
    else:
        type += "?"
    return type
        
def txt_to_dict(filename,data):
    lines = open(filename, "r").readlines()
    current_key = ""
    for i in range(len(lines)):
        line = lines[i].replace("\n", "").replace("\r", "")
        
        if "==" in line:
            current_key = line.replace("==", "")
            data["data"][current_key] = {}
            
        if len(current_key) > 0 and len(line) > 0 and len(line.split("\t")) > 1:
            attribute,phrase = line.split("\t")
            if attribute == "Indepentente":
                attribute = "Independente"
            data["data"][current_key][attribute] = phrase
            
            type = _sheet_type(current_key)
            analytic = phrase.lower().replace(",", "").replace(".", "").replace("(","").replace(")","").replace("\"", "").split(" ")            
            if attribute not in data["attributes"]:
                data["attributes"][attribute] = {}
            for a in analytic:
                if a.strip() in STOP_WORDS or len(a.strip()) < 1:
                    continue
                word = "/".join([a, type])
                if word not in data["words"]:
                    data["words"][word] = {}
                if word in data["words"] and attribute not in data["words"][word]:
                    data["words"][word][attribute] = {}
                    data["words"][word][attribute]["phrases"] = []
                    data["words"][word][attribute]["count"] = 0
                if word not in data["attributes"][attribute]:
                    data["attributes"][attribute][word] = {}
                    data["attributes"][attribute][word]["phrases"] = []
                    data["attributes"][attribute][word]["count"] = 0
                if word in data["words"] and attribute not in data["words"][word]:
                    data["words"][word][attribute] = {}
                    data["words"][word][attribute]["phrases"] = []
                    data["words"][word][attribute]["count"] = 0
                    
                data["words"][word][attribute]["count"] += 1
                data["words"][word][attribute]["phrases"].append(phrase)
                data["attributes"][attribute][word]["count"] += 1
                data["attributes"][attribute][word]["phrases"].append(phrase)
    return data
            
def dict_to_print(data, print_header):
    attributes_list = data["attributes"].keys()
    if print_header:
        print "\t".join(["id", "type"] + attributes_list)
    for sheet,opinions in data["data"].iteritems():
        to_print = [sheet]
        to_print.append(_sheet_type(sheet))
        for a in attributes_list:
            if a in opinions:
                to_print.append(opinions[a])
            else:
                to_print.append("")
        print "\t".join(to_print)
    
    print "="*100
    if print_header:
        print "\t".join(["id", "type"] + attributes_list)
    for word,data_per_attr in data["words"].iteritems():
        to_print = [word]
        to_print.append(_word_type(word.split("/")[0]))
        for a in attributes_list:
            if a in data_per_attr:
                to_print.append(str(data_per_attr[a]["count"]))
            else:
                to_print.append("0")
        print "\t".join(to_print)
        
    print "="*100
    for attr in attributes_list:
        print "\n== " + attr
        words_data_filtered = [(word.replace("/BDD",""), data["attributes"][attr][word]["count"], data["attributes"][attr][word]["phrases"]) 
                                                                       for word in data["attributes"][attr].keys() 
                                                                       if _word_type(word.split("/")[0]).startswith("N") 
                                                                       and "/BDD" in word]
        for w,c,p in sorted(words_data_filtered, key=lambda tup: tup[1], reverse=True): 
            print "\t".join([w,str(c)," || ".join(p)])
        
        
def find_analyze_xls(path, data, print_header):
    items = os.listdir(path)
    for i in items:
        new_path = os.path.join(path, i)
        if ".xls" in i:
            #analyze_file(new_path)
            filename = analyze_to_file(new_path)
            data = txt_to_dict(filename, data)    
    return data

if __name__ == "__main__":
    data = {"attributes" : {}, "data" : {}, "words" : {}}
    data = find_analyze_xls(PATH_1, data, True)
    data = find_analyze_xls(PATH_2, data, False)
    dict_to_print(data, True)
    #filename = analyze_to_file(SAMPLE_FILE_1)
    #data = txt_to_dict(filename, data)
    #filename = analyze_to_file(SAMPLE_FILE_2)
    #data = txt_to_dict(filename, data)
    #dict_to_print(data, True)