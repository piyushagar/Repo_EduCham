!function(e){var t={};function n(o){if(t[o])return t[o].exports;var i=t[o]={i:o,l:!1,exports:{}};return e[o].call(i.exports,i,i.exports,n),i.l=!0,i.exports}n.m=e,n.c=t,n.d=function(e,t,o){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var i in e)n.d(o,i,function(t){return e[t]}.bind(null,i));return o},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/assets/",n(n.s=347)}({347:function(e,t){$(document).ready((function(){n.initialize()}));var n={initialize:function(){$(".image-text-column-wide .play-button").on("click",n.clickPlayButton),$(".image-text-column-wide a").on("click",n.clickPlayButton)},clickPlayButton:function(e){e.preventDefault(),n.showVideo(e),location.href="#top-of-video",n.playVideo()},showVideo:function(e){$(".image-text-column-wide .video-container").show(),"circle"===e.target.tagName?e.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.classList.add("video-open"):e.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.classList.add("video-open")},playVideo:function(){var e=$("#top-of-video")[0].dataset.wistiaid;window._wq=window._wq||[],_wq.push({id:e,onReady:function(e){e.play(),Tracking.irisEmit("marketing_played_video",{target:"segment"})}})}}}});
//# sourceMappingURL=video-bundle-3d6eb8d45e2f37c43fd6.js.map