function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


var GRAD_YEARS = [
{value: '95', text: '1995'},
{value: '96', text: '1996'},
{value: '97', text: '1997'},
{value: '98', text: '1998'},
{value: '99', text: '1999'},
{value: '00', text: '2000'},
{value: '01', text: '2001'},
{value: '02', text: '2002'},
{value: '03', text: '2003'},
{value: '04', text: '2004'},
{value: '05', text: '2005'},
{value: '06', text: '2006'},
{value: '07', text: '2007'},
{value: '08', text: '2008'},
{value: '09', text: '2009'},
{value: '10', text: '2010'},
{value: '11', text: '2011'},
{value: '12', text: '2012'},
{value: '13', text: '2013'},
{value: '14', text: '2014'},
{value: '15', text: '2015'},
{value: '16', text: '2016'},
{value: '17', text: '2017'},
{value: '18', text: '2018'}];

var YEAR_JOINED = [
{value: 'F95', text: 'Fall 1995'},
{value: 'F96', text: 'Fall 1996'},
{value: 'F97', text: 'Fall 1997'},
{value: 'F98', text: 'Fall 1998'},
{value: 'F99', text: 'Fall 1999'},
{value: 'F00', text: 'Fall 2000'},
{value: 'F01', text: 'Fall 2001'},
{value: 'F02', text: 'Fall 2002'},
{value: 'F03', text: 'Fall 2003'},
{value: 'F04', text: 'Fall 2004'},
{value: 'F05', text: 'Fall 2005'},
{value: 'F06', text: 'Fall 2006'},
{value: 'F07', text: 'Fall 2007'},
{value: 'F08', text: 'Fall 2008'},
{value: 'F09', text: 'Fall 2009'},
{value: 'F10', text: 'Fall 2010'},
{value: 'F11', text: 'Fall 2011'},
{value: 'F12', text: 'Fall 2012'},
{value: 'F13', text: 'Fall 2013'},
{value: 'F14', text: 'Fall 2014'},
{value: 'F15', text: 'Fall 2015'},
{value: 'S95', text: 'Spring 1995'},
{value: 'S96', text: 'Spring 1996'},
{value: 'S97', text: 'Spring 1997'},
{value: 'S98', text: 'Spring 1998'},
{value: 'S99', text: 'Spring 1999'},
{value: 'S00', text: 'Spring 2000'},
{value: 'S01', text: 'Spring 2001'},
{value: 'S02', text: 'Spring 2002'},
{value: 'S03', text: 'Spring 2003'},
{value: 'S04', text: 'Spring 2004'},
{value: 'S05', text: 'Spring 2005'},
{value: 'S06', text: 'Spring 2006'},
{value: 'S07', text: 'Spring 2007'},
{value: 'S08', text: 'Spring 2008'},
{value: 'S09', text: 'Spring 2009'},
{value: 'S10', text: 'Spring 2010'},
{value: 'S11', text: 'Spring 2011'},
{value: 'S12', text: 'Spring 2012'},
{value: 'S13', text: 'Spring 2013'},
{value: 'S14', text: 'Spring 2014'},
{value: 'S15', text: 'Spring 2015'}];

$.fn.editable.defaults.mode = 'inline';
$(document).ready(function() {
    $('#email').editable();
    $('#github').editable();
    $('#linkedin').editable();
    $('#personal_website').editable();
	$('#bio').editable();
    $('#name').editable({
        validate: function(value) {
            var myRe = /([a-zA-Z]+\s+[a-zA-Z]+)/;
            var validate = myRe.exec($.trim(value));
            console.log(validate);
            if(!validate) return 'Input must match: First_Name Last_Name';
        }
    });
    $('#grad_year').editable({
        type: 'select',
        pk: 1,
        source: GRAD_YEARS,
        url: '/myprofile/',
        title: 'Choose Grad Year',
    });
    $('#year_joined').editable({
        type: 'select',
        pk: 1,
        source: YEAR_JOINED,
        url: '/myprofile/',
        title: 'Choose Year Joined',
    });

    $("#myModal3").on("hide.bs.modal", function() {
        location.reload(true);
    });

    $("#myModal4").on("hide.bs.modal", function() {
        location.reload(true);
    });
});

var days = [
  {value: 0, text:"Monday"},
  {value: 1, text:"Tuesday"},
  {value: 2, text:"Wednesday"},
  {value: 3, text:"Thursday"},
  {value: 4, text:"Friday"},
  {value: 5, text:"Saturday"},
  {value: 6, text:"Sunday"},
];

var times = [
  {value: 9, text:"9am - 10am"},
  {value: 10, text:"10am - 11am"},
  {value: 11, text:"11am - 12pm"},
  {value: 12, text:"12pm - 1pm"},
  {value: 13, text:"1pm - 2pm"},
  {value: 14, text:"2pm - 3pm"},
  {value: 15, text:"3pm - 4pm"},
  {value: 16, text:"4pm - 5pm"}
];

function resetModalForm() {
    var container = document.getElementById("modal-hour-container");
    var rows = container.getElementsByClassName("row");

    if (rows.length == 0) {
      addModalField();
    } else {
      while (container.getElementsByClassName("row").length > 1) {
        removeModalField();
      }
    }   
};

function addModalField() {
    var containerAdd = document.getElementById("modal-hour-container");
    var day_select_elements = containerAdd.getElementsByClassName("filter days");
    var time_select_elements = containerAdd.getElementsByClassName("filter times");

    var select_day = document.createElement("select");
    
    for (var i = 0; i < days.length; i++) {
        var day = days[i];
        var opt = document.createElement("option");
        opt.value = day.value;
        opt.text = day.text;
        select_day.appendChild(opt);
    }
    var day_num = day_select_elements.length + 1;
    select_day.name = "day_value" + day_num;
    select_day.className = "filter days";

    var select_time = document.createElement("select");
    for (var i = 0; i < times.length; i++) {
        var time = times[i];
        var opt = document.createElement("option");
        opt.value = time.value;
        opt.text = time.text;
        select_time.appendChild(opt);
    }
    var time_num = time_select_elements.length + 1;
    select_time.name = "time_value" + time_num;
    select_time.className = "filter times";

    var row = document.createElement("div");
    row.className = "row";

    var day_col = document.createElement("div");
    day_col.className = "col-md-5";
    var time_col = document.createElement("div");
    time_col.className = "col-md-5";
    day_col.appendChild(select_day);
    time_col.appendChild(select_time);

    row.appendChild(day_col);
    row.appendChild(time_col);

    containerAdd.appendChild(row);

};

function removeModalField() {
    var containerRemove = document.getElementById("modal-hour-container");
    var rows = containerRemove.getElementsByClassName("row");
    
    if (rows.length > 1) {
      // need to remove one row from the list of time selections possible
      containerRemove.removeChild(rows[rows.length - 1]);
    }
};

$(function() {
    $('input[type=submit]').attr('class', $('input').attr('class') + ' btn btn-primary');
});




