import { React, useEffect, useState } from "react";
import { Box, Typography, Button } from "@mui/material";
import MyDatePickerFields from "./froms/MyDatePickerFields";
import MyMultilineTextFields from "./froms/MyMultilineTextFields";
import MySelectFields from "./froms/MySelectFields";
import MyTextFields from "./froms/MyTextfFields";
import { useForm } from "react-hook-form";
import AxiosInstance from "./Axios";
// import Dayjs from "dayjs";
import dayjs from "dayjs";
import { useNavigate } from "react-router-dom";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

const Create = () => {
  const [projectManager, setProjectManager] = useState();
  const [loading, setLoading] = useState(true);

  const hardcoded_options = [
    { id: "", name: "None" },
    { id: "Open", name: "Open" },
    { id: "In prpgress", name: "In prpgress" },
    { id: "Completed", name: "Completed" },
  ];

  const GetData = () => {
    AxiosInstance.get(`projectManager/`).then((res) => {
      setProjectManager(res.data);
      console.log(res.data);
      setLoading(false);
    });
  };

  useEffect(() => {
    GetData();
  }, []);

  const navigate = useNavigate();
  const defaultValues = {
    name: "",
    comments: "",
    status: "",
    start_date: null,
    end_date: null,
    // start_date: "",
    // end_date: "",
  };

  const schema = yup.object({
    name: yup.string().required("Name is a required field"),
    status: yup.string().required("Status is a required field"),
    comments: yup.string(),
    start_date: yup.date().required("Start date is a required field"),
    end_date: yup
      .date()
      .required("End date is a required field")
      .min(
        yup.ref("start_date"),
        "The end date cannot be before the start date"
      ),
    projectManager: yup.string().required("Project manager is a required field"),
  });

  // useForm: 入力されたデータが扱いやすくなる。ここでは4つの機能を呼び出し。
  // handleSubmit: 「送信」ボタンが押されたときに、どうやってデータを送るか決めるための機能
  // reset: フォームを初期の状態に戻す機能（たとえば、送信後に入力欄を空にする）
  // setValue: フォームの中の特定の入力欄に新しい値を設定する機能
  // control: フォームの入力欄をツールとつなげるための機能
  //         （どのデータがどの入力欄に対応しているかを管理）
  const { handleSubmit, control } = useForm({
    // defaultValues: 初期値
    defaultValues: defaultValues,
    resolver: yupResolver(schema),
  });

  // 「送信」ボタンが押されたときのデータの送り方を定義
  const submission = (data) => {
    // dayjs(): 日付や時間を簡単に扱うためのツール
    // dayjs(日付).format('YYYY-MM-DD')
    const startDate = data.start_date
      ? dayjs(data.start_date).format("YYYY-MM-DD")
      : null;
    const endDate = data.end_date
      ? dayjs(data.end_date).format("YYYY-MM-DD")
      : null;

    AxiosInstance.post(`project/`, {
      name: data.name,
      status: data.status,
      comments: data.comments,
      start_date: startDate,
      end_date: endDate,
      projectManager: data.projectManager,
    }).then((res) => {
      navigate(`/`);
    });
  };

  return (
    <div>
      {loading ? (
        <p>Loading data...</p>
      ) : (
        <form onSubmit={handleSubmit(submission)}>
          <Box
            sx={{
              display: "flex",
              width: "100%",
              backgroundColor: "#00003f",
              marginBottom: "10px",
            }}
          >
            <Typography sx={{ marginLeft: "20px", color: "#fff" }}>
              Create records
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
                justifyContent: "space-around",
                marginBottom: "40px",
              }}
            >
              <MyTextFields
                label="Name"
                name="name"
                control={control}
                placeholder="Provide a project name"
                width={"30%"}
              />
              <MyDatePickerFields
                label="Start date"
                name="start_date"
                control={control}
                width={"30%"}
              />
              <MyDatePickerFields
                label="End date"
                name="end_date"
                control={control}
                width={"30%"}
              />
            </Box>

            <Box
              sx={{
                display: "flex",
                justifyContent: "space-around",
              }}
            >
              <MyMultilineTextFields
                label="Comments"
                name="comments"
                control={control}
                placeholder="Provide project's comment"
                width={"30%"}
              />
              <MySelectFields
                label="Status"
                name="status"
                control={control}
                width={"30%"}
                options={hardcoded_options}
              />
              <MySelectFields
                label="Project manager"
                name="projectManager"
                control={control}
                width={"30%"}
                options={projectManager}
              />
            </Box>

            <Box
              sx={{
                display: "flex",
                justifyContent: "start",
                marginTop: "40px",
              }}
            >
              <Button variant="contained" type="submit" sx={{ width: "30%" }}>
                Submit
              </Button>
            </Box>
          </Box>
        </form>
      )}
    </div>
  );
};

export default Create;
