import time
import textwrap
import random
from src.ui.components import title, border

EASY = {
    10: [
        "The sun rises early and birds sing near the quiet river",
        "Small kids played football outside during the cool evening weather",
        "My laptop battery died while I was finishing the final assignment",
    ],
    
    25: [
        "The little cat jumped onto the wooden table and carefully watched the rain falling outside through the large kitchen window during breakfast time.",
        
        "A young student practiced typing every single morning because he wanted faster speed and fewer mistakes before the upcoming computer competition started.",
    ],
    
    50: [
        "The old library near our school smelled like dusty paper and coffee. Students quietly studied there for hours while the librarian organized shelves and repaired damaged books. During winter evenings the place became warm and peaceful, making everyone feel comfortable enough to forget the noisy traffic and crowded streets waiting outside the building.",
    ],
    
    100: [
        "Every weekend our group of friends visited the public park beside the lake to relax after long study sessions. Some people brought snacks while others played cricket or listened to music under the trees. Children ran across the walking paths chasing each other with endless energy while older people discussed politics, business, and local news on nearby benches. As the sun slowly disappeared behind the buildings, the lights around the lake reflected beautifully across the water. Nobody wanted to leave early because the peaceful atmosphere made ordinary evenings feel surprisingly memorable and calm after exhausting days filled with assignments, deadlines, and endless digital distractions.",
    ]
}


MEDIUM = {
    10: [
        "Technology changes rapidly forcing companies to continuously improve their software systems",
        "The scientist carefully recorded observations before presenting results to the research committee",
        "Modern cities struggle with pollution traffic overcrowding and increasing housing costs everywhere",
    ],
    
    25: [
        "Several engineers collaborated overnight to repair the damaged network infrastructure before thousands of customers completely lost internet access across multiple regions.",
        
        "The documentary explained how ancient civilizations developed trade systems agriculture and architecture despite facing harsh environmental conditions and limited resources.",
    ],
    
    50: [
        "During the international conference the speaker discussed artificial intelligence cybersecurity and automation. Many professionals expressed concern about privacy risks and job displacement while others believed advanced technology would create entirely new industries and opportunities. The debate continued long after the presentation ended because nobody could fully agree on how rapidly society should depend on intelligent systems.",
    ],
    
    100: [
        "A successful business requires much more than creative ideas or attractive advertisements. Teams must communicate effectively manage deadlines solve unexpected problems and adapt quickly whenever market conditions suddenly change. Investors usually expect continuous growth which places additional pressure on employees and leadership. At the same time customers demand faster services lower prices and reliable support across multiple digital platforms. Companies unable to balance innovation with stability often struggle against competitors that respond more efficiently to consumer expectations. Even highly profitable organizations occasionally fail because internal conflicts poor planning or weak financial decisions slowly damage long term sustainability and public trust.",
    ]
}


HARD = {
    10: [
        "Philosophical discussions frequently challenge assumptions regarding morality consciousness and individual responsibility",
        "Cybersecurity analysts investigated sophisticated attacks targeting international financial infrastructure yesterday",
        "Mathematical optimization algorithms significantly improve computational efficiency across distributed enterprise systems",
    ],
    
    25: [
        "Researchers analyzing quantum computing advancements warned governments that encryption standards protecting sensitive communication may eventually become technologically obsolete.",
        
        "The controversial journalist articulated complex geopolitical arguments while responding aggressively to criticism during the internationally televised interview last night.",
    ],
    
    50: [
        "Economic instability combined with unpredictable regulatory policies created substantial uncertainty throughout international investment markets. Financial institutions attempted to minimize exposure by diversifying assets and reevaluating risk management strategies. Meanwhile independent analysts predicted that prolonged inflation and declining consumer confidence could potentially trigger additional disruptions affecting manufacturing employment and long term technological development worldwide.",
    ],
    
    100: [
        "Throughout human history civilizations repeatedly expanded scientific understanding while simultaneously struggling with ethical responsibility and political conflict. Revolutionary discoveries transformed medicine transportation communication and industrial productivity yet these advancements also introduced increasingly dangerous weapons surveillance systems and environmental consequences. Historians often argue that technological progress alone cannot guarantee societal improvement because leadership corruption misinformation and economic inequality continue influencing global stability. In modern society digital platforms accelerate the spread of both valuable knowledge and harmful manipulation at unprecedented speed. Consequently individuals must develop critical thinking skills capable of distinguishing reliable evidence from emotional persuasion fabricated narratives and strategically engineered propaganda. Humanity really invented machines capable of performing billions of calculations per second and still cannot organize traffic properly. Extraordinary species.",
    ]
}

