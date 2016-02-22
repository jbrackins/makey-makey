#!/usr/bin/python3

import sys
import datetime
from subprocess import call

# ===========================================================================
# Replacer Class
# ===========================================================================

class Replacer(object):

    def __init__( self, proj ):
        #Config File
        self.CONFIG = "renamer.conf"

        #General Stuff
        self.AUTHOR_NAME       = None
        self.CURRENT_DATE              = None
        self.PROJECT_NAME      = proj
        self.PROJECT_NAME_CAPS = proj.upper()

        #Course Information
        self.COURSE_NAME     = None
        self.COURSE_SECTION  = None
        self.COURSE_LOCATION = None
        self.PROFESSOR_NAME  = None
        
        #Value you are replacing
        self.OLD      = "<SKELETON>"
        self.OLD_CAPS = "<SKELETON_CAPS>"

    def setDate( self ):
        self.CURRENT_DATE = datetime.datetime.today().strftime('%B %d, %Y')

    def readConfig( self ):
        with open(self.CONFIG, "r") as ins:
            array = []
            for line in ins:
                if( line[0] != "#" and line[0] != "\n" ):
                    array.append(line)

        for input_line in array:
            pair = input_line.split('=', 1 )
            key = pair[0].strip()
            value = pair[1].strip()
            value = value.strip('\n')
            print(key,value)

            if(key=="AUTHOR_NAME"):
                self.AUTHOR_NAME = value
            elif(key=='COURSE_NAME'):
                self.COURSE_NAME = value
            elif(key=='COURSE_SECTION'):
                self.COURSE_SECTION = value
            elif(key=='COURSE_LOCATION'):
                self.COURSE_LOCATION = value
            elif(key=='PROFESSOR_NAME'):
                self.PROFESSOR_NAME = value

    def makeTemp( self ):
        call(["cp", "files/SKELETON.cpp", "files/temp.cpp"])

    def swap( self, old, new ):
        f = open("files/temp.cpp",'r')
        filedata = f.read()
        f.close()

        newdata = filedata.replace(old,new)

        f = open("files/temp.cpp",'w')
        f.write(newdata)
        f.close()


def replace( old, new ):
    print("replacing", old, "with", new)

def usage( args ):
    usage = "Usage: " + args[0] + " <filename> <projectname>\n"
    usage = usage + "<filename>    - The file you wish to search through\n"
    usage = usage + "<projectname> - New project name"
    return usage

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print( usage( sys.argv ) )
    else:
        r = Replacer("cool")
        r.makeTemp()
        r.readConfig()
        r.setDate()
        r.swap("<SKELETON>", r.PROJECT_NAME)
        r.swap("<SKELETON_CAPS>", r.PROJECT_NAME_CAPS)
        r.swap("<AUTHOR_NAME>", r.AUTHOR_NAME)
        r.swap("<CURRENT_DATE>", r.CURRENT_DATE)
        r.swap("<COURSE_NAME>", r.COURSE_NAME)
        r.swap("<COURSE_SECTION>", r.COURSE_SECTION)
        r.swap("<COURSE_LOCATION>", r.COURSE_LOCATION)
        r.swap("<PROFESSOR_NAME>", r.PROFESSOR_NAME)

        #replace( sys.argv[1], sys.argv[2] )