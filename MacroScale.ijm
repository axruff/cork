setBatchMode(true);

for (i=0; i<22; i++) {


open("Z:/tomo/ershov/cork/2019-11-InSitu-MotionAnalysis/Spray_43e/slices8bit_" + IJ.pad(i, 3) +".tif");
rename("Old");

run("Scale...", "x=0.5 y=0.5 z=0.5 width=450 height=450 depth=180 interpolation=Bilinear average process create");

selectWindow("Old");
close();

run("Reslice [/]...", "output=1.000 start=Top avoid");

saveAs("Tiff", "Z:/tomo/ershov/cork/2019-11-InSitu-MotionAnalysis/Spray_43e/input/" + IJ.pad(i, 3) + "_scaled2_450-450-180.tif");
saveAs("Raw Data", "Z:/tomo/ershov/cork/2019-11-InSitu-MotionAnalysis/Spray_43e/input/" + IJ.pad(i, 3) + "_scaled2_450-450-180.raw");

close();
close();
//close();
}

showMessage("Finished!");
