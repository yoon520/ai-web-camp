/*
- null은 리터럴 값으로 변수를 선언해 빈 값을 할당한 상태이다. 
아직 '값'이 정해지지 않았다는 것을 뜻한다.
- undefined는 변수를 선언했지만 값을 할당하지 않았거나 존재하지 않는 값에 접근할 때 반환된다.
아직 '타입(자료형)'이 정해지지 않았다는 것을 뜻한다.
*/

let a;
let b = null;
let obj = {name: null};
arr = [1,2,3]
function add(num1, num2) { num1 + num2 }
function f(x, y) {console.log(x, y)}

console.log(a);         // undefined
console.log(b);         // null
console.log(obj.age);   // undefined
console.log(obj.name);  // null
console.log(arr[3])     // undefined
console.log(add(1, 2))  // undefined
f(1);                   // 1 undefined

/* 
a는 변수로 선언되었지만 아직 초기화되지 않아 undefined이다.
b는 값을 null로 지정해 의도적으로 값이 없다는 것을 나타낸 것이기 때문에 null이다.
age는 obj 객체의 프로퍼티로 존재하지 않는 값이기 때문에 undefined이다.
obj.name의 프로퍼티 값은 null로 빈 값을 지정한 상태이므로 null이다.
배열의 범위에 존재하지 않는 값으로 undefined이다.
add함수에 리턴값이 존재하지 않아 undefined이다.
f함수에 매개변수 b의 값이 존재하지 않아 undefined이다.
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