from constants import *
import os
import shutil

os.system('cls')

class Cleaner:
   def __init__(self) -> None:
      self.files = os.listdir(DOWNLOADS_FOLDER)

      self.categorized_files = {
         'compressed': [],
         'documents': [],
         'images': [],
         'folders': [],
         'videos': [],
      }


   @staticmethod
   def is_compressed(file_extension: str) -> bool:
      return file_extension.lower() in COMPRESSED_EXTENSIONS


   @staticmethod
   def is_document(file_extension: str) -> bool:
      return file_extension.lower() in DOCUMENTS_EXTENSIONS


   @staticmethod
   def is_image(file_extension: str) -> bool:
      return file_extension.lower() in IMAGES_EXTENSIONS


   @staticmethod
   def is_folder(file: str) -> bool:
      if file.lower() in Cleaner().categorized_files.keys():
         return

      return os.path.isdir(os.path.join(DOWNLOADS_FOLDER, file))


   @staticmethod
   def is_video(file_extension: str) -> bool:
      return file_extension.lower() in VIDEOS_EXTENSIONS
   

   def __categorize(self, file: str) -> None:
      _, extension = os.path.splitext(file)

      for category in self.categorized_files.keys():
         function_name = f'is_{category.rstrip("s")}'

         type_checker = getattr(Cleaner, function_name)

         if category == 'folders':
            if type_checker(file):
               self.categorized_files[category].append(file)
         else:
            if type_checker(extension):
               self.categorized_files[category].append(file)


   def __organize_files(self):
      for category in self.categorized_files.keys():
         category_folder_path = os.path.join(DOWNLOADS_FOLDER, category.capitalize())

         has_folder = os.path.isdir(category_folder_path)
         
         if not has_folder:
            os.mkdir(category_folder_path)

         for file in self.categorized_files[category]:
            shutil.move(
               src=os.path.join(DOWNLOADS_FOLDER, file),
               dst=os.path.join(DOWNLOADS_FOLDER, category_folder_path)
            )


   def start_cleaning(self):
      [self.__categorize(file) for file in self.files]

      self.__organize_files()


if __name__ == '__main__':
   Cleaner().start_cleaning()
