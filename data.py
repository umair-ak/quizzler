import requests
import html
class Data:
    def __init__(self):
        self.questions = requests.get(url = "https://opentdb.com/api.php" ,params={"amount":10 , "type":"boolean"})
        self.info_list = self.questions.json()['results']
        self.fin = []

        for item in self.info_list:
            adding = {"question":html.unescape(item['question']), 'correct_answer':item['correct_answer']}
            self.fin.append(adding)
    
    def getQuestions(self):
        return self.fin

