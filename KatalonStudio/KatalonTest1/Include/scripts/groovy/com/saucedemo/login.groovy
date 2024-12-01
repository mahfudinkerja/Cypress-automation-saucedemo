import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.model.FailureHandling
import org.openqa.selenium.By

import cucumber.api.java.en.And
import cucumber.api.java.en.Given
import cucumber.api.java.en.Then
import cucumber.api.java.en.When
import internal.GlobalVariable



class login {
	@Given("The saucedemo URL")
	def theSauceDemoUrl() {
		WebUI.openBrowser(GlobalVariable.urlSauceDemo)
	}

	@When("I input (.*) and (.*) in the fields")
	def inputCredsLogin(String username, password) {
		WebUI.waitForElementPresent(findTestObject('Page_Swag Labs/login_screen/saucedemo_username'), 0)

		WebUI.sendKeys(findTestObject('Page_Swag Labs/login_screen/saucedemo_username'), username)
		WebUI.sendKeys(findTestObject('Page_Swag Labs/login_screen/saucedemo_password'), password)
	}

	@And("I click on the signin button")
	def clickOnSigninButton() {
		WebUI.click(findTestObject('Page_Swag Labs/login_screen/saucedemo_login_btn'))
	}

	@Then("Burger menu button will be displayed")
	def burgerMenuDisplayed () {
		WebUI.waitForElementVisible(findTestObject('Page_Swag Labs/login_screen/saucedemo_burger_btn'), 0)
	}
}




















