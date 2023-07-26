import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'd20':
        return str(random.randint(1,20 ))
    
    if p_message == 'd12':
        return str(random.randint(1,12 ))
    
    if p_message == 'd10':
        return str(random.randint(1,10 ))
    
    if p_message == 'd8':
        return str(random.randint(1,8 ))
    
    if p_message == 'd6':
        return str(random.randint(1,6 ))
    
    if p_message == 'd4':
        return str(random.randint(1,4 ))
    
    if p_message == '!help':
        return 'This is a help message that you can modify.'
    
    return 'Roll to roll dice'

    
    