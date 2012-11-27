#!/usr/bin/python
import sys
found="false"
class trie:
	count={}
	def __init__(self):
		self.node={}
	def similar(self,getstring):
		if self.node.keys()==[]:
        	        sys.stdout.write(' '+getstring+' '+str(a.count[getstring]))
			return
		if self.node.has_key('$'):
        	        sys.stdout.write(' '+getstring+' '+str(a.count[getstring]))
		for key in sorted(self.node.keys()):
			if key!='$':
				self.node[key].similar(getstring+key)

	def searchmore(self,string,getstring=''):
		 if len(string) > 0:
        	    char = string[0]
        	    string = string[1:]
        	    if self.node.has_key(char):
        	        getstring = getstring + char
        	        self.node[char].searchmore(string,getstring)
        	       
        	    else:
        	    	if self.node.has_key('$'):
        	        	sys.stdout.write(' '+getstring+' '+str(a.count[getstring]))
        	    	for key in sorted(self.node.iterkeys()):
				if(key!='$'):
					self.node[key].similar(getstring+key)
        	 else:
        	    for key in sorted(self.node.iterkeys()):
			if(key!='$'):
        	        	self.node[key].similar(getstring+key)
	def searchtrie(self,string):
		global found
		if len(string)>0:
			char=string[0]
			remaining_string=string[1:]
			if self.node.has_key(char):
				self.node[char].searchtrie(remaining_string)
			else:
				found="false"
				return
		else:
			if self.node.has_key('$'):
			 	found="true"
				return
	def insert(self,string,dep):
		if len(string)==0:
			self.node['$']=''
			self.depth=dep
			return

		char=string[0]
		remaining_string=string[1:]
		if char in self.node:
			self.depth=dep
			self.node[char].insert(remaining_string,dep+1)
		else:
			current_node=trie()
			self.node[char]=current_node
			self.depth=dep
			current_node.insert(remaining_string,dep+1)
	def printtrie(self,getstring):
		if self.node.keys()==[]:
			return
		if self.node.has_key('$'):
			for i in range(self.depth):
				sys.stdout.write('| ')
			sys.stdout.write('$')
			print 
		for key in sorted(self.node.iterkeys()):	 
			if key!='$':
				for i in range(self.depth):
					sys.stdout.write('| ')
				sys.stdout.write(key)
				print
				self.node[key].printtrie(getstring+key)
	def remove(self,string):
		char=string[0]
		if char in self.node:
			current_node=self.node[char]
			if len(string)>1:
				remaining_string=string[1:]
				current_node.remove(remaining_string)
			else:
				del self.node[string].node['$']
			if len(current_node.node)==0:
			 	del self.node[char]

if __name__=='__main__':
	a=trie()
	n=input()
	while n>0:
		x=raw_input()
		if len(x.split()) > 1:
			operation,s=x.split()
			s=s.lower()
			if operation=='insert':
				a.insert(s,1)
				a.searchtrie(s)
				if found=='true':
					if a.count.has_key(s) and a.count[s]!=-1:
						a.count[s]+=1
					else:
						a.count[s]=1
				found='false'
				print a.count[s]
			if operation=='search':
			   	found='false'
			   	a.searchtrie(s)
			   	if found=='true':
			   		print found+' '+str(a.count[s])
			   	else: 
					sys.stdout.write('false')
					a.searchmore(s)
					print
			if operation=='remove':
				if a.count.has_key(s):
					if a.count[s]==1:
			  			a.remove(s)
			  		if a.count[s]>=1:
						a.count[s]-=1
					else:
					 	a.count[s]=-1
				else:
					a.count[s]=-1
				print a.count[s]	
		else:
			if  x=='ptrie':
				print 'root'
				a.printtrie('')
		n-=1

