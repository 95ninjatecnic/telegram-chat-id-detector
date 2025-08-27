import { runBanner } from './banner.js';
import { spawn } from 'child_process';

// =========================
// Run Banner
// =========================
runBanner({
    callback: () => {
        // =========================
        // Run Python bot in same terminal
        // =========================
        const pythonProcess = spawn("python", ["chat_id.py"], {
            stdio: "inherit", // terminal output show করবে
            shell: true
        });

        pythonProcess.on("close", (code) => {
            console.log(`Python bot exited with code ${code}`);
        });
    }
});
