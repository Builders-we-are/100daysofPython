const { MongoClient, GridFSBucket } = require('mongodb');
const express = require('express');
const app = express();
const port = 3000;

const mongoUri = 'mongodb://localhost:27017'; // Replace with your MongoDB connection URI
const dbName = 'your-database-name'; // Replace with your database name
const filenameToRetrieve = 'your-filename'; // Replace with the actual filename

// Initialize MongoDB client
const client = new MongoClient(mongoUri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Connect to the MongoDB server
client.connect(async (err) => {
  if (err) {
    console.error('MongoDB connection error:', err);
    process.exit(1);
  }

  const db = client.db(dbName);

  // Create a GridFSBucket instance
  const gridFSBucket = new GridFSBucket(db);

  // Find the file by filename
  const file = await db.collection('fs.files').findOne({ filename: filenameToRetrieve });

  if (!file) {
    console.error('File not found');
    return;
  }

  // Open a download stream for the file
  const downloadStream = gridFSBucket.openDownloadStreamByName(filenameToRetrieve);

  // Handle data events
  downloadStream.on('data', (chunk) => {
    // Handle the chunk of data
    console.log(`Received ${chunk.length} bytes of data.`);
  });

  // Handle end event
  downloadStream.on('end', () => {
    console.log('Download stream ended.');
    // You have received the entire file.
  });

  // Handle errors
  downloadStream.on('error', (error) => {
    console.error('Error downloading file:', error);
  });

  // ... Rest of your code ...

  app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
});
