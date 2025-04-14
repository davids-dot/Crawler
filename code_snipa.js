// 过debug
const original_constructor = Function.prototype.constructor
Function.prototype.constructor = function(a) {
   if (x!="debugger") {
     return original_constructor(a)
   }
    return function() {}
}


// 清除所有代码注释
(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/|[ \t]*//.*)

// 清除块注释
 (/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)

// 清除行注释
([ \t]*//.*)
