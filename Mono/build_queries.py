
def build_ieee_query(set_of_words):
    queries = []
    for words in set_of_words:
        words_on_title = ["\"Document Title\":\""+w+"\"" for w in words]
        words_on_keyword = ["\"Author Keywords\":\""+w+"\"" for w in words]
        words_on_abstract = ["\"Abstract\":\""+w+"\"" for w in words]
        queries.append("(" + " OR ".join(words_on_title + words_on_keyword + words_on_abstract) + ")")
    ieee_query = " AND ".join(queries)
    return ieee_query

def build_acm_query(set_of_words):
    queries = []
    for words in set_of_words:
        words_quotation = ",".join(["\""+w+"\"" for w in words])
        query = "(acmdlTitle:(" + words_quotation + ") OR\r\n"
        query += "recordAbstract:(" + words_quotation + ") OR\r\n"
        query += "keywords.author.keyword:(" + words_quotation + "))\r\n"
        queries.append(query)
    acm_query = " AND ".join(queries)
    return acm_query

def build_scopus_query(set_of_words):
    queries = []
    for words in set_of_words:
        query = "\r\n("
        words_on_title_abs_key = ["TITLE-ABS-KEY(\""+w+"\")\r\n" for w in words]
        query += " OR ".join(words_on_title_abs_key)
        query += ")\r\n"
        queries.append(query)
    scopus_query = "AND".join(queries) + "AND (\r\nLIMIT-TO(SUBJAREA,\"COMP\" )\r\nOR LIMIT-TO(SUBJAREA,\"BUSI\" ))\r\nAND EXCLUDE(DOCTYPE,\"cr\" )"
    return scopus_query
        
if __name__ == "__main__":
    words = [
        ["quality","validation","criteria","heuristics","guidelines","anti-patterns","patterns","rule","pitfalls","classification","assessment","checklist"],
        ["requirements engineering","use case","use cases","story","user stories","feature","specifications","textual descriptions","templates","models","framework for integrated tests","fitnesse","living documentation","executable documentation","scenario","scenarios","behavior driven development", "bdd"],
        ["agile methodology","agile methodologies","scrum","extreme programming","feature driven development","lean software development", "adaptive software development"]
    ]
    print "="*100
    print build_scopus_query(words)
    print "="*100
    print build_acm_query(words)
    print "="*100
    print build_ieee_query(words)
