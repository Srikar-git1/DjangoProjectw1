import csv
from django.core.management.base import BaseCommand
from movies.forms import MovieForm


class Command(BaseCommand):
    help = ('import movies from csv file. Expected columns name,director,release,overview,genre,link')

    def add_arguments(self,parser):
        parser.add_argument("file_path", nargs=1, type=str)

    def handle(self, *args, **options):
        self.file_path = options["file_path"][0]
        self.prepare()
        self.main()
        self.finalise()

    def prepare(self):
        self.imported_counter = 0
        self.skipped_counter = 0

    def main(self):
        with open(self.file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for index, row_dict in enumerate(reader):
                form = MovieForm(data=row_dict)
                if form.is_valid():
                    movie = form.save()
                    self.imported_counter += 1
                else:
                    self.stderr.write(f"Errors importing movies"
                                      f"{row_dict['name']}:\n"
                                      )
                    self.stderr.write(f"{form.errors.as_json()}\n")

    def finalise(self):
        self.stdout(f"------------\n")
        self.stdout(f"Movies imported: {self.imported_counter}\n\n")