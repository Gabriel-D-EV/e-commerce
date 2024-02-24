import flet as ft


def main(page: ft.page):
    page.bgcolor = ft.colors.BLACK

    def charge_main_image(e):
        ...

    produto_imagem = ft.Container(
        bgcolor='#121212',
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='./imagens/rx3060-frent.png',
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='./imagens/rx3060-frent.png',
                            width=50,
                            height=50,
                            margin=ft.margin.all(10),
                            opacity=1,
                            on_click=charge_main_image
                        ),
                        ft.Container(
                            image_src='./imagens/rx3060-diag.png',
                            width=50,
                            height=50,
                            margin=ft.margin.all(10),
                            opacity=0.5,
                            on_click=charge_main_image
                        ),
                        ft.Container(
                            image_src='./imagens/rx3060-bp.png',
                            width=50,
                            height=50,
                            margin=ft.margin.all(10),
                            opacity=0.5,
                            on_click=charge_main_image
                        )
                    ]
                )
            ]
        )
    )

    produto_dados = ft.Container()

    layout = ft.Container(
        width=600,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=20, color='#8a2be2'),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                produto_imagem,
                produto_dados
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
