import React, { useEffect, useRef, useState } from "react";
import { io } from "socket.io-client";
import {
  Container,
  Typography,
  Grid,
  Card,
  CardContent,
  Chip,
} from "@mui/material";
import StatsChart from "../components/StatsChart";

export default function ResultsPage() {
  const [results, setResults] = useState([]);
  const [stats, setStats] = useState({ fake: 0, real: 0 });
  const socketRef = useRef(null);

  // Initial fetch
  useEffect(() => {
    fetch("http://localhost:8000/recent-results")
      .then((res) => res.json())
      .then((data) => {
        setResults(data);

        const fakeCount = data.filter(
          (item) => item.verdict?.verdict === "FAKE"
        ).length;
        const realCount = data.filter(
          (item) => item.verdict?.verdict === "REAL"
        ).length;
        setStats({ fake: fakeCount, real: realCount });
      });
  }, []);

  // Setup Socket.IO
  useEffect(() => {
    socketRef.current = io("http://localhost:8000");

    socketRef.current.on("connect", () => {
      console.log("Connected to WebSocket");
    });

    socketRef.current.on("new_result", (data) => {
      console.log("New result received:", data);
      setResults((prev) => [data, ...prev]);

      const verdictKey = data.verdict?.verdict?.toLowerCase();
      if (verdictKey === "fake" || verdictKey === "real") {
        setStats((prev) => ({
          ...prev,
          [verdictKey]: prev[verdictKey] + 1,
        }));
      }
    });

    socketRef.current.on("disconnect", () => {
      console.log("Disconnected from WebSocket");
    });

    return () => {
      if (socketRef.current) {
        socketRef.current.disconnect();
      }
    };
  }, []);

  return (
    <Container maxWidth="lg" sx={{ mt: 5 }}>
      <Typography variant="h4" gutterBottom>
        Recent Fake News Analysis
      </Typography>

      <StatsChart stats={stats} />

      <Grid container spacing={3}>
        {results.map((item, index) => (
          <Grid item xs={12} md={6} key={index}>
            <Card>
              <CardContent>
                <Typography variant="h6">Claim</Typography>
                <Typography>{item.claim}</Typography>

                <Typography variant="h6" sx={{ mt: 2 }}>
                  Verdict
                </Typography>
                <Chip
                  label={item.verdict?.verdict}
                  color={
                    item.verdict?.verdict === "FAKE" ? "error" : "success"
                  }
                />

                {item.verdict?.confidence !== undefined && (
                  <Typography sx={{ mt: 1 }}>
                    Confidence: {Math.round(item.verdict.confidence * 100)}%
                  </Typography>
                )}

                {item.reason && (
                  <Typography sx={{ mt: 1 }}>
                    Reason: {item.reason}
                  </Typography>
                )}
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}
