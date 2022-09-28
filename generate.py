from shutil import copyfile

def get_sample(a):
    bd, n, d = a.split()
    return f"""
    b_{bd}_{n}
    d
    s_{d}
    d
    s_015
    d
    """.strip().split()

samples = [
    "d", "d", "d",
    *get_sample("a 30 060"),
    *get_sample("a 30 060"),
    *get_sample("b 30 090"),
    *get_sample("b 30 090"),
    *get_sample("b 30 120"),
    *get_sample("c 30 120"),
    *get_sample("c 30 150"),
    *get_sample("c 30 150"),
    *get_sample("c 30 150"),
    *get_sample("c 30 150"),
    *get_sample("c 30 180"),
    *get_sample("c 30 180"),
    *get_sample("c 30 180"),
    *get_sample("c 30 180"),
]

for i, s in enumerate(samples):
    copyfile(f"sounds/{s}.mp3", f"playlist/{i:03d}_{s}.mp3")
