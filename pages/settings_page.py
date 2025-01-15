from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage
class Settings(BasePage):


  PROFILE_SETTING = "a[href='/profile-edit']"

  def click_on_profile_setting(self):
      self.wait_and_click(*self.PROFILE_SETTING)