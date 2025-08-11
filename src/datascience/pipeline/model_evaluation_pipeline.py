from src.datascience import logger
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.config.configuration import ConfigurationManager

STAGE_NAME = "Model Evaluation Phase"
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
    
    except Exception as e:
        logger.exception(e)
        raise e
