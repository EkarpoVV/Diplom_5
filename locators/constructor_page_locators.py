from selenium.webdriver.common.by import By

class ConstructorLocators: 

    INGREDIENT_BUTTON = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS_MODAL = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_DETAILS_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close__TnseK")
    INGREDIENTS_COUNTER = (By.CSS_SELECTOR, ".text_type_digits-medium")
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    CREATE_BURGER_PAGE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    DRUG_BUN_HERE_TOP = (By.XPATH, '//span[text()="Перетяните булочку сюда (верх)"]')
    YOUR_ORDER_HAS_BEEN_PREPARED = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    CLOSE_ORDER_ID_POPUP = (By.CSS_SELECTOR, '.Modal_modal__close__TnseK')
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    ORDER_NUMBER_IN_POPUP = (By.XPATH,'//h2[contains(@class, "Modal_modal__title") and contains(@class, "digits")]')
    MODAL_FF = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay__']")
    MODAL_CLOSE_FOR_FF = (By.XPATH, '//button[@class="close-modal-button"]')
    HEADER_ACCOUNT_PAGE = (By.XPATH, '//a[contains(@class, "AppHeader_header__link")]')
