#!/usr/bin/env python

source = '<ul class="header-nav left" role="navigation"> <li class="header-nav-item explore"> <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>		          </li>			            <li class="header-nav-item">				                <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>						          </li>							            <li class="header-nav-item">								                <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>										          </li>											          <li class="header-nav-item">												            <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>													            </li> </ul>'
#print source

while True:
    start = source.find('href="')
    if start<0:
        break
    end = source.find('"', start+6)
    url = source[start+6:end]
    print url
    source = source[end+1:]
