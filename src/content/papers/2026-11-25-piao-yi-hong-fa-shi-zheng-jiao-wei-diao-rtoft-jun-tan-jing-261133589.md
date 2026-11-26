---
title: 'Amortizing Exact Orthogonality: Drift-Triggered Restoration for Orthogonal
  Fine-Tuning'
title_zh: 漂移触发式正交微调RTOFT：均摊精确正交约束的训练开销
authors:
- Lanxin Zhao
- Xiaoyu Li
- Dai Shi
- Junbin Gao
- Andi Han
affiliations:
- The University of Sydney
- University of New South Wales
- University of Cambridge
arxiv_id: '2611.33589'
url: https://arxiv.org/abs/2611.33589
pdf_url: https://arxiv.org/pdf/2611.33589
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: PEFT优化 · 正交微调训练加速
tags:
- PEFT
- OFT
- LoRA
- fine-tuning
- orthogonal constraint
one_liner: 提出漂移触发的正交微调RTOFT，训练速度接近LoRA，效果优于现有OFT方案
practical_value: '- 业务场景做LLM/扩散模型参数高效微调时，可替换现有LoRA/OFT为RTOFT：相同参数量下训练速度接近LoRA，效果比LoRA高近2个点，且能更好保留预训练模型通用能力，适合多任务复用的推荐/广告/Agent场景

  - 该优化思路可迁移到推荐系统的特征正交化、用户/物品表征正则场景：无需每步做正交投影，仅监控漂移量超过阈值时再修复，大幅降低计算开销

  - 约束类优化通用技巧：若约束违反程度可通过当前迭代量精确计算，无需每步强制满足约束，仅在阈值触发时修复即可平衡精度与效率'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有正交微调（OFT）适配预训练模型时可保留权重奇异值与行夹角，比LoRA类低秩方法保留更好的预训练通用能力，但现有OFT方案每步都要构造并微分正交变换，训练速度比LoRA慢10%~58%；且OFTv2采用的截断Cayley-Neumann序列的截断阶数无法控制正交缺陷，相同阶数下不同任务的缺陷波动可达5个数量级，缺乏稳定的约束保证。

### 方法关键点
- 切向更新：每步仅用斜对称矩阵S做一阶更新\( W^+ = W(I+S) \)，无需构造正交矩阵，\( I+S \)的正交缺陷精确等于\( \|S\|_2^2 \)，定义\( \|S\|_2 \)为漂移量
- 漂移触发修复：仅当漂移量达到预设阈值τ时，通过极分解恢复精确正交性并重置S为0，每步仅需无梯度计算S的谱范数监控漂移，开销极低
- 严格正交保证：训练结束时额外做一次正交恢复，返回的变换严格正交，全程每步前向传播的正交缺陷上限为\( τ^2 \)，与损失、数据、模型、优化器无关

### 关键结果
- GLUE数据集上，块对角RTOFT训练速度为LoRA的0.97倍，6任务平均得分超OFTv2 1.09分，超LoRA 1.98±0.39分
- PEFT-Arena基准上，相同参数量下RTOFT通用能力损失仅2.35分，优于OFTv2的2.60分，同时目标任务收益更高
- Stable Diffusion可控生成任务上，RTOFT训练速度为LoRA的1.02倍，分割转图像任务mIoU达30.18，优于OFTv2的27.79
- 每步恢复正交的方案相比漂移触发无精度提升，单步训练开销反而高4.5%~27.5%

### 核心结论
当约束的违反程度可从当前迭代量精确计算时，无需每步强制满足约束，仅在阈值触发时修复即可兼顾精度与效率。
