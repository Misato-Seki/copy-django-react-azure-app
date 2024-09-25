import * as React from "react";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { Controller } from "react-hook-form";

export default function MyDatePickerFields(props) {
  const { label, width, control, name } = props;
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Controller
        name={name}
        control={control}
        // ボックスがどう表示されるかを書く
        render={({ 
          field: { onChange, value },
          fieldState: {error},
          formState,
        }) => (
          <DatePicker
            sx={{ width: [width] }}
            label={label}
            onChange={onChange}
            value={value}
            slotProps={{
              textField:{
                error: !!error,
                helperText: error?.message,
              }
            }}
          />
        )}
      />
    </LocalizationProvider>
  );
}
