# Bob is a lackadaisical teenager. In conversation, his responses are very limited.
# Bob answers 'Sure.' if you ask him a question, such as "How are you?".
# He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.
# Bob's conversational partner is a purist when it comes to written communication and always follows normal rules regarding sentence punctuation in English.

def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    if is_shout:
        if is_question:
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    if is_question:
        return 'Sure.'
    return 'Whatever.' 
