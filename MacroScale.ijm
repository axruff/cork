
i = 3

open("Z:/tomo/ershov/cork/2019-11-InSitu-MotionAnalysis/HP1031_KI/slices8bit_" + IJ.pad(i, 3) +".tif");


run("Scale...", "x=0.5 y=0.5 z=0.5 width=450 height=450 depth=180 interpolation=Bilinear average process create");

run("Reslice [/]...", "output=1.000 start=Top avoid");

saveAs("Tiff", "Z:/tomo/ershov/cork/2019-11-InSitu-MotionAnalysis/HP1031_KI/input/" + IJ.pad(i, 3) + "_scaled2_450-450-180.tif");

saveAs("Raw Data", "Z:/tomo/ershov/cork/2019-11-InSitu-MotionAnalysis/HP1031_KI/input/" + IJ.pad(i, 3) + "_scaled2_450-450-180.raw");

close();
close();
close();
