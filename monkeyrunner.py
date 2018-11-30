# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
device.installPackage('C:\Users\Consultants\AndroidStudioProjects\TestCodelab\Week6Daily4\app\build\outputs\apk\debug\app-debug.apk')

# sets a variable with the package's internal name
package = 'com.example.consultants.week6daily4'

# sets a variable with the name of an Activity in the package
activity = 'com.example.consultants.week6daily4.RobolectricActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)

MonkeyRunner.sleep(5)
# Presses the Menu button
device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
result = device.takeSnapshot()

# Writes the screenshot to a file
result.writeToFile('C:\Users\Consultants\AndroidStudioProjects\TestCodelab\shot1.png','png')