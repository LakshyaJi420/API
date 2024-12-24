document.addEventListener("DOMContentLoaded", () => {
    const coinsDisplay = document.getElementById("coins");
    const dailyRewardBtn = document.getElementById("daily-reward");
    const menuBtns = document.querySelectorAll(".menu-btn");
    const sections = document.querySelectorAll("main section");
    const loadingScreen = document.getElementById("loading-screen");
    const app = document.getElementById("app");

    let coins = 0;
    let dailyRewardTimer = null;

    // Show app after loading
    setTimeout(() => {
        loadingScreen.classList.add("hidden");
        app.classList.remove("hidden");
    }, 2000);

    // Coin generation logic
    setInterval(() => {
        coins += 0.00001;
        coinsDisplay.textContent = coins.toFixed(6);
    }, 1000);

    // Daily reward logic
    dailyRewardBtn.addEventListener("click", () => {
        if (!dailyRewardTimer) {
            coins += 1;
            dailyRewardBtn.disabled = true;
            dailyRewardBtn.textContent = "Next reward in 24h";
            coinsDisplay.textContent = coins.toFixed(6);

            // Set timer for 24h
            dailyRewardTimer = setTimeout(() => {
                dailyRewardBtn.disabled = false;
                dailyRewardBtn.textContent = "Claim Daily Reward";
                dailyRewardTimer = null;
            }, 24 * 60 * 60 * 1000);
        }
    });

    // Menu navigation logic
    menuBtns.forEach((btn) => {
        btn.addEventListener("click", (e) => {
            const target = e.target.getAttribute("data-target");
            sections.forEach((section) => {
                section.classList.add("hidden");
            });
            document.getElementById(target).classList.remove("hidden");
        });
    });
});
