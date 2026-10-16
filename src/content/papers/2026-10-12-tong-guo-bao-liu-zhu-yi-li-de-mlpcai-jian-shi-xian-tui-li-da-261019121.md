---
title: Unlocking Structured Pruning for Reasoning Language Models via Attention-Preserving
  MLP Trimming
title_zh: 通过保留注意力的MLP裁剪实现推理大模型的结构化剪枝
authors:
- Woosang Lim
- Haneul Yoo
- Vincent-Daniel Yun
- Sungjoo Yoo
affiliations:
- Seoul National University
- New York University
- University of Southern California
arxiv_id: '2610.19121'
url: https://arxiv.org/abs/2610.19121
pdf_url: https://arxiv.org/pdf/2610.19121
published: '2026-10-12'
collected: '2026-10-16'
category: LLM
direction: 推理大模型 · 结构化剪枝优化
tags:
- Structured Pruning
- Reasoning LLM
- MLP Trimming
- Training-free
- Model Compression
one_liner: 提出免训练结构化剪枝方法LayerTrim，在保留推理能力前提下大幅降低推理大模型部署成本
practical_value: '- 业务侧部署推理型LLM（如导购Agent、文案生成、复杂Query理解模型）可直接复用LayerTrim剪枝逻辑，无需额外训练即可获得约20%的推理速度提升与显存占用降低，推理能力损失远低于现有剪枝方案

  - 剪枝策略可直接迁移：优先裁剪低Block Influence层的MLP而非注意力模块或整层删除，既能拿到压缩收益，又能最大程度保留长序列推理、多步决策能力，避免推荐/导购场景多轮对话逻辑崩溃

  - MLP特征排序的轻量指标（激活平方期望乘以down投影权重L2范数）可复用至其他LLM压缩场景，无需计算交叉项即可实现13倍校准加速，效果与全量计算几乎一致'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有结构化剪枝方法应用于推理大模型（RLM）时会导致长链推理性能暴跌甚至完全失效，而RLM在电商导购、复杂Query理解、多步决策Agent等场景的应用越来越广泛，急需免训练、推理能力保留度高的结构化剪枝方案降低部署成本。
### 方法关键点
- 基于3个核心观测设计：MLP裁剪比注意力裁剪/整层删除的表示误差更低；MLP特征重要性高度集中（前38.2%的特征贡献89.4%的重要性）；优先裁剪低Block Influence层的MLP比均匀裁剪所有层的误差更小
- 剪枝流程完全免训练：首先用原始大模型生成的推理轨迹做校准，计算每层Block Influence选取2N个冗余层；然后用「激活平方期望乘down投影权重L2范数」作为特征重要性指标，保留每个冗余层MLP的top-m特征；最后直接物理裁剪对应MLP的门控、up、down投影矩阵，不修改注意力模块、不改变模型深度，无需梯度或恢复训练
### 关键结果
- 覆盖数学推理、科学推理、代码生成3类共5个benchmark，测试3款主流推理大模型，对比7种现有剪枝方法
- 同等参数量剪枝预算下，平均准确率比最强基线最高高出21.4个百分点；Qwen3-14B裁剪9层等效参数量时，prefill速度提升1.24倍，峰值显存降低19.7%，解码速度提升1.21倍，推理准确率保留率达84.9%
- 剪枝准备时间仅27.9s，比基线RESP快94~140倍
> 最值得记住的一句话：推理大模型剪枝优先保注意力、保深度，仅裁剪冗余层的低重要性MLP特征，就能用极低的成本拿到可观的压缩收益
