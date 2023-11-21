import webbrowser
import os
def open_html_file_in_browser():
    html_file_path = os.path.abspath('C:/Users/user/Desktop/HealthCare_AI/code/front/front_result.html')
    webbrowser.open('file://' + html_file_path, new=2)

if __name__ == '__main__':
    print("hello22")
    open_html_file_in_browser()