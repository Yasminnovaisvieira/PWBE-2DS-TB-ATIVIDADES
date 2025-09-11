import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Editora, Autor, Livro
 
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo_livros", default="population/livros.csv")
        parser.add_argument("--arquivo_editoras", action="population/editoras.csv")
        parser.add_argument("--arquivo_autores", action="population/autores.csv")
 
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")
 
    @transaction.atomic
    def handle(self, *a, **o):
 
        #Leitura dos códigos do arquivo colocados lá em cima
       
        df_autores= pd.read_csv(o["arquivo_autores"], encoding="utf-8-sig")
        df_editoras= pd.read_csv(o["arquivo_editoras"], encoding="utf-8-sig")
        df_livros= pd.read_csv(o["arquivo_livros"], encoding="utf-8-sig")
 
        df_autores.columns = [c.strip().lower().lstrip("\ufeff") for c in df_autores.columns]
        df_editoras.columns = [c.strip().lower().lstrip("\ufeff") for c in df_editoras.columns]
        df_livros.columns = [c.strip().lower().lstrip("\ufeff") for c in df_livros.columns]
 
        if o["truncate"]:
            Livro.objects.all().delete()
 
        df["editora"] = df["editora"].astype(str).str.strip()
        df["cnpj"] = df["cnpj"].astype(str).str.strip()
        df["endereco"] = df["endereco"].astype(str).str.strip()
        df["telefone"] = df["telefone"].astype(str).str.strip()
        df["email"] = df["email"].astype(str).str.strip()  # Corrected: Read from the 'email' column
        df["site"] = df["site"].astype(str).str.strip()
 
        if o["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Livro.objects.update_or_create(
                    cnpj=r.cnpj,  # Using a unique field like cnpj for lookup
                    defaults={
                        "editora": r.editora,
                        "endereco": r.endereco,
                        "telefone": r.telefone,
                        "email": r.email,
                        "site": r.site, # Corrected: 'r.ite' to 'r.site'
                    }
                )
                criados += int(created)
                atualizados += int(not created)
            self.stdout.write(self.style.SUCCESS(f"Criados: {criados} | Atualizados: {atualizados}"))
        else:
            objs = [
                Livro(
                    editora=r.editora,
                    cnpj=r.cnpj,
                    endereco=r.endereco,
                    telefone=r.telefone,
                    email=r.email,
                    site=r.site,
                )
                for r in df.itertuples(index=False)
            ]
            Livro.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objs)} editoras"))