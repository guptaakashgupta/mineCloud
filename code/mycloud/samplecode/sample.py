import xattr
print(xattr.listxattr("todo"))
#xattr.setxattr("todo","user.comment","samnk file")
print(xattr.getxattr("todo","user.comment"))
