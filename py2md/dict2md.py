# encoding:utf-8
class Dict2table:
    def __init__(self, dictionary, md_path, title=None, is_subLink=False, is_chief=True,
                 chief_flag="##", subLink_flag="###", mode='a+', sort="default", type_sort=None):
        """

        :param dictionary: a dict
        :param md_path: path to a Markdown file
        :param title: title of table
        :param is_subLink: generate a link for sub dict of your dict
        :param is_chief: MUST be True; specify the main table
        :param chief_flag: specify the title level of the main table
        :param subLink_flag: specify the title level of the sub table
        :param mode: MUST be 'a+'
        :param sort: sort the keys of your dict, "default" is default, "alphabetical" is in alphabetical order, "r_alphabetical" is in reverse alphabetical order
        :param type_sort: sort the keys of your dict by their types, MUST be None or a string of 's' (for str), 'l' (for list), 'd' (for dict), 'i' (for int), 'f' (for float), 'b' (for bool)
        """
        self.dictionary = dictionary
        self.md_path = md_path
        self.title = title
        self.is_subLink = is_subLink
        self.is_chief = is_chief
        self.chief_flag = chief_flag
        self.subLink_flag = subLink_flag
        self.mode = mode
        self.sort = sort
        self.type_sort = type_sort

    def load_md(self):
        """Load Markdown file"""
        f = open(self.md_path, mode=self.mode)
        if self.is_chief and self.is_subLink:   # Check the repeated title, if subLink was used.
            try:
                lines = f.readlines()
                titles = []
                for line in lines:
                    line = line.decode("utf-8")
                    if line[:len(self.chief_flag)+1] == (self.chief_flag + " "):
                        titles.append(line.split(" ")[1].split("\n")[0])
                if self.title.decode("utf-8") in titles:
                    print("Your subLink may fail, because of the repeated title: %s" % self.title)
            except:
                pass
        if (self.title is None) and self.is_subLink:    # subLink must be used with a title.
            print("Please set a title for your table!")
        elif self.title is not None:
            if self.is_chief:
                f.write(self.chief_flag + " " + self.title + "\n")
            else:
                f.write(self.subLink_flag + " " + self.title + "\n")
        f.write("|keys|values|\n")
        f.write("|:--:|:-----|\n")
        return f

    def keys_sort(self, keys):
        """Sort the keys

        :param keys: a list of keys in your dict
        :return keys: a list of ordered keys
        """
        if self.sort == "alphabetical":
            keys.sort()
        elif self.sort == "r_alphabetical":
            keys.sort(reverse=True)
        elif self.sort == "default":
            keys = keys
        else:
            print("sort must be 'default' or 'alphabetical' or 'r_alphabetical'.")
            raise NameError
        return keys

    @staticmethod
    def str2type(str_type):
        """Convert character into the corresponding type.

        :param str_type: a str of type_sort
        :return _type: the corresponding type of str_type
        """
        if str_type == "s":
            _type = str
        elif str_type == "l":
            _type = list
        elif str_type == "d":
            _type = dict
        elif str_type == "i":
            _type = int
        elif str_type == "f":
            _type = float
        elif str_type == "b":
            _type = bool
        else:
            print("type_sort must be None or made up of 's', 'l', 'd', 'i', 'f', 'b'.")
            raise NameError
        return _type

    def __type_sort(self, keys):
        """Sort the keys by their types.

        :param keys: a list of keys in your dict
        :return new_keys: a list of ordered keys
        """
        new_keys = []
        for str_type in self.type_sort:
            _type = self.str2type(str_type)
            for key in keys:
                if isinstance(self.dictionary[key], _type):
                    new_keys.append(key)
                else:
                    pass
        if len(new_keys) == len(keys):
            pass
        else:
            poor_set = list(set(keys) - set(new_keys))
            new_keys.extend(poor_set)
        return new_keys

    def dict2table(self):
        """Convert a python dict into Markdown table(s)."""
        keys = self.dictionary.keys()
        keys = self.keys_sort(keys)
        if self.type_sort is not None:
            keys = self.__type_sort(keys)
        f = self.load_md()
        _dict = self.dictionary
        for key in keys:
            value = _dict[key]
            if (isinstance(value, dict)) and (self.is_subLink is not None):
                sub_title = self.title + "_" + key
                f.write("|[%s](#%s)|%s|\n" % (key, str(sub_title).lower(), value))
                Dict2table(dictionary=value,
                           md_path=self.md_path,
                           title=sub_title,
                           is_subLink=self.is_subLink,
                           is_chief=False,
                           mode='a',
                           sort=self.sort,
                           type_sort=self.type_sort).dict2table()
            else:
                f.write("|%s|%s|\n" % (key, _dict[key]))
        if self.is_chief:
            f.close()
            print("dict2table Done!")
        else:
            pass
