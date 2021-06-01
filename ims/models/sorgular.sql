-- SQLite

-- bir ürünün en son alınan tarihi

select * 
from 'Ürün Hareketleri' 
where urun_id_id = 3
order by tarih desc
limit 1;

-- kullanıcının son aldıkları

select *
from 'ÜrünlerGrup Bilgileri' as ug
INNER JOIN 'Ürün Hareketleri' as uh on ug.id = uh.urun_id_id
where (mudurluk, grup) In (  select mudurluk, grup
                    from Personeller 
                    where isno = 22222);

-- kullanıcının her ürün için o ürünü son aldığı tarih

select ug.id, ug.isim, ug.istihkak, ug.grup, ug.mudurluk, uh.tarih, uh.per_isno_id, ug.id
from 'ÜrünlerGrup Bilgileri' as ug
left join 'Ürün Hareketleri' as uh on ug.id = uh.urun_id_id
        and uh.id = (
                select uhs.id 
                from 'Ürün Hareketleri' as uhs 
                where uhs.urun_id_id = uh.urun_id_id and uhs.per_isno_id = 22222
                order by uhs.tarih desc
                limit 1)
where (mudurluk, grup) In (  select mudurluk, grup
                    from Personeller 
                    where isno = 22222);

-- kullanıcının bağlı olduğu müdürlüğün alabileceği ürünler

select *
from 'ÜrünlerGrup Bilgileri'
where (mudurluk, grup) In (  select mudurluk, grup
                    from Personeller 
                    where isno = 22222);

-- kullanıcının alabileceği ürünler (adet bakılmaksızın)

select ug.id, ug.isim, ug.istihkak, ug.grup, ug.mudurluk
from 'ÜrünlerGrup Bilgileri' as ug
left join 'Ürün Hareketleri' as uh on ug.id = uh.urun_id_id
        and uh.id = (
                select uhs.id 
                from 'Ürün Hareketleri' as uhs 
                where uhs.urun_id_id = uh.urun_id_id and uhs.per_isno_id = 22222
                order by uhs.tarih desc
                limit 1)
where (mudurluk, grup) In ( select mudurluk, grup
                            from Personeller 
                            where isno = 22222)
        and (uh.per_isno_id is null
        or ug.frekans <= cast(julianday('now') - julianday(uh.tarih) as integer));


-- kullanıcının alabileceği ürünler (adet bakılmaksızın) / (selectlerin düzelmiş hali)
 
select ug.id, ug.isim, ug.istihkak, i.ds, m.ds
from 'ÜrünlerGrup Bilgileri' as ug
inner join İstihkak as i on i.grup = ug.grup
inner join Müdürlükler m on m.mudurluk = ug.mudurluk
left join 'Ürün Hareketleri' as uh on ug.id = uh.urun_id_id
        and uh.id = (
                select uhs.id 
                from 'Ürün Hareketleri' as uhs 
                where uhs.urun_id_id = uh.urun_id_id and uhs.per_isno_id = 22222
                order by uhs.tarih desc
                limit 1)
where (ug.mudurluk, ug.grup) In ( select mudurluk, grup
                            from Personeller  
                            where isno = 22222)
        and (uh.per_isno_id is null
        or ug.frekans <= cast(julianday('now') - julianday(uh.tarih) as integer));