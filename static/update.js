var objDiv = document.getElementsByClassName("messages")[0];
objDiv.scrollTop = objDiv.scrollHeight;$(function() {
  $("#message").focus();
});
setInterval(() => {
        $.ajax({
            type: "GET",
            url: "/dictionary",
            success: function(data) {
                let messages = "";
                for (let i = 0; i < data.length; i++) {
                    messages += data[i][0] + ": " + data[i][1] + "<br>";
                }
                $("#messages").html(messages);
            }
        });
    }, 1000);