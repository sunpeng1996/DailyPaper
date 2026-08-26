---
title: 'NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal
  Redistribution'
title_zh: NeuronGuard：通过消融感知安全信号重分布实现鲁棒LLM安全对齐
authors:
- Anjun Gao
- Yueyang Quan
- Yufei Xia
- Zhuqing Liu
- Minghong Fang
affiliations:
- University of Louisville
- University of North Texas
arxiv_id: '2608.23959'
url: https://arxiv.org/abs/2608.23959
pdf_url: https://arxiv.org/pdf/2608.23959
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: LLM安全对齐 · 鲁棒性防御
tags:
- LLM Safety
- Alignment
- Fine-tuning
- Neuron-level Defense
- Robustness
one_liner: 微调阶段通过安全信号神经元级重分布，同时抵御越狱与神经元级攻击且保留任务效用
practical_value: '- 业务使用开源LLM搭建Agent/智能客服/生成式文案系统时，可复用NeuronGuard的动态神经元识别+强制消融训练框架，解决安全对齐过脆易被越狱的问题，且无推理额外开销，适配高并发业务场景

  - 微调多任务（如同时兼顾业务效果与合规要求）出现梯度冲突时，可复用随机梯度投影trick，无需手工调损失权重即可平衡两个目标的训练效果，避免顾此失彼

  - 合规相关LLM微调仅需500对左右的安全/正常query探针集即可完成安全信号重分布训练，数据成本低，适合中小团队快速落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM安全对齐的安全信息高度集中在极少量稀疏神经元，导致两类攻击极易绕过：一类是越狱攻击通过构造prompt绕开安全机制，另一类是神经元级攻击直接剪枝安全关键神经元使对齐失效；现有防御要么仅能防御单类攻击，要么静态识别神经元无法适配训练时的表征漂移，未解决根本问题。

### 方法关键点
- 动态识别安全关键神经元：每N步用每层线性二分类器在安全/正常探针数据集上拟合，按权重排序选top-ρ神经元作为当前安全关键集，解决静态识别过时问题
- 消融鲁棒安全优化：同时计算正常前向的拒绝损失、安全神经元被消融后的拒绝损失，加KL散度正则保证两种前向的分布一致性，倒逼安全信号扩散到其他神经元
- 随机梯度投影：当业务任务梯度和安全梯度冲突时，随机选择一个梯度去掉反方向分量再叠加，避免两个目标的梯度互相抵消，无需人工调整损失权重

### 关键实验
在Llama-3.1-8B、Qwen2.5-7B、Falcon3-7B三个开源模型，SST2、AGNews等4个任务上微调，对比Perplexity Filter、SmoothLLM、SafeNeuron等7个基线，抵御PAIR、GCG、NeuroStrike等6种SOTA攻击，ASR降到接近0（最低0，最高0.04），任务准确率仅比无防御版本低1个百分点以内，微调开销与无防御相当，推理无额外开销。

### 最值得记住的一句话
安全对齐的脆性根因是安全信息的神经元级集中，通过主动消融强制信号扩散是从根因层面提升鲁棒性的高效路径。
