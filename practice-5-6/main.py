from models.record import create, read, update, delete


def run():
    create(
        title="Первая запись",
        note="В этой цитате вся суть произведения",
        quotation="В это лето больше уже никто не приезжал",
        pages=[4, 4],
        paragraphs=[5, 5],
        words=[0, 8]
    )
    update(record_id=2, values_dict={
        "title": "Комментарий к первой записи",
        "note": "Однако это не для всех может быть так",
    })
    delete(record_id=5)
    print(read(record_id=1))
    print(read(record_id=2))
    print(read(record_id=2))


if __name__ == '__main__':
    run()