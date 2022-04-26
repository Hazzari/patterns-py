class FormattedText:
    def __init__(self, plaint_text):
        self.plaint_text = plaint_text
        # Проблема: если загрузить слишком большой текст - придется хранить большой список [False]
        self.caps = [False] * len(plaint_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.plaint_text)):
            c = self.plaint_text[i]
            result.append(
                c.upper() if self.caps[i] else c
            )
        return ''.join(result)


# Шаблон приспособленец
class BetterFormattedText:
    def __init__(self, plaint_text):
        self.plaint_text = plaint_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        range_ = self.TextRange(start, end)
        self.formatting.append(range_)
        return range_

    def __str__(self):
        result = []
        for i in range(len(self.plaint_text)):
            c = self.plaint_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            result.append(c)
        return ''.join(result)


if __name__ == '__main__':
    text = 'Тут какой то текст для примера работы'
    ft = FormattedText(text)
    ft.capitalize(5, 15)
    print(ft)

    bft = BetterFormattedText(text)
    bft.get_range(7, 25).capitalize = True
    print(bft)
