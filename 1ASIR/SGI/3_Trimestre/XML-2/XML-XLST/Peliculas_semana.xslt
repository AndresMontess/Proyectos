<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:math="http://www.w3.org/2005/xpath-functions/math" xmlns:array="http://www.w3.org/2005/xpath-functions/array" xmlns:map="http://www.w3.org/2005/xpath-functions/map" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:err="http://www.w3.org/2005/xqt-errors" exclude-result-prefixes="array fn map math xhtml xs err" version="3.0">
	<xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:template match="/" name="xsl:initial-template">
		<html>
			<head>
				<link type="text/css" rel="stylesheet" href="./CSS/ESTILO.css"/>
			</head>
			<body>
				<header>
				<h1>Cartelera</h1>
					<nav class="nav">
						<a href="" class="nav2">Todos</a>
						<a href="" class="nav2">En Cartelera</a>
						<a href="" class="nav2">Próximos</a>
					</nav>
				</header>
				<main>
					<div class="padre">
						<xsl:for-each select="Pelis/pelicula">
							<p class="nombre"></p>
								<xsl:value-of select="nombre"/>
							<img class="imagen">
								<xsl:attribute name="src">
									<xsl:value-of select="foto"/>
								</xsl:attribute>
							</img>
						</xsl:for-each>
					</div>
					<div class="padre2">
					<a href="https://www.youtube.com/watch?v=FSyWAxUg3Go" class="avatar">VER TRAILER</a>
					<a href="https://www.youtube.com/watch?v=FSyWAxUg3Go" class="Bros">VER TRAILER</a>
					<a href="https://www.youtube.com/watch?v=FSyWAxUg3Go" class="shazam">VER TRAILER</a>
					</div>
				</main>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>