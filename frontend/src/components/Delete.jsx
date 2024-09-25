import { React, useEffect, useState } from "react";
import { Box, Typography, Button } from "@mui/material";
import AxiosInstance from "./Axios";
import { useNavigate, useParams } from "react-router-dom";

const Delete = () => {
  const myParam = useParams();
  const myId = myParam.id;

  const [myData, setMyData] = useState();
  const [loading, setLoading] = useState(true);

  const GetData = () => {
    AxiosInstance.get(`project/${myId}`).then((res) => {
      setMyData(res.data);
      console.log(res.data);
      setLoading(false);
    });
  };

  useEffect(() => {
    GetData();
  }, []);

  const navigate = useNavigate();

  // 「送信」ボタンが押されたときのデータの送り方を定義
  const submission = (data) => {
    AxiosInstance.delete(`project/${myId}/`).then((res) => {
      navigate(`/`);
    });
  };

  return (
    <div>
      {loading ? (
        <p>Loading data...</p>
      ) : (
        <div>
          <Box
            sx={{
              display: "flex",
              width: "100%",
              backgroundColor: "#00003f",
              marginBottom: "10px",
            }}
          >
            <Typography sx={{ marginLeft: "20px", color: "#fff" }}>
              Delete project: {myData.name}
            </Typography>
          </Box>

          <Box
            sx={{
              display: "flex",
              width: "100%",
              boxShadow: 3,
              padding: 4,
              flexDirection: "column",
            }}
          >
            <Box
              sx={{
                display: "flex",
                justifyContent: "start",
                marginBottom: "40px",
              }}
            >
              Are you sure that you want to delete project: {myData.name}
            </Box>
            <Box
              sx={{
                width: "30%",
              }}
            >
              <Button
                variant="contained"
                onClick={submission}
                sx={{ width: "100%" }}
              >
                Delete the project
              </Button>
            </Box>
          </Box>
        </div>
      )}
    </div>
  );
};

export default Delete;
