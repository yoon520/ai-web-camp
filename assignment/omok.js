// 입력 모듈 불러오기
const readline = require('readline');
// 인터페이스 생성
const rl = readline.createInterface({
	input: process.stdin,
    output: process.stdout
});

// 오목판 만들기
let board = new Array(32);
for (var i = 0; i < 32; i++) {
    board[i] = new Array(32);
    for (var j = 0; j < 32; j++) {
        if (i === 0 || i === 31 ) {
            board[i][j] = '-';
        } else if (j === 0 || j === 31) {
            board[i][j] = '|';
        } else {
            board[i][j] = '+';
        }
    }
}

// 오목판 출력 함수
let printBoard = function() {
    for (var i = 0; i < 32; i++) {
        console.log(board[i].join(' '));
    }
}

// player 승리 확인 함수
let checkWin = function(x, y, player) {
    // 이동방향 정의 | ㅡ \ /
    let moveX = [1, 0, 1, 1];
    let moveY = [0, 1, 1, -1];

    // flag = 1이면 승리
    let flag, nowX, nowY;

    // 시작 좌표가 player와 다르면 함수 종료
    if (board[x][y] !== player) {
        return 0;
    }

    // 각 이동 방향 별 오목 체크
    for (var i = 0; i < 4; i++) {
        flag = 1;
        [nowX, nowY] = [x, y];

        for (var j = 0; j < 4; j++) {
            nowX = nowX + moveX[i];
            nowY = nowY + moveY[i];
            if (board[nowX][nowY] !== player) {
                flag = 0;
                break;
            }
        }

        // player가 승리했다면
        if (flag) {
            console.log("Game over");
            if (player) {
                console.log("흑 승리");
            } else {
                console.log("백 승리");
            }
            return flag;
        }
        
    }
    return 0;
}

// 플레이어 설정 1은 흑, 0은 백
let player = 1;
// 플레이어가 선언할 좌표값
let px, py;

// 5분 후 프로그램 종료
setTimeout(() => { process.exit(0); }, 600000);

if (player === 1) {
    process.stdout.write("흑돌 차례: ")
} else {
    process.stdout.write("백돌 차례: ")
}

// 입력 받기
rl.on("line", (line) => {
    // 입력 받은 좌표 바둑판에 체크
    [px, py] = line.slice(1,-1).split(",").map((element)=>parseInt(element));
    board[px][py] = player;

    printBoard();

    // 승리했는지 판정하기
    for (var x = 1; x < 31; x++){
        for (var y = 1; y < 31; y++) {
            if (checkWin(x, y, player)) {
                rl.close();
            }
        }
    }
    
    player = (player + 1) % 2
    
    if (player === 1) {
        process.stdout.write("흑돌 차례: ")
    } else {
        process.stdout.write("백돌 차례: ")
    }
}).on("close", () => {
    // 인터페이스 종료와 함께 프로그램 종료
    process.exit();
});