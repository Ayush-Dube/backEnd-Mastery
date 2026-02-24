import ifNameModule

# When u import a file , it automatically runs that file.
# Meaning if there are some functions called  in that file they will be called here as well.

# So this __name__ == __main__ will be kept in module file , which is used by other files.
print(__name__)

ifNameModule.attack()