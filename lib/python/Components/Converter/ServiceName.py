# -*- coding: utf-8 -*-
from Components.Converter.Converter import Converter
from enigma import iServiceInformation, iPlayableService, iPlayableServicePtr
from Components.Element import cached

class ServiceName(Converter, object):
	NAME = 0
	PROVIDER = 1
	REFERENCE = 2
	SID = 3

	def __init__(self, type):
		Converter.__init__(self, type)
		if type == "Provider":
			self.type = self.PROVIDER
		elif type == "Reference":
			self.type = self.REFERENCE
		elif type == "Sid":
			self.type = self.SID
		else:
			self.type = self.NAME

	@cached
	def getText(self):
		service = self.source.service
		if isinstance(service, iPlayableServicePtr):
			info = service and service.info()
			ref = None
		else: # reference
			info = service and self.source.info
			ref = service
		if info is None:
			return ""
		if self.type == self.NAME:
			name = ref and info.getName(ref)
			if name is None:
				name = info.getName()
			return name.replace('\xc2\x86', '').replace('\xc2\x87', '')
		elif self.type == self.PROVIDER:
			return info.getInfoString(iServiceInformation.sProvider)
		elif self.type == self.REFERENCE:
			if ref is None:
				return info.getInfoString(iServiceInformation.sServiceref)
			else:
				return ref.toString()
		elif self.type == self.SID:
			if ref is None:
				tmpref = info.getInfoString(iServiceInformation.sServiceref)
			else:
				tmpref = ref.toString()

			if tmpref:
				refsplit = tmpref.split(':')
				if len(refsplit) >= 3: 
					return refsplit[3]
				else:
					return tmpref
			else:
				return 'N/A'

	text = property(getText)

	def changed(self, what):
		if what[0] != self.CHANGED_SPECIFIC or what[1] in (iPlayableService.evStart,):
			Converter.changed(self, what)
