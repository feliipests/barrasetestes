import tkinter as tk

class RoboEntrevistado:
    def __init__(self):
        self.perguntas = [
            "Qual é o seu nome?",
            "Qual é a sua idade?",
            "O que você gosta de fazer?",
            "Qual é a sua cor favorita?",
            "Qual é a sua comida preferida?",
            "Você tem algum hobby?",
            "Qual é a sua música favorita?",
            "O que você faria se fosse humano?",
            "Fim da entrevista. Obrigado!"
        ]
        self.respostas = [
            "Meu nome é Zii Bot.",
            "Eu sou um robô, não tenho idade.",
            "Eu gosto de executar tarefas e ajudar as pessoas.",
            "Não tenho preferência de cor, mas se fosse escolher diria amarelo.",
            "Como sou um robô, não como comida.",
            "Eu gosto de aprender coisas novas.",
            "Não tenho preferência de música, mas gosto de sons eletrônicos.",
            "Se eu fosse humano, gostaria de viajar pelo mundo e explorar diferentes culturas.",
            "Espero ter ajudado. Até mais!"
        ]
        self.indice_pergunta = 0

        self.janela = tk.Tk()
        self.janela.title("Entrevista com o Robô")
        self.janela.configure(background="#f2f2f2")  # Define a cor de fundo da janela

        self.label_resposta = tk.Label(self.janela, text="", font=("Arial", 14), bg="#f2f2f2")
        self.label_resposta.pack(pady=20)

        self.botao_a = tk.Button(self.janela, text="A", font=("Arial", 12), width=10, command=self.responder_pergunta)
        self.botao_a.pack(side=tk.LEFT, padx=10)

        self.botao_b = tk.Button(self.janela, text="B", font=("Arial", 12), width=10, command=self.responder_pergunta)
        self.botao_b.pack(side=tk.LEFT, padx=10)

        self.proxima_pergunta()

        self.janela.mainloop()

    def proxima_pergunta(self):
        if self.indice_pergunta < len(self.perguntas):
            pergunta_atual = self.perguntas[self.indice_pergunta]
            self.indice_pergunta += 1
            self.botao_a["text"] = "Próxima"
            self.botao_b["text"] = "Respostas"
            self.label_resposta["text"] = pergunta_atual
        else:
            self.janela.quit()

    def responder_pergunta(self):
        resposta_atual = self.respostas[self.indice_pergunta - 1]
        self.label_resposta.configure(text=resposta_atual)
        self.botao_a["text"] = "Próxima"
        self.botao_b["text"] = ""
        self.botao_a.configure(command=self.proxima_pergunta)

robo = RoboEntrevistado()
