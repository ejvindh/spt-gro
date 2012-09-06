#!/usr/bin/env python2.6
# coding: utf-8

import os
import gui
import dictionary

# Angiv stierne til ordbogsfilerne nedenfor. 
# Udkommenter sprog som du ikke ønsker at bruge
#EH
#-- Doubflag:
#  0 => envejs, uden reverse (storenda, stordaen, ret, frem, dansk, syn)
#  1 => envejs, med reverse
#  2 => tovejs, uden reverse (no, it, fag)
#  3 => tovejs, med reverse (en, ty, fr, sv, es)

dictionaries = {
#	'en': {
#		'name': 'Engelsk',
#		'gddfile': 'data/EngelskOrdbog.gdd',
#		'datfile': 'data/EngelskOrdbog.dat',
#		'doubflag': 3,
#	},
#	'de': {
#		'name': 'Tysk',
#		'gddfile': 'data/TyskOrdbog.gdd',
#		'datfile': 'data/TyskOrdbog.dat',
#		'doubflag': 3,
#	},
#	'fr': {
#		'name': 'Fransk',
#		'gddfile': 'data/FranskOrdbog.gdd',
#		'datfile': 'data/FranskOrdbog.dat',
#		'doubflag': 3,
#	},
#	'es': {
#		'name': 'Spansk',
#		'gddfile': 'data/SpanskOrdbog.gdd',
#		'datfile': 'data/SpanskOrdbog.dat',
#		'doubflag': 3,
#	},
#	'it':  {
#		'name': 'Italiensk',
#		'gddfile': 'data/ItalienskDownload.gdd',
#		'datfile': 'data/ItalienskDownload.dat',
#		'doubflag': 2,
#	},
#	'se':  {
#		'name': 'Svensk',
#		'gddfile': 'data/SvenskOrdbog.gdd',
#		'datfile': 'data/SvenskOrdbog.dat',
#		'doubflag': 3,
#	},
#	'no':  {
#		'name': 'Norsk',
#		'gddfile': 'data/NorskDownload.gdd',
#		'datfile': 'data/NorskDownload.dat',
#		'doubflag': 2,
#	},
#	'enfag': {
#		'name': 'Engelsk (Fag/Teknik)',
#		'gddfile': 'data/FagordbogEngelskDownload.gdd',
#		'datfile': 'data/FagordbogEngelskDownload.dat',
#		'doubflag': 2,
#	},
#	'daen': {
#		'name': 'Stor Dansk-Engelsk',
#		'gddfile': 'data/StorDanskEngelskDownload.gdd',
#		'datfile': 'data/StorDanskEngelskDownload.dat',
#		'doubflag': 0,
#	},
#	'enda': {
#		'name': 'Stor Engelsk-Dansk',
#		'gddfile': 'data/StorEngelskDanskDownload.gdd',
#		'datfile': 'data/StorEngelskDanskDownload.dat',
#		'doubflag': 0,
#	},
#	'ret': {
#		'name': 'Retskrivning',
#		'gddfile': 'data/RetskrivningsordbogDownload.gdd',
#		'datfile': 'data/RetskrivningsordbogDownload.dat',
#		'doubflag': 0,
#	},
#	'frem': {
#		'name': 'Fremmedord',
#		'gddfile': 'data/DanskFremmedordbogDownload.gdd',
#		'datfile': 'data/DanskFremmedordbogDownload.dat',
#		'doubflag': 0,
#	},
#	'da': {
#		'name': 'Dansk',
#		'gddfile': 'data/DanskDownload.gdd',
#		'datfile': 'data/DanskDownload.dat',
#		'doubflag': 0,
#	},
#	'syn': {
#		'name': 'Synonymer',
#		'gddfile': 'data/SynonymordbogDownload.gdd',
#		'datfile': 'data/SynonymordbogDownload.dat',
#		'doubflag': 0,
#	},
}

def main():

	# check om sprogene er tilgængelige
	filenotfound = False
	for d in dictionaries.keys():
		lang = dictionaries[d];
		if not (os.path.exists(lang['gddfile']) and os.path.exists(lang['datfile'])):
			print 'Ordbogsfiler for %s kan ikke findes i mappen %s'%(lang['name'],os.path.dirname(os.path.abspath(lang['gddfile'])))
			filenotfound = True
	if filenotfound:
		return
	dic = dictionary.Dictionary(dictionaries)
	dictionaryGUI = gui.DictionaryGUI(dic)
	dictionaryGUI.run()


if __name__ == '__main__':
	main()

