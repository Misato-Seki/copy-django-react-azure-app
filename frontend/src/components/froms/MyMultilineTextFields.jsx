import * as React from "react";
import TextField from "@mui/material/TextField";
import { Controller } from "react-hook-form";

export default function MyMultilineTextFields(props) {
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
          id="standard-multiline-static"
          label={label}
          multiline
          rows={1}
          variant="standard"
          placeholder={placeholder}
          error = {!!error}
          helperText = {error?.message}
        />
      )}
    />
  );
}
