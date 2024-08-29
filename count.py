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
        raise ValueError("Event must be a dictionary. In this format : {'sentence' : ' something here'}")
    
    sentence = event.get("sentence")
    
    if not isinstance(sentence, str):
        return {
            "Error": "Invalid input: 'sentence' must be a string."
        }

    count = len(sentence.split())

    return {
        "Sentence": sentence,
        "Count": count
    }