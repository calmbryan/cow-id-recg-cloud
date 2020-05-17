import http from "../http-common";

class UploadFilesService {
  upload(file, onUploadProgress) {
    let formData = new FormData();

    formData.append("file", file);

    return http.post("/file/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      },
      onUploadProgress
    });
  }
  correct(file, newlabel) {
    let formData = new FormData();

    formData.append("file", file);
    formData.append("newlabel", newlabel);

    return http.post("/file/correct", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  }
}

export default new UploadFilesService();
