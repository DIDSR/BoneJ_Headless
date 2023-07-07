array,array1header = nrrd.read(volume)  # should be a numpy array
voxel_size = [51.29980, 51.29980, 51.29980] #microns 
fiji_path = "~/Fiji.app/ImageJ-linux64"

nVectors_list = [100,200,300,400]
VectorIncrement_list = [1,2,3]
skipRatio_list = [1,2,3]
contactSensitivity_list = [1,2,3]
maxDrift_list = [1,2,3]
maxIterations_list = [30,40,50]
distanceThreshold_list = [.2,.4,.6,.8,1.0]

def Ellipsoid_Factor_Convergence(array,voxel_size,fiji_path,nVectors = nVectors_list,
vectorIncrement = VectorIncrement_list,
skipRatio = skipRatio_list,
contactSensitivity = contactSensitivity_list,
maxDrift = maxDrift_list,
maxIterations = maxIterations_list,
distanceThreshold = distanceThreshold_list,
runs = 1,
seedOnDistanceRidge = True,
seedOnTopologyPreserving = True,
showFlinnPlots = False,
showConvergence = False,
showSecondaryImages = False):

    for i in nVectors_list:
        for j in VectorIncrement_list: 
            for k in skipRatio_list: 
                for l in  contactSensitivity_list: 
                    for m in maxDrift_list: 
                        for n in maxIterations_list: 
                            for o in distanceThreshold_list: 

                                nVectors = str(i)
                                vectorIncrement = str(j)
                                skipRatio = str(k)
                                contactSensitivity = str(l)
                                maxDrift = str(m)
                                maxIterations = str(n)
                                distanceThreshold = str(o)
                                runs = str(runs)
                                seedOnDistanceRidge = str(seedOnDistanceRidge)
                                seedOnTopologyPreserving = str(seedOnTopologyPreserving)
                                showFlinnPlots = str(showFlinnPlots)
                                showConvergence = str(showConvergence)
                                showSecondaryImages = str(showSecondaryImages)

                                tempdir = tempfile.TemporaryDirectory()
                                data1_nrrd = os.path.join(tempdir.name,"img.nrrd")
                                table_csv = os.path.join(tempdir.name,"table.csv")
                                outputdir = os.path.join(tempdir.name, "outputdir")
                                img_ef_tif = os.path.join(tempdir.name,"img_ef.tif")
                                img_volume_tif = os.path.join(tempdir.name,"img_volume.tif")
                                img_id_tif = os.path.join(tempdir.name,"img_id.tif")
                                img_a_tif = os.path.join(tempdir.name,"img_a.tif")
                                img_c_tif = os.path.join(tempdir.name,"img_c.tif")
                                img_ab_tif = os.path.join(tempdir.name,"img_ab.tif")
                                img_bc_tif = os.path.join(tempdir.name,"img_bc.tif")
                                img_seed_points_tif = os.path.join(tempdir.name,"img_seed_points.tif")
                                img_flinn_peak_plot_tif = os.path.join(tempdir.name,"img_flinn_peak_plot.tif")
                                img_unweighted_flinn_plot_tif = os.path.join(tempdir.name,"img_unweighted_flinn_plot.tif")
                                macro_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"Macros/Ellipsoid_Factor_API_Test.py"))


                                # save to temporary directory
                                header = {'units': ['um', 'um', 'um'],'spacings': voxel_size}

                                nrrd.write(data1_nrrd,array,header)

                                # run BoneJ thickness wraapper 
                                # table is results of thickness plugin as csv file 
                                # thickness_tif is numpy array of thickness images 

                                fiji_cmd = "".join([fiji_path, " --ij2", " --headless", " --run", " "+macro_file, 
                                                     " \'image="+"\""+data1_nrrd+"\"", ", img_ef_tif="+"\""+img_ef_tif+"\"",
                                                     ", img_volume_tif="+"\""+img_volume_tif+"\"",", img_id_tif="+"\""+img_id_tif+"\"",
                                                     ", img_a_tif="+"\""+img_a_tif+"\"",", img_b_tif="+"\""+img_c_tif+"\"",
                                                     ", img_ab_tif="+"\""+img_ab_tif+"\"",", img_bc_tif="+"\""+img_bc_tif+"\"",
                                                     ", img_seed_points_tif="+"\""+img_seed_points_tif+"\"",", img_flinn_peak_plot_tif="+"\""+img_flinn_peak_plot_tif+"\"",
                                                     ", img_unweighted_flinn_plot_tif="+"\""+img_unweighted_flinn_plot_tif+"\"",
                                                     ", nVectors="+"\""+nVectors+"\"",
                                                     ", vectorIncrement="+"\""+vectorIncrement+"\"",
                                                     ", skipRatio="+"\""+skipRatio+"\"",
                                                     ", contactSensitivity="+"\""+contactSensitivity+"\"",
                                                     ", maxIterations="+"\""+maxIterations+"\"",
                                                     ", maxDrift="+"\""+maxDrift+"\"",
                                                     ", runs="+"\""+runs+"\"",
                                                     ", seedOnDistanceRidge="+"\""+seedOnDistanceRidge+"\"",
                                                     ", distanceThreshold="+"\""+distanceThreshold+"\"",
                                                     ", seedOnTopologyPreserving="+"\""+seedOnTopologyPreserving+"\"",
                                                     ", showFlinnPlots="+"\""+showFlinnPlots+"\"",
                                                     ", showConvergence="+"\""+showConvergence+"\"",
                                                     ", showSecondaryImages="+"\""+showSecondaryImages+"\"",
                                                     ", outputdir="+"\""+outputdir+"\"",
                                                     ", table_csv="+"\""+table_csv+"\""+"\'"])

                                print(f"{NAME}")             
                                b = subprocess.call(fiji_cmd, shell=True)
                                with open(outputdir+f"ROI-{NAME}-table.csv", "r",encoding='utf-8') as file:
                                    reader = csv.reader(file)
                                    metric_dict = {row[0]:row[1:] for row in reader if row and row[0]}
                                    print(metric_dict)


                                return metric_dict       


Ellipsoid_Factor_result = Ellipsoid_Factor_Convergence(array,voxel_size,fiji_path,nVectors = nVectors_list,
vectorIncrement = VectorIncrement_list,
skipRatio = skipRatio_list,
contactSensitivity = contactSensitivity_list,
maxIterations = maxIterations_list,
maxDrift = maxDrift_list,
runs = 1,
seedOnDistanceRidge = True,
distanceThreshold = .8,
seedOnTopologyPreserving = True,
showFlinnPlots = False,
showConvergence = False,
showSecondaryImages = False)
