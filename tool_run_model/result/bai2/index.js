function readStdin() {
    let input = "";
 
    return new Promise((resolve) => {
        process.stdin.on("data", (data) => {
            input += data;
        });
        process.stdin.on("end", () => {
            resolve(input);
        });
    });
}
 
function sum(n) {
    return n + 25;
}
 
async function main() {
    process.stdin.resume();
    process.stdin.setEncoding("utf8");
 
    const input = await readStdin();
    const n = parseInt(input);
    console.log(sum(n));
}
 
main();