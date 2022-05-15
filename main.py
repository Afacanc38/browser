#!/usr/bin/env python3
import gi, os, sys
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, Handy, GLib, GLib, WebKit2

Handy.init()

class MyWindow(Handy.Window):
    def __init__(self):
        super().__init__(title="Tarayıcı")
        self.set_title("Tarayıcı")
        GLib.set_application_name("Tarayıcı")
        GLib.set_prgname('Tarayıcı')
        self.set_default_size(900, 600)

        self.main_box = Gtk.Box(
            orientation = Gtk.Orientation.VERTICAL
        )
        self.add(self.main_box)
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.inp_url = Gtk.Entry(
            width_request = 370
        )
        self.scroll = Gtk.ScrolledWindow()
        self.web = WebKit2.WebView()
        self.web.load_uri("https://duckduckgo.com")
        self.inp_url.set_placeholder_text("Web'de arayın veya URL adresi girin...")
        self.inp_url.connect("activate", self.on_inp_url_activate)
        self.hb.set_custom_title(self.inp_url)
        self.btn_prev = Gtk.Button()
        self.btn_prev = Gtk.Button.new_from_icon_name("go-previous-symbolic", Gtk.IconSize.MENU)
        self.btn_prev.connect("clicked", self.on_btn_prev_clicked)
        self.btn_next = Gtk.Button()
        self.btn_next = Gtk.Button.new_from_icon_name("go-next-symbolic", Gtk.IconSize.MENU)
        self.btn_next.connect("clicked", self.on_btn_next_clicked)
        self.btn_box = Gtk.ButtonBox(width_request = 0)
        self.btn_box.set_layout(Gtk.ButtonBoxStyle.EXPAND)
        self.btn_box.pack_start(self.btn_prev, True, True, 0)
        self.btn_box.pack_start(self.btn_next, True, True, 0)
        self.btn_ref = Gtk.Button()
        self.btn_ref = Gtk.Button.new_from_icon_name("view-refresh-symbolic", Gtk.IconSize.MENU)
        self.btn_next.connect("clicked", self.on_btn_ref_clicked)
        self.hb.pack_start(self.btn_box)
        self.hb.pack_start(self.btn_ref)
        self.main_box.pack_start(
            self.hb,
            False,
            True,
            0
        )
        self.scroll.add(self.web)
        self.main_box.pack_start(
            self.scroll,
            True,
            True,
            0
        )
    def on_btn_next_clicked(self, widget):
        self.web.go_forward()
    def on_btn_prev_clicked(self, widget):
        self.web.go_back()
    def on_inp_url_activate(self, widget):
        url_text = self.inp_url.get_text()
        if "https://" in url_text:
            self.web.load_uri(url_text)
        else:
            self.web.load_uri(f"https://duckduckgo.com/?q={url_text}")
        self.inp_url.set_text("")
    def on_btn_ref_clicked(self, widget):
        self.web.reload()
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
