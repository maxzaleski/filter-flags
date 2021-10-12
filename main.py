import shutil, os

flagsDir = "./flags"
distDir = "./dist"

def main():
   to_copy = []

   for filename in os.listdir(flagsDir):
      # Filter for flags:
      if len(filename.replace(".svg", "")) == 2:
         to_copy.append(flagsDir + "/" + filename)

   for filename in to_copy:
      if not os.path.exists(distDir):
         os.mkdir(distDir)
      shutil.copy(filename, distDir)

   print(f"Copied %d files to %s" % (len(to_copy), distDir))

if __name__ == "__main__":
   main()
