// Flutter web app
console.log("Flutter ready");
window.connect = function() {
    const ws = new WebSocket(`ws://${location.host}/ws/chat?access_key=nano`);
    ws.onmessage = (e) => {
        const data = JSON.parse(e.data);
        const div = document.createElement('div');
        div.textContent = data.content;
        document.getElementById('messages').appendChild(div);
    };
    window.send = () => {
        const input = document.getElementById('input');
        ws.send(JSON.stringify({content: input.value}));
        input.value = '';
    };
};
connect();
