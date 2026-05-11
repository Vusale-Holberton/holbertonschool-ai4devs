function processUserData(user) {
    let greeting = "Hello, " + user.name;
    let ageInTenYears = user.age + 10;
    let bioLength = user.profile?.bio?.length || 0; 
    
    console.log(greeting);
    console.log("Age in 10 years: " + ageInTenYears);
    console.log("Bio length: " + bioLength);
}

let currentUser = { name: "Vusala", age: 20 };
processUserData(currentUser);