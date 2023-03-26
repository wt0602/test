import openai
def generate_prompt(prompt):
    return "请为我的论文进行润色，论文如下：{}".fromat(prompt);
def openai_reply(content, apikey):
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": generate_prompt(content)}
        ],
        tenperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content

while True:
    prompt=input("-------------------------\n")
    if prompt!="":
        response=openai_reply(prompt,"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")
        print(response)