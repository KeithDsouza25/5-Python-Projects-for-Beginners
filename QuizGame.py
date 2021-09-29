class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
# List of Questions
     "\nWhich of these is not a core data type in Python? \n (a) List         (b) Dictionary \n (c) Tuple        (d) Class\n\n"  ,
     "\nWhat data type is the object below ? \n L = [1, 23, ‘hello’, 1] \n (a) List         (b) Dictionary \n (c) Tuple        (d) Class\n\n",
     "\nWhich of the following statement(s) is TRUE?\nA hash function takes a message of arbitrary length and generates a fixed length code.\nA hash function takes a message of fixed length and generates a code of variable length.\nA hash function may give the same hash value for distinct messages.\n (a) I only              (b) II and III only \n (c) I and III only      (d) II only\n\n", 
     "\nWhich one of the following is the correct extension of the Python file? \n (a) .py        (b) .python \n (c) .p         (d) None of these\n\n",
     "\nWhat do we use to define a block of code in Python language? \n (a) Key          (b) Indentation \n (c) Brackets     (d) None of these\n\n",
     "\nWhich character is used in Python to make a single line comment? \n (a) / (b)// \n (c) #  (d) !\n\n",
     "\nWhat is the method inside the class in python language? \n (a) Object       (b) Function \n (c) Attribute    (d) Arguement\n\n",
     "\nWhich of the following precedence order is correct in Python? \n (a) Multiplication, Division, Addition, Subtraction, Parentheses, Exponential   (b) Division, Multiplication, Addition, Subtraction, Parentheses, Exponential \n (c) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction   (d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction\n\n",
     "\nWhich of the following is the use of id() function in python? \n (a) Every object doesn't have a unique ID   (b) ID returns the identity of the object \n (c) All of these                            (d) None of these\n\n",
     "\nWhat will be the output of 7^10 in python? \n (a) 13    (b) 14\n (c)7      (d)11\n\n",
]

# Right answers are stored here
questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "b"),
     Question(question_prompts[5], "c"),
     Question(question_prompts[6], "b"),
     Question(question_prompts[7], "d"),
     Question(question_prompts[8], "b"),
     Question(question_prompts[9], "a"),
]

def run_quiz(questions):
# Score in the quiz is counted here
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("\nYour total score is", score, "out of", len(questions))

print("Here's a basic python quiz to test your knowledge....")
run_quiz(questions)
