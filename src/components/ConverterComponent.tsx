import { Box, FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import Button from "@mui/material/Button";
import { useRef, useState } from "react";
import { MediaFormatHelper } from "../helpers/MediaFormatHelper";
import { ConversionFacade } from "../facades/ConversionFacade";
import LoadingDialog from "../dialogs/LoadingDialog";



export default function ConverterComponent() {

    const fileInputRef = useRef<any>(null)
    const [selectedFile, setSelectedFile] = useState({
        file: null,
        name: ""
    })


    const [outputFormat, setOutputFormat] = useState("")
    const [formats, setFormats] = useState<string[]>([])

    const [outputFile, setOutputFile] = useState({
        link: "",
        name: ""
    })

    const [conversionLoading, setConversionLoading] = useState(false)


    const setConversionOutputFormat = (event: any) => setOutputFormat(event.target.value as string)

    const handleFileChange = (event: any) => {

        setSelectedFile({
            file: event.target.files[0],
            name: event.target.files[0].name
        })

        loadFormats(event.target.files[0].name)



    }

    const upload = () => {
        if(fileInputRef.current) fileInputRef.current.click()
    }

    const fileAvailable = () => selectedFile.file !== null && outputFormat !== ""

    const loadFormats = (filename: string) => setFormats(MediaFormatHelper.filterFormats(filename))

    const convertFile = async () => {
        setConversionLoading(true)

        const file = await ConversionFacade.convert(selectedFile.file as unknown as File, selectedFile.name, outputFormat)
        setOutputFile({
            link: URL.createObjectURL(file),
            name: MediaFormatHelper.getFileName(selectedFile.name) + "." + outputFormat
        })

        setConversionLoading(false)

    }

    return (
        <div>
            <input
                type="file"
                accept="image/jpeg,image/png,image/webp,image/svg+xml,video/mp4,video/webm,video/x-avi,video/x-flv,video/quicktime,audio/ogg,audio/mp4,audio/mpeg,audio/wav"
                ref={fileInputRef}
                style={{ display: 'none' }}
                onChange={handleFileChange}
            />

            <Button variant="contained" component="span" onClick={upload}>Select File</Button>

            <h3>{selectedFile.name}</h3>

            <LoadingDialog message={`Converting to ${outputFormat}`} isOpen={conversionLoading}/>


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
                        {formats.map((format) => (
                            <MenuItem key={format} value={format} selected={formats.indexOf(format) === 0}>
                                {format.toUpperCase()}
                            </MenuItem>
                        ))}
                    </Select>
                </FormControl>
            </Box>
            
            <br/>
            <br/>
            <br/>

            <Button variant="contained" component="span" onClick={convertFile} disabled={!fileAvailable()}>Convert File</Button>

            <h3><a href={outputFile.link} hidden={outputFile.link === ""} download={outputFile.name}>Download File</a></h3>

        </div>
    )

    
}