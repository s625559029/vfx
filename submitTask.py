#!/usr/bin/env python
# submit wedge render task to DPA queue

import os
import time
import datetime

# directory
QUEUE = "brie"
SCRIPT_ROOT_DIR = "/DPA/jedi/xiaohao/script/"
EXE_DIR = "/DPA/jedi/xiaohao/Wedges/cmake-build-debug/wedges"
OUTPUT_ROOT_DIR = "/DPA/jedi/xiaohao/output"


start_frame = 0
task_num = 300
# wedge_type_dict = {"pyro": "-p", "noise": "-n", "wisp": "-w"}
wedge_type_dict = {"pipe": "-pipe"}


def submitTask():
    timestamp = time.time()
    dates = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d-%H-%M-%S')
    script_dir = os.path.join(SCRIPT_ROOT_DIR, dates)
    output_dir = os.path.join(OUTPUT_ROOT_DIR, dates)
    print "Script path: ", script_dir
    print "Output path: ", output_dir
    # create script path
    os.system("mkdir {}".format(script_dir))
    os.system("chmod 777 {}".format(script_dir))
    # create output path
    os.system("mkdir {}".format(output_dir))
    os.system("chmod 777 {}".format(output_dir))
    # generate script
    for (wedge_type, tag) in wedge_type_dict.items():
        for frame_id in xrange(start_frame, task_num):
            filename = "{}-{:04d}.sh".format(wedge_type, frame_id)
            filepath = os.path.join(script_dir, filename)
            f = open(filepath, 'w')
            f.write("#!/bin/bash\n")
            f.write("{exe} {tag} {startid} {endid} {out}\n".format(exe=EXE_DIR, tag=tag, startid=frame_id, endid=frame_id+1, out=output_dir))
            f.close()
            # chmod for script file
            os.system("chmod 777 {file}".format(file=filepath))
    print "Scripts generation complete."

    # submit task for each script
    num = 0
    for root, dir, files in os.walk(script_dir):
        for name in files:
            script_path = os.path.join(root, name)
            # there's .log file in the same dir
            if script_path.endswith('.sh'):
                frameid = int(script_path.split('/')[-1].split('-')[1].split('.')[0])
                print "Submit task for frame {:04d} from script {}...".format(frameid, script_path)
                os.system("cqsubmittask {queue} {script}".format(queue=QUEUE, script=script_path))
                num += 1

    print "Submission complete."
    print "\t | Task Num: ", num

if __name__ == '__main__':
    submitTask()
