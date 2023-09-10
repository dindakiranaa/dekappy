TUGAS 2

Nama    : Dinda Kirana Khairunnisa
NPM     : 2206082480
Kelas   : PBP - C

Link aplikasi Adaptable → https://dekappy.adaptable.app/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

-> Membuat sebuah proyek Django baru
Pada checklist ini, saya memulainya dari membuat folder bernama dekappy dan melakukan inisiasi repositori di GitHub. Setelah melakukan inisiasi, step berikutnya adalah menghubungkan repositori dekappy dengan repositori di Github. Untuk menghubungkannya dapat dimulai dengan membuat branch utama.

git branch -M main

Saya ingin membuat branch dengan nama branchnya adalah main. Oleh karena itu pada command diatas saya memasukkan main sebagai nama branch. Setelah branch dibuat, saya  menghubungkan repositori dekappy dengan repository di Github menggunakan perintah berikut :

git remote add origin https://github.com/dindakiranaa/dekappy.git

Command diatas bertujuan untuk membuat koneksi antara repository dekappy dan repository di Github sehingga dapat mengirim atau mengambil perubahan antara keduanya. Setelah itu, saya membuat virtual environment di dalam direktori utama dengan menjalankan command berikut di command prompt

python -m venv env

command tersebut digunakan untuk membuat lingkungan terpisah yang dapat digunakan untuk mengembangkan proyek tanpa mempengaruhi proyek lain. Setelah virtual environment dibuat, saya mengaktifkannya dengan menjalankan command :

env\Scripts\activate.bat

Step berikutnya adalah membuat dependencies supaya pengembangan aplikasi dapat berjalan dengan baik. Pembuatan dependencies dimulai dengan membuat file requirements.txt dan menambahkan komponen-komponen yang diperlukan, yaitu:

django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3

Setelah itu, dependencies dipasang dengan menjalankan command berikut

pip install -r requirements.txt

Kemudian, saya membuat proyek Django bernama dekappy dengan menjalankan command:

django-admin startproject dekappy .

Langkah selanjutnya adalah mengubah daftar host yang ada pada settings.py menjadi "*" yang berarti memberikan akses ke semua host.Kemudian, saya menjalankan server Django dengan command berikut.

python manage.py runserver

Setelah command tersebut dijalankan, proyek Django sudah terbuat.

-> Membuat aplikasi dengan nama main pada proyek tersebut.
Langkah pertama dalam checklist ini adalah mengaktifkan virtual environment. Kemudian saya menjalankan command berikut ini untuk membuat sebuah aplikasi baru dengan nama main di dalam proyek dekappy. Aplikasi tersebut berfungsi untuk menghandle bagian khusus dari proyek seperti halaman web, tampilan, dan model. 

python manage.py startapp main

Setelah itu, saya menambahkan 'main' ke dalam variable INSTALLED_APPS untuk mendaftarkan aplikasi main yang baru saja saya buat sebelumnya.

--> Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Pada checklist ini, saya akan melakukan konfigurasi rute URL proyek untuk menghubungkannya ke tampilan aplikasi. Konfigurasi tersebut dimulai dari import fungsi path dan include di file urls.py yang ada di dalam direktori proyek. Kemudian saya menambahkan rute url pada variabel urlpatterns.

path('main/', include('main.urls'))

'main' pada parameter pertama di fungsi path adalah pola URL yang akan dipantau. Kemudian fungsi include('main.urls') bertujuan untuk menghubungkan pola URL ini ke berkas konfigurasi URL di dalam aplikasi.


→ Membuat model pada aplikasi main dengan nama Item
Langkah pertama pada checklist ini adalah membuat class di dalam berkas model.py yang terdapat di dalam direktori aplikasi untuk membuat model.

class Item(models.Model):
    name = models.CharField(max_length=255)
    items = models.IntegerField()
    price= models.IntegerField()
    description = models.TextField()

Kemudian, saya melakukan migrasi model untuk melacak perubahan pada model dengan menjalankan command berikut.

python manage.py makemigrations

Command di atas bertujuan untuk menciptakan berkas migrasi yang berisi perubahan yang perlu dilakukan pada database.

python manage.py migrate

Command di atas bertujuan untuk menerapkan perubahan yang ada pada berkas migrasi sebelumnya ke dalam database.

→ Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Checklist ini saya mulai dengan membuat direktori templates di dalam direktori aplikasi. Dalam direktori tersebut, saya akan membuat berkas bernama main.html dimana pada berkas tersebut saya akan akan menambahkan nama aplikasi dan nama serta kelas saya.

