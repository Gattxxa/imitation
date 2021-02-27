def create(ul, ur, ll, lr):

  # upperLeft
  if ul == 1:
    upperLeft = '<:hytusx_1_0:813677968496918539>'
  elif ul == 2:
    upperLeft = '<:hytusx_1_90:813677968316039179>'
  elif ul == 3:
    upperLeft = '<:hytusx_1_180:813677969335779368>'
  elif ul == 4:
    upperLeft = '<:hytusx_1_270:813677969309958174>'
  elif ul == 5:
    upperLeft = '<:k_electory_1_0:813681135351234600>'
  elif ul == 6:
    upperLeft = '<:k_electory_1_90:813681132532006943>'
  elif ul == 7:
    upperLeft = '<:k_electory_1_180:813681133384237066>'
  elif ul == 8:
    upperLeft = '<:k_electory_1_270:813681133341376532>'

  # upperRight
  if ur == 1:
    upperRight = '<:hytusx_2_0:813677969129340949>'
  elif ur == 2:
    upperRight = '<:hytusx_2_90:813677969288462386>'
  elif ur == 3:
    upperRight = '<:hytusx_2_180:813677969410621462>'
  elif ur == 4:
    upperRight = '<:hytusx_2_270:813677969112694785>'
  elif ur == 5:
    upperRight = '<:k_electory_2_0:813681133421199370>'
  elif ur == 6:
    upperRight = '<:k_electory_2_90:813681133094436905>'
  elif ur == 7:
    upperRight = '<:k_electory_2_180:813681133555679273>'
  elif ur == 8:
    upperRight = '<:k_electory_2_270:813681133090242561>'

  # lowerLeft
  if ll == 1:
    lowerLeft = '<:hytusx_3_0:813677969104306177>'
  elif ll == 2:
    lowerLeft = '<:hytusx_3_90:813677969389649920>'
  elif ll == 3:
    lowerLeft = '<:hytusx_3_180:813677968986865686>'
  elif ll == 4:
    lowerLeft = '<:hytusx_3_270:813677969032609823>'
  elif ll == 5:
    lowerLeft = '<:k_electory_3_0:813681133656604682>'
  elif ll == 6:
    lowerLeft = '<:k_electory_3_90:813681133534838804>'
  elif ll == 7:
    lowerLeft = '<:k_electory_3_180:813681133513736243>'
  elif ll == 8:
    lowerLeft = '<:k_electory_3_270:813681133300482049>'

  # lowerRight
  if lr == 1:
    lowerRight = '<:hytusx_4_0:813677969322541057>'
  elif lr == 2:
    lowerRight = '<:hytusx_4_90:813677969037328436>'
  elif lr == 3:
    lowerRight = '<:hytusx_4_180:813677969352556584>'
  elif lr == 4:
    lowerRight = '<:hytusx_4_270:813677969263296582>'
  elif lr == 5:
    lowerRight = '<:k_electory_4_0:813681133161152543>'
  elif lr == 6:
    lowerRight = '<:k_electory_4_90:813681133375717397>'
  elif lr == 7:
    lowerRight = '<:k_electory_4_180:813681133295239200>'
  elif lr == 8:
    lowerRight = '<:k_electory_4_270:813681133505740840>'

  kashiwa = upperLeft + upperRight + "\n" + lowerLeft + lowerRight
  
  return kashiwa