


#define IN_AUTO_SHUTDOWN_SWITCH  12
#define IN_USB_POWER_SENSE       11
#define IN_MAN_SHUTDOWN_BUTTON   10

#define OUT_PI_SHUTDOWN_TRIGGER  9
#define OUT_PI_RESTART_TRIGGER   8

#define MS_GENERAL_WAIT          500
#define MS_MAN_SHUTDOWN_WAIT     5000

boolean piRunning = true;
boolean shutdownIssued = false;
boolean startupIssued = false;
boolean previousPowerState = HIGH;

void setup() {
  pinMode(IN_AUTO_SHUTDOWN_SWITCH, INPUT_PULLUP);
  pinMode(IN_USB_POWER_SENSE, INPUT_PULLUP);

  pinMode(OUT_PI_SHUTDOWN_TRIGGER, OUTPUT);
  pinMode(OUT_PI_RESTART_TRIGGER, OUTPUT);

  digitalWrite(OUT_PI_SHUTDOWN_TRIGGER, HIGH);
  digitalWrite(OUT_PI_RESTART_TRIGGER, HIGH);
}

void loop() {
  delay(MS_GENERAL_WAIT);
  checkForManualShutdown();
  delay(MS_GENERAL_WAIT);
  checkForPowerUp();
  delay(MS_GENERAL_WAIT);
  checkForPowerDown();
}

void startupPi() {
  shutdownIssued = false;
  startupIssued = true;
  digitalWrite(OUT_PI_SHUTDOWN_TRIGGER, HIGH);
  digitalWrite(OUT_PI_RESTART_TRIGGER, LOW);
  delay(MS_GENERAL_WAIT);
  digitalWrite(OUT_PI_RESTART_TRIGGER, HIGH);
}

void shutdownPi() {
  shutdownIssued = true;
  startupIssued = false;
  digitalWrite(OUT_PI_SHUTDOWN_TRIGGER, LOW);
}

boolean checkForPowerUp() {
  int newPowerState = digitalRead(IN_USB_POWER_SENSE);
  if((previousPowerState == LOW) && (newPowerState == HIGH)) {
    if(shutdownIssued) {
      cancelShutdown();
    } else if(startupIssued) {
      //do nothing
    } else {
      startupPi();
    }
  }
  previousPowerState = newPowerState;
}

boolean checkForPowerDown() {
  int newPowerState = digitalRead(IN_USB_POWER_SENSE);
  if((previousPowerState == HIGH) && (newPowerState == LOW)) {
    if(shutdownIssued) {
      //do nothing
    } else if(startupIssued) {
      cancelShutdown();
    } else {
      shutdownPi();
    }
  }
  previousPowerState = newPowerState;
}

boolean checkForManualShutdown() {
  if(digitalRead(IN_MAN_SHUTDOWN_BUTTON) == LOW) {
    int time1 = millis();
    while(true) {
      if(digitalRead(IN_MAN_SHUTDOWN_BUTTON) == LOW) {
        int time2 = millis();
        if(time2 - time1 > MS_MAN_SHUTDOWN_WAIT) {
          digitalWrite(OUT_PI_SHUTDOWN_TRIGGER, LOW);
          return;
        }
      }
      return;
    }
  }
}

void cancelShutdown() {
  shutdownIssued = false;
  digitalWrite(OUT_PI_SHUTDOWN_TRIGGER, HIGH);
}
