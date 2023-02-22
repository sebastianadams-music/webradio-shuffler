

var webradio = {
    player: function (i) {
        let id = "player" + i 
        return document.getElementById(id);
    },
    play_station: function (i, url){
        let id = "player" + i 
        document.getElementById(id).src = url;
        document.url = url
    },
    get_value: function (key) {
        if (window.localStorage[key] != undefined) {
            return window.localStorage[key];
        }
    },
    set_value: function (key, value) {
        window.localStorage[key] = value;
    }
};



