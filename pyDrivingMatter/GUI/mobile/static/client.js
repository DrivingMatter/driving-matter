/*global $, WebSocket, console, window, document*/
"use strict";

/**
 * Connects to Pi server and receives video data.
 */
var State = {

    // Connects to Pi via websocket
    connect: function (ip, port) {
        var self = this, 
        video = document.getElementById("video");

        this.socket = new WebSocket("ws://" + ip + ":" + port + "/state");

        // Request the video stream once connected
        this.socket.onopen = function () {
            console.log("Connected State!");
            self.readState();  
        };

        // Currently, all returned messages are video data. However, this is
        // extensible with full-spec JSON-RPC.
        this.socket.onmessage = function (messageEvent) {
            video.src = "data:image/jpeg;base64," + messageEvent.data;
        };
    },
    readState: function() {
        this.socket.send("read_state");  
    }
    stopState: function() {
        this.socket.send("stop_read_state");  
    }
};

var Action = {

    // Connects to Pi via websocket
    connect: function (ip, port) {
        var self = this;
        
        this.socket = new WebSocket("ws://" + ip + ":" + port + "/action");

        // Request the video stream once connected
        this.socket.onopen = function () {
            console.log("Connected Sensors!");
        };

        // Currently, all returned messages are video data. However, this is
        // extensible with full-spec JSON-RPC.
        this.socket.onmessage = function (messageEvent) {            
            console.log(messageEvent);
        };
    },
    sendAction: function(method) {
    	payload = "action " + method + " " + step + " "  + Date()
    	console.log(payload)
        this.socket.send(payload);
    }
};
