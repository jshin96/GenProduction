from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "tt012j_Vcb_NLO_CP5_FXFX"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "../config/run_crab_step1.py"
config.JobType.maxMemoryMB = 12000
config.JobType.numCores = 8

config.Data.inputDataset = "/tt012j_Vcb_NLO_CP5_FXFX/choij-RunIIFall18wmLHEGS-b83ba777a6314fd06886090a3c3834eb/USER" 
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputDatasetTag = "RunIIAutumn18DRPremix"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T3_KR_KNU"
config.Site.whitelist = ["T2_*","T3_*"]
