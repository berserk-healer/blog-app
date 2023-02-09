// Auto close bootstrap message after 3 seconds
let message_ele = document.getElementById("bootstrap-message");

setTimeout(()=>{
    message_ele.remove();
}, 3000);