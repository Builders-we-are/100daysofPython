print('Hello, World!')

const express = require('express');
const app = express();
const port = 3000;
const { MongoClient } = require('mongodb');
const Grid = require('gridfs-stream');
const path = require('path');

const mongoUri = 'mongodb://localhost:27017'; // Replace with your MongoDB connection URI
const dbName = 'your-database-name'; // Replace with your database name

// Initialize MongoDB client
const client = new MongoClient(mongoUri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Connect to the MongoDB server
client.connect((err) => {
  if (err) {
    console.error('MongoDB connection error:', err);
    process.exit(1);
  }

  const db = client.db(dbName);

  // Initialize GridFS
  const gfs = Grid(db, db.mongo);

  // Serve the Cesium viewer HTML
  app.get('/', async (req, res) => {
    try {
      // Fetch layer data from the database (replace with your specific query)
      const layers = await db.collection('layers').find({}).toArray();

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
    db.collection('layers').findOne({ _id: new ObjectId(layerId) }, (err, layer) => {
      if (err) {
        console.error(err);
        return res.status(500).send('Internal Server Error');
      }

      if (!layer) {
        return res.status(404).send('Layer not found');
      }

      // Fetch the file from GridFS
      const readstream = gfs.createReadStream({
        _id: layer.fileId,
      });

      // Set the appropriate content type (adjust as needed)
      res.setHeader('Content-Type', 'application/octet-stream');
      res.setHeader('Content-Disposition', `attachment; filename=${layer.value}.czml`);

      // Pipe the file data to the response
      readstream.pipe(res);
    });
  });

  app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
});
