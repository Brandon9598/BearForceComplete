$.getScript('http://arshaw.com/js/fullcalendar-1.6.4/fullcalendar/fullcalendar.min.js',function(){
  
  var date = new Date();
  var d = date.getDate();
  var m = date.getMonth();
  var y = date.getFullYear();
  
  $('#calendar').fullCalendar({
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    editable: true,
    events: [
      {
        title: 'Equipment Center',
        start: new Date(y, m, 5, 2, 0),
        allDay: false
      },  
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 5, 3, 0),
        allDay: false
      },
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 12, 2, 0),
        allDay: false
      },   
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 12, 3, 0),
        allDay: false
      },
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 15, 18, 0),
        allDay: false
      },
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 19, 2, 0),
        allDay: false
      },   
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 19, 3, 0),
        allDay: false
      },
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 26, 2, 0),
        allDay: false
      },   
	  {
        title: 'Equipment Center',
        start: new Date(y, m, 26, 3, 0),
        allDay: false
      },
    ]
  });
})