Setelah membuat template, langkah berikutnya adalah membuat fungsi pada views.py. Pembuatan fungsi ini dimulai dari membuka file views.py dan menambahkan fungsi show_maiin.

def show_main(request):
    context = {
        'appname' : 'DEKAPPY',
        'name': 'Dinda Kirana Khairunnisa',
        'class': 'PBP C',
    }

    return render(request, "main.html", context)

Pada kode diatas, terdapat variabel bernama context dengan tipe nya adalah dictionary, Context bertujuan untuk mengirimkan data yang berisi nama aplikasi serta nama dan kelas saya ke tampilan. Kemudian saya mengembalikan fungsi tersebut dengan memanggil fungsi render yang bertujuan untuk me-render tampilan main.html. Pada berkas main.html, saya menggunakan syntax Django {{ }} untuk menampilkan nilai dari variabel yang ada pada context.

→ Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Checklist ini dimulai dengan membuat file  urls.py di dalam direktori aplikasi. Dalam urls.py ini, saya mengimport dua fungsi yaitu:

from django.urls import path # import fungsi path dari modul django.urls untuk mengkonfigurasi pola URL yang ada di aplikasi Django

from main.views import show_main # import fungsi 'show_main' yang digunakan untuk menghandle request HTTP pada URL tertentu

setelah import dua fungsi diatas, saya mendefinisikan variabel 'app_name' dan mengisi variabel tersebut dengan 'main'. Hal tersebut bertujuan untuk mengidentifikasi aplikasi dalam proyek. Kemudian, saya mendefinisikan juga variabel 'urlpatterns', dimana variabel tersebut menentukan bagaimana URL di-handle oleh aplikasi main. Pada variabel urlpatterns, saya menggunakan fungsi path yang sebelumnya sudah saya import.

urlpatterns = [
    path('', show_main, name='show_main'),
]

→ Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Checklist ini diawali dengan melakukan add, commit, dan push ke repository terlebih dahulu. Kemudian, saya akan log in ke akun Adaptable saya yang connect dengan akun Github saya. Selanjutnya saya memilih repository proyek saya yaitu dekappy sebagai basis aplikasi. Lalu, saya memilih branch main sebagai deployment branch.
Pada pemilihan template deployment, saya menggunakan Python App Template dan memilih PostgreSQL sebagai database yang akan saya gunakan. Selanjutnya, pada python settings, saya memilih versi 3.10 dan menambahkan command berikut ke dalam Start Command

python manage.py migrate && gunicorn dekappy.wsgi

Setelah itu, saya menamakan aplikasi saya ‘Dekappy’ dan klik Deploy App untuk melakukan deployment aplikasi. 

→Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
Pada checklist ini, saya membuat berkas README.md di dalam direktori utama. Dalam berkas README.md tersebut saya isi dengan link adaptable saya dan jawaban dari pertanyaan-pertanyaan yang ada pada soal. Setelah itu, saya melakukan git add, commit, dan push.

2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Ketika client mengirim request ke web aplikasi berbasis Django, Django akan mencocokkan URL yang dikirim oleh client dengan pola URL yang telah didefinisikan dalam berkas ‘urls.py‘. Pola URL tersebut adalah aturan yang menghubungkan URL dengan View yang akan menanganinya. 
Jika Django menemukan pola yang cocok, komponen view akan memproses request tersebut, mengambil data dari model, dan merender template yang sesuai. View dapat berupa fungsi atau kelas, tergantung pada bagaimana kita menulis view kita. Kita menulis view kita di dalam berkas ‘views.py’ sebagai titik hubungan antara model dan template.
Dalam berkas ‘models.py’ akan berisi data yang diperlukan untuk request tersebut. Data-data dalam berkas ‘models.py’ akan digunakan oleh ‘views.py’ untuk mengambil, memanipulasi, dan menyimpan data dalam database.
Berkas HTML akan digunakan untuk menghasilkan tampilan halaman web yang akan diberikan kepada pengguna. Berkas HTML akan digunakan oleh ‘views.py’ untuk merender tampilan yang akan ditampilkan kepada pengguna dengan menggabungkan data dari ‘models.py’ .



