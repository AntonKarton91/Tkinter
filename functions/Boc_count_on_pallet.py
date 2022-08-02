# Расчет количества коробок на паллете

def get_boxOnPalletXY(l_box, w_box, L_PALLET, W_PALLET):
    count_x1 = L_PALLET // l_box
    count_y1 = W_PALLET // w_box
    sum_xy1 = count_x1 * count_y1
    count_x2 = L_PALLET // w_box
    count_y2 = W_PALLET // l_box
    sum_xy2 = count_x2 * count_y2
    sum_xy = sum_xy1 if sum_xy1 >= sum_xy2 else sum_xy2
    return sum_xy


def get_boxOnPalletZ(h_box, H_PRODUCT):
    count_z = H_PRODUCT // h_box
    return count_z


def get_boxOnPallet(l_box, w_box, h_box, L_PALLET, W_PALLET, H_PRODUCT):
    c1 = get_boxOnPalletXY(l_box, w_box, L_PALLET, W_PALLET) * get_boxOnPalletZ(h_box, H_PRODUCT)
    c2 = get_boxOnPalletXY(l_box, h_box, L_PALLET, W_PALLET) * get_boxOnPalletZ(w_box, H_PRODUCT)
    c3 = get_boxOnPalletXY(w_box, h_box, L_PALLET, W_PALLET) * get_boxOnPalletZ(l_box, H_PRODUCT)
    res = max(c1, c2, c3)

    if res==c1:
        row_count=get_boxOnPalletXY(l_box, w_box, L_PALLET, W_PALLET)
        coll_count=get_boxOnPalletZ(h_box, H_PRODUCT)
    elif res==c2:
        row_count=get_boxOnPalletXY(l_box, h_box, L_PALLET, W_PALLET)
        coll_count=get_boxOnPalletZ(w_box, H_PRODUCT)
    else:
        row_count=get_boxOnPalletXY(w_box, h_box, L_PALLET, W_PALLET)
        coll_count=get_boxOnPalletZ(l_box, H_PRODUCT)

    return res, [row_count,coll_count]

def pallet(l_pallet,w_pallet, h_absolute,l_box, w_box, h_box, overhang):
    L_PALLET = l_pallet+overhang
    W_PALLET = w_pallet+overhang
    H_ABSOLUTE = h_absolute
    H_PRODUCT = H_ABSOLUTE - 150
    return get_boxOnPallet(l_box, w_box, h_box, L_PALLET, W_PALLET, H_PRODUCT)

