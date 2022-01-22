from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword("China","Bitcoin Ban")
keyword_processor.add_keyword("Russia","Bitcoin Ban")


keywords_found = keyword_processor.extract_keywords("After the Chinese crackdown, the US, Kazakhstan and Russia became the world’s largest hubs for cryptocurrency mining.However, Russia’s central bank said it is weary of the vast amounts of energy required by the computers that mine cryptocurrencies. “The best solution is to introduce a ban on cryptocurrency mining in Russia,” it said.China was once the Bitcoin trading and mining capital of the world. However, the country's leadership struggled for several years to find ways to control cryptocurrency's spreading popularity and keep it from devaluing and replacing its fiat currency.")
#We get 4 instances of Bitcoin ban because of occurences of Russia 3 times and China 1 time in the above text
print(keywords_found)
