// import { useState } from 'react';

// function App() {
//   const [formData, setFormData] = useState({
//     ID: '',
//     AccountID: ''
//   });

//   const handleInputChange = (e) => {
//     const { name, value } = e.target;
//     setFormData({ ...formData, [name]: value });
//   };

//   const onSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       const response = await fetch('/details', {
//         method: "POST",
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(formData)
//       });
      
//       if (response.ok) {
//         console.log("data posted")
//         alert("Data submitted successfully!");
//       } else {
//         console.error("Something went wrong");
//       }
//     } catch (error) {
//       console.error("Error:", error.message);
//     }
//   };
  
//   return (
//     <div className="App">
//       <form onSubmit={onSubmit}>
//         ID<input type="text" name="ID" value={formData.ID} onChange={handleInputChange} />
//         <br></br>
//         AccountID <input type="email" name="AccountID" value={formData.AccountID} onChange={handleInputChange} />
//         <br></br>
//         <input type="submit" value="ADD" />
//       </form>
//     </div>
//   );
// }

// export default App;

// import React, { useState } from 'react';

// function App() {
//   const [formData, setFormData] = useState({
//     ID: '',
//     AccountID: ''
//   });

//   const handleInputChange = (e) => {
//     const { name, value } = e.target;
//     setFormData({ ...formData, [name]: value });
//   };

//   const onSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       const response = await fetch('/details', {
//         method: "POST",
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(formData)
//       });

//       if (response.ok) {
//         console.log("Data submitted successfully!");
//       } else {
//         console.error("Something went wrong");
//       }
//     } catch (error) {
//       console.error("Error:", error.message);
//     }
//   };

//   const executeRequest = async () => {
//     try {
//       const response = await fetch('http://localhost:8000/execute',{
//       method: "GET"
//     });
//       if (response.ok) {
//         const data = await response.json();
//         console.log(data);
//       } else {
//         throw new Error('Network response was not ok');
//       }
//     } catch (error) {
//       console.error('Fetch Error:', error);
//     }
//   };

//   return (
//     <div className="App">
//       <form onSubmit={onSubmit}>
//         ID<input type="text" name="ID" value={formData.ID} onChange={handleInputChange} />
//         <br></br>
//         AccountID <input type="email" name="AccountID" value={formData.AccountID} onChange={handleInputChange} />
//         <br></br>
//         <input type="submit" value="ADD" />
//       </form>
//       <button onClick={executeRequest}>Post</button>
//     </div>
//   );
// }

// export default App;

import { useState } from 'react';
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    ID: '',
    AccountID: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const onSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/details', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      
      if (response.ok) {
        console.log("Data posted successfully");
        alert("Login details Added successfully!");
      } else {
        console.error("Something went wrong");
      }
      
      
    } catch (error) {
      console.error("Error:", error.message);
    }
  };

  const executePythonScript = async () => {
    try {
      const response = await fetch('/execute');
      if (response.ok) {
        console.log("Python script executed successfully");
        alert("Account Updated Successfully");
      } else {
        console.error("Error executing Python script");
      }
    } catch (error) {
      console.error("Error:", error.message);
    }
  };

  // function alert(){
  //   alert("Account Updated Successfully");
  // }
  
  return (
    <div className="auth-form-container">
      
      <form onSubmit={onSubmit} className="login-form">
        <caption><b>OperatorPortal Services</b></caption>
      <label htmlFor="ID"><b>ID</b></label>
        <input type="text" name="ID" value={formData.ID} onChange={handleInputChange} />
        <br></br><br></br>
        <label htmlFor="AccountID"><b>AccountID</b></label>
        <input type="text" name="AccountID" value={formData.AccountID} onChange={handleInputChange} />

        <br></br><br></br>
        {/* <label htmlFor="Add Account">AccountID</label> */}
        <button type="submit">Add Login</button>
        {/* <label htmlFor="Add Account">Update Account</label> */}
      <button type ="button" onClick={executePythonScript}>Update Account</button>
      </form>
    </div>
  );
}

export default App;


