import flet, flet_core.types

def main(page: flet.Page) -> None:
    def open_checkout(event: str | None = None) -> None:
        my_coffee_shop_text.visible = False

        espresso_text.visible = False
        espresso_image.visible = False
        espresso_button.visible = False

        americano_text.visible = False
        americano_image.visible = False
        americano_button.visible = False

        capucino_text.visible = False
        capucino_image.visible = False
        capucino_button.visible = False

        latte_text.visible = False
        latte_image.visible = False
        latte_button.visible = False

        mocha_text.visible = False
        mocha_image.visible = False
        mocha_button.visible = False

        ice_espresso_text.visible = False
        ice_espresso_image.visible = False
        ice_espresso_button.visible = False

        ice_americano_text.visible = False
        ice_americano_image.visible = False
        ice_americano_button.visible = False

        ice_capucino_text.visible = False
        ice_capucino_image.visible = False
        ice_capucino_button.visible = False

        ice_latte_text.visible = False
        ice_latte_image.visible = False
        ice_latte_button.visible = False

        ice_mocha_text.visible = False
        ice_mocha_image.visible = False
        ice_mocha_button.visible = False

        checkout_button.visible = False
        clean_order_button.visible = False

        sum_text.visible = True
        sum_of_order.visible = True
        currency_text.visible = True
        order_text.visible = True
        go_back_button.visible = True
        continue_to_payment_button.visible = True

        page.update()

    def go_back(event: str | None = None) -> None:
        my_coffee_shop_text.visible = True

        espresso_text.visible = True
        espresso_image.visible = True
        espresso_button.visible = True

        americano_text.visible = True
        americano_image.visible = True
        americano_button.visible = True

        capucino_text.visible = True
        capucino_image.visible = True
        capucino_button.visible = True

        latte_text.visible = True
        latte_image.visible = True
        latte_button.visible = True

        mocha_text.visible = True
        mocha_image.visible = True
        mocha_button.visible = True

        ice_espresso_text.visible = True
        ice_espresso_image.visible = True
        ice_espresso_button.visible = True

        ice_americano_text.visible = True
        ice_americano_image.visible = True
        ice_americano_button.visible = True

        ice_capucino_text.visible = True
        ice_capucino_image.visible = True
        ice_capucino_button.visible = True

        ice_latte_text.visible = True
        ice_latte_image.visible = True
        ice_latte_button.visible = True

        ice_mocha_text.visible = True
        ice_mocha_image.visible = True
        ice_mocha_button.visible = True

        checkout_button.visible = True
        clean_order_button.visible = True

        sum_text.visible = False
        sum_of_order.visible = False
        currency_text.visible = False
        order_text.visible = False
        go_back_button.visible = False
        continue_to_payment_button.visible = False

        page.update()

    def continue_to_payment(event: str | None = None) -> None:
        sum_text.visible = True
        sum_of_order.visible = True
        currency_text.visible = True
        order_text.visible = True
        go_back_button.visible = False
        continue_to_payment_button.visible = False

        payment_text.visible = True
        finish_payment_button.visible = True  
        cancel_order_button.visible = True

        page.update()

    def new_order(event: str | None = None) -> None:
        my_coffee_shop_text.visible = True

        espresso_text.visible = True
        espresso_image.visible = True
        espresso_button.visible = True

        americano_text.visible = True
        americano_image.visible = True
        americano_button.visible = True

        capucino_text.visible = True
        capucino_image.visible = True
        capucino_button.visible = True

        latte_text.visible = True
        latte_image.visible = True
        latte_button.visible = True

        mocha_text.visible = True
        mocha_image.visible = True
        mocha_button.visible = True

        ice_espresso_text.visible = True
        ice_espresso_image.visible = True
        ice_espresso_button.visible = True

        ice_americano_text.visible = True
        ice_americano_image.visible = True
        ice_americano_button.visible = True

        ice_capucino_text.visible = True
        ice_capucino_image.visible = True
        ice_capucino_button.visible = True

        ice_latte_text.visible = True
        ice_latte_image.visible = True
        ice_latte_button.visible = True

        ice_mocha_text.visible = True
        ice_mocha_image.visible = True
        ice_mocha_button.visible = True

        checkout_button.visible = True
        clean_order_button.visible = True

        sum_text.visible = False
        sum_of_order.visible = False
        currency_text.visible = False
        order_text.visible = False
        go_back_button.visible = False
        continue_to_payment_button.visible = False

        payment_text.visible = False
        finish_payment_button.visible = False
        cancel_order_button.visible = False

        new_order_button.visible = False

        sum_of_order.value = 0
        
        order_text.value = f""

        page.update()

    def finish_payment(event: str | None = None) -> None:
        sum_text.visible = False
        sum_of_order.visible = False
        currency_text.visible = False

        payment_text.visible = False
        finish_payment_button.visible = False
        cancel_order_button.visible = False

        new_order_button.visible = True
        
        page.update()

    def add_coffee(event: str | None = None, price: int | None = None, drink: str | None = None) -> None:  
        sum_of_order.value = str(int(sum_of_order.value) + price)

        order_text.value += f"{drink}\n"

        page.update()

    def clean_order(event: str | None = None) -> None:
        sum_of_order.value = 0
        
        order_text.value = f""

    page.title = f"My Coffee Shop terminal"
    my_coffee_shop_text: flet.Text = flet.Text(f"My Coffee Shop terminal", size=100)

    espresso_text: flet.Text = flet.Text(f"espresso", size=20)
    espresso_image: flet.Image = flet.Image(src=f"images/ecspresso.jpeg", width=100, height=100)
    espresso_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=100, drink=f"espresso"))

    americano_text: flet.Text = flet.Text(f"americano", size=20)
    americano_image: flet.Image = flet.Image(src=f"images/americano.jpeg", width=100, height=100)
    americano_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=120, drink=f"americano"))

    capucino_text: flet.Text = flet.Text(f"capucino", size=20)
    capucino_image: flet.Image = flet.Image(src=f"images/capucino.jpeg", width=100, height=100)
    capucino_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=140, drink=f"capucino"))

    latte_text: flet.Text = flet.Text(f"latte", size=20)
    latte_image: flet.Image = flet.Image(src=f"images/latte.jpeg", width=100, height=100)
    latte_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=140, drink=f"latte"))

    mocha_text: flet.Text = flet.Text(f"mocha", size=20)
    mocha_image: flet.Image = flet.Image(src=f"images/mocha.jpeg", width=100, height=100)
    mocha_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=140, drink=f"mocha"))

    ice_espresso_text: flet.Text = flet.Text(f"ice espresso", size=20)
    ice_espresso_image: flet.Image = flet.Image(src=f"images/ice_espresso.jpeg", width=100, height=100)
    ice_espresso_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=110, drink=f"ice espresso"))

    ice_americano_text: flet.Text = flet.Text(f"ice americano", size=20)
    ice_americano_image: flet.Image = flet.Image(src=f"images/ice_americano.jpeg", width=100, height=100)
    ice_americano_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=130, drink=f"ice americano"))

    ice_capucino_text: flet.Text = flet.Text(f"ice capucino", size=20)
    ice_capucino_image: flet.Image = flet.Image(src=f"images/ice_capucino.jpeg", width=100, height=100)
    ice_capucino_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=150, drink=f"ice capucino"))

    ice_latte_text: flet.Text = flet.Text(f"ice latte", size=20)
    ice_latte_image: flet.Image = flet.Image(src=f"images/ice_latte.jpeg", width=100, height=100)
    ice_latte_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=150, drink=f"ice latte"))

    ice_mocha_text: flet.Text = flet.Text(f"ice mocha", size=20)
    ice_mocha_image: flet.Image = flet.Image(src=f"images/ice_mocha.jpeg", width=100, height=100)
    ice_mocha_button: flet.FilledButton = flet.FilledButton(f"add coffee", width=100, on_click=lambda event: add_coffee(price=150, drink=f"ice mocha"))

    checkout_button: flet.FilledButton = flet.FilledButton(f"check out your order", on_click=open_checkout)

    clean_order_button: flet.FilledButton = flet.FilledButton(f"clean order", on_click=clean_order)

    sum_of_order: flet.Text = flet.Text(value=f"0", size=100)
    sum_of_order.visible = False

    sum_text: flet.Text = flet.Text(f"You have to pay:", size=100)
    sum_text.visible = False

    currency_text: flet.Text = flet.Text(f"дин", size=100)
    currency_text.visible = False

    order_text: flet.Text = flet.Text(value=f"", size=30)
    order_text.visible = False

    go_back_button: flet.FilledButton = flet.FilledButton(f"go back", on_click=go_back)
    go_back_button.visible = False

    continue_to_payment_button: flet.FilledButton = flet.FilledButton(f"continue to payment", on_click=continue_to_payment)
    continue_to_payment_button.visible = False

    payment_text: flet.Text = flet.Text(f"send money to this phone number: +38165999000")
    payment_text.visible = False

    cancel_order_button: flet.FilledButton = flet.FilledButton(f"cancel order", on_click=new_order)
    cancel_order_button.visible = False

    finish_payment_button: flet.FilledButton = flet.FilledButton(f"finish payment", on_click=finish_payment)
    finish_payment_button.visible = False

    new_order_button: flet.FilledButton = flet.FilledButton(f"new order", on_click=new_order)
    new_order_button.visible = False

    page.add(flet.Row([sum_text, sum_of_order, currency_text]), flet.Row([order_text]), flet.Row([my_coffee_shop_text]), flet.Row([flet.Column([espresso_text, espresso_image, espresso_button]), flet.Column([americano_text, americano_image, americano_button]), flet.Column([capucino_text, capucino_image, capucino_button]), flet.Column([latte_text, latte_image, latte_button]), flet.Column([mocha_text, mocha_image, mocha_button]), flet.Column([ice_espresso_text, ice_espresso_image, ice_espresso_button]), flet.Column([ice_americano_text, ice_americano_image, ice_americano_button]), flet.Column([ice_capucino_text, ice_capucino_image, ice_capucino_button]), flet.Column([ice_latte_text, ice_latte_image, ice_latte_button]), flet.Column([ice_mocha_text, ice_mocha_image, ice_mocha_button])]), flet.Row([checkout_button, clean_order_button, go_back_button, continue_to_payment_button, payment_text]), flet.Row([cancel_order_button, finish_payment_button, new_order_button]))

    page.update()

if __name__ == f"__main__":
    flet.app(target=main, view=flet_core.types.WEB_BROWSER, assets_dir=f"assets")