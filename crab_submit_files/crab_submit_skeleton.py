from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'tt012j_Vcb_NLO_CP5_FXFX'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/Hadronizer_tt012j_Vcb_NLO_CP5_FXFX_cfg.py'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'tt012j_Vcb_NLO_CP5_FXFX'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100 # num. of jobs to submit
NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/choij/' 
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIIFall18wmLHEGS'

config.Site.storageSite = 'T3_KR_KNU'
