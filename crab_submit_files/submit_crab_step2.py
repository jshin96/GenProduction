from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "tt012j_Vcb_NLO_CP5_FXFX"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "../configs/run_crab_step2.py"
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 8

config.Data.inputDataset = "/tt012j_Vcb_NLO_CP5_FXFX/choij-RunIIFall18DRPremix-98b2ebbf2a73ad4baba14fc5516a6604/USER" 
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputDatasetTag = "RunIIAutumn18DRPremix"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T3_KR_KNU"
config.Site.whitelist = ["T2_*","T3_*"]
