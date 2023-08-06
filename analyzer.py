import openai
import json
import re
import ast

# Replace with your own API key
openai.api_key = "INSERT KEY HERE!"

def get_criteria(question):
    with open('get_learning_objectives.txt', 'r') as file:
        contents = file.read()

    prompt = contents.replace('[text]', question)

    # Call the OpenAI API and store the response in a variable
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = response["choices"][0]["text"]

    #I need to fix this part of the code to avoid unconsistent results.

    response = '['+response

    text = response.strip('[]')  # remove the square brackets
    lst_response = text.split(', ')   # split at each comma and remove any whitespace

    return (lst_response)

def analyze_text(text):
    with open('prompt.txt', 'r') as file:
        # Read the entire contents of the file and store them in a variable
        contents = file.read()

    prompt = contents.replace('[text]', text)

    # Call the OpenAI API and store the response in a variable

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Store the JSON object in a variable
    json_object = response["choices"][0]["text"]

    json_object = json.loads('{'+json_object)

    # Iterate over the questions
    for question in json_object['questions']:
    
        question['eval_items'] = get_criteria(question['question'])

    return json_object

def eval(answer, eval_items):

    with open('eval_items.txt', 'r') as file:
        contents = file.read()
    
    prompt = contents.replace('[answer]', answer).replace('[eval_items]', str(eval_items))

    # Call the OpenAI API and store the response in a variable
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = response["choices"][0]["text"]
    response = '['+response

    return (response) 

def correct(modified_json):
    
    for question in modified_json['questions']:
        question['eval_results'] = eval(question['answer'],question['eval_items'])
        
    # Initialize the score variable
    score = 0
    max_score = 0

    # Process the JSON data
    for question in modified_json['questions']:
        eval_results_str = question['eval_results']
        eval_results = ast.literal_eval(eval_results_str)
        marks = eval_results[:-1]
        comment = eval_results[-1]
        question['marks'] = marks
        question['comment'] = comment
        del question['eval_results']
        
        # Calculate the eval_points field
        true_count = sum(marks)
        true_ratio = true_count / len(marks)
        total_points = question.get("total points", 1)
        eval_points = true_ratio * total_points
        question['eval_points'] = eval_points
        
        # Update the score
        score += eval_points
        max_score += total_points

    # Add the score field to the JSON data
    modified_json['final score'] = round((score/max_score * 10),2)

    return modified_json