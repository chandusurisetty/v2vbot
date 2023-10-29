
# pip install google-generativeai
import google.generativeai as palm
from voiceToVoice import V2v
v2v = V2v()
palm.configure(api_key="Add your Key")

models = [m for m in palm.list_models(
) if 'generateText' in m.supported_generation_methods]
model = models[0].name


response = palm.chat(messages=["Hi Bard"])
print(response.last)
v2v.toSpeak(response.last)
while True:

    sentance = v2v.toText()
    print(sentance)
    if sentance != "ok bye":
        response = response.reply(sentance)

        print(response.last)
        v2v.toSpeak(text=response.last)
    else:
        v2v.toSpeak("bye bye!!", rate=100)
        break
