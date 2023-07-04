# iss-tracker
ISS Tracker using Python
When ISS is flying around our location, alert the user by sending mail.

**Tech stack and Tools** - Python, ISS tracking API

**1. Setting our location**
  - Set latitude and longitude of the current location

**2. Finding ISS**
  - Finding ISS's current position through this API, http://api.open-notify.org/iss-now.json
  - If the latitude and longitude are nearer to our location, send mail

    
