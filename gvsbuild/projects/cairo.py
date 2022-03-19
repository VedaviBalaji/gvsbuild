#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Cairo(Tarball, Meson):
    def __init__(self):
        Project.__init__(
            self,
            "cairo",
            archive_url="https://gitlab.freedesktop.org/cairo/cairo/-/archive/1.17.4/cairo-1.17.4.tar.gz",
            hash="0a673c88f7c049b4555c1f152b11d9fe16d8523b62632d2d5c14e1868499ce9f",
            dependencies=["fontconfig", "glib", "pixman", "libpng"],
            patches=[],
        )

    def build(self):
        Meson.build(self, meson_params="-Dgtk_docs=false")
        self.install(r".\COPYING share\doc\cairo")
