import re

class PhoneBooth:
    def __init__(self):
        self.state = "idle"
        self.money = 0
        self.call_cost = 0

    def process_input(self, input_str):
        if self.state == "idle":
            if input_str == "LEVANTAR":
                self.state = "receiving_money"
                return "Introduza moedas."
            else:
                return "Telefone desligado."
        elif self.state == "receiving_money":
            match = re.match(r"^MOEDA\s+((?:\d+e)?\d+[cCe]|\s)+$", input_str)
            if match:
                money_list = re.findall(r"((?:\d+e)?\d+[cCe])", input_str)
                money_sum = sum(self.parse_money(m) for m in money_list)
                self.money += money_sum
                return f"saldo = {self.format_money(self.money)}"
            elif input_str == "POUSAR":
                if self.money > 0:
                    return f"troco={self.format_money(self.money)}; Volte sempre!"
                else:
                    return "Volte sempre!"
            else:
                return "moeda inválida"
        elif self.state == "dialing":
            match = re.match(r"^T=(\d{9}|\d{2}\d+)$", input_str)
            if match:
                number = match.group(1)
                if number.startswith("601") or number.startswith("641"):
                    return "Esse número não é permitido neste telefone. Queira discar novo número!"
                elif number.startswith("00"):
                    if self.money >= 1.5:
                        self.money -= 1.5
                        self.call_cost = 1.5
                        self.state = "calling"
                        return f"Estabelecendo ligação com {number}..."
                    else:
                        return "Saldo insuficiente para chamada internacional."
                elif number.startswith("2"):
                    if self.money >= 0.25:
                        self.money -= 0.25
                        self.call_cost = 0.25
                        self.state = "calling"
                        return f"Estabelecendo ligação com {number}..."
                    else:
                        return "Saldo insuficiente para chamada nacional."
                elif number.startswith("800"):
                    self.call_cost = 0
                    self.state = "calling"
                    return f"Estabelecendo ligação com {number}..."
                elif number.startswith("808"):
                    self.call_cost = 0.1
                    self.money -= 0.1
                    self.state = "calling"
                    return f"Estabelecendo ligação com {number}..."
                else:
                    return "Número de telefone inválido."
            else:
                return "Número de telefone inválido."
        elif self.state == "calling":
            self.state = "receiving_money"
            return f"Ligação terminada. Custo da chamada: {self.format_money(self.call_cost)}. Saldo restante: {self.format_money(self.money)}"

    def parse_money(self, money_str):
        if money_str.endswith("e"):
            return int(money_str[:-1]) * 100
        elif money_str.endswith("c"):
            return int(money_str[:-1])
        elif money_str.endswith("E"):
            return int(money_str[:-1]) * 10000
        else:
            return 0

    def format_money(self, money):
        return f"R$ {money/100:.2f}"


phone_booth = PhoneBooth()
while True:
    user_input = input(">> ")
    output = phone_booth.process_input(user_input)
    print(output)
