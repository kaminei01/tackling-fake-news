import React from "react";
import { Container, Typography, Button, Box, Grid, Paper, Divider } from "@mui/material";
import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <Container maxWidth="lg" sx={{ mt: 5, mb: 8 }}>
      {/* Header Section */}
      <Box textAlign="center" mb={6}>
        <Typography variant="h3" gutterBottom>
          Tackling Fake News
        </Typography>
        <Typography variant="h6" color="text.secondary">
          A trustworthy initiative to fight misinformation and promote responsible media consumption.
        </Typography>
        <Button
          variant="contained"
          size="large"
          sx={{ mt: 3 }}
          component={Link}
          to="/analyze"
        >
          Analyze News Now
        </Button>
      </Box>

      <Divider sx={{ mb: 6 }} />

      {/* About Fake News */}
      <Grid container spacing={4}>
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>
              What is Fake News?
            </Typography>
            <Typography>
              Fake news refers to false or misleading information presented as news. It spreads rapidly through social media and other digital platforms, often without fact-checking or accountability.
            </Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>
              Why It Matters
            </Typography>
            <Typography>
              Fake news undermines democracy, spreads fear, manipulates public opinion, and erodes trust in legitimate sources. By detecting and reporting fake news, we help preserve information integrity.
            </Typography>
          </Paper>
        </Grid>
      </Grid>

      {/* Platform Mission & Approach */}
      <Box sx={{ mt: 6 }}>
        <Paper elevation={3} sx={{ p: 4 }}>
          <Typography variant="h5" gutterBottom>
            How Our Platform Works
          </Typography>
          <Typography>
            This website leverages AI and machine learning to analyze news articles or claims. By examining linguistic cues, metadata, and common fake news patterns, we offer an intelligent verdict on the claim's credibility.
          </Typography>
          <Typography sx={{ mt: 2 }}>
            Our goal is not only to automate fact-checking but also to educate users about recognizing misleading content themselves.
          </Typography>
        </Paper>
      </Box>

      {/* Resources Section */}
      <Box sx={{ mt: 6 }}>
        <Paper elevation={3} sx={{ p: 4 }}>
          <Typography variant="h5" gutterBottom>
            Learn More
          </Typography>
          <Typography>
            Explore these reliable resources to build your media literacy and stay updated:
          </Typography>
          <ul style={{ paddingLeft: "1.5em", marginTop: "1em" }}>
            <li><a href="https://www.factcheck.org" target="_blank" rel="noopener noreferrer">FactCheck.org</a> – A nonpartisan site for political fact-checking.</li>
            <li><a href="https://www.snopes.com" target="_blank" rel="noopener noreferrer">Snopes.com</a> – Debunks urban legends, hoaxes, and rumors.</li>
            <li><a href="https://newslit.org" target="_blank" rel="noopener noreferrer">News Literacy Project</a> – Offers educational tools and courses.</li>
            <li><a href="https://www.poynter.org/ifcn/" target="_blank" rel="noopener noreferrer">IFCN (International Fact-Checking Network)</a> – Promotes best practices in fact-checking.</li>
          </ul>
        </Paper>
      </Box>

      {/* Final Call-to-Action */}
      <Box textAlign="center" mt={6}>
        <Typography variant="h6" gutterBottom>
          Ready to check a headline or claim?
        </Typography>
        <Button
          variant="contained"
          size="large"
          color="success"
          component={Link}
          to="/analyze"
        >
          Start Analyzing
        </Button>
      </Box>
    </Container>
  );
}
