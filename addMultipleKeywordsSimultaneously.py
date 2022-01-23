from flashtext import KeywordProcessor


class addMultikeywords:

     def __init__(self, text, keyword_dict):
          self.text = text
          self.keyword_dict = keyword_dict

     def addkey(self):
          keyword_processor = KeywordProcessor(case_sensitive=False)
          keyword_processor.add_keywords_from_dict(self.keyword_dict)
          extractedKeyword = keyword_processor.extract_keywords(self.text)
          return extractedKeyword



adding = addMultikeywords("The development in Blockchain technology in recent years has caused it to take one step closer to transparency and a decentralized system, In simple words, Blockchain is an open and distributed ledger that stores data electronically in a digital format with identical copies across each system of computer within a network.Machine learning (ML) is a type of artificial intelligence (AI) that allows software applications to become more accurate at predicting outcomes without being explicitly programmed to do so",{"Blockchain": ["decentralized"],"Machine Learning": ["AI"]})
result = adding.addkey()
print(result)
