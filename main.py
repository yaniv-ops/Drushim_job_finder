from jobfinder import JobFinder
from time import sleep
from jobfinder import send_cv_file


url = "https://www.drushim.co.il/jobs/search/Python%20Developer/?ssaen=1"
chrome_path = '/home/tamar-alter/Desktop/web_developer/chromedriver'


my_job = JobFinder(chrome_path)
my_new_job = my_job.connect_to_linkedin()
my_new_job.get(url)

sleep(3)

close_window = my_new_job.find_element_by_xpath('//*[@id="app"]/div[8]/div/div/div[1]/button')
close_window.click()
enter = my_new_job.find_element_by_css_selector('div[id*="user-menu-wrapper"]')

my_new_job.maximize_window()
enter.click()


e_mail = my_new_job.find_element_by_id('email-login-field')
e_mail.send_keys("yaniv.ayalon@gmail.com")
password = my_new_job.find_element_by_id('password-login-field')
password.send_keys("Yours e-mail password")
enter_account = my_new_job.find_element_by_css_selector('#submit-login-btn')
enter_account.click()
my_job.scroll_page()
jobs_list = my_new_job.find_elements_by_xpath('//*[@id="cv-send-btn"]/span/button')
for item in jobs_list:
    print(item.text)
    my_job.scroll_to_next_add(item)
        #send_cv_file = my_new_job.find_element_by_xpath('//*[@id="submitApply"]/span')
        #send_cv_file.click()
    sleep(5)

#each_job_apply_button = //*[@id="submitApply"]/span








