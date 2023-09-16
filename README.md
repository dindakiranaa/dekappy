<h1> TUGAS 2 </h1>

Nama    : Dinda Kirana Khairunnisa

NPM     : 2206082480

Kelas   : PBP - C

Link aplikasi Adaptable → https://dekappy.adaptable.app/

<hr>

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
    
    → Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
   
    Pada checklist ini, saya membuat berkas README.md di dalam direktori utama. Dalam berkas README.md tersebut saya isi dengan link adaptable saya dan jawaban dari pertanyaan-pertanyaan yang ada pada soal. Setelah itu, saya melakukan git add, commit, dan push.

<hr>

2.   Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![C:\Dinda\Kuliah\PBP\dekappy\Colorful Pastel Childish Handmade Scheme Concept Mind Map Graph.png](<Colorful Pastel Childish Handmade Scheme Concept Mind Map Graph.png>)

→ Ketika client mengirim request ke web aplikasi berbasis Django, Django akan mencocokkan URL yang dikirim oleh client dengan pola URL yang telah didefinisikan dalam berkas ‘urls.py‘. Pola URL tersebut adalah aturan yang menghubungkan URL dengan View yang akan menanganinya. 

→ Jika Django menemukan pola yang cocok, komponen view akan memproses request tersebut, mengambil data dari model, dan merender template yang sesuai. View dapat berupa fungsi atau kelas, tergantung pada bagaimana kita menulis view kita. Kita menulis view kita di dalam berkas ‘views.py’ sebagai titik hubungan antara model dan template.

→ Dalam berkas ‘models.py’ akan berisi data yang diperlukan untuk request tersebut. Data-data dalam berkas ‘models.py’ akan digunakan oleh ‘views.py’ untuk mengambil, memanipulasi, dan menyimpan data dalam database.

→ Berkas HTML akan digunakan untuk menghasilkan tampilan halaman web yang akan diberikan kepada pengguna. Berkas HTML akan digunakan oleh ‘views.py’ untuk merender tampilan yang akan ditampilkan kepada pengguna dengan menggabungkan data dari ‘models.py’ .

<hr>

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

   Virtual environment merupakan tools yang penting ketika mengembangkan aplikasi web berbasis Django. Dengan virtual environment, kita dapat mengelola dependensi dengan mudah dan menghindari konflik antara perbedaan versi pada libraries dan packages. Selain itu, kita dapat memastikan bahwa proyek Django kita terisolasi dan mudah untuk dilakukan maintenance. Walaupun virtual environment merupakan tools yang penting, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Jika kita ingin membuat aplikasi tanpa virtual environment, kita dapat melakukannya dengan melakukan instalasi libraries secara global. Namun, langkah tersebut tidak disarankan karena adanya kemungkinan error akibat perbedaan versi Django yang digunakan. Oleh karena itu, pembuatan aplikasi web berbasis Django akan lebih mudah jika kita menggunakan virtual environment karena kita dapat memanage package proyek kita dengan mudah. 

