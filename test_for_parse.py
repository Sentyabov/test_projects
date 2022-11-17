import glob
for filename in glob.glob("C:\\Users\\m.sentyabov\\Desktop\\Данные с групп ВК\\Парсинг микрорайоны\*.txt*"):
    with open(f"{filename}", "r") as file:
        group_ids = file.read().splitlines()
    for i in group_ids:
        new_filename = filename.split('\\')
