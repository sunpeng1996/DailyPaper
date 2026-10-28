---
title: Robust LLM Data Selection via Content-Invariant Gradient Attribution
title_zh: 基于内容不变梯度归因的鲁棒LLM指令微调数据选择方法
authors:
- Jia Gu
- Liang Pang
- Huawei Shen
affiliations:
- Institute of Computing Technology, CAS
- University of Chinese Academy of Sciences
arxiv_id: '2610.36755'
url: https://arxiv.org/abs/2610.36755
pdf_url: https://arxiv.org/pdf/2610.36755
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM训练 · 指令微调数据选择
tags:
- DataSelection
- GradientAttribution
- InstructionTuning
- LLM
- Robustness
one_liner: 提出CIGA框架缓解梯度归因表面形式偏差，提升指令微调数据选择的稳定性、效率与下游性能
practical_value: '- 做垂域Agent、电商大模型微调的数据筛选时，可复用CIGA的中间层梯度提取方案，仅计算稳定高影响力中间层的梯度，无需全层计算，可降低70%左右的归因成本，速度提升3倍以上

  - 梯度排序与语义排序的RRF动态融合方法可直接迁移到推荐多路召回融合、搜索结果融合场景，根据信号质量自适应调权，无需人工预设融合权重，稳定性更强

  - 做数据选择前仅需构造3-5个语义不变的prompt变体即可校准梯度稳定性，无需统一所有样本的prompt格式，大幅降低垂域数据集的预处理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前基于全局梯度的指令微调数据选择方法存在表面形式偏差：相同语义的prompt仅修改措辞、格式，梯度归因得分差异极大，选出来的训练子集重叠率不足40%，既不稳定也浪费计算资源；而纯语义匹配方法又无法反映样本对模型优化的实际价值，需要同时兼顾优化层面的影响和内容层面的语义一致性。

### 方法关键点
- 先通过少量样本warm-up微调得到checkpoint，针对每个Transformer层计算梯度的平均强度和语义不变扰动下的离散度，平衡两者选出一致影响力层（CIL），仅用该层的梯度计算归因得分，过滤表层噪声
- 用外部文本编码器计算训练样本和验证集的语义相似度得分，采用Reciprocal Rank Fusion（RRF）融合梯度排序和语义排序，融合权重β根据梯度信噪比（SNR）和语义得分分布动态自适应调整，无需人工调参
- 按最终得分选Top-k%样本重新微调基础模型，全程不修改原始训练样本的格式多样性

### 关键结果
在LLaMA-2-7B、Qwen3-4B两个基础模型上，针对MMLU、GSM8K等5个基准测试集，对比LESS、TracIn等SOTA基线：CIGA的选择一致性提升8.65~9.27个百分点，下游任务平均性能比随机选择高1.04~2.11个百分点，计算成本降低71.1%，速度提升3.46倍。

### 核心结论
Transformer中间层的梯度特征天然兼顾任务相关性和表面形式稳定性，是比全局梯度更适合数据归因的信号。
