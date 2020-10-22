import json


def f(a, b):
    # First time 'a' is a string, next iterations it is a dict
    y = json.loads(a) if isinstance(a, str) else a
    ret = {}
    for item in b:
        # Split for '.'
        x = item.split('.', 1)
        # Verify if the item has children
        if len(x) == 1:
            s = x[0].split('[', 1)
            if item in y:
                if isinstance(a, str):
                    ret[item] = y[item]
                else:
                    return y[item]
            else:
                try:
                    # Verify if item is an array
                    if isinstance(y[s[0]], list):
                        try:
                            r = s[1].split(']', 1)
                            u = y[s[0]][int(r[0])]
                            ret[item] = u
                        except Exception:
                            None
                except Exception:
                    None
        # If item has children
        else:
            s = x[0].split('[', 1)
            try:
                # Verify if the first level is an array
                if isinstance(y[s[0]], list):
                    try:
                        r = s[1].split(']', 1)
                        u = y[s[0]][int(r[0])]
                        v = []
                        v.append(x[1])
                        z = f(u, v)
                        ret[item] = z
                    except Exception:
                        None
                else:
                    w = x[1].split('.', 1)
                    # Verify if not is the first iteration
                    if not isinstance(a, str):
                        v = []
                        v.append(x[1])
                        z = f(y[x[0]], v)
                        return z                    
                    # Verify if the item is an object
                    if isinstance(y[x[0]], dict) and w[0] in y[x[0]]:
                        v = []
                        v.append(x[1])
                        z = f(y[x[0]], v)
                        ret[item] = z
                    else:
                        try:
                            s = x[1].split('[', 1)
                            # Verify if the next level is an array
                            if isinstance(y[s[0]], list):
                                try:
                                    r = s[1].split(']', 1)
                                    u = y[s[0]][int(r[0])]
                                    ret[item] = u
                                except Exception:
                                    None
                        except Exception:
                                    None
            except Exception:
                None
    # Clean empty values
    res = {k: v for k, v in ret.items() if v}
    return res
