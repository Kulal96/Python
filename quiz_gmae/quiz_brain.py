class QuizBrain:
    def __init__(self,q_list):
        self.qustion_list=q_list
        self.question_number=0
        self.score=0

    def still_has_question(self):
        if self.question_number < len(self.qustion_list):
            return True
        else:
            return False
    
    def next_question(self):
        current_question=self.qustion_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"{self.question_number} {current_question.text}('True/False')")
        self.checkanswer(user_answer,current_question.answer)
    
    def checkanswer(self,u_answer,c_answer):
        if u_answer==c_answer:
            self.score+=1
            print('You got it right')
            print(f'Your score is {self.score}')
    
