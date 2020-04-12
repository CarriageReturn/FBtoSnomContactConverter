<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:strip-space elements="*"/>
<xsl:output method="text"/>
  <xsl:template match="/phonebooks/phonebook/contact">
      <xsl:for-each select = "telephony/number">
         <xsl:value-of select="../../person/realName"/> (<xsl:value-of select="@type"/>),<xsl:value-of select="current()"/>
         <xsl:text>&#xa;</xsl:text>
     </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
