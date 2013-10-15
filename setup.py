
# -*- coding: utf-8 -*-
 
''' 为程序添加右键菜单打开方式 '''
 
import _winreg
 
# 此处以IE浏览器为例
# 通过修改代码中prog_name和prog_path的值，可以指定任意的其他程序
 
prog_name = 'send_to_myself_7' # 程序名称（即右键菜单中显示的名称）
prog_path = r'C:\Dropbox\projects\send_to_gmail\build\exe.win32-2.7\run.exe' # 程序路径（即可执行文件所在路径）

# 打开名称为“HEKY_CLASSES_ROOT\*\shell”的键key
key = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, r'*\\shell')
# 为键key新建名称为prog_name的子键，
# 并设置其数据为REG_SZ（字符串值）类型的prog_name（(&I)表示指定快捷键为I）
_winreg.SetValue(key, prog_name, _winreg.REG_SZ, prog_name ) #+ '(&I)')
 
# 打开名称为prog_name的子键prog_key
prog_key = _winreg.OpenKey(key, prog_name)
# 为键prog_key新建名称为'command'的子键，
# 并设置其数据为REG_SZ（字符串值）类型的prog_path + ' %1'
_winreg.SetValue(prog_key, 'command', _winreg.REG_SZ, prog_path + ' %1')
 
_winreg.CloseKey(prog_key) # 关闭键prog_key
_winreg.CloseKey(key) # 关闭键key
