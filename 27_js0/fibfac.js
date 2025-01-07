//Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>

var fact = function(n){
    if (n==1){
        return n;
    }
    else return (n * fact(n-1));
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

fact(4)
fact(5)

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

var fib = function(n){
    if (n==0){
        return 0;
    }
    if (n==1){
        return 1;
    }
    else return (fib(n-1) + fib(n-2));
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

fib(4)
fib(5)

//=================================================================

