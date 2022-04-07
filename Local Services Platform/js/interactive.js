// CURRENT VALUES ARE PLACEHOLDERS
var accountType = 'provider'; //Default user: guest
var signedIn = true; //User signed in?
var username = 'Johnson Doe'; //Username
var userStarRate = 0; //Star rating given by customer

// Content for Provider Account
if (signedIn==true && accountType=='provider'){
    document.getElementById('uploadCertLicButton').style.display='block';
    document.getElementById('nameContactInfoHR').style.display='block';
    document.getElementById('providerContactInfoDiv').style.display='block';
    document.getElementById('uploadProfileButton').style.display='block';
    document.getElementById('submitProviderImageBtn').style.display='block';
    document.getElementById('submitCertOrLicBtn').style.display='block';
    //Editing Contact Information
    document.getElementById('saveChangesBtn').style.display='block';
    document.getElementById('phoneNumber').contentEditable=true;
    document.getElementById('phoneNumber').addEventListener('click', function(){
        var element = document.getElementById('phoneNumber');
        element.style.backgroundColor= '#0d6efd';
        element.style.color='#fff';
        //Exits edit focus when pressing 'Enter'
        element.addEventListener('keydown', (evt) => {
            if (evt.key === 'Enter') {
                evt.preventDefault();
                element.blur();
                element.style.backgroundColor= '';
                element.style.color='';
            }
        });
        //Exits edit focus when clicking outside html element
        document.addEventListener('click', function(e){
            var isClickedInside = element.contains(e.target);
            if(!isClickedInside){
                element.blur();
                element.style.backgroundColor= '';
                element.style.color='';
            }
        });
    })
    document.getElementById('email').contentEditable=true;
    document.getElementById('email').addEventListener('click', function(){
        var element = document.getElementById('email');
        element.style.backgroundColor= '#0d6efd';
        element.style.color='#fff';
        //Exits edit focus when pressing 'Enter'
        element.addEventListener('keydown', (evt) => {
            if (evt.key === 'Enter') {
                evt.preventDefault();
                element.blur();
                element.style.backgroundColor= '';
                element.style.color='';
            }
        });
        //Exits edit focus when clicking outside html element
        document.addEventListener('click', function(e){
            var isClickedInside = element.contains(e.target);
            if(!isClickedInside){
                element.blur();
                element.style.backgroundColor= '';
                element.style.color='';
            }
        });
    });
}

// Content for Customer Account
if (signedIn==true && accountType=='customer'){
    document.getElementById('nameContactInfoHR').style.display='block';
    document.getElementById('providerContactInfoDiv').style.display='block';
    document.getElementById('customerFeedback').style.display='block';
}

// Changes page contents once signed in
if(signedIn==true && (accountType=='customer' || accountType=='provider')){
    document.getElementById('signInBtn').style.display='none';
    document.getElementById('signOutBtn').style.display='block';
    document.getElementById('registerBtn').innerHTML = truncate(username,5);
    document.getElementById('registerModalHeader').innerHTML = 'Account Information';
    document.getElementById('registerBtnFooter').innerHTML = 'Save Changes';
    document.getElementById('firstNameRegister').placeholder = 'Enter New Username';
    document.getElementById('emailAddressRegister').placeholder = 'Enter New Email';
    document.getElementById('passwordRegister').placeholder = 'Enter New Password';
    document.getElementById('userLocationRegister').placeholder = 'Enter New Town';
    document.getElementById('selectAccountLabel').innerHTML = 'Change Account Type';
}

// Cuts string if length above limit, and adds '...'
function truncate(string, limit) {
    if (string.length > limit) {
      return string.substring(0, limit) + "..."
    } else {
      return string
    }
  }

// Gets star value from user rating. 
function getStarValue(id){
    userStarRate = document.getElementById(id).value;
    // console.log(userStarRate); //Debug
}
