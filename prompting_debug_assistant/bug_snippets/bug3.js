function updateProfile(user) {
    console.log("Updating...");
    
    let displayName = user.firstName + " " + user.lastName;
    let birthYear = 2026 - user.age;
    
    let info = user.settings.theme.color;
    
    console.log("Name: " + displayName);
    console.log("Born: " + birthYear);
    console.log("Theme: " + info);
}

let profileData = {
    firstName: "Vusala",
    age: 20
};

updateProfile(profileData);