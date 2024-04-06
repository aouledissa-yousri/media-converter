import { Box, FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import Button from "@mui/material/Button";
import { useRef, useState } from "react";



export default function ConverterComponent() {

    const fileInputRef = useRef<any>(null)
    const [selectedFile, setSelectedFile] = useState({
        file: null,
        name: ""
    })


    const [outputFormat, setOutputFormat] = useState("")


    const setConversionOutputFormat = () => {

    }

    const handleFileChange = (event: any) => {

        setSelectedFile({
            file: event.target.files[0],
            name: event.target.files[0].name
        })

    }

    const upload = () => {
        fileInputRef.current.click()
    }

    const fileAvailable = () => selectedFile.file === null

    return (
        <div>
            <input
                type="file"
                accept="image/*,video/*,audio/*"
                ref={fileInputRef}
                style={{ display: 'none' }}
                onChange={handleFileChange}
            />

            <Button variant="contained" component="span" onClick={upload}>Select File</Button>

            <h3>{selectedFile.name}</h3>


            <Box>


                <FormControl fullWidth>
                    <InputLabel id="demo-simple-select-label">Output Format</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        value={outputFormat}
                        label="Output Format"
                        onChange={setConversionOutputFormat}
                    >
                        <MenuItem value={10}>Ten</MenuItem>
                        <MenuItem value={20}>Twenty</MenuItem>
                        <MenuItem value={30}>Thirty</MenuItem>
                    </Select>
                </FormControl>
            </Box>
            
            <br/>
            <br/>
            <br/>

            <Button variant="contained" component="span" onClick={upload} disabled={fileAvailable()}>Convert File</Button>

        </div>
    )

    
}