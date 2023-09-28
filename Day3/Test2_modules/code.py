#импортировать модуль
import datamodule

data = datamodule.data_from_json('data.json')
#используя функции из модуля считать данные из файла data.json, преобразовать в словарь, вывести данные о пользователе по ключам ['name','username','job','allergy','mail','married']
datamodule.info(data, 'name', 'username', 'job', 'allergy', 'mail', 'married')

#Запросить изменение нескольких параметров, допустим профессии, компании и даты выхода на пенсию
#datamodule.change_value('data.json', "name", "Иван Петрович Янсковский")