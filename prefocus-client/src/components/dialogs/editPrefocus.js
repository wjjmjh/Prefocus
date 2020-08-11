import React from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import "../../styles/dialogs/dialog.scss";

class EditPrefocus extends React.Component {
  constructor(props) {
    super(props);
    this.state = { open: false, value: "" };
  }

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
    console.log(this.state.value);
  };

  setTextValue = (event) => {
    this.setState({ value: event.target.value });
  };

  render() {
    return (
      <div>
        <Button
          id={"dialog_button"}
          variant="outlined"
          color="primary"
          onClick={this.handleClickOpen}
        >
          edit this Prefocus
        </Button>
        <Dialog
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogContent>
            <DialogContentText>Edit this Prefocus.</DialogContentText>
            <TextField
              autoFocus
              onChange={this.setTextValue}
              margin="dense"
              id="name"
              label="new Prefocus"
              fullWidth
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={this.handleClose} color="primary">
              Edit
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
  }
}

export default EditPrefocus;
