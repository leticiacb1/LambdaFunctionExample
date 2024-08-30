import json
import typing

def count_words(event, context) -> typing.Dict[str, str]:
    '''
        Receive a sentence and return the number of words.
        
        Parameters:
        - event: dict, required
        The event object that contains the input to the Lambda function. 
        Expected to have a 'sentence' key.
        
        - context: object, required
        The context object provided by AWS Lambda, containing metadata and runtime information.
        
        Returns:
        - dict: A dictionary containing the original sentence and the word count.
    '''

    print("\n    [INFO] Event Recieved :  \n")
    print(event)

    if not isinstance(event, dict):
        raise ValueError("Event must be a dictionary.")

    body = event.get("body")
    if not body:
        return {
            "Error": "Invalid input: no body found."
        }

    try:
        json_body = json.loads(body)
    except json.JSONDecodeError:
        return {
            "Error": "Invalid input: unable to parse JSON body."
        }
    sentence = json_body.get("sentence")
    
    if not isinstance(sentence, str):
        return {
            "Error": "Invalid input: 'sentence' must be a string."
        }

    count = len(sentence.split())
    return {
        "Sentence": sentence,
        "Count": count
    }