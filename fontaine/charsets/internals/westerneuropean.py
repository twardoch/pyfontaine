class Charset:
    common_name = "Western European"
    native_name = "Western European"
    abbreviation = "WE"

    def glyphs(self):
        glyphs = list(range(0x00C0, 0x00CF))
        glyphs += list(range(0x00D0, 0x00D6))
        glyphs += list(range(0x00D8, 0x00DF))
        glyphs += list(range(0x00E0, 0x00EF))
        glyphs += list(range(0x00F0, 0x00F6))
        glyphs += list(range(0x00F8, 0x00FF))
        return glyphs
