import errno
import os
import unicodedata

from fontaine.ext.base import BaseExt


class Extension(BaseExt):
    path = os.path.join(BaseExt.CHARACTER_SET_PATH, "subsets")
    extension_name = "subsets"
    description = "Subsets collections"

    @staticmethod
    def get_subsets():
        for filepath in os.listdir(Extension.path):
            yield os.path.splitext(os.path.basename(filepath))[0]

    @staticmethod
    def get_subset_path(subsetname):
        path = os.path.join(Extension.path, subsetname) + ".txt"
        if not os.path.exists(path):
            raise OSError(errno.ENOENT, "File [%s] does not exist" % path)
        return path

    @staticmethod
    def get_glyphs(subsetname):
        path = os.path.join(Extension.path, subsetname) + ".txt"
        if not os.path.exists(path):
            return ""
        return open(path).read()

    @staticmethod
    def __getcharsets__():
        for filepath in os.listdir(Extension.path):
            common_name = os.path.splitext(os.path.basename(filepath))[0]

            with open(os.path.join(Extension.path, filepath)) as fp:
                contents = fp.read()

            lines = contents.split("\n")
            unicodes = []
            for ch in lines:
                if not ch:
                    continue
                unicodes.append(int(ch.lstrip("U+"), 16))
            yield type(
                "Charset",
                (object,),
                dict(
                    glyphs=unicodes,
                    common_name="Subset %s" % common_name,
                    short_name=unicodedata.normalize("NFKD", f"subset-{common_name}"),
                    native_name="",
                ),
            )
