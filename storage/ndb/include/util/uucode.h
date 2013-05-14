/* Copyright (c) 2003-2005 MySQL AB


   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; version 2 of the License.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA */


#ifndef UUCODE_H
#define UUCODE_H

#include <ndb_global.h>

#ifdef	__cplusplus
extern "C" {
#endif

  void uuencode(const char * data, int dataLen, FILE * out);
  int uudecode(FILE * input, char * outBuf, int bufLen);
  
  int uuencode_mem(char * dst, const char * src, int src_len);
  int uudecode_mem(char * dst, int dst_len, const char * src);

#ifdef	__cplusplus
}
#endif

#endif
