!function(e){var t={};function r(n){if(t[n])return t[n].exports;var o=t[n]={i:n,l:!1,exports:{}};return e[n].call(o.exports,o,o.exports,r),o.l=!0,o.exports}r.m=e,r.c=t,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)r.d(n,o,function(t){return e[t]}.bind(null,o));return n},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/assets/",r(r.s=817)}({817:function(e,t){$(document).ready((function(){r.initialize()}));var r={initialize:function(){$blogNav=$("section.blog-nav-menu"),$blogNav.find("input.search-bar").on("search",r.redirectSearch),$blogNav.find("form.search-container-form").on("submit",(function(e){e.preventDefault()})),$blogSubNav=$("section.blog-sub-nav"),$blogSubNav.find("input.search-bar").on("search",r.redirectSearch),$blogSubNav.find("form.search-container-form").on("submit",(function(e){e.preventDefault()}))},redirectSearch:function(e){Tracking.irisEmit("searched_blog_posts",{search_value:e.currentTarget.value}),window.location.href="https://www.google.com/search?q=site:https://teachable.com/blog%20"+e.currentTarget.value}}}});
//# sourceMappingURL=blog-nav-bundle-3d6eb8d45e2f37c43fd6.js.map