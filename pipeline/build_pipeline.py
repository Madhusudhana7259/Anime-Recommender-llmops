from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


load_dotenv()

logger = get_logger(__name__)


def main():
    try:
        logger.info("Starting Anime Recommendation Pipeline")

        loader = AnimeDataLoader(original_csv="data/anime_with_synopsis.csv",processed_csv="data/anime_updated.csv")
        processed_csv = loader.load_and_process()

        logger.info("Data loaded and processed successfully")

        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store built and saved successfully")
    
    except Exception as e:
        logger.error(f"Failed to execute the exception {str(e)}")
        raise CustomException("Error during pipeline execution}")


if __name__ == "__main__":
    main()