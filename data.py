import requests
class Data:
    def __init__(self):
        self.questions = requests.get(url = "https://opentdb.com/api.php" ,params={"amount":10 , "type":"boolean"})
        self.fquestions = self.questions.json()
    
    def getQuestions(self):
        return self.fquestions
