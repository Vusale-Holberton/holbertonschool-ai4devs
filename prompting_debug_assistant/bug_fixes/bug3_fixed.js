function updateProfile(user) {
    let firstName = user.firstName || "Anonymous";
    let lastName = user.lastName || "User";
    let displayName = firstName + " " + lastName;
    
    let info = user.settings?.theme?.color || "default-blue";
    
    console.log("Starting profile update...");
    console.log("Name: " + displayName);
    console.log("Theme Color: " + info);
    console.log("Profile update successful.");
}

let profileData = { 
    firstName: "Vusala", 
    age: 20 
};

updateProfile(profileData);