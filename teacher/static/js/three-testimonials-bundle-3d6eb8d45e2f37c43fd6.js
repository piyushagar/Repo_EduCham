!function(e){var t={};function r(i){if(t[i])return t[i].exports;var n=t[i]={i:i,l:!1,exports:{}};return e[i].call(n.exports,n,n.exports,r),n.l=!0,n.exports}r.m=e,r.c=t,r.d=function(e,t,i){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:i})},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var i=Object.create(null);if(r.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)r.d(i,n,function(t){return e[t]}.bind(null,n));return i},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/assets/",r(r.s=873)}({873:function(e,t){$(document).ready((function(){r.initialize()}));var r={initialize:function(){$(".three-testimonials .profile-images img").click(r.clickProfileImage)},clickProfileImage:function(e){var t=e.target.dataset.id,r=$(".three-testimonials img");r.removeClass("active"),r[t].classList.add("active");var i=$(".three-testimonials blockquote");i.removeClass("active"),i[t].classList.add("active");var n=$(".three-testimonials cite");n.removeClass("active"),n[t].classList.add("active")}}}});
//# sourceMappingURL=three-testimonials-bundle-3d6eb8d45e2f37c43fd6.js.map