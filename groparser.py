# coding: utf-8
from array import array
import re
#from copy import deepcopy

KEY = [
	0xBA, 0x59, 0xD9, 0xC2, 0x32, 0xB7, 0x21, 0x78, 0xB5, 0x86, 0x0C, 0x8C,
	0xA7, 0x3E, 0xA5, 0x12, 0xA2, 0xA4, 0x4B, 0x95, 0xE0, 0x31, 0xBD, 0x9E,
	0x4D, 0x86, 0x45, 0xCE, 0x17, 0xD5, 0x5D, 0x7D, 0x08, 0xC0, 0x52, 0x40,
	0xA3, 0x6E, 0x86, 0x1B, 0xD4, 0xAC, 0xBA, 0xC4, 0x5B, 0x2B, 0xC4, 0xE1,
	0x84, 0x12, 0x19, 0x91, 0x88, 0xB1, 0xEC, 0x5A, 0x52, 0x61, 0x39, 0x25,
	0xA8, 0x98, 0x07, 0x26, 0x35, 0x64, 0x5D, 0xA4, 0x98, 0x32, 0xDB, 0x57,
	0x57, 0x5A, 0xCC, 0xDD, 0x2A, 0x67, 0xE0, 0x11, 0x65, 0xC9, 0x61, 0x47,
	0x62, 0x79, 0x60, 0x6E, 0x22, 0x27, 0x17, 0x86, 0x67, 0x29, 0x72, 0x59,
	0x72, 0xB8, 0xDB, 0x14, 0x2D, 0x3A, 0x53, 0x72, 0x36, 0x4C, 0xC8, 0xED,
	0xC6, 0x2E, 0xEA, 0xE4, 0xBD, 0x23, 0x3D, 0x16, 0x0D, 0x53, 0x3C, 0x13,
	0xE0, 0x50, 0xC7, 0xBD, 0x3C, 0xB7, 0x92, 0x57, 0xEE, 0xD6, 0x14, 0xD5,
	0x5D, 0xBE, 0x3B, 0x9E, 0x4D, 0xEE, 0x4D, 0x63, 0x13, 0x05, 0x29, 0xCD,
	0x7D, 0x34, 0xD9, 0x2A, 0x10, 0xAE, 0xBB, 0xA7, 0x3B, 0x2A, 0x26, 0x20,
	0x79, 0x4C, 0x47, 0x2B, 0x0C, 0x65, 0x75, 0x09, 0xB4, 0xC3, 0x36, 0x75,
	0x87, 0x25, 0x61, 0xA1, 0xA3, 0xB4, 0x44, 0x68, 0xDE, 0xDD, 0x45, 0x0C,
	0xB8, 0xED, 0x8E, 0xC1, 0x2E, 0x4B, 0x5C, 0x4E, 0x15, 0x93, 0x8B, 0x46,
	0xC3, 0x53, 0x79, 0x02, 0x74, 0x8D, 0x2C, 0x7B, 0x6A, 0x25, 0x09, 0x31,
	0x9E, 0xBE, 0xAB, 0x40, 0x38, 0x04, 0x98, 0x87, 0xD1, 0x40, 0x36, 0xC4,
	0xDD, 0xCC, 0x9E, 0x53, 0x03, 0x98, 0xC1, 0x7A, 0xE8, 0x98, 0xB2, 0x1C,
	0x29, 0x6D, 0x53, 0xC2, 0x26, 0x1B, 0xE7, 0x64, 0x2C, 0x45, 0xEE, 0xAC,
	0x98, 0x0A, 0xB3, 0x8A, 0xBE, 0xA0, 0x77, 0xDB, 0x66, 0x65, 0x0A, 0xB7,
	0x25, 0x6E, 0xCB, 0xD2, 0xD8, 0x4B, 0x32, 0x6D, 0xD5, 0xE0, 0xB6, 0xBA,
	0xE7, 0xE8, 0x84, 0xCE, 0xC7, 0x76, 0xC9, 0xC0, 0x07, 0x1D, 0x21, 0x83,
	0x07, 0x69, 0xAA, 0xBA, 0x9A, 0xE4, 0xC5, 0x99, 0xB4, 0xEA, 0x90, 0x14,
	0x7E, 0xE3, 0x5C, 0x7D, 0xEA, 0x70, 0xC2, 0x41, 0xBB, 0xB1, 0x97, 0x39,
	0xD6, 0x2C, 0x1D, 0x80, 0x62, 0x1A, 0xA7, 0x5C, 0x31, 0x51, 0xC9, 0xB8,
	0x0D, 0xEC, 0x30, 0xA0, 0xA5, 0x5D, 0x99, 0xB1, 0x17, 0x9A, 0x08, 0x53,
	0x6E, 0xC8, 0x21, 0xB4, 0xA8, 0xC2, 0xDA, 0xB5, 0x71, 0xE5, 0x27, 0x28,
	0x44, 0xE4, 0x01, 0x87, 0x7A, 0x63, 0x22, 0xC9, 0x81, 0x31, 0xC8, 0x26,
	0xB3, 0x3E, 0x8E, 0x1D, 0xC4, 0x3C, 0x27, 0x38, 0x04, 0x92, 0x37, 0x35,
	0x35, 0xC0, 0x31, 0xAA, 0x18, 0x8B, 0xC9, 0xE8, 0x98, 0x6D, 0xD0, 0x71,
	0xC9, 0x08, 0xDE, 0x23, 0x0D, 0xA2, 0x20, 0x9A, 0x87, 0xA8, 0xD6, 0xB6,
	0x51, 0x8A, 0x05, 0x63, 0xDB, 0x39, 0x02, 0xB2, 0x64, 0xBE, 0xDB, 0x58,
	0xDA, 0x46, 0x4D, 0x25, 0xD9, 0x3C, 0x66, 0x29, 0x66, 0x36, 0xC0, 0xA5,
	0xA8, 0x28, 0xAB, 0x78, 0xA0, 0xC5,
]

