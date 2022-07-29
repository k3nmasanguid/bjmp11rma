;(function () {
    const modal = new bootstrap.Modal(document.getElementById("register-modal"))

    htmx.on("htmx:beforeSwap", (e) => {
      // Empty response targeting #dialog => hide the modal
      if (e.detail.target.id == "register-modal-dialog" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
      }
    })
  
    // Remove dialog content after hiding
    htmx.on("hidden.bs.modal", () => {
      document.getElementById("register-modal-dialog").innerHTML = ""
    })
  })()

  ;(function () {
    const modal = new bootstrap.Modal(document.getElementById("personal-info-modal"))

    htmx.on("htmx:beforeSwap", (e) => {
      // Empty response targeting #dialog => hide the modal
      if (e.detail.target.id == "personal-info-modal-dialog" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
      }
    })
  
    // Remove dialog content after hiding
    htmx.on("hidden.bs.modal", () => {
      document.getElementById("personal-info-modal-dialog").innerHTML = ""
    })
  })()