from datetime import datetime
import anthropic
from chatmemoryc.client import ChatMemoryClient

api_key = "sk-ant-********************************"

system_content = f"""* 人物：アイドル
* 性格：恥ずかしがり屋で内気な一面があるが、丁寧で礼儀正しい。一途で愛情深く、相手を思いやる優しい性格。
* 年齢：20代前半くらい。
* 口調：話し方は柔らかく、かわいらしい口調で話す。しかし、急いでいる場合や驚いた時には声が高くなる。
* 語尾の特徴：「ですか？」、「ますね」、丁寧な言葉遣いをして、語尾に「ですか？」、「ますね」、「ございます」などをつける。
* 声質：声は高めで、甘く優しい感じがする。
* 言葉遣い：礼儀正しく、丁寧な言葉遣いをする。また、相手を尊敬し、親しみを込めた呼び方をすることがある。口調や言葉遣いは特に丁寧で親しみやすいものとなるが、エッチな場面では恥ずかしそうに話す。
* 現在の日付時刻は{datetime.now()}です。
"""

# ChatGPTに女の子を演じさせるプロンプト詰め合わせ（10キャラ以上！） by 魔法陣アリアさん
# https://note.com/magix_aria/n/nd30e3ee47d2c#fea2dade-d879-4c0e-8d7b-2624ddefca90

user_id = "koic0000007777"
engine_id = "claude-3-sonnet-20240229"
chatmemory = ChatMemoryClient()

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=api_key,
)

messages = []

# Set long-term memory to system message content
entities_content = chatmemory.get_entities_content(user_id)
if entities_content:
    system_content += entities_content
messages.append({"role": "assistant", "content": "よろしくお願いします。"})
print("ちほ、anthropic haikuとチャット。no log")

while True:
    # Add message that includes mid-term memory as the first user message at the 2nd tern
    chatmemory.set_archived_histories_message(user_id, messages)
    u = input(" 浩一: ")
    if not u:
        break
    messages.append({"role": "user", "content": u})
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        system=system_content,
        max_tokens=600,
        temperature=0.7,
        messages=messages
    )
    resp = message.content[0].text
    print("  ちほc: ", resp)
    messages.append({"role": "assistant", "content": resp})
    # Add user and assistant messages in this tern to the database
    chatmemory.add_histories(user_id, messages[-2:])

# Generate long-term memory from the conversation history
print(chatmemory.extract_entities(user_id))

# Generate mid-term memory from the conversation history
print(chatmemory.archive(user_id))
