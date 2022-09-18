import os
import time

import matplotlib.pyplot as plt

from utils import *

device = torch.device('cuda')
IS_EVALUATION = False
MAX_TEST_NUM = 20 if IS_EVALUATION else 1000



def main(task_id):
    model, test_loader, vocab_tgt, vocab_src = load_model_data(task_id)
    model = model.to(device)
    model.set_device(device)

    config = {
        "PAD_ID":  model.PAD_ID,
        "SOS_ID":  model.SOS_ID,
        "EOS_ID":  model.EOS_ID,
        "UNK_ID":  model.UNK_ID,
        'sp_token': [],
        'vocab_size': len(vocab_src),
        'src_vocab': vocab_src,
        'tgt_vocab': vocab_tgt,
        'max_length': model.max_length,
        'mutate_num': model.mutate_num,
        'mutate_rate': model.mutate_rate
    }

    exp_list = [exp(model, config, device) for exp in EXPLAIN_LIST]
    base_exp = BaseExpClass(model, config, device)
    exp_res = [[] for _ in range(len(exp_list))]
    final_deduction_res = [[] for _ in range(len(exp_list))]
    final_augment_res = [[] for _ in range(len(exp_list))]
    final_sys_res = [[] for _ in range(len(exp_list))]

    for i, batch in tqdm(enumerate(test_loader)):
        if i > MAX_TEST_NUM:
            break
        if task_id == 0:
            src_tk, src_len, tgt_tk, tgt_len = batch  # deepAPI
        elif task_id == 1:
            src_tk, src_len = batch[0], batch[1].sum(1)
        elif task_id == 2:
            src_tk, src_len = batch, torch.tensor(len(batch[0])).reshape([-1, 1])
        else:
            raise NotImplementedError
        for jjj, exp in enumerate(exp_list):
            explain, out_tk, out_len = exp.explain([src_tk, src_len])
            assert type(out_len) == int
            assert len(explain) == out_len


if __name__ == '__main__':
    seed = 101
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)

    parser = argparse.ArgumentParser(description='Measure Latency')
    parser.add_argument('--task', default=0, type=int, help='experiment subjects')
    args = parser.parse_args()
    main(args.task)
