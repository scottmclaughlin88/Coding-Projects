from pickle import FALSE
import random

#Inside a class, most functions need self declared.
class Record(): 
    def __init__(self,user,score):
        self.user=user
        self.score=int(score)

    def __str__(self):
        return self.user + ":" + str(self.score)

    def __repr__(self): 
        return self.user + ":" + str(self.score)

class Database():
    def __init__(self,filename):
        self.records=[]
        self.filename=filename
        self.load_records()

    def load_records(self): 
        f = open(self.filename,"r",encoding="utf8")
        lines = f.readlines()
        f.close()
        for line in lines:
#strip is used to remove blank spaces, lines, etc.
            line = line.strip() 
            user = line.split(":")[0]
            score = line.split(":")[1]
            self.records.append(Record(user,score))
        self.sort_records()

    def save_records(self):
        self.sort_records()
        f = open(self.filename,"w",encoding="utf8")
        for record in self.records:
            f.write(record.user + ":" + str(record.score) + "\n")
        f.close()
            
    def sort_records(self):
        self.records.sort(key=lambda x:x.score,reverse=True)

    def increase_score(self,user):
        found = False
        for record in self.records:
            if record.user == user:
                record.score += 1
                found = True
        if not found:
            self.records.append(Record(user,1))
        self.save_records()

class Trivia():
    def __init__(self,filename):
        self.filename=filename
        self.question_data=self.load_question_data()
        self.trivia_questions=self.create_questions()
        self.active_question = False

    def load_question_data(self):
        f = open(self.filename,"r",encoding="utf8")
        lines = f.readlines()
        f.close()
        return lines

    def create_questions(self):
        trivia_questions = []
        for question in self.question_data:
            question_info = question.strip().split(":")
            trivia_questions.append(TriviaQuestion(question_info[0],question_info[1]))
        return trivia_questions

    def random_question(self):
        self.current_question = random.choice(self.trivia_questions)
        self.active_question = True
        

class TriviaQuestion():
    def __init__(self,question,answers):
        self.question=question
        self.answers=answers.split(",")
        self.answer_index=self.get_answerindex()
        self.answers[self.answer_index] = self.answers[self.answer_index].replace("@","")

    def get_answerindex(self):
        for x in range(len(self.answers)):
            if self.answers[x].startswith("@"):
                return x

    def __str__(self):
        return self.question + str(self.answers) + str(self.answer_index)

    def get_question(self):
        return "Q: " + self.question

    def get_answers(self):
        answers_string = ""
        index = 1
        for answer in self.answers:
            answers_string += str(index) + ") " + answer + "\n"
            index += 1
        return answers_string

    def get_correct_answer(self):
        return "The correct answer was " + self.answers[self.answer_index]

trivia_host = Trivia("general.txt")
for trivia_question in trivia_host.trivia_questions:
    print(trivia_question)

# data = Database("ranking.txt")

# print(data.records)
# data.records[0].score=15
# data.save_records()