<hr>

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

   Dikutip dari Geeksforgeeks, MVC merupakan singkatan dari Model-View-Controller, yaitu sebuah framework atau pola desain arsitektur yang memisahkan sebuah aplikasi menjadi tiga komponen utama, yaitu Model, View, dan Controller. Setiap komponen dibangun untuk mengelola aspek pengembangan tertentu dari sebuah aplikasi. Komponen model adalah komponen yang berkaitan dengan semua logika terkait data yang digunakan pengguna. Model berinteraksi dengan database dan memberikan data yang dibutuhkan kembali ke komponen controller. Komponen berikutnya adalah Controller, yaitu penghubung antara view dan model. Komponen ini memproses semua logika bisnis dan request yang masuk, memanipulasi data menggunakan komponen model, dan berinteraksi dengan komponen view untuk menampilkan hasil akhir. Komponen berikutnya adalah komponen view dimana komponen ini digunakan untuk menciptakan user interface kepada penggunanya. Komponen view dibentuk oleh data yang dikumpulkan oleh komponen model, tetapi data tersebut tidak diakses secara langsung melainkan melalui komponen controller
   
    Struktur proyek berikutnya adalah Model-View-Template atau disingkat dengan MVT. MVT merupakan software design pattern yang digunakan untuk mengembangkan aplikasi web. MVT dibagi menjadi tiga komponen. Yang pertama adalah model yang berfungsi untuk mengelola database dan menjaga data. Komponen berikutnya adalah view yang digunakan untuk menjalankan logika bisnis dan berinteraksi dengan model untuk mengambil data serta menampilkan template. Komponen terakhir adalah template yang berfungsi untuk mengurus seluruh bagian interface pengguna dengan detail.
   Berdasarkan artikel Builtin dengan judul What Is MVVM Architecture?, MVVM atau Model-View-ViewModel merupakan software design pattern yang memisahkan logika bisnis aplikasi dari interface pengguna. Tujuan utama dari MVVM ini adalah membuat tampilan sepenuhnya independen dari logika aplikasi. Komponen model mencakup model data dan logika bisnis serta validasi. Model berkomunikasi dengan ViewModel, tetapi tidak memiliki informasi mengenai view. Komponen view mewakili interface pengguna aplikasi dan hanya memiliki logika presentasi yang terbatas untuk mengimplementasikan perilaku visual. Komponen ViewModel adalah penghubung antara view dan model. Komponen ini mengimplementasikan dan mengekspos properti dan perintah yang digunakan oleh view melalui ikatan data.
   
   Berdasarkan penjelasan pada paragraf-paragraf sebelumnya, terdapat beberapa perbedaan antara MVC, MVT, dan MVVM. Perbedaan yang pertama adalah dari segi pola arsitektur dasarnya. MVC memisahkan aplikasi menjadi Model, View, dan Controller. MVT yang biasa digunakan oleh Django, membagi aplikasi menjadi Model, View, dan Template. Sedangkan MVVM memisahkan aplikasi menjadi Model, View, dan ViewModel. Perbedaan berikutnya adalah hubungan dan aliran data.  Pada MVC, komponen View dan Controller terikat erat satu sama lain. Hal tersebut berarti bahwa tampilan dan cara aplikasi berinteraksi dengan data sangat tergantung satu sama lain. View mengirim permintaan ke Controller dan controller mengelola aliran data antara model dan view. Sedangkan, MVVM lebih berfokus pada peristiwa (event-driven) karena menggunakan ikatan data (data binding). Hal ini membuat pemisahan logika bisnis inti dari View menjadi lebih mudah. MVT memiliki pola yang sedikit mirip dengan MVC, yaitu sama-sama menggunakan controller untuk mengatur aliran data antara model dan view. Akan tetapi, dalam MVT, komponen View yang bertanggung jawab dalam mengelola permintaan dari pengguna dan berinteraksi dengan controller untuk mengatur aliran data antara model dan view. 

<h1> TUGAS 3 </h1>

