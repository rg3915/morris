$(function() {
	new Morris.Donut({
	  element: 'donutchart',
	  data: [
	    { label: 'verde', value: 10 },
	    { label: 'laranja', value: 10 },
	    { label: 'azul', value: 20 },
	    { label: 'amarelo', value: 30 },
	    { label: 'roxo', value: 16 },
	    { label: 'vermelho', value: 14 }
	  ],
	  colors: [
	    '#8a9b0f', // verde
	    '#FF6600', // laranja
	    '#000066', // azul
	    '#FFDE00', // amarelo
	    '#490a3d', // roxo
	    '#FF0000'  // vermelho
	  ],
	  formatter: function (x) { return x + "%"}
	});

	var day_data = [
	  {"period": "2015-10-01", "licensed": 3407, "sorned": 660},
	  {"period": "2015-09-30", "licensed": 3351, "sorned": 629},
	  {"period": "2015-09-29", "licensed": 3269, "sorned": 618},
	  {"period": "2015-09-25", "licensed": 4500, "sorned": 1000},
	  {"period": "2015-09-20", "licensed": 3746, "sorned": 661},
	  {"period": "2015-09-19", "licensed": 3957, "sorned": 667},
	  {"period": "2015-09-18", "licensed": 3600, "sorned": 627},
	  {"period": "2015-09-17", "licensed": 2571, "sorned": 660},
	  {"period": "2015-09-16", "licensed": 3171, "sorned": 676},
	  {"period": "2015-09-15", "licensed": 1201, "sorned": 300},
	  {"period": "2015-09-10", "licensed": 0, "sorned": 0}
	];
	Morris.Line({
	  element: 'graph',
	  data: day_data,
	  xkey: 'period',
	  ykeys: ['licensed', 'sorned'],
	  labels: ['Licensed', 'SORN'],
	  lineColors: [
	  	'#1f3a93', // azul
	  	'#96a5a6', // cinza
	  ]
	});
    // new Morris.Donut({
        // element: 'genderchart',
        // data: [
            // {% for gender in object_list %}
                // { label: "{{ gender.gender }}", value:  {{ gender.gender }}},
            // {%endfor%}
            // ],
        // });

	Morris.Bar({
        element: 'barchart',
        data: [{
            y: '2009',
            a: 100,
            b: 90
        }, {
            y: '2010',
            a: 75,
            b: 65
        }, {
            y: '2011',
            a: 50,
            b: 40
        }, {
            y: '2012',
            a: 75,
            b: 65
        }, {
            y: '2013',
            a: 50,
            b: 40
        }, {
            y: '2014',
            a: 75,
            b: 65
        }, {
            y: '2015',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true,
        barColors: [
		    '#FF6600', // laranja
		    '#000066', // azul
		],
    });

	Morris.Area({
        element: 'areachart',
        data: [{
            period: '2013 Q1',
            iphone: 2666,
            ipad: null,
            itouch: 2647
        }, {
            period: '2013 Q2',
            iphone: 2778,
            ipad: 2294,
            itouch: 2441
        }, {
            period: '2013 Q3',
            iphone: 4912,
            ipad: 1969,
            itouch: 2501
        }, {
            period: '2013 Q4',
            iphone: 3767,
            ipad: 3597,
            itouch: 5689
        }, {
            period: '2014 Q1',
            iphone: 6810,
            ipad: 1914,
            itouch: 2293
        }, {
            period: '2014 Q2',
            iphone: 5670,
            ipad: 4293,
            itouch: 1881
        }, {
            period: '2014 Q3',
            iphone: 4820,
            ipad: 3795,
            itouch: 1588
        }, {
            period: '2014 Q4',
            iphone: 15073,
            ipad: 5967,
            itouch: 5175
        }, {
            period: '2015 Q1',
            iphone: 10687,
            ipad: 4460,
            itouch: 2028
        }, {
            period: '2015 Q2',
            iphone: 8432,
            ipad: 5713,
            itouch: 1791
        }],
        xkey: 'period',
        ykeys: ['iphone', 'ipad', 'itouch'],
        labels: ['iPhone', 'iPad', 'iPod Touch'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true,
        lineColors: [
            '#FFDE00', // amarelo
            '#FF6600', // laranja
            '#000066', // azul
            '#8a9b0f', // verde
            '#490a3d', // roxo
            '#FF0000'  // vermelho
        ],
    });
});
