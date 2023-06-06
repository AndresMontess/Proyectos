<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:math="http://www.w3.org/2005/xpath-functions/math" xmlns:array="http://www.w3.org/2005/xpath-functions/array" xmlns:map="http://www.w3.org/2005/xpath-functions/map" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:err="http://www.w3.org/2005/xqt-errors" exclude-result-prefixes="array fn map math xhtml xs err" version="3.0">
	<xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:template match="/" name="xsl:initial-template">
		<html>
			<head>
				<link type="text/css" rel="stylesheet" href="./CSS/CSS.css"/>
			</head>
			<body>
			<header>
				<h2 class="titulo">Cuestionario:</h2>		
			</header>
	
				<main>
				<nav>
					<ul>
						<li><a href="">OMG</a></li>
						<li><a href="">CORBA</a></li>
						<li><a href="">XML</a></li>
						<li><a href="">OMG AND THE ALL</a></li>
						<li><a href="">MEMBER ONLY</a></li>
					</ul>
				</nav>	
				<div>
					<form action="get">
						<xsl:for-each select="Formulario/Preguntas">
							<h2>
								<xsl:value-of select="titulo"/>
							</h2>
							<div class="buttons">
						 <input type="radio" id="cos a" class="Boton" name="pregunta" value="cosa"/>  <label for="xls">
									<xsl:value-of select="opcion">	</xsl:value-of>
								</label>		  <input type="radio" id="cosa" class="Boton" name="pregunta" value="cosa"/>  <label for="html">
									<xsl:value-of select="opcion2">	</xsl:value-of>
								</label>		  <input type="radio" id="cosa" class="Boton" name="pregunta" value="cosa"/>  <label for="css">
									<xsl:value-of select="opcion3">	</xsl:value-of>
								</label>	
						</div>
						</xsl:for-each>
						  <input type="submit" value="Enviar"/>
					</form>
					</div>
				</main>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>