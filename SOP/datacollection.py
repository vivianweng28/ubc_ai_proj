import ollama 

class DataCollector:
    def __init__(self):
        self.model = 'llama3'
        userPrompt = ""
        f = open("data collection.txt", "r")
        self.questions = f.read()               # read from txt 
        self.promptCount = -1                   # prompt number in txt
        self.prompt = ""                        # specific prompt
        self.response = []                      # record response

    def nextQuestion(self):
        self.promptCount += 1                   # goto next prompt 
        if self.promptCount == 2:               # modify prompt when necessary 
            self.modifyPrompt()             
        self.prompt = f.read[self.promptCount]  # read current prompt
        stream = ollama.chat(
            model = model, 
            messages = [{'role': 'user', 'content': prompt[0]}],
            stream = True,
        )
        for chunk in stream: 
            print(chunk['message']['content'], end = '')


    def modifyPrompt(self):
        #find [], insert prompt[1] contents