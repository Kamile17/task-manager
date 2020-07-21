$(document).ready(function(){
  
  var user = '{{ request.user }}';
  function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
  var csrftoken = getToken('csrftoken');


  var select = $(".status-dropdown")
  for(i = 0; i < select.length; i++){
    select[i].addEventListener('change', function(){
      var taskId = this.getAttribute("data-taskId")
      var status = this.value
      console.log(taskId, status)
      updateStatus(taskId, status)
      $("#complete-task-form").submit();
    });
  }


  function updateStatus(taskId, status){
    var url = "/update_status/"
    console.log("url: ", url)
    fetch(url, {
      method: "POST",
      headers:{
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body:JSON.stringify({'taskId': taskId, 'status': status})
    })

    .then((response) => {
      return response.json()
    })
  }
})
