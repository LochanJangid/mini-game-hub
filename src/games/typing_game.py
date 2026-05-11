import time
import textwrap
import random
from src.ui.components import title, border
from typing import Dict, List, Union

class SentenceBank:
    """Handles the storage and retrieval of test sentence."""
    _data: Dict[str, Dict[int, List[str]]]

    def __init__(self) -> None:
        self._data = {
            "easy": {
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
        },
    "medium": {
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
    },
    "hard": {
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
    }
        pass
    
    def get_sentence(self, difficulty: str, word_count: int) -> str:
        """Retrieve a random sentence based on provide keys."""
        try:
            return random.choice(self._data[difficulty][word_count])
        except KeyError:
            raise ValueError(f"Sentnce not found for difficulty '{difficulty}' and word count '{word_count}'.")
         
class TypingSession:
    """Encapsulates the logic and state of a single typing round."""

    target_sentence: str
    user_input: str
    start_time: float
    end_time: float

    def __init__(self, target_sentence: str) -> None:
        self.target_sentence = target_sentence
        self.user_input = ""
        self.start_time = 0.0
        self.end_time = 0.0

    def start(self) -> None:
        """Records the start time."""
        self.start_time = time.time()

    def stop(self, user_input: str) -> None:
        """Records the end time and user input."""
        self.end_time = time.time()
        self.user_input = user_input

    def _get_elapsed_time(self) -> float:
        """Returns total seconds of elapsed."""
        return  self.end_time - self.start_time

    def calculate_results(self) -> Dict[str, Union[int, float]]:
        """Calculate WPM, Accuracy and Coins based on the session data."""
        elapsed = self._get_elapsed_time()

        # Edge Case: prevent Zero Division Error if user hit enter instantly
        if elapsed <= 0:
            return {"wpm": 0, "accuracy": 0.0, "coins": 0}
        
        total_chars = len(self.target_sentence.replace(" ", ""))
        # Safe Gaurd
        if total_chars == 0:
            return {"wpm": 0, "accuracy": 0.0, "coins": 0}
        
        corrected_chars = 0
        target_words = self.target_sentence.split(" ")
        typed_words = self.user_input.split(" ")
        minimum = min(len(target_words), len(typed_words))
        for i in range(minimum):
            corrected_ch_in_word = sum(
                1 for a, b in zip(target_words[i], typed_words[i]) if a == b
            )
            corrected_chars += corrected_ch_in_word
        
        wpm = round((corrected_chars * 60)/(5*elapsed))
        accuracy = round((corrected_chars / total_chars) * 100, 2)
        coins = 0
        if accuracy > 90:
            coins = 10
        elif accuracy > 80:
            coins = 5
        elif accuracy > 40:
            coins = 2
        elif accuracy > 20:
            coins = 1

        return {
            "wpm": wpm, 
            "accuracy": accuracy, 
            "coins": coins}

class TerminalUI:
    
    @staticmethod
    def display_title() -> None:
        """Display the game title."""
        title("Typing Speed Test 🧑‍💻", "My eyes are on your fingers 🫵.")

    @staticmethod
    def prompt_word_count() -> int:
        """Prompt word count, handle input related errors and return it."""
        while True:
            try:
                word_count = int(input("Words (10, 25, 50, 100): "))
                if word_count in (10, 25, 50, 100):
                    break
                print("❌ Please Choose input for word count between (10, 25, 50, 100).")
            except ValueError:
                print('❌ Please give only number input.')
        return word_count
            
    
    @staticmethod
    def prompt_difficulty() -> str:
        """prompt difficulty, handle input related errors and return it."""
        while True:
            difficulty = input("Difficulty (easy/medium/hard): ").strip().lower()
            if difficulty in ("easy", "medium", "hard"):
                break
            print('❌ Invalid input Choose Betwen (easy/medium/hard).')
        return difficulty

    @staticmethod
    def display_target_text(sentence: str) -> None:
        """Display the target text by wrapping it in a box."""
        wrapped_lines = textwrap.wrap(sentence, width=70)
        max_line_width = max((len(line) for line in sentence), default=70)

        separator_line = "-"*(max_line_width+14)
        print(separator_line)
        for line in wrapped_lines:
                print(f"| {line:^{max_line_width + 10}} |")
        print(separator_line)

    @staticmethod
    def display_score_card(result: Dict[str, Union[int, float]]) -> None:
        """Display score card of Gamer."""
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

class TypingGame:
    """The main controller coordinating the game flow."""

    bank: SentenceBank
    ui: TerminalUI

    def __init__(self) -> None:
        self.bank = SentenceBank()
        self.ui = TerminalUI()

    def run(self) -> None:
        """The center point which connect everything and run game."""
        self.ui.display_title()
        word_count = self.ui.prompt_word_count()
        difficulty = self.ui.prompt_difficulty()
        target_sentence = self.bank.get_sentence(difficulty, word_count)
        self.ui.display_target_text(target_sentence)

        print("When you ready hit enter ↲.")
        session = TypingSession(target_sentence)
        input() # Start Trigger
        session.start()
        user_input = input(">> ")
        session.stop(user_input)
        results = session.calculate_results()
        self.ui.display_score_card(results)