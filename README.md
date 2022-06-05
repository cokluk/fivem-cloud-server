# Fivem Cloud Server Nedir?

Basit mantık olarak tek sunucuda birden fazla port ile mutlithreading kullanarak yaptığım bu sistemi daha önce nitrado.net'in kullandığını görmüştüm. Ucuz maliyetle
ve ortalama performans veren bu sistem eğer tamamlansaydı beta aşamasında sunucularınızı ücretsiz oluşturabilecek & yönetebilecektiniz.

# Neden Proje Sona Erdi?

Fivem desteklemediği için proje başlamadan bitti. Sistemi yaptıktan sonra öğrendim ki sadece Fivem bu sistemin kullanımını kısıtlayarak sadece "ZAP-Hosting"'e bu sistemi
kullanabilir kılmış. Ben de bu projeyi bu aşamaya gelince sistemin çalışmayacağını anlayarak projeyi sonlandırıp kaynak kodunu paylaşma kararı aldım. Umarım birilerinin işine yarar.

# Ne Nasıl Çalışıyor?

| Request  | Method | Require | Response |
| ------------- | ------------- | ------------- |  ------------- | 
| requestSlot  |  GET |  sv_licenseKey | Boş bir sunucu rezerve eder |
| stopServer  |  POST |  port | Portu kullanan threadları stoplar |

 

# Değişkenler

| Değişkenler  | Ne işe yaradıkları |
| ------------- | ------------- |
| ports  | Rezerve edilmiş portlar  |
| servers[port]  | Rezerve edilmiş sunucu Thread'ı  |
| min_port | Rezerve başlangıç portu  |
| max_port | Rezerve bitiş portu  |
| server_ip | Sunucu Ağ Adresi  |



# License
    Copyright (C) 2022 Salih ÇOKLUK

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>

