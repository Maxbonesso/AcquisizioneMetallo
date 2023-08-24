from pypylon import pylon
import platform

exposure_time = 100
num_img_to_save = 12
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()
cam = pylon.InstantCamera(tlf.CreateFirstDevice())
for i in range(num_img_to_save):
    cam.Open()
    cam.ChunkModeActive.SetValue(True);
    # Select and enable Exposure Time chunk
    cam.ChunkSelector.SetValue("ExposureTime")
    cam.ChunkEnable.SetValue(True)
    cam.StartGrabbing()

    with cam.RetrieveResult(1000) as result:

        # Calling AttachGrabResultBuffer creates another reference to the
        # grab result buffer. This prevents the buffer's reuse for grabbing.
        img.AttachGrabResultBuffer(result)

        if platform.system() == 'Windows':
            # The JPEG format that is used here supports adjusting the image
            # quality (100 -> best quality, 0 -> poor quality).
            ipo = pylon.ImagePersistenceOptions()
            quality = 100
            ipo.SetQuality(quality)
            cam.ExposureTime=exposure_time

            filename = "materiale7_00_speculare_00%d.jpeg" % exposure_time
            img.Save(pylon.ImageFileFormat_Jpeg, "img/acquisizione_3/materiale7/"+filename, ipo)
        else:
            filename = "saved_pypylon_img_00%d.png" % i
            img.Save(pylon.ImageFileFormat_Png, "img/acquisizione_3/materiale7/"+filename)

        # In order to make it possible to reuse the grab result for grabbing
        # again, we have to release the image (effectively emptying the
        # image object).
        img.Release()

    cam.StopGrabbing()
    cam.Close()
    exposure_time = exposure_time + 1000