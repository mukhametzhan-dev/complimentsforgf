import telebot
import random

# Replace 'YOUR_BOT_TOKEN' with the actual token you received from BotFather
bot = telebot.TeleBot('6439203293:AAE9NYQO9wymDznSebxkk_IVnFWJK9x_vuE')
heart_strings = [
    "(●♡∀♡)",
    "(｡♥‿♥｡)",
    "(♥ω♥ ) ~♪",
    "(♥ω♥*)",
    "(✿ ♥‿♥)",
    "✿♥‿♥✿",
    "٩(♡ε♡ )۶",
    "乂❤‿❤乂",
    "♱♡‿♡♰",
    "⊆♥_㇁♥⊇",
    "(●♡∀♡))ヾ☆*。",
    "❤⃛ヾ(๑❛ ▿ ◠๑ )",
    "♡(ŐωŐ人)",
    "♥(ˆ⌣ˆԅ)",
    "༼♥ل͜♥༽",
    "(●♡∀♡))ヾ☆*。",
    "(ﾉ´ з `)ノ",
    "(♡-_-♡)",
    "(❤‿❤)♡",
    "(❤ω❤)",
    "(❤‿❤✿)",
    "(◠‿◠✿)",
    "(◠﹏◠✿)",
    "（＊＾Ｕ＾）人（≧Ｖ≦＊）/",
    "ôヮô",
    "∧( ‘Θ’ )∧( ‘Θ’ )∧",
    "(¤﹏¤)",
    "●‿●",
    "ʕ·ᴥ·ʔ",
    "＼（＾○＾）人（＾○＾）／",
    "ヾ(＠⌒▽⌒＠)ﾉ",
    "(°∀°)",
    "ヾ｜￣ー￣｜ﾉ",
    "(☉‿☉✿)",
    "┏(＾＾)┛┗(＾＾)",
    "┏(＾＾)┛┗(＾＾)┓",
    "(◡‿◡✿)",
    "✿❤ ‿ ❤✿",
    "ヽ(‘ ∇‘ )ヽ(‘ ∇‘ )ノ",
    "☆(❁‿❁)☆(❁‿❁)☆",
    "❀❤ ‿ ❤❀",
    "ヽ(^◇^*)/(•⊙ω⊙•)",
    "!⑈ˆ~ˆ!!⑈ˆ~ˆ!⑈(*^ -^*)(*^ -^*)",
    "(⊙‿⊙✿)(⊙‿⊙✿)",
    "(ﾟヮﾟ)(ﾟヮﾟ)",
    "¢‿¢",
    "ヅ",
    "●ᴥ●",
    "(∪ ◡ ∪)(∪ ◡ ∪)",
    "｡❤ ‿ ｡❤ ‿ ❤｡",
    "(✿◠‿◠)(✿◠‿◠)",
    "(￣ｰ￣)(￣ｰ￣)",
    "╰(◡‿◡✿╰)╰(◡‿◡✿╰)",
    "~,~~,~(ﾉ❤ヮ❤)ﾉ*:(ﾉ❤ヮ❤)ﾉ*:･ﾟ✧",
    "(*~▽~)(*~▽~)❀‿❀",
    "❤‿❤(^L^)(^L^)",
    "(^▽^)(^▽^)❤",
    "◡ ❤ ◡ ❤",
    "(❤‿❤✿)(❤‿❤✿)",
    "（ （ ；´Д｀）",
    "⊙﹏⊙✿｡✿",
    "ヽ(゜∇゜)ヽ(゜∇゜)ノ",
    "｡(✿‿✿)｡(✿‿✿)｡",
    "(´ー｀)(´ー｀)",
    "ツ",
    "q(❂‿❂)pq(❂‿❂)p",
    "( ́ ❤◞ε◟❤`)( ́ ❤◞ε◟❤`)",
    "☆⌒ヽ(*'､^*)",
    "(ღ˘⌣˘ღ)",
    "╰(*´︶`*)╯♡",
    "♡ ～('▽^人",
    "｡❤ ‿ ｡❤ ‿ ❤｡",
    "❀❤ ‿ ❤❀",
    "❤ ‿ ❤✿",
    "{❤ ◡ ❤}",
    "(>‘o’)>",
    "シ",
    "(❀‿❀)",
    "ヾ(●⌒∇⌒●)ﾉ",
    "（ （ ´∀｀）",
    "☾˙❀‿❀˙☽",
    "❤",
    "(ɔˆз(ˆ⌣ˆc)",
    "(˘∀˘)/(μ‿μ)",
    "❤",
    "(´,,•ω•,,)♡",
    "(/^-^(^ ^*)/",
    "♡",
    "(♡°▽°♡)",
    "(─‿‿─)♡",
    "(´ ε ` )♡",
    "(´｡• ω •｡`)",
    "♡",
    "♡＼(￣▽￣)／♡",
    "(°٢° )( °٢° )",
    "Ü",
    "(●´ω｀●) ❤‿❤",
    "ᵔᴥᵔ",
    "◙‿◙",
    "ヽ(ﾟｰﾟ*ヽ)ヽ(*ﾟｰﾟ*)ﾉ(ﾉ*ﾟｰﾟ)ﾉ",
    "create list of these strings in python",
]
compliments = [
    "You're the most amazing person I know.",
    "Your smile brightens up my day.",
    "You make the world a better place just by being in it.",
    "I'm grateful to have you in my life.",
    "You're incredibly special to me.",
    "Your kindness and compassion inspire me.",
    "You're a true gift.","You are gorgeous."," You do not need makeup. You are already so naturally beautiful.","You are adorable.","You are really cute.",
    "You are adorable.",
    "You look mesmerizing.",
    "You look prettier than a picture.",
    "You are alluring.",
    "You look dazzling.",
    "You are attractive.",
    "You are elegant.",
    "You are very fashionable.",
    "You are breathtaking.",
    "You are beautiful.",
    "You are gorgeous.",
    "I love your eyes.",
    "I love your hands.",
    "I love your lips.",
    "You have the most beautiful smile.",
    "I love how beautiful you look when you sleep.",
    "I like your style.",
    "Your sense of fashion is amazing.",
    "I like your dress.",
    "You have the most beautiful, radiant eyes.",
    "You have amazing cheekbones.",
    "I like your hair.",
    "You have a really great sense of fashion.",
    "You have such a talent for putting together the most gorgeous outfits.",
    "You really know how to dress well.",
    "I love how curly your hair is.",
    "I love how straight your hair is.",
    "I wish I had your hair.",
    "You are so gorgeous and that is the least interesting thing about you.",
    "You are so good with makeup. It looks amazing.",
    "You look even more beautiful without makeup.",
    "You are such a natural beauty.",
    "You look stunning in that dress.",
    "You are so good at putting clothes together. You could be a stylist.",
    "You are so kissable.",
    "You are intoxicating.",
    "I love how sensual you are.",
    "I love how comfortable you are in your own body.",
    "I love your curves.",
    "You are the sweetest.",
    "You are my safe place.",
    "I feel so happy here with you.",
    "There is something about being with you that makes me want to be the best person that I can be.",
    "You never fail to show me that you care about me. Thank you for that.",
    "You are the most loveliest person I have been with.",
    "How did I get so lucky to have you in my life?",
    "You know how to make me feel like a man.",
    "You make me the happiest person in the world.",
    "You are too adorable.",
    "You are the reason that I wake up every day with a huge smile on my face.",
    "You are the sweetest.",
    "Nobody in this world makes me happier than you do.",
    "To me, you are perfect.",
    "Could you be any cuter?",
    "You cook better than my mom.",
    "I love that I can just be myself when I am with you.",
    "I never have to pretend to be someone else when I am with you.",
    "Whoever is lucky enough to end up with you will never be bored a day in their life.",
    "You are my greatest adventure.",
    "You are such a good kisser.",
    "You just take my breath away.",
    "You have the softest kisses.",
    "You are a strong, sensual person.",
    "You are so sultry.",
    "I love every inch of you.",
    "You are a dream come to life.",
    "You are my dream come true.",
    "They say that there are plenty of fish in the sea, but you are my perfect catch.",
    "I love holding you in my arms.",
    "I love holding you in my embrace.",
    "Your skin is so soft.",
    "I feel so much happier around you.",
    "With you in my life, everything just makes sense.",
    "You fill up an empty space in my heart that I never knew existed.",
    "You make me feel so full in my heart and in my soul.",
    "I could listen to you talk for hours and never get tired of it.",
    "I love how confident you are. It makes me even more attracted to you.",
    "You smell so nice.",
    "You are always the most beautiful person in the room.",
    "My friends love you. And that is how I know that you are the real deal.",
    "My parents love you. That is how I know that you are the right person for me.",
    "I love how well you get along with my family.",
    "You are a part of the family now.",
    "You are everything to me.",
    "You are my whole world.",
    "You are my entire universe.",
    "You complete me.",
    "Being with you means the world to me.",
    "Being with you has made me so happy.",
    "You are the first thing that I want to wake up to every morning and the last thing I want to see before I fall asleep. I want my days to begin and end with you.",
    "Without you standing by my side, my life would have no meaning or purpose.",
    "I would rather spend time with you than with my friends tonight.",
    "I cannot keep my eyes off of you.",
   "My whole life changed the day I met you" , "You’re my dream girl. Cute!", " i want you" , " i love your boobs " , " I love how your smell"]


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = telebot.types.KeyboardButton("compliment")
    markup.add(item)
    bot.send_message(message.chat.id, 'Hello , maybe i am busy with work/study , however you can get there random compliment❤😁', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def send_compliment(message):
    if message.text == "get a compliment":
        compliment = random.choice(compliments)
        string = random.choice(heart_strings)
        bot.send_message(message.chat.id, compliment)
        bot.send_message(message.chat.id, string)
bot.polling()
