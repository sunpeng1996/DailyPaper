---
title: Channel Selection for Mixture-of-Experts Decoding Needs No Calibration Data
title_zh: 无需校准数据的MoE大模型解码通道选择方案
authors:
- Geunhyoung Kim
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2610.37386'
url: https://arxiv.org/abs/2610.37386
pdf_url: https://arxiv.org/pdf/2610.37386
published: '2026-10-26'
collected: '2026-10-28'
category: LLM
direction: LLM MoE推理 · 无校准通道稀疏优化
tags:
- MoE
- LLM Inference
- Channel Pruning
- Sparsity
- Top-k Selection
one_liner: 证明MoE解码通道选择无需校准数据，提出无校准top-k方案与纯权重reader，兼顾高准确率与解码加速
practical_value: '- 业务侧用MoE LLM做生成式推荐、Agent多轮对话、Query改写时，直接用top-k替代原有校准阈值的通道选择规则，可避免校准数据分布偏移导致的效果下降、长文本重复生成等问题，无需额外准备校准数据

  - 可直接复用论文提出的纯权重reader方案：三元sketch预打分+低秩恢复跳过通道，无需重新训练MoE模型，即可在几乎无损效果的前提下降低推理显存占用、提升吞吐，适配电商高并发的文案生成、广告创意生成场景

  - 工程上可直接复用其开源的Triton kernel实现，小批量（batch≤16）的用户实时请求场景下，MoE模块提速1.6~2.69倍，全模型提速最高1.88倍，优于优化后的vLLM
  baseline'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MoE模型小批量交互式解码时，路由专家权重的内存读取是延迟瓶颈，现有通道选择方案依赖离线校准数据设置阈值，存在实际读取量偏离目标预算、校准数据分布漂移导致效果下降的问题，甚至会触发长推理场景的重复循环崩溃，亟需无校准的高效通道选择方案。
### 方法关键点
- 通道保留规则直接采用per-token top-k替代校准阈值，无需任何校准数据，每个token固定保留k个得分最高的通道，确保读取预算100%可控
- 提出纯基于预训练权重构建的reader：① 用旋转三元sketch（仅占BF16 checkpoint的7%）预打分所有候选通道，低开销得到通道贡献估计；② 按输出单位缩放得分，跨所有路由专家选top-k通道做精确计算；③ 用权重SVD得到的低秩映射恢复跳过通道的贡献，仅额外增加0.5%显存开销
- 配套优化Triton kernel，适配GPU 32字节内存扇区读取特性，减少无效内存访问
### 关键结果
在Qwen3-Thinking、Gemma 4、Qwen3.5三个主流MoE模型上测试，对比Prox、TEAL、WINA等现有方案：17.8%读取预算下保留98.1%的全模型准确率；MoE block推理速度比优化后的vLLM最高快2.69倍，全模型解码batch=1时提速1.15~1.36倍，batch=8/16时最高提速1.88倍；43组对比实验中top-k规则在40组里持平或超过校准阈值方案，完全避免Gemma 4的重复生成崩溃问题。
最值得记住的一句话：MoE解码通道选择的校准阈值既不能保证稳定的读取预算，也不能带来一致的准确率提升，无校准的top-k方案是更可靠的选择
