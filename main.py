from customtkinter import *
from tkinter import messagebox
from tkinter import Canvas

# Array med frågor och svar
questions = [
    {"question": "Vad av följande kan du inte programmera en dator till att göra?",
     "options": ["Lösa matematiska problem",
                 "Skriva en roman",
                 "Känna kärlek",
                 "Spela schack"],
     "answer": 2,
     "type": "multiple_choice"},
    {"question": "Vad betyder binärkod?",
     "options": ["Ett språk som använder två tecken, vanligtvis 0 och 1",
                 "Ett språk som använder tre tecken, vanligtvis 0, 1 och 2",
                 "Ett språk som använder bokstäver och siffror",
                 "Ett språk som använder symboler"],
     "answer": 0,
     "type": "multiple_choice"},
    {"question": "Vad gör en kompilator?",
     "options": ["Översätter högnivåspråk till maskinkod",
                 "Översätter maskinkod till högnivåspråk",
                 "Skriver kod åt programmeraren",
                 "Testar kod för buggar"],
     "answer": 0,
     "type": "multiple_choice"},
    {"question": "Vad menas med att ett språk är objektorienterat?",
     "options": ["Att språket använder objekt och klasser för att strukturera kod",
                 "Att språket är lätt att lära sig",
                 "Att språket är snabbt att exekvera",
                 "Att språket är kompatibelt med alla operativsystem"],
     "answer": 0,
     "type": "multiple_choice"},
    {"question": "Vad menas med maskininlärning?",
     "options": ["Att datorer lär sig genom att interagera med människor",
                 "Att datorer lär sig genom att läsa böcker",
                 "Att datorer lär sig av data utan att vara explicit programmerade",
                 "Att datorer lär sig genom att spela spel"],
     "answer": 2,
     "type": "multiple_choice"},
    {"question": "När skapades den första programmerbara datorn?",
     "options": ["1970",
                 "1950",
                 "1960",
                 "1941"],
     "answer": 3,
     "type": "multiple_choice"},
    {"question": "Ta ställning till följande seriebild xkcd: Tasks, är exemplet utdaterat?",
     "options": ["Ja, det är utdaterat",
                 "Nej, det är fortfarande relevant",
                 "Delvis, vissa aspekter är fortfarande relevanta",
                 "Vet ej"],
     "answer": 1,
     "type": "multiple_choice"},
    {"question": "Vilket av följande val beskriver Moores lag?",
     "options": ["Antalet transistorer i en integrerad krets fördubblas ungefär varje två år",
                 "Datorers prestanda fördubblas varje år",
                 "Lagringskapaciteten för hårddiskar fördubblas varje år",
                 "Nätverkshastigheten fördubblas varje år"],
     "answer": 0,
     "type": "multiple_choice"},
    {"question": "Kommer Moores lag att följas i framtiden? Motivera!",
     "type": "text", "answer": ""},
    {"question": "Förklara vad open-source är, redogör även för dess nackdelar och fördelar.",
     "type": "text", "answer": ""},
    {"question": "Varför är det viktigt att hålla en konsekvent kodningsstil? Exempelvis variabelnamngivning m.m.",
     "type": "text", "answer": ""},
    {"question": "Varför behöver applikationer olika versioner för olika operativsystem?",
     "type": "text", "answer": ""},
    {"question": "Hur har AI påverkat programmeringens möjligheter och begränsningar?",
     "type": "text", "answer": ""}

]

#variabler
current_question = 0
user_answers = []

root = CTk()
root.title("Prov")
root.geometry("600x500")
set_appearance_mode("dark")

# Frames
Welcome_frame = CTkFrame(root)
question_frame = CTkFrame(root)
result_frame = CTkFrame(root)


# Visa välkommenskärmen
def start_quiz():       #startar quizet och döljer välkommen listan
    Welcome_frame.pack_forget()
    show_question()


def save_text_answer(user_input):            #sparar svaren för text frågorna samt kontrollerar om användaren skrev något innan, avslutar också quizet och visar svar om alla frågor är besvarade
    global current_question, user_answers

    if user_input.strip():
        user_answers.append(user_input)
        current_question += 1

        if current_question < len(questions):
            show_question()
        else:
            show_result()
    else:
        messagebox.showwarning("Varning", "du måste skriva ett svar innan du går vidare")






