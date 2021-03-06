INSERT INTO `entity_definition` (`keyname`, `public_path`, `estonian_label`, `estonian_label_plural`, `estonian_description`, `estonian_menu`, `estonian_public`, `estonian_displayname`, `estonian_displayinfo`, `estonian_displaytable`, `estonian_sort`, `actions_add`)
VALUES
    ('acceptance-report', NULL, 'Vastuvõtuakt', 'Vastuvõtuaktid', NULL, 'Raamatukogu', NULL, '@number@ @issuer@', '@date@', '@number@|@issuer@|@date@', NULL, NULL),
    ('audiovideo', 'library', 'Auvis', 'Auvised', NULL, 'Raamatukogu', 'Raamatukogu', '@title@', '@subtitle@', '@title@|@author@|@ publishing-date@', '@name@', 'ester'),
    ('book', 'library', 'Raamat', 'Raamatud', NULL, 'Raamatukogu', 'Raamatukogu', '@title@', '@subtitle@', '@title@|@author@|@ publishing-date@', '@name@', 'ester'),
    ('class', NULL, 'Klass', 'Klassid', NULL, 'Seaded', NULL, '@number@@letter@', NULL, '@number@@letter@|@description@', '@number@@letter@', NULL),
    ('copy', NULL, 'Eksemplar', 'Eksemplarid', NULL, NULL, NULL, '@barcode@', '@inventory-number@', '@barcode@|@inventory-number@', '@name@', NULL),
    ('department', NULL, 'Osakond', 'Osakonnad', NULL, 'Seaded', NULL, '@name@', NULL, NULL, '@name@', NULL),
    ('gender', NULL, 'Sugu', 'Sood', NULL, NULL, NULL, '@name@', NULL, NULL, NULL, NULL),
    ('institution', NULL, 'Asutus', 'Asutused', NULL, 'Seaded', NULL, '@name@', NULL, NULL, '@name@', NULL),
    ('lending', NULL, 'Laenutus', 'Laenutused', NULL, 'Raamatukogu', NULL, '@lender@ * @item@', '@lending-date@…@returning-date@) @returned-date@', '@lender@|@item@|@lending-date@|@returning-date@|@returned-date@', '@item@@returned-date@@lending-date@@returning-date@', 'ester'),
    ('library', NULL, 'Raamatukogu', 'Raamatukogud', NULL, 'Raamatukogu', NULL, '@name@', NULL, NULL, '@name@', NULL),
    ('methodical', 'library', 'Metoodika', 'Metoodika', 'Metoodiline kirjandus', 'Raamatukogu', 'Raamatukogu', '@title@', '@subtitle@', '@title@|@author@|@publishing-date@', '@name@', 'ester'),
    ('periodical', 'library', 'Perioodika', 'Perioodika', NULL, 'Raamatukogu', 'Raamatukogu', '@title@', '@subtitle@', '@title@|@author@|@ publishing-date@', '@name@', 'ester'),
    ('person', NULL, 'Persoon', 'Persoonid', NULL, 'Seaded', NULL, '@forename@ @surname@', '@user@', '@forename@ @surname@|@user@', '@forename@ @surname@', NULL),
    ('personal', NULL, 'Personal', 'Personal', NULL, 'Seaded', NULL, '@name@', NULL, NULL, '@name@', NULL),
    ('textbook', 'library', 'Õpik', 'Õpikud', NULL, 'Raamatukogu', 'Raamatukogu', '@title@', '@subtitle@', '@title@|@author@|@ publishing-date@', '@name@', 'ester'),
    ('workbook', 'library', 'Töövihik', 'Töövihikud', NULL, 'Raamatukogu', 'Raamatukogu', '@title@', '@subtitle@', '@title@|@author@|@ publishing-date@', '@name@', 'ester');


