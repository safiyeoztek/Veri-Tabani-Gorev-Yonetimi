import database

database.create_tables()

print("1 - Kullanıcı oluştur\n2 -Görev ekle\n3 -Görevleri listele\n4 - Çıkış\n")

while True:
    secim = input("Seçim: ")

    if secim == '1':
            username = input("Kullanıcı adı: ").strip()
            if username:
                print(database.add_user(username))
            else:
                print("Kullanıcı adı boş bırakılamaz!")

    elif secim == '2':
        task = input("Görev: ").strip()
        if task:
            print(database.add_task(username, task))

    elif secim == '3':
        tasks = database.get_tasks(username)
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("Görev bulunamadı veya kullanıcı yok.")

    elif secim == '4':
        break