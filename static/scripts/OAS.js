      
var OAS = {
    
    url:'http://oasde.jornada.com.mx/RealMedia/ads/',
    sitepage:'www.jornada.unam.mx/ultimas',
    listpos:['Top','TopLeft','TopRight','Right1','Right2','Right3','Right4','Right5','Bottom','Middle',],
    query:'',
    target:'_blank',
    
    rns: Math.random ().toString ().substring (2, 11),
    version: ((navigator.userAgent.indexOf('Mozilla/3') != -1) || (navigator.userAgent.indexOf('Mozilla/4.0 WebTV') != -1))? 10: 11,
    
    linkGen: function (cgi, pos) {
	pos = (pos)? '!' + pos: '';
	return this.url + cgi + '/' + this.sitepage + '/1' + this.rns + '@' + this.listpos.join (',') + pos + '?' + this.query;
    },
    
    normal: function (pos) {
      document.write('<a href="' + this.linkGen ('click_nx.ads', pos) + '" target=' + this.target + '>');
	document.write('<img src="' + this.linkGen ('adstream_nx.ads', pos) + '" border="0"><\/a>');
    },
    
    ad: function (pos) {
	if (this.version > 10)
	    OAS_RICH (pos);
	else
	    this.normal (pos);
    }
};

if (OAS.version > 10)
    document.write('<script type="text/javascript" src="' + OAS.linkGen ('adstream_mjx.ads') + '"><\/script>');
