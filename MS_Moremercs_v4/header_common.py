###################################################
# header_common.py
# This file contains common declarations.
# DO NOT EDIT THIS FILE!
###################################################

bignum = 0x40000000000000000000000000000000

op_num_value_bits = 24 + 32

tag_register        =  1
tag_variable        =  2
tag_string          =  3
tag_item            =  4
tag_troop           =  5
tag_faction         =  6
tag_quest           =  7
tag_party_tpl       =  8
tag_party           =  9
tag_scene           = 10
tag_mission_tpl     = 11
tag_menu            = 12
tag_script          = 13
tag_particle_sys    = 14
tag_scene_prop      = 15
tag_sound           = 16
tag_local_variable  = 17
tag_map_icon        = 18
tag_skill           = 19
tag_mesh            = 20
tag_presentation    = 21
tag_quick_string    = 22
tag_track	    = 23
tag_tableau         = 24
tag_animation       = 25
tags_end            = 26


opmask_register             =  tag_register       << op_num_value_bits
opmask_variable             =  tag_variable       << op_num_value_bits
##opmask_string             =  tag_string         << op_num_value_bits
##opmask_item_index         =  tag_item           << op_num_value_bits
##opmask_troop_index        =  tag_troop          << op_num_value_bits
##opmask_faction_index      =  tag_faction        << op_num_value_bits
opmask_quest_index          =  tag_quest          << op_num_value_bits
##opmask_p_template_index   =  tag_party_tpl      << op_num_value_bits
##opmask_party_index        =  tag_party          << op_num_value_bits
##opmask_scene_index        =  tag_scene          << op_num_value_bits
##opmask_mission_tpl_index  =  tag_mission_tpl    << op_num_value_bits
##opmask_menu_index         =  tag_menu           << op_num_value_bits
##opmask_script             =  tag_script         << op_num_value_bits
##opmask_particle_sys       =  tag_particle_sys   << op_num_value_bits
##opmask_scene_prop         =  tag_scene_prop     << op_num_value_bits
##opmask_sound              =  tag_sound          << op_num_value_bits
##opmask_map_icon           =  tag_map_icon       << op_num_value_bits
opmask_local_variable       =  tag_local_variable << op_num_value_bits
opmask_quick_string         =  tag_quick_string   << op_num_value_bits


def reg(reg_no):
  if (reg_no < 0):
    print ("Error register_no negative")
    cause_error()
  return opmask_register | reg_no

def find_object(objects,object_id):
  result = -1
  num_objects = len(objects)
  i_object = 0
  object_id_lowercase = object_id.lower()
  while (i_object < num_objects) and (result == -1):
    object = objects[i_object]
    if (object[0].lower() == object_id_lowercase):
      result = i_object
    i_object += 1
  return result

s0  =  0
s1  =  1
s2  =  2
s3  =  3
s4  =  4
s5  =  5
s6  =  6
s7  =  7
s8  =  8
s9  =  9
s10 = 10
s11 = 11
s12 = 12
s13 = 13
s14 = 14
s15 = 15
s16 = 16
s17 = 17
s18 = 18
s19 = 19
s20 = 20
s21 = 21
s22 = 22
s23 = 23
s24 = 24
s25 = 25
s26 = 26
s27 = 27
s28 = 28
s29 = 29
s30 = 30
s31 = 31
s32 = 32
s33 = 33
s34 = 34
s35 = 35
s36 = 36
s37 = 37
s38 = 38
s39 = 39
s40 = 40
s41 = 41
s42 = 42
s43 = 43
s44 = 44
s45 = 45
s46 = 46
s47 = 47
s48 = 48
s49 = 49
s50 = 50
s51 = 51
s52 = 52
s53 = 53
s54 = 54
s55 = 55
s56 = 56
s57 = 57
s58 = 58
s59 = 59
s60 = 60
s61 = 61
s62 = 62
s63 = 63

s64 = 64
s65 = 65
s66 = 66
s67 = 67


pos0  =  0
pos1  =  1
pos2  =  2
pos3  =  3
pos4  =  4
pos5  =  5
pos6  =  6
pos7  =  7
pos8  =  8
pos9  =  9
pos10 = 10
pos11 = 11
pos12 = 12
pos13 = 13
pos14 = 14
pos15 = 15
pos16 = 16
pos17 = 17
pos18 = 18
pos19 = 19
pos20 = 20
pos21 = 21
pos22 = 22
pos23 = 23
pos24 = 24
pos25 = 25
pos26 = 26
pos27 = 27
pos28 = 28
pos29 = 29
pos30 = 30
pos31 = 31
pos32 = 32
pos33 = 33
pos34 = 34
pos35 = 35
pos36 = 36
pos37 = 37
pos38 = 38
pos39 = 39
pos40 = 40
pos41 = 41
pos42 = 42
pos43 = 43
pos44 = 44
pos45 = 45
pos46 = 46
pos47 = 47
pos48 = 48
pos49 = 49
pos50 = 50
pos51 = 51
pos52 = 52
pos53 = 53
pos54 = 54
pos55 = 55
pos56 = 56
pos57 = 57
pos58 = 58
pos59 = 59
pos60 = 60
pos61 = 61
pos62 = 62
pos63 = 63
pos_belfry_begin = 64

reg0   = opmask_register| 0
reg1   = opmask_register| 1
reg2   = opmask_register| 2
reg3   = opmask_register| 3
reg4   = opmask_register| 4
reg5   = opmask_register| 5
reg6   = opmask_register| 6
reg7   = opmask_register| 7
reg8   = opmask_register| 8
reg9   = opmask_register| 9
reg10  = opmask_register|10
reg11  = opmask_register|11
reg12  = opmask_register|12
reg13  = opmask_register|13
reg14  = opmask_register|14
reg15  = opmask_register|15
reg16  = opmask_register|16
reg17  = opmask_register|17
reg18  = opmask_register|18
reg19  = opmask_register|19
reg20  = opmask_register|20
reg21  = opmask_register|21
reg22  = opmask_register|22
reg23  = opmask_register|23
reg24  = opmask_register|24
reg25  = opmask_register|25
reg26  = opmask_register|26
reg27  = opmask_register|27
reg28  = opmask_register|28
reg29  = opmask_register|29
reg30  = opmask_register|30
reg31  = opmask_register|31
reg32  = opmask_register|32
reg33  = opmask_register|33
reg34  = opmask_register|34
reg35  = opmask_register|35
reg36  = opmask_register|36
reg37  = opmask_register|37
reg38  = opmask_register|38
reg39  = opmask_register|39
reg40  = opmask_register|40
reg41  = opmask_register|41
reg42  = opmask_register|42
reg43  = opmask_register|43
reg44  = opmask_register|44
reg45  = opmask_register|45
reg46  = opmask_register|46
reg47  = opmask_register|47
reg48  = opmask_register|48
reg49  = opmask_register|49
reg50  = opmask_register|50
reg51  = opmask_register|51
reg52  = opmask_register|52
reg53  = opmask_register|53
reg54  = opmask_register|54
reg55  = opmask_register|55
reg56  = opmask_register|56
reg57  = opmask_register|57
reg58  = opmask_register|58
reg59  = opmask_register|59
reg60  = opmask_register|60
reg61  = opmask_register|61
reg62  = opmask_register|62
reg63  = opmask_register|63

reg65  = opmask_register|65
