from django.db import models


class Chefe(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='chefes/')
    info_chefe = models.TextField()
    skills = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Npc(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='npcs/')
    funcao = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Exploracao(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='exploração/', blank=True)
    chefes = models.ManyToManyField(Chefe, blank=True)
    npcs = models.ManyToManyField(Npc, blank=True)

    def __str__(self):
        return self.nome


class Amuleto(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='amuletos/')
    efeito = models.TextField()
    custo = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Mascara(models.Model):
    img = models.ImageField(upload_to='mascaras/')
    fragmentos_necessarios = models.PositiveIntegerField()
    aumenta_vida = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.fragmentos_necessarios} fragmentos (+{self.aumenta_vida} vida)"


class Recipiente(models.Model):
    img = models.ImageField(upload_to='recipientes/')
    fragmentos_necessarios = models.PositiveIntegerField()
    soul = models.PositiveIntegerField(help_text="Quantidade de alma que esse recipiente fornece")

    def __str__(self):
        return f"{self.fragmentos_necessarios} fragmentos (+{self.soul} alma)"


class PaleOre(models.Model):
    img = models.ImageField(upload_to='pale_ores/')

    def __str__(self):
        return "Pale Ore"


class Feitico(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='feiticos/')
    efeito = models.TextField()
    custo = models.CharField(max_length=50)
    localizacao = models.TextField()

    def __str__(self):
        return self.nome


class ArteDoFerrao(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='artes_do_ferrao/')
    efeito = models.TextField()
    mestre = models.ForeignKey(Npc, on_delete=models.CASCADE)
    localizacao = models.TextField()

    def __str__(self):
        return self.nome

class Skill(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='skills/')
    efeito = models.TextField()
    localizacao = models.TextField()
    observacao = models.TextField()
    
    def __str__(self):
        return self.nome

class MiniChefe(models.Model):
    nome = models.CharField(max_length=100)
    img = models.ImageField(upload_to='minichefes/')
    local = models.TextField()
    dica = models.TextField()
    recompensa = models.TextField()

    def __str__(self):
        return self.nome

class InimigoComum(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.TextField()
    dificuldade = models.TextField()
    drop_em_geos = models.TextField()

    def __str__(self):
        return self.nome
