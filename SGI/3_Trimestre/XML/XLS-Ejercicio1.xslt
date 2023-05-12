<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:math="http://www.w3.org/2005/xpath-functions/math" xmlns:array="http://www.w3.org/2005/xpath-functions/array" xmlns:map="http://www.w3.org/2005/xpath-functions/map" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:err="http://www.w3.org/2005/xqt-errors" exclude-result-prefixes="array fn map math xhtml xs err" version="3.0">
	<xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:template match="/" name="xsl:initial-template">
		<xsl:value-of select="/DATA/ROW/cod_paciente"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Nombre"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Apellido"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Apellido2"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Localidad"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Provincia"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Edad"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Email"></xsl:value-of>
		<xsl:value-of select="/DATA/ROW/Historia"></xsl:value-of>
	</xsl:template>
</xsl:stylesheet>
