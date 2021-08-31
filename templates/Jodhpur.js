// JavaScript source code
function getBathValue() {
    var uiBath = document.getElementsByName("uiBath");
    for(var i in uiBath) {
      if(uiBath[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedCalculatePrice() {
    console.log("Calculate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bath = getBathValue();
    var location = document.getElementById("uiLocations");
    var calPrice = document.getElementById("uiCalculatePrice");
  
    var url = "";
    
  
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bath,
        location: location.value
    },function(data, status) {
        console.log(data.price_calculate);
        calPrice.innerHTML = "<h2>" + data.price_calculate.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  
  function onPageLoad() {
    var url = " "; 
    $.get(url,function(data, status) {
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;