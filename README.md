# Test Project Thinkland

Bu loyiha **Django + Docker + PostgreSQL** asosida qurilgan.  
Loyihada `apps/`, `core/`, `media/`, `envs/` kabi asosiy papkalar mavjud.  

---

## 📦 O‘rnatish

### 1. Repository-ni clone qilish
```bash
git clone <repo-url>
cd test_project_thinkland
```

### 2. env faylini to'ldirish
```bash
cp envs/.env.django.example envs/.env.django
cp envs/.env.database.example envs/.env.database
```

### 3. Docker orqali containerlarni ishlash
```bash
docker-compose up --build -d
```

### 4. Elasticsearch-indexlarni qo'shish
```bash
docker-compose exec web python manage.py search_index --rebuild
```



