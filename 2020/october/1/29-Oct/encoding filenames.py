def encode_name_from_object(self,obj):

    name = obj[0]

    #If the name contains a slash then replaces it with a dot.
    new_name = u".".join(name.split(u"/"))

    if self.adfsdisc.disc_type.find("adE") == 0:

        if type(obj[1] != type([]) and u"."not in new_name:

                #construct a suffix from the object's load address/filetype.
                suffix = u"%03x" % ((obj[2] >> 8) & 0xfff)
                new_name = new_name + "." + suffix


        return unicode(KURL.encoe_string_no_slash(new_name))

    def decode_name(self,name):

        return unicode(KURL.decode_string(name))