3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment merupakan tools yang penting ketika mengembangkan aplikasi web berbasis Django. Dengan virtual environment, kita dapat mengelola dependensi dengan mudah dan menghindari konflik antara perbedaan versi pada libraries dan packages. Selain itu, kita dapat memastikan bahwa proyek Django kita terisolasi dan mudah untuk dilakukan maintenance. Walaupun virtual environment merupakan tools yang penting, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Jika kita ingin membuat aplikasi tanpa virtual environment, kita dapat melakukannya dengan melakukan instalasi libraries secara global. Namun, langkah tersebut tidak disarankan karena adanya kemungkinan error akibat perbedaan versi Django yang digunakan. Oleh karena itu, pembuatan aplikasi web berbasis Django akan lebih mudah jika kita menggunakan virtual environment karena kita dapat memanage package proyek kita dengan mudah. 


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Dikutip dari Geeksforgeeks, MVC merupakan singkatan dari Model-View-Controller, yaitu sebuah framework atau pola desain arsitektur yang memisahkan sebuah aplikasi menjadi tiga komponen utama, yaitu Model, View, dan Controller. Setiap komponen dibangun untuk mengelola aspek pengembangan tertentu dari sebuah aplikasi. Komponen model adalah komponen yang berkaitan dengan semua logika terkait data yang digunakan pengguna. Model berinteraksi dengan database dan memberikan data yang dibutuhkan kembali ke komponen controller. Komponen berikutnya adalah Controller, yaitu penghubung antara view dan model. Komponen ini memproses semua logika bisnis dan request yang masuk, memanipulasi data menggunakan komponen model, dan berinteraksi dengan komponen view untuk menampilkan hasil akhir. Komponen berikutnya adalah komponen view dimana komponen ini digunakan untuk menciptakan user interface kepada penggunanya. Komponen view dibentuk oleh data yang dikumpulkan oleh komponen model, tetapi data tersebut tidak diakses secara langsung melainkan melalui komponen controller

Struktur proyek berikutnya adalah Model-View-Template atau disingkat dengan MVT. MVT merupakan software design pattern yang digunakan untuk mengembangkan aplikasi web. MVT dibagi menjadi tiga komponen. Yang pertama adalah model yang berfungsi untuk mengelola database dan menjaga data. Komponen berikutnya adalah view yang digunakan untuk menjalankan logika bisnis dan berinteraksi dengan model untuk mengambil data serta menampilkan template. Komponen terakhir adalah template yang berfungsi untuk mengurus seluruh bagian interface pengguna dengan detail. 

Berdasarkan artikel Builtin dengan judul What Is MVVM Architecture?, MVVM atau Model-View-ViewModel merupakan software design pattern yang memisahkan logika bisnis aplikasi dari interface pengguna. Tujuan utama dari MVVM ini adalah membuat tampilan sepenuhnya independen dari logika aplikasi. Komponen model mencakup model data dan logika bisnis serta validasi. Model berkomunikasi dengan ViewModel, tetapi tidak memiliki informasi mengenai view. Komponen view mewakili interface pengguna aplikasi dan hanya memiliki logika presentasi yang terbatas untuk mengimplementasikan perilaku visual. Komponen ViewModel adalah penghubung antara view dan model. Komponen ini mengimplementasikan dan mengekspos properti dan perintah yang digunakan oleh view melalui ikatan data. 

Berdasarkan penjelasan pada paragraf-paragraf sebelumnya, terdapat beberapa perbedaan antara MVC, MVT, dan MVVM. Perbedaan yang pertama adalah dari segi pola arsitektur dasarnya. MVC memisahkan aplikasi menjadi Model, View, dan Controller. MVT yang biasa digunakan oleh Django, membagi aplikasi menjadi Model, View, dan Template. Sedangkan MVVM memisahkan aplikasi menjadi Model, View, dan ViewModel. Perbedaan berikutnya adalah hubungan dan aliran data.  Pada MVC, komponen View dan Controller terikat erat satu sama lain. Hal tersebut berarti bahwa tampilan dan cara aplikasi berinteraksi dengan data sangat tergantung satu sama lain. View mengirim permintaan ke Controller dan controller mengelola aliran data antara model dan view. Sedangkan, MVVM lebih berfokus pada peristiwa (event-driven) karena menggunakan ikatan data (data binding). Hal ini membuat pemisahan logika bisnis inti dari View menjadi lebih mudah. MVT memiliki pola yang sedikit mirip dengan MVC, yaitu sama-sama menggunakan controller untuk mengatur aliran data antara model dan view. Akan tetapi, dalam MVT, komponen View yang bertanggung jawab dalam mengelola permintaan dari pengguna dan berinteraksi dengan controller untuk mengatur aliran data antara model dan view. 

