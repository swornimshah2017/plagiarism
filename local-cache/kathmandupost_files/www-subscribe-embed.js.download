(function(){var k,aa="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ba;
if("function"==typeof Object.setPrototypeOf)ba=Object.setPrototypeOf;else{var ca;a:{var da={cb:!0},ea={};try{ea.__proto__=da;ca=ea.cb;break a}catch(a){}ca=!1}ba=ca?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}
var fa=ba,ha="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)},ia="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this;
function ja(a,b){if(b){for(var c=ia,d=a.split("."),e=0;e<d.length-1;e++){var f=d[e];f in c||(c[f]={});c=c[f]}d=d[d.length-1];e=c[d];f=b(e);f!=e&&null!=f&&ha(c,d,{configurable:!0,writable:!0,value:f})}}
function ka(){ka=function(){};
ia.Symbol||(ia.Symbol=la)}
var la=function(){var a=0;return function(b){return"jscomp_symbol_"+(b||"")+a++}}();
function ma(){ka();var a=ia.Symbol.iterator;a||(a=ia.Symbol.iterator=ia.Symbol("iterator"));"function"!=typeof Array.prototype[a]&&ha(Array.prototype,a,{configurable:!0,writable:!0,value:function(){return oa(this)}});
ma=function(){}}
function oa(a){var b=0;return pa(function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}})}
function pa(a){ma();a={next:a};a[ia.Symbol.iterator]=function(){return this};
return a}
var qa=function(){function a(){function a(){}
Reflect.construct(a,[],function(){});
return new a instanceof a}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(a,d,e){a=b(a,d);e&&Reflect.setPrototypeOf(a,e.prototype);return a}}return function(a,b,e){void 0===e&&(e=a);
e=aa(e.prototype||Object.prototype);return Function.prototype.apply.call(a,e,b)||e}}();
ja("Reflect.construct",function(){return qa});
function ra(a){ma();var b=a[Symbol.iterator];return b?b.call(a):oa(a)}
function sa(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
ja("WeakMap",function(a){function b(a){this.b=(f+=Math.random()+1).toString();if(a){ka();ma();a=ra(a);for(var b;!(b=a.next()).done;)b=b.value,this.set(b[0],b[1])}}
function c(a){sa(a,e)||ha(a,e,{value:{}})}
function d(a){var b=Object[a];b&&(Object[a]=function(a){c(a);return b(a)})}
if(function(){if(!a||!Object.seal)return!1;try{var b=Object.seal({}),c=Object.seal({}),d=new a([[b,2],[c,3]]);if(2!=d.get(b)||3!=d.get(c))return!1;d["delete"](b);d.set(c,4);return!d.has(b)&&4==d.get(c)}catch(n){return!1}}())return a;
var e="$jscomp_hidden_"+Math.random();d("freeze");d("preventExtensions");d("seal");var f=0;b.prototype.set=function(a,b){c(a);if(!sa(a,e))throw Error("WeakMap key fail: "+a);a[e][this.b]=b;return this};
b.prototype.get=function(a){return sa(a,e)?a[e][this.b]:void 0};
b.prototype.has=function(a){return sa(a,e)&&sa(a[e],this.b)};
b.prototype["delete"]=function(a){return sa(a,e)&&sa(a[e],this.b)?delete a[e][this.b]:!1};
return b});
ja("Map",function(a){function b(){var a={};return a.previous=a.next=a.head=a}
function c(a,b){var c=a.b;return pa(function(){if(c){for(;c.head!=a.b;)c=c.previous;for(;c.next!=c.head;)return c=c.next,{done:!1,value:b(c)};c=null}return{done:!0,value:void 0}})}
function d(a,b){var c=b&&typeof b;"object"==c||"function"==c?f.has(b)?c=f.get(b):(c=""+ ++g,f.set(b,c)):c="p_"+b;var d=a.f[c];if(d&&sa(a.f,c))for(var e=0;e<d.length;e++){var h=d[e];if(b!==b&&h.key!==h.key||b===h.key)return{id:c,list:d,index:e,A:h}}return{id:c,list:d,index:-1,A:void 0}}
function e(a){this.f={};this.b=b();this.size=0;if(a){a=ra(a);for(var c;!(c=a.next()).done;)c=c.value,this.set(c[0],c[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var b=Object.seal({x:4}),c=new a(ra([[b,"s"]]));if("s"!=c.get(b)||1!=c.size||c.get({x:4})||c.set({x:4},"t")!=c||2!=c.size)return!1;var d=c.entries(),e=d.next();if(e.done||e.value[0]!=b||"s"!=e.value[1])return!1;e=d.next();return e.done||4!=e.value[0].x||"t"!=e.value[1]||!d.next().done?!1:!0}catch(x){return!1}}())return a;
ka();ma();var f=new WeakMap;e.prototype.set=function(a,b){a=0===a?0:a;var c=d(this,a);c.list||(c.list=this.f[c.id]=[]);c.A?c.A.value=b:(c.A={next:this.b,previous:this.b.previous,head:this.b,key:a,value:b},c.list.push(c.A),this.b.previous.next=c.A,this.b.previous=c.A,this.size++);return this};
e.prototype["delete"]=function(a){a=d(this,a);return a.A&&a.list?(a.list.splice(a.index,1),a.list.length||delete this.f[a.id],a.A.previous.next=a.A.next,a.A.next.previous=a.A.previous,a.A.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.f={};this.b=this.b.previous=b();this.size=0};
e.prototype.has=function(a){return!!d(this,a).A};
e.prototype.get=function(a){return(a=d(this,a).A)&&a.value};
e.prototype.entries=function(){return c(this,function(a){return[a.key,a.value]})};
e.prototype.keys=function(){return c(this,function(a){return a.key})};
e.prototype.values=function(){return c(this,function(a){return a.value})};
e.prototype.forEach=function(a,b){for(var c=this.entries(),d;!(d=c.next()).done;)d=d.value,a.call(b,d[1],d[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
ja("Set",function(a){function b(a){this.b=new Map;if(a){a=ra(a);for(var b;!(b=a.next()).done;)this.add(b.value)}this.size=this.b.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var b=Object.seal({x:4}),d=new a(ra([b]));if(!d.has(b)||1!=d.size||d.add(b)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=b||f.value[1]!=b)return!1;f=e.next();return f.done||f.value[0]==b||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
ka();ma();b.prototype.add=function(a){a=0===a?0:a;this.b.set(a,a);this.size=this.b.size;return this};
b.prototype["delete"]=function(a){a=this.b["delete"](a);this.size=this.b.size;return a};
b.prototype.clear=function(){this.b.clear();this.size=0};
b.prototype.has=function(a){return this.b.has(a)};
b.prototype.entries=function(){return this.b.entries()};
b.prototype.values=function(){return this.b.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(a,b){var c=this;this.b.forEach(function(d){return a.call(b,d,d,c)})};
return b});
ja("Object.is",function(a){return a?a:function(a,c){return a===c?0!==a||1/a===1/c:a!==a&&c!==c}});
var m=this;function p(a){return void 0!==a}
function t(a){return"string"==typeof a}
function ta(a){return"number"==typeof a}
function u(a){a=a.split(".");for(var b=m,c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function ua(){}
function va(a){a.ba=void 0;a.v=function(){return a.ba?a.ba:a.ba=new a}}
function wa(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function xa(a){return"array"==wa(a)}
function ya(a){var b=wa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function za(a){return"function"==wa(a)}
function Aa(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Ba(a){return a[Ca]||(a[Ca]=++Da)}
var Ca="closure_uid_"+(1E9*Math.random()>>>0),Da=0;function Ea(a,b,c){return a.call.apply(a.bind,arguments)}
function Fa(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function v(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?v=Ea:v=Fa;return v.apply(null,arguments)}
function Ga(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
var Ha=Date.now||function(){return+new Date};
function y(a,b){var c=a.split("."),d=m;c[0]in d||"undefined"==typeof d.execScript||d.execScript("var "+c[0]);for(var e;c.length&&(e=c.shift());)!c.length&&p(b)?d[e]=b:d[e]&&d[e]!==Object.prototype[e]?d=d[e]:d=d[e]={}}
function z(a,b){function c(){}
c.prototype=b.prototype;a.w=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Pb=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}}
;function Ia(a){if(Error.captureStackTrace)Error.captureStackTrace(this,Ia);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
z(Ia,Error);Ia.prototype.name="CustomError";var Ja;var Ka=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(t(a))return t(b)&&1==b.length?a.indexOf(b,0):-1;
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},A=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=t(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},La=Array.prototype.filter?function(a,b,c){return Array.prototype.filter.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=[],f=0,g=t(a)?a.split(""):a,h=0;h<d;h++)if(h in g){var l=g[h];
b.call(c,l,h,a)&&(e[f++]=l)}return e},Ma=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e=t(a)?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},Na=Array.prototype.some?function(a,b){return Array.prototype.some.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=t(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a))return!0;
return!1};
function Oa(a,b){a:{var c=a.length;for(var d=t(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:t(a)?a.charAt(c):a[c]}
function Pa(a,b){return 0<=Ka(a,b)}
function Qa(a){return Array.prototype.concat.apply([],arguments)}
function Ra(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function Sa(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(ya(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
function Ta(a,b,c,d){return Array.prototype.splice.apply(a,Ua(arguments,1))}
function Ua(a,b,c){return 2>=arguments.length?Array.prototype.slice.call(a,b):Array.prototype.slice.call(a,b,c)}
function Va(a){for(var b=[],c=0;c<arguments.length;c++){var d=arguments[c];if(xa(d))for(var e=0;e<d.length;e+=8192)for(var f=Va.apply(null,Ua(d,e,e+8192)),g=0;g<f.length;g++)b.push(f[g]);else b.push(d)}return b}
;var Wa=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]},Xa=String.prototype.repeat?function(a,b){return a.repeat(b)}:function(a,b){return Array(b+1).join(a)};
function Ya(a){a=p(void 0)?a.toFixed(void 0):String(a);var b=a.indexOf(".");-1==b&&(b=a.length);return Xa("0",Math.max(0,2-b))+a}
function Za(a,b){for(var c=0,d=Wa(String(a)).split("."),e=Wa(String(b)).split("."),f=Math.max(d.length,e.length),g=0;0==c&&g<f;g++){var h=d[g]||"",l=e[g]||"";do{h=/(\d*)(\D*)(.*)/.exec(h)||["","","",""];l=/(\d*)(\D*)(.*)/.exec(l)||["","","",""];if(0==h[0].length&&0==l[0].length)break;c=$a(0==h[1].length?0:parseInt(h[1],10),0==l[1].length?0:parseInt(l[1],10))||$a(0==h[2].length,0==l[2].length)||$a(h[2],l[2]);h=h[3];l=l[3]}while(0==c)}return c}
function $a(a,b){return a<b?-1:a>b?1:0}
function ab(a){return String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()})}
function bb(a){var b=t(void 0)?"undefined".replace(/([-()\[\]{}+?*.$\^|,:#<!\\])/g,"\\$1").replace(/\x08/g,"\\x08"):"\\s";return a.replace(new RegExp("(^"+(b?"|["+b+"]+":"")+")([a-z])","g"),function(a,b,e){return b+e.toUpperCase()})}
;var cb;a:{var db=m.navigator;if(db){var eb=db.userAgent;if(eb){cb=eb;break a}}cb=""}function B(a){return-1!=cb.indexOf(a)}
;function fb(a,b,c){for(var d in a)b.call(c,a[d],d,a)}
function gb(a){var b=[],c=0,d;for(d in a)b[c++]=a[d];return b}
function hb(a){var b=ib,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
var jb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function kb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<jb.length;f++)c=jb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;function lb(){return B("Safari")&&!(mb()||B("Coast")||B("Opera")||B("Edge")||B("Silk")||B("Android"))}
function mb(){return(B("Chrome")||B("CriOS"))&&!B("Edge")}
function nb(){return B("Android")&&!(mb()||B("Firefox")||B("Opera")||B("Silk"))}
;function ob(){return B("iPhone")&&!B("iPod")&&!B("iPad")}
function pb(){return ob()||B("iPad")||B("iPod")}
;function qb(a){qb[" "](a);return a}
qb[" "]=ua;function rb(a,b){var c=sb;return Object.prototype.hasOwnProperty.call(c,a)?c[a]:c[a]=b(a)}
;var tb=B("Opera"),C=B("Trident")||B("MSIE"),ub=B("Edge"),vb=ub||C,wb=B("Gecko")&&!(-1!=cb.toLowerCase().indexOf("webkit")&&!B("Edge"))&&!(B("Trident")||B("MSIE"))&&!B("Edge"),xb=-1!=cb.toLowerCase().indexOf("webkit")&&!B("Edge"),yb=B("Macintosh"),zb=B("Windows"),Ab=B("Android"),Bb=ob(),Cb=B("iPad"),Db=B("iPod"),Eb=pb();function Fb(){var a=m.document;return a?a.documentMode:void 0}
var Gb;a:{var Hb="",Ib=function(){var a=cb;if(wb)return/rv:([^\);]+)(\)|;)/.exec(a);if(ub)return/Edge\/([\d\.]+)/.exec(a);if(C)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(xb)return/WebKit\/(\S+)/.exec(a);if(tb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
Ib&&(Hb=Ib?Ib[1]:"");if(C){var Jb=Fb();if(null!=Jb&&Jb>parseFloat(Hb)){Gb=String(Jb);break a}}Gb=Hb}var Kb=Gb,sb={};function Lb(a){return rb(a,function(){return 0<=Za(Kb,a)})}
var Mb;var Nb=m.document;Mb=Nb&&C?Fb()||("CSS1Compat"==Nb.compatMode?parseInt(Kb,10):5):void 0;var Ob=!wb&&!C||C&&9<=Number(Mb)||wb&&Lb("1.9.1"),Pb=C&&!Lb("9");function Qb(){this.b="";this.f=Rb}
Qb.prototype.aa=!0;Qb.prototype.Z=function(){return this.b};
var Sb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i,Rb={};function Tb(a){var b=new Qb;b.b=a;return b}
Tb("about:blank");function Ub(){this.b="";this.f=Vb}
Ub.prototype.aa=!0;Ub.prototype.Z=function(){return this.b};
function Wb(a){if(a instanceof Ub&&a.constructor===Ub&&a.f===Vb)return a.b;wa(a);return"type_error:SafeHtml"}
var Vb={};function Xb(a){var b=new Ub;b.b=a;return b}
Xb("<!DOCTYPE html>");Xb("");Xb("<br>");function D(a,b){this.x=p(a)?a:0;this.y=p(b)?b:0}
D.prototype.equals=function(a){return a instanceof D&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
function Yb(a,b){return new D(a.x-b.x,a.y-b.y)}
D.prototype.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
D.prototype.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
D.prototype.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Zb(a,b){this.width=a;this.height=b}
k=Zb.prototype;k.fb=function(){return this.width*this.height};
k.aspectRatio=function(){return this.width/this.height};
k.isEmpty=function(){return!this.fb()};
k.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
k.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
k.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function $b(a){return a?new ac(bc(a)):Ja||(Ja=new ac)}
function E(a){return t(a)?document.getElementById(a):a}
function cc(a,b){var c=b||document;return c.querySelectorAll&&c.querySelector?c.querySelectorAll("."+a):dc(document,"*",a,b)}
function F(a,b){var c=b||document;if(c.getElementsByClassName)c=c.getElementsByClassName(a)[0];else{c=document;var d=b||c;c=d.querySelectorAll&&d.querySelector&&a?d.querySelector(a?"."+a:""):dc(c,"*",a,b)[0]||null}return c||null}
function dc(a,b,c,d){a=d||a;b=b&&"*"!=b?String(b).toUpperCase():"";if(a.querySelectorAll&&a.querySelector&&(b||c))return a.querySelectorAll(b+(c?"."+c:""));if(c&&a.getElementsByClassName){a=a.getElementsByClassName(c);if(b){d={};for(var e=0,f=0,g;g=a[f];f++)b==g.nodeName&&(d[e++]=g);d.length=e;return d}return a}a=a.getElementsByTagName(b||"*");if(c){d={};for(f=e=0;g=a[f];f++)b=g.className,"function"==typeof b.split&&Pa(b.split(/\s+/),c)&&(d[e++]=g);d.length=e;return d}return a}
function ec(a,b){fb(b,function(b,d){b&&b.aa&&(b=b.Z());"style"==d?a.style.cssText=b:"class"==d?a.className=b:"for"==d?a.htmlFor=b:fc.hasOwnProperty(d)?a.setAttribute(fc[d],b):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,b):a[d]=b})}
var fc={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};function gc(a){a=a.document;a=hc(a)?a.documentElement:a.body;return new Zb(a.clientWidth,a.clientHeight)}
function ic(a){var b=jc(a);a=kc(a);return C&&Lb("10")&&a.pageYOffset!=b.scrollTop?new D(b.scrollLeft,b.scrollTop):new D(a.pageXOffset||b.scrollLeft,a.pageYOffset||b.scrollTop)}
function jc(a){return a.scrollingElement?a.scrollingElement:!xb&&hc(a)?a.documentElement:a.body||a.documentElement}
function kc(a){return a.parentWindow||a.defaultView}
function hc(a){return"CSS1Compat"==a.compatMode}
function lc(a){a&&a.parentNode&&a.parentNode.removeChild(a)}
function mc(a){return Ob&&void 0!=a.children?a.children:La(a.childNodes,function(a){return 1==a.nodeType})}
function nc(a){return Aa(a)&&1==a.nodeType}
function oc(a,b){if(!a||!b)return!1;if(a.contains&&1==b.nodeType)return a==b||a.contains(b);if("undefined"!=typeof a.compareDocumentPosition)return a==b||!!(a.compareDocumentPosition(b)&16);for(;b&&a!=b;)b=b.parentNode;return b==a}
function bc(a){return 9==a.nodeType?a:a.ownerDocument||a.document}
function pc(a,b){if("textContent"in a)a.textContent=b;else if(3==a.nodeType)a.data=String(b);else if(a.firstChild&&3==a.firstChild.nodeType){for(;a.lastChild!=a.firstChild;)a.removeChild(a.lastChild);a.firstChild.data=String(b)}else{for(var c;c=a.firstChild;)a.removeChild(c);a.appendChild(bc(a).createTextNode(String(b)))}}
function qc(a,b){var c=[];return rc(a,b,c,!0)?c[0]:void 0}
function rc(a,b,c,d){if(null!=a)for(a=a.firstChild;a;){if(b(a)&&(c.push(a),d)||rc(a,b,c,d))return!0;a=a.nextSibling}return!1}
var sc={SCRIPT:1,STYLE:1,HEAD:1,IFRAME:1,OBJECT:1},tc={IMG:" ",BR:"\n"};function uc(a){var b;if((b="A"==a.tagName||"INPUT"==a.tagName||"TEXTAREA"==a.tagName||"SELECT"==a.tagName||"BUTTON"==a.tagName?!a.disabled&&(!vc(a)||wc(a)):vc(a)&&wc(a))&&C){var c;!za(a.getBoundingClientRect)||C&&null==a.parentElement?c={height:a.offsetHeight,width:a.offsetWidth}:c=a.getBoundingClientRect();a=null!=c&&0<c.height&&0<c.width}else a=b;return a}
function vc(a){return C&&!Lb("9")?(a=a.getAttributeNode("tabindex"),null!=a&&a.specified):a.hasAttribute("tabindex")}
function wc(a){a=a.tabIndex;return ta(a)&&0<=a&&32768>a}
function xc(a){if(Pb&&null!==a&&"innerText"in a)a=a.innerText.replace(/(\r\n|\r|\n)/g,"\n");else{var b=[];yc(a,b,!0);a=b.join("")}a=a.replace(/ \xAD /g," ").replace(/\xAD/g,"");a=a.replace(/\u200B/g,"");Pb||(a=a.replace(/ +/g," "));" "!=a&&(a=a.replace(/^\s*/,""));return a}
function yc(a,b,c){if(!(a.nodeName in sc))if(3==a.nodeType)c?b.push(String(a.nodeValue).replace(/(\r\n|\r|\n)/g,"")):b.push(a.nodeValue);else if(a.nodeName in tc)b.push(tc[a.nodeName]);else for(a=a.firstChild;a;)yc(a,b,c),a=a.nextSibling}
function zc(a,b,c,d){if(!b&&!c)return null;var e=b?String(b).toUpperCase():null;return Ac(a,function(a){return(!e||a.nodeName==e)&&(!c||t(a.className)&&Pa(a.className.split(/\s+/),c))},!0,d)}
function G(a,b){return zc(a,null,b,void 0)}
function Ac(a,b,c,d){a&&!c&&(a=a.parentNode);for(c=0;a&&(null==d||c<=d);){if(b(a))return a;a=a.parentNode;c++}return null}
function ac(a){this.b=a||m.document||document}
ac.prototype.getElementsByTagName=function(a,b){return(b||this.b).getElementsByTagName(String(a))};
ac.prototype.createElement=function(a){return this.b.createElement(String(a))};
ac.prototype.appendChild=function(a,b){a.appendChild(b)};
ac.prototype.isElement=nc;/*
 gapi.loader.OBJECT_CREATE_TEST_OVERRIDE &&*/
var Bc=window,Cc=document,Dc=Bc.location;function Ec(){}
var Gc=/\[native code\]/;function H(a,b,c){return a[b]=a[b]||c}
function Hc(a){a=a.sort();for(var b=[],c=void 0,d=0;d<a.length;d++){var e=a[d];e!=c&&b.push(e);c=e}return b}
function Ic(){var a;if((a=Object.create)&&Gc.test(a))a=a(null);else{a={};for(var b in a)a[b]=void 0}return a}
var Jc=H(Bc,"gapi",{});var I;I=H(Bc,"___jsl",Ic());H(I,"I",0);H(I,"hel",10);function Kc(){var a=Dc.href;if(I.dpo)var b=I.h;else{b=I.h;var c=RegExp("([#].*&|[#])jsh=([^&#]*)","g"),d=RegExp("([?#].*&|[?#])jsh=([^&#]*)","g");if(a=a&&(c.exec(a)||d.exec(a)))try{b=decodeURIComponent(a[2])}catch(e){}}return b}
function Lc(a){var b=H(I,"PQ",[]);I.PQ=[];var c=b.length;if(0===c)a();else for(var d=0,e=function(){++d===c&&a()},f=0;f<c;f++)b[f](e)}
function Mc(a){return H(H(I,"H",Ic()),a,Ic())}
;function Nc(){this.b=("undefined"==typeof document?null:document)||{cookie:""}}
k=Nc.prototype;k.isEnabled=function(){return navigator.cookieEnabled};
k.set=function(a,b,c,d,e,f){if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');p(c)||(c=-1);e=e?";domain="+e:"";d=d?";path="+d:"";f=f?";secure":"";c=0>c?"":0==c?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Ha()+1E3*c)).toUTCString();this.b.cookie=a+"="+b+e+d+c+f};
k.get=function(a,b){for(var c=a+"=",d=(this.b.cookie||"").split(";"),e=0,f;e<d.length;e++){f=Wa(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
k.remove=function(a,b,c){var d=p(this.get(a));this.set(a,"",0,b,c);return d};
k.isEmpty=function(){return!this.b.cookie};
k.clear=function(){for(var a=(this.b.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=Wa(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Oc=new Nc;Oc.f=3950;var Pc=H(I,"perf",Ic());H(Pc,"g",Ic());var Qc=H(Pc,"i",Ic());H(Pc,"r",[]);Ic();Ic();function Rc(a,b,c){b&&0<b.length&&(b=Sc(b),c&&0<c.length&&(b+="___"+Sc(c)),28<b.length&&(b=b.substr(0,28)+(b.length-28)),c=b,b=H(Qc,"_p",Ic()),H(b,c,Ic())[a]=(new Date).getTime(),b=Pc.r,"function"===typeof b?b(a,"_p",c):b.push([a,"_p",c]))}
function Sc(a){return a.join("__").replace(/\./g,"_").replace(/\-/g,"_").replace(/,/g,"_")}
;var Tc=Ic(),Uc=[];function Vc(a){throw Error("Bad hint"+(a?": "+a:""));}
Uc.push(["jsl",function(a){for(var b in a)if(Object.prototype.hasOwnProperty.call(a,b)){var c=a[b];"object"==typeof c?I[b]=H(I,b,[]).concat(c):H(I,b,c)}if(b=a.u)a=H(I,"us",[]),a.push(b),(b=/^https:(.*)$/.exec(b))&&a.push("http:"+b[1])}]);
var Wc=/^(\/[a-zA-Z0-9_\-]+)+$/,Xc=[/\/amp\//,/\/amp$/,/^\/amp$/],Yc=/^[a-zA-Z0-9\-_\.,!]+$/,Zc=/^gapi\.loaded_[0-9]+$/,$c=/^[a-zA-Z0-9,._-]+$/;function ad(a,b,c,d){var e=a.split(";"),f=e.shift(),g=Tc[f],h=null;g?h=g(e,b,c,d):Vc("no hint processor for: "+f);h||Vc("failed to generate load url");b=h;c=b.match(bd);(d=b.match(cd))&&1===d.length&&dd.test(b)&&c&&1===c.length||Vc("failed sanity: "+a);return h}
function ed(a,b,c,d){function e(a){return encodeURIComponent(a).replace(/%2C/g,",")}
a=fd(a);Zc.test(c)||Vc("invalid_callback");b=gd(b);d=d&&d.length?gd(d):null;return[encodeURIComponent(a.pathPrefix).replace(/%2C/g,",").replace(/%2F/g,"/"),"/k=",e(a.version),"/m=",e(b),d?"/exm="+e(d):"","/rt=j/sv=1/d=1/ed=1",a.ka?"/am="+e(a.ka):"",a.Ea?"/rs="+e(a.Ea):"",a.Na?"/t="+e(a.Na):"","/cb=",e(c)].join("")}
function fd(a){"/"!==a.charAt(0)&&Vc("relative path");for(var b=a.substring(1).split("/"),c=[];b.length;){a=b.shift();if(!a.length||0==a.indexOf("."))Vc("empty/relative directory");else if(0<a.indexOf("=")){b.unshift(a);break}c.push(a)}a={};for(var d=0,e=b.length;d<e;++d){var f=b[d].split("="),g=decodeURIComponent(f[0]),h=decodeURIComponent(f[1]);2==f.length&&g&&h&&(a[g]=a[g]||h)}b="/"+c.join("/");Wc.test(b)||Vc("invalid_prefix");c=0;for(d=Xc.length;c<d;++c)Xc[c].test(b)&&Vc("invalid_prefix");c=hd(a,
"k",!0);d=hd(a,"am");e=hd(a,"rs");a=hd(a,"t");return{pathPrefix:b,version:c,ka:d,Ea:e,Na:a}}
function gd(a){for(var b=[],c=0,d=a.length;c<d;++c){var e=a[c].replace(/\./g,"_").replace(/-/g,"_");$c.test(e)&&b.push(e)}return b.join(",")}
function hd(a,b,c){a=a[b];!a&&c&&Vc("missing: "+b);if(a){if(Yc.test(a))return a;Vc("invalid: "+b)}return null}
var dd=/^https?:\/\/[a-z0-9_.-]+\.google(rs)?\.com(:\d+)?\/[a-zA-Z0-9_.,!=\-\/]+$/,cd=/\/cb=/g,bd=/\/\//g;function id(){var a=Kc();if(!a)throw Error("Bad hint");return a}
Tc.m=function(a,b,c,d){(a=a[0])||Vc("missing_hint");return"https://apis.google.com"+ed(a,b,c,d)};
var jd=decodeURI("%73cript"),kd=/^[-+_0-9\/A-Za-z]+={0,2}$/;function ld(a,b){for(var c=[],d=0;d<a.length;++d){var e=a[d],f;if(f=e){a:{for(f=0;f<b.length;f++)if(b[f]===e)break a;f=-1}f=0>f}f&&c.push(e)}return c}
function md(){var a=I.nonce;return void 0!==a?a&&a===String(a)&&a.match(kd)?a:I.nonce=null:Cc.querySelector?(a=Cc.querySelector("script[nonce]"))?(a=a.nonce||a.getAttribute("nonce")||"",a&&a===String(a)&&a.match(kd)?I.nonce=a:I.nonce=null):null:null}
function nd(a){if("loading"!=Cc.readyState)od(a);else{var b=md(),c="";null!==b&&(c=' nonce="'+b+'"');Cc.write("<"+jd+' src="'+encodeURI(a)+'"'+c+"></"+jd+">")}}
function od(a){var b=Cc.createElement(jd);b.setAttribute("src",a);a=md();null!==a&&b.setAttribute("nonce",a);b.async="true";(a=Cc.getElementsByTagName(jd)[0])?a.parentNode.insertBefore(b,a):(Cc.head||Cc.body||Cc.documentElement).appendChild(b)}
function pd(a,b){var c=b&&b._c;if(c)for(var d=0;d<Uc.length;d++){var e=Uc[d][0],f=Uc[d][1];f&&Object.prototype.hasOwnProperty.call(c,e)&&f(c[e],a,b)}}
function qd(a,b,c){rd(function(){var c=b===Kc()?H(Jc,"_",Ic()):Ic();c=H(Mc(b),"_",c);a(c)},c)}
function sd(a,b){var c=b||{};"function"==typeof b&&(c={},c.callback=b);pd(a,c);var d=a?a.split(":"):[],e=c.h||id(),f=H(I,"ah",Ic());if(f["::"]&&d.length){for(var g=[],h=null;h=d.shift();){var l=h.split(".");l=f[h]||f[l[1]&&"ns:"+l[0]||""]||e;var n=g.length&&g[g.length-1]||null,r=n;n&&n.hint==l||(r={hint:l,features:[]},g.push(r));r.features.push(h)}var x=g.length;if(1<x){var q=c.callback;q&&(c.callback=function(){0==--x&&q()})}for(;d=g.shift();)td(d.features,c,d.hint)}else td(d||[],c,e)}
function td(a,b,c){function d(a,b){if(x)return 0;Bc.clearTimeout(r);q.push.apply(q,w);var d=((Jc||{}).config||{}).update;d?d(f):f&&H(I,"cu",[]).push(f);if(b){Rc("me0",a,J);try{qd(b,c,n)}finally{Rc("me1",a,J)}}return 1}
a=Hc(a)||[];var e=b.callback,f=b.config,g=b.timeout,h=b.ontimeout,l=b.onerror,n=void 0;"function"==typeof l&&(n=l);var r=null,x=!1;if(g&&!h||!g&&h)throw"Timeout requires both the timeout parameter and ontimeout parameter to be set";l=H(Mc(c),"r",[]).sort();var q=H(Mc(c),"L",[]).sort(),J=[].concat(l);0<g&&(r=Bc.setTimeout(function(){x=!0;h()},g));
var w=ld(a,q);if(w.length){w=ld(a,l);var na=H(I,"CP",[]),U=na.length;na[U]=function(a){function b(){var a=na[U+1];a&&a()}
function c(b){na[U]=null;d(w,a)&&Lc(function(){e&&e();b()})}
if(!a)return 0;Rc("ml1",w,J);0<U&&na[U-1]?na[U]=function(){c(b)}:c(b)};
if(w.length){var Fc="loaded_"+I.I++;Jc[Fc]=function(a){na[U](a);Jc[Fc]=null};
a=ad(c,w,"gapi."+Fc,l);l.push.apply(l,w);Rc("ml0",w,J);b.sync||Bc.___gapisync?nd(a):od(a)}else na[U](Ec)}else d(w)&&e&&e()}
function rd(a,b){if(I.hee&&0<I.hel)try{return a()}catch(c){b&&b(c),I.hel--,sd("debug_error",function(){try{window.___jsl.hefn(c)}catch(d){throw c;}})}else try{return a()}catch(c){throw b&&b(c),c;
}}
Jc.load=function(a,b){return rd(function(){return sd(a,b)})};function ud(a,b){this.g=a;this.j=b;this.f=0;this.b=null}
ud.prototype.get=function(){if(0<this.f){this.f--;var a=this.b;this.b=a.next;a.next=null}else a=this.g();return a};
function vd(a,b){a.j(b);100>a.f&&(a.f++,b.next=a.b,a.b=b)}
;function wd(a){m.setTimeout(function(){throw a;},0)}
var xd;
function yd(){var a=m.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!B("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=v(function(a){if(("*"==d||a.origin==d)&&a.data==
c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&!B("Trident")&&!B("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(p(c.next)){c=c.next;var a=c.ma;c.ma=null;a()}};
return function(a){d.next={ma:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){m.setTimeout(a,0)}}
;function zd(){this.f=this.b=null}
var Bd=new ud(function(){return new Ad},function(a){a.reset()});
zd.prototype.add=function(a,b){var c=Bd.get();c.set(a,b);this.f?this.f.next=c:this.b=c;this.f=c};
zd.prototype.remove=function(){var a=null;this.b&&(a=this.b,this.b=this.b.next,this.b||(this.f=null),a.next=null);return a};
function Ad(){this.next=this.scope=this.b=null}
Ad.prototype.set=function(a,b){this.b=a;this.scope=b;this.next=null};
Ad.prototype.reset=function(){this.next=this.scope=this.b=null};function Cd(a,b){Dd||Ed();Fd||(Dd(),Fd=!0);Gd.add(a,b)}
var Dd;function Ed(){if(m.Promise&&m.Promise.resolve){var a=m.Promise.resolve(void 0);Dd=function(){a.then(Hd)}}else Dd=function(){var a=Hd;
!za(m.setImmediate)||m.Window&&m.Window.prototype&&!B("Edge")&&m.Window.prototype.setImmediate==m.setImmediate?(xd||(xd=yd()),xd(a)):m.setImmediate(a)}}
var Fd=!1,Gd=new zd;function Hd(){for(var a;a=Gd.remove();){try{a.b.call(a.scope)}catch(b){wd(b)}vd(Bd,a)}Fd=!1}
;var Id=B("Firefox"),Jd=ob()||B("iPod"),Kd=B("iPad"),Ld=nb(),Md=mb(),Nd=lb()&&!pb();function Od(a,b,c){ta(a)?(this.date=Pd(a,b||0,c||1),Qd(this,c||1)):Aa(a)?(this.date=Pd(a.getFullYear(),a.getMonth(),a.getDate()),Qd(this,a.getDate())):(this.date=new Date(Ha()),a=this.date.getDate(),this.date.setHours(0),this.date.setMinutes(0),this.date.setSeconds(0),this.date.setMilliseconds(0),Qd(this,a))}
function Pd(a,b,c){b=new Date(a,b,c);0<=a&&100>a&&b.setFullYear(b.getFullYear()-1900);return b}
k=Od.prototype;k.getFullYear=function(){return this.date.getFullYear()};
k.getMonth=function(){return this.date.getMonth()};
k.getDate=function(){return this.date.getDate()};
k.getTime=function(){return this.date.getTime()};
k.set=function(a){this.date=new Date(a.getFullYear(),a.getMonth(),a.getDate())};
k.add=function(a){if(a.f||a.b){var b=this.getMonth()+a.b+12*a.f,c=this.getFullYear()+Math.floor(b/12);b%=12;0>b&&(b+=12);a:{switch(b){case 1:var d=0!=c%4||0==c%100&&0!=c%400?28:29;break a;case 5:case 8:case 10:case 3:d=30;break a}d=31}d=Math.min(d,this.getDate());this.date.setDate(1);this.date.setFullYear(c);this.date.setMonth(b);this.date.setDate(d)}a.days&&(a=new Date((new Date(this.getFullYear(),this.getMonth(),this.getDate(),12)).getTime()+864E5*a.days),this.date.setDate(1),this.date.setFullYear(a.getFullYear()),
this.date.setMonth(a.getMonth()),this.date.setDate(a.getDate()),Qd(this,a.getDate()))};
k.V=function(a){return[this.getFullYear(),Ya(this.getMonth()+1),Ya(this.getDate())].join(a?"-":"")+""};
k.equals=function(a){return!(!a||this.getFullYear()!=a.getFullYear()||this.getMonth()!=a.getMonth()||this.getDate()!=a.getDate())};
k.toString=function(){return this.V()};
function Qd(a,b){a.getDate()!=b&&a.date.setUTCHours(a.date.getUTCHours()+(a.getDate()<b?1:-1))}
k.valueOf=function(){return this.date.valueOf()};
function Rd(a,b,c,d,e,f,g){this.date=ta(a)?new Date(a,b||0,c||1,d||0,e||0,f||0,g||0):new Date(a&&a.getTime?a.getTime():Ha())}
z(Rd,Od);Rd.prototype.add=function(a){Od.prototype.add.call(this,a);a.hours&&this.date.setUTCHours(this.date.getUTCHours()+a.hours);a.minutes&&this.date.setUTCMinutes(this.date.getUTCMinutes()+a.minutes);a.seconds&&this.date.setUTCSeconds(this.date.getUTCSeconds()+a.seconds)};
Rd.prototype.V=function(a){var b=Od.prototype.V.call(this,a);return a?b+" "+Ya(this.date.getHours())+":"+Ya(this.date.getMinutes())+":"+Ya(this.date.getSeconds()):b+"T"+Ya(this.date.getHours())+Ya(this.date.getMinutes())+Ya(this.date.getSeconds())};
Rd.prototype.equals=function(a){return this.getTime()==a.getTime()};
Rd.prototype.toString=function(){return this.V()};function Sd(){this.g=this.g;this.j=this.j}
Sd.prototype.g=!1;Sd.prototype.T=function(){return this.g};
Sd.prototype.dispose=function(){this.g||(this.g=!0,this.Y())};
Sd.prototype.Y=function(){if(this.j)for(;this.j.length;)this.j.shift()()};
function Td(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function Ud(a){if(a.classList)return a.classList;a=a.className;return t(a)&&a.match(/\S+/g)||[]}
function K(a,b){return a.classList?a.classList.contains(b):Pa(Ud(a),b)}
function L(a,b){a.classList?a.classList.add(b):K(a,b)||(a.className+=0<a.className.length?" "+b:b)}
function Vd(a,b){if(a.classList)A(b,function(b){L(a,b)});
else{var c={};A(Ud(a),function(a){c[a]=!0});
A(b,function(a){c[a]=!0});
a.className="";for(var d in c)a.className+=0<a.className.length?" "+d:d}}
function M(a,b){a.classList?a.classList.remove(b):K(a,b)&&(a.className=La(Ud(a),function(a){return a!=b}).join(" "))}
function Wd(a,b){a.classList?A(b,function(b){M(a,b)}):a.className=La(Ud(a),function(a){return!Pa(b,a)}).join(" ")}
function Xd(a,b,c){c?L(a,b):M(a,b)}
function Yd(a,b,c){K(a,b)&&(M(a,b),L(a,c))}
function Zd(a,b){var c=!K(a,b);Xd(a,b,c)}
;var $d=!C&&!lb();function ae(a,b){if(/-[a-z]/.test(b))return null;if($d&&a.dataset){if(nb()&&!(b in a.dataset))return null;var c=a.dataset[b];return void 0===c?null:c}return a.getAttribute("data-"+String(b).replace(/([A-Z])/g,"-$1").toLowerCase())}
;var be="StopIteration"in m?m.StopIteration:{message:"StopIteration",stack:""};function ce(){}
ce.prototype.next=function(){throw be;};
ce.prototype.H=function(){return this};
function de(a){if(a instanceof ce)return a;if("function"==typeof a.H)return a.H(!1);if(ya(a)){var b=0,c=new ce;c.next=function(){for(;;){if(b>=a.length)throw be;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function ee(a,b){if(ya(a))try{A(a,b,void 0)}catch(c){if(c!==be)throw c;}else{a=de(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==be)throw c;}}}
function fe(a){if(ya(a))return Ra(a);a=de(a);var b=[];ee(a,function(a){b.push(a)});
return b}
;function ge(a,b){this.g={};this.b=[];this.J=this.f=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof ge)for(c=he(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function he(a){ie(a);return a.b.concat()}
k=ge.prototype;k.equals=function(a,b){if(this===a)return!0;if(this.f!=a.f)return!1;var c=b||je;ie(this);for(var d,e=0;d=this.b[e];e++)if(!c(this.get(d),a.get(d)))return!1;return!0};
function je(a,b){return a===b}
k.isEmpty=function(){return 0==this.f};
k.clear=function(){this.g={};this.J=this.f=this.b.length=0};
k.remove=function(a){return Object.prototype.hasOwnProperty.call(this.g,a)?(delete this.g[a],this.f--,this.J++,this.b.length>2*this.f&&ie(this),!0):!1};
function ie(a){if(a.f!=a.b.length){for(var b=0,c=0;b<a.b.length;){var d=a.b[b];Object.prototype.hasOwnProperty.call(a.g,d)&&(a.b[c++]=d);b++}a.b.length=c}if(a.f!=a.b.length){var e={};for(c=b=0;b<a.b.length;)d=a.b[b],Object.prototype.hasOwnProperty.call(e,d)||(a.b[c++]=d,e[d]=1),b++;a.b.length=c}}
k.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.g,a)?this.g[a]:b};
k.set=function(a,b){Object.prototype.hasOwnProperty.call(this.g,a)||(this.f++,this.b.push(a),this.J++);this.g[a]=b};
k.forEach=function(a,b){for(var c=he(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
k.H=function(a){ie(this);var b=0,c=this.J,d=this,e=new ce;e.next=function(){if(c!=d.J)throw Error("The map has changed since the iterator was created");if(b>=d.b.length)throw be;var e=d.b[b++];return a?e:d.g[e]};
return e};function ke(a){var b=[];le(new me,a,b);return b.join("")}
function me(){}
function le(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(xa(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),le(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),ne(d,c),c.push(":"),le(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":ne(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var oe={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},pe=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function ne(a,b){b.push('"',a.replace(pe,function(a){var b=oe[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),oe[a]=b);return b}),'"')}
;function qe(a,b,c,d){this.top=a;this.right=b;this.bottom=c;this.left=d}
qe.prototype.getHeight=function(){return this.bottom-this.top};
qe.prototype.ceil=function(){this.top=Math.ceil(this.top);this.right=Math.ceil(this.right);this.bottom=Math.ceil(this.bottom);this.left=Math.ceil(this.left);return this};
qe.prototype.floor=function(){this.top=Math.floor(this.top);this.right=Math.floor(this.right);this.bottom=Math.floor(this.bottom);this.left=Math.floor(this.left);return this};
qe.prototype.round=function(){this.top=Math.round(this.top);this.right=Math.round(this.right);this.bottom=Math.round(this.bottom);this.left=Math.round(this.left);return this};function re(a,b,c,d){this.left=a;this.top=b;this.width=c;this.height=d}
re.prototype.ceil=function(){this.left=Math.ceil(this.left);this.top=Math.ceil(this.top);this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
re.prototype.floor=function(){this.left=Math.floor(this.left);this.top=Math.floor(this.top);this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
re.prototype.round=function(){this.left=Math.round(this.left);this.top=Math.round(this.top);this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function se(a,b,c){if(t(b))(b=te(a,b))&&(a.style[b]=c);else for(var d in b){c=a;var e=b[d],f=te(c,d);f&&(c.style[f]=e)}}
var ue={};function te(a,b){var c=ue[b];if(!c){var d=ab(b);c=d;void 0===a.style[d]&&(d=(xb?"Webkit":wb?"Moz":C?"ms":tb?"O":null)+bb(d),void 0!==a.style[d]&&(c=d));ue[b]=c}return c}
function ve(a,b){var c=bc(a);return c.defaultView&&c.defaultView.getComputedStyle&&(c=c.defaultView.getComputedStyle(a,null))?c[b]||c.getPropertyValue(b)||"":""}
function we(a,b){return ve(a,b)||(a.currentStyle?a.currentStyle[b]:null)||a.style&&a.style[b]}
function xe(a){try{var b=a.getBoundingClientRect()}catch(c){return{left:0,top:0,right:0,bottom:0}}C&&a.ownerDocument.body&&(a=a.ownerDocument,b.left-=a.documentElement.clientLeft+a.body.clientLeft,b.top-=a.documentElement.clientTop+a.body.clientTop);return b}
function ye(a){if(C&&!(8<=Number(Mb)))return a.offsetParent;var b=bc(a),c=we(a,"position"),d="fixed"==c||"absolute"==c;for(a=a.parentNode;a&&a!=b;a=a.parentNode)if(11==a.nodeType&&a.host&&(a=a.host),c=we(a,"position"),d=d&&"static"==c&&a!=b.documentElement&&a!=b.body,!d&&(a.scrollWidth>a.clientWidth||a.scrollHeight>a.clientHeight||"fixed"==c||"absolute"==c||"relative"==c))return a;return null}
function ze(a){for(var b=new qe(0,Infinity,Infinity,0),c=$b(a),d=c.b.body,e=c.b.documentElement,f=jc(c.b);a=ye(a);)if(!(C&&0==a.clientWidth||xb&&0==a.clientHeight&&a==d)&&a!=d&&a!=e&&"visible"!=we(a,"overflow")){var g=Ae(a),h=new D(a.clientLeft,a.clientTop);g.x+=h.x;g.y+=h.y;b.top=Math.max(b.top,g.y);b.right=Math.min(b.right,g.x+a.clientWidth);b.bottom=Math.min(b.bottom,g.y+a.clientHeight);b.left=Math.max(b.left,g.x)}d=f.scrollLeft;f=f.scrollTop;b.left=Math.max(b.left,d);b.top=Math.max(b.top,f);c=
gc(kc(c.b)||window);b.right=Math.min(b.right,d+c.width);b.bottom=Math.min(b.bottom,f+c.height);return 0<=b.top&&0<=b.left&&b.bottom>b.top&&b.right>b.left?b:null}
function Ae(a){var b=bc(a),c=new D(0,0);var d=b?bc(b):document;d=!C||9<=Number(Mb)||hc($b(d).b)?d.documentElement:d.body;if(a==d)return c;a=xe(a);b=ic($b(b).b);c.x=a.left+b.x;c.y=a.top+b.y;return c}
function Be(a){a=xe(a);return new D(a.left,a.top)}
function Ce(a,b){"number"==typeof a&&(a=(b?Math.round(a):a)+"px");return a}
function De(a){var b=Ee;if("none"!=we(a,"display"))return b(a);var c=a.style,d=c.display,e=c.visibility,f=c.position;c.visibility="hidden";c.position="absolute";c.display="inline";a=b(a);c.display=d;c.position=f;c.visibility=e;return a}
function Ee(a){var b=a.offsetWidth,c=a.offsetHeight,d=xb&&!b&&!c;return p(b)&&!d||!a.getBoundingClientRect?new Zb(b,c):(a=xe(a),new Zb(a.right-a.left,a.bottom-a.top))}
function Fe(a){var b=Ae(a);a=De(a);return new re(b.x,b.y,a.width,a.height)}
function Ge(a){return"rtl"==we(a,"direction")}
function He(a,b){if(/^\d+px?$/.test(b))return parseInt(b,10);var c=a.style.left,d=a.runtimeStyle.left;a.runtimeStyle.left=a.currentStyle.left;a.style.left=b;var e=a.style.pixelLeft;a.style.left=c;a.runtimeStyle.left=d;return+e}
function Ie(a,b){var c=a.currentStyle?a.currentStyle[b]:null;return c?He(a,c):0}
var Je={thin:2,medium:4,thick:6};function Ke(a,b){if("none"==(a.currentStyle?a.currentStyle[b+"Style"]:null))return 0;var c=a.currentStyle?a.currentStyle[b+"Width"]:null;return c in Je?Je[c]:He(a,c)}
;var Le=function(){if(zb){var a=/Windows NT ([0-9.]+)/;return(a=a.exec(cb))?a[1]:"0"}return yb?(a=/10[_.][0-9_.]+/,(a=a.exec(cb))?a[0].replace(/_/g,"."):"10"):Ab?(a=/Android\s+([^\);]+)(\)|;)/,(a=a.exec(cb))?a[1]:""):Bb||Cb||Db?(a=/(?:iPhone|CPU)\s+OS\s+(\S+)/,(a=a.exec(cb))?a[1].replace(/_/g,"."):""):""}();function Me(a){return(a=a.exec(cb))?a[1]:""}
var Ne=function(){if(Id)return Me(/Firefox\/([0-9.]+)/);if(C||ub||tb)return Kb;if(Md)return pb()?Me(/CriOS\/([0-9.]+)/):Me(/Chrome\/([0-9.]+)/);if(Nd&&!pb())return Me(/Version\/([0-9.]+)/);if(Jd||Kd){var a=/Version\/(\S+).*Mobile\/(\S+)/.exec(cb);if(a)return a[1]+"."+a[2]}else if(Ld)return(a=Me(/Android\s+([0-9.]+)/))?a:Me(/Version\/([0-9.]+)/);return""}();function Oe(a,b,c,d,e,f,g){var h;if(h=c.offsetParent){var l="HTML"==h.tagName||"BODY"==h.tagName;if(!l||"static"!=we(h,"position")){var n=Ae(h);if(!l){l=Ge(h);var r;if(r=l){if(r=Nd)r=0<=Za(Ne,10);var x;if(x=Eb)x=0<=Za(Le,10);r=wb||r||x}l=r?-h.scrollLeft:!l||vb&&Lb("8")||"visible"==we(h,"overflowX")?h.scrollLeft:h.scrollWidth-h.clientWidth-h.scrollLeft;n=Yb(n,new D(l,h.scrollTop))}}}h=n||new D;n=Fe(a);if(l=ze(a)){var q=new re(l.left,l.top,l.right-l.left,l.bottom-l.top);l=Math.max(n.left,q.left);r=
Math.min(n.left+n.width,q.left+q.width);l<=r&&(x=Math.max(n.top,q.top),q=Math.min(n.top+n.height,q.top+q.height),x<=q&&(n.left=l,n.top=x,n.width=r-l,n.height=q-x))}l=$b(a);x=$b(c);if(l.b!=x.b){r=l.b.body;x=kc(x.b);q=new D(0,0);var J=(J=bc(r))?kc(J):window;b:{try{qb(J.parent);var w=!0;break b}catch(Fc){}w=!1}if(w){w=r;do{var na=J==x?Ae(w):Be(w);q.x+=na.x;q.y+=na.y}while(J&&J!=x&&J!=J.parent&&(w=J.frameElement)&&(J=J.parent))}w=Yb(q,Ae(r));!C||9<=Number(Mb)||hc(l.b)||(w=Yb(w,ic(l.b)));n.left+=w.x;n.top+=
w.y}a=Pe(a,b);b=n.left;a&4?b+=n.width:a&2&&(b+=n.width/2);b=new D(b,n.top+(a&1?n.height:0));b=Yb(b,h);e&&(b.x+=(a&4?-1:1)*e.x,b.y+=(a&1?-1:1)*e.y);var U;g&&(U=ze(c))&&(U.top-=h.y,U.right-=h.x,U.bottom-=h.y,U.left-=h.x);return Qe(b,c,d,f,U,g,void 0)}
function Qe(a,b,c,d,e,f,g){a=new D(a.x,a.y);var h=Pe(b,c);c=De(b);g=g?new Zb(g.width,g.height):new Zb(c.width,c.height);a=new D(a.x,a.y);g=new Zb(g.width,g.height);var l=0;if(d||0!=h)h&4?a.x-=g.width+(d?d.right:0):h&2?a.x-=g.width/2:d&&(a.x+=d.left),h&1?a.y-=g.height+(d?d.bottom:0):d&&(a.y+=d.top);if(f){if(e){d=a;h=g;l=0;65==(f&65)&&(d.x<e.left||d.x>=e.right)&&(f&=-2);132==(f&132)&&(d.y<e.top||d.y>=e.bottom)&&(f&=-5);d.x<e.left&&f&1&&(d.x=e.left,l|=1);if(f&16){var n=d.x;d.x<e.left&&(d.x=e.left,l|=
4);d.x+h.width>e.right&&(h.width=Math.min(e.right-d.x,n+h.width-e.left),h.width=Math.max(h.width,0),l|=4)}d.x+h.width>e.right&&f&1&&(d.x=Math.max(e.right-h.width,e.left),l|=1);f&2&&(l|=(d.x<e.left?16:0)|(d.x+h.width>e.right?32:0));d.y<e.top&&f&4&&(d.y=e.top,l|=2);f&32&&(n=d.y,d.y<e.top&&(d.y=e.top,l|=8),d.y+h.height>e.bottom&&(h.height=Math.min(e.bottom-d.y,n+h.height-e.top),h.height=Math.max(h.height,0),l|=8));d.y+h.height>e.bottom&&f&4&&(d.y=Math.max(e.bottom-h.height,e.top),l|=2);f&8&&(l|=(d.y<
e.top?64:0)|(d.y+h.height>e.bottom?128:0));e=l}else e=256;l=e}f=new re(0,0,0,0);f.left=a.x;f.top=a.y;f.width=g.width;f.height=g.height;e=l;if(e&496)return e;g=new D(f.left,f.top);g instanceof D?(a=g.x,g=g.y):(a=g,g=void 0);b.style.left=Ce(a,!1);b.style.top=Ce(g,!1);g=new Zb(f.width,f.height);c==g||c&&g&&c.width==g.width&&c.height==g.height||(c=g,g=hc($b(bc(b)).b),!C||Lb("10")||g&&Lb("8")?(b=b.style,wb?b.MozBoxSizing="border-box":xb?b.WebkitBoxSizing="border-box":b.boxSizing="border-box",b.width=Math.max(c.width,
0)+"px",b.height=Math.max(c.height,0)+"px"):(a=b.style,g?(C?(g=Ie(b,"paddingLeft"),f=Ie(b,"paddingRight"),d=Ie(b,"paddingTop"),h=Ie(b,"paddingBottom"),g=new qe(d,f,h,g)):(g=ve(b,"paddingLeft"),f=ve(b,"paddingRight"),d=ve(b,"paddingTop"),h=ve(b,"paddingBottom"),g=new qe(parseFloat(d),parseFloat(f),parseFloat(h),parseFloat(g))),!C||9<=Number(Mb)?(f=ve(b,"borderLeftWidth"),d=ve(b,"borderRightWidth"),h=ve(b,"borderTopWidth"),b=ve(b,"borderBottomWidth"),b=new qe(parseFloat(h),parseFloat(d),parseFloat(b),
parseFloat(f))):(f=Ke(b,"borderLeft"),d=Ke(b,"borderRight"),h=Ke(b,"borderTop"),b=Ke(b,"borderBottom"),b=new qe(h,d,b,f)),a.pixelWidth=c.width-b.left-g.left-g.right-b.right,a.pixelHeight=c.height-b.top-g.top-g.bottom-b.bottom):(a.pixelWidth=c.width,a.pixelHeight=c.height)));return e}
function Pe(a,b){return(b&8&&Ge(a)?b^4:b)&-9}
;function Re(a){this.b=0;this.B=void 0;this.j=this.f=this.g=null;this.l=this.o=!1;if(a!=ua)try{var b=this;a.call(void 0,function(a){Se(b,2,a)},function(a){Se(b,3,a)})}catch(c){Se(this,3,c)}}
function Te(){this.next=this.context=this.onRejected=this.f=this.b=null;this.g=!1}
Te.prototype.reset=function(){this.context=this.onRejected=this.f=this.b=null;this.g=!1};
var Ue=new ud(function(){return new Te},function(a){a.reset()});
function Ve(a,b,c){var d=Ue.get();d.f=a;d.onRejected=b;d.context=c;return d}
Re.prototype.then=function(a,b,c){return We(this,za(a)?a:null,za(b)?b:null,c)};
Re.prototype.then=Re.prototype.then;Re.prototype.$goog_Thenable=!0;Re.prototype.cancel=function(a){0==this.b&&Cd(function(){var b=new Xe(a);Ye(this,b)},this)};
function Ye(a,b){if(0==a.b)if(a.g){var c=a.g;if(c.f){for(var d=0,e=null,f=null,g=c.f;g&&(g.g||(d++,g.b==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.b&&1==d?Ye(c,b):(f?(d=f,d.next==c.j&&(c.j=d),d.next=d.next.next):Ze(c),$e(c,e,3,b)))}a.g=null}else Se(a,3,b)}
function af(a,b){a.f||2!=a.b&&3!=a.b||bf(a);a.j?a.j.next=b:a.f=b;a.j=b}
function We(a,b,c,d){var e=Ve(null,null,null);e.b=new Re(function(a,g){e.f=b?function(c){try{var e=b.call(d,c);a(e)}catch(n){g(n)}}:a;
e.onRejected=c?function(b){try{var e=c.call(d,b);!p(e)&&b instanceof Xe?g(b):a(e)}catch(n){g(n)}}:g});
e.b.g=a;af(a,e);return e.b}
Re.prototype.K=function(a){this.b=0;Se(this,2,a)};
Re.prototype.R=function(a){this.b=0;Se(this,3,a)};
function Se(a,b,c){if(0==a.b){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.b=1;a:{var d=c,e=a.K,f=a.R;if(d instanceof Re){af(d,Ve(e||ua,f||null,a));var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(n){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(Aa(d))try{var l=d.then;if(za(l)){cf(d,l,e,f,a);g=!0;break a}}catch(n){f.call(a,n);g=!0;break a}g=!1}}}g||(a.B=c,a.b=b,a.g=null,bf(a),3!=b||c instanceof Xe||df(a,c))}}
function cf(a,b,c,d,e){function f(a){h||(h=!0,d.call(e,a))}
function g(a){h||(h=!0,c.call(e,a))}
var h=!1;try{b.call(a,g,f)}catch(l){f(l)}}
function bf(a){a.o||(a.o=!0,Cd(a.D,a))}
function Ze(a){var b=null;a.f&&(b=a.f,a.f=b.next,b.next=null);a.f||(a.j=null);return b}
Re.prototype.D=function(){for(var a;a=Ze(this);)$e(this,a,this.b,this.B);this.o=!1};
function $e(a,b,c,d){if(3==c&&b.onRejected&&!b.g)for(;a&&a.l;a=a.g)a.l=!1;if(b.b)b.b.g=null,ef(b,c,d);else try{b.g?b.f.call(b.context):ef(b,c,d)}catch(e){ff.call(null,e)}vd(Ue,b)}
function ef(a,b,c){2==b?a.f.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function df(a,b){a.l=!0;Cd(function(){a.l&&ff.call(null,b)})}
var ff=wd;function Xe(a){Ia.call(this,a)}
z(Xe,Ia);Xe.prototype.name="cancel";function N(a){Sd.call(this);this.B=1;this.l=[];this.o=0;this.b=[];this.f={};this.D=!!a}
z(N,Sd);k=N.prototype;k.subscribe=function(a,b,c){var d=this.f[a];d||(d=this.f[a]=[]);var e=this.B;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.B=e+3;d.push(e);return e};
function gf(a,b){var c=!1,d=a.subscribe("ROOT_MENU_REMOVED",function(a){c||(c=!0,this.P(d),b.apply(void 0,arguments))},a)}
function hf(a,b,c){if(b=a.f[b]){var d=a.b;(b=Oa(b,function(a){return d[a+1]==c&&void 0==d[a+2]}))&&a.P(b)}}
k.P=function(a){var b=this.b[a];if(b){var c=this.f[b];if(0!=this.o)this.l.push(a),this.b[a+1]=ua;else{if(c){var d=Ka(c,a);0<=d&&Array.prototype.splice.call(c,d,1)}delete this.b[a];delete this.b[a+1];delete this.b[a+2]}}return!!b};
k.G=function(a,b){var c=this.f[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.D)for(e=0;e<c.length;e++){var g=c[e];jf(this.b[g+1],this.b[g+2],d)}else{this.o++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.o--,0<this.l.length&&0==this.o)for(;c=this.l.pop();)this.P(c)}}return 0!=e}return!1};
function jf(a,b,c){Cd(function(){a.apply(b,c)})}
k.clear=function(a){if(a){var b=this.f[a];b&&(A(b,this.P,this),delete this.f[a])}else this.b.length=0,this.f={}};
function kf(a,b){if(b){var c=a.f[b];return c?c.length:0}c=0;for(var d in a.f)c+=kf(a,d);return c}
k.Y=function(){N.w.Y.call(this);this.clear();this.l.length=0};function lf(a){this.b=a}
lf.prototype.set=function(a,b){p(b)?this.b.set(a,ke(b)):this.b.remove(a)};
lf.prototype.get=function(a){try{var b=this.b.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
lf.prototype.remove=function(a){this.b.remove(a)};function mf(a){this.b=a}
z(mf,lf);function nf(a){this.data=a}
function of(a){return!p(a)||a instanceof nf?a:new nf(a)}
mf.prototype.set=function(a,b){mf.w.set.call(this,a,of(b))};
mf.prototype.f=function(a){a=mf.w.get.call(this,a);if(!p(a)||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
mf.prototype.get=function(a){if(a=this.f(a)){if(a=a.data,!p(a))throw"Storage: Invalid value was encountered";}else a=void 0;return a};function pf(a){this.b=a}
z(pf,mf);pf.prototype.set=function(a,b,c){if(b=of(b)){if(c){if(c<Ha()){pf.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Ha()}pf.w.set.call(this,a,b)};
pf.prototype.f=function(a){var b=pf.w.f.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Ha()||c&&c>Ha())pf.prototype.remove.call(this,a);else return b}};function qf(){}
;function rf(){}
z(rf,qf);rf.prototype.clear=function(){var a=fe(this.H(!0)),b=this;A(a,function(a){b.remove(a)})};function sf(a){this.b=a}
z(sf,rf);k=sf.prototype;k.isAvailable=function(){if(!this.b)return!1;try{return this.b.setItem("__sak","1"),this.b.removeItem("__sak"),!0}catch(a){return!1}};
k.set=function(a,b){try{this.b.setItem(a,b)}catch(c){if(0==this.b.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
k.get=function(a){a=this.b.getItem(a);if(!t(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
k.remove=function(a){this.b.removeItem(a)};
k.H=function(a){var b=0,c=this.b,d=new ce;d.next=function(){if(b>=c.length)throw be;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!t(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
k.clear=function(){this.b.clear()};
k.key=function(a){return this.b.key(a)};function tf(){var a=null;try{a=window.localStorage||null}catch(b){}this.b=a}
z(tf,sf);function uf(a,b){this.f=a;this.b=null;if(C&&!(9<=Number(Mb))){vf||(vf=new ge);this.b=vf.get(a);this.b||(b?this.b=document.getElementById(b):(this.b=document.createElement("userdata"),this.b.addBehavior("#default#userData"),document.body.appendChild(this.b)),vf.set(a,this.b));try{this.b.load(this.f)}catch(c){this.b=null}}}
z(uf,rf);var wf={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},vf=null;function xf(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(a){return wf[a]})}
k=uf.prototype;k.isAvailable=function(){return!!this.b};
k.set=function(a,b){this.b.setAttribute(xf(a),b);yf(this)};
k.get=function(a){a=this.b.getAttribute(xf(a));if(!t(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
k.remove=function(a){this.b.removeAttribute(xf(a));yf(this)};
k.H=function(a){var b=0,c=this.b.XMLDocument.documentElement.attributes,d=new ce;d.next=function(){if(b>=c.length)throw be;var d=c[b++];if(a)return decodeURIComponent(d.nodeName.replace(/\./g,"%")).substr(1);d=d.nodeValue;if(!t(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
k.clear=function(){for(var a=this.b.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);yf(this)};
function yf(a){try{a.b.save(a.f)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function zf(a,b){this.f=a;this.b=b+"::"}
z(zf,rf);zf.prototype.set=function(a,b){this.f.set(this.b+a,b)};
zf.prototype.get=function(a){return this.f.get(this.b+a)};
zf.prototype.remove=function(a){this.f.remove(this.b+a)};
zf.prototype.H=function(a){var b=this.f.H(!0),c=this,d=new ce;d.next=function(){for(var d=b.next();d.substr(0,c.b.length)!=c.b;)d=b.next();return a?d.substr(c.b.length):c.f.get(d)};
return d};var Af=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function Bf(a){return a?decodeURI(a):a}
function Cf(a,b){if(!b)return a;var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);c=[a.substr(0,d),e,a.substr(c)];d=c[1];c[1]=b?d?d+"&"+b:b:d;return c[0]+(c[1]?"?"+c[1]:"")+c[2]}
function Df(a,b,c){if(xa(b))for(var d=0;d<b.length;d++)Df(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function Ef(a,b){for(var c=[],d=b||0;d<a.length;d+=2)Df(a[d],a[d+1],c);return c.join("&")}
function Ff(a){var b=[],c;for(c in a)Df(c,a[c],b);return b.join("&")}
function Gf(a,b){var c=2==arguments.length?Ef(arguments[1],0):Ef(arguments,1);return Cf(a,c)}
function Hf(a,b){var c=Ff(b);return Cf(a,c)}
;var If=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};y("yt.config_",If);function Jf(a){var b=arguments;if(1<b.length)If[b[0]]=b[1];else{b=b[0];for(var c in b)If[c]=b[c]}}
function O(a,b){return a in If?If[a]:b}
;function Kf(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Lf(b)}}:a}
function Lf(a){var b=u("yt.logging.errors.log");b?b(a,void 0,void 0,void 0,void 0):(b=O("ERRORS",[]),b.push([a,void 0,void 0,void 0,void 0]),Jf("ERRORS",b))}
;function P(a,b){za(a)&&(a=Kf(a));return window.setTimeout(a,b)}
;var Mf=u("ytPubsubPubsubInstance")||new N;N.prototype.subscribe=N.prototype.subscribe;N.prototype.unsubscribeByKey=N.prototype.P;N.prototype.publish=N.prototype.G;N.prototype.clear=N.prototype.clear;y("ytPubsubPubsubInstance",Mf);var Nf=u("ytPubsubPubsubSubscribedKeys")||{};y("ytPubsubPubsubSubscribedKeys",Nf);var Of=u("ytPubsubPubsubTopicToKeys")||{};y("ytPubsubPubsubTopicToKeys",Of);var Pf=u("ytPubsubPubsubIsSynchronous")||{};y("ytPubsubPubsubIsSynchronous",Pf);
function Qf(a,b,c){var d=Rf();if(d){var e=d.subscribe(a,function(){var d=arguments;var g=function(){Nf[e]&&b.apply(c||window,d)};
try{Pf[a]?g():P(g,0)}catch(h){Lf(h)}},c);
Nf[e]=!0;Of[a]||(Of[a]=[]);Of[a].push(e);return e}return 0}
function Sf(a){var b=Rf();b&&(ta(a)?a=[a]:t(a)&&(a=[parseInt(a,10)]),A(a,function(a){b.unsubscribeByKey(a);delete Nf[a]}))}
function Q(a,b){var c=Rf();return c?c.publish.apply(c,arguments):!1}
function Tf(a,b){Pf[a]=!0;var c=Rf();c&&c.publish.apply(c,arguments);Pf[a]=!1}
function Rf(){return u("ytPubsubPubsubInstance")}
;function Uf(a,b,c){a&&(a.dataset?a.dataset[Vf(b)]=String(c):a.setAttribute("data-"+b,c))}
function Wf(a,b){return a?a.dataset?a.dataset[Vf(b)]:a.getAttribute("data-"+b):null}
function Xf(a,b){a&&(a.dataset?delete a.dataset[Vf(b)]:a.removeAttribute("data-"+b))}
var Yf={};function Vf(a){return Yf[a]||(Yf[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;function R(a,b){this.version=a;this.args=b}
;function S(a,b){this.topic=a;this.b=b}
S.prototype.toString=function(){return this.topic};function Zf(a){var b=void 0;isNaN(b)&&(b=void 0);var c=u("yt.scheduler.instance.addJob");c?c(a,1,b):void 0===b?a():P(a,b||0)}
;function $f(){}
function ag(){}
$f.prototype=aa(ag.prototype);$f.prototype.constructor=$f;if(fa)fa($f,ag);else for(var bg in ag)if("prototype"!=bg)if(Object.defineProperties){var cg=Object.getOwnPropertyDescriptor(ag,bg);cg&&Object.defineProperty($f,bg,cg)}else $f[bg]=ag[bg];$f.w=ag.prototype;$f.prototype.start=function(){var a=u("yt.scheduler.instance.start");a&&a()};
va($f);$f.v();var dg=u("ytPubsub2Pubsub2Instance")||new N;N.prototype.subscribe=N.prototype.subscribe;N.prototype.unsubscribeByKey=N.prototype.P;N.prototype.publish=N.prototype.G;N.prototype.clear=N.prototype.clear;y("ytPubsub2Pubsub2Instance",dg);var eg=u("ytPubsub2Pubsub2SubscribedKeys")||{};y("ytPubsub2Pubsub2SubscribedKeys",eg);var fg=u("ytPubsub2Pubsub2TopicToKeys")||{};y("ytPubsub2Pubsub2TopicToKeys",fg);var gg=u("ytPubsub2Pubsub2IsAsync")||{};y("ytPubsub2Pubsub2IsAsync",gg);
y("ytPubsub2Pubsub2SkipSubKey",null);function T(a,b){var c=hg();c&&c.publish.call(c,a.toString(),a,b)}
function ig(a,b,c){var d=hg();if(!d)return 0;var e=d.subscribe(a.toString(),function(d,g){var f=u("ytPubsub2Pubsub2SkipSubKey");f&&f==e||(f=function(){if(eg[e])try{if(g&&a instanceof S&&a!=d)try{var f=a.b,h=g;if(!h.args||!h.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!f.J){var r=new f;f.J=r.version}var x=f.J}catch(q){}if(!x||h.version!=x)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{g=Reflect.construct(f,Ra(h.args))}catch(q){throw q.message=
"yt.pubsub2.Data.deserialize(): "+q.message,q;}}catch(q){throw q.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+a.toString()+": "+q.message,q;}b.call(c||window,g)}catch(q){Lf(q)}},gg[a.toString()]?u("yt.scheduler.instance")?Zf(f):P(f,0):f())});
eg[e]=!0;fg[a.toString()]||(fg[a.toString()]=[]);fg[a.toString()].push(e);return e}
function jg(a){var b=hg();b&&(ta(a)&&(a=[a]),A(a,function(a){b.unsubscribeByKey(a);delete eg[a]}))}
function hg(){return u("ytPubsub2Pubsub2Instance")}
;var kg=0;function lg(a){var b=a.__yt_uid_key;b||(b=mg(),a.__yt_uid_key=b);return b}
function ng(a,b){a=E(a);b=E(b);return!!Ac(a,function(a){return a===b},!0,void 0)}
function og(a,b){var c=dc(document,a,null,b);return c.length?c[0]:null}
function pg(){var a=document,b;Na(["fullscreenElement","webkitFullscreenElement","mozFullScreenElement","msFullscreenElement"],function(c){b=a[c];return!!b});
return b}
function qg(){Xd(document.body,"hide-players",!1);A(cc("preserve-players"),function(a){M(a,"preserve-players")})}
var mg=u("ytDomDomGetNextId")||function(){return++kg};
y("ytDomDomGetNextId",mg);var rg={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function sg(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;if(a=a||window.event){this.event=a;for(var b in a)b in rg||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?
b=a.fromElement:"mouseout"==this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey}}
sg.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
sg.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
sg.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var ib=u("ytEventsEventsListeners")||{};y("ytEventsEventsListeners",ib);var tg=u("ytEventsEventsCounter")||{count:0};y("ytEventsEventsCounter",tg);
function ug(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return hb(function(e){var f="boolean"==typeof e[4]&&e[4]==!!d,g;if(g=Aa(e[4])&&Aa(d))a:{g=e[4];for(var h in g)if(!(h in d)||g[h]!==d[h]){g=!1;break a}for(h in d)if(!(h in g)){g=!1;break a}g=!0}return!!e.length&&e[0]==a&&e[1]==b&&e[2]==
c&&(f||g)})}
function V(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=ug(a,b,c,d);if(e)return e;e=++tg.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(d){d=new sg(d);if(!Ac(d.relatedTarget,function(b){return b==a},!0))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new sg(b);
b.currentTarget=a;return c.call(a,b)};
g=Kf(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),vg()||"boolean"==typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);ib[e]=[a,b,c,g,d];return e}
function wg(a,b,c){var d=a||document;return V(d,"click",function(a){var e=Ac(a.target,function(a){return a===d||c(a)},!0);
e&&e!==d&&!e.disabled&&(a.currentTarget=e,b.call(e,a))})}
function xg(a){a=a||window.event;a=a.target||a.srcElement;3==a.nodeType&&(a=a.parentNode);return a}
var vg=function(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}(function(){var a=!1;
try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function yg(a,b,c){return wg(a,b,function(a){return K(a,c)})}
function zg(a){if(document.createEvent){var b=document.createEvent("HTMLEvents");b.initEvent("click",!0,!0);a.dispatchEvent(b)}else b=document.createEventObject(),a.fireEvent("onclick",b)}
function W(a){a&&("string"==typeof a&&(a=[a]),A(a,function(a){if(a in ib){var b=ib[a],d=b[0],e=b[1],f=b[3];b=b[4];d.removeEventListener?vg()||"boolean"==typeof b?d.removeEventListener(e,f,b):d.removeEventListener(e,f,!!b.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete ib[a]}}))}
;var Ag={},Bg="ontouchstart"in document;function Cg(a,b,c){switch(a){case "mouseover":case "mouseout":var d=3;break;case "mouseenter":case "mouseleave":d=9}return Ac(c,function(a){return K(a,b)},!0,d)}
function Dg(a){var b="mouseover"==a.type&&"mouseenter"in Ag||"mouseout"==a.type&&"mouseleave"in Ag,c=a.type in Ag||b;if("HTML"!=a.target.tagName&&c){if(b){b="mouseover"==a.type?"mouseenter":"mouseleave";c=Ag[b];for(var d in c.f){var e=Cg(b,d,a.target);e&&!Ac(a.relatedTarget,function(a){return a==e},!0)&&c.G(d,e,b,a)}}if(b=Ag[a.type])for(d in b.f)(e=Cg(a.type,d,a.target))&&b.G(d,e,a.type,a)}}
V(document,"blur",Dg,!0);V(document,"change",Dg,!0);V(document,"click",Dg);V(document,"focus",Dg,!0);V(document,"mouseover",Dg);V(document,"mouseout",Dg);V(document,"mousedown",Dg);V(document,"keydown",Dg);V(document,"keyup",Dg);V(document,"keypress",Dg);V(document,"cut",Dg);V(document,"paste",Dg);Bg&&(V(document,"touchstart",Dg),V(document,"touchend",Dg),V(document,"touchcancel",Dg));function Eg(a){this.l=a;this.B={};this.K=[];this.D=[]}
k=Eg.prototype;k.C=function(a){return G(a,X(this))};
function X(a,b){return"yt-uix"+(a.l?"-"+a.l:"")+(b?"-"+b:"")}
k.unregister=function(){Sf(this.K);this.K.length=0;jg(this.D);this.D.length=0};
k.init=ua;k.dispose=ua;function Fg(a,b,c){a.K.push(Qf(b,c,a))}
function Gg(a,b,c){a.D.push(ig(b,c,a))}
function Y(a,b,c,d){d=X(a,d);var e=v(c,a);b in Ag||(Ag[b]=new N);Ag[b].subscribe(d,e);a.B[c]=e}
function Z(a,b,c,d){if(b in Ag){var e=Ag[b];hf(e,X(a,d),a.B[c]);0>=kf(e)&&(e.dispose(),delete Ag[b])}delete a.B[c]}
k.O=function(a,b,c){var d=this.i(a,b);if(d&&(d=u(d))){var e=Ua(arguments,2);Ta(e,0,0,a);d.apply(null,e)}};
k.i=function(a,b){return Wf(a,b)};
function Hg(a,b){Uf(a,"tooltip-text",b)}
;var Ig=window.yt&&window.yt.uix&&window.yt.uix.widgets_||{};y("yt.uix.widgets_",Ig);function Jg(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length){var f=decodeURIComponent((e[0]||"").replace(/\+/g," "));e=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?xa(b[f])?Sa(b[f],e):b[f]=[b[f],e]:b[f]=e}}return b}
;function Kg(a){a=void 0===a?{}:a;za(a)&&(a={callback:a});if(a.gapiHintOverride||O("GAPI_HINT_OVERRIDE")){var b=document.location.href;-1!=b.indexOf("?")?(b=(b||"").split("#")[0],b=b.split("?",2),b=Jg(1<b.length?b[1]:b[0])):b={};(b=b.gapi_jsh)&&kb(a,{_c:{jsl:{h:b}}})}sd("gapi.iframes:gapi.iframes.style.common",a)}
;function Lg(){return u("gapi.iframes.getContext")()}
;function Mg(a){R.call(this,1,arguments);this.b=a}
z(Mg,R);function Ng(a){R.call(this,1,arguments);this.b=a}
z(Ng,R);function Og(a,b,c){R.call(this,3,arguments);this.g=a;this.f=b;this.b=null!=c?!!c:null}
z(Og,R);function Pg(a,b,c,d,e){R.call(this,2,arguments);this.f=a;this.b=b;this.j=c||null;this.g=d||null;this.source=e||null}
z(Pg,R);function Qg(a,b,c){R.call(this,1,arguments);this.b=a;this.f=b}
z(Qg,R);function Rg(a,b,c,d,e,f,g){R.call(this,1,arguments);this.f=a;this.l=b;this.b=c;this.o=d||null;this.j=e||null;this.g=f||null;this.source=g||null}
z(Rg,R);
var Sg=new S("subscription-batch-subscribe",Mg),Tg=new S("subscription-batch-unsubscribe",Mg),Ug=new S("subscription-subscribe",Pg),Vg=new S("subscription-subscribe-loading",Ng),Wg=new S("subscription-subscribe-loaded",Ng),Xg=new S("subscription-subscribe-success",Qg),Yg=new S("subscription-subscribe-external",Pg),Zg=new S("subscription-unsubscribe",Rg),$g=new S("subscription-unsubscirbe-loading",Ng),ah=new S("subscription-unsubscribe-loaded",Ng),bh=new S("subscription-unsubscribe-success",Ng),ch=
new S("subscription-external-unsubscribe",Rg),dh=new S("subscription-enable-ypc",Ng),eh=new S("subscription-disable-ypc",Ng),fh=new S("subscription-prefs",Og),gh=new S("subscription-prefs-success",Og),hh=new S("subscription-prefs-failure",Og);function ih(){var a=pg();return a?a:null}
;function jh(a,b){(a=E(a))&&a.style&&(a.style.display=b?"":"none",Xd(a,"hid",!b))}
function kh(a){return(a=E(a))?"none"!=a.style.display&&!K(a,"hid"):!1}
function lh(a){A(arguments,function(a){!ya(a)||a instanceof Element?jh(a,!0):A(a,function(a){lh(a)})})}
function mh(a){A(arguments,function(a){!ya(a)||a instanceof Element?jh(a,!1):A(a,function(a){mh(a)})})}
;function nh(){Eg.call(this,"tooltip");this.b=0;this.f={}}
z(nh,Eg);va(nh);k=nh.prototype;k.register=function(){Y(this,"mouseover",this.U);Y(this,"mouseout",this.L);Y(this,"focus",this.qa);Y(this,"blur",this.la);Y(this,"click",this.L);Y(this,"touchstart",this.Ha);Y(this,"touchend",this.W);Y(this,"touchcancel",this.W)};
k.unregister=function(){Z(this,"mouseover",this.U);Z(this,"mouseout",this.L);Z(this,"focus",this.qa);Z(this,"blur",this.la);Z(this,"click",this.L);Z(this,"touchstart",this.Ha);Z(this,"touchend",this.W);Z(this,"touchcancel",this.W);this.dispose();nh.w.unregister.call(this)};
k.dispose=function(){for(var a in this.f)this.L(this.f[a]);this.f={}};
k.U=function(a){if(!(this.b&&1E3>Ha()-this.b)){var b=parseInt(this.i(a,"tooltip-hide-timer"),10);b&&(Xf(a,"tooltip-hide-timer"),window.clearTimeout(b));b=v(function(){oh(this,a);Xf(a,"tooltip-show-timer")},this);
var c=parseInt(this.i(a,"tooltip-show-delay"),10)||0;b=P(b,c);Uf(a,"tooltip-show-timer",b.toString());a.title&&(Hg(a,ph(this,a)),a.title="");b=Ba(a).toString();this.f[b]=a}};
k.L=function(a){var b=parseInt(this.i(a,"tooltip-show-timer"),10);b&&(window.clearTimeout(b),Xf(a,"tooltip-show-timer"));b=v(function(){if(a){var b=E(qh(this,a));b&&(rh(b),lc(b),Xf(a,"content-id"));b=E(qh(this,a,"arialabel"));lc(b)}Xf(a,"tooltip-hide-timer")},this);
b=P(b,50);Uf(a,"tooltip-hide-timer",b.toString());if(b=this.i(a,"tooltip-text"))a.title=b;b=Ba(a).toString();delete this.f[b]};
k.qa=function(a,b){this.b=0;this.U(a,b)};
k.la=function(a){this.b=0;this.L(a)};
k.Ha=function(a,b,c){c.changedTouches&&(this.b=0,(a=Cg(b,X(this),c.changedTouches[0].target))&&this.U(a,b))};
k.W=function(a,b,c){c.changedTouches&&(this.b=Ha(),(a=Cg(b,X(this),c.changedTouches[0].target))&&this.L(a))};
function sh(a,b,c){Hg(b,c);a=a.i(b,"content-id");(a=E(a))&&pc(a,c)}
function ph(a,b){return a.i(b,"tooltip-text")||b.title}
function oh(a,b){if(b){var c=ph(a,b);if(c){var d=E(qh(a,b));if(!d){d=document.createElement("div");d.id=qh(a,b);d.className=X(a,"tip");var e=document.createElement("div");e.className=X(a,"tip-body");var f=document.createElement("div");f.className=X(a,"tip-arrow");var g=document.createElement("div");g.setAttribute("aria-hidden","true");g.className=X(a,"tip-content");var h=th(a,b),l=qh(a,b,"content");g.id=l;Uf(b,"content-id",l);e.appendChild(g);h&&d.appendChild(h);d.appendChild(e);d.appendChild(f);
var n=xc(b);l=qh(a,b,"arialabel");f=document.createElement("div");L(f,X(a,"arialabel"));f.id=l;n=b.hasAttribute("aria-label")?b.getAttribute("aria-label"):"rtl"==document.body.getAttribute("dir")?c+" "+n:n+" "+c;pc(f,n);b.setAttribute("aria-labelledby",l);l=ih()||document.body;l.appendChild(f);l.appendChild(d);sh(a,b,c);(c=parseInt(a.i(b,"tooltip-max-width"),10))&&e.offsetWidth>c&&(e.style.width=c+"px",L(g,X(a,"normal-wrap")));g=K(b,X(a,"reverse"));uh(a,b,d,e,h,g)||uh(a,b,d,e,h,!g);var r=X(a,"tip-visible");
P(function(){L(d,r)},0)}}}}
function uh(a,b,c,d,e,f){Xd(c,X(a,"tip-reverse"),f);var g=0;f&&(g=1);var h=De(b);f=new D((h.width-10)/2,f?h.height:0);var l=Ae(b);Qe(new D(l.x+f.x,l.y+f.y),c,g);f=gc(window);if(1==c.nodeType)var n=Be(c);else c=c.changedTouches?c.changedTouches[0]:c,n=new D(c.clientX,c.clientY);c=De(d);var r=Math.floor(c.width/2);g=!!(f.height<n.y+h.height);h=!!(n.y<h.height);l=!!(n.x<r);f=!!(f.width<n.x+r);n=(c.width+3)/-2- -5;a=a.i(b,"force-tooltip-direction");if("left"==a||l)n=-5;else if("right"==a||f)n=20-c.width-
3;a=Math.floor(n)+"px";d.style.left=a;e&&(e.style.left=a,e.style.height=c.height+"px",e.style.width=c.width+"px");return!(g||h)}
function qh(a,b,c){a=X(a)+lg(b);c&&(a+="-"+c);return a}
function th(a,b){var c=null;zb&&K(b,X(a,"masked"))&&((c=E("yt-uix-tooltip-shared-mask"))?(c.parentNode.removeChild(c),lh(c)):(c=document.createElement("IFRAME"),c.src='javascript:""',c.id="yt-uix-tooltip-shared-mask",c.className=X(a,"tip-mask")));return c}
function rh(a){var b=E("yt-uix-tooltip-shared-mask"),c=b&&Ac(b,function(b){return b==a},!1,2);
b&&c&&(b.parentNode.removeChild(b),mh(b),document.body.appendChild(b))}
;function vh(a){var b=wh();if(b=window.open(b,"loginPopup","width=375,height=440,resizable=yes,scrollbars=yes",!0)){var c=Qf("LOGGED_IN",function(b){Sf(O("LOGGED_IN_PUBSUB_KEY",void 0));Jf("LOGGED_IN",!0);a(b)});
Jf("LOGGED_IN_PUBSUB_KEY",c);b.moveTo((screen.width-375)/2,(screen.height-440)/2)}}
function wh(){var a=document.location.protocol+"//"+document.domain+"/post_login";a=Gf(a,"mode","subscribe");a=Gf("/signin?context=popup","next",a);return a=Gf(a,"feature","sub_button")}
y("yt.pubsub.publish",Q);var xh=Object.create(null);xh.log_event="GENERIC_EVENT_LOGGING";xh.log_interaction="INTERACTION_LOGGING";y("ytLoggingTransportLogPayloadsQueue_",u("ytLoggingTransportLogPayloadsQueue_")||{});y("ytLoggingTransportTokensToCttTargetIds_",u("ytLoggingTransportTokensToCttTargetIds_")||{});y("ytLoggingTransportDispatchedStats_",u("ytLoggingTransportDispatchedStats_")||{});y("ytytLoggingTransportCapturedTime_",u("ytLoggingTransportCapturedTime_")||{});Ha();var yh=p(XMLHttpRequest)?function(){return new XMLHttpRequest}:p(ActiveXObject)?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function zh(){if(!yh)return null;var a=yh();return"open"in a?a:null}
;var Ah={"X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},Bh=!1;
function Ch(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=a.match(Af)[1]||null,e=Bf(a.match(Af)[3]||null);d&&e?(d=c,c=a.match(Af),d=d.match(Af),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?Bf(c.match(Af)[3]||null)==e&&(Number(c.match(Af)[4]||null)||null)==(Number(a.match(Af)[4]||null)||null):!0;for(var f in Ah)(d=O(Ah[f]))&&(c||Dh(a,f))&&(b[f]=d);if(c||Dh(a,"X-YouTube-Utc-Offset"))b["X-YouTube-Utc-Offset"]=-(new Date).getTimezoneOffset();return b}
function Dh(a,b){var c=O("CORS_HEADER_WHITELIST")||{},d=Bf(a.match(Af)[3]||null);return d?(c=c[d])?Pa(c,b):!1:!0}
function Eh(a,b){var c=b.format||"JSON";a=Fh(a,b);var d=Gh(a,b),e=!1,f,g=Hh(a,function(a){if(!e){e=!0;f&&window.clearTimeout(f);a:switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:var d=!0;break a;default:d=!1}var g=null;if(d||400<=a.status&&500>a.status)g=Ih(c,a,b.Qb);if(d)a:if(a&&204==a.status)d=!0;else{switch(c){case "XML":d=0==parseInt(g&&g.return_code,10);break a;case "RAW":d=!0;break a}d=!!g}g=g||{};var h=b.context||m;d?b.onSuccess&&
b.onSuccess.call(h,a,g):b.onError&&b.onError.call(h,a,g);b.ca&&b.ca.call(h,a,g)}},b.method,d,b.headers,b.responseType,b.withCredentials);
b.yb&&0<b.timeout&&(f=P(function(){e||(e=!0,g.abort(),window.clearTimeout(f),b.yb.call(b.context||m,g))},b.timeout))}
function Fh(a,b){b.Sb&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=O("XSRF_FIELD_NAME",void 0),d=b.Ia;if(d){d[c]&&delete d[c];d=d||{};var e=a.split("#",2);c=e[0];e=1<e.length?"#"+e[1]:"";var f=c.split("?",2);c=f[0];f=Jg(f[1]||"");for(var g in d)f[g]=d[g];a=Hf(c,f)+e}return a}
function Gh(a,b){var c=O("XSRF_FIELD_NAME",void 0),d=O("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.M,g=O("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.Rb||Bf(a.match(Af)[3]||null)&&!b.withCredentials&&Bf(a.match(Af)[3]||null)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.M&&b.M[g]||(f||(f={}),f[c]=d);f&&t(e)&&(e=Jg(e),kb(e,f),e=b.Bb&&"JSON"==b.Bb?JSON.stringify(e):Ff(e));if(!(c=e)&&(c=f)){a:{for(var l in f){f=!1;break a}f=!0}c=!f}!Bh&&
c&&"POST"!=b.method&&(Bh=!0,Lf(Error("AJAX request with postData should use POST")));return e}
function Ih(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=JSON.parse(a));break;case "XML":if(b=(b=b.responseXML)?Jh(b):null)d={},A(b.getElementsByTagName("*"),function(a){d[a.tagName]=Kh(a)})}c&&Lh(d);
return d}
function Lh(a){if(Aa(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Xb(a[b]);a[c]=d}else Lh(a[b])}}
function Jh(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Kh(a){var b="";A(a.childNodes,function(a){b+=a.nodeValue});
return b}
function Hh(a,b,c,d,e,f,g){function h(){4==(l&&"readyState"in l?l.readyState:0)&&b&&Kf(b)(l)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var l=zh();if(!l)return null;"onloadend"in l?l.addEventListener("loadend",h,!1):l.onreadystatechange=h;l.open(c,a,!0);f&&(l.responseType=f);g&&(l.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=Ch(a,e))for(var n in e)l.setRequestHeader(n,e[n]),"content-type"==n.toLowerCase()&&(c=!1);c&&l.setRequestHeader("Content-Type","application/x-www-form-urlencoded");l.send(d);return l}
;function Mh(){var a=new tf;(a=a.isAvailable()?new zf(a,"yt.innertube"):null)||(a=new uf("yt.innertube"),a=a.isAvailable()?a:null);this.b=a?new pf(a):null;this.f=document.domain||window.location.hostname}
Mh.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.b)try{this.b.set(a,b,Ha()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(ke(b))}catch(f){return}else e=escape(b);b=this.f;Oc.set(""+a,e,c,"/",void 0===b?"youtube.com":b,!1)};
Mh.prototype.get=function(a,b){var c=void 0,d=!this.b;if(!d)try{c=this.b.get(a)}catch(e){d=!0}if(d&&(c=Oc.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
Mh.prototype.remove=function(a){this.b&&this.b.remove(a);var b=this.f;Oc.remove(""+a,"/",void 0===b?"youtube.com":b)};new Mh;var Nh=Ha().toString();var Oh;a:{if(window.crypto&&window.crypto.getRandomValues)try{var Ph=Array(16),Qh=new Uint8Array(16);window.crypto.getRandomValues(Qh);for(var Rh=0;Rh<Ph.length;Rh++)Ph[Rh]=Qh[Rh];Oh=Ph;break a}catch(a){}for(var Sh=Array(16),Th=0;16>Th;Th++){for(var Uh=Ha(),Vh=0;Vh<Uh%23;Vh++)Sh[Th]=Math.random();Sh[Th]=Math.floor(256*Math.random())}if(Nh)for(var Wh=1,Xh=0;Xh<Nh.length;Xh++)Sh[Wh%16]=Sh[Wh%16]^Sh[(Wh-1)%16]/4^Nh.charCodeAt(Xh),Wh++;Oh=Sh}
for(var Yh=Oh,Zh=[],$h=0;$h<Yh.length;$h++)Zh.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(Yh[$h]&63));y("yt.logging.screen.getRootVeType",function(a){a=void 0===a?0:a;a=void 0===a?0:a;return O(0==a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a,void 0)});
y("yt.logging.screen.getCurrentCsn",function(a){var b=a=void 0===a?0:a;b=void 0===b?0:b;(b=O(0==b?"client-screen-nonce":"client-screen-nonce."+b))||0!=a||(b=O("EVENT_ID"));return b?b:null});function ai(){Eg.call(this,"button");this.b=null;this.g=[];this.f={}}
z(ai,Eg);va(ai);k=ai.prototype;k.register=function(){Y(this,"click",this.Ja);Y(this,"keydown",this.ua);Y(this,"keypress",this.va);Fg(this,"page-scroll",this.lb)};
k.unregister=function(){Z(this,"click",this.Ja);Z(this,"keydown",this.ua);Z(this,"keypress",this.va);bi(this);this.f={};ai.w.unregister.call(this)};
k.Ja=function(a){a&&!a.disabled&&(this.toggle(a),this.click(a))};
k.ua=function(a,b,c){if(!(c.altKey||c.ctrlKey||c.shiftKey||c.metaKey)&&(b=ci(this,a))){var d=function(a){var b="";a.tagName&&(b=a.tagName.toLowerCase());return"ul"==b||"table"==b},e;
d(b)?e=b:e=qc(b,d);if(e){e=e.tagName.toLowerCase();if("ul"==e)var f=this.sb;else"table"==e&&(f=this.rb);f&&di(this,a,b,c,v(f,this))}}};
k.lb=function(){var a=this.f,b=0;for(d in a)b++;if(0!=b)for(var c in a){b=a[c];var d=G(b.activeButtonNode||b.parentNode,X(this));if(void 0==d||void 0==b)break;ei(this,d,b,!0)}};
function di(a,b,c,d,e){var f=kh(c),g=9==d.keyCode;if(g||32==d.keyCode||13==d.keyCode)if(d=fi(a,c)){if(p(d.firstElementChild))b=d.firstElementChild;else for(b=d.firstChild;b&&1!=b.nodeType;)b=b.nextSibling;if("a"==b.tagName.toLowerCase()){var h=void 0===h?{}:h;var l=void 0===l?"":l;var n=void 0===n?window:n;n=n.location;h=Hf(b.href,h)+l;h instanceof Qb||h instanceof Qb||(h=h.aa?h.Z():String(h),Sb.test(h)||(h="about:invalid#zClosurez"),h=Tb(h));h instanceof Qb&&h.constructor===Qb&&h.f===Rb?h=h.b:(wa(h),
h="type_error:SafeUrl");n.href=h}else zg(b)}else g&&gi(a,b);else f?27==d.keyCode?(fi(a,c),gi(a,b)):e(b,c,d):(h=K(b,X(a,"reverse"))?38:40,d.keyCode==h&&(zg(b),d.preventDefault()))}
k.va=function(a,b,c){c.altKey||c.ctrlKey||c.shiftKey||c.metaKey||(a=ci(this,a),kh(a)&&c.preventDefault())};
function fi(a,b){var c=X(a,"menu-item-highlight"),d=F(c,b);d&&M(d,c);return d}
function hi(a,b,c){L(c,X(a,"menu-item-highlight"));var d=c.getAttribute("id");d||(d=X(a,"item-id-"+Ba(c)),c.setAttribute("id",d));b.setAttribute("aria-activedescendant",d)}
k.rb=function(a,b,c){var d=fi(this,b);if(d){var e=og("table",b);b=dc(document,"td",null,e);d=ii(d,b,dc(document,"td",null,og("tr",e)).length,c);-1!=d&&(hi(this,a,b[d]),c.preventDefault())}};
k.sb=function(a,b,c){if(40==c.keyCode||38==c.keyCode){var d=fi(this,b);d&&(b=La(dc(document,"li",null,b),kh),hi(this,a,b[ii(d,b,1,c)]),c.preventDefault())}};
function ii(a,b,c,d){var e=b.length;a=Ka(b,a);if(-1==a)if(38==d.keyCode)a=e-c;else{if(37==d.keyCode||38==d.keyCode||40==d.keyCode)a=0}else 39==d.keyCode?(a%c==c-1&&(a-=c),a+=1):37==d.keyCode?(0==a%c&&(a+=c),--a):38==d.keyCode?(a<c&&(a+=e),a-=c):40==d.keyCode&&(a>=e-c&&(a-=e),a+=c);return a}
function ji(a,b){var c=b.iframeMask;c||(c=document.createElement("IFRAME"),c.src='javascript:""',c.className=X(a,"menu-mask"),mh(c),b.iframeMask=c);return c}
function ei(a,b,c,d){var e=G(b,X(a,"group")),f=!!a.i(b,"button-menu-ignore-group");e=e&&!f?e:b;f=9;var g=8,h=Fe(b);if(K(b,X(a,"reverse"))){f=8;g=9;h=h.top+"px";try{c.style.maxHeight=h}catch(r){}}K(b,"flip")&&(K(b,X(a,"reverse"))?(f=12,g=13):(f=13,g=12));var l;a.i(b,"button-has-sibling-menu")?l=ye(e):a.i(b,"button-menu-root-container")&&(l=ki(a,b));C&&!Lb("8")&&(l=null);if(l){var n=Fe(l);n=new qe(-n.top,n.left,n.top,-n.left)}l=new D(0,1);K(b,X(a,"center-menu"))&&(l.x-=Math.round((De(c).width-De(b).width)/
2));d&&(l.y+=ic(document).y);if(a=ji(a,b))b=De(c),a.style.width=b.width+"px",a.style.height=b.height+"px",Oe(e,f,a,g,l,n,197),d&&se(a,"position","fixed");Oe(e,f,c,g,l,n,197)}
function ki(a,b){if(a.i(b,"button-menu-root-container")){var c=a.i(b,"button-menu-root-container");return G(b,c)}return document.body}
k.La=function(a){if(a){var b=ci(this,a);if(b){a.setAttribute("aria-pressed","true");a.setAttribute("aria-expanded","true");b.originalParentNode=b.parentNode;b.activeButtonNode=a;b.parentNode.removeChild(b);var c;this.i(a,"button-has-sibling-menu")?c=a.parentNode:c=ki(this,a);c.appendChild(b);b.style.minWidth=a.offsetWidth-2+"px";var d=ji(this,a);d&&c.appendChild(d);(c=!!this.i(a,"button-menu-fixed"))&&(this.f[lg(a).toString()]=b);ei(this,a,b,c);Tf("yt-uix-button-menu-before-show",a,b);lh(b);d&&lh(d);
this.O(a,"button-menu-action",!0);L(a,X(this,"active"));b=v(this.Ka,this,a,!1);d=v(this.Ka,this,a,!0);c=v(this.Db,this,a,void 0);this.b&&ci(this,this.b)==ci(this,a)||bi(this);Q("yt-uix-button-menu-show",a);W(this.g);this.g=[V(document,"click",d),V(document,"contextmenu",b),V(window,"resize",c)];this.b=a}}};
function gi(a,b){if(b){var c=ci(a,b);if(c){a.b=null;b.setAttribute("aria-pressed","false");b.setAttribute("aria-expanded","false");b.removeAttribute("aria-activedescendant");mh(c);a.O(b,"button-menu-action",!1);var d=ji(a,b),e=lg(c).toString();delete a.f[e];P(function(){d&&d.parentNode&&(mh(d),d.parentNode.removeChild(d));c.originalParentNode&&(c.parentNode.removeChild(c),c.originalParentNode.appendChild(c),c.originalParentNode=null,c.activeButtonNode=null)},1)}e=G(b,X(a,"group"));
var f=[X(a,"active")];e&&f.push(X(a,"group-active"));Wd(b,f);Q("yt-uix-button-menu-hide",b);W(a.g);a.g.length=0}}
k.Db=function(a,b){var c=ci(this,a);if(c){b&&(b instanceof Ub?c.innerHTML=Wb(b):pc(c,b));var d=!!this.i(a,"button-menu-fixed");ei(this,a,c,d)}};
k.Ka=function(a,b,c){c=xg(c);var d=G(c,X(this));if(d){d=ci(this,d);var e=ci(this,a);if(d==e)return}d=G(c,X(this,"menu"));e=d==ci(this,a);var f=K(c,X(this,"menu-item")),g=K(c,X(this,"menu-close"));if(!d||e&&(f||g))gi(this,a),d&&b&&this.i(a,"button-menu-indicate-selected")&&((a=F(X(this,"content"),a))&&pc(a,xc(c)),li(this,d,c))};
function li(a,b,c){var d=X(a,"menu-item-selected");A(cc(d,b),function(a){M(a,d)});
L(c.parentNode,d)}
function ci(a,b){if(!b.widgetMenu){var c=a.i(b,"button-menu-id");c=c&&E(c);var d=X(a,"menu");c?Vd(c,[d,X(a,"menu-external")]):c=F(d,b);b.widgetMenu=c}return b.widgetMenu}
k.isToggled=function(a){return K(a,X(this,"toggled"))};
k.toggle=function(a){if(this.i(a,"button-toggle")){var b=G(a,X(this,"group")),c=X(this,"toggled"),d=K(a,c);if(b&&this.i(b,"button-toggle-group")){var e=this.i(b,"button-toggle-group");A(cc(X(this),b),function(b){b!=a||"optional"==e&&d?(M(b,c),b.removeAttribute("aria-pressed")):(L(a,c),b.setAttribute("aria-pressed","true"))})}else d?a.removeAttribute("aria-pressed"):a.setAttribute("aria-pressed","true"),Zd(a,c)}};
k.click=function(a){if(ci(this,a)){var b=ci(this,a);if(b){var c=G(b.activeButtonNode||b.parentNode,X(this));c&&c!=a?(gi(this,c),P(v(this.La,this,a),1)):kh(b)?gi(this,a):this.La(a)}a.focus()}this.O(a,"button-action")};
function bi(a){a.b&&gi(a,a.b)}
;function mi(a){Eg.call(this,a);this.g=null}
z(mi,Eg);k=mi.prototype;k.C=function(a){var b=Eg.prototype.C.call(this,a);return b?b:a};
k.register=function(){Fg(this,"yt-uix-kbd-nav-move-out-done",this.hide)};
k.dispose=function(){ni(this);mi.w.dispose.call(this)};
k.i=function(a,b){var c=mi.w.i.call(this,a,b);return c?c:(c=mi.w.i.call(this,a,"card-config"))&&(c=u(c))&&c[b]?c[b]:null};
k.show=function(a){var b=this.C(a);if(b){L(b,X(this,"active"));var c=oi(this,a,b);if(c){c.cardTargetNode=a;c.cardRootNode=b;pi(this,a,c);var d=X(this,"card-visible"),e=this.i(a,"card-delegate-show")&&this.i(b,"card-action");this.O(b,"card-action",a);this.g=a;mh(c);P(v(function(){e||(lh(c),Q("yt-uix-card-show",b,a,c));qi(c);L(c,d);Q("yt-uix-kbd-nav-move-in-to",c)},this),10)}}};
function oi(a,b,c){var d=c||b,e=X(a,"card");c=ri(a,d);var f=E(X(a,"card")+lg(d));if(f)return a=F(X(a,"card-body"),f),oc(a,c)||(lc(c),a.appendChild(c)),f;f=document.createElement("div");f.id=X(a,"card")+lg(d);f.className=e;(d=a.i(d,"card-class"))&&Vd(f,d.split(/\s+/));d=document.createElement("div");d.className=X(a,"card-border");b=a.i(b,"orientation")||"horizontal";e=document.createElement("div");e.className="yt-uix-card-border-arrow yt-uix-card-border-arrow-"+b;var g=document.createElement("div");
g.className=X(a,"card-body");a=document.createElement("div");a.className="yt-uix-card-body-arrow yt-uix-card-body-arrow-"+b;lc(c);g.appendChild(c);d.appendChild(a);d.appendChild(g);f.appendChild(e);f.appendChild(d);document.body.appendChild(f);return f}
function pi(a,b,c){var d=a.i(b,"orientation")||"horizontal",e=F(X(a,"anchor"),b)||b,f=a.i(b,"position"),g=!!a.i(b,"force-position"),h=a.i(b,"position-fixed");d="horizontal"==d;var l="bottomright"==f||"bottomleft"==f,n="topright"==f||"bottomright"==f;if(n&&l){var r=13;var x=8}else n&&!l?(r=12,x=9):!n&&l?(r=9,x=12):(r=8,x=13);var q=Ge(document.body);f=Ge(b);q!=f&&(r^=4);if(d){f=b.offsetHeight/2-12;var J=new D(-12,b.offsetHeight+6)}else f=b.offsetWidth/2-6,J=new D(b.offsetWidth+6,-12);var w=De(c);f=
Math.min(f,(d?w.height:w.width)-24-6);6>f&&(f=6,d?J.y+=12-b.offsetHeight/2:J.x+=12-b.offsetWidth/2);w=null;g||(w=10);b=X(a,"card-flip");a=X(a,"card-reverse");Xd(c,b,n);Xd(c,a,l);w=Oe(e,r,c,x,J,null,w);!g&&w&&(w&48&&(n=!n,r^=4,x^=4),w&192&&(l=!l,r^=1,x^=1),Xd(c,b,n),Xd(c,a,l),Oe(e,r,c,x,J));h&&(e=parseInt(c.style.top,10),g=ic(document).y,se(c,"position","fixed"),se(c,"top",e-g+"px"));q&&(c.style.right="",e=Fe(c),e.left=e.left||parseInt(c.style.left,10),g=gc(window),c.style.left="",c.style.right=g.width-
e.left-e.width+"px");e=F("yt-uix-card-body-arrow",c);g=F("yt-uix-card-border-arrow",c);d=d?l?"top":"bottom":!q&&n||q&&!n?"left":"right";e.setAttribute("style","");g.setAttribute("style","");e.style[d]=f+"px";g.style[d]=f+"px";l=F("yt-uix-card-arrow",c);n=F("yt-uix-card-arrow-background",c);l&&n&&(c="right"==d?De(c).width-f-13:f+11,f=c/Math.sqrt(2),l.style.left=c+"px",l.style.marginLeft="1px",n.style.marginLeft=-f+"px",n.style.marginTop=f+"px")}
k.hide=function(a){if(a=this.C(a)){var b=E(X(this,"card")+lg(a));b&&(M(a,X(this,"active")),M(b,X(this,"card-visible")),mh(b),this.g=null,b.cardTargetNode=null,b.cardRootNode=null,b.cardMask&&(lc(b.cardMask),b.cardMask=null))}};
function ni(a){a.g&&a.hide(a.g)}
k.Cb=function(a,b){var c=this.C(a);if(c){if(b){var d=ri(this,c);if(!d)return;b instanceof Ub?d.innerHTML=Wb(b):pc(d,b)}K(c,X(this,"active"))&&(c=oi(this,a,c),pi(this,a,c),lh(c),qi(c))}};
k.isActive=function(a){return(a=this.C(a))?K(a,X(this,"active")):!1};
function ri(a,b){var c=b.cardContentNode;if(!c){var d=X(a,"content"),e=X(a,"card-content");(c=(c=a.i(b,"card-id"))?E(c):F(d,b))||(c=document.createElement("div"));var f=c;M(f,d);L(f,e);b.cardContentNode=c}return c}
function qi(a){var b=a.cardMask;b||(b=document.createElement("IFRAME"),b.src='javascript:""',Vd(b,["yt-uix-card-iframe-mask"]),a.cardMask=b);b.style.position=a.style.position;b.style.top=a.style.top;b.style.left=a.offsetLeft+"px";b.style.height=a.clientHeight+"px";b.style.width=a.clientWidth+"px";document.body.appendChild(b)}
;function si(){Eg.call(this,"kbd-nav")}
var ti;z(si,Eg);va(si);k=si.prototype;k.register=function(){Y(this,"keydown",this.sa);Fg(this,"yt-uix-kbd-nav-move-in",this.Aa);Fg(this,"yt-uix-kbd-nav-move-in-to",this.tb);Fg(this,"yt-uix-kbd-move-next",this.Ba);Fg(this,"yt-uix-kbd-nav-move-to",this.S)};
k.unregister=function(){Z(this,"keydown",this.sa);W(ti)};
k.sa=function(a,b,c){var d=c.keyCode;if(a=G(a,X(this)))switch(d){case 13:case 32:this.Aa(a);break;case 27:c.preventDefault();c.stopImmediatePropagation();a:{for(c=ae(a,"kbdNavMoveOut");!c;){c=G(a.parentElement,X(this));if(!c)break a;c=ae(c,"kbdNavMoveOut")}c=E(c);this.S(c);Q("yt-uix-kbd-nav-move-out-done",c)}break;case 40:case 38:if((b=c.target)&&K(a,X(this,"list")))switch(d){case 40:this.Ba(b,a);break;case 38:d=document.activeElement==a,a=ui(a),b=a.indexOf(b),0>b&&!d||(b=d?a.length-1:(a.length+b-
1)%a.length,a[b].focus(),vi(this,a[b]))}c.preventDefault()}};
k.Aa=function(a){var b=ae(a,"kbdNavMoveIn");b=E(b);wi(this,a,b);this.S(b)};
k.tb=function(a){var b=document;try{var c=b&&b.activeElement;var d=c&&c.nodeName?c:null}catch(e){d=null}wi(this,d,a);this.S(a)};
k.S=function(a){if(a)if(uc(a))a.focus();else{var b=qc(a,function(a){return nc(a)?uc(a):!1});
b?b.focus():(a.setAttribute("tabindex","-1"),a.focus())}};
function wi(a,b,c){if(b&&c)if(L(c,X(a)),a=b.id,a||(a="kbd-nav-"+Math.floor(1E6*Math.random()+1),b.id=a),b=a,$d&&c.dataset)c.dataset.kbdNavMoveOut=b;else{if(/-[a-z]/.test("kbdNavMoveOut"))throw Error("");c.setAttribute("data-"+"kbdNavMoveOut".replace(/([A-Z])/g,"-$1").toLowerCase(),b)}}
k.Ba=function(a,b){var c=document.activeElement==b,d=ui(b),e=d.indexOf(a);0>e&&!c||(c=c?0:(e+1)%d.length,d[c].focus(),vi(this,d[c]))};
function vi(a,b){if(b){var c=zc(b,"LI");c&&(L(c,X(a,"highlight")),ti=V(b,"blur",v(function(a){M(a,X(this,"highlight"));W(ti)},a,c)))}}
function ui(a){if("UL"!=a.tagName.toUpperCase())return[];a=La(mc(a),function(a){return"LI"==a.tagName.toUpperCase()});
return La(Ma(a,function(a){return kh(a)?qc(a,function(a){return nc(a)?uc(a):!1}):!1}),function(a){return!!a})}
;function xi(){Eg.call(this,"menu");this.f=this.b=null;this.g={};this.o={};this.j=null}
z(xi,Eg);va(xi);function yi(a){var b=xi.v();if(K(a,X(b)))return a;var c=b.C(a);return c?c:G(a,X(b,"content"))==b.b?b.f:null}
k=xi.prototype;k.register=function(){Y(this,"click",this.ra);Y(this,"mouseenter",this.jb);Fg(this,"page-scroll",this.mb);Fg(this,"yt-uix-kbd-nav-move-out-done",function(a){a=this.C(a);zi(this,a)});
this.j=new N};
k.unregister=function(){Z(this,"click",this.ra);this.f=this.b=null;W(Va(gb(this.g)));this.g={};fb(this.o,function(a){lc(a)},this);
this.o={};Td(this.j);this.j=null;xi.w.unregister.call(this)};
k.ra=function(a,b,c){a&&(b=Ai(this,a),!b.disabled&&ng(c.target,b)&&Bi(this,a))};
k.jb=function(a,b,c){a&&K(a,X(this,"hover"))&&ng(c.target,Ai(this,a))&&Bi(this,a,!0)};
k.mb=function(){this.b&&this.f&&Ci(this,this.f,this.b)};
function Ci(a,b,c){var d=Di(a,b);if(d){var e=De(c);if(e instanceof Zb){var f=e.height;e=e.width}else throw Error("missing height argument");d.style.width=Ce(e,!0);d.style.height=Ce(f,!0)}c==a.b&&(e=9,f=8,K(b,X(a,"reversed"))&&(e^=1,f^=1),K(b,X(a,"flipped"))&&(e^=4,f^=4),a=new D(0,1),d&&Oe(b,e,d,f,a,null,197),Oe(b,e,c,f,a,null,197))}
function Bi(a,b,c){Ei(a,b)&&!c?zi(a,b):(Fi(a,b),!a.b||ng(b,a.b)?a.Ma(b):gf(a.j,v(a.Ma,a,b)))}
k.Ma=function(a){if(a){var b=Gi(this,a);if(b){Tf("yt-uix-menu-before-show",a,b);this.b?ng(a,this.b)||zi(this,this.f):(this.f=a,this.b=b,K(a,X(this,"sibling-content"))||(lc(b),document.body.appendChild(b)),b.style.minWidth=Ai(this,a).offsetWidth-2+"px");var c=Di(this,a);c&&b.parentNode&&b.parentNode.insertBefore(c,b.nextSibling);M(b,X(this,"content-hidden"));Ci(this,a,b);Vd(Ai(this,a),[X(this,"trigger-selected"),"yt-uix-button-toggled"]);Q("yt-uix-menu-show",a);Hi(b);Ii(this,a);Q("yt-uix-kbd-nav-move-in-to",
b);var d=v(this.Eb,this,a),e=v(this.pb,this,a);c=Ba(a).toString();this.g[c]=[V(b,"click",e),V(document,"click",d)];K(a,X(this,"indicate-selected"))&&(d=v(this.qb,this,a),this.g[c].push(V(b,"click",d)));K(a,X(this,"hover"))&&(a=v(this.kb,this,a),this.g[c].push(V(document,"mousemove",a)))}}};
k.kb=function(a,b){var c=xg(b);c&&(ng(c,Ai(this,a))||Ji(this,c)||Ki(this,a))};
k.Eb=function(a,b){var c=xg(b);if(c){if(Ji(this,c)){var d=G(c,X(this,"content")),e=zc(c,"LI");e&&d&&oc(d,e)&&Tf("yt-uix-menu-item-clicked",c);c=G(c,X(this,"close-on-select"));if(!c)return;d=yi(c)}zi(this,d||a)}};
function Fi(a,b){if(b){var c=G(b,X(a,"content"));c&&A(cc(X(a),c),function(a){!ng(a,b)&&Ei(this,a)&&Ki(this,a)},a)}}
function zi(a,b){if(b){var c=[];c.push(b);var d=Gi(a,b);d&&(d=cc(X(a),d),d=Ra(d),c=c.concat(d),A(c,function(a){Ei(this,a)&&Ki(this,a)},a))}}
function Ki(a,b){if(b){var c=Gi(a,b);Wd(Ai(a,b),[X(a,"trigger-selected"),"yt-uix-button-toggled"]);L(c,X(a,"content-hidden"));var d=Gi(a,b);d&&ec(d,{"aria-expanded":"false"});(d=Di(a,b))&&d.parentNode&&lc(d);c&&c==a.b&&(a.f.appendChild(c),a.b=null,a.f=null,a.j&&a.j.G("ROOT_MENU_REMOVED"));Q("yt-uix-menu-hide",b);c=Ba(b).toString();W(a.g[c]);delete a.g[c]}}
k.pb=function(a,b){var c=xg(b);c&&Li(this,a,c)};
k.qb=function(a,b){var c=xg(b);if(c){var d=Ai(this,a);if(d&&(c=zc(c,"LI")))if(c=xc(c).trim(),d.hasChildNodes()){var e=ai.v();(d=F(X(e,"content"),d))&&pc(d,c)}else pc(d,c)}};
function Ii(a,b){var c=Gi(a,b);if(c){A(c.children,function(a){"LI"==a.tagName&&ec(a,{role:"menuitem"})});
ec(c,{"aria-expanded":"true"});var d=c.id;d||(d="aria-menu-id-"+Ba(c),c.id=d);(c=Ai(a,b))&&ec(c,{"aria-controls":d})}}
function Li(a,b,c){var d=Gi(a,b);d&&K(b,X(a,"checked"))&&(a=zc(c,"LI"))&&(a=F("yt-ui-menu-item-checked-hid",a))&&(A(cc("yt-ui-menu-item-checked",d),function(a){Yd(a,"yt-ui-menu-item-checked","yt-ui-menu-item-checked-hid")}),Yd(a,"yt-ui-menu-item-checked-hid","yt-ui-menu-item-checked"))}
function Ei(a,b){var c=Gi(a,b);return c?!K(c,X(a,"content-hidden")):!1}
function Hi(a){A(dc(document,"UL",null,a),function(a){a.tabIndex=0;var b=si.v();Vd(a,[X(b),X(b,"list")])})}
function Gi(a,b){var c=Wf(b,"menu-content-id");return c&&(c=E(c))?(Vd(c,[X(a,"content"),X(a,"content-external")]),c):b==a.f?a.b:F(X(a,"content"),b)}
function Di(a,b){var c=Ba(b).toString(),d=a.o[c];if(!d){d=document.createElement("IFRAME");d.src='javascript:""';var e=[X(a,"mask")];A(Ud(b),function(a){e.push(a+"-mask")});
Vd(d,e);a.o[c]=d}return d||null}
function Ai(a,b){return F(X(a,"trigger"),b)}
function Ji(a,b){return ng(b,a.b)||ng(b,a.f)}
;function Mi(){mi.call(this,"clickcard");this.b={};this.f={}}
z(Mi,mi);va(Mi);k=Mi.prototype;k.register=function(){Mi.w.register.call(this);Y(this,"click",this.oa,"target");Y(this,"click",this.na,"close")};
k.unregister=function(){Mi.w.unregister.call(this);Z(this,"click",this.oa,"target");Z(this,"click",this.na,"close");for(var a in this.b)W(this.b[a]);this.b={};for(a in this.f)W(this.f[a]);this.f={}};
k.oa=function(a,b,c){c.preventDefault();b=zc(c.target,"button");if(!b||!b.disabled){if(b=this.i(a,"card-target"))a=document,a=t(b)?a.getElementById(b):b;b=this.C(a);this.i(b,"disabled")||(K(b,X(this,"active"))?(this.hide(a),M(b,X(this,"active"))):(this.show(a),L(b,X(this,"active"))))}};
k.show=function(a){Mi.w.show.call(this,a);var b=this.C(a),c=Ba(a).toString();if(!Wf(b,"click-outside-persists")){if(this.b[c])return;b=V(document,"click",v(this.pa,this,a));var d=V(window,"blur",v(this.pa,this,a));this.b[c]=[b,d]}a=V(window,"resize",v(this.Cb,this,a,void 0));this.f[c]=a};
k.hide=function(a){Mi.w.hide.call(this,a);a=Ba(a).toString();var b=this.b[a];b&&(W(b),this.b[a]=null);if(b=this.f[a])W(b),delete this.f[a]};
k.pa=function(a,b){var c="yt-uix"+(this.l?"-"+this.l:"")+"-card",d=null;b.target&&(d=G(b.target,c)||G(yi(b.target),c));(d=d||G(document.activeElement,c)||G(yi(document.activeElement),c))||this.hide(a)};
k.na=function(a){(a=G(a,X(this,"card")))&&(a=a.cardTargetNode)&&this.hide(a)};function Ni(){mi.call(this,"hovercard")}
z(Ni,mi);va(Ni);k=Ni.prototype;k.register=function(){Y(this,"mouseenter",this.wa,"target");Y(this,"mouseleave",this.ya,"target");Y(this,"mouseenter",this.xa,"card");Y(this,"mouseleave",this.za,"card")};
k.unregister=function(){Z(this,"mouseenter",this.wa,"target");Z(this,"mouseleave",this.ya,"target");Z(this,"mouseenter",this.xa,"card");Z(this,"mouseleave",this.za,"card")};
k.wa=function(a){if(Oi!=a){Oi&&(this.hide(Oi),Oi=null);var b=v(this.show,this,a),c=parseInt(this.i(a,"delay-show"),10);b=P(b,-1<c?c:200);Uf(a,"card-timer",b.toString());Oi=a;a.alt&&(Uf(a,"card-alt",a.alt),a.alt="");a.title&&(Uf(a,"card-title",a.title),a.title="")}};
k.ya=function(a){var b=parseInt(this.i(a,"card-timer"),10);window.clearTimeout(b);this.C(a).isCardHidable=!0;b=parseInt(this.i(a,"delay-hide"),10);b=-1<b?b:200;P(v(this.nb,this,a),b);if(b=this.i(a,"card-alt"))a.alt=b;if(b=this.i(a,"card-title"))a.title=b};
k.nb=function(a){this.C(a).isCardHidable&&(this.hide(a),Oi=null)};
k.xa=function(a){a&&(a.cardRootNode.isCardHidable=!1)};
k.za=function(a){a&&this.hide(a.cardTargetNode)};
var Oi=null;function Pi(a,b,c,d,e,f){this.b=a;this.B=null;this.g=F("yt-dialog-fg",this.b)||this.b;if(a=F("yt-dialog-title",this.g)){var g="yt-dialog-title-"+Ba(this.g);a.setAttribute("id",g);this.g.setAttribute("aria-labelledby",g)}this.g.setAttribute("tabindex","-1");this.R=F("yt-dialog-focus-trap",this.b);this.fa=!1;this.j=new N;this.D=[];this.D.push(yg(this.b,v(this.ub,this),"yt-dialog-dismiss"));this.D.push(V(this.R,"focus",v(this.ib,this),!0));Qi(this);this.Qa=b;this.Xa=c;this.Wa=d;this.K=e;this.Ya=f;this.o=
this.l=null}
var Ri={LOADING:"loading",Hb:"content",Ob:"working"};function Si(a,b){a.T()||a.j.subscribe("post-all",b)}
function Qi(a){a=F("yt-dialog-fg-content",a.b);var b=[];fb(Ri,function(a){b.push("yt-dialog-show-"+a)});
Wd(a,b);L(a,"yt-dialog-show-content")}
k=Pi.prototype;
k.show=function(){if(!this.T()){this.B=document.activeElement;if(!this.Wa){this.f||(this.f=E("yt-dialog-bg"),this.f||(this.f=document.createElement("div"),this.f.id="yt-dialog-bg",this.f.className="yt-dialog-bg",document.body.appendChild(this.f)));var a=window,b=a.document;var c=0;if(b){c=b.body;var d=b.documentElement;if(d&&c)if(a=gc(a).height,hc(b)&&d.scrollHeight)c=d.scrollHeight!=a?d.scrollHeight:d.offsetHeight;else{b=d.scrollHeight;var e=d.offsetHeight;d.clientHeight!=e&&(b=c.scrollHeight,e=
c.offsetHeight);c=b>a?b>e?b:e:b<e?b:e}else c=0}this.f.style.height=c+"px";lh(this.f)}this.ta();c=Ti(this);Ui(c);this.l=V(document,"keydown",v(this.ob,this));c=this.b;d=Qf("player-added",this.ta,this);Uf(c,"player-ready-pubsub-key",d);this.Xa&&(this.o=V(document,"click",v(this.Ab,this)));lh(this.b);this.g.setAttribute("tabindex","0");Vi(this);this.K||L(document.body,"yt-dialog-active");bi(ai.v());ni(Mi.v());ni(Ni.v());Q("yt-ui-dialog-show-complete",this)}};
function Wi(){return Na(cc("yt-dialog"),function(a){return kh(a)})}
k.ta=function(){if(!this.Ya){var a=this.b;Xd(document.body,"hide-players",!0);a&&Xd(a,"preserve-players",!0)}};
function Ti(a){var b=dc(document,"iframe",null,a.b);A(b,function(a){var b=Wf(a,"onload");b&&(b=u(b))&&V(a,"load",b);if(b=Wf(a,"src"))a.src=b},a);
return Ra(b)}
function Ui(a){A(document.getElementsByTagName("iframe"),function(b){-1==Ka(a,b)&&L(b,"iframe-hid")})}
function Xi(){A(cc("iframe-hid"),function(a){M(a,"iframe-hid")})}
k.ub=function(a){a=a.currentTarget;a.disabled||(a=Wf(a,"action")||"",this.dismiss(a))};
k.dismiss=function(a){if(!this.T()){this.j.G("pre-all");this.j.G("pre-"+a);mh(this.b);ni(Mi.v());ni(Ni.v());this.g.setAttribute("tabindex","-1");Wi()||(mh(this.f),this.K||M(document.body,"yt-dialog-active"),qg(),Xi());this.l&&(W(this.l),this.l=null);this.o&&(W(this.o),this.o=null);var b=this.b;if(b){var c=Wf(b,"player-ready-pubsub-key");c&&(Sf(c),Xf(b,"player-ready-pubsub-key"))}this.j.G("post-all");Q("yt-ui-dialog-hide-complete",this);"cancel"==a&&Q("yt-ui-dialog-cancelled",this);this.j&&this.j.G("post-"+
a);this.B&&this.B.focus()}};
k.setTitle=function(a){pc(F("yt-dialog-title",this.b),a)};
k.ob=function(a){P(v(function(){this.Qa||27!=a.keyCode||this.dismiss("cancel")},this),0);
9==a.keyCode&&a.shiftKey&&K(document.activeElement,"yt-dialog-fg")&&a.preventDefault()};
k.Ab=function(a){"yt-dialog-base"==a.target.className&&this.dismiss("cancel")};
k.T=function(){return this.fa};
k.dispose=function(){kh(this.b)&&this.dismiss("dispose");W(this.D);this.D.length=0;P(v(function(){this.B=null},this),0);
this.R=this.g=null;this.j.dispose();this.j=null;this.fa=!0};
k.ib=function(a){a.stopPropagation();Vi(this)};
function Vi(a){P(v(function(){this.g&&this.g.focus()},a),0)}
y("yt.ui.Dialog",Pi);function Yi(){Eg.call(this,"overlay");this.j=this.f=this.g=this.b=null}
z(Yi,Eg);va(Yi);k=Yi.prototype;k.register=function(){Y(this,"click",this.da,"target");Y(this,"click",this.hide,"close");Zi(this)};
k.unregister=function(){Yi.w.unregister.call(this);Z(this,"click",this.da,"target");Z(this,"click",this.hide,"close");this.j&&(Sf(this.j),this.j=null);this.f&&(W(this.f),this.f=null)};
k.da=function(a){if(!this.b||!kh(this.b.b)){var b=this.C(a);a=$i(b,a);b||(b=a?a.overlayParentNode:null);if(b&&a){var c=!!this.i(b,"disable-shortcuts")||!1,d=!!this.i(b,"disable-outside-click-dismiss")||!1;this.b=new Pi(a,c);this.g=b;var e=F("yt-dialog-fg",a);if(e){var f=this.i(b,"overlay-class")||"",g=this.i(b,"overlay-style")||"default",h=this.i(b,"overlay-shape")||"default";f=f?f.split(" "):[];f.push(X(this,g));f.push(X(this,h));Vd(e,f)}this.b.show();Q("yt-uix-kbd-nav-move-to",e||a);Zi(this);c||
d||(c=v(function(a){K(a.target,"yt-dialog-base")&&aj(this)},this),this.f=V(F("yt-dialog-base",a),"click",c));
this.O(b,"overlay-shown");Q("yt-uix-overlay-shown",b)}}};
function Zi(a){a.j||(a.j=Qf("yt-uix-overlay-hide",bj));a.b&&Si(a.b,function(){var a=Yi.v();a.g=null;a.b.dispose();a.b=null})}
function aj(a){if(a.b){var b=a.g;a.b.dismiss("overlayhide");b&&a.O(b,"overlay-hidden");a.g=null;a.f&&(W(a.f),a.f=null);a.b=null}}
function $i(a,b){var c;if(a)if(c=F("yt-dialog",a)){var d=E("body-container");d&&(d.appendChild(c),a.overlayContentNode=c,c.overlayParentNode=a)}else c=a.overlayContentNode;else b&&(c=G(b,"yt-dialog"));return c}
function cj(){var a=Yi.v();if(a.g)a=F("yt-dialog-fg-content",a.g.overlayContentNode);else a:{if(a=cc("yt-dialog-fg-content"))for(var b=0;b<a.length;b++){var c=G(a[b],"yt-dialog");if(kh(c)){a=a[b];break a}}a=null}return a}
k.hide=function(a){a&&a.disabled||Q("yt-uix-overlay-hide")};
function bj(){aj(Yi.v())}
k.show=function(a){this.da(a)};var dj={},ej=[];function fj(a){a=G(a,"yt-uix-button-subscription-container");return F("yt-dialog",F("unsubscribe-confirmation-overlay-container",a))}
function gj(a,b){W(ej);ej.length=0;dj[b]||(dj[b]=fj(a));Yi.v().show(dj[b]);var c=cj();return new Re(function(a){ej.push(yg(c,function(){a()},"overlay-confirmation-unsubscribe-button"))})}
;function hj(){var a=O("PLAYER_CONFIG");return a&&a.args&&void 0!==a.args.authuser?!0:!(!O("SESSION_INDEX")&&!O("LOGGED_IN"))}
;function ij(){Eg.call(this,"subscription-button")}
z(ij,Eg);va(ij);ij.prototype.register=function(){Y(this,"click",this.ea);Gg(this,Vg,this.Da);Gg(this,Wg,this.Ca);Gg(this,Xg,this.xb);Gg(this,$g,this.Da);Gg(this,ah,this.Ca);Gg(this,bh,this.zb);Gg(this,dh,this.wb);Gg(this,eh,this.vb)};
ij.prototype.unregister=function(){Z(this,"click",this.ea);ij.w.unregister.call(this)};
ij.prototype.isSubscribed=function(a){return!!this.i(a,"is-subscribed")};
var jj={ga:"hover-enabled",Oa:"yt-uix-button-subscribe",Pa:"yt-uix-button-subscribed",Fb:"ypc-enabled",Ra:"yt-uix-button-subscription-container",Sa:"yt-subscription-button-disabled-mask-container"},kj={Gb:"channel-external-id",Ta:"subscriber-count-show-when-subscribed",Ua:"subscriber-count-tooltip",Va:"subscriber-count-title",Ib:"href",Jb:"insecure",ha:"is-subscribed",Kb:"parent-url",Lb:"clicktracking",Za:"show-unsub-confirm-dialog",Mb:"show-unsub-confirm-time-frame",ab:"style-type",ia:"subscribed-timestamp",
ja:"subscription-id",Nb:"target",bb:"ypc-enabled"};k=ij.prototype;k.ea=function(a){var b=this.i(a,"href"),c=this.i(a,"insecure");if(b)a=this.i(a,"target")||"_self",window.open(b,a);else if(!c)if(hj()){b=this.i(a,"channel-external-id");c=this.i(a,"clicktracking");var d=lj(this,a),e=this.i(a,"parent-url");if(this.i(a,"is-subscribed")){var f=this.i(a,"subscription-id"),g=new Rg(b,f,d,a,c,e);mj(this,a)?gj(a,b).then(function(){T(Zg,g)}):T(Zg,g)}else T(Ug,new Pg(b,d,c,e))}else nj(this,a)};
k.Da=function(a){this.N(a.b,this.Fa,!0)};
k.Ca=function(a){this.N(a.b,this.Fa,!1)};
k.xb=function(a){this.N(a.b,this.Ga,!0,a.f)};
k.zb=function(a){this.N(a.b,this.Ga,!1)};
k.wb=function(a){this.N(a.b,this.hb)};
k.vb=function(a){this.N(a.b,this.gb)};
k.Ga=function(a,b,c){b?(Uf(a,kj.ha,"true"),c&&Uf(a,kj.ja,c),this.i(a,kj.Za)&&(b=new Rd,Uf(a,kj.ia,(b.getTime()/1E3).toString()))):(Xf(a,kj.ha),Xf(a,kj.ia),Xf(a,kj.ja));oj(this,a)};
function lj(a,b){if(!a.i(b,"ypc-enabled"))return null;var c=a.i(b,"ypc-item-type"),d=a.i(b,"ypc-item-id");return{itemType:c,itemId:d,subscriptionElement:b}}
k.Fa=function(a,b){var c=G(a,jj.Ra);Xd(c,jj.Sa,b);a.setAttribute("aria-busy",b?"true":"false");a.disabled=b};
function oj(a,b){var c=a.i(b,kj.ab),d=!!a.i(b,"is-subscribed");c="-"+c;var e=jj.Pa+c;Xd(b,jj.Oa+c,!d);Xd(b,e,d);a.i(b,kj.Ua)&&!a.i(b,kj.Ta)&&(c=X(nh.v()),Xd(b,c,!d),b.title=d?"":a.i(b,kj.Va));d?P(function(){L(b,jj.ga)},1E3):M(b,jj.ga)}
k.hb=function(a){var b=!!this.i(a,"ypc-item-type"),c=!!this.i(a,"ypc-item-id");!this.i(a,"ypc-enabled")&&b&&c&&(L(a,"ypc-enabled"),Uf(a,kj.bb,"true"))};
k.gb=function(a){this.i(a,"ypc-enabled")&&(M(a,"ypc-enabled"),Xf(a,"ypc-enabled"))};
function pj(a,b){return La(cc(X(a)),function(a){return b==this.i(a,"channel-external-id")},a)}
k.eb=function(a,b,c){var d=Ua(arguments,2);A(a,function(a){b.apply(this,Qa(a,d))},this)};
k.N=function(a,b,c){var d=pj(this,a);this.eb.apply(this,Qa([d],Ua(arguments,1)))};
function nj(a,b){var c=v(function(a){a.discoverable_subscriptions&&Jf("SUBSCRIBE_EMBED_DISCOVERABLE_SUBSCRIPTIONS",a.discoverable_subscriptions);this.ea(b)},a);
vh(c)}
function mj(a,b){if(!a.i(b,"show-unsub-confirm-dialog"))return!1;var c=a.i(b,"show-unsub-confirm-time-frame");return"always"==c||"ten_minutes"==c&&(c=parseInt(a.i(b,"subscribed-timestamp"),10),(new Rd).getTime()<1E3*(c+600))?!0:!1}
;function qj(a){this.b=a;this.F=null;O("SUBSCRIBE_EMBED_HOVERCARD_URL")&&(rj(this),V(this.b,"mouseover",v(this.j,this)),V(this.b,"mouseout",v(this.X,this)),V(this.b,"click",v(this.X,this)),ig(Xg,Ga(this.f,!0),this),ig(bh,Ga(this.f,!1),this),sj(this))}
function rj(a){var b={url:O("SUBSCRIBE_EMBED_HOVERCARD_URL"),style:"bubble",hideClickDetection:!0,show:!1,anchor:a.b,relayOpen:"-1"};a=v(a.g,a);Lg().open(b,a)}
function sj(a){hj()||Qf("LOGGED_IN",function(){this.F&&(this.X(),this.F.close(),this.F=null,rj(this))},a)}
qj.prototype.g=function(a){this.F=a;a=ij.v().isSubscribed(this.b);this.f(a)};
qj.prototype.j=function(){this.F&&this.F.restyle({show:!0})};
qj.prototype.X=function(){this.F&&this.F.restyle({show:!1})};
qj.prototype.f=function(a){if(this.F){a={isSubscribed:a};try{this.F.send("msg-hovercard-subscription",a,void 0,u("gapi.iframes.SAME_ORIGIN_IFRAMES_FILTER"))}catch(b){}}};function tj(){Kg(function(){var a=De(E("yt-subscribe"));a={width:a.width,height:a.height};var b=uj;Lg().ready(a,null,b)})}
function uj(a){if(a.length&&a[a.length-1]){a=a[a.length-1].eurl;var b=E("yt-subscribe"),c=ij.v();if(b=F(X(c),b))a&&(ij.v(),Uf(b,"parent-url",a)),new qj(b)}}
;function vj(a){R.call(this,1,arguments);this.b=a}
z(vj,R);function wj(a,b){R.call(this,2,arguments);this.f=a;this.b=b}
z(wj,R);function xj(a,b,c,d){R.call(this,1,arguments);this.b=b;this.f=c||null;this.itemId=d||null}
z(xj,R);function yj(a,b){R.call(this,1,arguments);this.f=a;this.b=b||null}
z(yj,R);function zj(a){R.call(this,1,arguments)}
z(zj,R);var Aj=new S("ypc-core-load",vj),Bj=new S("ypc-guide-sync-success",wj),Cj=new S("ypc-purchase-success",xj),Dj=new S("ypc-subscription-cancel",zj),Ej=new S("ypc-subscription-cancel-success",yj),Fj=new S("ypc-init-subscription",zj);var Gj=!1,Hj=[];function Ij(a){a.b?Gj?T(Yg,a):T(Aj,new vj(function(){T(Fj,new zj(a.b))})):Jj(a.f,a.j,a.g,a.source)}
function Kj(a){a.b?Gj?T(ch,a):T(Aj,new vj(function(){T(Dj,new zj(a.b))})):Lj(a.f,a.l,a.j,a.g,a.source)}
function Mj(a){Nj(Ra(a.b))}
function Oj(a){Pj(Ra(a.b))}
function Qj(a){Rj(a.g,a.f,a.b)}
function Sj(a){var b=a.itemId,c=a.b.subscriptionId;b&&c&&T(Xg,new Qg(b,c,a.b.channelInfo))}
function Tj(a){var b=a.b;fb(a.f,function(a,d){T(Xg,new Qg(d,a,b[d]))})}
function Uj(a){T(bh,new Ng(a.f.itemId));a.b&&a.b.length&&(Vj(a.b,bh),Vj(a.b,dh))}
function Jj(a,b,c,d){var e=new Ng(a);T(Vg,e);var f={};f.c=a;c&&(f.eurl=c);d&&(f.source=d);c={};(d=O("PLAYBACK_ID"))&&(c.plid=d);(d=O("EVENT_ID"))&&(c.ei=d);b&&Wj(b,c);Eh("/subscription_ajax?action_create_subscription_to_channel=1",{method:"POST",Ia:f,M:c,onSuccess:function(b,c){var d=c.response;T(Xg,new Qg(a,d.id,d.channel_info));d.show_feed_privacy_dialog&&Q("SHOW-FEED-PRIVACY-SUBSCRIBE-DIALOG",a)},
ca:function(){T(Wg,e)}})}
function Lj(a,b,c,d,e){var f=new Ng(a);T($g,f);var g={};g.c=a;d&&(g.eurl=d);e&&(g.source=e);d={};d.c=a;d.s=b;(a=O("PLAYBACK_ID"))&&(d.plid=a);(a=O("EVENT_ID"))&&(d.ei=a);c&&Wj(c,d);Eh("/subscription_ajax?action_remove_subscriptions=1",{method:"POST",Ia:g,M:d,onSuccess:function(){T(bh,f)},
ca:function(){T(ah,f)}})}
function Rj(a,b,c){if(a){var d={};d.channel_id=a;switch(b){case "receive-all-updates":d.receive_all_updates=!0;break;case "receive-no-updates":d.receive_no_updates=!0;d.receive_post_updates=!1;break;case "receive-highlight-updates":d.receive_all_updates=!1;d.receive_no_updates=!1;break;default:return}null===c||d.receive_no_updates||(d.receive_post_updates=c);var e=new Og(a,b,c);Eh("/subscription_ajax?action_update_subscription_preferences=1",{method:"POST",M:d,onError:function(){T(hh,e)},
onSuccess:function(){T(gh,e)}})}}
function Nj(a){if(a.length){var b=Ta(a,0,40);T("subscription-batch-subscribe-loading");Vj(b,Vg);var c={};c.a=b.join(",");var d=function(){T("subscription-batch-subscribe-loaded");Vj(b,Wg)};
Eh("/subscription_ajax?action_create_subscription_to_all=1",{method:"POST",M:c,onSuccess:function(c,f){d();var e=f.response,h=e.id;if(xa(h)&&h.length==b.length){var l=e.channel_info_map;A(h,function(a,c){var d=b[c];T(Xg,new Qg(d,a,l[d]))});
a.length?Nj(a):T("subscription-batch-subscribe-finished")}},
onError:function(){d();T("subscription-batch-subscribe-failure")}})}}
function Pj(a){if(a.length){var b=Ta(a,0,40);T("subscription-batch-unsubscribe-loading");Vj(b,$g);var c={};c.c=b.join(",");var d=function(){T("subscription-batch-unsubscribe-loaded");Vj(b,ah)};
Eh("/subscription_ajax?action_remove_subscriptions=1",{method:"POST",M:c,onSuccess:function(){d();Vj(b,bh);a.length&&Pj(a)},
onError:function(){d()}})}}
function Vj(a,b){A(a,function(a){T(b,new Ng(a))})}
function Wj(a,b){var c=Jg(a),d;for(d in c)b[d]=c[d]}
;y("yt.setConfig",Jf);y("yt.config.set",Jf);y("ytbin.www.subscribeembed.init",function(){Gj=!0;Hj.push(ig(Ug,Ij),ig(Zg,Kj));Gj||Hj.push(ig(Yg,Ij),ig(ch,Kj),ig(Sg,Mj),ig(Tg,Oj),ig(fh,Qj),ig(Cj,Sj),ig(Ej,Uj),ig(Bj,Tj));var a=ij.v(),b=X(a);b in Ig||(a.register(),Fg(a,"yt-uix-init-"+b,a.init),Fg(a,"yt-uix-dispose-"+b,a.dispose),Ig[b]=a);tj()});}).call(this);
