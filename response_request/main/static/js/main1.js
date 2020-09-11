$(document).ready(function () {
function sleep(ms) {
ms += new Date().getTime();
while (new Date() < ms){}
};
function sendData() {
    var server = "/urlresponse"; // Адрес, куда нужно запрос отправить
    var data = {}
    $.ajax({
      url: server,
      method: "POST",
      data: data,
      success: function(data) {
        let data_urls = data.urls;
        for (name_url in data_urls){
          var stat = $('#'+data.urls[name_url].id+ ' .status_response_body');
          if (data.urls[name_url].status){
            stat.removeClass('passive');
            stat.addClass('active');
            
          }
          else {
            stat.removeClass('active');
            stat.addClass('passive');
          };
        };
        }});

  
}
var settime = Number($('.interval').html()) * 1000;
setInterval( () => {
    sendData()
}, settime)
  

});
