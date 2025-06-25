class Charset:
    common_name = "NotoNaskhArabic-Bold"
    native_name = ""

    def glyphs(self):
        chars = []
        chars.append(0x0000)  # uniFEFF	????
        chars.append(0xFEAB)  # uni0630	ARABIC LETTER THAL ISOLATED FORM
        chars.append(0xFEAC)  # uniFEAC	ARABIC LETTER THAL FINAL FORM
        chars.append(0x200B)  # uni200B	ZERO WIDTH SPACE
        chars.append(0x200C)  # uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x200D)  # uni200D	ZERO WIDTH JOINER
        chars.append(0x200E)  # uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x200F)  # uni200F	RIGHT-TO-LEFT MARK
        chars.append(0x2010)  # uni2010	HYPHEN
        chars.append(0x2011)  # uni2011	NON-BREAKING HYPHEN
        chars.append(
            0xFC03
        )  # uniFC03	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFEAE)  # uniFEAE	ARABIC LETTER REH FINAL FORM
        chars.append(0xFEAF)  # uni0632	ARABIC LETTER ZAIN ISOLATED FORM
        chars.append(0x0020)  # uni00A0	SPACE
        chars.append(0x0021)  # exclam	EXCLAMATION MARK
        chars.append(0xFEB1)  # uni0633	ARABIC LETTER SEEN ISOLATED FORM
        chars.append(0x002C)  # comma	COMMA
        chars.append(0xFEB2)  # uniFEB2	ARABIC LETTER SEEN FINAL FORM
        chars.append(0x002E)  # period	FULL STOP
        chars.append(0x0030)  # zero	DIGIT ZERO
        chars.append(0x0031)  # one	DIGIT ONE
        chars.append(0x0032)  # two	DIGIT TWO
        chars.append(0x0033)  # three	DIGIT THREE
        chars.append(0x0034)  # four	DIGIT FOUR
        chars.append(0x0035)  # five	DIGIT FIVE
        chars.append(0x0036)  # six	DIGIT SIX
        chars.append(0x0037)  # seven	DIGIT SEVEN
        chars.append(0x0038)  # eight	DIGIT EIGHT
        chars.append(0x0039)  # nine	DIGIT NINE
        chars.append(0x003A)  # colon	COLON
        chars.append(0xFEB5)  # uni0634	ARABIC LETTER SHEEN ISOLATED FORM
        chars.append(0xFEAD)  # uni0631	ARABIC LETTER REH ISOLATED FORM
        chars.append(0xFEB6)  # uniFEB6	ARABIC LETTER SHEEN FINAL FORM
        chars.append(0xFEB7)  # uniFEB7	ARABIC LETTER SHEEN INITIAL FORM
        chars.append(0xFEB8)  # uniFEB8	ARABIC LETTER SHEEN MEDIAL FORM
        chars.append(0xFEB9)  # uni0635	ARABIC LETTER SAD ISOLATED FORM
        chars.append(0xFEBA)  # uniFEBA	ARABIC LETTER SAD FINAL FORM
        chars.append(0xFEBB)  # uniFEBB	ARABIC LETTER SAD INITIAL FORM
        chars.append(0xFED4)  # uniFED4	ARABIC LETTER FEH MEDIAL FORM
        chars.append(0xFEBC)  # uniFEBC	ARABIC LETTER SAD MEDIAL FORM
        chars.append(0xFEBD)  # uni0636	ARABIC LETTER DAD ISOLATED FORM
        chars.append(0xFEBE)  # uniFEBE	ARABIC LETTER DAD FINAL FORM
        chars.append(0xFEBF)  # uniFEBF	ARABIC LETTER DAD INITIAL FORM
        chars.append(0xFEC0)  # uniFEC0	ARABIC LETTER DAD MEDIAL FORM
        chars.append(0xFBC1)  # uniFBC1	????
        chars.append(0xFEC1)  # uni0637	ARABIC LETTER TAH ISOLATED FORM
        chars.append(0xFEC2)  # uniFEC2	ARABIC LETTER TAH FINAL FORM
        chars.append(0xFEC3)  # uniFEC3	ARABIC LETTER TAH INITIAL FORM
        chars.append(0xFEC4)  # uniFEC4	ARABIC LETTER TAH MEDIAL FORM
        chars.append(0xFEB0)  # uniFEB0	ARABIC LETTER ZAIN FINAL FORM
        chars.append(0xFEC5)  # uni0638	ARABIC LETTER ZAH ISOLATED FORM
        chars.append(0x00A0)  # uni00A0	NO-BREAK SPACE
        chars.append(0x08A2)  # uni08A2	????
        chars.append(0x08A3)  # uni08A3	????
        chars.append(0x08A4)  # uni08A4	????
        chars.append(0x08A5)  # uni08A5	????
        chars.append(0x08A6)  # uni08A6	????
        chars.append(0x08A7)  # uni08A7	????
        chars.append(0x08A8)  # uni08A8	????
        chars.append(0x08A9)  # uni08A9	????
        chars.append(0x08AA)  # uni08AA	????
        chars.append(
            0x00AB
        )  # guillemotleft	LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x08AC)  # uni08AC	????
        chars.append(0xFEC8)  # uniFEC8	ARABIC LETTER ZAH MEDIAL FORM
        chars.append(0xFEC9)  # uni0639	ARABIC LETTER AIN ISOLATED FORM
        chars.append(
            0x00BB
        )  # guillemotright	RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0xFECA)  # uniFECA	ARABIC LETTER AIN FINAL FORM
        chars.append(0xFECB)  # uniFECB	ARABIC LETTER AIN INITIAL FORM
        chars.append(0xFECC)  # uniFECC	ARABIC LETTER AIN MEDIAL FORM
        chars.append(0xFECD)  # uni063A	ARABIC LETTER GHAIN ISOLATED FORM
        chars.append(0xFECE)  # uniFECE	ARABIC LETTER GHAIN FINAL FORM
        chars.append(0xFECF)  # uniFECF	ARABIC LETTER GHAIN INITIAL FORM
        chars.append(0xFED0)  # uniFED0	ARABIC LETTER GHAIN MEDIAL FORM
        chars.append(0x08E4)  # uni08E4	????
        chars.append(0x08E5)  # uni08E5	????
        chars.append(0x08E6)  # uni08E6	????
        chars.append(0x08E7)  # uni08E7	????
        chars.append(0x08E8)  # uni08E8	????
        chars.append(0x08E9)  # uni08E9	????
        chars.append(0x08EA)  # uni08EA	????
        chars.append(0x08EB)  # uni08EB	????
        chars.append(0x08EC)  # uni08EC	????
        chars.append(0x08ED)  # uni08ED	????
        chars.append(0x08EE)  # uni08EE	????
        chars.append(0x08EF)  # uni08EF	????
        chars.append(0x08F0)  # uni08F0	????
        chars.append(0x08F1)  # uni08F1	????
        chars.append(0x08F2)  # uni08F2	????
        chars.append(0x08F3)  # uni08F3	????
        chars.append(0x08F4)  # uni08F4	????
        chars.append(0x08F5)  # uni08F5	????
        chars.append(0x08F6)  # uni08F6	????
        chars.append(0x08F7)  # uni08F7	????
        chars.append(0x08F8)  # uni08F8	????
        chars.append(0x08F9)  # uni08F9	????
        chars.append(0x08FA)  # uni08FA	????
        chars.append(0x08FB)  # uni08FB	????
        chars.append(0x08FC)  # uni08FC	????
        chars.append(0x08FD)  # uni08FD	????
        chars.append(0x08FE)  # uni08FE	????
        chars.append(0xFED5)  # uni0642	ARABIC LETTER QAF ISOLATED FORM
        chars.append(0xFED6)  # uniFED6	ARABIC LETTER QAF FINAL FORM
        chars.append(0xFED7)  # uniFED7	ARABIC LETTER QAF INITIAL FORM
        chars.append(0xFED8)  # uniFED8	ARABIC LETTER QAF MEDIAL FORM
        chars.append(0xFEB4)  # uniFEB4	ARABIC LETTER SEEN MEDIAL FORM
        chars.append(0xFED9)  # uni0643	ARABIC LETTER KAF ISOLATED FORM
        chars.append(0xFE91)  # uniFE91	ARABIC LETTER BEH INITIAL FORM
        chars.append(0xFE70)  # uniFE70	ARABIC FATHATAN ISOLATED FORM
        chars.append(0xFEDA)  # uniFEDA	ARABIC LETTER KAF FINAL FORM
        chars.append(0xFEDB)  # uniFEDB	ARABIC LETTER KAF INITIAL FORM
        chars.append(0xFEDC)  # uniFEDC	ARABIC LETTER KAF MEDIAL FORM
        chars.append(0xFED1)  # uni0641	ARABIC LETTER FEH ISOLATED FORM
        chars.append(0xFEB3)  # uniFEB3	ARABIC LETTER SEEN INITIAL FORM
        chars.append(0xFE95)  # uni062A	ARABIC LETTER TEH ISOLATED FORM
        chars.append(0xFEDE)  # uniFEDE	ARABIC LETTER LAM FINAL FORM
        chars.append(0xFE71)  # uniFE71	ARABIC TATWEEL WITH FATHATAN ABOVE
        chars.append(0xFEDF)  # uniFEDF	ARABIC LETTER LAM INITIAL FORM
        chars.append(0xFEE0)  # uniFEE0	ARABIC LETTER LAM MEDIAL FORM
        chars.append(0xFEE1)  # uni0645	ARABIC LETTER MEEM ISOLATED FORM
        chars.append(0xFEE2)  # uniFEE2	ARABIC LETTER MEEM FINAL FORM
        chars.append(0xFEE3)  # uniFEE3	ARABIC LETTER MEEM INITIAL FORM
        chars.append(0xFE72)  # uniFE72	ARABIC DAMMATAN ISOLATED FORM
        chars.append(0xFEE4)  # uniFEE4	ARABIC LETTER MEEM MEDIAL FORM
        chars.append(0xFEE5)  # uni0646	ARABIC LETTER NOON ISOLATED FORM
        chars.append(0xFEE6)  # uniFEE6	ARABIC LETTER NOON FINAL FORM
        chars.append(0xFEE7)  # uniFEE7	ARABIC LETTER NOON INITIAL FORM
        chars.append(0xFEE8)  # uniFEE8	ARABIC LETTER NOON MEDIAL FORM
        chars.append(0xFE73)  # uniFE73	ARABIC TAIL FRAGMENT
        chars.append(0xFEE9)  # uni0647	ARABIC LETTER HEH ISOLATED FORM
        chars.append(0xFEEA)  # uniFEEA	ARABIC LETTER HEH FINAL FORM
        chars.append(0xFEEB)  # uniFEEB	ARABIC LETTER HEH INITIAL FORM
        chars.append(0xFEEC)  # uniFEEC	ARABIC LETTER HEH MEDIAL FORM
        chars.append(0xFEED)  # uni0648	ARABIC LETTER WAW ISOLATED FORM
        chars.append(0xFE74)  # uniFE74	ARABIC KASRATAN ISOLATED FORM
        chars.append(0xFEEE)  # uniFEEE	ARABIC LETTER WAW FINAL FORM
        chars.append(0xFEEF)  # uni0649	ARABIC LETTER ALEF MAKSURA ISOLATED FORM
        chars.append(0xFEF0)  # uniFEF0	ARABIC LETTER ALEF MAKSURA FINAL FORM
        chars.append(0xFEF1)  # uni064A	ARABIC LETTER YEH ISOLATED FORM
        chars.append(0xFEF2)  # uniFEF2	ARABIC LETTER YEH FINAL FORM
        chars.append(0xFE92)  # uniFE92	ARABIC LETTER BEH MEDIAL FORM
        chars.append(0xFEF3)  # uniFEF3	ARABIC LETTER YEH INITIAL FORM
        chars.append(0xFEF4)  # uniFEF4	ARABIC LETTER YEH MEDIAL FORM
        chars.append(
            0xFEF5
        )  # uniFEF5	ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM
        chars.append(
            0xFEF6
        )  # uniFEF6	ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE FINAL FORM
        chars.append(
            0xFEF7
        )  # uniFEF7	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFE76)  # uniFE76	ARABIC FATHA ISOLATED FORM
        chars.append(
            0xFEF8
        )  # uniFEF8	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE FINAL FORM
        chars.append(
            0xFEF9
        )  # uniFEF9	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA BELOW ISOLATED FORM
        chars.append(
            0xFEFA
        )  # uniFEFA	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA BELOW FINAL FORM
        chars.append(0xFEFB)  # uniFEFB	ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
        chars.append(0xFEFC)  # uniFEFC	ARABIC LIGATURE LAM WITH ALEF FINAL FORM
        chars.append(0xFE77)  # uniFE77	ARABIC FATHA MEDIAL FORM
        chars.append(0xFEFF)  # uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xFE78)  # uniFE78	ARABIC DAMMA ISOLATED FORM
        chars.append(0xFE8E)  # uniFE8E	ARABIC LETTER ALEF FINAL FORM
        chars.append(0xFE79)  # uniFE79	ARABIC DAMMA MEDIAL FORM
        chars.append(0xFE93)  # uni0629	ARABIC LETTER TEH MARBUTA ISOLATED FORM
        chars.append(0xFE7A)  # uniFE7A	ARABIC KASRA ISOLATED FORM
        chars.append(0xFE7B)  # uniFE7B	ARABIC KASRA MEDIAL FORM
        chars.append(0xFE7C)  # uniFE7C	ARABIC SHADDA ISOLATED FORM
        chars.append(0xFE90)  # uniFE90	ARABIC LETTER BEH FINAL FORM
        chars.append(0xFE7D)  # uniFE7D	ARABIC SHADDA MEDIAL FORM
        chars.append(0xFE7E)  # uniFE7E	ARABIC SUKUN ISOLATED FORM
        chars.append(0xFE94)  # uniFE94	ARABIC LETTER TEH MARBUTA FINAL FORM
        chars.append(0xFE7F)  # uniFE7F	ARABIC SUKUN MEDIAL FORM
        chars.append(0xFEC6)  # uniFEC6	ARABIC LETTER ZAH FINAL FORM
        chars.append(0xFEC7)  # uniFEC7	ARABIC LETTER ZAH INITIAL FORM
        chars.append(0xFB50)  # uni0671	ARABIC LETTER ALEF WASLA ISOLATED FORM
        chars.append(0xFB51)  # uniFB51	ARABIC LETTER ALEF WASLA FINAL FORM
        chars.append(0xFB52)  # uni067B	ARABIC LETTER BEEH ISOLATED FORM
        chars.append(0xFB53)  # uniFB53	ARABIC LETTER BEEH FINAL FORM
        chars.append(0xFB54)  # uniFB54	ARABIC LETTER BEEH INITIAL FORM
        chars.append(0xFB55)  # uniFB55	ARABIC LETTER BEEH MEDIAL FORM
        chars.append(0xFB56)  # uni067E	ARABIC LETTER PEH ISOLATED FORM
        chars.append(0xFB57)  # uniFB57	ARABIC LETTER PEH FINAL FORM
        chars.append(0xFB58)  # uniFB58	ARABIC LETTER PEH INITIAL FORM
        chars.append(0xFB59)  # uniFB59	ARABIC LETTER PEH MEDIAL FORM
        chars.append(0xFB5A)  # uni0680	ARABIC LETTER BEHEH ISOLATED FORM
        chars.append(0xFB5B)  # uniFB5B	ARABIC LETTER BEHEH FINAL FORM
        chars.append(0xFB5C)  # uniFB5C	ARABIC LETTER BEHEH INITIAL FORM
        chars.append(0xFB5D)  # uniFB5D	ARABIC LETTER BEHEH MEDIAL FORM
        chars.append(0xFB5E)  # uni067A	ARABIC LETTER TTEHEH ISOLATED FORM
        chars.append(0xFB5F)  # uniFB5F	ARABIC LETTER TTEHEH FINAL FORM
        chars.append(0xFB60)  # uniFB60	ARABIC LETTER TTEHEH INITIAL FORM
        chars.append(0xFB61)  # uniFB61	ARABIC LETTER TTEHEH MEDIAL FORM
        chars.append(0xFB62)  # uni067F	ARABIC LETTER TEHEH ISOLATED FORM
        chars.append(0xFB63)  # uniFB63	ARABIC LETTER TEHEH FINAL FORM
        chars.append(0xFB64)  # uniFB64	ARABIC LETTER TEHEH INITIAL FORM
        chars.append(0xFB65)  # uniFB65	ARABIC LETTER TEHEH MEDIAL FORM
        chars.append(0xFB66)  # uni0679	ARABIC LETTER TTEH ISOLATED FORM
        chars.append(0xFB67)  # uniFB67	ARABIC LETTER TTEH FINAL FORM
        chars.append(0xFB68)  # uniFBA2	ARABIC LETTER TTEH INITIAL FORM
        chars.append(0xFB69)  # uniFBA3	ARABIC LETTER TTEH MEDIAL FORM
        chars.append(0xFB6A)  # uni06A4	ARABIC LETTER VEH ISOLATED FORM
        chars.append(0xFB6B)  # uniFB6B	ARABIC LETTER VEH FINAL FORM
        chars.append(0xFB6C)  # uniFB6C	ARABIC LETTER VEH INITIAL FORM
        chars.append(0xFB6D)  # uniFB6D	ARABIC LETTER VEH MEDIAL FORM
        chars.append(0xFB6E)  # uni06A6	ARABIC LETTER PEHEH ISOLATED FORM
        chars.append(0xFB6F)  # uniFB6F	ARABIC LETTER PEHEH FINAL FORM
        chars.append(0xFB70)  # uniFB70	ARABIC LETTER PEHEH INITIAL FORM
        chars.append(0xFB71)  # uniFB71	ARABIC LETTER PEHEH MEDIAL FORM
        chars.append(0xFB72)  # uni0684	ARABIC LETTER DYEH ISOLATED FORM
        chars.append(0xFB73)  # uniFB73	ARABIC LETTER DYEH FINAL FORM
        chars.append(0xFB74)  # uniFB74	ARABIC LETTER DYEH INITIAL FORM
        chars.append(0xFB75)  # uniFB75	ARABIC LETTER DYEH MEDIAL FORM
        chars.append(0xFB76)  # uni0683	ARABIC LETTER NYEH ISOLATED FORM
        chars.append(0xFB77)  # uniFB77	ARABIC LETTER NYEH FINAL FORM
        chars.append(0xFB78)  # uniFB78	ARABIC LETTER NYEH INITIAL FORM
        chars.append(0xFB79)  # uniFB79	ARABIC LETTER NYEH MEDIAL FORM
        chars.append(0xFB7A)  # uni0686	ARABIC LETTER TCHEH ISOLATED FORM
        chars.append(0xFB7B)  # uniFB7B	ARABIC LETTER TCHEH FINAL FORM
        chars.append(0xFB7C)  # uniFB7C	ARABIC LETTER TCHEH INITIAL FORM
        chars.append(0xFB7D)  # uniFB7D	ARABIC LETTER TCHEH MEDIAL FORM
        chars.append(0xFB7E)  # uni0687	ARABIC LETTER TCHEHEH ISOLATED FORM
        chars.append(0xFB7F)  # uniFB7F	ARABIC LETTER TCHEHEH FINAL FORM
        chars.append(0xFB80)  # uniFB80	ARABIC LETTER TCHEHEH INITIAL FORM
        chars.append(0xFB81)  # uniFB81	ARABIC LETTER TCHEHEH MEDIAL FORM
        chars.append(0xFB82)  # uni068D	ARABIC LETTER DDAHAL ISOLATED FORM
        chars.append(0xFB83)  # uniFB83	ARABIC LETTER DDAHAL FINAL FORM
        chars.append(0xFB84)  # uni068C	ARABIC LETTER DAHAL ISOLATED FORM
        chars.append(0xFB85)  # uniFB85	ARABIC LETTER DAHAL FINAL FORM
        chars.append(0xFB86)  # uni068E	ARABIC LETTER DUL ISOLATED FORM
        chars.append(0xFB87)  # uniFB87	ARABIC LETTER DUL FINAL FORM
        chars.append(0xFB88)  # uni0688	ARABIC LETTER DDAL ISOLATED FORM
        chars.append(0xFB89)  # uniFB89	ARABIC LETTER DDAL FINAL FORM
        chars.append(0xFB8A)  # uni0698	ARABIC LETTER JEH ISOLATED FORM
        chars.append(0xFB8B)  # uniFB8B	ARABIC LETTER JEH FINAL FORM
        chars.append(0xFB8C)  # uni0691	ARABIC LETTER RREH ISOLATED FORM
        chars.append(0xFB8D)  # uniFB8D	ARABIC LETTER RREH FINAL FORM
        chars.append(0xFB8E)  # uni06A9	ARABIC LETTER KEHEH ISOLATED FORM
        chars.append(0xFB8F)  # uniFB8F	ARABIC LETTER KEHEH FINAL FORM
        chars.append(0xFB90)  # uniFB90	ARABIC LETTER KEHEH INITIAL FORM
        chars.append(0xFB91)  # uniFB91	ARABIC LETTER KEHEH MEDIAL FORM
        chars.append(0xFB92)  # uni06AF	ARABIC LETTER GAF ISOLATED FORM
        chars.append(0xFB93)  # uniFB93	ARABIC LETTER GAF FINAL FORM
        chars.append(0xFB94)  # uniFB94	ARABIC LETTER GAF INITIAL FORM
        chars.append(0xFB95)  # uniFB95	ARABIC LETTER GAF MEDIAL FORM
        chars.append(0xFB96)  # uni06B2	ARABIC LETTER GUEH ISOLATED FORM
        chars.append(0xFB97)  # uniFB97	ARABIC LETTER GUEH FINAL FORM
        chars.append(0xFB98)  # uniFB98	ARABIC LETTER GUEH INITIAL FORM
        chars.append(0xFB99)  # uniFB99	ARABIC LETTER GUEH MEDIAL FORM
        chars.append(0xFB9A)  # uni06B1	ARABIC LETTER NGOEH ISOLATED FORM
        chars.append(0xFB9B)  # uniFB9B	ARABIC LETTER NGOEH FINAL FORM
        chars.append(0xFB9C)  # uniFB9C	ARABIC LETTER NGOEH INITIAL FORM
        chars.append(0xFB9D)  # uniFB9D	ARABIC LETTER NGOEH MEDIAL FORM
        chars.append(0xFB9E)  # uni06BA	ARABIC LETTER NOON GHUNNA ISOLATED FORM
        chars.append(0xFB9F)  # uniFB9F	ARABIC LETTER NOON GHUNNA FINAL FORM
        chars.append(0xFBA0)  # uni06BB	ARABIC LETTER RNOON ISOLATED FORM
        chars.append(0xFBA1)  # uniFBA1	ARABIC LETTER RNOON FINAL FORM
        chars.append(0xFBA2)  # uniFBA2	ARABIC LETTER RNOON INITIAL FORM
        chars.append(0xFBA3)  # uniFBA3	ARABIC LETTER RNOON MEDIAL FORM
        chars.append(
            0xFBA4
        )  # uni06C0	ARABIC LETTER HEH WITH YEH ABOVE ISOLATED FORM
        chars.append(0xFBA5)  # uniFBA5	ARABIC LETTER HEH WITH YEH ABOVE FINAL FORM
        chars.append(0xFBA6)  # uni06C1	ARABIC LETTER HEH GOAL ISOLATED FORM
        chars.append(0xFBA7)  # uniFBA7	ARABIC LETTER HEH GOAL FINAL FORM
        chars.append(0xFBA8)  # uniFBA8	ARABIC LETTER HEH GOAL INITIAL FORM
        chars.append(0xFBA9)  # uniFBA9	ARABIC LETTER HEH GOAL MEDIAL FORM
        chars.append(0xFBAA)  # uni06BE	ARABIC LETTER HEH DOACHASHMEE ISOLATED FORM
        chars.append(0xFBAB)  # uniFBAB	ARABIC LETTER HEH DOACHASHMEE FINAL FORM
        chars.append(0xFBAC)  # uniFBAC	ARABIC LETTER HEH DOACHASHMEE INITIAL FORM
        chars.append(0xFBAD)  # uniFBAD	ARABIC LETTER HEH DOACHASHMEE MEDIAL FORM
        chars.append(0xFBAE)  # uni06D2	ARABIC LETTER YEH BARREE ISOLATED FORM
        chars.append(0xFBAF)  # uniFBAF	ARABIC LETTER YEH BARREE FINAL FORM
        chars.append(
            0xFBB0
        )  # uni06D3	ARABIC LETTER YEH BARREE WITH HAMZA ABOVE ISOLATED FORM
        chars.append(
            0xFBB1
        )  # uniFBB1	ARABIC LETTER YEH BARREE WITH HAMZA ABOVE FINAL FORM
        chars.append(0xFBB2)  # uniFBB2	????
        chars.append(0xFBB3)  # uniFBB3	????
        chars.append(0xFBB4)  # uniFBB4	????
        chars.append(0xFBB5)  # uniFBB5	????
        chars.append(0xFBB6)  # uniFBB6	????
        chars.append(0xFBB7)  # uniFBB7	????
        chars.append(0xFBB8)  # uniFBB8	????
        chars.append(0xFBB9)  # uniFBB9	????
        chars.append(0xFBBA)  # uniFBBA	????
        chars.append(0xFBBB)  # uniFBBB	????
        chars.append(0xFBBC)  # uniFBBC	????
        chars.append(0xFBBD)  # uniFBBD	????
        chars.append(0xFBBE)  # uniFBBE	????
        chars.append(0xFBBF)  # uniFBBF	????
        chars.append(0xFBC0)  # uniFBC0	????
        chars.append(0x08A0)  # uni08A0	????
        chars.append(0xFBD3)  # uni06AD	ARABIC LETTER NG ISOLATED FORM
        chars.append(0xFBD4)  # uniFBD4	ARABIC LETTER NG FINAL FORM
        chars.append(0xFBD5)  # uniFBD5	ARABIC LETTER NG INITIAL FORM
        chars.append(0xFBD6)  # uniFBD6	ARABIC LETTER NG MEDIAL FORM
        chars.append(0xFBD7)  # uni06C7	ARABIC LETTER U ISOLATED FORM
        chars.append(0xFBD8)  # uniFBD8	ARABIC LETTER U FINAL FORM
        chars.append(0xFBD9)  # uni06C6	ARABIC LETTER OE ISOLATED FORM
        chars.append(0xFBDA)  # uniFBDA	ARABIC LETTER OE FINAL FORM
        chars.append(0xFBDB)  # uni06C8	ARABIC LETTER YU ISOLATED FORM
        chars.append(0xFBDC)  # uniFBDC	ARABIC LETTER YU FINAL FORM
        chars.append(
            0xFBDD
        )  # uni0677	ARABIC LETTER U WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFBDE)  # uni06CB	ARABIC LETTER VE ISOLATED FORM
        chars.append(0xFBDF)  # uniFBDF	ARABIC LETTER VE FINAL FORM
        chars.append(0xFBE0)  # uni06C5	ARABIC LETTER KIRGHIZ OE ISOLATED FORM
        chars.append(0xFBE1)  # uniFBE1	ARABIC LETTER KIRGHIZ OE FINAL FORM
        chars.append(0xFBE2)  # uni06C9	ARABIC LETTER KIRGHIZ YU ISOLATED FORM
        chars.append(0xFBE3)  # uniFBE3	ARABIC LETTER KIRGHIZ YU FINAL FORM
        chars.append(0xFBE4)  # uni06D0	ARABIC LETTER E ISOLATED FORM
        chars.append(0xFBE5)  # uniFBE5	ARABIC LETTER E FINAL FORM
        chars.append(0xFBE6)  # uniFBE6	ARABIC LETTER E INITIAL FORM
        chars.append(0xFBE7)  # uniFBE7	ARABIC LETTER E MEDIAL FORM
        chars.append(
            0xFBE8
        )  # uniFBE8	ARABIC LETTER UIGHUR KAZAKH KIRGHIZ ALEF MAKSURA INITIAL FORM
        chars.append(
            0xFBE9
        )  # uniFBE9	ARABIC LETTER UIGHUR KAZAKH KIRGHIZ ALEF MAKSURA MEDIAL FORM
        chars.append(
            0xFBEA
        )  # uniFBEA	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH ALEF ISOLATED FORM
        chars.append(
            0xFBEB
        )  # uniFBEB	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH ALEF FINAL FORM
        chars.append(
            0xFBEC
        )  # uniFBEC	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH AE ISOLATED FORM
        chars.append(
            0xFBED
        )  # uniFBED	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH AE FINAL FORM
        chars.append(
            0xFBEE
        )  # uniFBEE	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH WAW ISOLATED FORM
        chars.append(
            0xFBEF
        )  # uniFBEF	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH WAW FINAL FORM
        chars.append(
            0xFBF0
        )  # uniFBF0	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH U ISOLATED FORM
        chars.append(
            0xFBF1
        )  # uniFBF1	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH U FINAL FORM
        chars.append(
            0xFBF2
        )  # uniFBF2	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH OE ISOLATED FORM
        chars.append(
            0xFBF3
        )  # uniFBF3	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH OE FINAL FORM
        chars.append(
            0xFBF4
        )  # uniFBF4	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH YU ISOLATED FORM
        chars.append(
            0xFBF5
        )  # uniFBF5	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH YU FINAL FORM
        chars.append(
            0xFBF6
        )  # uniFBF6	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH E ISOLATED FORM
        chars.append(
            0xFBF7
        )  # uniFBF7	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH E FINAL FORM
        chars.append(
            0xFBF8
        )  # uniFBF8	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH E INITIAL FORM
        chars.append(
            0xFBF9
        )  # uniFBF9	ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH HAMZA ABOVE WITH ALEF MAKSURA ISOLATED FORM
        chars.append(
            0xFBFA
        )  # uniFBFA	ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH HAMZA ABOVE WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFBFB
        )  # uniFBFB	ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH HAMZA ABOVE WITH ALEF MAKSURA INITIAL FORM
        chars.append(0xFBFC)  # uni06CC	ARABIC LETTER FARSI YEH ISOLATED FORM
        chars.append(0xFBFD)  # uniFBFD	ARABIC LETTER FARSI YEH FINAL FORM
        chars.append(0xFBFE)  # uniFBFE	ARABIC LETTER FARSI YEH INITIAL FORM
        chars.append(0xFBFF)  # uniFBFF	ARABIC LETTER FARSI YEH MEDIAL FORM
        chars.append(
            0xFC00
        )  # uniFC00	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH JEEM ISOLATED FORM
        chars.append(
            0xFC01
        )  # uniFC01	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH HAH ISOLATED FORM
        chars.append(
            0xFC02
        )  # uniFC02	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH MEEM ISOLATED FORM
        chars.append(0x08AB)  # uni08AB	????
        chars.append(
            0xFC04
        )  # uniFC04	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH YEH ISOLATED FORM
        chars.append(0xFC05)  # uniFC05	ARABIC LIGATURE BEH WITH JEEM ISOLATED FORM
        chars.append(0xFC06)  # uniFC06	ARABIC LIGATURE BEH WITH HAH ISOLATED FORM
        chars.append(0xFC07)  # uniFC07	ARABIC LIGATURE BEH WITH KHAH ISOLATED FORM
        chars.append(0xFC08)  # uniFC08	ARABIC LIGATURE BEH WITH MEEM ISOLATED FORM
        chars.append(
            0xFC09
        )  # uniFC09	ARABIC LIGATURE BEH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC0A)  # uniFC0A	ARABIC LIGATURE BEH WITH YEH ISOLATED FORM
        chars.append(0xFC0B)  # uniFC0B	ARABIC LIGATURE TEH WITH JEEM ISOLATED FORM
        chars.append(0xFC0C)  # uniFC0C	ARABIC LIGATURE TEH WITH HAH ISOLATED FORM
        chars.append(0xFC0D)  # uniFC0D	ARABIC LIGATURE TEH WITH KHAH ISOLATED FORM
        chars.append(0xFC0E)  # uniFC0E	ARABIC LIGATURE TEH WITH MEEM ISOLATED FORM
        chars.append(
            0xFC0F
        )  # uniFC0F	ARABIC LIGATURE TEH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC10)  # uniFC10	ARABIC LIGATURE TEH WITH YEH ISOLATED FORM
        chars.append(0xFC11)  # uniFC11	ARABIC LIGATURE THEH WITH JEEM ISOLATED FORM
        chars.append(0xFC12)  # uniFC12	ARABIC LIGATURE THEH WITH MEEM ISOLATED FORM
        chars.append(
            0xFC13
        )  # uniFC13	ARABIC LIGATURE THEH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC14)  # uniFC14	ARABIC LIGATURE THEH WITH YEH ISOLATED FORM
        chars.append(0xFC15)  # uniFC15	ARABIC LIGATURE JEEM WITH HAH ISOLATED FORM
        chars.append(0xFC16)  # uniFC16	ARABIC LIGATURE JEEM WITH MEEM ISOLATED FORM
        chars.append(0xFC17)  # uniFC17	ARABIC LIGATURE HAH WITH JEEM ISOLATED FORM
        chars.append(0xFC18)  # uniFC18	ARABIC LIGATURE HAH WITH MEEM ISOLATED FORM
        chars.append(0xFC19)  # uniFC19	ARABIC LIGATURE KHAH WITH JEEM ISOLATED FORM
        chars.append(0xFC1A)  # uniFC1A	ARABIC LIGATURE KHAH WITH HAH ISOLATED FORM
        chars.append(0xFC1B)  # uniFC1B	ARABIC LIGATURE KHAH WITH MEEM ISOLATED FORM
        chars.append(0xFC1C)  # uniFC1C	ARABIC LIGATURE SEEN WITH JEEM ISOLATED FORM
        chars.append(0xFC1D)  # uniFC1D	ARABIC LIGATURE SEEN WITH HAH ISOLATED FORM
        chars.append(0xFC1E)  # uniFC1E	ARABIC LIGATURE SEEN WITH KHAH ISOLATED FORM
        chars.append(0xFC1F)  # uniFC1F	ARABIC LIGATURE SEEN WITH MEEM ISOLATED FORM
        chars.append(0xFC20)  # uniFC20	ARABIC LIGATURE SAD WITH HAH ISOLATED FORM
        chars.append(0xFC21)  # uniFC21	ARABIC LIGATURE SAD WITH MEEM ISOLATED FORM
        chars.append(0xFC22)  # uniFC22	ARABIC LIGATURE DAD WITH JEEM ISOLATED FORM
        chars.append(0xFC23)  # uniFC23	ARABIC LIGATURE DAD WITH HAH ISOLATED FORM
        chars.append(0xFC24)  # uniFC24	ARABIC LIGATURE DAD WITH KHAH ISOLATED FORM
        chars.append(0xFC25)  # uniFC25	ARABIC LIGATURE DAD WITH MEEM ISOLATED FORM
        chars.append(0xFC26)  # uniFC26	ARABIC LIGATURE TAH WITH HAH ISOLATED FORM
        chars.append(0xFC27)  # uniFC27	ARABIC LIGATURE TAH WITH MEEM ISOLATED FORM
        chars.append(0xFC28)  # uniFC28	ARABIC LIGATURE ZAH WITH MEEM ISOLATED FORM
        chars.append(0xFC29)  # uniFC29	ARABIC LIGATURE AIN WITH JEEM ISOLATED FORM
        chars.append(0xFC2A)  # uniFC2A	ARABIC LIGATURE AIN WITH MEEM ISOLATED FORM
        chars.append(0xFC2B)  # uniFC2B	ARABIC LIGATURE GHAIN WITH JEEM ISOLATED FORM
        chars.append(0xFC2C)  # uniFC2C	ARABIC LIGATURE GHAIN WITH MEEM ISOLATED FORM
        chars.append(0xFC2D)  # uniFC2D	ARABIC LIGATURE FEH WITH JEEM ISOLATED FORM
        chars.append(0xFC2E)  # uniFC2E	ARABIC LIGATURE FEH WITH HAH ISOLATED FORM
        chars.append(0xFC2F)  # uniFC2F	ARABIC LIGATURE FEH WITH KHAH ISOLATED FORM
        chars.append(0xFC30)  # uniFC30	ARABIC LIGATURE FEH WITH MEEM ISOLATED FORM
        chars.append(
            0xFC31
        )  # uniFC31	ARABIC LIGATURE FEH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC32)  # uniFC32	ARABIC LIGATURE FEH WITH YEH ISOLATED FORM
        chars.append(0xFC33)  # uniFC33	ARABIC LIGATURE QAF WITH HAH ISOLATED FORM
        chars.append(0xFC34)  # uniFC34	ARABIC LIGATURE QAF WITH MEEM ISOLATED FORM
        chars.append(
            0xFC35
        )  # uniFC35	ARABIC LIGATURE QAF WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC36)  # uniFC36	ARABIC LIGATURE QAF WITH YEH ISOLATED FORM
        chars.append(0xFC37)  # uniFC37	ARABIC LIGATURE KAF WITH ALEF ISOLATED FORM
        chars.append(0xFC38)  # uniFC38	ARABIC LIGATURE KAF WITH JEEM ISOLATED FORM
        chars.append(0xFC39)  # uniFC39	ARABIC LIGATURE KAF WITH HAH ISOLATED FORM
        chars.append(0xFC3A)  # uniFC3A	ARABIC LIGATURE KAF WITH KHAH ISOLATED FORM
        chars.append(0xFC3B)  # uniFC3B	ARABIC LIGATURE KAF WITH LAM ISOLATED FORM
        chars.append(0xFC3C)  # uniFC3C	ARABIC LIGATURE KAF WITH MEEM ISOLATED FORM
        chars.append(
            0xFC3D
        )  # uniFC3D	ARABIC LIGATURE KAF WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC3E)  # uniFC3E	ARABIC LIGATURE KAF WITH YEH ISOLATED FORM
        chars.append(0xFC3F)  # uniFC3F	ARABIC LIGATURE LAM WITH JEEM ISOLATED FORM
        chars.append(0xFC40)  # uniFC40	ARABIC LIGATURE LAM WITH HAH ISOLATED FORM
        chars.append(0xFC41)  # uniFC41	ARABIC LIGATURE LAM WITH KHAH ISOLATED FORM
        chars.append(0xFC42)  # uniFC42	ARABIC LIGATURE LAM WITH MEEM ISOLATED FORM
        chars.append(
            0xFC43
        )  # uniFC43	ARABIC LIGATURE LAM WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC44)  # uniFC44	ARABIC LIGATURE LAM WITH YEH ISOLATED FORM
        chars.append(0xFC45)  # uniFC45	ARABIC LIGATURE MEEM WITH JEEM ISOLATED FORM
        chars.append(0xFC46)  # uniFC46	ARABIC LIGATURE MEEM WITH HAH ISOLATED FORM
        chars.append(0xFC47)  # uniFC47	ARABIC LIGATURE MEEM WITH KHAH ISOLATED FORM
        chars.append(0xFC48)  # uniFC48	ARABIC LIGATURE MEEM WITH MEEM ISOLATED FORM
        chars.append(
            0xFC49
        )  # uniFC49	ARABIC LIGATURE MEEM WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC4A)  # uniFC4A	ARABIC LIGATURE MEEM WITH YEH ISOLATED FORM
        chars.append(0xFC4B)  # uniFC4B	ARABIC LIGATURE NOON WITH JEEM ISOLATED FORM
        chars.append(0xFC4C)  # uniFC4C	ARABIC LIGATURE NOON WITH HAH ISOLATED FORM
        chars.append(0xFC4D)  # uniFC4D	ARABIC LIGATURE NOON WITH KHAH ISOLATED FORM
        chars.append(0xFC4E)  # uniFC4E	ARABIC LIGATURE NOON WITH MEEM ISOLATED FORM
        chars.append(
            0xFC4F
        )  # uniFC4F	ARABIC LIGATURE NOON WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC50)  # uniFC50	ARABIC LIGATURE NOON WITH YEH ISOLATED FORM
        chars.append(0xFC51)  # uniFC51	ARABIC LIGATURE HEH WITH JEEM ISOLATED FORM
        chars.append(0xFC52)  # uniFC52	ARABIC LIGATURE HEH WITH MEEM ISOLATED FORM
        chars.append(
            0xFC53
        )  # uniFC53	ARABIC LIGATURE HEH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC54)  # uniFC54	ARABIC LIGATURE HEH WITH YEH ISOLATED FORM
        chars.append(0xFC55)  # uniFC55	ARABIC LIGATURE YEH WITH JEEM ISOLATED FORM
        chars.append(0xFC56)  # uniFC56	ARABIC LIGATURE YEH WITH HAH ISOLATED FORM
        chars.append(0xFC57)  # uniFC57	ARABIC LIGATURE YEH WITH KHAH ISOLATED FORM
        chars.append(0xFC58)  # uniFC58	ARABIC LIGATURE YEH WITH MEEM ISOLATED FORM
        chars.append(
            0xFC59
        )  # uniFC59	ARABIC LIGATURE YEH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFC5A)  # uniFC5A	ARABIC LIGATURE YEH WITH YEH ISOLATED FORM
        chars.append(
            0xFC5B
        )  # uniFC5B	ARABIC LIGATURE THAL WITH SUPERSCRIPT ALEF ISOLATED FORM
        chars.append(
            0xFC5C
        )  # uniFC5C	ARABIC LIGATURE REH WITH SUPERSCRIPT ALEF ISOLATED FORM
        chars.append(
            0xFC5D
        )  # uniFC5D	ARABIC LIGATURE ALEF MAKSURA WITH SUPERSCRIPT ALEF ISOLATED FORM
        chars.append(
            0xFC5E
        )  # uniFC5E	ARABIC LIGATURE SHADDA WITH DAMMATAN ISOLATED FORM
        chars.append(
            0xFC5F
        )  # uniFC5F	ARABIC LIGATURE SHADDA WITH KASRATAN ISOLATED FORM
        chars.append(
            0xFC60
        )  # uniFC60	ARABIC LIGATURE SHADDA WITH FATHA ISOLATED FORM
        chars.append(
            0xFC61
        )  # uniFC61	ARABIC LIGATURE SHADDA WITH DAMMA ISOLATED FORM
        chars.append(
            0xFC62
        )  # uniFC62	ARABIC LIGATURE SHADDA WITH KASRA ISOLATED FORM
        chars.append(
            0xFC63
        )  # uniFC63	ARABIC LIGATURE SHADDA WITH SUPERSCRIPT ALEF ISOLATED FORM
        chars.append(
            0xFC64
        )  # uniFC64	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH REH FINAL FORM
        chars.append(
            0xFC65
        )  # uniFC65	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH ZAIN FINAL FORM
        chars.append(
            0xFC66
        )  # uniFC66	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH MEEM FINAL FORM
        chars.append(
            0xFC67
        )  # uniFC67	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH NOON FINAL FORM
        chars.append(
            0xFC68
        )  # uniFC68	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFC69
        )  # uniFC69	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH YEH FINAL FORM
        chars.append(0xFC6A)  # uniFC6A	ARABIC LIGATURE BEH WITH REH FINAL FORM
        chars.append(0xFC6B)  # uniFC6B	ARABIC LIGATURE BEH WITH ZAIN FINAL FORM
        chars.append(0xFC6C)  # uniFC6C	ARABIC LIGATURE BEH WITH MEEM FINAL FORM
        chars.append(0xFC6D)  # uniFC6D	ARABIC LIGATURE BEH WITH NOON FINAL FORM
        chars.append(
            0xFC6E
        )  # uniFC6E	ARABIC LIGATURE BEH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC6F)  # uniFC6F	ARABIC LIGATURE BEH WITH YEH FINAL FORM
        chars.append(0xFC70)  # uniFC70	ARABIC LIGATURE TEH WITH REH FINAL FORM
        chars.append(0xFC71)  # uniFC71	ARABIC LIGATURE TEH WITH ZAIN FINAL FORM
        chars.append(0xFC72)  # uniFC72	ARABIC LIGATURE TEH WITH MEEM FINAL FORM
        chars.append(0xFC73)  # uniFC73	ARABIC LIGATURE TEH WITH NOON FINAL FORM
        chars.append(
            0xFC74
        )  # uniFC74	ARABIC LIGATURE TEH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC75)  # uniFC75	ARABIC LIGATURE TEH WITH YEH FINAL FORM
        chars.append(0xFC76)  # uniFC76	ARABIC LIGATURE THEH WITH REH FINAL FORM
        chars.append(0xFC77)  # uniFC77	ARABIC LIGATURE THEH WITH ZAIN FINAL FORM
        chars.append(0xFC78)  # uniFC78	ARABIC LIGATURE THEH WITH MEEM FINAL FORM
        chars.append(0xFC79)  # uniFC79	ARABIC LIGATURE THEH WITH NOON FINAL FORM
        chars.append(
            0xFC7A
        )  # uniFC7A	ARABIC LIGATURE THEH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC7B)  # uniFC7B	ARABIC LIGATURE THEH WITH YEH FINAL FORM
        chars.append(
            0xFC7C
        )  # uniFC7C	ARABIC LIGATURE FEH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC7D)  # uniFC7D	ARABIC LIGATURE FEH WITH YEH FINAL FORM
        chars.append(
            0xFC7E
        )  # uniFC7E	ARABIC LIGATURE QAF WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC7F)  # uniFC7F	ARABIC LIGATURE QAF WITH YEH FINAL FORM
        chars.append(0xFC80)  # uniFC80	ARABIC LIGATURE KAF WITH ALEF FINAL FORM
        chars.append(0xFC81)  # uniFC81	ARABIC LIGATURE KAF WITH LAM FINAL FORM
        chars.append(0xFC82)  # uniFC82	ARABIC LIGATURE KAF WITH MEEM FINAL FORM
        chars.append(
            0xFC83
        )  # uniFC83	ARABIC LIGATURE KAF WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC84)  # uniFC84	ARABIC LIGATURE KAF WITH YEH FINAL FORM
        chars.append(0xFC85)  # uniFC85	ARABIC LIGATURE LAM WITH MEEM FINAL FORM
        chars.append(
            0xFC86
        )  # uniFC86	ARABIC LIGATURE LAM WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC87)  # uniFC87	ARABIC LIGATURE LAM WITH YEH FINAL FORM
        chars.append(0xFC88)  # uniFC88	ARABIC LIGATURE MEEM WITH ALEF FINAL FORM
        chars.append(0xFC89)  # uniFC89	ARABIC LIGATURE MEEM WITH MEEM FINAL FORM
        chars.append(0xFC8A)  # uniFC8A	ARABIC LIGATURE NOON WITH REH FINAL FORM
        chars.append(0xFC8B)  # uniFC8B	ARABIC LIGATURE NOON WITH ZAIN FINAL FORM
        chars.append(0xFC8C)  # uniFC8C	ARABIC LIGATURE NOON WITH MEEM FINAL FORM
        chars.append(0xFC8D)  # uniFC8D	ARABIC LIGATURE NOON WITH NOON FINAL FORM
        chars.append(
            0xFC8E
        )  # uniFC8E	ARABIC LIGATURE NOON WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC8F)  # uniFC8F	ARABIC LIGATURE NOON WITH YEH FINAL FORM
        chars.append(
            0xFC90
        )  # uniFC90	ARABIC LIGATURE ALEF MAKSURA WITH SUPERSCRIPT ALEF FINAL FORM
        chars.append(0xFC91)  # uniFC91	ARABIC LIGATURE YEH WITH REH FINAL FORM
        chars.append(0xFC92)  # uniFC92	ARABIC LIGATURE YEH WITH ZAIN FINAL FORM
        chars.append(0xFC93)  # uniFC93	ARABIC LIGATURE YEH WITH MEEM FINAL FORM
        chars.append(0xFC94)  # uniFC94	ARABIC LIGATURE YEH WITH NOON FINAL FORM
        chars.append(
            0xFC95
        )  # uniFC95	ARABIC LIGATURE YEH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFC96)  # uniFC96	ARABIC LIGATURE YEH WITH YEH FINAL FORM
        chars.append(
            0xFC97
        )  # uniFC97	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH JEEM INITIAL FORM
        chars.append(
            0xFC98
        )  # uniFC98	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH HAH INITIAL FORM
        chars.append(
            0xFC99
        )  # uniFC99	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH KHAH INITIAL FORM
        chars.append(
            0xFC9A
        )  # uniFC9A	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH MEEM INITIAL FORM
        chars.append(
            0xFC9B
        )  # uniFC9B	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH HEH INITIAL FORM
        chars.append(0xFC9C)  # uniFC9C	ARABIC LIGATURE BEH WITH JEEM INITIAL FORM
        chars.append(0xFC9D)  # uniFC9D	ARABIC LIGATURE BEH WITH HAH INITIAL FORM
        chars.append(0xFC9E)  # uniFC9E	ARABIC LIGATURE BEH WITH KHAH INITIAL FORM
        chars.append(0xFC9F)  # uniFC9F	ARABIC LIGATURE BEH WITH MEEM INITIAL FORM
        chars.append(0xFCA0)  # uniFCA0	ARABIC LIGATURE BEH WITH HEH INITIAL FORM
        chars.append(0xFCA1)  # uniFCA1	ARABIC LIGATURE TEH WITH JEEM INITIAL FORM
        chars.append(0xFCA2)  # uniFCA2	ARABIC LIGATURE TEH WITH HAH INITIAL FORM
        chars.append(0xFCA3)  # uniFCA3	ARABIC LIGATURE TEH WITH KHAH INITIAL FORM
        chars.append(0xFCA4)  # uniFCA4	ARABIC LIGATURE TEH WITH MEEM INITIAL FORM
        chars.append(0xFCA5)  # uniFCA5	ARABIC LIGATURE TEH WITH HEH INITIAL FORM
        chars.append(0xFCA6)  # uniFCA6	ARABIC LIGATURE THEH WITH MEEM INITIAL FORM
        chars.append(0xFCA7)  # uniFCA7	ARABIC LIGATURE JEEM WITH HAH INITIAL FORM
        chars.append(0xFCA8)  # uniFCA8	ARABIC LIGATURE JEEM WITH MEEM INITIAL FORM
        chars.append(0xFCA9)  # uniFCA9	ARABIC LIGATURE HAH WITH JEEM INITIAL FORM
        chars.append(0xFCAA)  # uniFCAA	ARABIC LIGATURE HAH WITH MEEM INITIAL FORM
        chars.append(0xFCAB)  # uniFCAB	ARABIC LIGATURE KHAH WITH JEEM INITIAL FORM
        chars.append(0xFCAC)  # uniFCAC	ARABIC LIGATURE KHAH WITH MEEM INITIAL FORM
        chars.append(0xFCAD)  # uniFCAD	ARABIC LIGATURE SEEN WITH JEEM INITIAL FORM
        chars.append(0xFCAE)  # uniFCAE	ARABIC LIGATURE SEEN WITH HAH INITIAL FORM
        chars.append(0xFCAF)  # uniFCAF	ARABIC LIGATURE SEEN WITH KHAH INITIAL FORM
        chars.append(0xFCB0)  # uniFCB0	ARABIC LIGATURE SEEN WITH MEEM INITIAL FORM
        chars.append(0xFCB1)  # uniFCB1	ARABIC LIGATURE SAD WITH HAH INITIAL FORM
        chars.append(0xFCB2)  # uniFCB2	ARABIC LIGATURE SAD WITH KHAH INITIAL FORM
        chars.append(0xFCB3)  # uniFCB3	ARABIC LIGATURE SAD WITH MEEM INITIAL FORM
        chars.append(0xFCB4)  # uniFCB4	ARABIC LIGATURE DAD WITH JEEM INITIAL FORM
        chars.append(0xFCB5)  # uniFCB5	ARABIC LIGATURE DAD WITH HAH INITIAL FORM
        chars.append(0xFCB6)  # uniFCB6	ARABIC LIGATURE DAD WITH KHAH INITIAL FORM
        chars.append(0xFCB7)  # uniFCB7	ARABIC LIGATURE DAD WITH MEEM INITIAL FORM
        chars.append(0xFCB8)  # uniFCB8	ARABIC LIGATURE TAH WITH HAH INITIAL FORM
        chars.append(0xFCB9)  # uniFCB9	ARABIC LIGATURE ZAH WITH MEEM INITIAL FORM
        chars.append(0xFCBA)  # uniFCBA	ARABIC LIGATURE AIN WITH JEEM INITIAL FORM
        chars.append(0xFCBB)  # uniFCBB	ARABIC LIGATURE AIN WITH MEEM INITIAL FORM
        chars.append(0xFCBC)  # uniFCBC	ARABIC LIGATURE GHAIN WITH JEEM INITIAL FORM
        chars.append(0xFCBD)  # uniFCBD	ARABIC LIGATURE GHAIN WITH MEEM INITIAL FORM
        chars.append(0xFCBE)  # uniFCBE	ARABIC LIGATURE FEH WITH JEEM INITIAL FORM
        chars.append(0xFCBF)  # uniFCBF	ARABIC LIGATURE FEH WITH HAH INITIAL FORM
        chars.append(0xFCC0)  # uniFCC0	ARABIC LIGATURE FEH WITH KHAH INITIAL FORM
        chars.append(0xFCC1)  # uniFCC1	ARABIC LIGATURE FEH WITH MEEM INITIAL FORM
        chars.append(0xFCC2)  # uniFCC2	ARABIC LIGATURE QAF WITH HAH INITIAL FORM
        chars.append(0xFCC3)  # uniFCC3	ARABIC LIGATURE QAF WITH MEEM INITIAL FORM
        chars.append(0xFCC4)  # uniFCC4	ARABIC LIGATURE KAF WITH JEEM INITIAL FORM
        chars.append(0xFCC5)  # uniFCC5	ARABIC LIGATURE KAF WITH HAH INITIAL FORM
        chars.append(0xFCC6)  # uniFCC6	ARABIC LIGATURE KAF WITH KHAH INITIAL FORM
        chars.append(0xFCC7)  # uniFCC7	ARABIC LIGATURE KAF WITH LAM INITIAL FORM
        chars.append(0xFCC8)  # uniFCC8	ARABIC LIGATURE KAF WITH MEEM INITIAL FORM
        chars.append(0xFCC9)  # uniFCC9	ARABIC LIGATURE LAM WITH JEEM INITIAL FORM
        chars.append(0xFCCA)  # uniFCCA	ARABIC LIGATURE LAM WITH HAH INITIAL FORM
        chars.append(0xFCCB)  # uniFCCB	ARABIC LIGATURE LAM WITH KHAH INITIAL FORM
        chars.append(0xFCCC)  # uniFCCC	ARABIC LIGATURE LAM WITH MEEM INITIAL FORM
        chars.append(0xFCCD)  # uniFCCD	ARABIC LIGATURE LAM WITH HEH INITIAL FORM
        chars.append(0xFCCE)  # uniFCCE	ARABIC LIGATURE MEEM WITH JEEM INITIAL FORM
        chars.append(0xFCCF)  # uniFCCF	ARABIC LIGATURE MEEM WITH HAH INITIAL FORM
        chars.append(0xFCD0)  # uniFCD0	ARABIC LIGATURE MEEM WITH KHAH INITIAL FORM
        chars.append(0xFCD1)  # uniFCD1	ARABIC LIGATURE MEEM WITH MEEM INITIAL FORM
        chars.append(0xFCD2)  # uniFCD2	ARABIC LIGATURE NOON WITH JEEM INITIAL FORM
        chars.append(0xFCD3)  # uniFCD3	ARABIC LIGATURE NOON WITH HAH INITIAL FORM
        chars.append(0xFCD4)  # uniFCD4	ARABIC LIGATURE NOON WITH KHAH INITIAL FORM
        chars.append(0xFCD5)  # uniFCD5	ARABIC LIGATURE NOON WITH MEEM INITIAL FORM
        chars.append(0xFCD6)  # uniFCD6	ARABIC LIGATURE NOON WITH HEH INITIAL FORM
        chars.append(0xFCD7)  # uniFCD7	ARABIC LIGATURE HEH WITH JEEM INITIAL FORM
        chars.append(0xFCD8)  # uniFCD8	ARABIC LIGATURE HEH WITH MEEM INITIAL FORM
        chars.append(
            0xFCD9
        )  # uniFCD9	ARABIC LIGATURE HEH WITH SUPERSCRIPT ALEF INITIAL FORM
        chars.append(0xFCDA)  # uniFCDA	ARABIC LIGATURE YEH WITH JEEM INITIAL FORM
        chars.append(0xFCDB)  # uniFCDB	ARABIC LIGATURE YEH WITH HAH INITIAL FORM
        chars.append(0xFCDC)  # uniFCDC	ARABIC LIGATURE YEH WITH KHAH INITIAL FORM
        chars.append(0xFCDD)  # uniFCDD	ARABIC LIGATURE YEH WITH MEEM INITIAL FORM
        chars.append(0xFCDE)  # uniFCDE	ARABIC LIGATURE YEH WITH HEH INITIAL FORM
        chars.append(
            0xFCDF
        )  # uniFCDF	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH MEEM MEDIAL FORM
        chars.append(
            0xFCE0
        )  # uniFCE0	ARABIC LIGATURE YEH WITH HAMZA ABOVE WITH HEH MEDIAL FORM
        chars.append(0xFCE1)  # uniFCE1	ARABIC LIGATURE BEH WITH MEEM MEDIAL FORM
        chars.append(0xFCE2)  # uniFCE2	ARABIC LIGATURE BEH WITH HEH MEDIAL FORM
        chars.append(0xFCE3)  # uniFCE3	ARABIC LIGATURE TEH WITH MEEM MEDIAL FORM
        chars.append(0xFCE4)  # uniFCE4	ARABIC LIGATURE TEH WITH HEH MEDIAL FORM
        chars.append(0xFCE5)  # uniFCE5	ARABIC LIGATURE THEH WITH MEEM MEDIAL FORM
        chars.append(0xFCE6)  # uniFCE6	ARABIC LIGATURE THEH WITH HEH MEDIAL FORM
        chars.append(0xFCE7)  # uniFCE7	ARABIC LIGATURE SEEN WITH MEEM MEDIAL FORM
        chars.append(0xFCE8)  # uniFCE8	ARABIC LIGATURE SEEN WITH HEH MEDIAL FORM
        chars.append(0xFCE9)  # uniFCE9	ARABIC LIGATURE SHEEN WITH MEEM MEDIAL FORM
        chars.append(0xFCEA)  # uniFCEA	ARABIC LIGATURE SHEEN WITH HEH MEDIAL FORM
        chars.append(0xFCEB)  # uniFCEB	ARABIC LIGATURE KAF WITH LAM MEDIAL FORM
        chars.append(0xFCEC)  # uniFCEC	ARABIC LIGATURE KAF WITH MEEM MEDIAL FORM
        chars.append(0xFCED)  # uniFCED	ARABIC LIGATURE LAM WITH MEEM MEDIAL FORM
        chars.append(0xFCEE)  # uniFCEE	ARABIC LIGATURE NOON WITH MEEM MEDIAL FORM
        chars.append(0xFCEF)  # uniFCEF	ARABIC LIGATURE NOON WITH HEH MEDIAL FORM
        chars.append(0xFCF0)  # uniFCF0	ARABIC LIGATURE YEH WITH MEEM MEDIAL FORM
        chars.append(0xFCF1)  # uniFCF1	ARABIC LIGATURE YEH WITH HEH MEDIAL FORM
        chars.append(0xFCF2)  # uniFCF2	ARABIC LIGATURE SHADDA WITH FATHA MEDIAL FORM
        chars.append(0xFCF3)  # uniFCF3	ARABIC LIGATURE SHADDA WITH DAMMA MEDIAL FORM
        chars.append(0xFCF4)  # uniFCF4	ARABIC LIGATURE SHADDA WITH KASRA MEDIAL FORM
        chars.append(
            0xFCF5
        )  # uniFCF5	ARABIC LIGATURE TAH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFCF6)  # uniFCF6	ARABIC LIGATURE TAH WITH YEH ISOLATED FORM
        chars.append(
            0xFCF7
        )  # uniFCF7	ARABIC LIGATURE AIN WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFCF8)  # uniFCF8	ARABIC LIGATURE AIN WITH YEH ISOLATED FORM
        chars.append(
            0xFCF9
        )  # uniFCF9	ARABIC LIGATURE GHAIN WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFCFA)  # uniFCFA	ARABIC LIGATURE GHAIN WITH YEH ISOLATED FORM
        chars.append(
            0xFCFB
        )  # uniFCFB	ARABIC LIGATURE SEEN WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFCFC)  # uniFCFC	ARABIC LIGATURE SEEN WITH YEH ISOLATED FORM
        chars.append(
            0xFCFD
        )  # uniFCFD	ARABIC LIGATURE SHEEN WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFCFE)  # uniFCFE	ARABIC LIGATURE SHEEN WITH YEH ISOLATED FORM
        chars.append(
            0xFCFF
        )  # uniFCFF	ARABIC LIGATURE HAH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFD00)  # uniFD00	ARABIC LIGATURE HAH WITH YEH ISOLATED FORM
        chars.append(
            0xFD01
        )  # uniFD01	ARABIC LIGATURE JEEM WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFD02)  # uniFD02	ARABIC LIGATURE JEEM WITH YEH ISOLATED FORM
        chars.append(
            0xFD03
        )  # uniFD03	ARABIC LIGATURE KHAH WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFD04)  # uniFD04	ARABIC LIGATURE KHAH WITH YEH ISOLATED FORM
        chars.append(
            0xFD05
        )  # uniFD05	ARABIC LIGATURE SAD WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFD06)  # uniFD06	ARABIC LIGATURE SAD WITH YEH ISOLATED FORM
        chars.append(
            0xFD07
        )  # uniFD07	ARABIC LIGATURE DAD WITH ALEF MAKSURA ISOLATED FORM
        chars.append(0xFD08)  # uniFD08	ARABIC LIGATURE DAD WITH YEH ISOLATED FORM
        chars.append(0xFD09)  # uniFD09	ARABIC LIGATURE SHEEN WITH JEEM ISOLATED FORM
        chars.append(0xFD0A)  # uniFD0A	ARABIC LIGATURE SHEEN WITH HAH ISOLATED FORM
        chars.append(0xFD0B)  # uniFD0B	ARABIC LIGATURE SHEEN WITH KHAH ISOLATED FORM
        chars.append(0xFD0C)  # uniFD0C	ARABIC LIGATURE SHEEN WITH MEEM ISOLATED FORM
        chars.append(0xFD0D)  # uniFD0D	ARABIC LIGATURE SHEEN WITH REH ISOLATED FORM
        chars.append(0xFD0E)  # uniFD0E	ARABIC LIGATURE SEEN WITH REH ISOLATED FORM
        chars.append(0xFD0F)  # uniFD0F	ARABIC LIGATURE SAD WITH REH ISOLATED FORM
        chars.append(0xFD10)  # uniFD10	ARABIC LIGATURE DAD WITH REH ISOLATED FORM
        chars.append(
            0xFD11
        )  # uniFD11	ARABIC LIGATURE TAH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD12)  # uniFD12	ARABIC LIGATURE TAH WITH YEH FINAL FORM
        chars.append(
            0xFD13
        )  # uniFD13	ARABIC LIGATURE AIN WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD14)  # uniFD14	ARABIC LIGATURE AIN WITH YEH FINAL FORM
        chars.append(
            0xFD15
        )  # uniFD15	ARABIC LIGATURE GHAIN WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD16)  # uniFD16	ARABIC LIGATURE GHAIN WITH YEH FINAL FORM
        chars.append(
            0xFD17
        )  # uniFD17	ARABIC LIGATURE SEEN WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD18)  # uniFD18	ARABIC LIGATURE SEEN WITH YEH FINAL FORM
        chars.append(
            0xFD19
        )  # uniFD19	ARABIC LIGATURE SHEEN WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD1A)  # uniFD1A	ARABIC LIGATURE SHEEN WITH YEH FINAL FORM
        chars.append(
            0xFD1B
        )  # uniFD1B	ARABIC LIGATURE HAH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD1C)  # uniFD1C	ARABIC LIGATURE HAH WITH YEH FINAL FORM
        chars.append(
            0xFD1D
        )  # uniFD1D	ARABIC LIGATURE JEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD1E)  # uniFD1E	ARABIC LIGATURE JEEM WITH YEH FINAL FORM
        chars.append(
            0xFD1F
        )  # uniFD1F	ARABIC LIGATURE KHAH WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD20)  # uniFD20	ARABIC LIGATURE KHAH WITH YEH FINAL FORM
        chars.append(
            0xFD21
        )  # uniFD21	ARABIC LIGATURE SAD WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD22)  # uniFD22	ARABIC LIGATURE SAD WITH YEH FINAL FORM
        chars.append(
            0xFD23
        )  # uniFD23	ARABIC LIGATURE DAD WITH ALEF MAKSURA FINAL FORM
        chars.append(0xFD24)  # uniFD24	ARABIC LIGATURE DAD WITH YEH FINAL FORM
        chars.append(0xFD25)  # uniFD25	ARABIC LIGATURE SHEEN WITH JEEM FINAL FORM
        chars.append(0xFD26)  # uniFD26	ARABIC LIGATURE SHEEN WITH HAH FINAL FORM
        chars.append(0xFD27)  # uniFD27	ARABIC LIGATURE SHEEN WITH KHAH FINAL FORM
        chars.append(0xFD28)  # uniFD28	ARABIC LIGATURE SHEEN WITH MEEM FINAL FORM
        chars.append(0xFD29)  # uniFD29	ARABIC LIGATURE SHEEN WITH REH FINAL FORM
        chars.append(0xFD2A)  # uniFD2A	ARABIC LIGATURE SEEN WITH REH FINAL FORM
        chars.append(0xFD2B)  # uniFD2B	ARABIC LIGATURE SAD WITH REH FINAL FORM
        chars.append(0xFD2C)  # uniFD2C	ARABIC LIGATURE DAD WITH REH FINAL FORM
        chars.append(0xFD2D)  # uniFD2D	ARABIC LIGATURE SHEEN WITH JEEM INITIAL FORM
        chars.append(0xFD2E)  # uniFD2E	ARABIC LIGATURE SHEEN WITH HAH INITIAL FORM
        chars.append(0xFD2F)  # uniFD2F	ARABIC LIGATURE SHEEN WITH KHAH INITIAL FORM
        chars.append(0xFD30)  # uniFD30	ARABIC LIGATURE SHEEN WITH MEEM INITIAL FORM
        chars.append(0xFD31)  # uniFD31	ARABIC LIGATURE SEEN WITH HEH INITIAL FORM
        chars.append(0xFD32)  # uniFD32	ARABIC LIGATURE SHEEN WITH HEH INITIAL FORM
        chars.append(0xFD33)  # uniFD33	ARABIC LIGATURE TAH WITH MEEM INITIAL FORM
        chars.append(0xFD34)  # uniFD34	ARABIC LIGATURE SEEN WITH JEEM MEDIAL FORM
        chars.append(0xFD35)  # uniFD35	ARABIC LIGATURE SEEN WITH HAH MEDIAL FORM
        chars.append(0xFD36)  # uniFD36	ARABIC LIGATURE SEEN WITH KHAH MEDIAL FORM
        chars.append(0xFD37)  # uniFD37	ARABIC LIGATURE SHEEN WITH JEEM MEDIAL FORM
        chars.append(0xFD38)  # uniFD38	ARABIC LIGATURE SHEEN WITH HAH MEDIAL FORM
        chars.append(0xFD39)  # uniFD39	ARABIC LIGATURE SHEEN WITH KHAH MEDIAL FORM
        chars.append(0xFD3A)  # uniFD3A	ARABIC LIGATURE TAH WITH MEEM MEDIAL FORM
        chars.append(0xFD3B)  # uniFD3B	ARABIC LIGATURE ZAH WITH MEEM MEDIAL FORM
        chars.append(0xFD3C)  # uniFD3C	ARABIC LIGATURE ALEF WITH FATHATAN FINAL FORM
        chars.append(
            0xFD3D
        )  # uniFD3D	ARABIC LIGATURE ALEF WITH FATHATAN ISOLATED FORM
        chars.append(0xFD3E)  # uniFD3E	ORNATE LEFT PARENTHESIS
        chars.append(0xFD3F)  # uniFD3F	ORNATE RIGHT PARENTHESIS
        chars.append(
            0xFD50
        )  # uniFD50	ARABIC LIGATURE TEH WITH JEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD51
        )  # uniFD51	ARABIC LIGATURE TEH WITH HAH WITH JEEM FINAL FORM
        chars.append(
            0xFD52
        )  # uniFD52	ARABIC LIGATURE TEH WITH HAH WITH JEEM INITIAL FORM
        chars.append(
            0xFD53
        )  # uniFD53	ARABIC LIGATURE TEH WITH HAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD54
        )  # uniFD54	ARABIC LIGATURE TEH WITH KHAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD55
        )  # uniFD55	ARABIC LIGATURE TEH WITH MEEM WITH JEEM INITIAL FORM
        chars.append(
            0xFD56
        )  # uniFD56	ARABIC LIGATURE TEH WITH MEEM WITH HAH INITIAL FORM
        chars.append(
            0xFD57
        )  # uniFD57	ARABIC LIGATURE TEH WITH MEEM WITH KHAH INITIAL FORM
        chars.append(
            0xFD58
        )  # uniFD58	ARABIC LIGATURE JEEM WITH MEEM WITH HAH FINAL FORM
        chars.append(
            0xFD59
        )  # uniFD59	ARABIC LIGATURE JEEM WITH MEEM WITH HAH INITIAL FORM
        chars.append(
            0xFD5A
        )  # uniFD5A	ARABIC LIGATURE HAH WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFD5B
        )  # uniFD5B	ARABIC LIGATURE HAH WITH MEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD5C
        )  # uniFD5C	ARABIC LIGATURE SEEN WITH HAH WITH JEEM INITIAL FORM
        chars.append(
            0xFD5D
        )  # uniFD5D	ARABIC LIGATURE SEEN WITH JEEM WITH HAH INITIAL FORM
        chars.append(
            0xFD5E
        )  # uniFD5E	ARABIC LIGATURE SEEN WITH JEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD5F
        )  # uniFD5F	ARABIC LIGATURE SEEN WITH MEEM WITH HAH FINAL FORM
        chars.append(
            0xFD60
        )  # uniFD60	ARABIC LIGATURE SEEN WITH MEEM WITH HAH INITIAL FORM
        chars.append(
            0xFD61
        )  # uniFD61	ARABIC LIGATURE SEEN WITH MEEM WITH JEEM INITIAL FORM
        chars.append(
            0xFD62
        )  # uniFD62	ARABIC LIGATURE SEEN WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD63
        )  # uniFD63	ARABIC LIGATURE SEEN WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD64
        )  # uniFD64	ARABIC LIGATURE SAD WITH HAH WITH HAH FINAL FORM
        chars.append(
            0xFD65
        )  # uniFD65	ARABIC LIGATURE SAD WITH HAH WITH HAH INITIAL FORM
        chars.append(
            0xFD66
        )  # uniFD66	ARABIC LIGATURE SAD WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD67
        )  # uniFD67	ARABIC LIGATURE SHEEN WITH HAH WITH MEEM FINAL FORM
        chars.append(
            0xFD68
        )  # uniFD68	ARABIC LIGATURE SHEEN WITH HAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD69
        )  # uniFD69	ARABIC LIGATURE SHEEN WITH JEEM WITH YEH FINAL FORM
        chars.append(
            0xFD6A
        )  # uniFD6A	ARABIC LIGATURE SHEEN WITH MEEM WITH KHAH FINAL FORM
        chars.append(
            0xFD6B
        )  # uniFD6B	ARABIC LIGATURE SHEEN WITH MEEM WITH KHAH INITIAL FORM
        chars.append(
            0xFD6C
        )  # uniFD6C	ARABIC LIGATURE SHEEN WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD6D
        )  # uniFD6D	ARABIC LIGATURE SHEEN WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD6E
        )  # uniFD6E	ARABIC LIGATURE DAD WITH HAH WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD6F
        )  # uniFD6F	ARABIC LIGATURE DAD WITH KHAH WITH MEEM FINAL FORM
        chars.append(
            0xFD70
        )  # uniFD70	ARABIC LIGATURE DAD WITH KHAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD71
        )  # uniFD71	ARABIC LIGATURE TAH WITH MEEM WITH HAH FINAL FORM
        chars.append(
            0xFD72
        )  # uniFD72	ARABIC LIGATURE TAH WITH MEEM WITH HAH INITIAL FORM
        chars.append(
            0xFD73
        )  # uniFD73	ARABIC LIGATURE TAH WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD74
        )  # uniFD74	ARABIC LIGATURE TAH WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFD75
        )  # uniFD75	ARABIC LIGATURE AIN WITH JEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD76
        )  # uniFD76	ARABIC LIGATURE AIN WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD77
        )  # uniFD77	ARABIC LIGATURE AIN WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD78
        )  # uniFD78	ARABIC LIGATURE AIN WITH MEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD79
        )  # uniFD79	ARABIC LIGATURE GHAIN WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD7A
        )  # uniFD7A	ARABIC LIGATURE GHAIN WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFD7B
        )  # uniFD7B	ARABIC LIGATURE GHAIN WITH MEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD7C
        )  # uniFD7C	ARABIC LIGATURE FEH WITH KHAH WITH MEEM FINAL FORM
        chars.append(
            0xFD7D
        )  # uniFD7D	ARABIC LIGATURE FEH WITH KHAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD7E
        )  # uniFD7E	ARABIC LIGATURE QAF WITH MEEM WITH HAH FINAL FORM
        chars.append(
            0xFD7F
        )  # uniFD7F	ARABIC LIGATURE QAF WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD80
        )  # uniFD80	ARABIC LIGATURE LAM WITH HAH WITH MEEM FINAL FORM
        chars.append(
            0xFD81
        )  # uniFD81	ARABIC LIGATURE LAM WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFD82
        )  # uniFD82	ARABIC LIGATURE LAM WITH HAH WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD83
        )  # uniFD83	ARABIC LIGATURE LAM WITH JEEM WITH JEEM INITIAL FORM
        chars.append(
            0xFD84
        )  # uniFD84	ARABIC LIGATURE LAM WITH JEEM WITH JEEM FINAL FORM
        chars.append(
            0xFD85
        )  # uniFD85	ARABIC LIGATURE LAM WITH KHAH WITH MEEM FINAL FORM
        chars.append(
            0xFD86
        )  # uniFD86	ARABIC LIGATURE LAM WITH KHAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD87
        )  # uniFD87	ARABIC LIGATURE LAM WITH MEEM WITH HAH FINAL FORM
        chars.append(
            0xFD88
        )  # uniFD88	ARABIC LIGATURE LAM WITH MEEM WITH HAH INITIAL FORM
        chars.append(
            0xFD89
        )  # uniFD89	ARABIC LIGATURE MEEM WITH HAH WITH JEEM INITIAL FORM
        chars.append(
            0xFD8A
        )  # uniFD8A	ARABIC LIGATURE MEEM WITH HAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD8B
        )  # uniFD8B	ARABIC LIGATURE MEEM WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFD8C
        )  # uniFD8C	ARABIC LIGATURE MEEM WITH JEEM WITH HAH INITIAL FORM
        chars.append(
            0xFD8D
        )  # uniFD8D	ARABIC LIGATURE MEEM WITH JEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD8E
        )  # uniFD8E	ARABIC LIGATURE MEEM WITH KHAH WITH JEEM INITIAL FORM
        chars.append(
            0xFD8F
        )  # uniFD8F	ARABIC LIGATURE MEEM WITH KHAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD92
        )  # uniFD92	ARABIC LIGATURE MEEM WITH JEEM WITH KHAH INITIAL FORM
        chars.append(
            0xFD93
        )  # uniFD93	ARABIC LIGATURE HEH WITH MEEM WITH JEEM INITIAL FORM
        chars.append(
            0xFD94
        )  # uniFD94	ARABIC LIGATURE HEH WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD95
        )  # uniFD95	ARABIC LIGATURE NOON WITH HAH WITH MEEM INITIAL FORM
        chars.append(
            0xFD96
        )  # uniFD96	ARABIC LIGATURE NOON WITH HAH WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD97
        )  # uniFD97	ARABIC LIGATURE NOON WITH JEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD98
        )  # uniFD98	ARABIC LIGATURE NOON WITH JEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD99
        )  # uniFD99	ARABIC LIGATURE NOON WITH JEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD9A
        )  # uniFD9A	ARABIC LIGATURE NOON WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFD9B
        )  # uniFD9B	ARABIC LIGATURE NOON WITH MEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFD9C
        )  # uniFD9C	ARABIC LIGATURE YEH WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFD9D
        )  # uniFD9D	ARABIC LIGATURE YEH WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFD9E
        )  # uniFD9E	ARABIC LIGATURE BEH WITH KHAH WITH YEH FINAL FORM
        chars.append(
            0xFD9F
        )  # uniFD9F	ARABIC LIGATURE TEH WITH JEEM WITH YEH FINAL FORM
        chars.append(
            0xFDA0
        )  # uniFDA0	ARABIC LIGATURE TEH WITH JEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFDA1
        )  # uniFDA1	ARABIC LIGATURE TEH WITH KHAH WITH YEH FINAL FORM
        chars.append(
            0xFDA2
        )  # uniFDA2	ARABIC LIGATURE TEH WITH KHAH WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFDA3
        )  # uniFDA3	ARABIC LIGATURE TEH WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDA4
        )  # uniFDA4	ARABIC LIGATURE TEH WITH MEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFDA5
        )  # uniFDA5	ARABIC LIGATURE JEEM WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDA6
        )  # uniFDA6	ARABIC LIGATURE JEEM WITH HAH WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFDA7
        )  # uniFDA7	ARABIC LIGATURE JEEM WITH MEEM WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFDA8
        )  # uniFDA8	ARABIC LIGATURE SEEN WITH KHAH WITH ALEF MAKSURA FINAL FORM
        chars.append(
            0xFDA9
        )  # uniFDA9	ARABIC LIGATURE SAD WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFDAA
        )  # uniFDAA	ARABIC LIGATURE SHEEN WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFDAB
        )  # uniFDAB	ARABIC LIGATURE DAD WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFDAC
        )  # uniFDAC	ARABIC LIGATURE LAM WITH JEEM WITH YEH FINAL FORM
        chars.append(
            0xFDAD
        )  # uniFDAD	ARABIC LIGATURE LAM WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDAE
        )  # uniFDAE	ARABIC LIGATURE YEH WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFDAF
        )  # uniFDAF	ARABIC LIGATURE YEH WITH JEEM WITH YEH FINAL FORM
        chars.append(
            0xFDB0
        )  # uniFDB0	ARABIC LIGATURE YEH WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDB1
        )  # uniFDB1	ARABIC LIGATURE MEEM WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDB2
        )  # uniFDB2	ARABIC LIGATURE QAF WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDB3
        )  # uniFDB3	ARABIC LIGATURE NOON WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFDB4
        )  # uniFDB4	ARABIC LIGATURE QAF WITH MEEM WITH HAH INITIAL FORM
        chars.append(
            0xFDB5
        )  # uniFDB5	ARABIC LIGATURE LAM WITH HAH WITH MEEM INITIAL FORM
        chars.append(
            0xFDB6
        )  # uniFDB6	ARABIC LIGATURE AIN WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDB7
        )  # uniFDB7	ARABIC LIGATURE KAF WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDB8
        )  # uniFDB8	ARABIC LIGATURE NOON WITH JEEM WITH HAH INITIAL FORM
        chars.append(
            0xFDB9
        )  # uniFDB9	ARABIC LIGATURE MEEM WITH KHAH WITH YEH FINAL FORM
        chars.append(
            0xFDBA
        )  # uniFDBA	ARABIC LIGATURE LAM WITH JEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFDBB
        )  # uniFDBB	ARABIC LIGATURE KAF WITH MEEM WITH MEEM FINAL FORM
        chars.append(
            0xFDBC
        )  # uniFDBC	ARABIC LIGATURE LAM WITH JEEM WITH MEEM FINAL FORM
        chars.append(
            0xFDBD
        )  # uniFDBD	ARABIC LIGATURE NOON WITH JEEM WITH HAH FINAL FORM
        chars.append(
            0xFDBE
        )  # uniFDBE	ARABIC LIGATURE JEEM WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFDBF
        )  # uniFDBF	ARABIC LIGATURE HAH WITH JEEM WITH YEH FINAL FORM
        chars.append(
            0xFDC0
        )  # uniFDC0	ARABIC LIGATURE MEEM WITH JEEM WITH YEH FINAL FORM
        chars.append(
            0xFDC1
        )  # uniFDC1	ARABIC LIGATURE FEH WITH MEEM WITH YEH FINAL FORM
        chars.append(
            0xFDC2
        )  # uniFDC2	ARABIC LIGATURE BEH WITH HAH WITH YEH FINAL FORM
        chars.append(
            0xFDC3
        )  # uniFDC3	ARABIC LIGATURE KAF WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFDC4
        )  # uniFDC4	ARABIC LIGATURE AIN WITH JEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFDC5
        )  # uniFDC5	ARABIC LIGATURE SAD WITH MEEM WITH MEEM INITIAL FORM
        chars.append(
            0xFDC6
        )  # uniFDC6	ARABIC LIGATURE SEEN WITH KHAH WITH YEH FINAL FORM
        chars.append(
            0xFDC7
        )  # uniFDC7	ARABIC LIGATURE NOON WITH JEEM WITH YEH FINAL FORM
        chars.append(0x25CC)  # uni25CC	DOTTED CIRCLE
        chars.append(0xFEDD)  # uni0644	ARABIC LETTER LAM ISOLATED FORM
        chars.append(0xFDF2)  # uniFDF2	ARABIC LIGATURE ALLAH ISOLATED FORM
        chars.append(0xFDFA)  # uniFDFA	ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM
        chars.append(0xFDFB)  # uniFDFB	ARABIC LIGATURE JALLAJALALOUHOU
        chars.append(0xFDFC)  # uniFDFC	RIAL SIGN
        chars.append(0xFDFD)  # uniFDFD	ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM
        chars.append(0x0600)  # uni0600	ARABIC NUMBER SIGN
        chars.append(0x0601)  # uni0601	ARABIC SIGN SANAH
        chars.append(0x0602)  # uni0602	ARABIC FOOTNOTE MARKER
        chars.append(0x0603)  # uni0603	ARABIC SIGN SAFHA
        chars.append(0x0604)  # uni0604	????
        chars.append(0x0606)  # uni0606	ARABIC-INDIC CUBE ROOT
        chars.append(0x0607)  # uni0607	ARABIC-INDIC FOURTH ROOT
        chars.append(0x0608)  # uni0608	ARABIC RAY
        chars.append(0x0609)  # uni0609	ARABIC-INDIC PER MILLE SIGN
        chars.append(0x060A)  # uni060A	ARABIC-INDIC PER TEN THOUSAND SIGN
        chars.append(0x060B)  # uni060B	AFGHANI SIGN
        chars.append(0x060C)  # uni060C	ARABIC COMMA
        chars.append(0x060D)  # uni060D	ARABIC DATE SEPARATOR
        chars.append(0x060E)  # uni060E	ARABIC POETIC VERSE SIGN
        chars.append(0x060F)  # uni060F	ARABIC SIGN MISRA
        chars.append(0x0610)  # uni0610	ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM
        chars.append(0x0611)  # uni0611	ARABIC SIGN ALAYHE ASSALLAM
        chars.append(0x0612)  # uni0612	ARABIC SIGN RAHMATULLAH ALAYHE
        chars.append(0x0613)  # uni0613	ARABIC SIGN RADI ALLAHOU ANHU
        chars.append(0x0614)  # uni0614	ARABIC SIGN TAKHALLUS
        chars.append(0x0615)  # uni0615	ARABIC SMALL HIGH TAH
        chars.append(
            0x0616
        )  # uni0616	ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH
        chars.append(0x0617)  # uni0617	ARABIC SMALL HIGH ZAIN
        chars.append(0x0618)  # uni0618	ARABIC SMALL FATHA
        chars.append(0x0619)  # uni0619	ARABIC SMALL DAMMA
        chars.append(0x061A)  # uni061A	ARABIC SMALL KASRA
        chars.append(0x061B)  # uni061B	ARABIC SEMICOLON
        chars.append(0x061E)  # uni061E	ARABIC TRIPLE DOT PUNCTUATION MARK
        chars.append(0x061F)  # uni061F	ARABIC QUESTION MARK
        chars.append(0x0620)  # uni0620	????
        chars.append(0x0621)  # uniFE80	ARABIC LETTER HAMZA
        chars.append(0x0622)  # uniFE81	ARABIC LETTER ALEF WITH MADDA ABOVE
        chars.append(0x0623)  # uniFE83	ARABIC LETTER ALEF WITH HAMZA ABOVE
        chars.append(0x0624)  # uniFE85	ARABIC LETTER WAW WITH HAMZA ABOVE
        chars.append(0x0625)  # uniFE87	ARABIC LETTER ALEF WITH HAMZA BELOW
        chars.append(0x0626)  # uniFE89	ARABIC LETTER YEH WITH HAMZA ABOVE
        chars.append(0x0627)  # uniFE8D	ARABIC LETTER ALEF
        chars.append(0x0628)  # uniFE8F	ARABIC LETTER BEH
        chars.append(0x0629)  # uni0629	ARABIC LETTER TEH MARBUTA
        chars.append(0x062A)  # uni062A	ARABIC LETTER TEH
        chars.append(0x062B)  # uniFE99	ARABIC LETTER THEH
        chars.append(0x062C)  # uniFE9D	ARABIC LETTER JEEM
        chars.append(0x062D)  # uniFEA1	ARABIC LETTER HAH
        chars.append(0x062E)  # uniFEA5	ARABIC LETTER KHAH
        chars.append(0x062F)  # uniFEA9	ARABIC LETTER DAL
        chars.append(0x0630)  # uni0630	ARABIC LETTER THAL
        chars.append(0x0631)  # uni0631	ARABIC LETTER REH
        chars.append(0x0632)  # uni0632	ARABIC LETTER ZAIN
        chars.append(0x0633)  # uni0633	ARABIC LETTER SEEN
        chars.append(0x0634)  # uni0634	ARABIC LETTER SHEEN
        chars.append(0x0635)  # uni0635	ARABIC LETTER SAD
        chars.append(0x0636)  # uni0636	ARABIC LETTER DAD
        chars.append(0x0637)  # uni0637	ARABIC LETTER TAH
        chars.append(0x0638)  # uni0638	ARABIC LETTER ZAH
        chars.append(0x0639)  # uni0639	ARABIC LETTER AIN
        chars.append(0x063A)  # uni063A	ARABIC LETTER GHAIN
        chars.append(0x063B)  # uni063B	ARABIC LETTER KEHEH WITH TWO DOTS ABOVE
        chars.append(0x063C)  # uni063C	ARABIC LETTER KEHEH WITH THREE DOTS BELOW
        chars.append(0x063D)  # uni063D	ARABIC LETTER FARSI YEH WITH INVERTED V
        chars.append(0x063E)  # uni063E	ARABIC LETTER FARSI YEH WITH TWO DOTS ABOVE
        chars.append(0x063F)  # uni063F	ARABIC LETTER FARSI YEH WITH THREE DOTS ABOVE
        chars.append(0x0640)  # uni0640	ARABIC TATWEEL
        chars.append(0x0641)  # uni0641	ARABIC LETTER FEH
        chars.append(0x0642)  # uni0642	ARABIC LETTER QAF
        chars.append(0x0643)  # uni0643	ARABIC LETTER KAF
        chars.append(0x0644)  # uni0644	ARABIC LETTER LAM
        chars.append(0x0645)  # uni0645	ARABIC LETTER MEEM
        chars.append(0x0646)  # uni0646	ARABIC LETTER NOON
        chars.append(0x0647)  # uni0647	ARABIC LETTER HEH
        chars.append(0x0648)  # uni0648	ARABIC LETTER WAW
        chars.append(0x0649)  # uni0649	ARABIC LETTER ALEF MAKSURA
        chars.append(0x064A)  # uni064A	ARABIC LETTER YEH
        chars.append(0x064B)  # uni064B	ARABIC FATHATAN
        chars.append(0x064C)  # uni064C	ARABIC DAMMATAN
        chars.append(0x064D)  # uni064D	ARABIC KASRATAN
        chars.append(0x064E)  # uni064E	ARABIC FATHA
        chars.append(0x064F)  # uni064F	ARABIC DAMMA
        chars.append(0x0650)  # uni0650	ARABIC KASRA
        chars.append(0x0651)  # uni0651	ARABIC SHADDA
        chars.append(0x0652)  # uni0652	ARABIC SUKUN
        chars.append(0x0653)  # uni0653	ARABIC MADDAH ABOVE
        chars.append(0x0654)  # uni0654	ARABIC HAMZA ABOVE
        chars.append(0x0655)  # uni0655	ARABIC HAMZA BELOW
        chars.append(0x0656)  # uni0656	ARABIC SUBSCRIPT ALEF
        chars.append(0x0657)  # uni0657	ARABIC INVERTED DAMMA
        chars.append(0x0658)  # uni0658	ARABIC MARK NOON GHUNNA
        chars.append(0x0659)  # uni0659	ARABIC ZWARAKAY
        chars.append(0x065A)  # uni065A	ARABIC VOWEL SIGN SMALL V ABOVE
        chars.append(0x065B)  # uni065B	ARABIC VOWEL SIGN INVERTED SMALL V ABOVE
        chars.append(0x065C)  # uni065C	ARABIC VOWEL SIGN DOT BELOW
        chars.append(0x065D)  # uni065D	ARABIC REVERSED DAMMA
        chars.append(0x065E)  # uni065E	ARABIC FATHA WITH TWO DOTS
        chars.append(0x065F)  # uni065F	????
        chars.append(0x0660)  # uni0660	ARABIC-INDIC DIGIT ZERO
        chars.append(0x0661)  # uni0661	ARABIC-INDIC DIGIT ONE
        chars.append(0x0662)  # uni0662	ARABIC-INDIC DIGIT TWO
        chars.append(0x0663)  # uni0663	ARABIC-INDIC DIGIT THREE
        chars.append(0x0664)  # uni0664	ARABIC-INDIC DIGIT FOUR
        chars.append(0x0665)  # uni0665	ARABIC-INDIC DIGIT FIVE
        chars.append(0x0666)  # uni0666	ARABIC-INDIC DIGIT SIX
        chars.append(0x0667)  # uni0667	ARABIC-INDIC DIGIT SEVEN
        chars.append(0x0668)  # uni0668	ARABIC-INDIC DIGIT EIGHT
        chars.append(0x0669)  # uni0669	ARABIC-INDIC DIGIT NINE
        chars.append(0x066A)  # uni066A	ARABIC PERCENT SIGN
        chars.append(0x066B)  # uni066B	ARABIC DECIMAL SEPARATOR
        chars.append(0x066C)  # uni066C	ARABIC THOUSANDS SEPARATOR
        chars.append(0x066D)  # uni066D	ARABIC FIVE POINTED STAR
        chars.append(0x066E)  # uni066E	ARABIC LETTER DOTLESS BEH
        chars.append(0x066F)  # uni066F	ARABIC LETTER DOTLESS QAF
        chars.append(0x0670)  # uni0670	ARABIC LETTER SUPERSCRIPT ALEF
        chars.append(0x0671)  # uni0671	ARABIC LETTER ALEF WASLA
        chars.append(0x0672)  # uni0672	ARABIC LETTER ALEF WITH WAVY HAMZA ABOVE
        chars.append(0x0673)  # uni0673	ARABIC LETTER ALEF WITH WAVY HAMZA BELOW
        chars.append(0x0674)  # uni0674	ARABIC LETTER HIGH HAMZA
        chars.append(0x0675)  # uni0675	ARABIC LETTER HIGH HAMZA ALEF
        chars.append(0x0676)  # uni0676	ARABIC LETTER HIGH HAMZA WAW
        chars.append(0x0677)  # uni0677	ARABIC LETTER U WITH HAMZA ABOVE
        chars.append(0x0678)  # uni0678	ARABIC LETTER HIGH HAMZA YEH
        chars.append(0x0679)  # uni0679	ARABIC LETTER TTEH
        chars.append(0x067A)  # uni067A	ARABIC LETTER TTEHEH
        chars.append(0x067B)  # uni067B	ARABIC LETTER BEEH
        chars.append(0x067C)  # uni067C	ARABIC LETTER TEH WITH RING
        chars.append(
            0x067D
        )  # uni067D	ARABIC LETTER TEH WITH THREE DOTS ABOVE DOWNWARDS
        chars.append(0x067E)  # uni067E	ARABIC LETTER PEH
        chars.append(0x067F)  # uni067F	ARABIC LETTER TEHEH
        chars.append(0x0680)  # uni0680	ARABIC LETTER BEHEH
        chars.append(0x0681)  # uni0681	ARABIC LETTER HAH WITH HAMZA ABOVE
        chars.append(
            0x0682
        )  # uni0682	ARABIC LETTER HAH WITH TWO DOTS VERTICAL ABOVE
        chars.append(0x0683)  # uni0683	ARABIC LETTER NYEH
        chars.append(0x0684)  # uni0684	ARABIC LETTER DYEH
        chars.append(0x0685)  # uni0685	ARABIC LETTER HAH WITH THREE DOTS ABOVE
        chars.append(0x0686)  # uni0686	ARABIC LETTER TCHEH
        chars.append(0x0687)  # uni0687	ARABIC LETTER TCHEHEH
        chars.append(0x0688)  # uni0688	ARABIC LETTER DDAL
        chars.append(0x0689)  # uni0689	ARABIC LETTER DAL WITH RING
        chars.append(0x068A)  # uni068A	ARABIC LETTER DAL WITH DOT BELOW
        chars.append(
            0x068B
        )  # uni068B	ARABIC LETTER DAL WITH DOT BELOW AND SMALL TAH
        chars.append(0x068C)  # uni068C	ARABIC LETTER DAHAL
        chars.append(0x068D)  # uni068D	ARABIC LETTER DDAHAL
        chars.append(0x068E)  # uni068E	ARABIC LETTER DUL
        chars.append(
            0x068F
        )  # uni068F	ARABIC LETTER DAL WITH THREE DOTS ABOVE DOWNWARDS
        chars.append(0x0690)  # uni0690	ARABIC LETTER DAL WITH FOUR DOTS ABOVE
        chars.append(0x0691)  # uni0691	ARABIC LETTER RREH
        chars.append(0x0692)  # uni0692	ARABIC LETTER REH WITH SMALL V
        chars.append(0x0693)  # uni0693	ARABIC LETTER REH WITH RING
        chars.append(0x0694)  # uni0694	ARABIC LETTER REH WITH DOT BELOW
        chars.append(0x0695)  # uni0695	ARABIC LETTER REH WITH SMALL V BELOW
        chars.append(
            0x0696
        )  # uni0696	ARABIC LETTER REH WITH DOT BELOW AND DOT ABOVE
        chars.append(0x0697)  # uni0697	ARABIC LETTER REH WITH TWO DOTS ABOVE
        chars.append(0x0698)  # uni0698	ARABIC LETTER JEH
        chars.append(0x0699)  # uni0699	ARABIC LETTER REH WITH FOUR DOTS ABOVE
        chars.append(
            0x069A
        )  # uni069A	ARABIC LETTER SEEN WITH DOT BELOW AND DOT ABOVE
        chars.append(0x069B)  # uni069B	ARABIC LETTER SEEN WITH THREE DOTS BELOW
        chars.append(
            0x069C
        )  # uni069C	ARABIC LETTER SEEN WITH THREE DOTS BELOW AND THREE DOTS ABOVE
        chars.append(0x069D)  # uni069D	ARABIC LETTER SAD WITH TWO DOTS BELOW
        chars.append(0x069E)  # uni069E	ARABIC LETTER SAD WITH THREE DOTS ABOVE
        chars.append(0x069F)  # uni069F	ARABIC LETTER TAH WITH THREE DOTS ABOVE
        chars.append(0x06A0)  # uni06A0	ARABIC LETTER AIN WITH THREE DOTS ABOVE
        chars.append(0x06A1)  # uni06A1	ARABIC LETTER DOTLESS FEH
        chars.append(0x06A2)  # uni06A2	ARABIC LETTER FEH WITH DOT MOVED BELOW
        chars.append(0x06A3)  # uni06A3	ARABIC LETTER FEH WITH DOT BELOW
        chars.append(0x06A4)  # uni06A4	ARABIC LETTER VEH
        chars.append(0x06A5)  # uni06A5	ARABIC LETTER FEH WITH THREE DOTS BELOW
        chars.append(0x06A6)  # uni06A6	ARABIC LETTER PEHEH
        chars.append(0x06A7)  # uni06A7	ARABIC LETTER QAF WITH DOT ABOVE
        chars.append(0x06A8)  # uni06A8	ARABIC LETTER QAF WITH THREE DOTS ABOVE
        chars.append(0x06A9)  # uni06A9	ARABIC LETTER KEHEH
        chars.append(0x06AA)  # uni06AA	ARABIC LETTER SWASH KAF
        chars.append(0x06AB)  # uni06AB	ARABIC LETTER KAF WITH RING
        chars.append(0x06AC)  # uni06AC	ARABIC LETTER KAF WITH DOT ABOVE
        chars.append(0x06AD)  # uni06AD	ARABIC LETTER NG
        chars.append(0x06AE)  # uni06AE	ARABIC LETTER KAF WITH THREE DOTS BELOW
        chars.append(0x06AF)  # uni06AF	ARABIC LETTER GAF
        chars.append(0x06B0)  # uni06B0	ARABIC LETTER GAF WITH RING
        chars.append(0x06B1)  # uni06B1	ARABIC LETTER NGOEH
        chars.append(0x06B2)  # uni06B2	ARABIC LETTER GAF WITH TWO DOTS BELOW
        chars.append(0x06B3)  # uni06B3	ARABIC LETTER GUEH
        chars.append(0x06B4)  # uni06B4	ARABIC LETTER GAF WITH THREE DOTS ABOVE
        chars.append(0x06B5)  # uni06B5	ARABIC LETTER LAM WITH SMALL V
        chars.append(0x06B6)  # uni06B6	ARABIC LETTER LAM WITH DOT ABOVE
        chars.append(0x06B7)  # uni06B7	ARABIC LETTER LAM WITH THREE DOTS ABOVE
        chars.append(0x06B8)  # uni06B8	ARABIC LETTER LAM WITH THREE DOTS BELOW
        chars.append(0x06B9)  # uni06B9	ARABIC LETTER NOON WITH DOT BELOW
        chars.append(0x06BA)  # uni06BA	ARABIC LETTER NOON GHUNNA
        chars.append(0x06BB)  # uni06BB	ARABIC LETTER RNOON
        chars.append(0x06BC)  # uni06BC	ARABIC LETTER NOON WITH RING
        chars.append(0x06BD)  # uni06BD	ARABIC LETTER NOON WITH THREE DOTS ABOVE
        chars.append(0x06BE)  # uni06BE	ARABIC LETTER HEH DOACHASHMEE
        chars.append(0x06BF)  # uni06BF	ARABIC LETTER TCHEH WITH DOT ABOVE
        chars.append(0x06C0)  # uni06C0	ARABIC LETTER HEH WITH YEH ABOVE
        chars.append(0x06C1)  # uni06C1	ARABIC LETTER HEH GOAL
        chars.append(0x06C2)  # uni06C2	ARABIC LETTER HEH GOAL WITH HAMZA ABOVE
        chars.append(0x06C3)  # uni06C3	ARABIC LETTER TEH MARBUTA GOAL
        chars.append(0x06C4)  # uni06C4	ARABIC LETTER WAW WITH RING
        chars.append(0x06C5)  # uni06C5	ARABIC LETTER KIRGHIZ OE
        chars.append(0x06C6)  # uni06C6	ARABIC LETTER OE
        chars.append(0x06C7)  # uni06C7	ARABIC LETTER U
        chars.append(0x06C8)  # uni06C8	ARABIC LETTER YU
        chars.append(0x06C9)  # uni06C9	ARABIC LETTER KIRGHIZ YU
        chars.append(0x06CA)  # uni06CA	ARABIC LETTER WAW WITH TWO DOTS ABOVE
        chars.append(0x06CB)  # uni06CB	ARABIC LETTER VE
        chars.append(0x06CC)  # uni06CC	ARABIC LETTER FARSI YEH
        chars.append(0x06CD)  # uni06CD	ARABIC LETTER YEH WITH TAIL
        chars.append(0x06CE)  # uni06CE	ARABIC LETTER YEH WITH SMALL V
        chars.append(0x06CF)  # uni06CF	ARABIC LETTER WAW WITH DOT ABOVE
        chars.append(0x06D0)  # uni06D0	ARABIC LETTER E
        chars.append(0x06D1)  # uni06D1	ARABIC LETTER YEH WITH THREE DOTS BELOW
        chars.append(0x06D2)  # uni06D2	ARABIC LETTER YEH BARREE
        chars.append(0x06D3)  # uni06D3	ARABIC LETTER YEH BARREE WITH HAMZA ABOVE
        chars.append(0x06D4)  # uni06D4	ARABIC FULL STOP
        chars.append(0x06D5)  # uni06D5	ARABIC LETTER AE
        chars.append(
            0x06D6
        )  # uni06D6	ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA
        chars.append(
            0x06D7
        )  # uni06D7	ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA
        chars.append(0x06D8)  # uni06D8	ARABIC SMALL HIGH MEEM INITIAL FORM
        chars.append(0x06D9)  # uni06D9	ARABIC SMALL HIGH LAM ALEF
        chars.append(0x06DA)  # uni06DA	ARABIC SMALL HIGH JEEM
        chars.append(0x06DB)  # uni06DB	ARABIC SMALL HIGH THREE DOTS
        chars.append(0x06DC)  # uni06DC	ARABIC SMALL HIGH SEEN
        chars.append(0x06DD)  # uni06DD	ARABIC END OF AYAH
        chars.append(0x06DE)  # uni06DE	ARABIC START OF RUB EL HIZB
        chars.append(0x06DF)  # uni06DF	ARABIC SMALL HIGH ROUNDED ZERO
        chars.append(0x06E0)  # uni06E0	ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO
        chars.append(0x06E1)  # uni06E1	ARABIC SMALL HIGH DOTLESS HEAD OF KHAH
        chars.append(0x06E2)  # uni06E2	ARABIC SMALL HIGH MEEM ISOLATED FORM
        chars.append(0x06E3)  # uni06E3	ARABIC SMALL LOW SEEN
        chars.append(0x06E4)  # uni06E4	ARABIC SMALL HIGH MADDA
        chars.append(0x06E5)  # uni06E5	ARABIC SMALL WAW
        chars.append(0x06E6)  # uni06E6	ARABIC SMALL YEH
        chars.append(0x06E7)  # uni06E7	ARABIC SMALL HIGH YEH
        chars.append(0x06E8)  # uni06E8	ARABIC SMALL HIGH NOON
        chars.append(0x06E9)  # uni06E9	ARABIC PLACE OF SAJDAH
        chars.append(0x06EA)  # uni06EA	ARABIC EMPTY CENTRE LOW STOP
        chars.append(0x06EB)  # uni06EB	ARABIC EMPTY CENTRE HIGH STOP
        chars.append(0x06EC)  # uni06EC	ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE
        chars.append(0x06ED)  # uni06ED	ARABIC SMALL LOW MEEM
        chars.append(0x06EE)  # uni06EE	ARABIC LETTER DAL WITH INVERTED V
        chars.append(0x06EF)  # uni06EF	ARABIC LETTER REH WITH INVERTED V
        chars.append(0x06F0)  # uni06F0	EXTENDED ARABIC-INDIC DIGIT ZERO
        chars.append(0x06F1)  # uni06F1	EXTENDED ARABIC-INDIC DIGIT ONE
        chars.append(0x06F2)  # uni06F2	EXTENDED ARABIC-INDIC DIGIT TWO
        chars.append(0x06F3)  # uni06F3	EXTENDED ARABIC-INDIC DIGIT THREE
        chars.append(0x06F4)  # uni06F4	EXTENDED ARABIC-INDIC DIGIT FOUR
        chars.append(0x06F5)  # uni06F5	EXTENDED ARABIC-INDIC DIGIT FIVE
        chars.append(0x06F6)  # uni06F6	EXTENDED ARABIC-INDIC DIGIT SIX
        chars.append(0x06F7)  # uni06F7	EXTENDED ARABIC-INDIC DIGIT SEVEN
        chars.append(0x06F8)  # uni06F8	EXTENDED ARABIC-INDIC DIGIT EIGHT
        chars.append(0x06F9)  # uni06F9	EXTENDED ARABIC-INDIC DIGIT NINE
        chars.append(0x06FA)  # uni06FA	ARABIC LETTER SHEEN WITH DOT BELOW
        chars.append(0x06FB)  # uni06FB	ARABIC LETTER DAD WITH DOT BELOW
        chars.append(0x06FC)  # uni06FC	ARABIC LETTER GHAIN WITH DOT BELOW
        chars.append(0x06FD)  # uni06FD	ARABIC SIGN SINDHI AMPERSAND
        chars.append(0x06FE)  # uni06FE	ARABIC SIGN SINDHI POSTPOSITION MEN
        chars.append(0x06FF)  # uni06FF	ARABIC LETTER HEH WITH INVERTED V
        chars.append(0xFE80)  # uniFE80	ARABIC LETTER HAMZA ISOLATED FORM
        chars.append(
            0xFE81
        )  # uniFE81	ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM
        chars.append(
            0xFE82
        )  # uniFE82	ARABIC LETTER ALEF WITH MADDA ABOVE FINAL FORM
        chars.append(
            0xFE83
        )  # uniFE83	ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM
        chars.append(
            0xFE84
        )  # uniFE84	ARABIC LETTER ALEF WITH HAMZA ABOVE FINAL FORM
        chars.append(
            0xFE85
        )  # uniFE85	ARABIC LETTER WAW WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFE86)  # uniFE86	ARABIC LETTER WAW WITH HAMZA ABOVE FINAL FORM
        chars.append(
            0xFE87
        )  # uniFE87	ARABIC LETTER ALEF WITH HAMZA BELOW ISOLATED FORM
        chars.append(
            0xFE88
        )  # uniFE88	ARABIC LETTER ALEF WITH HAMZA BELOW FINAL FORM
        chars.append(
            0xFE89
        )  # uniFE89	ARABIC LETTER YEH WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFED2)  # uniFED2	ARABIC LETTER FEH FINAL FORM
        chars.append(0xFE8A)  # uniFE8A	ARABIC LETTER YEH WITH HAMZA ABOVE FINAL FORM
        chars.append(
            0xFE8B
        )  # uniFE8B	ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM
        chars.append(
            0xFE8C
        )  # uniFE8C	ARABIC LETTER YEH WITH HAMZA ABOVE MEDIAL FORM
        chars.append(0xFE8D)  # uniFE8D	ARABIC LETTER ALEF ISOLATED FORM
        chars.append(
            0x0750
        )  # uni0750	ARABIC LETTER BEH WITH THREE DOTS HORIZONTALLY BELOW
        chars.append(
            0x0751
        )  # uni0751	ARABIC LETTER BEH WITH DOT BELOW AND THREE DOTS ABOVE
        chars.append(
            0x0752
        )  # uni0752	ARABIC LETTER BEH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(
            0x0753
        )  # uni0753	ARABIC LETTER BEH WITH THREE DOTS POINTING UPWARDS BELOW AND TWO DOTS ABOVE
        chars.append(
            0x0754
        )  # uni0754	ARABIC LETTER BEH WITH TWO DOTS BELOW AND DOT ABOVE
        chars.append(0x0755)  # uni0755	ARABIC LETTER BEH WITH INVERTED SMALL V BELOW
        chars.append(0x0756)  # uni0756	ARABIC LETTER BEH WITH SMALL V
        chars.append(0x0757)  # uni0757	ARABIC LETTER HAH WITH TWO DOTS ABOVE
        chars.append(
            0x0758
        )  # uni0758	ARABIC LETTER HAH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(
            0x0759
        )  # uni0759	ARABIC LETTER DAL WITH TWO DOTS VERTICALLY BELOW AND SMALL TAH
        chars.append(0x075A)  # uni075A	ARABIC LETTER DAL WITH INVERTED SMALL V BELOW
        chars.append(0x075B)  # uni075B	ARABIC LETTER REH WITH STROKE
        chars.append(0x075C)  # uni075C	ARABIC LETTER SEEN WITH FOUR DOTS ABOVE
        chars.append(0x075D)  # uni075D	ARABIC LETTER AIN WITH TWO DOTS ABOVE
        chars.append(
            0x075E
        )  # uni075E	ARABIC LETTER AIN WITH THREE DOTS POINTING DOWNWARDS ABOVE
        chars.append(
            0x075F
        )  # uni075F	ARABIC LETTER AIN WITH TWO DOTS VERTICALLY ABOVE
        chars.append(0x0760)  # uni0760	ARABIC LETTER FEH WITH TWO DOTS BELOW
        chars.append(
            0x0761
        )  # uni0761	ARABIC LETTER FEH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(0x0762)  # uni0762	ARABIC LETTER KEHEH WITH DOT ABOVE
        chars.append(0x0763)  # uni0763	ARABIC LETTER KEHEH WITH THREE DOTS ABOVE
        chars.append(
            0x0764
        )  # uni0764	ARABIC LETTER KEHEH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(0x0765)  # uni0765	ARABIC LETTER MEEM WITH DOT ABOVE
        chars.append(0x0766)  # uni0766	ARABIC LETTER MEEM WITH DOT BELOW
        chars.append(0x0767)  # uni0767	ARABIC LETTER NOON WITH TWO DOTS BELOW
        chars.append(0x0768)  # uni0768	ARABIC LETTER NOON WITH SMALL TAH
        chars.append(0x0769)  # uni0769	ARABIC LETTER NOON WITH SMALL V
        chars.append(0x076A)  # uni076A	ARABIC LETTER LAM WITH BAR
        chars.append(
            0x076B
        )  # uni076B	ARABIC LETTER REH WITH TWO DOTS VERTICALLY ABOVE
        chars.append(0x076C)  # uni076C	ARABIC LETTER REH WITH HAMZA ABOVE
        chars.append(
            0x076D
        )  # uni076D	ARABIC LETTER SEEN WITH TWO DOTS VERTICALLY ABOVE
        chars.append(
            0x076E
        )  # uni076E	ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH BELOW
        chars.append(
            0x076F
        )  # uni076F	ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH AND TWO DOTS
        chars.append(
            0x0770
        )  # uni0770	ARABIC LETTER SEEN WITH SMALL ARABIC LETTER TAH AND TWO DOTS
        chars.append(
            0x0771
        )  # uni0771	ARABIC LETTER REH WITH SMALL ARABIC LETTER TAH AND TWO DOTS
        chars.append(
            0x0772
        )  # uni0772	ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH ABOVE
        chars.append(
            0x0773
        )  # uni0773	ARABIC LETTER ALEF WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(
            0x0774
        )  # uni0774	ARABIC LETTER ALEF WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(
            0x0775
        )  # uni0775	ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(
            0x0776
        )  # uni0776	ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(
            0x0777
        )  # uni0777	ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT FOUR BELOW
        chars.append(
            0x0778
        )  # uni0778	ARABIC LETTER WAW WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(
            0x0779
        )  # uni0779	ARABIC LETTER WAW WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(
            0x077A
        )  # uni077A	ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(
            0x077B
        )  # uni077B	ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(
            0x077C
        )  # uni077C	ARABIC LETTER HAH WITH EXTENDED ARABIC-INDIC DIGIT FOUR BELOW
        chars.append(
            0x077D
        )  # uni077D	ARABIC LETTER SEEN WITH EXTENDED ARABIC-INDIC DIGIT FOUR ABOVE
        chars.append(0x077E)  # uni077E	ARABIC LETTER SEEN WITH INVERTED V
        chars.append(0x077F)  # uni077F	ARABIC LETTER KAF WITH TWO DOTS ABOVE
        chars.append(0xFE96)  # uniFE96	ARABIC LETTER TEH FINAL FORM
        chars.append(0xFE97)  # uniFE97	ARABIC LETTER TEH INITIAL FORM
        chars.append(0xFE98)  # uniFE98	ARABIC LETTER TEH MEDIAL FORM
        chars.append(0xFE99)  # uniFE99	ARABIC LETTER THEH ISOLATED FORM
        chars.append(0xFE9A)  # uniFE9A	ARABIC LETTER THEH FINAL FORM
        chars.append(0xFE9B)  # uniFE9B	ARABIC LETTER THEH INITIAL FORM
        chars.append(0xFE9C)  # uniFE9C	ARABIC LETTER THEH MEDIAL FORM
        chars.append(0xFE9D)  # uniFE9D	ARABIC LETTER JEEM ISOLATED FORM
        chars.append(0xFE9E)  # uniFE9E	ARABIC LETTER JEEM FINAL FORM
        chars.append(0xFE9F)  # uniFE9F	ARABIC LETTER JEEM INITIAL FORM
        chars.append(0xFEA0)  # uniFEA0	ARABIC LETTER JEEM MEDIAL FORM
        chars.append(0xFEA1)  # uniFEA1	ARABIC LETTER HAH ISOLATED FORM
        chars.append(0xFEA2)  # uniFEA2	ARABIC LETTER HAH FINAL FORM
        chars.append(0xFED3)  # uniFED3	ARABIC LETTER FEH INITIAL FORM
        chars.append(0xFEA3)  # uniFEA3	ARABIC LETTER HAH INITIAL FORM
        chars.append(0xFEA4)  # uniFEA4	ARABIC LETTER HAH MEDIAL FORM
        chars.append(0xFEA5)  # uniFEA5	ARABIC LETTER KHAH ISOLATED FORM
        chars.append(0xFEA6)  # uniFEA6	ARABIC LETTER KHAH FINAL FORM
        chars.append(0xFEA7)  # uniFEA7	ARABIC LETTER KHAH INITIAL FORM
        chars.append(0xFE8F)  # uniFE8F	ARABIC LETTER BEH ISOLATED FORM
        chars.append(0xFEA8)  # uniFEA8	ARABIC LETTER KHAH MEDIAL FORM
        chars.append(0xFEA9)  # uniFEA9	ARABIC LETTER DAL ISOLATED FORM
        chars.append(0xFEAA)  # uniFEAA	ARABIC LETTER DAL FINAL FORM
        return chars
