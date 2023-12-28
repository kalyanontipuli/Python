s={10,20,30,40}
fs=frozenset(s)
type(fs) # <class 'frozenset'>
fs.add(50) # attribuite error bcz fronset is immutable
fs.remove(10) # attribute error
