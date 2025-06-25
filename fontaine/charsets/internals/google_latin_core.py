from fontaine.namelist import codepointsInNamelist


class Charset:
    common_name = "Google Fonts: Latin Core"
    native_name = ""
    abbreviation = "LAT"

    def glyphs(self):
        glyphs = codepointsInNamelist(
            "charsets/internals/google_glyphsets/GF-latin-core_unique-glyphs.nam"
        )
        return glyphs
