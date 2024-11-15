const { app, BrowserWindow } = require('electron');
const path = require('path');
const { exec } = require('child_process');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: true,
            contextIsolation: false,
        },
    });

    win.loadURL('http://127.0.0.1:5000');
}

app.whenReady().then(() => {
    // Start the Flask server
    exec('python ../path/to/your/app.py', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error starting Flask server: ${err}`);
            return;
        }
        console.log(`Flask server stdout: ${stdout}`);
        console.error(`Flask server stderr: ${stderr}`);
    });

    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});