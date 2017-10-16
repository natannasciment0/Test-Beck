import sqlite3

#sending the address to where from the BD will be created
address = r'C:\Users\user\aula\\'
connection = sqlite3.connect(address+ r"testeEstag.db")
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tb_customer_account(id_customer integer UNIQUE, \
                cpf_cnpj text, nm_customer text, is_active text, vl_total integer)')

create_table()
connection.commit()

def dataentry():
    c.execute("INSERT INTO tb_customer_account VALUES(1340, '116.029.121-10', 'José Algusto', 'ativa', 330) ")
    c.execute("INSERT INTO tb_customer_account VALUES(1400, '066.299.876-00', 'Maria Rosa', 'ativa', 430) ")
    c.execute("INSERT INTO tb_customer_account VALUES(1550, '122.117.776-12', 'Marcos Alberto', 'não ativa', 580) ")
    c.execute("INSERT INTO tb_customer_account VALUES(1701, '278.921.728-87', 'Eva Ribeiro', 'ativa', 410) ")
    c.execute("INSERT INTO tb_customer_account VALUES(1800, '221.112.018-18', 'João da Mata', 'não ativa', 720) ")
    c.execute("INSERT INTO tb_customer_account VALUES(2100, '011.144.091-34', 'Bianca Duarte', 'não ativa', 600) ")
    c.execute("INSERT INTO tb_customer_account VALUES(2550, '721.001.627-91', 'Joyce da Silva', 'ativa', 560) ")
    c.execute("INSERT INTO tb_customer_account VALUES(2730, '282.920.177-12', 'Pedro Cabral', 'não ativa', 800) ")
    c.execute("INSERT INTO tb_customer_account VALUES(2780, '181.019.728-02', 'Humberto Roberto', 'ativa', 790) ")

#dataentry()
#connection.commit()


connection.close()

connection = sqlite3.connect(r"C:\Users\user\aula\testeEstag.db")

#update the status is_active in client Bianca Duarte
connection.execute("UPDATE tb_customer_account SET is_active = 'ativo' WHERE cpf_cnpj = '011.144.091-34'")

cursor = connection.execute('select * from tb_customer_account \
                            where id_customer between 1500 and 2700 and (vl_total >560) order by vl_total desc')
cursor2 = connection.execute('select round(AVG(vl_total), 2) from tb_customer_account \
                            where id_customer between 1500 and 2700 and (vl_total >560)')
rows = cursor.fetchall()
rows2 = cursor2.fetchall()

print("AVG =", rows2[0])
print("Customers:")
for i in range(len(rows)):
    print(rows[i]);
