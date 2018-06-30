(function(){
  var $ = jQuery;
  $(function() {
    permission('dashboard:zxlerator','#dashboard-zxlerator');
    permission('dashboard:investments','#dashboard-investments');
    permission('dashboard:concept','#dashboard-concept');
    permission('dashboard:reports','#dashboard-reports');
    permission('dashboard:bex','#dashboard-bex');
  });

  function permission(rule, domQuery) {
    var url = '/api/permissions?rule=' + rule;
    $.get(url, function(data) {
      if(data.allowed) {
        if(domQuery) {
          $(domQuery).show();
          $('.dashboard').show();
        }
      }
    });
  }
})();
