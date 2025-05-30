import React from "react";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

export default function StatsChart({ stats }) {
  const data = {
    labels: ["Fake News", "Real News"],
    datasets: [
      {
        data: [stats.fake, stats.real],
        backgroundColor: ["#f44336", "#4caf50"],
        hoverOffset: 8,
      },
    ],
  };

  return (
    <div style={{ maxWidth: "400px", margin: "2rem auto" }}>
      <h3 style={{ textAlign: "center" }}>Fake vs Real News</h3>
      <Pie data={data} />
    </div>
  );
}
