from enigma import eConsoleAppContainer
from Components.Console import Console
from Components.About import about
from Components.DreamInfoHandler import DreamInfoHandler
from Components.Language import language
from Components.Sources.List import List
from Components.Ipkg import IpkgComponent
from Components.Network import iNetwork
from Tools.Directories import pathExists, fileExists, resolveFilename, SCOPE_METADIR

from time import time

class SoftwareTools(DreamInfoHandler):
	lastDownloadDate = None
	NetworkConnectionAvailable = None
	list_updating = False
	available_updates = 0
	available_updatelist  = []
	available_packetlist  = []
	installed_packetlist = {}

	
	def __init__(self):
		aboutInfo = about.getImageVersionString()
		if aboutInfo.startswith("dev-"):
			self.ImageVersion = 'Experimental'
		else:
			self.ImageVersion = 'Stable'
		self.language = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
		DreamInfoHandler.__init__(self, self.statusCallback, blocking = False, neededTag = 'ALL_TAGS', neededFlag = self.ImageVersion, language = self.language)
		self.directory = resolveFilename(SCOPE_METADIR)
		self.list = List([])
		self.NotifierCallback = None
		self.Console = Console()
		self.UpdateConsole = Console()
		self.cmdList = []
		self.unwanted_extensions = ('-dbg', '-dev', '-doc')
		self.ipkg = IpkgComponent()
		self.ipkg.addCallback(self.ipkgCallback)		

	def statusCallback(self, status, progress):
		pass		

	def startSoftwareTools(self, callback = None):
		if callback is not None:
			self.NotifierCallback = callback
		iNetwork.checkNetworkState(self.checkNetworkCB)
		
	def checkNetworkCB(self,data):
		if data is not None:
			if data <= 2:
				SoftwareTools.NetworkConnectionAvailable = True
				self.getUpdates()
			else:
				SoftwareTools.NetworkConnectionAvailable = False
				self.getUpdates()

	def getUpdates(self, callback = None):
		if SoftwareTools.NetworkConnectionAvailable == True:
			SoftwareTools.lastDownloadDate = time()
			if SoftwareTools.list_updating is False and callback is None:
				SoftwareTools.list_updating = True
				self.ipkg.startCmd(IpkgComponent.CMD_UPDATE)
			elif SoftwareTools.list_updating is False and callback is not None:
				SoftwareTools.list_updating = True
				self.NotifierCallback = callback
				self.ipkg.startCmd(IpkgComponent.CMD_UPDATE)
			elif SoftwareTools.list_updating is True and callback is not None:
				#update info collecting already in progress
				self.NotifierCallback = callback
		else:
			SoftwareTools.list_updating = False
			if callback is not None:
				callback(False)
			elif self.NotifierCallback is not None:
				self.NotifierCallback(False)

	def ipkgCallback(self, event, param):
		if event == IpkgComponent.EVENT_ERROR:
			SoftwareTools.list_updating = False
		elif event == IpkgComponent.EVENT_DONE:
			if SoftwareTools.list_updating:
				self.startIpkgListAvailable()
		pass

	def startIpkgListAvailable(self, callback = None):
		if callback is not None:
			SoftwareTools.list_updating = True
		if SoftwareTools.list_updating:
			if not self.UpdateConsole:
				self.UpdateConsole = Console()
			cmd = "ipkg list"
			self.UpdateConsole.ePopen(cmd, self.IpkgListAvailableCB, callback)

	def IpkgListAvailableCB(self, result, retval, extra_args = None):
		(callback) = extra_args
		if len(result):
			if SoftwareTools.list_updating:
				SoftwareTools.available_packetlist = []
				for x in result.splitlines():
					split = x.split(' - ')
					name = split[0].strip()
					if not any(name.endswith(x) for x in self.unwanted_extensions):
						SoftwareTools.available_packetlist.append([name, split[1].strip(), split[2].strip()])
				if callback is None:
					self.startInstallMetaPackage()
				else:
					if self.UpdateConsole:
						if len(self.UpdateConsole.appContainers) == 0:
								callback(True)
		else:
			SoftwareTools.list_updating = False
			if self.UpdateConsole:
				if len(self.UpdateConsole.appContainers) == 0:
					if callback is not None:
						callback(False)

	def startInstallMetaPackage(self, callback = None):
		if callback is not None:
			SoftwareTools.list_updating = True
		if SoftwareTools.list_updating:
			if not self.UpdateConsole:
				self.UpdateConsole = Console()
			cmd = "ipkg install enigma2-meta enigma2-plugins-meta enigma2-skins-meta"
			self.UpdateConsole.ePopen(cmd, self.InstallMetaPackageCB, callback)

	def InstallMetaPackageCB(self, result, retval, extra_args = None):
		(callback) = extra_args
		if len(result):
			self.fillPackagesIndexList()
			if callback is None:
				self.startIpkgListInstalled()
			else:
				if self.UpdateConsole:
					if len(self.UpdateConsole.appContainers) == 0:
							callback(True)
		else:
			SoftwareTools.list_updating = False
			if self.UpdateConsole:
				if len(self.UpdateConsole.appContainers) == 0:
					if callback is not None:
						callback(False)

	def startIpkgListInstalled(self, callback = None):
		if callback is not None:
			SoftwareTools.list_updating = True
		if SoftwareTools.list_updating:
			if not self.UpdateConsole:
				self.UpdateConsole = Console()
			cmd = "ipkg list_installed"
			self.UpdateConsole.ePopen(cmd, self.IpkgListInstalledCB, callback)

	def IpkgListInstalledCB(self, result, retval, extra_args = None):
		(callback) = extra_args
		if len(result):
			SoftwareTools.installed_packetlist = {}
			for x in result.splitlines():
				split = x.split(' - ')
				name = split[0].strip()
				if not any(name.endswith(x) for x in self.unwanted_extensions):
					SoftwareTools.installed_packetlist[name] = split[1].strip()
			if callback is None:
				self.countUpdates()
			else:
				if self.UpdateConsole:
					if len(self.UpdateConsole.appContainers) == 0:
							callback(True)
		else:
			SoftwareTools.list_updating = False
			if self.UpdateConsole:
				if len(self.UpdateConsole.appContainers) == 0:
					if callback is not None:
						callback(False)

	def countUpdates(self, callback = None):
		SoftwareTools.available_updates = 0
		SoftwareTools.available_updatelist  = []
		for package in self.packagesIndexlist[:]:
			attributes = package[0]["attributes"]
			packagename = attributes["packagename"]
			for x in SoftwareTools.available_packetlist:
				if x[0] == packagename:
					if SoftwareTools.installed_packetlist.has_key(packagename):
						if SoftwareTools.installed_packetlist[packagename] != x[1]:
							SoftwareTools.available_updates +=1
							SoftwareTools.available_updatelist.append([packagename])

		SoftwareTools.list_updating = False
		if self.UpdateConsole:
			if len(self.UpdateConsole.appContainers) == 0:
				if callback is not None:
					callback(True)
					callback = None
				elif self.NotifierCallback is not None:
					self.NotifierCallback(True)
					self.NotifierCallback = None

	def startIpkgUpdate(self, callback = None):
		if not self.Console:
			self.Console = Console()
		cmd = "ipkg update"
		self.Console.ePopen(cmd, self.IpkgUpdateCB, callback)

	def IpkgUpdateCB(self, result, retval, extra_args = None):
		(callback) = extra_args
		if len(result):
			if self.Console:
				if len(self.Console.appContainers) == 0:
					if callback is not None:
						callback(True)
						callback = None

	def cleanupSoftwareTools(self):
		if self.NotifierCallback is not None:
			self.NotifierCallback = None
		self.ipkg.stop()
		if self.Console is not None:
			if len(self.Console.appContainers):
				for name in self.Console.appContainers.keys():
					self.Console.kill(name)
		if self.UpdateConsole is not None:
			if len(self.UpdateConsole.appContainers):
				for name in self.UpdateConsole.appContainers.keys():
					self.UpdateConsole.kill(name)

iSoftwareTools = SoftwareTools()