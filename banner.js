// banner.js
import CFonts from 'cfonts';
import chalk from 'chalk';
import gradient from 'gradient-string';
import ora from 'ora';

/**
 * Banner Options
 * @param {Object} options
 *   - title: Main banner title (string)
 *   - dynamicLines: Array of strings to show dynamically
 *   - spinnerMessage: Spinner text
 *   - spinnerColor: Spinner color
 *   - legalText: Legal / disclaimer text
 *   - lineDelay: Delay between dynamic lines (ms)
 *   - callback: Function to run after banner finished
 */
export function runBanner({
    title = '🚀 Ninja Dora Ultimate 🚀',
    dynamicLines = [
        '⚡ Ninja Dora Ultimate ⚡',
        '🔥 Advanced CLI Operations 🔥',
        '💻 Node.js Powered CLI 💻'
    ],
    spinnerMessage = 'Initializing engines...',
    spinnerColor = 'magenta',
    legalText = `
⚠️ LEGAL & EDUCATIONAL PURPOSE ONLY ⚠️
🚨 Do NOT use for illegal activities 🚨
📚 For learning & testing only
💡 Contact: Tamim Ikbal (Owner of Ninjatecnic Ti)
💻 GitHub: https://github.com/95ninjatecnic
📱 Telegram: https://t.me/ninjatecnic_ti

❌ DISCLAIMER:
The owner is NOT responsible for any misuse or illegal activity performed
using this software. All actions are solely the responsibility of the user.
`,
    lineDelay = 600,
    callback = null
} = {}) {
    console.clear();
    console.log(chalk.cyan.bold(title));

    // Big ASCII style title
    CFonts.say('Ninja Tecnic', {
        font: 'block',
        align: 'center',
        colors: ['cyan', 'yellowBright'],
        background: 'black',
        letterSpacing: 1,
        lineHeight: 1,
        space: true,
        maxLength: '0',
    });

    console.log(gradient.rainbow('💥 Advanced CLI Banner Activated 💥\n'));
    console.log(chalk.yellow(legalText));

    const spinner = ora({
        text: spinnerMessage,
        spinner: 'dots',
        color: spinnerColor
    }).start();

    dynamicLines.forEach((line, index) => {
        setTimeout(() => {
            process.stdout.write(gradient.pastel(line) + '\n');
        }, lineDelay * (index + 1));
    });

    setTimeout(() => {
        spinner.succeed(chalk.green('✔ Engines successfully started! 🚀\n'));
        if (callback) callback();
    }, 2500 + dynamicLines.length * lineDelay);
}
