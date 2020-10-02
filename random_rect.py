def random_rect(img, area):
  assert 0<=area<=1, "area should be a valid fraction"

  a, b = np.random.uniform(), np.random.uniform()
  a, b = math.sqrt(area*a/b), math.sqrt(area*b/a)
  if a>1:
    a = 1
    b = area
  elif b>1:
    a = area
    b = 1
  
  sx, sy = np.random.uniform(low = 0, high = 1-a), np.random.uniform(low = 0, high = 1-b)
  ex, ey = sx+a, sy+b
  sx, sy = math.floor(sx*img.shape[0]), math.floor(sy*img.shape[1])
  ex, ey = math.floor(ex*img.shape[0]), math.floor(ey*img.shape[1])
    
  rect_img = img.copy()
  rect_img[sx:ex, sy:ey, :] = 0

  
  mask = np.zeros(img.shape[:2])
  mask[sx:ex,sy:ey] = 1
  
  return rect_img, mask