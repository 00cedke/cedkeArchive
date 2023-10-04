import math
import socket
import os

ip='192.168.1.97' # IP Address
print('\n ** Sending Cafe Code! **\n')
print('  Connecting to: '+ip)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,7331))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10014CFC00000000'))

cafe='0302000010F5E82800000001000000000502000011003000000000000000000000020000110030000000000000000000D0000000DEADCAFE0302000010F5E82800000002000000000502000011003000000000010000000000020000110030000000000100000000D0000000DEADCAFE0302000010F5E82800000003000000000502000011003000000000020000000000020000110030000000000200000000D0000000DEADCAFE0302000010F5E82800000004000000000502000011003000000000030000000000020000110030000000000300000000D0000000DEADCAFE0302000010F5E82800000005000000000502000011003000000000040000000000020000110030000000000400000000D0000000DEADCAFE0302000010F5E82800000006000000000502000011003000000000050000000000020000110030000000000500000000D0000000DEADCAFE0302000010F5E82800000007000000000502000011003000000000060000000000020000110030000000000600000000D0000000DEADCAFE0302000010F5E82800000008000000000502000011003000000000070000000000020000110030000000000700000000D0000000DEADCAFE0602000011003000000000000000000000020000110030000000000000000000D0000000DEADCAFE03010000102EFA66000001000000000000020000110030000000000000000000D0000000DEADCAFE03010000102EFA6600000100000000000C00000000000001100200001100300014040000FFFFFFFF1102000011003000D2000000CAFEBABED0000000DEADCAFE0D000000102EFA6603010000102EFA6600000200000000000C00000000000001100200001100300014040000000000011102000011003000D2000000CAFEBABED0000000DEADCAFE0D000000102EFA66030200001100300000000001000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000000830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000002000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000001030100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000003000000003000000010A7274C100000005000000031000000000000C830100000000000001000000050000000310000000000001830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000004000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000002030100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000005000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000002830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000006000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000003030100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000007000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000003830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE0302000010F5E82800000001000000000502000011003000000000000000000000020000110030000000000000000000D0000000DEADCAFE0302000010F5E82800000002000000000502000011003000000000010000000000020000110030000000000100000000D0000000DEADCAFE0302000010F5E82800000003000000000502000011003000000000020000000000020000110030000000000200000000D0000000DEADCAFE0302000010F5E82800000004000000000502000011003000000000030000000000020000110030000000000300000000D0000000DEADCAFE0302000010F5E82800000005000000000502000011003000000000040000000000020000110030000000000400000000D0000000DEADCAFE0302000010F5E82800000006000000000502000011003000000000050000000000020000110030000000000500000000D0000000DEADCAFE0302000010F5E82800000007000000000502000011003000000000060000000000020000110030000000000600000000D0000000DEADCAFE0302000010F5E82800000008000000000502000011003000000000070000000000020000110030000000000700000000D0000000DEADCAFE0602000011003000000000000000000000020000110030000000000000000000D0000000DEADCAFE03010000102EFA66000001000000000000020000110030000000000000000000D0000000DEADCAFE03010000102EFA6600000400000000000C00000000000001100200001100300014040000FFFFFFFF1102000011003000D2000000CAFEBABED0000000DEADCAFE0D000000102EFA6603010000102EFA6600000400000000000C00000000000001100200001100300014040000000000011102000011003000D2000000CAFEBABED0000000DEADCAFE0D000000102EFA66030200001100300000000001000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000000830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000002000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000001030100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000003000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000001830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000004000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000002030100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000005000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000002830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000006000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000003030100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE030200001100300000000007000000003000000010A72A4C100000005000000031000000000000C830100000000000001000000050000000310000000000003830100000000000001000000050000000310000000000015830100000000000001000000050000000121000010000000012100002000000041210000300000008121000040000000C121000050000001012100006000000141210000700000018121000080000001C12100009000000201210000A000000241210000B000000281210000C0000002C3000000010A0A6441000000050000000310000000000002C3010000000000000100000005000000031000000000001583010000000000000100000004DF9FFFF131000010000000013100002000000041310000300000008131000040000000C131000050000001013100006000000141310000700000018131000080000001C13100009000000201310000A000000241310000B000000281310000C0000002CD0000000DEADCAFE' # Cafe Code
for x in range(math.floor(len(cafe)/8)):
    s.send(bytes.fromhex('03'))
    s.send(bytes.fromhex('0'+format(0x01133000+x*4,'X')+cafe[x*8:x*8+8]))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10014CFC00000001'))

asm='' # Assembly RAM Write
for x in range(math.floor(len(asm)/16)):
    s.send(bytes.fromhex('03'))
    s.send(bytes.fromhex(asm[x*16:x*16+16]))
s.close()
print('\nSent Codes Successfully')