def create_scrollable_frame(parent): # funktion för att kunna skrolla!

    canvas = Canvas(parent, background="#2a2d2e", highlightthickness=0)
    scrollbar = CTkScrollbar(parent, command=canvas.yview)
    frame = CTkFrame(canvas)  # Innehållsramen som placeras i canvas

    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return frame, canvas



def show_question():            #visar frågor på skärmen och visar fråga efter fråga, samt anpassar sig till en viss typ av fråga "multiple answers" eller "text"
    global current_question

    # Rensa frågefönster
    for widget in question_frame.winfo_children():
        widget.destroy()

    # Hämta frågan
    question = questions[current_question]
    CTkLabel(question_frame, text=question["question"], font=("Arial", 14)).pack(pady=20)

    # Visa olika typer av frågor
    if question["type"] == "multiple_choice":
        option_var = StringVar(value="Välj ett alternativ")
        CTkOptionMenu(question_frame, variable=option_var, values=question["options"]).pack(pady=10)
        CTkButton(question_frame, text="Nästa", command=lambda: save_answer(option_var.get())).pack(pady=20)

    elif question["type"] == "text":
        answer_var = StringVar()
        CTkEntry(question_frame, textvariable=answer_var, font=("Arial", 14), width=400).pack(pady=10)
        CTkButton(question_frame, text="Nästa", command=lambda: save_text_answer(answer_var.get())).pack(pady=20)

    question_frame.pack()



def save_answer(selected_option):           #sparar användarens flervalssvarfrågorna, samt kontrollerar om svaret är gilitigt eller om användaren har tryckt i något
    global current_question, user_answers

    if selected_option != "Välj ett alternativ":
        user_answers.append(selected_option)
        current_question += 1

        if current_question < len(questions):
            show_question()
        else:
            show_result()
    else:
        messagebox.showwarning("Varning", "Välj ett alternativ innan du fortsätter")


def show_result():              #visar resultat för provet och räknar korrekta svar i slutet, för text frågorna visar den att den ska kontrolleras av en lärare
    question_frame.pack_forget()

    # Skapa en ny skrollbar för resultatvyn
    for widget in result_frame.winfo_children():
        widget.destroy()  # Rensa gammalt innehåll i result_frame

    scrollable_frame, canvas = create_scrollable_frame(result_frame)

    # Räkna poäng för flervalsfrågor
    score = 0
    for i, question in enumerate(questions):
        if question["type"] == "multiple_choice":
            correct_answer = question["options"][question["answer"]]
            if user_answers[i].strip().lower() == correct_answer.strip().lower():
                score += 1

    # Visa total rätt poäng
    CTkLabel(scrollable_frame,
             text=f"Du fick {score} av {len([q for q in questions if q['type'] == 'multiple_choice'])} på flervalsfrågorna!",
             font=("Arial", 14)).pack(pady=20)

    # Loopa och visa varje fråga med användarens svar och status
    for i, question in enumerate(questions):
        user_answer = user_answers[i]
        CTkLabel(scrollable_frame, text=f"Fråga {i + 1}: {question['question']}", font=("Arial", 12)).pack(pady=10)
        CTkLabel(scrollable_frame, text=f"Ditt svar: {user_answer}", font=("Arial", 12)).pack(pady=5)

        if question["type"] == "multiple_choice":
            correct_answer = question["options"][question["answer"]]
            CTkLabel(scrollable_frame, text=f"Rätt svar: {correct_answer}", font=("Arial", 12)).pack(pady=5)

        elif question["type"] == "text":
            CTkLabel(scrollable_frame, text="Detta svar ska kontrolleras av en lärare.", font=("Arial", 12),
                     fg_color="orange").pack(pady=5)

    result_frame.pack()


CTkLabel(Welcome_frame, text="Välkommen till provhanteraren", font=("Arial", 14)).pack(pady=20)
CTkButton(Welcome_frame, text="Starta quiz", command=start_quiz).pack(pady=20)
Welcome_frame.pack()



root.mainloop()
