from django.db import models

class MultiSelectField(models.CharField):
    """
    Custom Implementation of MultiSelectField to achieve Django 5.0 compatibility

    See: https://github.com/goinnn/django-multiselectfield/issues/141#issuecomment-1911731471
    """

    def _get_flatchoices(self):
        flat_choices = super(models.CharField, self).flatchoices

        class MSFFlatchoices(list):
            # Used to trick django.contrib.admin.utils.display_for_field into not treating the list of values as a
            # dictionary key (which errors out)
            def __bool__(self):
                return False

            __nonzero__ = __bool__

        return MSFFlatchoices(flat_choices)

    flatchoices = property(_get_flatchoices)

class Locale(models.Model):
    name = models.CharField(max_length=100)
    banner_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default="media/photos/2024/04/01/default.jpg")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default="media/photos/2024/04/01/default.jpg")

    def __str__(self):
        return self.name



class Dessert(models.Model):
    locale_choice = (
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
        ("Hawaii", "Hawaii"),
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
        ("North America - Louisiana Creole", "North America - Louisiana Creole"),
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
        ("Wales", "Wales")

    )
    locale_choice_add = (
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
        ("Hawaii", "Hawaii"),
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
        ("North America - Louisiana Creole", "North America - Louisiana Creole"),
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
        ("Wales", "Wales")

    )
    ingredients_choice = (
        ("agar", "agar"),
        ("almond", "almond"),
        ("anise", "anise"),
        ("apple", "apple"),
        ("berries", "berries"),
        ("cassava", "cassava"),
        ("cardamom", "cardamom"),
        ("chancaca", "chancaca"),
        ("chocolate", "chocolate"),
        ("cinnamon", "cinnamon"),
        ("coconut", "coconut"),
        ("corn", "corn"),
        ("cocoa-powder", "cocoa-powder"),
        ("cottage cheese", "cottage cheese"),
        ("custard", "custard"),
        ("dates", "dates"),
        ("dulce de leche", "dulce de leche"),
        ("dulce de parchita", "dulce de parchita"),
        ("eggs", "eggs"),
        ("egg whites", "egg whites"),
        ("egg yolk", "egg yolk"),
        ("filo pastry", "filo pastry"),
        ("flour", "flour"),
        ("hazelnut", "hazelnut"),
        ("honey", "honey"),
        ("kiwifruit", "kiwifruit"),
        ("lucuma", "lucuma"),
        ("maple syrup", "maple syrup"),
        ("Maria cookies", "Maria cookies"),
        ("mascarpone", "mascarpone"),
        ("matcha", "matcha"),
        ("milk", "milk"),
        ("oat", "oat"),
        ("palm sugar", "palm sugar"),
        ("paneer", "paneer"),
        ("peanuts", "peanuts"),
        ("pasta", "pasta"),
        ("pistachio", "pistachio"),
        ("plantain", "plantain"),
        ("poppy seed", "poppy seed"),
        ("powdered sugar", "powdered sugar"),
        ("puff pastry", "puff pastry"),
        ("quinoa", "quinoa"),
        ("red bean paste", "red bean paste"),
        ("rice", "rice"),
        ("rosewater", "rosewater"),
        ("rum", "rum"),
        ("sugar", "sugar"),
        ("sugarcane", "sugarcane"),
        ("sweetened condensed milk", "sweetened condensed milk"),
        ("taro", "taro"),
        ("tovrog", "tovrog"),
        ("tropical fruit", "tropical fruit"),
        ("ube", "ube"),
        ("vanilla", "vanilla"),
        ("walnut", "walnut"),
        ("whiskey", "whiskey"),
        ("yeast", "yeast")
    )
    category_choice = (
        ("Cakes", "Cakes"),
        ("Pies & Tarts", "Pies & Tarts"),
        ("Cookies & Bars", "Cookies & Bars"),
        ("Pastries", "Pastries"),
        ("Puddings & Custards", "Puddings & Custards"),
        ("Frozen Desserts", "Frozen Desserts"),
        ("Confections & Candies", "Confections & Candies"),
        ("Fruit Desserts", "Fruit Desserts"),
        ("Fried Dough", "Fried Dough"),
    )
    dessert_name = models.CharField(max_length=100)
    locale_name = models.ManyToManyField(Locale)

    category = models.CharField(max_length=100, choices=category_choice, default = False)
    featured_ingredient = models.ManyToManyField(Ingredient, related_name = "desserts")

    description = models.TextField(max_length=800)
    dessert_photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    dessert_photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", default="media/photos/2024/04/01/default.jpg")
    dessert_photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", default="media/photos/2024/04/01/default.jpg")
    dessert_photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", default="media/photos/2024/04/01/default.jpg")
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.dessert_name

class DessertVariation(models.Model):
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, related_name="variations")
    name = models.CharField(max_length=100)
    locale = models.ForeignKey(Locale, on_delete=models.CASCADE, related_name="dessert_variations")
    preparation_method = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", default="media/photos/2024/04/01/default.jpg")
    image_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", default="media/photos/2024/04/01/default.jpg")
    ingredients = models.ManyToManyField(Ingredient, related_name="variation_desserts")

    def __str__(self):
        return f"{self.dessert.dessert_name} - {self.name} - {self.locale.name}"

class IngredientVariation(models.Model):
    dessert_variation = models.ForeignKey(DessertVariation, on_delete=models.CASCADE, related_name = "ingredient_variations", default=None)
    name = models.CharField(max_length=100)
    locale = models.ForeignKey(Locale, on_delete=models.CASCADE, related_name = "ingredient_variations")
    preparation_method = models.TextField(max_length=800, blank=True)

    def __str__(self):
        return f"{self.ingredient.name} - {self.name} - {self.locale.name}"
