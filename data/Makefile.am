SUBDIRS = fonts extensions keymaps skin_default rc_models

dist_pkgdata_DATA = \
	encoding.conf \
	keymap.xml \
	keymap.ntr \
	keymap.u80 \
	menu.xml \
	prev.png \
	black.mvi \
	rcpositions.xml \
	setup.xml \
	skin_default.xml \
	skin_subtitles.xml \
	skin.xml \
	Skin_ExtPlugins.xml \
	startwizard.xml \
	userinterfacepositionerwizard.xml \
	freesat.t1 \
	freesat.t2 \
	unicable.xml \
	hd-testcard.mvi

if HAVE_TEXTLCD
dist_pkgdata_DATA += skin_text.xml skin_text_clock.xml
endif

if HAVE_DISPLAY96
dist_pkgdata_DATA += skin_display96.xml
endif

if HAVE_DISPLAY128
dist_pkgdata_DATA += skin_display128.xml
endif

if HAVE_DISPLAYDM
dist_pkgdata_DATA += skin_display.xml
endif

if HAVE_COLORLCD220
SUBDIRS += lcd220 lcd_skin220
endif

if HAVE_BWLCD255
SUBDIRS += lcd255 lcd_skin255
endif
