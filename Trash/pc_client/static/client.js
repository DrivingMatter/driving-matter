/*global $, WebSocket, console, window, document*/
"use strict";

/**
 * Connects to Pi server and receives video data.
 */
var CameraOne = {

    // Connects to Pi via websocket
    connect: function (port) {
        var self = this, 
        video = document.getElementById("video");

        this.socket = new WebSocket("ws://localhost:" + port + "/CameraOne");

        // Request the video stream once connected
        this.socket.onopen = function () {
            console.log("Connected!");
            self.readCamera();  
        };

        // Currently, all returned messages are video data. However, this is
        // extensible with full-spec JSON-RPC.
        this.socket.onmessage = function (messageEvent) {
            video.src = "data:image/jpeg;base64," + messageEvent.data;
        };
    },
    readCamera: function() {
        this.socket.send("read_camera");  
    }
};

var ActionAndSensor = {

    // Connects to Pi via websocket
    connect: function (port) {
        var self = this;
        
        this.socket = new WebSocket("ws://localhost:" + port + "/ActionAndSensor");

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
    sendAction: function(msg) {
        this.socket.send(msg);
    }
};
