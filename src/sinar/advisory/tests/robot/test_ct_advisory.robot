# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.advisory -t test_advisory.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.advisory.testing.SINAR_ADVISORY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/sinar/advisory/tests/robot/test_advisory.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Advisory
  Given a logged-in site administrator
    and an add Advisory form
   When I type 'My Advisory' into the title field
    and I submit the form
   Then a Advisory with the title 'My Advisory' has been created

Scenario: As a site administrator I can view a Advisory
  Given a logged-in site administrator
    and a Advisory 'My Advisory'
   When I go to the Advisory view
   Then I can see the Advisory title 'My Advisory'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Advisory form
  Go To  ${PLONE_URL}/++add++Advisory

a Advisory 'My Advisory'
  Create content  type=Advisory  id=my-advisory  title=My Advisory

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Advisory view
  Go To  ${PLONE_URL}/my-advisory
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Advisory with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Advisory title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
