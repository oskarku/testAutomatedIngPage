"""This is test page  individual page accont banking https://www.ing.pl/indywidualni/konta-osobiste
This code include  methode to test pages like as
chckSubmenu, breadcrumb_item
"""
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class accountBankingTestPage():

    def __init__(self, driver):
        self.driver = driver

    def __init__(self, driver, listCorrectStringElementNameSubMenu, correctTitleString, listDictCardElement):
        self.driver = driver

    def testAllPages(self):
        pass

    def checkSubmenuCountElement(self,listOfStringBreadcrumbsInnerElement):
        isCheckFlagSubmenuCountElement=False
        try:
            elementsSubMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.ID, "breadcrumb_item"))
            )
            if len(listOfStringBreadcrumbsInnerElement)==len(elementsSubMenu):
                isCheckFlagSubmenuCountElement=True

        except Exception as e:
            print("Exception during while an element :", str(e))

        return isCheckFlagSubmenuCountElement


    def validNameElementInSubmenu(self,listOfStringBreadcrumbsInnerElement):
        isValidNameElementInSubmenu=False
        try:
            elementsSubMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.ID, "breadcrumb_item"))
            )
            for x in len(elementsSubMenu):
                if elementsSubMenu[x]==listOfStringBreadcrumbsInnerElement[x]:
                    isValidNameElementInSubmenu=True
                else:
                    isValidNameElementInSubmenu=False
        except Exception as e:
            print("Exception during while an element ", str(e))

        return isValidNameElementInSubmenu

    def checkTitlePage(self, validTitle):
        isCheckTitlePage=False
        try:
            elementTitlePage = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "breadcrumb_item"))
            )
            if validTitle==elementTitlePage:
                isCheckTitlePage=True
        except Exception as e:
            print("Exception during while an element :", str(e))
        return isCheckTitlePage

    def readeElementInMenu(self):
        try:
            elementTitlePage = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "breadcrumb_item"))
            )
        except Exception as e:
            print("Exception during while an element :", str(e))

        return {}


    def getTestRaportMenu(self,listDictWithInformationdDistroTileBodyElement):
        return{}


    def getRaportTestGreySection(self, listDictElement):
        return{}

    def getRaportTestSectionWithImage(selfs,listelementWithImage):
        return {}

    def chceckSectionTitleText(self,stringValidTitle):
        return False

    def getRaportTestSectionText(self, listOfDictTextFormula):
        return {}

    def sectionInfo(self, listOfDictElement):
        return {}

#################################################################################







