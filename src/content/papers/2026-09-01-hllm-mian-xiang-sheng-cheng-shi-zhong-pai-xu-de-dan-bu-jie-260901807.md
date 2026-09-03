---
title: 'hLLM: Single Pass Decoding for Generative Reranking'
title_zh: hLLM：面向生成式重排序的单步解码方法
authors:
- Emil Laftchiev
- Prachi Agrawal
- Moe Kayali
- Bixing Yan
- Qi Xu
- Zijie Lei
- Chen Qiu
- Zhi Hua
- Ke Li
- Luke Simon
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2609.01807'
url: https://arxiv.org/abs/2609.01807
pdf_url: https://arxiv.org/pdf/2609.01807
published: '2026-09-01'
collected: '2026-09-03'
category: GenRec
direction: 生成式推荐 · LLM重排序加速
tags:
- Generative Reranking
- LLM Inference
- LoRA
- Knowledge Distillation
- Hungarian Algorithm
one_liner: 将排序转为最优匹配问题，从LLM预填充隐藏态单步解码，实现45-64倍提速且质量无损
practical_value: '- 生成式重排序落地可参考该方案解决自回归解码延迟瓶颈：将排序转为二分图匹配问题，从LLM Prefill隐藏态直接拉取结果，避免O(N)次序列解码开销，实测排序规模N≤50时组合优化开销可忽略

  - 训练范式可复用：用成熟自回归排序大模型做教师，离线蒸馏全排列标签，学生用LoRA微调骨干+轻量注意力头+Sinkhorn交叉熵损失，对齐教师效果成本极低

  - 重排序头选型参考：LoRA适配骨干时选2层自注意力头最优；如果骨干冻结，线性探针的效果差距极小，可进一步压缩参数和延迟

  - 工程落地可直接复用延迟优化结论：瓶颈完全在Prefill阶段，后续优化可聚焦骨干量化、剪枝、Early Exit，排序解码模块几乎无额外开销'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式LLM重排序能联合建模候选间关联，质量远超pointwise打分，但自回归解码需要O(N)次前向传播，延迟随候选规模线性增长，是落地实时推荐、广告、搜索重排序场景的核心瓶颈。此前的非自回归解码方法要么仍需多轮迭代，要么无法保证输出是合法排列，仍存在质量损失或延迟不足的问题。

### 方法关键点
- 将排序问题转化为最大权二分图匹配问题：仅用一次LLM Prefill前向传播，提取每个候选对应位置的隐藏态
- 新增轻量2层自注意力头处理候选隐藏态，输出N×K的候选-位置亲和度矩阵
- 训练时用Sinkhorn算子做排列的可微松弛，以教师模型的全排列结果为标签，用Sinkhorn交叉熵损失训练，骨干用LoRA微调适配排序任务
- 推理时跳过Sinkhorn，直接用匈牙利算法（LAPJV变种）求解亲和度矩阵的最优匹配，天然保证输出为合法排列，无需后处理

### 关键实验
在内部电商重排序数据集和公开Amazon Beauty数据集测试：内部数据集相比带推理链的自回归教师模型提速64.5倍，端到端延迟28ms，AUC保留99.9%，NDCG@1、Recall@1甚至略优于教师；相比无推理链的教师模型仍提速3.1倍。Amazon Beauty数据集相比32B Qwen教师模型提速44.9倍，NDCG@1保留97.3%效果。延迟拆解显示Prefill占99.6%以上开销，匈牙利算法仅占0.03%，几乎可忽略。

### 核心结论
生成式排序的核心信息已经完全蕴含在LLM的Prefill隐藏态中，无需额外序列解码，利用任务的排列结构做定制化解码可实现数量级的延迟提升且质量无损。
