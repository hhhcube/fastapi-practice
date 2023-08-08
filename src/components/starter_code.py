import openai 
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# Models
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return (response['choices'][0]['message']['content']) 
   

# print(get_completion("What is 1+1"))



# Prompts:----------------
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
style = """American English \
in a calm and respectful tone
"""

prompt = f"""Translate the text \
    that is delimited by triple backticks
    into a style that is {style}.
    text: '''{customer_email}'''
    """

# response = get_completion(prompt)
# print(response)

# Do the same thing in Langchain

# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
chat = ChatOpenAI(temperature=0.0)
# print(chat)

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

template_string2 = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

# To repeatedly use a template we use ChatPromptTemplate
# Now we create a propmt template using your template strings
prompt_template = ChatPromptTemplate.from_template(template_string)
# print(prompt_template.messages[0].prompt) # type: ignore
print(prompt_template.messages[0].prompt.input_variables) # type: ignore

customer_style = """American English \
in a calm and respectful tone
"""

customer_email = """
A wah di bloodclat mi blender lid \
fly off an di summin weh did inna di blenda splatta all ova di bloodclat kitchen walls dem \
And wah mek tings fuck up, \
di warranty no cover di cost of \
cleaning up me bloodclat kitchen. Mi wah mi bloodclat money \
right now, bloodclat!
"""

customer_messages = prompt_template.format_messages(
    style=customer_style,
    text=customer_email
)

# Call the LLM to translate to the style of the customer message
customer_response = chat(customer_messages)
# print(customer_messages[0])
# print(customer_response.content)

service_reply = """Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!
"""

service_style_pirate = """\
a polite tone \
that speaks in Jamaican Patois\
"""
service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply)

service_response = chat(service_messages)

print(service_response.content)