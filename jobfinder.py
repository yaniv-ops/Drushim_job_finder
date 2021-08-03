from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class JobFinder:

    def __init__(self, chrome_path):
        self.chrome_driver = chrome_path


    def connect_to_linkedin(self):
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver)
        return self.driver



    def jobs_list(self):

        self.list_of_jobs = self.driver.find_elements_by_id("ember242")
        print(self.list_of_jobs)

    def scroll_page(self):
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)
                expand_jobs = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div[1]/div[5]/button')
                expand_jobs.click()
            except NoSuchElementException:
                self.driver.find_element_by_css_selector('.INDlangdirRTL').send_keys(Keys.CONTROL + Keys.HOME)
                break

    def scroll_to_next_add(self, element):
        element.click()
        send_cv_file = self.driver.find_element_by_xpath('//*[@id="submitApply"]/span')
        send_cv_file.click()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        sleep(5)

def send_cv_file(job_object):

    print(f"{job_object.text} ...Sending cv file.")
    job_object.click()


    #sleep(5)
    #JobFinder.scroll_to_next_add(job_object)
    #sleep(5)










