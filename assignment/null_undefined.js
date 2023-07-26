let a;
let b = null;
let obj = {name: null};

console.log(a);         // undefined
console.log(b);         // null
console.log(obj.age);   // undefined
console.log(obj.name);  // null

/* 
a는 변수로 선언되었지만 아직 초기화되지 않아 undefined이다.
b는 값을 null로 지정해 의도적으로 값이 없다는 것을 나타낸 것이기 때문에 null이다.
obj.age는 obj 객체의 프로퍼티로 지정되어 있지 않아 존재하지 않는 값에 접근했기 때문에 undefined이다.
obj.name의 프로퍼티 값은 null로 빈 값을 지정한 상태이므로 null이다.
*/

console.log(typeof a);          // undefined
console.log(typeof b);          // object
console.log(typeof obj.age);    // undefined
console.log(typeof obj.name);   // object
console.log(typeof null);       // object
console.log(typeof undefined);  //undefined

/*
null과 undefined 모두 원시타입이지만 typeof로 null의 타입을 검사했을 때 object를 반환한다.
이는 자바스크립트 초기 버전의 버그이며 고칠 수 없는 버그이다. 
typeof에 null인지 검사하는 부분이 없어 생기는 버그라고 한다.
출처: https://2ality.com/2013/10/typeof-null.html
*/

console.log(a == null);         // true
console.log(a == undefined);    // true
console.log(a === null);        // false
console.log(a === undefined);   // true
console.log(b == null);         // true
console.log(b == undefined);    // true
console.log(b === null);        // true
console.log(b === undefined);   // false
console.log(obj.age == null);   // true
console.log(obj.age === null);  // false

/* 
'==' 연산자는 강제로 피연산자를 같은 형으로 변환시켜 변환된 값이 같으면 true를 반환한다. null과 undefined는 true를 반환한다.
'===' 연산자는 값과 자료형까지 같아야 true를 반환한다.
null인지 체크하려면 '==='를 사용해야 한다.
*/