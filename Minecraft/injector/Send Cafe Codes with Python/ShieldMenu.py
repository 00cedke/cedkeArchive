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

cafe='0002000012000000120000100000000030000000120000001000000041F0000000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000001310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000001310000000000003000120000108709580012000C000000010012002000000002310000000000003000120000108709580012000C000000010012002000000003310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000001310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C000000010012002000000000310000000000003000120000108709580012000C0000000100120018400000100012002000000000310000000000003000120000108709580012000C0000000100120018400005080012002000000000310000000000003000120000108709580012000C0000000100120018400008800012002000000000310000000000003000120000108709580012000C000000010012001840000AE40012002000000000310000000000003000120000108709580012000C000000010012001840000D480012002000000000310000000000003000120000108709580012000C000000010012001840000FAC0012002000000000310000000000003000120000108709580012000C0000000100120018400012100012002000000000310000000000003000120000108709580012000C0000000100120018400016D80012002000000000310000000000003000120000108709580012000C000000400012002000000000310000000000003000120000108709580012000C0000004000120020000000003100000000000030D0000000DEADCAFE30000000109DF84C1000000041F000001210000000000410121000010000046812100003000004FC1210000400000500121000050000050812100007000005741210000B000005781210000D000001701210000E000005941210000F000005A0121000100000072412100011000005AC12100012000005B012100013000005B412100014000005B812100015000005BC12100016000005DC121000170000061C121000180000062012100019000006241210001A000006281210001B000006401210001C0000066C1210001D000006701210001E000006741210001F0000069C12100020000006A0121000210000033C12100022000006D0121000230000063012100024000006C0121000250000000012100028000004AC12100029000005D41210002A000006D8D0000000DEADCAFE30000000120000001000000041F0000013100000000000141310000100000044131000010000007413100003000000A413100004000000D4131000050000010413100005000001341310000700000164131000070000019413100007000001C413100007000001F41310000B000002241310000B000002541310000D000002841310000E000002B41310000F000002E413100010000003141310001100000344131000120000037413100013000003A413100014000003D4131000150000040413100016000004341310001700000464131000180000049413100019000004C41310001A000004F41310001B000005241310001C000005541310001D000005841310001E000005B41310001F000005E413100020000006141310002100000644131000220000067413100023000006A413100024000006D4131000250000070413100025000007341310002500000764131000280000079413100029000007C41310002A000007F41310002A000008241310002A000008541310002A000008841310002A000008B41310002A000008E413100025000009141310002500000944011000C800000960120000101200004012000070120000A0120000D012000100120001301200016012000190120001C0120001F0120002201200025012000280120002B0120002E0120003101200034012000370120003A0120003D012000400120004301200046012000490120004C0120004F0120005201200055012000580120005B0120005E0120006101200064012000670120006A0120006D012000700120007301200076012000790120007C0120007F0120008201200085012000880120008B0120008E0120009101200094000000000000000FFD0000000DEADCAFE0100000C10A0A7101200097012000A3812000A40000000FFD0000000DEADCAFE30000000109C9BF01800000019F000000012012800000001D0000000DEADCAFE0002000040000000400000100000000030000000400000001000000041F00000001200001058FA5400120008000000110012000C00000001001200103F8000000012001400000011001200184000003000120064400001B40012019C0000000801100124000000681078314400000000006800650061006400000000000000004000008000000004107831440000000000630068006500730074000000000000400000A0000000051078314400000000006C0065006700730000000000000000400000C000000004107831440000000000660065006500740000000000000000400000E0000000041078314400000000006F0066006600680061006E0064000040000100000000071078314400000000006D00610069006E00680061006E00644000012000000008004100740074007200690062007500740065004D006F006400690066006900650072007300000049004400000041006D006F0075006E00740000004F007000650072006100740069006F006E00000053006C006F00740000000000550055004900440000000000FF0012019440000138001201A0400001C0001201A4400004CC01100020000001B01067DAF000000000400001E0400001E8400001F00A000000000000000000000000000000000000FF01100008000001D0400001F84000030800000000000000FF31000000000001E8001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000218011000A0000000644000027C0000000000000000000000004000015E0000000000000008400002804000029C1065993C0000000200000000400001640000000000000008400002A0400002BC1065993C0000000A00000000400001720000000000000008400002C0400002DC1065993C0000000100000000400001920000000000000008400002E0400002FC1065993C00000001000000004000018600000000000000084000011800000000000000FF3100000000000110001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000328011000A0000000644000038C0000000000000000000000004000015E000000000000000840000390400003AC1065993C0000000800000000400001640000000000000008400003B0400003CC1065993C7FFFFFFF00000000400001720000000000000008400003D0400003EC1065993C0000000100000000400001920000000000000008400003F04000040C1065993C00000002000000004000018600000000000000084000011800000000000000FFD0000000DEADCAFE0002000040000418400004280000000030000000400004181000000041F000000110001C000000001058FA540000000000000011000000013F8000000000001140000448000000FF0110006C00000064400004CC0055006E0062007200650061006B00610062006C0065000000480069006400650046006C0061006700730000400004900000000000000008400004D0400004EC1065993C0000000100000000400004A80000000000000008400004F0000000001065993C00000000000000FFD0000000DEADCAFE00020000400004F8400005080000000030000000400004F81000000041F00000001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000528001200644000060C001200FC000000080110007E000000680043007500730074006F006D0050006F00740069006F006E00450066006600650063007400730000004900640000004400750072006100740069006F006E00000041006D0070006C0069006600690065007200000041006D006200690065006E0074000000530068006F0077005000610072007400690063006C0065007300FF001200F4400005700012010040000618001201040000000001100020000001101067DAF0000000004000063840000640400006480A000000000000000000000000000000000000FF0110000800000130400006504000076000000000000000FF3100000000000148001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000670011000AC00000064400006D4000000000000000000000000400005980000000000000008400006D8400006F41065993C00000001000000004000059E0000000000000008400006F8400007141065993C0000258000000000400005B0000000000000000840000718400007341065993C0000000000000000400005C4000000000000000840000738400007541056415C0100000000000000400005D4000000000000000840000758000000001056415C01000000000000FF3100000000000110001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000780011000AC00000064400007E4000000000000000000000000400005980000000000000008400007E8400008041065993C00000005000000004000059E000000000000000840000808400008241065993C0000258000000000400005B0000000000000000840000828400008441065993C0000000100000000400005C4000000000000000840000848400008641056415C0100000000000000400005D4000000000000000840000868000000001056415C01000000000000FFD0000000DEADCAFE0002000040000870400008800000000030000000400008701000000041F00000001200001058FA5400120008000000110012000C00000001001200103F800000001200140000001100120018400008A00012006440000984001200FC000000080110007E000000680043007500730074006F006D0050006F00740069006F006E00450066006600650063007400730000004900640000004400750072006100740069006F006E00000041006D0070006C0069006600690065007200000041006D006200690065006E0074000000530068006F0077005000610072007400690063006C0065007300FF001200F4400008E80012010040000990001201040000000001100020000001101067DAF000000000400009B0400009B4400009BC0A000000000000000000000000000000000000FF0110000800000130400009C440000AD400000000000000FF3100000000000144001200001058FA5400120008000000110012000C00000001001200103F800000001200140000001100120018400009E4011000AC0000006440000A4800000000000000000000000040000910000000000000000840000A4C40000A681065993C0000000F0000000040000916000000000000000840000A6C40000A881065993C00000E100000000040000928000000000000000840000A8C40000AA81065993C000000FF000000004000093C000000000000000840000AAC40000AC81056415C01000000000000004000094C000000000000000840000ACC000000001056415C01000000000000FFD0000000DEADCAFE0002000040000AD440000AE4000000003000000040000AD41000000041F00000001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000B040012006440000BE8001200FC000000080110007E000000680043007500730074006F006D0050006F00740069006F006E00450066006600650063007400730000004900640000004400750072006100740069006F006E00000041006D0070006C0069006600690065007200000041006D006200690065006E0074000000530068006F0077005000610072007400690063006C0065007300FF001200F440000B4C0012010040000BF4001201040000000001100020000001101067DAF00000000040000C1440000C1840000C200A000000000000000000000000000000000000FF011000080000013040000C2840000D3800000000000000FF3100000000000144001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000C48011000AC0000006440000CAC00000000000000000000000040000B74000000000000000840000CB040000CCC1065993C000000090000000040000B7A000000000000000840000CD040000CEC1065993C00000E100000000040000B8C000000000000000840000CF040000D0C1065993C000000FF0000000040000BA0000000000000000840000D1040000D2C1056415C010000000000000040000BB0000000000000000840000D30000000001056415C01000000000000FFD0000000DEADCAFE0002000040000D3840000D48000000003000000040000D381000000041F00000001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000D680012006440000E4C001200FC000000080110007E000000680043007500730074006F006D0050006F00740069006F006E00450066006600650063007400730000004900640000004400750072006100740069006F006E00000041006D0070006C0069006600690065007200000041006D006200690065006E0074000000530068006F0077005000610072007400690063006C0065007300FF001200F440000DB00012010040000E58001201040000000001100020000001101067DAF00000000040000E7840000E7C40000E840A000000000000000000000000000000000000FF011000080000013040000E8C40000F9C00000000000000FF3100000000000144001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000EAC011000AC0000006440000F1000000000000000000000000040000DD8000000000000000840000F1440000F301065993C000000190000000040000DDE000000000000000840000F3440000F501065993C00000E100000000040000DF0000000000000000840000F5440000F701065993C000000010000000040000E04000000000000000840000F7440000F901056415C010000000000000040000E14000000000000000840000F94000000001056415C01000000000000FFD0000000DEADCAFE0002000040000F9C40000FAC000000003000000040000F9C1000000041F00000001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840000FCC00120064400010B0001200FC000000080110007E000000680043007500730074006F006D0050006F00740069006F006E00450066006600650063007400730000004900640000004400750072006100740069006F006E00000041006D0070006C0069006600690065007200000041006D006200690065006E0074000000530068006F0077005000610072007400690063006C0065007300FF001200F44000101400120100400010BC001201040000000001100020000001101067DAF000000000400010DC400010E0400010E80A000000000000000000000000000000000000FF0110000800000130400010F04000120000000000000000FF3100000000000144001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840001110011000AC00000064400011740000000000000000000000004000103C000000000000000840001178400011941065993C000000190000000040001042000000000000000840001198400011B41065993C00000E1000000000400010540000000000000008400011B8400011D41065993C0000000500000000400010680000000000000008400011D8400011F41056415C0100000000000000400010780000000000000008400011F8000000001056415C01000000000000FFD0000000DEADCAFE0002000040001200400012100000000030000000400012001000000041F00000001200001058FA5400120008000000110012000C00000001001200103F800000001200140000001100120018400012300012006440001314001200FC000000080110007E000000680043007500730074006F006D0050006F00740069006F006E00450066006600650063007400730000004900640000004400750072006100740069006F006E00000041006D0070006C0069006600690065007200000041006D006200690065006E0074000000530068006F0077005000610072007400690063006C0065007300FF001200F4400012780012010040001320001201040000000001100020000001101067DAF00000000040001340400013444000134C0A000000000000000000000000000000000000FF0110000800000130400013544000146400000000000000FF3100000000000144001200001058FA5400120008000000110012000C00000001001200103F80000000120014000000110012001840001374011000AC00000064400013D8000000000000000000000000400012A00000000000000008400013DC400013F81065993C0000001900000000400012A60000000000000008400013FC400014181065993C00000E1000000000400012B800000000000000084000141C400014381065993C000000FF00000000400012CC00000000000000084000143C400014581056415C0100000000000000400012DC00000000000000084000145C000000001056415C01000000000000FFD0000000DEADCAFE0002000040001464400014740000000030000000400014641000000041F00000001200001058FA5400120008000000110012000C00000001001200103F800000001200140000001100120018400014940012006440001578001200FC000000080110007E000000680043007500730074006F006D0050006F00740069006F006E00450066006600650063007400730000004900640000004400750072006100740069006F006E00000041006D0070006C0069006600690065007200000041006D006200690065006E0074000000530068006F0077005000610072007400690063006C0065007300FF001200F4400014DC0012010040001584001201040000000001100020000001101067DAF000000000400015A4400015A8400015B00A000000000000000000000000000000000000FF0110000800000130400015B8400016C800000000000000FF3100000000000144001200001058FA5400120008000000110012000C00000001001200103F800000001200140000001100120018400015D8011000AC000000644000163C000000000000000000000000400015040000000000000008400016404000165C1065993C00000006000000004000150A0000000000000008400016604000167C1065993C00000000000000004000151C0000000000000008400016804000169C1065993C0000000200000000400015300000000000000008400016A0400016BC1056415C0100000000000000400015400000000000000008400016C0000000001056415C01000000000000FFD0000000DEADCAFE00020000400016C8400016D80000000030000000400016C81000000041F000000110001C000000001058FA540000000000000011000000013F80000000000011400016F8000000FF0110003400000064400017AC0043007500730074006F006D0050006F00740069006F006E0043006F006C006F007200000050006F00740069006F006E000000FF31000000000000A4011000540000000040001740000000000000000840001790400017AC1065993C0000000000000000400017640000000000000008400017B040001578107831440000000000000000000000000000000000000000400017D000000018000000FF0110003000000054006D0069006E006500630072006100660074003A007300740072006F006E0067005F006800650061006C0069006E006700000000000000FFD0000000DEADCAFE' # Cafe Code
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

