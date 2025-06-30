import React from "react";
import { useNavigate } from "react-router-dom";
import { Box, Button, Typography, Card, CardContent } from "@mui/material";
import { ShieldCheck, BarChart, AlertTriangle } from "lucide-react";
import { motion } from "framer-motion";

const HomePage = () => {
  const navigate = useNavigate();

  const features = [
    {
      title: "AI-Powered Detection",
      description: "Our advanced transformer model analyzes text patterns to identify fake news.",
      icon: <ShieldCheck size={36} color="#1e88e5" />,
    },
    {
      title: "Real-time Analysis",
      description: "Get instant results with confidence scores and reference sources.",
      icon: <BarChart size={36} color="green" />,
    },
    {
      title: "Source Verification",
      description: "Cross-reference with trusted fact-checking organizations.",
      icon: <AlertTriangle size={36} color="red" />,
    },
  ];

  return (
    <Box
      sx={{
        minHeight: "100vh",
        backgroundColor: "#f7f9fc",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        py: 6,
      }}
    >
      <Typography variant="h3" fontWeight="bold" gutterBottom>
        Fight Fake News with AI
      </Typography>
      <Typography variant="h6" color="textSecondary" textAlign="center" maxWidth="800px" mb={4}>
        Advanced machine learning technology to detect and combat misinformation in real time.
      </Typography>

      <Box
        display="flex"
        justifyContent="center"
        flexWrap="wrap"
        gap={4}
        mb={6}
      >
        {features.map((feature, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.2 }}
          >
            <Card
              sx={{
                width: 300,
                p: 2,
                borderRadius: 4,
                boxShadow: 4,
              }}
            >
              <CardContent sx={{ textAlign: "center" }}>
                <Box mb={2}>{feature.icon}</Box>
                <Typography variant="h6" fontWeight="bold">
                  {feature.title}
                </Typography>
                <Typography variant="body2" color="textSecondary" mt={1}>
                  {feature.description}
                </Typography>
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </Box>

      <Button
        variant="contained"
        size="large"
        onClick={() => navigate("/analyze")}
        sx={{ borderRadius: "12px", px: 4 }}
      >
        Start Analyzing News
      </Button>
    </Box>
  );
};

export default HomePage;
