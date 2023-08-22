print('Hello, World!')
const express = require('express');
const app = express();
const port = 3000;
const mongoose = require('mongoose');
const { GridFSBucket } = require('mongodb');
const fs = require('fs');
const path = require('path');

// Replace with your actual MongoDB connection string
mongoose.connect('mongodb://localhost:27017/your-database-name', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define a model for layers (replace with your actual model)
const Layer = mongoose.model('Layer', {
  value: String,
  label: String,
  fileId: mongoose.Types.ObjectId, // Store the MongoDB ObjectId of the file
});

// Initialize GridFS bucket
const db = mongoose.connection;
const gridFSBucket = new GridFSBucket(db.db, {
  bucketName: 'your-bucket-name', // Replace with your bucket name
});

// Serve the Cesium viewer HTML
app.get('/', async (req, res) => {
  try {
    // Fetch layer data from the database (replace with your specific query)
    const layers = await Layer.find({});

    res.render('index', { layers });
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

// Route to fetch and serve the selected layer file from GridFS
app.get('/getLayerFile/:layerId', (req, res) => {
  const layerId = req.params.layerId;

  // Fetch the layer by ID (replace with your specific query)
  Layer.findById(layerId, (err, layer) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Internal Server Error');
    }

    if (!layer) {
      return res.status(404).send('Layer not found');
    }

    // Fetch the file from GridFS
    const downloadStream = gridFSBucket.openDownloadStream(layer.fileId);

    // Set the appropriate content type (adjust as needed)
    res.setHeader('Content-Type', 'application/octet-stream');
    res.setHeader('Content-Disposition', `attachment; filename=${layer.value}.czml`);

    // Pipe the file data to the response
    downloadStream.pipe(res);
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
