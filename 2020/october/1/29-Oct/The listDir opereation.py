def listDir(self,url):

    path = self.parse_url(url)

    if path is None:

        redir_url = KURL(url.path())

        self.redirection(redir_url)
        self.finished()
        return

    adfs_object = self.find_file_within_image(path)

    if not adfs_object:

        self.error(KIO.ERR_DOES_NOT_EXIST,path)
        return
    elif path != u"" and path[-1] !- u"/":

        url.setPath(unicode(url.path()) + u"/")
        self.redirection(url)
        self.finished()
        return
    elif type(adfs_object[1]) != type([]):

        self.error(KIO.ERR_IS_FILE,path)
        return

    #Obtain a list of files.
    files = adfs_object[1]

    #Return the objects in the list to the application.

    for this_file in files:

        entr = self.build_entry(this_file)

        if entry != []:

            self.listEntry(entry,0)

            #For old style disk images, return a .inf file, too....
            if self.adfsdisc.disc_type.find("adE") == -1:

                this_inf = self.find_file_within_image(
                    path + "/" + this_file[0] + ".inf"
                    )

                if this_inf is not None:

                    entry = self.build_entry(this_inf)

                    if entry != []:

                        self.listEntry(entry,0)

    #We have finished listing the contents of a directory.
    self.listEntry([],1)

    self.finished()


                        
