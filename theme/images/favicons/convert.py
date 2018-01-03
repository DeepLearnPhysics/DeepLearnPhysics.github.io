import os,sys 

targets = [f for f in os.listdir(sys.argv[1]) if f.endswith('.png') and len(f.rstrip('.png').split('-')[-1].split('x'))==2]
source  = sys.argv[2]
if not os.path.isfile(source):
    print 'source',source,'does not exist...'
    sys.exit(1)

for f in targets:

    target = os.path.join(sys.argv[1],f)
    sizearg = f.rstrip('.png').split('-')[-1]

    os.system('convert %s -resize %s %s' % (source,sizearg,f))
    


