class PrivateSocket {
    constructor(rurl, sid, rid) {
        this.rurl = rurl;
        this.sid = sid;
        this.rid = rid;
        this.room_name = "chat_" + Math.min(sid, rid) + "_" + Math.max(sid, rid);
        this.route_url = "ws://101.35.183.71:10000/ws/chat/" + this.room_name + "/";
        this.ws = new WebSocket(this.route_url);
        this.receive();
    }

    receive() {
        let outer = this;
        this.ws.onmessage = function(e) {
            let data = JSON.parse(e.data);
            if (data.sid == outer.sid) return false;
            if (data.event == "send_message") {
                outer.receive_message(data.text);
            }
        };
    }

    receive_message(content) {
        var $message = $(`
        <div class="chat-fieldbox-body-show-message-receive">
            <div class="chat-fieldbox-body-show-message-receive-img">
                <img class="receive-img">
            </div>
            <div class="chat-fieldbox-body-show-message-receive-item"></div>
        </div>
        `);
        var $item = $message.find(".chat-fieldbox-body-show-message-receive-item");
        var $img = $message.find(".receive-img");
        $img.attr('src', this.rurl);
        $item.append(content);
        $('#chat-fieldbox-body-show').append($message);
        move_to_end("chat-fieldbox-body-show");
    }

    move_to_end(divid) {
        var obj = $("#" + divid);
        if (obj.length)
            obj.scrollTop(obj[0].scrollHeight - obj.height());
    }


    send_message(text) {
        let outer = this;
        this.ws.send(JSON.stringify({
            'event': "send_message",
            'sid': outer.sid,
            'rid': outer.rid,
            'text': text,
        }));
    }
}