def parse_entry(entry_data, entry_id, offset, nbyte):
	""" Hent artikel fra datafil

	file_path = sti til datafilen
	entry_id = artikelID fra databasen
	offset = byte offset i filen
	nbyte = antal af bytes der skal læses """

	key_offset = ((entry_id + 0x170A8) * 1103) % 414
	for i in range(len(entry_data)):
		entry_data[i] ^= KEY[(i + key_offset) % 414]
	return entry_data.tostring()


def entry_to_html(entry, entry_type):
	entry = entry.strip()
	entry = re.sub(r'</?font.*?>', '', entry)
	entry = re.sub(r'<fx><ul><li/>', '', entry)
	entry = re.sub(r'<td>&nbsp;</td>', '<pre>                     </pre>', entry)
	entry = re.sub(r'&nbsp;', '<pre> </pre>', entry)
	entry = re.sub(r'<tr><ih><b>singularis</b></td><td>', '<pre><b>singularis:          </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>singularis \(intetkøn\)</b></td>', '<pre><b>singul. (intetkøn):  </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>singularis \(fælleskøn\)</b></td>', '<pre><b>singul. (fælleskøn): </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>singularis intetkøn</b></td><td>', '<pre><b>singularis intetkøn: </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>singularis fælleskøn</b></td><td>', '<pre><b>singularis fælleskøn:</b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>pluralis</b></td><td>', '<pre><b>pluralis:            </b></pre>', entry)
	entry = re.sub(r'<tr><ih colspan="."><b>positiv</b></td></tr><tr><td colspan=".">', '<b>positiv: </b>', entry)
	entry = re.sub(r'<tr><ih colspan="."><b>komparativ</b></td></tr><tr><td colspan=".">', '<b>komparativ: </b>', entry)
	entry = re.sub(r'<tr><ih colspan="3"><b>superlativ</b></td></tr><tr><td colspan="3">', '<pre><b>superlativ:          </b></pre>', entry)
	entry = re.sub(r'<tr><ih colspan="1"><b>superlativ</b></td></tr><tr><td colspan="1">', '<b>superlativ:          </b>', entry)
	entry = re.sub(r'<tr><ih><b>infinitiv</b></td><td>', '<pre><b>infinitiv:             </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>præsens</b></td><td>', '<pre><b>præsens:               </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>præteritum</b></td><td>', '<pre><b>præteritum:            </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>præsens participium</b></td><td>', '<pre><b>præsens participium:   </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>præteritum participium</b></td><td>', '<pre><b>præteritum participium:</b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>imperativ</b></td><td>', '<pre><b>imperativ:             </b></pre>', entry)
	entry = re.sub(r'<tr><ih><b>pluralis</b></td><td colspan="2"><i><b>ordet har ikke pluralis</b></i></td></tr>', '<pre><b>pluralis:</b>            <i>ordet har ikke pluralis</i></pre><br/>', entry)
	entry = re.sub(r'<tr><ih><b>singularis</b></td><td colspan="2"><i><b>adjektivet har ikke singularis</b></i></td></tr>', '<pre><b>singularis:</b>          <i>adjektivet har ikke singularis</i></pre><br/>', entry)
	entry = re.sub(r'<tr><td><b>antonymer</b></td></tr>', '<b><br/><br/>antonymer: </b>', entry)
	entry = re.sub(r'<etym>', '<b><br/><br/>etymologi: </b>', entry)
	entry = re.sub(r'<syn>', '<b><br/><br/>synonymer: </b>', entry)
	entry = re.sub(r'<syn2>', '<b><br/><br/>synonymer: </b>', entry)
	entry = re.sub(r'<inflect>', '', entry)
	entry = re.sub(r'<ih>', '', entry)
	entry = re.sub(r'<ih colspan="3">', '', entry)
	entry = re.sub(r'</inflect>', '', entry)
	entry = re.sub(r'<td>', '', entry)
	entry = re.sub(r'<td colspan="3">', '', entry)
	entry = re.sub(r'<td colspan="2">', '', entry)
	entry = re.sub(r'</td></tr>', '<br/>', entry)
	entry = re.sub(r'</td>', ', ', entry)
	entry = re.sub(r'<tr>', '', entry)
	entry = re.sub(r'</tr>', '<br/>', entry)
	entry = re.sub(r'<table>', '', entry)
	entry = re.sub(r'</table>', '', entry)
	entry = re.sub(r'<fx>', '<span>- fx:', entry)
	entry = re.sub(r'<f1>', '<i>', entry)
	entry = re.sub(r'<p1>', ' <i>', entry)
	entry = re.sub(r'</p1>', '</i>', entry)
	entry = re.sub(r'<p2>', '<i>', entry)
	entry = re.sub(r'<p3>', '<i>', entry)
	entry = re.sub(r'<m.>', 'm.', entry)
	entry = re.sub(r'<f.>', 'f.', entry)
	entry = re.sub(r'<n.>', 'n.', entry)
	entry = re.sub(r'<pl.>', 'pl.', entry)
	entry = re.sub(r'�', '*', entry)
	entry = re.sub(r'<sup>', '^', entry)
	entry = re.sub(r'</sup>', '', entry)
	entry = re.sub(r'<od>', '<br/>', entry)

	if entry_type == 'lookup':
		entry = re.sub(r'<div><h2>', '<span style="font-size:8pt">- ', entry)
		entry = re.sub(r'</h2></div>', ' </span>', entry)
		entry = re.sub(r'</h2><div>', ' </span>', entry)
		entry = re.sub(r'<h3>.*?</h3>', '<br/>', entry)
		entry = re.sub(r' </span><span>', ', </span><span>', entry)
	elif entry_type == 'collocation_lookup':
		entry = re.sub(r'<div><h3>', '<span style="font-size:8pt">- ', entry)
		entry = re.sub(r'<h3>', '<span style="font-size:8pt">- ', entry)
		entry = re.sub(r'</h3>', ' </span><br/>', entry)
	elif entry_type == 'reverse':
		if entry.find('h2') == -1:
			entry = re.sub(r'<div><h3>', '<span style="font-size:8pt">- ', entry)
			entry = re.sub(r'</h3>', ' </span>', entry)
		else:
			entry = re.sub(r'<div><h2>', '<span style="font-size:8pt">- ', entry)
			entry = re.sub(r'</h2>', ' </span>', entry)
			entry = re.sub(r'<h3>.*?</h3>', '<br/>', entry)
	entry = re.sub(r'\[LYD\]', '', entry)
	entry = re.sub(r'\[INFO\]', '', entry)
	entry = re.sub(r'<li><div>', '<li>', entry)
	entry = re.sub(r'<div><a href', ' <a href', entry)
	entry = re.sub(r'<br/><div>', '<br/>', entry)
	entry = re.sub(r'<div><br/>', '<br/>', entry)
	entry = re.sub(r'<div></div>', '', entry)
	entry = re.sub(r'</div><div>', ' ', entry)
	entry = re.sub(r'<div>', ', ', entry)
	entry = re.sub(r'</div>', '', entry)
	entry = re.sub(r'</?h[1-9]>', '', entry)
	if entry.endswith('</ol>') or entry.endswith('</ul>'):
		entry = entry + '<br/>'
	else:
		entry = entry + '<br/><br/>'			
	return entry

