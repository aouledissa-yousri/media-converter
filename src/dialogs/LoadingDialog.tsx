import { CircularProgress, Dialog, DialogContent, DialogTitle } from "@mui/material";

interface LoadingDialogPropsInterface {
    message: string
    isOpen: boolean
}


export default function LoadingDialog(props: LoadingDialogPropsInterface) {
    

    return (
            <div>
            {/* Your application content here */}
            <Dialog open={props.isOpen}>
                <DialogTitle>{props.message}</DialogTitle>
                <DialogContent sx={{ display: 'flex', justifyContent: 'center' }}>
                    <CircularProgress />
                </DialogContent>
            </Dialog>
    </div>
    )
}
