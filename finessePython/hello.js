// Executing python scripts from Node Js Tutorial: https://www.youtube.com/watch?v=aoMzOgiE7rY

const { spawn } = require('child_process');

// const childPython = spawn('python3', ['--version']);
const childPython = spawn('python3', ['main.py']);
// const childPython = spawn('python3', ['main.py', 'test']);
let text = ""
childPython.stdout.on('data', (data) => {
    // text = `${data}`;
    console.log(`stdout: ${data}`);
    // console.log("TESTING:");
    // console.log(text);
});

childPython.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
});

childPython.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});