import random

def multiple_choice_quiz(questions_and_options):
  

  for question, options in questions_and_options:
    # Shuffle the options for this question
    random.shuffle(options)

    print(question)

    # Display the shuffled options 
    for i, option in enumerate(options):
      print(f"{chr(65 + i)}. {option}")

    print("\n") 

questions_and_options = [
    (
        "Question 1:criterion \n",
        [
            "A. Mistral",
            "B. Llama-2 ",
            "C. Gpt-neo"
        ]
    ),
    (
        "Question 2:similarity \n",
        [
            "A. Mistral",
            "B. Llama-2 ",
            "C. Gpt-neo"
        ]
    ),
    (
        "Question 3:authority \n",
        [
            "A. Mistral",
            "B. Llama-2 ",
            "C. Gpt-neo"
        ]
    ),
    (
        "Question 4:example \n",
        [
            "A. Mistral",
            "B. Llama-2 ",
            "C. Gpt-neo"
        ]
    ),
    (
        "Question 5:Goal \n",
        [
            "A. Mistral",
            "B. Llama-2 ",
            "C. Gpt-neo"
        ]
    ),
    (
        "Question 6:consequences \n",
        [
            "A. Mistral",
            "B. Llama-2 ",
            "C. Gpt-neo"
        ]
    ),
    (
        "Question 7:cimmitment \n",
        [
            "A. Mistral",
            "B. Llama-2 ",
            "C. Gpt-neo"
        ]
    )
    
]

multiple_choice_quiz(questions_and_options)