1. Apa perbedaan antara form POST dan form GET dalam Django?
   
    Form POST digunakan ketika user ingin mengirim data dari form elements ke server web dengan menggunakan parameter URL. Cara tersebut lebih aman karena data tidak akan terlihat dalam URL sehingga lebih cocok untuk mengirimkan data sensitif atau ketika user perlu mengirimkan banyak informasi, seperti saat membuat, mengedit, atau menghapus entitas. Di sisi lain, form GET digunakan untuk mengambil data dari server tanpa membuat perubahan. Namun, data yang dikirimkan dengan GET dapat terlihat dalam URL sehingga menjadi kurang aman. Selain itu, GET juga dapat disimpan di dalam cache. 

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

   Extensible Markup Language atau biasa disebut dengan XML merupakan markup language dan file format yang digunakan untuk menyimpan, mengorganisasi, dan mengirim data secara struktural. Sedangkan, JSON adalah open standard file format yang menggunakan teks yang mudah dibaca oleh manusia sehingga dapat digunakan untuk berkomunikasi antara berbagai program dan aplikasi di internet. Selain itu, terdapat HTML yang digunakan untuk mendefinisikan struktur dan tampilan halaman web. 

    XML, JSON, dan HTML adalah tiga format populer untuk menyimpan dan bertukar data di web. Ketiga format tersebut memiliki struktur yang berbeda dan kelebihan masing-masing.   XML digunakan untuk menyimpan dan mengorganisasi data secara struktural, cocok untuk pertukaran data antara sistem. JSON, lebih mudah dibaca oleh manusia, digunakan untuk pertukaran data antara aplikasi web. HTML digunakan untuk mendefinisikan tampilan halaman web, menggambarkan konten yang ditampilkan di peramban web. 

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   
    JSON sering digunakan dalam pertukaran dara karena merupakan format data yang ringkas, mudah dibaca, dan mudah digunakan. JSON mendukung struktur data yang jelas dan membuatnya fleksibel dalam merepresentasikan informasi. Selain itu, JSON memiliki kompatibilitas yang luas dengan berbagai bahasa pemrograman dan sangat cocok digunakan untuk pengembangan web. 

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    ### Membuat input form untuk menambahkan objek model pada app sebelumnya.
    Checklist ini saya mulai dari pembuatan skeleton yang digunakan untuk merancang tampilan situs web. Fungsi utama dari skeleton ini adalah untuk memberikan landasan atau kerangka kerja awal yang memungkinkan pengembang untuk memastikan konsistensi dalam desain situs web yang sedang dibangun.

    Pertama, saya membuat folder bernama templates pada root folder dekappy, bukan folder dekappy yang dalam. Kemudian, saya membuat file bernama base.html yang berfungsi sebagai kerangka dasar dalam pengembangan web. Selanjutnya, saya akan menambahkan kode berikut sebagai value dari key ‘DIRS’ ke dalam variable TEMPLATES di file settings.py yang ada di dalam direktori aplikasi dekappy.

    ``` 'DIRS': [BASE_DIR / 'templates'], ```

    Kode tersebut bertujuan supaya base.html dapat terdeteksi sebagai berkas template. Kemudian, saya mengubah kode pada file main.html yang ada di dalam folder templates pada direktori main menjadi seperti berikut ini.

    ```
    {% extends 'base.html' %}

    {% block content %}
        <h1>{{ appname }}</h1>
        <h2>Name:</h2>
        <p><b>{{ name }}</b></p>
        <h2>Class: </h2>
        <p><b>{{ class }}</b></p>

        <hr/>

    {% endblock content %}
    ```

    Kode tambahan diatas bertujuan untuk meng-extend base.html supaya bisa menggunakan struktur dasar dari base.html. Kemudian terdapat block content yang diisi dengan konten dekappy untuk memisahkan tampilan umum dan tampilan khusus halaman-halaman berbeda dalam situs web.

    Setelah melakukan langkah yang diatas, saya akan membuat input form untuk menambahkan objek model. Langkah pertama adalah membuat file dengan nama forms.py di dalam direktori main. Kemudian saya mengisi forms.py dengan kode berikut.

    ```
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "items", "price", "description"]
    ```

    Variable fields akan saya isi dengan atribut yang saya gunakan yang ada di dalam model. 

    Langkah berikutnya adalah mengimpor beberapa fungsi berikut ke dalam file views.py yang ada di dalam folder main.

    ```
    from django.http import HttpResponseRedirect
    from main.forms import ItemForm
    from django.urls import reverse
    ```

    Line pertama bertujuan untuk mendirect request HTTP ke URL lain. Line kedua bertujuan untuk mengimport class ItemForm dari modul ‘forms’ yang berada di folder main. Kemudian, line ketiga bertujuan untuk mengimpor fungsi ‘reverse’ dari modul ‘urls; untuk menghasilkan URL berdasarkan nama URL yang telah ditentukan.

    Langkah berikutnya adalah membuat fungsi baru bernama ‘create_item’ di dalam file views.py untuk menghasilkan form yang dapat menambahkan data item secara otomatis.  Fungsi tersebut akan diisi dengan kode berikut ini. 

    ```
    def create_item(request):
    form = ItemForm(request.POST or None) // mengumpulkan data yang akan digunakan

    if form.is_valid() and request.method == "POST": // memeriksa apakah form valid dan request methodnya adalah metode POST
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form} // melewati data ke template yang akan digunakan untuk merender halaman web
    return render(request, "create_product.html", context)

    ```

    Setelah itu, saya menambahkan  kode berikut ke dalam fungsi ‘show_main’.

    ```
        items = Item.objects.all() // menyimpan seluruh object Item yang tersimpan di database
    ```

    Setelah itu saya menambahkan key baru ke dalam variable context bernama ‘item’ dengan valuenya adalah items yang sebelumnya sudah saya tambahkan.

    ### Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
    Setelah membuat fungsi create_item di checklist sebelumnya, saya membuat berkas HTML baru dengan nama create_item.html di folder templates pada direktori main. Kemudian saya menambahkan beberapa kode di dalam block content yang terdapat di main.html untuk menampilkan data produk.

    Langkah berikutnya adalah mengimpor fungsi HttpResponse yang berfungsi ke dalam folder views.py untuk menghasilkan response HTTP kepada klien dan Serializer yang berfungsi untuk mengelola konversi data dalam aplikasi Django menjadi format yang dapat di-serialize, terutama saat mentransfer data dalam aplikasi.

    Kemudian, saya membuat fungsi baru yang bernama show_xml dan menambah variabel baru dengan nama data dan me-return function HttpResponse seperti berikut.
    ```
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

    Setelah itu, saya membuat fungsi baru yang bernama ‘show_json’ untuk mengambil data dari model. Kemudian mengirimkannya sebaga respons HTTP dalam format json. Fungsi tersebut akan saya isi dengan code berikut. 

    ```
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    Langkah berikutnya adalah membuat fungsi baru dengan nama ‘show_xml_by_id’ untuk mengambil data produk spesifik berdasarkan ID yang diberikan dalam request HTTP. Fungsi ini mirip dengan fungsi show_xml sebelumnya. Namun, terdapat perubahan pada nilai variabel data yaitu sebagai berikut.
    ```
    data = Item.objects.filter(pk=id) // untuk mengambil produk dengan ID yang sesuai dari model ‘Item’ .
    ```
    Kemudian, saya membuat fungsi baru lagi dengan nama ‘show_json_by_id’ untuk mengambil data produk spesifik berdasarkan ID yang diberikan dalam request HTTP. Fungsi ini mirip dseperti fungsi show_json, tetapi ada perubahan pada variable data.

    ```
    data = Item.objects.filter(pk=id)
    ```

    ### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
    Pada langkah ini saya mulai dengan membuat routing URL untuk fungsi create_item. Saya mengimpor fungsi ‘create_item’ ke file urls.py yang berada di folder main dan menambahkan path url baru untuk mengakses fungsi ‘create_item’.

    ```
    path('create-item', create_item, name='create_item'),
    ```

    Langkah berikutnya adalah mengimpor fungsi show_xml ke dalam file urls.py. Setelah itu menambahkan path ke dalam variable urlpatterns seperti berikut.

    path('xml/', show_xml, name='show_xml'), 

    Kemudian, saya mengimpor fungsi show_json ke dalam file urls.py yang ada pada folder main. Setelah itu, saya menambah path baru ke variable urlpatterns seperti sebelumnya. 

    path('json/', show_json, name='show_json'), 

    Setelah itu, saya juga mengimpor fungsi show_xml_by_id dan show_json_by_id ke dalam file urls.py. Kemudian saya menambahkan path baru ke dalam variable urlpatterns.
    ```
    path('xml/<int:id>/', show_xml_by_id. name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ```
    
    ### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
    Fungsi create_item :
    ![image](https://github.com/dindakiranaa/dekappy/assets/124904747/9d46763f-083c-4dfb-ad99-9c5550fa93e3)
    ![image](https://github.com/dindakiranaa/dekappy/assets/124904747/0f03cc3c-ed63-4575-a446-36ea84f98ea5)
    ![image](https://github.com/dindakiranaa/dekappy/assets/124904747/bf247f17-56ac-439a-b68b-36b26bea53b1)


    Fungsi show_xml :
    ![image](https://github.com/dindakiranaa/dekappy/assets/124904747/c068e2ad-21e8-43e1-90d2-21955a1683a3)

    Fungsi show_json :
    ![image](https://github.com/dindakiranaa/dekappy/assets/124904747/b09d1ebe-455b-4c00-a34b-a9aae31fc508)


    Fungsi show_xml_by_id dengan index 1 :
    ![image](https://github.com/dindakiranaa/dekappy/assets/124904747/7d10e193-b583-4135-8106-5e29036e453e)


    Fungsi show_json_by_id dengan index 1:
    ![image](https://github.com/dindakiranaa/dekappy/assets/124904747/2e9abfa8-b87d-4922-a69e-40dc42037f9d)

    ###  Melakukan add-commit-push ke GitHub.
    Setelah melakukan langkah-langkah diatas, saya melakukan git add dengan memasukan command ```git add . ``` kemudian saya melakukan commit dengan pesan update. Setelah itu, saya melakukan git push dengan menjalankan command ```git push -u origin main```.
