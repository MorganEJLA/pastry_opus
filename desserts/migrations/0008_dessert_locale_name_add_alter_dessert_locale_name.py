# Generated by Django 5.0.3 on 2024-04-15 21:39

import desserts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("desserts", "0007_remove_dessert_locale_name_add_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dessert",
            name="locale_name_add",
            field=desserts.models.MultiSelectField(
                blank=True,
                choices=[
                    ("Açores", "Açores"),
                    ("Albania", "Albania"),
                    ("Algeria", "Algeria"),
                    ("Ashkenazi", "Ashkenazi"),
                    ("Argentina", "Argentina"),
                    ("Australia", "Australia"),
                    ("Belgium", "Belgium"),
                    ("Belize", "Belize"),
                    ("Bolivia", "Bolivia"),
                    ("Brazil", "Brazil"),
                    ("Cameroon", "Cameroon"),
                    ("Canada", "Canada"),
                    ("Cape Verde", "Cape Verde"),
                    ("China-Beijing", "China-Beijing"),
                    ("China-Guangzhou", "China-Guangzhou"),
                    ("China-Hong Kong", "China-Hong Kong"),
                    ("Colombia", "Colombia"),
                    ("Croatia", "Croatia"),
                    ("Cuba", "Cuba"),
                    ("Curacao", "Curacao"),
                    ("Dominican Republic", "Dominican Republic"),
                    ("Egypt", "Egypt"),
                    ("El Salvador", "El Salvador"),
                    ("England", "England"),
                    ("Fiji", "Fiji"),
                    ("France", "France"),
                    ("Germany", "Germany"),
                    ("Ghana", "Ghana"),
                    ("Greece", "Greece"),
                    ("Grenada", "Grenada"),
                    ("Guadaloupe", "Guadaloupe"),
                    ("Guatemala", "Guatemala"),
                    ("Guyana", "Guyana"),
                    ("India", "India"),
                    ("Indonesia", "Indonesia"),
                    ("Iran", "Iran"),
                    ("Ireland", "Ireland"),
                    ("Israel", "Israel"),
                    ("Italy", "Italy"),
                    ("Jamaica", "Jamaica"),
                    ("Japan", "Japan"),
                    ("Kenya", "Kenya"),
                    ("Liberia", "Liberia"),
                    ("Madeira", "Madeira"),
                    ("Mali", "Mali"),
                    ("Mexico", "Mexico"),
                    ("Morocco", "Morocco"),
                    ("Nepal", "Nepal"),
                    ("Nigeria", "Nigeria"),
                    ("New Zealand", "New Zealand"),
                    ("Nicaragua", "Nicaragua"),
                    ("North America - Appalachia", "North America - Appalachia"),
                    ("North America - Cajun", "North America - Cajun"),
                    (
                        "North America - Louisiana Creole",
                        "North America - Louisiana Creole",
                    ),
                    ("North America - Lowcountry", "North America - Lowcountry"),
                    ("North America - Southern", "North America - Southern"),
                    ("North America - Southwest", "North America - Southwest"),
                    ("Norway", "Norway"),
                    ("Pakistan", "Pakistan"),
                    ("Palestine", "Palestine"),
                    ("Panama", "Panama"),
                    ("Peru", "Peru"),
                    ("Philippines", "Philippines"),
                    ("Poland", "Poland"),
                    ("Portugal", "Portugal"),
                    ("Puerto Rico", "Puerto Rico"),
                    ("Samoa", "Samoa"),
                    ("Scotland", "Scotland"),
                    ("Sephardic", "Sephardic"),
                    ("Senegal", "Senegal"),
                    ("Sicily", "Sicily"),
                    ("South Africa", "South Africa"),
                    ("South Korea", "South Korea"),
                    ("Spain", "Spain"),
                    ("Sri Lanka", "Sri Lanka"),
                    ("Suriname", "Suriname"),
                    ("Sweden", "Sweden"),
                    ("Taiwan", "Taiwan"),
                    ("Thailand", "Thailand"),
                    ("Trinidad & Tobago", "Trinidad & Tobago"),
                    ("Turkiye", "Turkiye"),
                    ("Ukraine", "Ukraine"),
                    ("Wales", "Wales"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="dessert",
            name="locale_name",
            field=desserts.models.MultiSelectField(
                blank=True,
                choices=[
                    ("Açores", "Açores"),
                    ("Albania", "Albania"),
                    ("Algeria", "Algeria"),
                    ("Ashkenazi", "Ashkenazi"),
                    ("Argentina", "Argentina"),
                    ("Australia", "Australia"),
                    ("Belgium", "Belgium"),
                    ("Belize", "Belize"),
                    ("Bolivia", "Bolivia"),
                    ("Brazil", "Brazil"),
                    ("Cameroon", "Cameroon"),
                    ("Canada", "Canada"),
                    ("Cape Verde", "Cape Verde"),
                    ("China-Beijing", "China-Beijing"),
                    ("China-Guangzhou", "China-Guangzhou"),
                    ("China-Hong Kong", "China-Hong Kong"),
                    ("Colombia", "Colombia"),
                    ("Croatia", "Croatia"),
                    ("Cuba", "Cuba"),
                    ("Curacao", "Curacao"),
                    ("Dominican Republic", "Dominican Republic"),
                    ("Egypt", "Egypt"),
                    ("El Salvador", "El Salvador"),
                    ("England", "England"),
                    ("Fiji", "Fiji"),
                    ("France", "France"),
                    ("Germany", "Germany"),
                    ("Ghana", "Ghana"),
                    ("Greece", "Greece"),
                    ("Grenada", "Grenada"),
                    ("Guadaloupe", "Guadaloupe"),
                    ("Guatemala", "Guatemala"),
                    ("Guyana", "Guyana"),
                    ("India", "India"),
                    ("Indonesia", "Indonesia"),
                    ("Iran", "Iran"),
                    ("Ireland", "Ireland"),
                    ("Israel", "Israel"),
                    ("Italy", "Italy"),
                    ("Jamaica", "Jamaica"),
                    ("Japan", "Japan"),
                    ("Kenya", "Kenya"),
                    ("Liberia", "Liberia"),
                    ("Madeira", "Madeira"),
                    ("Mali", "Mali"),
                    ("Mexico", "Mexico"),
                    ("Morocco", "Morocco"),
                    ("Nepal", "Nepal"),
                    ("Nigeria", "Nigeria"),
                    ("New Zealand", "New Zealand"),
                    ("Nicaragua", "Nicaragua"),
                    ("North America - Appalachia", "North America - Appalachia"),
                    ("North America - Cajun", "North America - Cajun"),
                    (
                        "North America - Louisiana Creole",
                        "North America - Louisiana Creole",
                    ),
                    ("North America - Lowcountry", "North America - Lowcountry"),
                    ("North America - Southern", "North America - Southern"),
                    ("North America - Southwest", "North America - Southwest"),
                    ("Norway", "Norway"),
                    ("Pakistan", "Pakistan"),
                    ("Palestine", "Palestine"),
                    ("Panama", "Panama"),
                    ("Peru", "Peru"),
                    ("Philippines", "Philippines"),
                    ("Poland", "Poland"),
                    ("Portugal", "Portugal"),
                    ("Puerto Rico", "Puerto Rico"),
                    ("Samoa", "Samoa"),
                    ("Scotland", "Scotland"),
                    ("Sephardic", "Sephardic"),
                    ("Senegal", "Senegal"),
                    ("Sicily", "Sicily"),
                    ("South Africa", "South Africa"),
                    ("South Korea", "South Korea"),
                    ("Spain", "Spain"),
                    ("Sri Lanka", "Sri Lanka"),
                    ("Suriname", "Suriname"),
                    ("Sweden", "Sweden"),
                    ("Taiwan", "Taiwan"),
                    ("Thailand", "Thailand"),
                    ("Trinidad & Tobago", "Trinidad & Tobago"),
                    ("Turkiye", "Turkiye"),
                    ("Ukraine", "Ukraine"),
                    ("Wales", "Wales"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]