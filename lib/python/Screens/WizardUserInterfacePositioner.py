from Screens.Wizard import wizardManager, WizardSummary
from Screens.WizardLanguage import WizardLanguage
from Screens.Rc import Rc
from Screens.MessageBox import MessageBox
from Components.Pixmap import Pixmap, MovingPixmap, MultiPixmap
from Components.Sources.Boolean import Boolean
from Tools.Directories import resolveFilename, SCOPE_SKIN
from Components.config import config, configfile
from enigma import getDesktop, getBoxType
from Components.Sources.StaticText import StaticText

class WizardUserInterfacePositioner(WizardLanguage, Rc):
	if (getDesktop(0).size().width() == 1280):
		skin = """
			<screen position="center,center" size="1280,720" backgroundColor="#000000" title="OSD Adjustment" >

				<widget source="title" render="Label" position="200,130" zPosition="1" size="880,60" font="Regular;58" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget name="config" position="150,250" zPosition="1" size="980,150" font="Regular;20" halign="center" valign="center" transparent="1" />
				<widget source="info1" render="Label" position="200,450" zPosition="1" size="880,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="info2" render="Label" position="200,480" zPosition="1" size="880,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="info3" render="Label" position="200,510" zPosition="1" size="880,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				
				<eLabel backgroundColor="red" position="0,0" size="1280,1" zPosition="0" />
				<eLabel backgroundColor="red" position="0,719" size="1280,1" zPosition="0" />
				<eLabel backgroundColor="red" position="0,0" size="1,720" zPosition="0" />
				<eLabel backgroundColor="red" position="1279,0" size="1,720" zPosition="0" />
				<eLabel backgroundColor="green" position="25,25" size="1230,1" zPosition="0" />
				<eLabel backgroundColor="green" position="25,694" size="1230,1" zPosition="0" />
				<eLabel backgroundColor="green" position="25,25" size="1,670" zPosition="0" />
				<eLabel backgroundColor="green" position="1254,25" size="1,670" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,50" size="1180,1" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,669" size="1180,1" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,50" size="1,620" zPosition="0" />
				<eLabel backgroundColor="yellow" position="1229,50" size="1,620" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,75" size="1130,1" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,644" size="1130,1" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,75" size="1,570" zPosition="0" />
				<eLabel backgroundColor="blue" position="1204,75" size="1,570" zPosition="0" />

			</screen>"""

	elif (getDesktop(0).size().width() == 1024):
		skin = """
			<screen position="center,center" size="1024,576" backgroundColor="#000000" title="OSD Adjustment" >

				<widget source="title" render="Label" position="200,100" zPosition="1" size="624,40" font="Regular;38" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="config" render="Label" position="100,180" zPosition="1" size="824,50" font="Regular;24" halign="center" valign="center" transparent="1" />
				<widget source="info1" render="Label" position="200,450" zPosition="1" size="624,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="info2" render="Label" position="200,480" zPosition="1" size="624,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="info3" render="Label" position="200,510" zPosition="1" size="624,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				
				<eLabel backgroundColor="red" position="0,0" size="1024,1" zPosition="0" />
				<eLabel backgroundColor="red" position="0,575" size="1024,1" zPosition="0" />
				<eLabel backgroundColor="red" position="0,0" size="1,576" zPosition="0" />
				<eLabel backgroundColor="red" position="1023,0" size="1,576" zPosition="0" />
				<eLabel backgroundColor="green" position="25,25" size="974,1" zPosition="0" />
				<eLabel backgroundColor="green" position="25,551" size="974,1" zPosition="0" />
				<eLabel backgroundColor="green" position="25,25" size="1,526" zPosition="0" />
				<eLabel backgroundColor="green" position="999,25" size="1,526" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,50" size="924,1" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,526" size="924,1" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,50" size="1,476" zPosition="0" />
				<eLabel backgroundColor="yellow" position="974,50" size="1,476" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,75" size="874,1" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,501" size="874,1" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,75" size="1,426" zPosition="0" />
				<eLabel backgroundColor="blue" position="949,75" size="1,426" zPosition="0" />

			</screen>"""

	else:
		skin = """
			<screen position="center,center" size="720,576" backgroundColor="#000000" title="OSD Adjustment" >

				<widget source="title" render="Label" position="75,100" zPosition="1" size="570,40" font="Regular;38" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="config" render="Label" position="75,180" zPosition="1" size="570,50" font="Regular;21" halign="center" valign="center" transparent="1" />
				<widget source="info1" render="Label" position="75,450" zPosition="1" size="570,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="info2" render="Label" position="75,480" zPosition="1" size="570,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				<widget source="info3" render="Label" position="75,510" zPosition="1" size="570,40" font="Regular;21" halign="center" valign="center" foregroundColor="yellow" backgroundColor="#1f771f" transparent="1" />
				
				<eLabel backgroundColor="red" position="0,0" size="720,1" zPosition="0" />
				<eLabel backgroundColor="red" position="0,575" size="720,1" zPosition="0" />
				<eLabel backgroundColor="red" position="0,0" size="1,576" zPosition="0" />
				<eLabel backgroundColor="red" position="719,0" size="1,576" zPosition="0" />
				<eLabel backgroundColor="green" position="25,25" size="670,1" zPosition="0" />
				<eLabel backgroundColor="green" position="25,551" size="670,1" zPosition="0" />
				<eLabel backgroundColor="green" position="25,25" size="1,526" zPosition="0" />
				<eLabel backgroundColor="green" position="694,25" size="1,526" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,50" size="620,1" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,526" size="620,1" zPosition="0" />
				<eLabel backgroundColor="yellow" position="50,50" size="1,476" zPosition="0" />
				<eLabel backgroundColor="yellow" position="670,50" size="1,476" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,75" size="570,1" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,501" size="570,1" zPosition="0" />
				<eLabel backgroundColor="blue" position="75,75" size="1,426" zPosition="0" />
				<eLabel backgroundColor="blue" position="645,75" size="1,426" zPosition="0" />

			</screen>"""
	def __init__(self, session, interface = None):
		self.xmlfile = resolveFilename(SCOPE_SKIN, "userinterfacepositionerwizard.xml")
		WizardLanguage.__init__(self, session, showSteps = False, showStepSlider = False)
		Rc.__init__(self)
		self.session = session
		self["wizard"] = Pixmap()
		
		self["title"] = StaticText(_("OSD Adjustment"))
		self["info1"] = StaticText(_("Use arrows Up/Down to select"))
		self["info2"] = StaticText(_("Use arrows Left/Right to adjust"))
		self["info3"] = StaticText(_("Press OK for save"))

		self.NextStep = None
		self.Text = None

	def exitWizardQuestion(self, ret = False):
		if (ret):
			self.markDone()
			self.close()

	def markDone(self):
		pass

	def back(self):
		WizardLanguage.back(self)
