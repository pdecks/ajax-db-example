"use strict";


// PART 1: SHOW A FORTUNE

function getFortune(evt) {

    // TODO: get the fortune and show it in the #fortune-text div
    // call getFortune()
    $.get('/fortune', replaceFortune);
}

function replaceFortune(result) {
    var fortune = result;
    $('#fortune-text').html(fortune);

}
$('#get-fortune-button').on('click', getFortune);





// PART 2: SHOW WEATHER
function getForecast(results){
    var forecast = results.forecast;
    console.log(forecast);
    $('#weather-info').html(forecast);

}

function showWeather(evt) {
    evt.preventDefault();

    // var zipcode = $("#zipcode-field").val()

    var url = "/weather.json?zipcode=" + $("#zipcode-field").val();
    console.log(url);


    // TODO: request weather with that URL and show the forecast in #weather-info
    $.get(url, getForecast);
    // $.get("/weather.json", {'zipcode': zipcode }, getForecast);

}

$("#weather-form").on('submit', showWeather);




// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    // TODO: show the result message after your form
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}

$("#order-form").on('submit', orderMelons);