def play():
    title("Typing Speed Test 🧑‍💻", "My eyes are on your fingers 🫵.")
    is_invalid_word_count = True
    while is_invalid_word_count:
        words_input = input("Words (10, 25, 50, 100): ")
        if words_input.isnumeric() and int(words_input) in (10, 25, 50, 100):
            is_invalid_word_count = False
            words_input = int(words_input)
        else:
            print("❌ Invalid Input. Choose Betwen (10, 25, 50, 100)")
            
    is_invalid_difficulty = True
    while is_invalid_difficulty:
        difficulty_input = input("Difficulty (1: Easy, 2: Medium, 3: Hard): ").strip().lower()
        if difficulty_input not in ("1", "2", "3", "easy", "medium", "hard"):
            print("❌ Invalid Input Choose Betwen (1: Easy, 2: Medium, 3: Hard)")
        else:
            is_invalid_difficulty = False

            difficulty_input = "easy" if difficulty_input == "1" else difficulty_input
            difficulty_input = "medium" if difficulty_input == "2" else difficulty_input
            difficulty_input = "hard" if difficulty_input == "3" else difficulty_input

            if difficulty_input == "easy":
                    target_sentence = random.choice(EASY[words_input])
            if difficulty_input == "medium":
                    target_sentence = random.choice(MEDIUM[words_input])
            if difficulty_input == "hard":
                    target_sentence = random.choice(HARD[words_input])

    wrapped_lines = textwrap.wrap(target_sentence, width=70)
    max_line_width = max((len(line) for line in wrapped_lines), default=70)

    separator_line = "-"*(max_line_width+14)
    print(separator_line)
    for line in wrapped_lines:
            print(f"| {line:^{max_line_width + 10}} |")
    print(separator_line)

    print("Enter Click When you Ready 🏃")
    input("")
    start_time = time.time()
    user_input_sentence = input(">> ")
    elapsed = time.time() - start_time
    result = calculate_score(target_sentence, user_input_sentence, elapsed)
    score_card(result)
    
def score_card(result):    
    print(border("top", 30))
    # Header - centered roughly
    print(f"┃{'🏆 Result 🏆':^28}┃")
    print(f"┃{"-"*30}┃")
    print(border("empty", 30))
    
    # Data rows with dynamic padding to keep the box width consistent
    wpm_text = f" WORDS PER MINUTE: {result['wpm']} WPM"
    acc_text = f" ACCURACY: {result['accuracy']}%"
    coins_text = f" COINS: +{result['coins']} 🪙"
    
    print(f"┃{wpm_text:<30}┃")
    print(f"┃{acc_text:<30}┃")
    print(f"┃{coins_text:<30}┃")
    
    print(border("empty", 30))
    print(border("bottom", 30))

def calculate_score(original: str, user_typed: str, elapsed: int) -> dict:
    # filter there characted characters and wrong
    total_chars = len(  )
    correct_chars = 0
    words = original.split(" ")
    user_words = user_typed.split(" ")
    errors = []
    minimum = min(len(words), len(user_words))
    for i in range(0, minimum):
        correct_ch_in_word = sum(1 for a, b in zip(words[i], user_words[i]) if a == b)
        correct_chars += correct_ch_in_word
        if correct_ch_in_word != len(words[i]):
            errors.append([words[i], user_words[i]])

    wpm = round((correct_chars*60)/(5*elapsed))
    accuracy = round(correct_chars/total_chars * 100, 2)
    coins = 0 
    coins = 1 if accuracy > 20 else coins
    coins = 2 if accuracy > 40 else coins
    coins = 5 if accuracy > 80 else coins
    coins = 10 if accuracy > 90 else coins
    return {"wpm": wpm, "accuracy": accuracy, "coins": coins}