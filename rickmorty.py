def get_season_files(season, episodes, dataset_dir='./dataset'):
    files = []
    for episode in episodes:
        myfile = dataset_dir +'/season' + str(season) + '/episode' + str(episode) + '.txt'
        files.append(myfile)
    return files

def parse_episode(episode_file):
    cues = []
    name = ''
    with open(episode_file, encoding = 'utf-8') as text:
        for line in text:
            line = clear_text(line)
            old_name = name
            if line == '' or line[0] == '(' and line[-1] == ')':
                continue
            else:
                parts = line.split(':', maxsplit=1)
                replic = parts[-1]
                words = replic.split()
                if len(parts) == 1:
                    name = old_name
                else:
                    name = parts[0]
                cues.append((name,words))
    return cues

def clear_text(text):
    trash_symbols = '!"#$%&\'-()*+,./;<=>?@[\\]^_`{|}~«»—'

    return text.strip(trash_symbols)
def main():
    files = get_season_files(1,[1,2,3,4,5,6,7,8,9,10])
    cues = parse_episode(files[0])
    print(cues)

if __name__ == '__main__':
    main()

