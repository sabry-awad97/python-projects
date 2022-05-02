import os
import time

from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        UnexpectedAlertPresentException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class WhatsApp(object):
    def __init__(self, browser=None, headless_mode=False):
        self.BASE_URL = "https://web.whatsapp.com/"
        self.suffix_link = "https://wa.me/"

        self.headless_mode = headless_mode
        if not browser:
            s = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(
                service=s,
                options=self.chrome_options,
            )

        self.browser = browser

        self.wait = WebDriverWait(self.browser, 60)
        self.login()
        self.mobile = ""

    @property
    def chrome_options(self):
        chrome_options = Options()
        chrome_options.headless = self.headless_mode
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")
        chrome_options.add_experimental_option("detach", True)
        return chrome_options

    def login(self):
        self.browser.maximize_window()
        self.browser.get(self.BASE_URL)
        print("Site loaded successfully...")

    def logout(self):
        prefix = "//div[@id='side']/header/div[2]/div/span/div[3]"
        dots_button = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"{prefix}/div[@role='button']",
                )
            )
        )
        dots_button.click()

        logout_item = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"{prefix}/span/div[1]/ul/li[last()]/div[@role='button']",
                )
            )
        )
        logout_item.click()

    def get_phone_link(self, mobile) -> str:
        return f"{self.suffix_link}{mobile}"

    def catch_alert(self, seconds=3):
        try:
            WebDriverWait(self.browser, seconds).until(EC.alert_is_present())
            self.browser.switch_to_alert.accept()
            return True
        except Exception as e:
            # print(e)
            return False

    def find_user(self, mobile) -> None:
        try:
            self.mobile = mobile
            link = self.get_phone_link(mobile)
            self.browser.get(link)
            action_button = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="action-button"]'))
            )
            action_button.click()
            time.sleep(2)
            go_to_web = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="fallback_block"]/div/div/a')
                )
            )
            go_to_web.click()
            time.sleep(1)
        except UnexpectedAlertPresentException as bug:
            # print(bug)
            time.sleep(1)
            self.find_user(mobile)

    def find_by_username(self, username):
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')
                )
            )
            search_box.clear()
            search_box.send_keys(username)
            search_box.send_keys(Keys.ENTER)
        except Exception as bug:
            error = f"Exception raised while finding user {username}\n{bug}"
            # print(error)

    def username_exists(self, username):
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')
                )
            )
            search_box.clear()
            search_box.send_keys(username)
            search_box.send_keys(Keys.ENTER)
            opened_chat = self.browser.find_element(
                By.XPATH,
                "/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[1]/div/span"
            )
            title = opened_chat.get_attribute("title")
            if title.upper() == username.upper():
                return True
            else:
                return False
        except Exception as bug:
            error = f"Exception raised while finding user {username}\n{bug}"
            # print(error)

    def send_message(self, message):
        try:
            inp_xpath = (
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
            )
            input_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, inp_xpath))
            )
            input_box.send_keys(message + Keys.ENTER)
            print(f"Message sent successfully to {self.mobile}")
        except (NoSuchElementException, Exception) as bug:
            # print(bug)
            print(f"Failed to send a message to {self.mobile}")

        finally:
            pass

    def find_attachment(self):
        clip_button = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..')
            )
        )
        clip_button.click()

    def send_attachment(self):
        # Waiting for the pending clock icon to disappear
        self.wait.until_not(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]//*[@data-icon="msg-time"]')
            )
        )

        send_button = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span',
                )
            )
        )
        send_button.click()

    def send_picture(self, picture):
        try:
            filename = os.path.realpath(picture)
            self.find_attachment()
            img_button = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input',
                    )
                )
            )

            img_button.send_keys(filename)
            self.send_attachment()
            print(f"Picture {picture} has been successfully sent to {self.mobile}")
            with open('success.log', 'a') as fd:
                fd.write(f'{picture} => {self.mobile}\n')
        except (NoSuchElementException, Exception) as bug:
            with open('failure.log', 'a') as fd:
                fd.write(f'{picture} => {self.mobile}\n')
            # print(bug)
            print(f"Failed to send a picture {picture} to {self.mobile}")


        finally:
            pass

    def send_video(self, video):
        try:
            filename = os.path.realpath(video)
            self.find_attachment()
            video_button = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input',
                    )
                )
            )
            video_button.send_keys(filename)
            self.send_attachment()
            print(f"Video has been successfully sent to {self.mobile}")
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print(f"Failed to send a video to {self.mobile}")
        finally:
            pass

    def send_file(self, file):
        try:
            filename = os.path.realpath(file)
            self.find_attachment()
            document_button = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="main"]/footer//*[@data-icon="attach-document"]/../input'
                    )
                )
            )
            document_button.send_keys(filename)
            self.send_attachment()

        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print(f"Failed to send a PDF to {self.mobile}")
        finally:
            pass
