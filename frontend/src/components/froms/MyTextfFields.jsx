import * as React from "react";
import TextField from "@mui/material/TextField";
// Controllerはテキストボックスを便利に操作するための道具
import { Controller } from "react-hook-form";

export default function MyTextFields(props) {
  const { label, width, placeholder, name, control } = props;
  return (
    <Controller
      name={name}
      control={control}
      // ボックスがどう表示されるかを書く
      render={({
        field: { onChange, value },
        fieldState: { error },
        formState,
      }) => (
        <TextField
          sx={{ width: [width] }}
          onChange={onChange}
          value={value}
          id="standard-basic"
          label={label}
          variant="standard"
          placeholder={placeholder}
          error = {!!error}
          helperText = {error?.message}
        />
      )}
    />
  );
}
