import flet as ft
import edupage

def main(page: ft.Page):
    page.title = "Testy"
    page.vertical_alignment = ft.MainAxisAlignment.START

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)


    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    lv.controls.append(ft.Text("test1"))

    def gettesty(e):
        testy = edupage.getTest()
        for t in testy:
            lv.controls.append(ft.Text(f'{t["name"]}, {t["date"]}@{t["time"]}'))

            page.update()

    



    page.add(
        ft.IconButton(ft.icons.REFRESH, on_click=gettesty),
        lv
    )

ft.app(target=main)