INSERT INTO `property_definition` (`keyname`, `entity_definition_keyname`, `dataproperty`, `datatype`, `defaultvalue`, `estonian_fieldset`, `estonian_label`, `estonian_label_plural`, `estonian_description`, `ordinal`, `multilingual`, `multiplicity`, `readonly`, `createonly`, `public`, `mandatory`, `search`, `propagates`, `autocomplete`, `classifying_entity_definition_keyname`)
VALUES
    ('acceptance-report-date', 'acceptance-report', 'date', 'date', NULL, NULL, 'Kuupäev', 'Kuupäevad', '', 3, 0, 1, 0, 0, 1, 1, 1, 0, 0, NULL),
    ('acceptance-report-issuer', 'acceptance-report', 'issuer', 'string', NULL, NULL, 'Väljaandja', 'Väljaandjad', '', 2, 0, 1, 0, 0, 1, 1, 1, 0, 0, NULL),
    ('acceptance-report-note', 'acceptance-report', 'note', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 4, 0, 1, 0, 0, 1, 1, 1, 0, 0, NULL),
    ('acceptance-report-number', 'acceptance-report', 'number', 'string', NULL, NULL, 'Number', 'Numbrid', '', 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, NULL),
    ('audiovideo-author', 'audiovideo', 'author', 'string', NULL, NULL, 'Autor', 'Autorid', '', 8, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-class', 'audiovideo', 'class', 'string', NULL, NULL, 'Klass', 'Klassid', '', 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-compiler', 'audiovideo', 'compiler', 'string', NULL, NULL, 'Koostaja', 'Koostajad', '', 52, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-designer', 'audiovideo', 'designer', 'string', NULL, NULL, 'Disainer', 'Disainerid', '', 53, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-dimensions', 'audiovideo', 'dimensions', 'string', NULL, NULL, 'Mõõdud', 'Mõõdud', '', 74, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-edition', 'audiovideo', 'edition', 'string', NULL, NULL, 'Väljalase', 'Väljalase', '', 25, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-editor', 'audiovideo', 'editor', 'string', NULL, NULL, 'Toimetaja', 'Toimetajad', '', 51, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-epilogue-author', 'audiovideo', 'epilogue-author', 'string', NULL, NULL, 'Järelsõna autor', 'Järelsõna autorid', '', 57, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-ester-id', 'audiovideo', 'ester-id', 'string', NULL, NULL, 'Ester ID', 'Ester ID', '', 1000, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-illustrator', 'audiovideo', 'illustrator', 'string', NULL, NULL, 'Illustraator', 'Illustraatorid', '', 55, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-isn', 'audiovideo', 'isn', 'string', NULL, NULL, 'IS*N', 'IS*N', '', 13, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('audiovideo-language', 'audiovideo', 'language', 'string', NULL, NULL, 'Keel', 'Keeled', '', 22, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-location', 'audiovideo', 'location', 'string', NULL, NULL, 'Asukoht/Riiul', 'Asukohad/Riiulid', '', 29, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-media', 'audiovideo', 'media', 'string', NULL, NULL, 'Andmekandja', 'Andmekandjad', '', 7, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-notes', 'audiovideo', 'notes', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 27, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('audiovideo-number', 'audiovideo', 'number', 'string', NULL, NULL, 'Number', 'Number', '', 6, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-original-language', 'audiovideo', 'original-language', 'string', NULL, NULL, 'Originaalkeel', 'Originaalkeeled', '', 23, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-pages', 'audiovideo', 'pages', 'string', NULL, NULL, 'Lehekülgi', 'Lehekülgi', '', 73, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-photographer', 'audiovideo', 'photographer', 'string', NULL, NULL, 'Fotograaf', 'Fotograafid', '', 56, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-picture', 'audiovideo', 'picture', 'file', NULL, NULL, 'Pilt', 'Pildid', '', 28, 0, 0, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('audiovideo-publisher', 'audiovideo', 'publisher', 'string', NULL, NULL, 'Kirjastus', 'Kirjastused', '', 10, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-publishing-date', 'audiovideo', 'publishing-date', 'string', NULL, NULL, 'Ilmumisaasta', 'Ilmumisaastad', '', 9, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-publishing-place', 'audiovideo', 'publishing-place', 'string', NULL, NULL, 'Ilmumiskoht', 'Ilmumiskohad', '', 11, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-series', 'audiovideo', 'series', 'string', NULL, NULL, 'Sari', 'Sarjad', '', 4, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-series-number', 'audiovideo', 'series-number', 'string', NULL, NULL, 'Number sarjas', 'Number sarjas', '', 5, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-subtitle', 'audiovideo', 'subtitle', 'string', NULL, NULL, 'Alapealkiri', 'Alapealkirjad', '', 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-tag', 'audiovideo', 'tag', 'string', NULL, NULL, 'Märksõna', 'Märksõnad', '', 26, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('audiovideo-title', 'audiovideo', 'title', 'string', NULL, NULL, 'Pealkiri', 'Pealkirjad', '', 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-translator', 'audiovideo', 'translator', 'string', NULL, NULL, 'Tõlkija', 'Tõlkijad', '', 54, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-type', 'audiovideo', 'type', 'string', NULL, NULL, 'Tüüp', 'Tüübid', '', 19, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('audiovideo-udc', 'audiovideo', 'udc', 'string', NULL, NULL, 'Liik', 'Liigid', '', 12, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-author', 'book', 'author', 'string', NULL, NULL, 'Autor', 'Autorid', '', 8, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-class', 'book', 'class', 'string', NULL, NULL, 'Klass', 'Klassid', '', 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-compiler', 'book', 'compiler', 'string', NULL, NULL, 'Koostaja', 'Koostajad', '', 52, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-designer', 'book', 'designer', 'string', NULL, NULL, 'Disainer', 'Disainerid', '', 53, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-dimensions', 'book', 'dimensions', 'string', NULL, NULL, 'Mõõdud', 'Mõõdud', '', 74, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-edition', 'book', 'edition', 'string', NULL, NULL, 'Väljalase', 'Väljalase', '', 25, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-editor', 'book', 'editor', 'string', NULL, NULL, 'Toimetaja', 'Toimetajad', '', 51, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-epilogue-author', 'book', 'epilogue-author', 'string', NULL, NULL, 'Järelsõna autor', 'Järelsõna autorid', '', 57, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-ester-id', 'book', 'ester-id', 'string', NULL, NULL, 'Ester ID', 'Ester ID', '', 1000, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-illustrator', 'book', 'illustrator', 'string', NULL, NULL, 'Illustraator', 'Illustraatorid', '', 55, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-isn', 'book', 'isn', 'string', NULL, NULL, 'IS*N', 'IS*N', '', 13, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('book-language', 'book', 'language', 'string', NULL, NULL, 'Keel', 'Keeled', '', 22, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-location', 'book', 'location', 'string', NULL, NULL, 'Asukoht/Riiul', 'Asukohad/Riiulid', '', 29, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-media', 'audiovideo', 'media', 'string', NULL, NULL, 'Andmekandja', 'Andmekandjad', '', 7, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-notes', 'book', 'notes', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 27, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('book-number', 'book', 'number', 'string', NULL, NULL, 'Number', 'Number', '', 6, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-original-language', 'book', 'original-language', 'string', NULL, NULL, 'Originaalkeel', 'Originaalkeeled', '', 23, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-pages', 'book', 'pages', 'string', NULL, NULL, 'Lehekülgi', 'Lehekülgi', '', 73, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-photographer', 'book', 'photographer', 'string', NULL, NULL, 'Fotograaf', 'Fotograafid', '', 56, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-picture', 'book', 'picture', 'file', NULL, NULL, 'Pilt', 'Pildid', '', 28, 0, 0, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('book-publisher', 'book', 'publisher', 'string', NULL, NULL, 'Kirjastus', 'Kirjastused', '', 10, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-publishing-date', 'book', 'publishing-date', 'string', NULL, NULL, 'Ilmumisaasta', 'Ilmumisaastad', '', 9, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-publishing-place', 'book', 'publishing-place', 'string', NULL, NULL, 'Ilmumiskoht', 'Ilmumiskohad', '', 11, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-series', 'book', 'series', 'string', NULL, NULL, 'Sari', 'Sarjad', '', 4, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-series-number', 'book', 'series-number', 'string', NULL, NULL, 'Number sarjas', 'Number sarjas', '', 5, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-subtitle', 'book', 'subtitle', 'string', NULL, NULL, 'Alapealkiri', 'Alapealkirjad', '', 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-tag', 'book', 'tag', 'string', NULL, NULL, 'Märksõna', 'Märksõnad', '', 26, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('book-title', 'book', 'title', 'string', NULL, NULL, 'Pealkiri', 'Pealkirjad', '', 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-translator', 'book', 'translator', 'string', NULL, NULL, 'Tõlkija', 'Tõlkijad', '', 54, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-type', 'book', 'type', 'string', NULL, NULL, 'Tüüp', 'Tüübid', '', 19, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('book-udc', 'book', 'udc', 'string', NULL, NULL, 'Liik', 'Liigid', '', 12, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('class-letter', 'class', 'letter', 'string', NULL, NULL, 'Täht', 'Tähed', '', 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('class-notes', 'class', 'notes', 'string', NULL, NULL, 'Märkused', 'Märkused', '', 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('class-number', 'class', 'number', 'integer', NULL, NULL, 'Number', 'Number', '', 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('copy-barcode', 'copy', 'barcode', 'string', NULL, NULL, 'Võõtkood', 'Võõtkoodidi', '', 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, NULL),
    ('copy-date-added', 'copy', 'date-added', 'date', NULL, NULL, 'Sissekandekuupäev', 'Sissekandekuupäevad', '', 6, 0, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('copy-document', 'copy', 'document', 'file', NULL, NULL, 'Dokument/Arve', 'Dokumendid/Arved', '', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL),
    ('copy-inventory-number', 'copy', 'inventory-number', 'string', NULL, NULL, 'Inventari number', 'Inventari numbrid', '', 2, 0, 1, 0, 1, 0, 1, 1, 0, 0, NULL),
    ('copy-notes', 'copy', 'notes', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, NULL),
    ('copy-number', 'copy', 'number', 'string', NULL, NULL, 'Number', 'Numbrid', '', 2, 0, 1, 0, 1, 0, 1, 1, 0, 0, NULL),
    ('copy-price', 'copy', 'price', 'decimal', NULL, NULL, 'Hind', 'Hinnad', '', 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, NULL),
    ('department-description', 'department', 'description', 'text', NULL, NULL, 'Kirjeldus', 'Kirjeldused', '', 2, 1, 1, 0, 0, 0, 0, 1, 0, 0, NULL),
    ('department-name', 'department', 'name', 'string', NULL, NULL, 'Nimi', 'Nimed', '', 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('gender-name', 'gender', 'name', 'string', NULL, NULL, 'Nimi', 'Nimed', '', 1, 1, NULL, 0, 0, 1, 0, 0, 0, 0, NULL),
    ('institution-description', 'institution', 'description', 'text', NULL, NULL, 'Kirjeldus', 'Kirjeldused', '', 2, 1, 1, 0, 0, 0, 0, 1, 0, 0, NULL),
    ('institution-name', 'institution', 'name', 'string', NULL, NULL, 'Nimi', 'Nimed', '', 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('lending-item', 'lending', 'item', 'reference', NULL, NULL, 'Teavik', 'Teavikud', '', 1, 0, 2, 0, 0, 0, 1, 1, 0, 0, 'copy'),
    ('lending-lending-date', 'lending', 'lending-date', 'date', NULL, NULL, 'Laenutuskuupäev', 'Laenutuskuupäevad', '', 3, 0, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('lending-note', 'lending', 'note', 'text', NULL, NULL, 'Märkus', 'Märkused', '', 6, 0, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('lending-person', 'lending', 'person', 'reference', NULL, NULL, 'Laenutaja', 'Laenutajad', '', 2, 0, 1, 0, 0, 0, 1, 1, 0, 0, 'person'),
    ('lending-returned-date', 'lending', 'returned-date', 'date', NULL, NULL, 'Tagastatud', 'Tagastatud', '', 5, 0, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('lending-returning-date', 'lending', 'returning-date', 'date', NULL, NULL, 'Tagastuskuupäev', 'Tagastuskuupäevad', '', 4, 0, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('library-description', 'library', 'description', 'text', NULL, NULL, 'Kirjeldus', 'Kirjeldused', '', 2, 1, 1, 0, 0, 0, 0, 1, 0, 0, NULL),
    ('library-name', 'library', 'name', 'string', NULL, NULL, 'Nimi', 'Nimed', '', 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('methodical-author', 'methodical', 'author', 'string', NULL, NULL, 'Autor', 'Autorid', '', 8, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-class', 'methodical', 'class', 'string', NULL, NULL, 'Klass', 'Klassid', '', 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-compiler', 'methodical', 'compiler', 'string', NULL, NULL, 'Koostaja', 'Koostajad', '', 52, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-designer', 'methodical', 'designer', 'string', NULL, NULL, 'Disainer', 'Disainerid', '', 53, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-dimensions', 'methodical', 'dimensions', 'string', NULL, NULL, 'Mõõdud', 'Mõõdud', '', 74, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-edition', 'methodical', 'edition', 'string', NULL, NULL, 'Väljalase', 'Väljalase', '', 25, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-editor', 'methodical', 'editor', 'string', NULL, NULL, 'Toimetaja', 'Toimetajad', '', 51, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-epilogue-author', 'methodical', 'epilogue-author', 'string', NULL, NULL, 'Järelsõna autor', 'Järelsõna autorid', '', 57, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-ester-id', 'methodical', 'ester-id', 'string', NULL, NULL, 'Ester ID', 'Ester ID', '', 1000, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-illustrator', 'methodical', 'illustrator', 'string', NULL, NULL, 'Illustraator', 'Illustraatorid', '', 55, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-isn', 'methodical', 'isn', 'string', NULL, NULL, 'IS*N', 'IS*N', '', 13, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('methodical-language', 'methodical', 'language', 'string', NULL, NULL, 'Keel', 'Keeled', '', 22, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-location', 'methodical', 'location', 'string', NULL, NULL, 'Asukoht/Riiul', 'Asukohad/Riiulid', '', 29, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-media', 'audiovideo', 'media', 'string', NULL, NULL, 'Andmekandja', 'Andmekandjad', '', 7, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-notes', 'methodical', 'notes', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 27, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('methodical-number', 'methodical', 'number', 'string', NULL, NULL, 'Number', 'Number', '', 6, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-original-language', 'methodical', 'original-language', 'string', NULL, NULL, 'Originaalkeel', 'Originaalkeeled', '', 23, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-pages', 'methodical', 'pages', 'string', NULL, NULL, 'Lehekülgi', 'Lehekülgi', '', 73, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-photographer', 'methodical', 'photographer', 'string', NULL, NULL, 'Fotograaf', 'Fotograafid', '', 56, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-picture', 'methodical', 'picture', 'file', NULL, NULL, 'Pilt', 'Pildid', '', 28, 0, 0, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('methodical-publisher', 'methodical', 'publisher', 'string', NULL, NULL, 'Kirjastus', 'Kirjastused', '', 10, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-publishing-date', 'methodical', 'publishing-date', 'string', NULL, NULL, 'Ilmumisaasta', 'Ilmumisaastad', '', 9, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-publishing-place', 'methodical', 'publishing-place', 'string', NULL, NULL, 'Ilmumiskoht', 'Ilmumiskohad', '', 11, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-series', 'methodical', 'series', 'string', NULL, NULL, 'Sari', 'Sarjad', '', 4, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-series-number', 'methodical', 'series-number', 'string', NULL, NULL, 'Number sarjas', 'Number sarjas', '', 5, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-subtitle', 'methodical', 'subtitle', 'string', NULL, NULL, 'Alapealkiri', 'Alapealkirjad', '', 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-tag', 'methodical', 'tag', 'string', NULL, NULL, 'Märksõna', 'Märksõnad', '', 26, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('methodical-title', 'methodical', 'title', 'string', NULL, NULL, 'Pealkiri', 'Pealkirjad', '', 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-translator', 'methodical', 'translator', 'string', NULL, NULL, 'Tõlkija', 'Tõlkijad', '', 54, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-type', 'methodical', 'type', 'string', NULL, NULL, 'Tüüp', 'Tüübid', '', 19, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('methodical-udc', 'methodical', 'udc', 'string', NULL, NULL, 'Liik', 'Liigid', '', 12, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-author', 'periodical', 'author', 'string', NULL, NULL, 'Autor', 'Autorid', '', 8, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-class', 'periodical', 'class', 'string', NULL, NULL, 'Klass', 'Klassid', '', 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-compiler', 'periodical', 'compiler', 'string', NULL, NULL, 'Koostaja', 'Koostajad', '', 52, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-designer', 'periodical', 'designer', 'string', NULL, NULL, 'Disainer', 'Disainerid', '', 53, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-dimensions', 'periodical', 'dimensions', 'string', NULL, NULL, 'Mõõdud', 'Mõõdud', '', 74, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-edition', 'periodical', 'edition', 'string', NULL, NULL, 'Väljalase', 'Väljalase', '', 25, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-editor', 'periodical', 'editor', 'string', NULL, NULL, 'Toimetaja', 'Toimetajad', '', 51, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-epilogue-author', 'periodical', 'epilogue-author', 'string', NULL, NULL, 'Järelsõna autor', 'Järelsõna autorid', '', 57, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-ester-id', 'periodical', 'ester-id', 'string', NULL, NULL, 'Ester ID', 'Ester ID', '', 1000, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-illustrator', 'periodical', 'illustrator', 'string', NULL, NULL, 'Illustraator', 'Illustraatorid', '', 55, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-isn', 'periodical', 'isn', 'string', NULL, NULL, 'IS*N', 'IS*N', '', 13, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('periodical-language', 'periodical', 'language', 'string', NULL, NULL, 'Keel', 'Keeled', '', 22, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-location', 'periodical', 'location', 'string', NULL, NULL, 'Asukoht/Riiul', 'Asukohad/Riiulid', '', 29, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-media', 'audiovideo', 'media', 'string', NULL, NULL, 'Andmekandja', 'Andmekandjad', '', 7, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-notes', 'periodical', 'notes', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 27, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('periodical-number', 'periodical', 'number', 'string', NULL, NULL, 'Number', 'Number', '', 6, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-original-language', 'periodical', 'original-language', 'string', NULL, NULL, 'Originaalkeel', 'Originaalkeeled', '', 23, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-pages', 'periodical', 'pages', 'string', NULL, NULL, 'Lehekülgi', 'Lehekülgi', '', 73, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-photographer', 'periodical', 'photographer', 'string', NULL, NULL, 'Fotograaf', 'Fotograafid', '', 56, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-picture', 'periodical', 'picture', 'file', NULL, NULL, 'Pilt', 'Pildid', '', 28, 0, 0, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('periodical-publisher', 'periodical', 'publisher', 'string', NULL, NULL, 'Kirjastus', 'Kirjastused', '', 10, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-publishing-date', 'periodical', 'publishing-date', 'string', NULL, NULL, 'Ilmumisaasta', 'Ilmumisaastad', '', 9, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-publishing-place', 'periodical', 'publishing-place', 'string', NULL, NULL, 'Ilmumiskoht', 'Ilmumiskohad', '', 11, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-series', 'periodical', 'series', 'string', NULL, NULL, 'Sari', 'Sarjad', '', 4, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-series-number', 'periodical', 'series-number', 'string', NULL, NULL, 'Number sarjas', 'Number sarjas', '', 5, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-subtitle', 'periodical', 'subtitle', 'string', NULL, NULL, 'Alapealkiri', 'Alapealkirjad', '', 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-tag', 'periodical', 'tag', 'string', NULL, NULL, 'Märksõna', 'Märksõnad', '', 26, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('periodical-title', 'periodical', 'title', 'string', NULL, NULL, 'Pealkiri', 'Pealkirjad', '', 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-translator', 'periodical', 'translator', 'string', NULL, NULL, 'Tõlkija', 'Tõlkijad', '', 54, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-type', 'periodical', 'type', 'string', NULL, NULL, 'Tüüp', 'Tüübid', '', 19, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('periodical-udc', 'periodical', 'udc', 'string', NULL, NULL, 'Liik', 'Liigid', '', 12, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('person-address', 'person', 'address', 'string', NULL, '2. Kontakt', 'Aadress', 'Aadressid', '', 120, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('person-birthdate', 'person', 'birthdate', 'date', NULL, '1. Isik', 'Sünnikuupäev', 'Sünnikuupäevad', '', 35, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('person-county', 'person', 'county', 'string', NULL, '2. Kontakt', 'Maakond', 'Maakonnad', '', 123, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('person-email', 'person', 'email', 'string', NULL, '', 'Email', 'Emailid', '', 38, 0, 1, 1, 0, 0, 1, 1, 0, 0, NULL),
    ('person-forename', 'person', 'forename', 'string', NULL, '1. Isik', 'Eesnimi', 'Eesnimed', '', 30, 0, 1, 0, 0, 1, 1, 1, 0, 0, NULL),
    ('person-gender', 'person', 'gender', 'string', NULL, '1. Isik', 'Sugu', 'Sood', '', 36, 1, 1, 0, 0, 0, 1, 0, 0, 1, 'gender'),
    ('person-idcode', 'person', 'idcode', 'string', NULL, '1. Isik', 'Isikukood', 'Isikukoodid', '', 34, 0, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('person-notes', 'person', 'notes', 'string', NULL, '2. Kontakt', 'Märkused', 'Märkused', '', 120, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('person-phone', 'person', 'phone', 'string', NULL, '2. Kontakt', 'Telefon', 'Telefonid', '', 39, 0, 1, 0, 0, 0, 1, 1, 0, 0, NULL),
    ('person-photo', 'person', 'photo', 'file', NULL, '1. Isik', 'Näopilt', 'Näopildid', '', 37, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('person-postalcode', 'person', 'postalcode', 'string', NULL, '2. Kontakt', 'Postiindeks', 'Postiindeksid', '', 124, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('person-surname', 'person', 'surname', 'string', NULL, '1. Isik', 'Perenimi', 'Perenimed', '', 31, 0, 1, 0, 0, 1, 1, 1, 0, 0, NULL),
    ('person-town', 'person', 'town', 'string', NULL, '2. Kontakt', 'Linn', 'Linnad', '', 122, 0, 1, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('person-user', 'person', 'user', 'string', NULL, NULL, 'Kasutaja', 'Kasutajad', '', 32, 0, NULL, 0, 0, 0, 1, 0, 0, 0, NULL),
    ('textbook-author', 'textbook', 'author', 'string', NULL, NULL, 'Autor', 'Autorid', '', 8, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-class', 'textbook', 'class', 'string', NULL, NULL, 'Klass', 'Klassid', '', 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-compiler', 'textbook', 'compiler', 'string', NULL, NULL, 'Koostaja', 'Koostajad', '', 52, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-designer', 'textbook', 'designer', 'string', NULL, NULL, 'Disainer', 'Disainerid', '', 53, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-dimensions', 'textbook', 'dimensions', 'string', NULL, NULL, 'Mõõdud', 'Mõõdud', '', 74, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-edition', 'textbook', 'edition', 'string', NULL, NULL, 'Väljalase', 'Väljalase', '', 25, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-editor', 'textbook', 'editor', 'string', NULL, NULL, 'Toimetaja', 'Toimetajad', '', 51, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-epilogue-author', 'textbook', 'epilogue-author', 'string', NULL, NULL, 'Järelsõna autor', 'Järelsõna autorid', '', 57, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-ester-id', 'textbook', 'ester-id', 'string', NULL, NULL, 'Ester ID', 'Ester ID', '', 1000, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-illustrator', 'textbook', 'illustrator', 'string', NULL, NULL, 'Illustraator', 'Illustraatorid', '', 55, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-isn', 'textbook', 'isn', 'string', NULL, NULL, 'IS*N', 'IS*N', '', 13, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('textbook-language', 'textbook', 'language', 'string', NULL, NULL, 'Keel', 'Keeled', '', 22, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-location', 'textbook', 'location', 'string', NULL, NULL, 'Asukoht/Riiul', 'Asukohad/Riiulid', '', 29, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-media', 'audiovideo', 'media', 'string', NULL, NULL, 'Andmekandja', 'Andmekandjad', '', 7, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-notes', 'textbook', 'notes', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 27, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('textbook-number', 'textbook', 'number', 'string', NULL, NULL, 'Number', 'Number', '', 6, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-original-language', 'textbook', 'original-language', 'string', NULL, NULL, 'Originaalkeel', 'Originaalkeeled', '', 23, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-pages', 'textbook', 'pages', 'string', NULL, NULL, 'Lehekülgi', 'Lehekülgi', '', 73, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-photographer', 'textbook', 'photographer', 'string', NULL, NULL, 'Fotograaf', 'Fotograafid', '', 56, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-picture', 'textbook', 'picture', 'file', NULL, NULL, 'Pilt', 'Pildid', '', 28, 0, 0, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('textbook-publisher', 'textbook', 'publisher', 'string', NULL, NULL, 'Kirjastus', 'Kirjastused', '', 10, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-publishing-date', 'textbook', 'publishing-date', 'string', NULL, NULL, 'Ilmumisaasta', 'Ilmumisaastad', '', 9, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-publishing-place', 'textbook', 'publishing-place', 'string', NULL, NULL, 'Ilmumiskoht', 'Ilmumiskohad', '', 11, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-series', 'textbook', 'series', 'string', NULL, NULL, 'Sari', 'Sarjad', '', 4, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-series-number', 'textbook', 'series-number', 'string', NULL, NULL, 'Number sarjas', 'Number sarjas', '', 5, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-subtitle', 'textbook', 'subtitle', 'string', NULL, NULL, 'Alapealkiri', 'Alapealkirjad', '', 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-tag', 'textbook', 'tag', 'string', NULL, NULL, 'Märksõna', 'Märksõnad', '', 26, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('textbook-title', 'textbook', 'title', 'string', NULL, NULL, 'Pealkiri', 'Pealkirjad', '', 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-translator', 'textbook', 'translator', 'string', NULL, NULL, 'Tõlkija', 'Tõlkijad', '', 54, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-type', 'textbook', 'type', 'string', NULL, NULL, 'Tüüp', 'Tüübid', '', 19, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('textbook-udc', 'textbook', 'udc', 'string', NULL, NULL, 'Liik', 'Liigid', '', 12, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-author', 'workbook', 'author', 'string', NULL, NULL, 'Autor', 'Autorid', '', 8, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-class', 'workbook', 'class', 'string', NULL, NULL, 'Klass', 'Klassid', '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-compiler', 'workbook', 'compiler', 'string', NULL, NULL, 'Koostaja', 'Koostajad', '', 52, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-designer', 'workbook', 'designer', 'string', NULL, NULL, 'Disainer', 'Disainerid', '', 53, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-dimensions', 'workbook', 'dimensions', 'string', NULL, NULL, 'Mõõdud', 'Mõõdud', '', 74, 0, 1, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-edition', 'workbook', 'edition', 'string', NULL, NULL, 'Väljalase', 'Väljalase', '', 25, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-editor', 'workbook', 'editor', 'string', NULL, NULL, 'Toimetaja', 'Toimetajad', '', 51, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-epilogue-author', 'workbook', 'epilogue-author', 'string', NULL, NULL, 'Järelsõna autor', 'Järelsõna autorid', '', 57, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-ester-id', 'workbook', 'ester-id', 'string', NULL, NULL, 'Ester ID', 'Ester ID', '', 1000, 0, 1, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-illustrator', 'workbook', 'illustrator', 'string', NULL, NULL, 'Illustraator', 'Illustraatorid', '', 55, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-isn', 'workbook', 'isn', 'string', NULL, NULL, 'IS*N', 'IS*N', '', 13, 0, 1, 0, 0, 1, 0, 1, 0, 0, NULL),
    ('workbook-language', 'workbook', 'language', 'string', NULL, NULL, 'Keel', 'Keeled', '', 22, 0, 0, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-location', 'workbook', 'location', 'string', NULL, NULL, 'Asukoht/Riiul', 'Asukohad/Riiulid', '', 29, 0, 0, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-media', 'audiovideo', 'media', 'string', NULL, NULL, 'Andmekandja', 'Andmekandjad', '', 7, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-notes', 'workbook', 'notes', 'text', NULL, NULL, 'Märkused', 'Märkused', '', 27, 0, 1, 0, 0, 0, 0, 0, 0, 0, NULL),
    ('workbook-number', 'workbook', 'number', 'string', NULL, NULL, 'Number', 'Number', '', 6, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-original-language', 'workbook', 'original-language', 'string', NULL, NULL, 'Originaalkeel', 'Originaalkeeled', '', 23, 0, 1, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-pages', 'workbook', 'pages', 'string', NULL, NULL, 'Lehekülgi', 'Lehekülgi', '', 73, 0, 1, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-photographer', 'workbook', 'photographer', 'string', NULL, NULL, 'Fotograaf', 'Fotograafid', '', 56, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-picture', 'workbook', 'picture', 'file', NULL, NULL, 'Pilt', 'Pildid', '', 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL),
    ('workbook-publisher', 'workbook', 'publisher', 'string', NULL, NULL, 'Kirjastus', 'Kirjastused', '', 10, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-publishing-date', 'workbook', 'publishing-date', 'string', NULL, NULL, 'Ilmumisaasta', 'Ilmumisaastad', '', 9, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-publishing-place', 'workbook', 'publishing-place', 'string', NULL, NULL, 'Ilmumiskoht', 'Ilmumiskohad', '', 11, 0, 1, 0, 0, 0, 0, 0, 0, 1, NULL),
    ('workbook-series', 'workbook', 'series', 'string', NULL, NULL, 'Sari', 'Sarjad', '', 4, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-series-number', 'workbook', 'series-number', 'string', NULL, NULL, 'Number sarjas', 'Number sarjas', '', 5, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-subtitle', 'workbook', 'subtitle', 'string', NULL, NULL, 'Alapealkiri', 'Alapealkirjad', '', 2, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-tag', 'workbook', 'tag', 'string', NULL, NULL, 'Märksõna', 'Märksõnad', '', 26, 0, 1, 0, 0, 0, 0, 0, 0, 0, NULL),
    ('workbook-title', 'workbook', 'title', 'string', NULL, NULL, 'Pealkiri', 'Pealkirjad', '', 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-translator', 'workbook', 'translator', 'string', NULL, NULL, 'Tõlkija', 'Tõlkijad', '', 54, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-type', 'workbook', 'type', 'string', NULL, NULL, 'Tüüp', 'Tüübid', '', 19, 0, 0, 0, 0, 1, 0, 1, 0, 1, NULL),
    ('workbook-udc', 'workbook', 'udc', 'string', NULL, NULL, 'Liik', 'Liigid', '', 12, 0, 0, 0, 0, 0, 0, 0, 0, 1, NULL);


INSERT INTO `relationship_definition` (`keyname`, `estonian_label`, `estonian_label_plural`, `english_label`, `english_label_plural`)
VALUES
    ('allowed-child', 'Lubatud alam', 'Lubatud alamad', 'Allowed child', 'Allowed childs'),
    ('child', 'Alam', 'Alamad', 'Child', 'Childs'),
    ('editor', 'Muutja', 'Muutjad', 'Editor', 'Editors'),
    ('lending', 'Laenutus', 'Laenutused', 'Lending', 'Lendings'),
    ('owner', 'Omanik', 'Omanikud', 'Owner', 'Owners'),
    ('propagated-property', 'Propageeruv väli', 'Propageeruvad väljad', 'Propagated property', 'Propagated properties'),
    ('target-property', 'Sihtväli', 'Sihtväljad', 'Targeted property', 'Targeted properties'),
    ('viewer', 'Vaataja', 'Vaatajad', 'Viewer', 'Viewers');



INSERT INTO `entity` (`entity_definition_keyname`, `old_id`)
VALUES
    ('person', 'argo'),
    ('person', 'mihkel'),
    ('institution', 'root_node');

INSERT INTO `relationship` (`relationship_definition_keyname`, `entity_id`, `related_entity_id`)
VALUES
    ('viewer', (SELECT id FROM entity WHERE old_id = 'root_node'), (SELECT id FROM entity WHERE old_id = 'argo')),
    ('viewer', (SELECT id FROM entity WHERE old_id = 'root_node'), (SELECT id FROM entity WHERE old_id = 'mihkel'));

INSERT INTO `property` (`property_definition_keyname`, `entity_id`, `value_string`)
VALUES
    ('person-user', (SELECT id FROM entity WHERE old_id = 'argo'), 'argoroots@gmail.com'),
    ('person-user', (SELECT id FROM entity WHERE old_id = 'mihkel'), 'mihkel@entu.ee'),
    ('person-forename', (SELECT id FROM entity WHERE old_id = 'argo'), 'Argo'),
    ('person-forename', (SELECT id FROM entity WHERE old_id = 'mihkel'), 'Mihkel'),
    ('institution-name', (SELECT id FROM entity WHERE old_id = 'root_node'), 'Asutuse Nimi');

INSERT INTO `relationship` (`relationship_definition_keyname`, `entity_definition_keyname`, `related_entity_definition_keyname`)
VALUES
    ('allowed-child', 'institution', 'department'),
    ('allowed-child', 'institution', 'library'),
    ('allowed-child', 'library', 'book'),
    ('allowed-child', 'library', 'textbook'),
    ('allowed-child', 'library', 'workbook'),
    ('allowed-child', 'library', 'audiovideo'),
    ('allowed-child', 'library', 'periodical'),
    ('allowed-child', 'library', 'methodical'),
    ('allowed-child', 'book', 'copy'),
    ('allowed-child', 'textbook', 'copy'),
    ('allowed-child', 'workbook', 'copy'),
    ('allowed-child', 'audiovideo', 'copy'),
    ('allowed-child', 'periodical', 'copy'),
    ('allowed-child', 'methodical', 'copy'),
    ('allowed-child', 'institution', 'person'),
    ('allowed-child', 'department', 'person'),
    ('allowed-child', 'institution', 'class'),
    ('allowed-child', 'library', 'acceptance-report');
