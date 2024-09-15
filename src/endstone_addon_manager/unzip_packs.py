import zipfile, os, shutil, re, json

# search manifest file
def search_manifest(dir):
    manifest_paths = []

    for root, dirs, files in os.walk(dir):
        if 'manifest.json' in files:
            manifest_path = os.path.join(root, 'manifest.json')
            manifest_paths.append(manifest_path)

    if len(manifest_paths) == 1:
        return os.path.dirname(manifest_paths[0])
    elif len(manifest_paths) > 1:
        return None
    else:
        return None

# unzip file
def unzip(zip_file, od):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(od)

packs_dir = "./plugins/endstone_addonmanager/packs/"
bds_dir = "./"

if not os.path.exists(packs_dir):
    os.makedirs(packs_dir)
else:
    pack_full_name = os.listdir(packs_dir)
    for p in pack_full_name:
        
        tmp_type = p.split('.')[-1]
        print(tmp_type)
        tmp_name = p.split('.')[0]
        print(tmp_name)
        
        extract_dir = packs_dir + tmp_type + "_" + tmp_name
        print(extract_dir)
        unzip(packs_dir + p,extract_dir)
        right_pack_dir = search_manifest(extract_dir)
        print(right_pack_dir)

        if right_pack_dir != None:
            
            # get right path to place
            with open(bds_dir + "server.properties", "r") as f: 
                data = f.read()
            match = re.search("level-name=",data)
            rp_dir = bds_dir + "'" + match.group() + "'/resource_packs/"
            bp_dir = bds_dir + "'" + match.group() + "'/behavior_packs/"
            print(rp_dir)
            print(bp_dir)

            # get the type of pack
            with open(right_pack_dir + "/manifest.json", "r") as f:
                manifest_data = f.read()
            format_data = json.loads(manifest_data)
            post_install_command = format_data['commands']['post_install'][0]
            ptype = re.search("type", post_install_command)
            right_pack_type = ptype.group()
            print(right_pack_type)

            if right_pack_type == "resources":
                shutil.move(right_pack_dir,rp_dir)
                #write info
            elif right_pack_type == "data":
                shutil.move(right_pack_dir,bp_dir)
                #write info
            else:
                    print("Don't support this pack!")
        else:
            print("Broken pack!")
