// import express from 'express';
// const app=express();
// import details from "./details.mjs";

// app.use('/details',details);
//  const port= +process.env.PORT || 8000;
//  app.listen(port,() => {
//     console.log(`Server is running at ${port}`);
    
//  })

// server.mjs
// server.mjs
// server.mjs
// server.mjs
// server.mjs
// import express from 'express';
// import fs from 'fs';

// const app = express();
// const PORT = 8000;
// const JSON_FILE_PATH = 'userData.json';

// // Middleware to parse JSON bodies
// app.use(express.json());

// // Define a route to handle POST requests from your React app
// app.post('/details', (req, res) => {
//   try {
//     const newData = req.body;

//     // Write the new data to the JSON file
//     fs.writeFile(JSON_FILE_PATH, JSON.stringify(newData, null, 2), (err) => {
//       if (err) {
//         console.error('Error writing to file:', err);
//         res.status(500).send('Error writing to file');
//       } else {
//         console.log('Data replaced and saved to submittedData.json');
//         // Send success response after writing to the file
//         res.status(200).send('Data replaced and saved successfully');
//       }
//     });
//   } catch (error) {
//     console.error('Error:', error);
//     res.status(500).send('Internal server error');
//   }
// });

// // Start the server
// app.listen(PORT, () => {
//   console.log(`Server is running on http://localhost:${PORT}`);
// });

import express from 'express';
import fs from 'fs';
import { spawn } from 'child_process';
import cors from 'cors'; 


const app = express();
const PORT = 8000;
const JSON_FILE_PATH = 'userData.json';
const PYTHON_SCRIPT_PATH = 'C:/user-datasubmission-react/frontend/src/app.py';

app.use(cors());
// Middleware to parse JSON bodies
app.use(express.json());

// Define a route to handle both POST and GET requests
app.post('/details', (req, res) => {
  try {
    const newData = req.body;

    // Write the new data to the JSON file
    fs.writeFile(JSON_FILE_PATH, JSON.stringify(newData, null, 2), (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        res.status(500).send('Error writing to file');
      } else {
        console.log('Data replaced and saved to userData.json');
        res.status(200).send('Data replaced and saved successfully');
      }
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal server error');
  }
});

// Define a route to execute Python script
  app.get('/execute', (req, res) => {
    try {
      // Execute the Python script
      const pythonProcess = spawn('python', ['C:/user-datasubmission-react/frontend/src/app.py']);
  
      // Handle script execution events
      pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
      });
  
      pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
      });
  
      pythonProcess.on('close', (code) => {
        console.log(`Python script exited with code ${code}`);
        res.status(200).send('Python script executed successfully');
      });
    } catch (error) {
      console.error('Error executing Python script:', error);
      res.status(500).send('Internal server error');
    }
  });
  
  // Start the server
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });