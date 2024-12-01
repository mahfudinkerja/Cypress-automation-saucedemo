import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.github.javafaker.Faker as Faker
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

s(Faker)

Faker faker = new Faker()

String firstNameOrder = faker.name().firstName()

String lastNameOrder = faker.name().lastName()

String postalCodeOrder = faker.address().zipCode()

WebUI.callTestCase(findTestCase('sauceDemo/TC Login Success'), [('Login_Username') : 'standard_user', ('Login_Password') : 'secret_sauce'], 
    FailureHandling.STOP_ON_FAILURE)

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Add to cart'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Add to cart_1'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Add to cart_1_2'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Add to cart_1_2_3'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Add to cart_1_2_3_4'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Add to cart_1_2_3_4_5'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/a_6'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Checkout'))

WebUI.setText(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/input_Checkout Your Information_firstName'), 
    firstNameOrder)

WebUI.setText(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/input_Checkout Your Information_lastName'), 
    lastNameOrder)

WebUI.setText(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/input_Checkout Your Information_postalCode'), 
    postalCodeOrder)

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/input_Cancel_continue'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Finish'))

WebUI.click(findTestObject('Object Repository/Page_Swag Labs/Checkout_Orders/button_Back Home'))

WebUI.closeBrowser()