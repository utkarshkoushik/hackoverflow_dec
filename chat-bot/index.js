
const express = require('express');
const socket = require('socket.io');
const port =8000;

// App setup
const app = express();
const server=app.listen(port,function(err)
{
    if(err)
    {
        console.log('error in running the server:'+port);

    }
    else{
        console.log('server is running on the port: '+port);
    }
});

// using Static files
app.use(express.static('assets'));

// setting up caht server & pass server
const io = socket(server);
io.on('connection', (socket) => {

    console.log('connection established', socket.id);

    // Handle chat event
    socket.on('chat', function(data){
        // console.log(data);
        io.sockets.emit('chat', data);
    });

    // Handle typing event
    socket.on('typing', function(data){
        socket.broadcast.emit('typing', data);
    });

});