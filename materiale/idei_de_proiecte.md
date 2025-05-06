STRUCTURA RECOMANDATA DE PROIECT DJANGO

1. Creare de proiect Django nou

2. Configurare mediu virtual (venv)

3. Creare aplicatie Django

4. Definire modele in models.py (minim 2 modele)

5. Implementare views (CBV) in views.py
   - CreateView: creare obiect
   - UpdateView: actualizare obiect
   - DeleteView: stergere obiect
   - DetailView: detalii obiect
   - ListView: afisare lista obiecte

6. Validari in formular (forms.py)
   - Creare clasa custom: ModelForm
   - Validari prin clean()

7. Creare de user si login
   - Utilizare auth: from django.contrib.auth.forms import UserCreationForm
   - LoginView, LogoutView din django.contrib.auth.views
   - Decoratori: @login_required sau LoginRequiredMixin

8. Trimitere de emailuri
   - Configurare server mail in settings.py
   - Folosire send_mail() in views.py

9. Configurare static si media
   - settings.py:
       STATIC_URL = '/static/'
       MEDIA_URL = '/media/'
       MEDIA_ROOT = BASE_DIR / 'media'
   - urls.py:
       from django.conf import settings
       from django.conf.urls.static import static
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

10. Folosirea context processors
    - Adaugare functii in context_processors.py
    - In settings.py, adaugare calea in TEMPLATES > OPTIONS > 'context_processors'

EXTRA: Structura directoare recomandata
- nume_proiect/
  - settings.py
  - urls.py
  - wsgi.py
- nume_aplicatie/
  - models.py
  - views.py
  - forms.py
  - admin.py
  - urls.py
- templates/
  - base.html
- static/
  - css/
  - js/
- media/
- context_processors.py (optional)


