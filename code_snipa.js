const original_constructor = Function.prototype.constructor
Function.prototype.constructor = function(a) {
   if (x!="debugger") {
     return original_constructor(a)
   }
    return function() {}
}
