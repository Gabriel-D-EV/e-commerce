import flet as ft


def main(page: ft.page):
    page.scroll = ft.ScrollMode.AUTO
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
        col={'xs': 12, 'md': 6},
        bgcolor='#c9c9c9',
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='imagens/rx3060-fr.png'
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='imagens/rx3060-fr.png',
                            width=50,
                            height=50,
                            opacity=1,
                            on_click=charge_main_image
                        ),
                        ft.Container(
                            image_src='imagens/rx3060-diag.png',
                            width=50,
                            height=50,
                            opacity=0.5,
                            on_click=charge_main_image
                        ),
                        ft.Container(
                            image_src='imagens/rx3060-bp.png',
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
        col={'xs': 12, 'md': 6},
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
                    color=ft.colors.GREY,
                    italic=True
                ),
                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 1700,00',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=25
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER,
                                    size=15
                                ) for i in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    height=150,
                    selected_index=0,
                    indicator_color='#8a2be2',
                    label_color='#8a2be2',
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Com a GeForce® RTX 3060 Ti e a RTX 3060, você pode jogar os games mais atuais usando o poder da Ampere, a 2ª geração da arquitetura RTX da NVIDIA.',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='RTX 3060, NVIDIA CUDA Cores: 3584, Boost Clock (GHz): 1,78, Tamanho da memória: 12 GB / 8 GB, Tipo de memória: GDDR6.',
                                    color=ft.colors.GREY,
                                )
                            )
                        )

                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=ft.TextStyle(color='#ffffff', size=16),
                            border_color='#8a2ba2',
                            options=[
                                ft.dropdown.Option(
                                    text=f'{n} unid.'
                                ) for n in range(1, 11)
                            ]
                        )
                    ]
                ),
                ft.Container(expand=True),
                ft.ElevatedButton(
                    width=700,
                    text='Adicionar a lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(
                                width=2, color='#8a2ba2')
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: '#121212',
                            ft.MaterialState.HOVERED: '#8a2ba2'
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: '#121212'
                        }
                    )
                ),
                ft.ElevatedButton(
                    width=700,
                    text='Adicionar ao carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(
                                width=2, color=ft.colors.AMBER)
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: '#121212',
                            ft.MaterialState.HOVERED: ft.colors.AMBER
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: '#121212'
                        }
                    )
                )
            ]
        )
    )

    layout = ft.Container(
        width=700,
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
