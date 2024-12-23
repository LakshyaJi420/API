let coins = 0;
let level = 1;
let carsOwned = ["Damaged Car"];
let currentCar = "Damaged Car";
let dailyReward = 1;
let progress = 0;
let lastClaimTime = localStorage.getItem("lastClaimTime") || Date.now();
let dailyRewardCooldown = 86400000; // 24 hours in ms
let carIncomeRate = 0.000010; // Default income rate per second
let lastCarIncomeTime = Date.now();

// Cars Data (showroom cars) with PNG images
const showroomCars = [
    { name: "Toyota Supra", price: 100, speed: 250, performance: 85, image: "images/toyota_supra.png" },
    { name: "Tesla Model S", price: 150, speed: 220, performance: 90, image: "images/tesla_model_s.png" },
    { name: "Tata Nexon", price: 50, speed: 150, performance: 70, image: "images/tata_nexon.png" },
    { name: "Mahindra XUV700", price: 120, speed: 200, performance: 80, image: "images/mahindra_xuv700.png" },
    { name: "Land Rover Defender", price: 180, speed: 210, performance: 95, image: "images/land_rover_defender.png" },
    { name: "Tata Nano", price: 500, speed: 65, performance: 50, image: "images/tata_nano.png" },
    { name: "Maruti Alto", price: 25, speed: 80, performance: 60, image: "images/maruti_alto.png" }
];

// Update username from Telegram
document.getElementById("username").innerText = `Welcome, ${getTelegramUsername()}`;
document.getElementById("coins").innerText = coins.toFixed(6);

// Coin generation function
function generateCoins() {
    let currentTime = Date.now();
    let elapsedTime = (currentTime - lastCarIncomeTime) / 1000; // Time in seconds
    coins += carIncomeRate * elapsedTime;
    lastCarIncomeTime = currentTime;
    updateDisplay();
}

// Update display elements
function updateDisplay() {
    document.getElementById("coins").innerText = coins.toFixed(6);
    document.getElementById("level").innerText = level;
}

// Earn coins by tapping the car
function earnCoins() {
    coins += 0.0003;
    progress += 1; // Increase progress for leveling
    updateDisplay();
    checkLevelUp();
}

// Level up system
function checkLevelUp() {
    if (level < 3 && progress >= 100) {
        level += 1;
        progress = 0; // Reset progress for next level
        if (level === 3) {
            document.getElementById("showroom-btn").disabled = false;
            alert("You unlocked the Showroom!");
        }
    }
}

// Daily reward system
function claimDailyReward() {
    if (Date.now() - lastClaimTime >= dailyRewardCooldown) {
        coins += dailyReward;
        dailyReward *= 2;
        lastClaimTime = Date.now();
        localStorage.setItem("lastClaimTime", lastClaimTime);
        updateDailyRewardButton();
        alert(`You claimed ${dailyReward / 2}!`);
        updateDisplay();
    } else {
        alert("You have to wait 24 hours for your next reward.");
    }
}

// Display countdown for daily reward
function updateDailyRewardButton() {
    let timeRemaining = lastClaimTime + dailyRewardCooldown - Date.now();
    let button = document.getElementById("daily-reward-btn");

    if (timeRemaining <= 0) {
        button.disabled = false;
        button.innerText = "Claim Daily Reward";
    } else {
        button.disabled = true;
        button.innerText = `Next Reward in: ${formatTime(timeRemaining)}`;
        setTimeout(updateDailyRewardButton, 1000);
    }
}

function formatTime(ms) {
    let seconds = Math.floor(ms / 1000);
    let minutes = Math.floor(seconds / 60);
    let hours = Math.floor(minutes / 60);
    let days = Math.floor(hours / 24);
    return `${days}d ${hours % 24}h ${minutes % 60}m ${seconds % 60}s`;
}

// Show profile
function showProfile() {
    let profileContent = `
        <h2>Your Profile</h2>
        <p><strong>Level:</strong> ${level}</p>
        <p><strong>Coins:</strong> ${coins.toFixed(6)}</p>
        <p><strong>Cars Owned:</strong> ${carsOwned.join(", ")}</p>
    `;
    document.getElementById("dynamic-content").innerHTML = profileContent;
}

// Show garage
function showGarage() {
    let garageContent = `
        <h2>Your Garage</h2>
        ${carsOwned.map(car => `<p>${car}</p>`).join("")}
    `;
    document.getElementById("dynamic-content").innerHTML = garageContent;
}

// Show leaderboard (real players from Telegram)
function showLeaderboard() {
    // Mock data for now. Replace this with actual data fetching from your backend.
    let leaderboard = [
        { username: "Player1", coins: 500 },
        { username: "Player2", coins: 400 },
        { username: "Player3", coins: 300 },
        { username: "You", coins: coins.toFixed(6) }
    ];
    
    let leaderboardContent = `
        <h2>Leaderboard</h2>
        ${leaderboard.map(player => `
            <p>${player.username} - ${player.coins}</p>
        `).join("")}
    `;
    document.getElementById("dynamic-content").innerHTML = leaderboardContent;
}

// Show showroom (available at level 1)
function showShowroom() {
    let showroomContent = `
        <h2>Showroom</h2>
        ${showroomCars.map(car => `
            <div class="showroom-item" onclick="buyCar('${car.name}')">
                <img src="${car.image}" alt="${car.name}" />
                <p>${car.name}</p>
                <p>Price: ${car.price}</p>
                <p>Speed: ${car.speed} km/h</p>
                <p>Performance: ${car.performance}%</p>
            </div>
        `).join("")}
    `;
    document.getElementById("dynamic-content").innerHTML = showroomContent;
}

// Buy a car
function buyCar(carName) {
    let car = showroomCars.find(c => c.name === carName);
    if (coins >= car.price) {
        coins -= car.price;
        carsOwned.push(carName);
        updateDisplay();
        alert(`${carName} bought!`);
    } else {
        alert("You don't have enough coins.");
    }
}

// Get user's Telegram username (mocked for now)
function getTelegramUsername() {
    return "Player";
}

// Initial setup
updateDailyRewardButton();
setInterval(generateCoins, 1000); // Increase coins every second
