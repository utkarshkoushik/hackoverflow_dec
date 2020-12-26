const socket = io.connect('http://localhost:8000');

// Query DOM
var message = document.getElementById('message'),
    user = document.getElementById('user'),
    btn = document.getElementById('send'),
    output = document.getElementById('output'),
    feedback = document.getElementById('feedback');

// Emit events
btn.addEventListener('click', function(){
    socket.emit('chat', {
        message: message.value,
        user: user.value
    });
    message.value = "";
});

message.addEventListener('keypress', function(){
    socket.emit('typing', user.value);
})

// Listen for events
socket.on('chat', function(data){
    feedback.innerHTML = '';
    output.innerHTML += '<p><strong>' + data.user + ': </strong>' + data.message + '</p>';
});

socket.on('typing', function(data){
    feedback.innerHTML = '<p><em>' + data + ' is typing a message...</em></p>';
});