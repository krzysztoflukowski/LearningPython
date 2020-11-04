# Stacks (LIFO)
# Działanie stosu można opisać na zasadzie działania przeglądarki
# przechodzenie pomiędzy stronami
# czyli byliśmy na wp.pl poszliśmy na onet.pl to wp.pl powinno zostać
# zapamiętane w historii dzięki temu będziemy mogli się cofnąć

# Do przechowywania Stosu możemy użyć Listy

class BrowserSimulator:
    def __init__(self):
        self.browser_history = []

    def print_browser_history(self):
        if self.browser_history:
            for website in reversed(self.browser_history):
                print(website)
        else:
            print("History is empty.")

    def add_website_to_history(self, website):
        self.browser_history.append(website)

    def get_current_page(self):
        if self.browser_history:
            return self.browser_history[-1]
        return None

    def go_beck(self):
        if self.browser_history:
            self.browser_history.pop()


b = BrowserSimulator()

b.add_website_to_history("www.wp.pl")
b.add_website_to_history("www.Onet.pl")
b.add_website_to_history("www.softvig.pl")

b.print_browser_history()

b.add_website_to_history("www.google.pl")
print("Current page:", b.get_current_page())

b.go_beck()
print("Current page:", b.get_current_page())

b.go_beck()
b.go_beck()
b.go_beck()

print("Current page:", b.get_current_page())
b.print_browser_history()
