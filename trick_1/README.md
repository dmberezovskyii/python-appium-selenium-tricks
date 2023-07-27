# python-appium-tricks

## Trick 1 - connection check
** The first trick is to check an android device connection, 
there are cases when we need to work with the connection, 
appium allows to toggle the connection using the adb shell or through the device UI,
but it's just a toggle to get the connection to appear,
it takes some time, which is affected by many factors and we do not know when this connection will appear, accordingly we need to set long delays, but this does not guarantee the stable work of a test script

### in order for our test scripts to work stably can be used

```
   self.driver.execute_script("mobile: deviceInfo")
```

#### more details about execute_script [here](https://github.com/clarabez/appium-1/blob/master/docs/en/commands/mobile-command.md)