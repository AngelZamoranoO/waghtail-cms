from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# Importamos el MutiFieldPanel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel



class HomePage(Page):
    #Agregamos la section Heroe desde HomePage

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete = models.SET_NULL,
        related_name= "+",
        help_text="Homepage Image"
    )

    hero_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Hero CTA",
        )
    
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"), 
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link")
            ],
            heading="Hero Section", 
        ),
        FieldPanel("body")
    ]