from prompt_tokens import PromptTokens
from testing import prompt_tokens

source = prompt_tokens.PromptTokens(["I", "reside", "in", "Delhi", "."])
longest = ""

while source.has_next():
    token = source.next_token()

    if len(token) > len(longest):
        longest = token

print("Longest token:", longest)    
