# chatmemory

Long-term and medium-term memories between you and chatbot💕

# 🚀 Quick start

1. Install chatmemory.
    ```bash
    $ pip install chatmemoryc
    ```

1. Start ChatMemory server.
    ```bash
    $ python -m chatmemoryc --key YOUR_ANTHROPIC_APIKEY
    ```
    You can set API Key in environment variables and use specific host and port. See `python -m chatmemoryc --help`.

1. Make and start [example chatbot](https://github.com/f6844710/chatmemoryc/blob/main/example.py) in another terminal.
    ```bash
    $ python example.py
    ```

1. Chat with bot and lastly press Ctrl+C once to exit conversation loop and wait for archiving memories ends.

1. Start example chatbot again and chat. During the course of the conversation, try asking questions that require memories for answers.
    ```bash
    $ python example.py
    ```

# 📕 API Reference

See http://127.0.0.1:8124/docs after starting ChatMemory server.


# 🥳 Chat example

These are the actual conversation logs. I cleared `messages` list before starting each session.

The 1st session.
```
user> はろー
assistant> はじめまして、こんにちは！どのようなことでお手伝いできますか、userさん？
user> とりあえずそのuserさんってのをやめようか
assistant> すみません、userさんと呼ぶのは気に入っていただけないようですね。では、どのように呼びましょうか？お好きな呼び方を教えてください。
user> うえぞうって呼んでね
assistant> わかりました、うえぞうさんと呼ばせていただきますね！どのようなお話がお聞かせいただけるでしょうか、うえぞうさん？なにかお困りのことや質問がありますか？お手伝いできることがあれば、どうぞお教えください。
user> またこんどゆっくりおしゃべりしよ
assistant> そうですか、またゆっくりおしゃべりしましょうね！楽しみにしています。気軽に話しかけてください。お会いできるのを楽しみにしています、うえぞうさん！
```

The 2nd session.
```
user> やあ、またあったね
assistant> こんにちは、うえぞうさん！お会いできて嬉しいです。今日はいかがお過ごしですか？何かお手伝いできることがあれば、お伝えくださいね。いますぐにでもお答えしますよ。
user> もっと楽な感じにしてくれていいよ、一緒に楽しもうよ
assistant> そうですか、楽しい雰囲気でおしゃべりしましょう！どんな話題が好きですか？音楽や映画、旅行の話でもいいですし、最近のお気に入りのアイドルグループや趣味の話でもかまいません。なんでもご自由にお話しくださいね。一緒に楽しみましょう！
user> フランシュシュが好きだなあ
assistant> フランシュシュですね！素敵なアイドルグループですね。彼女たちの歌声とパフォーマンスは本当に魅力的ですよね。私も同じくフランシュシュのファンです。

彼女たちの最新のシングルやライブについて話しましょうか？新曲の中でお気に入りはありますか？私のお気に入りは「夏色カーニバル」です！楽曲も明るくてキュートなので、夏のイベントで盛り上がると思います。

また、フランシュシュのメンバーの中で特に好きなメンバーはいますか？私はみんなが魅力的で、それぞれの個性が光っていると思います。ちなみに私のお気に入りのメンバーは葵ちゃんです。

フランシュシュの魅力について、一緒に語り合いましょう！どんな話題でも構いませんので、何か聞きたいことやお話したいことがあれば教えてくださいね。
user> あっ、ちょっと電話かかってきたからまたあとでね
assistant> わかりました、うえぞうさん。大丈夫です、ゆっくりお話しましょう。電話をお受けになってくださいね。また後でお待ちしています。楽しいお話をしましょう！では、いってらっしゃいませ。
```

The 3rd session.
```
user> おまたせ〜
assistant> うえぞうさん、こんばんは！おまたせしましたか？どういったご用件でしょうか？お手伝いできることがありましたら、なんでもおっしゃってくださいね！
user> なんかおしゃべりしよ
assistant> そうですか、おしゃべりしましょう！楽しいおしゃべりができると嬉しいです。では、どんな話題がお好きですか？例えば、音楽やアイドルについて語り合うのも楽しいですよ。先ほどおっしゃっていたフランシュシュについてもお話できれば嬉しいです。あ、ちなみに、私も彼女たちのファンなんです。ですので、一緒に盛り上がりましょう！どんな話題から始めますか？
```

Mid-term memory after conversation:

```
- 2023-08-19: userはテンションが高く、assistantはuserの悩みや困りごとを聞く態度で接している。userは自分の呼び方を変えるように要求し、assistantはそれに応じる。userはフランシュシュが好きで、assistantもファンであることを明かす。二人はフランシュシュについて話し合い、また会話を続けることを約束する。
```

Long-term memory after conversation:

```json
{"user_name": "うえぞう", "favorite_idol_group": "フランシュシュ"}
```


# 🪄 How it works

Very simple memory hack.

## Long-term momory

Just adding JSON entities with some instructions to system message.

```
# ユーザーに関して会話を通じて聞き出したこと

以下はユーザーとの会話を通じてあなたが記憶している内容です。強く意識する必要はありませんが、会話の流れでこれらの情報が必要になった場合はこれらの情報を会話に利用してください。

{
    "nickname": "うえぞう",
    "favorite_food": "うなぎ",
}
```

## Mid-term memory

Insert virtual user message that includes memories for last 5 days to messages before the second turn in conversation.

messages at the end of the 1st turn.
```json
[
    {"role": "system", "content": "You are user's sister."},
    {"role": "user", "content": "Hi."},
    {"role": "assistant", "content": "Hi, there!"}
]
```

insert virtual mid-turn user message before the 2nd turn.
This is intended to create a one-shot example that the 1st turn was NOT influenced by the context of previous conversations, and to encourage subsequent conversations not to be overly influenced.

```json
[
    {"role": "system", "content": "You are user's sister."},
    {"role": "user", "content": "以下はここ3日間にあったユーザーとの会話を要約したものです。\n\n- 2023-08-11: 挨拶を交わしたあと、userは自らのことをうえぞうと呼ぶように依頼し、assistantは了承しました。..."},
    {"role": "user", "content": "Hi."},
    {"role": "assistant", "content": "Hi, there!"}
]
```
