if (!window.UTILS) {
    window.UTILS = {};
}
if (!UTILS.LOAD) {
    UTILS.LOAD = {};
}
if (!UTILS.LOAD.CONFIG) {
    UTILS.LOAD.CONFIG = {};
}

function loadConfig(key, value) {
    if (!value) {
        return UTILS.LOAD.CONFIG[key];
    } else {
        UTILS.LOAD.CONFIG[key] = value;
    }
}

/**
 * 加载JS
 */
function loadJS(url, callBack, callBackArgs) {
    var _e = document.createElement('script'),
        _done = false,
        _debug = loadConfig('debug');
    _e.type = 'text/javascript';
    _e.onload = _e.onreadystatechange = function () {
        if (!_done && (!this.readyState || this.readyState == 'loaded' || this.readyState == 'complete')) {
            _done = true;
            if (typeof callBack === 'function') {
                callBack(callBackArgs);
            }
            // Handle memory leak in IE
            _e.onload = _e.onreadystatechange = null;
            _e.parentNode.removeChild(_e);
        }
    };
    _e.src = url + (_debug ? ('?t=' + (new Date()).getTime()) : '');
    document.body.appendChild(_e);
}

/**
 * 链式加载JS
 */
function chainLoadJS() {
    if (arguments.length > 0) {
        var args = [].slice.call(arguments);
        var first_url = args.shift();
        if (first_url) {
            if (first_url instanceof Array) {
                args = first_url;
                first_url = args.shift();
            }
            if (args && (args instanceof Array) && args.length > 0) {
                loadJS(first_url, arguments.callee, args);
            } else {
                loadJS(first_url);
            }
        } else {
            console.log('应该永远都不会执行到这里吧');
        }
    }
}

/**
 * 加载CSS
 */
function loadCSS(url, callBack) {
    var _e = document.createElement('link'),
        _done = false,
        _debug = loadConfig('debug');
    _e.type = 'text/css';
    _e.rel = 'stylesheet';
    _e.media = 'screen';
    _e.onload = _e.onreadystatechange = function () {
        if (!_done && (!this.readyState || this.readyState == 'loaded' || this.readyState == 'complete')) {
            _done = true;
            if (typeof callBack === 'function') {
                callBack();
            }
            // Handle memory leak in IE
            _e.onload = _e.onreadystatechange = null;
        }
    };
    _e.href = url + (_debug ? ('?t=' + (new Date()).getTime()) : '');
    (document.querySelector('head') || document.body).appendChild(_e);
}