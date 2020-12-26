// login page
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function userlogin() {
  const email=document.getElementById("email-login").value;
  const password=document.getElementById("password-login").value;
  const data={email,password};
    const url = "http://127.0.0.1:8000/api/login";
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body:JSON.stringify(data), 
  })
  // Converting to JSON 
  .then(response => response.json()) 
  // Displaying results to console 
  .then(json => console.log(json),
  // function(json){
  // if(response >=200 && response<400)
  //   {
  // window.location.replace("http://127.0.0.1:5500/index.html");
  // }
  // else
  // {
  //   window.alert("error");
  // }
  )
  .catch(err => console.log('Request Failed', err));
  }
  // const myform=document.getElementById("myFormsignup")
  function usersignup() {
    // e.preventDefault();
    const formData=new formData(this);
    const email=document.getElementById("signup-email").value;
    const password=document.getElementById("signup-password").value;
    const username=document.getElementById("signup-user").value;
    const data={email,password,username};
      const url = "http://127.0.0.1:8000/api/login";
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body:JSON.stringify(data), 
      } )
    
    // Converting to JSON 
    .then(response => response.json()) 
    
    // Displaying results to console 
    .then(json => console.log(json),
    // window.location.replace("http://127.0.0.1:5500/index.html")
    )
    .catch(err => console.log('Request Failed', err));
    }