1. **Aplicatie "Bucket List" cu gamificare**
   - Utilizatorii isi creeaza lista de obiective (ex: calatorii, hobby-uri, sporturi).
   - Pot marca obiectivele ca realizate + pot adauga poze ca dovezi.
   - Badge-uri pentru realizari (ex: "100% completat", "Inceput de calatorie").
   - Email motivant daca nu au bifat niciun obiectiv recent.
   - Context processor: afisare cate obiective au fost realizate in ultima luna.

   Modele:
   class Objective(models.Model):
       title = models.CharField(max_length=255)
       description = models.TextField()
       completed = models.BooleanField(default=False)
       date_added = models.DateField(auto_now_add=True)
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       image = models.ImageField(upload_to='objectives/', blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Objective: {self.title} - Completed: {self.completed}"

   class Badge(models.Model):
       name = models.CharField(max_length=100)
       description = models.TextField()
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Badge: {self.name} - User: {self.user.username}"

2. **Aplicatie Interactiva "Money Manager" - Gestiune Financiara Personala**
   - Pagini dinamice: Dashboard cu bugetul curent, Lista tranzactii, Categorii.
   - Utilizatorii autentificati pot adauga venituri si cheltuieli folosind CreateView.
   - Editarea si stergerea tranzactiilor existente cu UpdateView si DeleteView.
   - Vizualizarea detaliilor tranzactiilor (ex: data, suma, descriere) cu DetailView.
   - Formular cu validari: suma trebuie sa fie pozitiva si data sa nu fie in viitor.
   - Sistem complet de autentificare (register/login/logout).
   - Trimitere email cu un sumar al tranzactiilor si bugetului.
   - Context processor pentru a afisa balanta curenta a utilizatorului in navbar.

   Modele:
   class Category(models.Model):
       name = models.CharField(max_length=100)
       is_income = models.BooleanField(default=False)  # Venituri vs Cheltuieli
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Category: {self.name} - Type: {'Income' if self.is_income else 'Expense'}"

   class Transaction(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
       amount = models.DecimalField(max_digits=10, decimal_places=2)
       date = models.DateField()
       description = models.TextField(blank=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Transaction: {self.amount} - {self.category.name}"

3. **Sistem de review pentru produse**
   - Modele: Produs, Review.
   - Utilizatorii pot lasa review-uri doar daca sunt logati.
   - Email de multumire dupa ce un utilizator lasa un review.
   - Validari: scorul sa fie intre 1 si 5.
   - Media pentru poze ale produselor.

   Modele:
   class Product(models.Model):
       name = models.CharField(max_length=255)
       description = models.TextField()
       price = models.DecimalField(max_digits=10, decimal_places=2)
       image = models.ImageField(upload_to='products/', blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Product: {self.name} - Price: {self.price}"

   class Review(models.Model):
       product = models.ForeignKey(Product, on_delete=models.CASCADE)
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
       comment = models.TextField(blank=True)
       date_created = models.DateTimeField(auto_now_add=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Review: {self.rating} - {self.product.name} by {self.user.username}"

4. **Platforma de cursuri online**
   - Modele: Curs, Instructor, Student.
   - Instructorii pot adauga si modifica cursuri.
   - Studentii pot vizualiza cursurile si se pot inscrie.
   - Email de confirmare pentru inscrierea la un curs.
   - Static files pentru stiluri si materiale curs (ex: PDF-uri, poze, video-uri).
   - Context processor pentru a afisa cursurile populare.

   Modele:
    class Course(models.Model):
       title = models.CharField(max_length=255)
       description = models.TextField()
       instructor = models.ForeignKey(User, on_delete=models.CASCADE)
       start_date = models.DateField()
       end_date = models.DateField()
       price = models.DecimalField(max_digits=10, decimal_places=2)
       materials = models.FileField(upload_to='courses/', blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Course: {self.title} - Instructor: {self.instructor.username}"

   class Enrollment(models.Model):
       student = models.ForeignKey(User, on_delete=models.CASCADE)
       course = models.ForeignKey(Course, on_delete=models.CASCADE)
       date_enrolled = models.DateTimeField(auto_now_add=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Enrollment: {self.student.username} - {self.course.title}"

5. **Aplicatie de gestionare a cheltuielilor personale**
   - Modele: Cheltuiala, Categorie.
   - Utilizatorii pot urmari cheltuielile si veniturile lor.
   - Trimitere email lunar cu sumarul cheltuielilor.
   - Validari: suma trebuie sa fie pozitiva, data trebuie sa fie intr-un interval valid.
   - Context processor pentru a afisa suma totala cheltuita si bugetul disponibil.

   Modele:
   class Expense(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
       amount = models.DecimalField(max_digits=10, decimal_places=2)
       date = models.DateField()
       description = models.TextField(blank=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Expense: {self.amount} - {self.category.name} on {self.date}"

   class Income(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       amount = models.DecimalField(max_digits=10, decimal_places=2)
       date = models.DateField()
       description = models.TextField(blank=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Income: {self.amount} on {self.date}"

6. **Aplicatie de tip blog cu sistem de comentarii**
   - Modele: Articol, Comentariu, Autor.
   - Vizitatorii pot citi articolele, iar utilizatorii logati pot comenta.
   - Email catre autor cand un comentariu nou este postat.
   - Validari: campuri obligatorii pentru comentarii, lungime minima.
   - Static files pentru stilizarea articolelor si imagini.
   - Context processor pentru a afisa ultimele 5 articole publicate.

   Modele:
   class Article(models.Model):
       title = models.CharField(max_length=255)
       content = models.TextField()
       author = models.ForeignKey(User, on_delete=models.CASCADE)
       date_published = models.DateTimeField(auto_now_add=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Article: {self.title} - By {self.author.username}"

   class Comment(models.Model):
       article = models.ForeignKey(Article, on_delete=models.CASCADE)
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       text = models.TextField()
       date_posted = models.DateTimeField(auto_now_add=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Comment by {self.user.username} on {self.article.title}"
