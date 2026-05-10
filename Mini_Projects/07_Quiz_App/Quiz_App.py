class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

class QuizApp:
    def __init__(self):
        self.question = None

    def set_question(self, question):
        self.question = question

    def ask_question(self):
        print(20 * '=', 'Answer a question', 20 * '=', sep='\n')
        print(self.question.question)

    def check_answer(self, user, answer):
        if answer == self.question.correct_answer:
            print(f'{user.name}, you answer is "{answer}". Correct!\n')
            user.score += 1

        else:
            print(f'{user.name}, your answer is "{answer}". Wrong!\n')

    def show_results(self, user):
        print(f'{user.name}, you got "{user.score}" points.')

quizapp = QuizApp()

user1 = User('Ivan')
user2 = User('Anton')

quizapp.set_question(Question('How many continents are there on planet Earth?', 6))
quizapp.ask_question()
quizapp.check_answer(user1, 6)

quizapp.set_question(Question('How many oceans are there on planet Earth?', 5))
quizapp.ask_question()
quizapp.check_answer(user2, 5)

quizapp.set_question(Question('What is the capital of USA?', 'Washington'))
quizapp.ask_question()
quizapp.check_answer(user1, 'Washington')

quizapp.set_question(Question('What is the capital of Italy?', 'Rome'))
quizapp.ask_question()
quizapp.check_answer(user2, 'London')

quizapp.show_results(user1)
quizapp.show_results(user2)
