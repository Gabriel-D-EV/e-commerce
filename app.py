import flet as ft


def main(page: ft.page):
    page.title = "E-Commerce"
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def charge_main_image(e):
        for item in options.controls:
            if item == e.control:
                item.opacity = 1
                main_image.src = item.image_src
            else:
                item.opacity = 0.5
                
        main_image.update()
        options.update()

    produto_imagem = ft.Container(
        bgcolor='#c9c9c9',
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='./imagens/rx3060-fr.png'
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='./imagens/rx3060-fr.png',
                            width=50,
                            height=50,
                            opacity=1,
                            on_click=charge_main_image
                        ),
                        ft.Container(
                            image_src='./imagens/rx3060-diag.png',
                            width=50,
                            height=50,
                            opacity=0.5,
                            on_click=charge_main_image
                        ),
                        ft.Container(
                            image_src='./imagens/rx3060-bp.png',
                            width=50,
                            height=50,
                            opacity=0.5,
                            on_click=charge_main_image
                        )
                    ]
                )
            ]
        )
    )

    produto_dados = ft.Container(
        padding=ft.padding.all(30),
        bgcolor='#121212',
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='GPU',
                    color='#8a2be2',
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Geforce RTX-3060',
                    color='#ffffff',
                    weight=ft.FontWeight.BOLD,
                    size=30
                ),
                ft.Text(
                    value='12GB, GDDR6, DLSS, Ray Tracing, NOVO',
                    color='#c8c8d8',
                    italic=True
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 1700,00',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER
                                ) for i in range(5)
                            ]
                        )
                    ]
                )
            ]
        )
    )

    layout = ft.Container(
        width=600,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=20, color='#8a2be2'),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                #produto_imagem,
                produto_dados
            ]
        )
    )
    
    page.add(layout)
    


if __name__ == '__main__':
    ft.app(target=main)
