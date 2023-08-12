from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class BuzzPage(PageObject):
    btn_comentario = 'bi-chat-text-fill'
    btn_curtir = 'heart-svg'
    btn_curtido = 'orangehrm-like-animation'
    btn_compartilhar = 'bi-share-fill'
    btn_postar_compartilhado = 'orangehrm-buzz-post-modal-actions'
    input_txt_add_comentario = "//input[@placeholder='Write your comment...']"
    input_txt_compartilhar_comentario = '.oxd-dialog-container-default--inner [placeholder="What\'s on your mind?"]'
    comentario_adicionado = 'orangehrm-post-comment-text'
    txt_comentario_adicionado = 'Comentario do grupo_6_teste'
    comentario_compartilhado = 'orangehrm-buzz-post-body-text'

    def __init__(self, driver):
        super(BuzzPage, self).__init__(driver=driver)

    def click_btn_adicionar_comentario(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_comentario).click()

    def click_btn_curtir(self):
        self.driver.find_element(By.ID, self.btn_curtir).click()

    def click_btn_compartilhar(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_compartilhar).click()

    def inserir_novo_comentario(self, text='Comentario do grupo_6_teste'):
        self.driver.find_element(By.XPATH, self.input_txt_add_comentario).click()
        self.driver.find_element(By.XPATH, self.input_txt_add_comentario).send_keys(text)
        self.driver.find_element(By.XPATH, self.input_txt_add_comentario).submit()

    def compartilhar_comentario(self, text='Comentario do grupo_6_teste'):
        self.driver.find_element(By.CSS_SELECTOR, self.input_txt_compartilhar_comentario).click()
        self.driver.find_element(By.CSS_SELECTOR, self.input_txt_compartilhar_comentario).send_keys(text)
        self.driver.find_element(By.CLASS_NAME, self.btn_postar_compartilhado).click()

    def validar_comentario_adicionado(self):
        comentario = self.driver.find_element(By.CLASS_NAME, self.comentario_adicionado).text
        return comentario == self.txt_comentario_adicionado

    def validar_postagem_curtida(self):
        return self.driver.find_element(By.CLASS_NAME, self.btn_curtido).is_displayed()

    def validar_comentario_compartilhado(self):
        comentario = self.driver.find_element(By.CLASS_NAME, self.comentario_compartilhado).text
        return comentario == self.txt_comentario_adicionado
