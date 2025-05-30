import React, { useState } from "react";
import {
  Container,
  TextField,
  Button,
  Typography,
  CircularProgress,
  Box,
  Paper,
} from "@mui/material";

export default function AnalyzePage() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setResult({ error: "Something went wrong!" });
    }
    setLoading(false);
  };

  return (
    <Container maxWidth="md" sx={{ mt: 5 }}>
      <Typography variant="h4" gutterBottom>
        Analyze News Article
      </Typography>
      <TextField
        label="Paste article text"
        multiline
        rows={6}
        fullWidth
        value={text}
        onChange={(e) => setText(e.target.value)}
        sx={{ mb: 2 }}
      />
      <Box display="flex" alignItems="center" gap={2}>
        <Button variant="contained" onClick={handleAnalyze} disabled={!text || loading}>
          Analyze
        </Button>
        {loading && <CircularProgress size={24} />}
      </Box>

      {result && (
        <Paper elevation={3} sx={{ mt: 4, p: 2 }}>
          <Typography variant="h6">Analysis Result:</Typography>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </Paper>
      )}
    </Container>
  );
}
