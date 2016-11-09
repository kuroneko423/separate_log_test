#!/usr/bin/env python
# -*- coding: utf-8 -*-

# xxx logを"is start"〜"is end"までで分割するツール

import sys
import re

def main():
	argv = sys.argv
	if (len(argv) != 2):
		#引数がちゃんとあるかチェック
		#正しくなければメッセージを出力して終了
		print 'Usage: python {0} path_to_logfile'.format(argv[0])
		quit()

	senario_name = 'senario'
	host_name = 'host'

	f = open(argv[1],'r')
	lines = f.readlines()
	f.close()

	r_start = re.compile('is start$')
	r_end = re.compile('is end$')
	r_senario = re.compile('\[([a-zA-Z0-9]*)\]')
	r_host = re.compile('^([a-z][a-zA-Z0-9]*)#$')

	ll = ''

	for line in lines:
		m_start = r_start.search(line)
		m_end = r_end.search(line)
		m_host = r_host.search(line)
		m_senario = r_senario.search(line)
		ll = ll + line
		if m_start:
			senario_name = 'senario'
			host_name = 'host'
			ll = line
		if m_senario:
			senario_name =  m_senario.group(1)
		if m_host:
			host_name = m_host.group(1)
		if m_end:
			file_name = '{0}_{1}.log'.format(senario_name,host_name)
			with open(file_name,'w') as f_w:
				f_w.writelines(ll)

if __name__ == '__main__':
	main()
