from easygui import buttonbox, msgbox, diropenbox
from Catalog import Catalog
from Translator import Tranlator

if __name__ == "__main__":
    log = "ReTrans"
    translate_sys = ("Yandex", "Google")
    trans_sys = buttonbox("Выберите какой системой перевода воспользоваться\nРекомендую ЯНДЕКС", log, translate_sys)
    if trans_sys == translate_sys[1]:
        num = 0
    else:
        num = 1
    trans = Tranlator(num)
    msgbox('Выбери каталог\nВ котором надо УНИЧТОЖИТЬ транслит', log, ('Выбрать каталог'))
    path = diropenbox()
    dir = Catalog(path)
    list_files = dir.list_file()
    trans.site_translator()
    msgbox('Решите капчу и нажмите продолжить\nЕсли капчи нет => продолжить', log, ('Продолжить'))
    dir.go_path()
    for one in list_files:
        n, e = dir.expansion_file(one)
        t = trans.translate(n)
        new = t.replace("_", " ", 255)
        full_name = f"{new}.{e}"
        dir.rename_file(one, full_name)
    trans.closed()
    exit()
