import torch
import time

if torch.cuda.is_available():
	print("CUDA available")
else:
	print("CPU only")

# with torch.no_grad():
#     # 程序计时开始
#     time_start = time.time()
#
#     tensor1 = torch.randn(100, 1000, 1000)
#     tensor2 = torch.randn(100, 1000, 1000)
#
#     result = tensor1 * tensor2
#     for i in range(1000):
#         result = result + tensor1 * tensor2
#
#     # 程序片段后插入以下两行
#     time_end = time.time()
#     print('Time cost on CPU = %fs' % (time_end - time_start))
#
#
#     # 程序计时开始
#     time_start = time.time()
#
#     tensor1 = torch.randn(100, 1000, 1000).cuda()
#     tensor2 = torch.randn(100, 1000, 1000).cuda()
#
#     result = tensor1 * tensor2
#     for i in range(1000):
#         result = result + tensor1 * tensor2
#
#     # 程序片段后插入以下两行
#     time_end = time.time()
#     print('Time cost on GPU = %fs' % (time_end - time_start))