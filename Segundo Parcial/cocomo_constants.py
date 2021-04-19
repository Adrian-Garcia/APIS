tipo_de_sistema = { 
	'organico': {
		'aBasico': 2.4,
		'aIntermedio': 3.2,
		'b': 1.05,
		'C': 2.5,
		'd': 0.38
	},

	'semiacoplado': {
		'aBasico': 3.0,
		'aIntermedio': 3.0,
		'b': 1.12,
		'C': 2.5,
		'd': 0.35
	},

	'empotrado': {
		'aBasico': 3.6,
		'aIntermedio': 2.8,
		'b': 1.2,
		'C': 2.05,
		'd': 0.32
	}
}

factores_cocomo_intermedio = {
	# Atributos del producto
	'RELY' : {
		'MB' : 0.75,
		'B' : 0.88,
		'N' : 1,
		'A' : 1.15,
		'MA' : 1.4,
		'EA' : None
	},

	'DATA' : {
		'MB' : None,
		'B' : 0.94,
		'N' : 1,
		'A' : 1.08,
		'MA' : 1.16,
		'EA' : None
	},

	'CPLX' : {
		'MB' : 0.7,
		'B' : 0.85,
		'N' : 1,
		'A' : 1.15,
		'MA' : 1.3,
		'EA' : 1.65
	},

	# Atributos del hardware
	'TIME' : {
		'MB' : None,
		'B' : None,
		'N' : 1,
		'A' : 1.11,
		'MA' : 1.3,
		'EA' : 1.66
	},

	'STOR' : {
		'MB' : None,
		'B' : None,
		'N' : 1,
		'A' : 1.06,
		'MA' : 1.21,
		'EA' : 1.56
	},

	'VIRT' : {
		'MB' : None,
		'B' : 0.87,
		'N' : 1,
		'A' : 1.15,
		'MA' : 1.3,
		'EA' : None
	},

	'TURN' : {
		'MB' : None,
		'B' : 0.87,
		'N' : 1,
		'A' : 1.07,
		'MA' : 1.15,
		'EA' : None
	},

	# Atributos del personal
	'ACAP' : {
		'MB' : 1.46,
		'B' : 1.19,
		'N' : 1,
		'A' : 0.86,
		'MA' : 0.71,
		'EA' : None
	},

	'AEXP' : {
		'MB' : 1.29,
		'B' : 1.13,
		'N' : 1,
		'A' : 0.91,
		'MA' : 0.82,
		'EA' : None
	},

	'PCAP' : {
		'MB' : 1.42,
		'B' : 1.17,
		'N' : 1,
		'A' : 0.86,
		'MA' : 0.7,
		'EA' : None
	},

	'VEXP' : {
		'MB' : 1.21,
		'B' : 1.1,
		'N' : 1,
		'A' : 0.9,
		'MA' : None,
		'EA' : None
	},

	'LEXP' : {
		'MB' : 1.14,
		'B' : 1.07,
		'N' : 1,
		'A' : 0.95,
		'MA' : None,
		'EA' : None
	},

	# Atributos del proyecto
	'TOOL' : {
		'MB' : 1.24,
		'B' : 1.1,
		'N' : 1,
		'A' : 0.91,
		'MA' : 0.82,
		'EA' : None
	},

	'MODP' : {
		'MB' : 1.24,
		'B' : 1.1,
		'N' : 1,
		'A' : 0.91,
		'MA' : 0.83,
		'EA' : None
	},

	'SCED' : {
		'MB' : 1.23,
		'B' : 1.08,
		'N' : 1,
		'A' : 1.04,
		'MA' : 1.1,
		'EA' : None
	}
}

salario_promedio_por_recurso = 4000
