---
title: 'Good Pretraining, Bad SFT: Checkpoint Quality Across the Training Stack'
title_zh: 多阶段LLM训练流水线Checkpoint质量评估：预训练优未必SFT效果好
authors:
- Sohir Maskey
- Philipp Scholl
- Jonas Knupp
- Pit Neitemeier
- Sascha Wirges
affiliations:
- Aleph Alpha
arxiv_id: '2609.08966'
url: https://arxiv.org/abs/2609.08966
pdf_url: https://arxiv.org/pdf/2609.08966
published: '2026-09-08'
collected: '2026-09-09'
category: Training
direction: LLM训练 · Checkpoint选择优化
tags:
- Checkpoint Selection
- SFT
- MoE
- Solution Density
- Pretraining
one_liner: 发现预训练指标最优的Checkpoint未必SFT后效果最优，提出解密度可作为适配性辅助信号
practical_value: '- 业务场景做SFT/LoRA的base模型选型时，不要仅依赖pretrain loss或公开Benchmark分数，可新增轻量高斯扰动测试解密度，解密度更高的Checkpoint后续微调效果更稳定

  - 预训练收尾阶段不要盲目用学习率cooldown策略，恒定LR训练的Checkpoint或多个连续Checkpoint加权合并的版本，后续SFT效果普遍优于单独cooldown
  Checkpoint

  - 若SFT后模型出现生成重复、不停机的病理问题，优先排查base Checkpoint的解密度，仅调整SFT学习率无法修复低解密度Checkpoint的固有缺陷

  - 多阶段训练的Checkpoint筛选可推迟到长上下文适配阶段后，此阶段的指标和最终SFT得分相关系数达0.884，此时筛选可大幅节省算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM训练普遍分为预训练、中训练、长上下文适配、SFT等多阶段，业界默认预训练指标最优的Checkpoint在后续全流程训练后效果也最优，但若该假设不成立，全流程验证所有候选Checkpoint的算力成本极高，亟需更可靠的中间选型信号。

### 方法关键点
- 测试对象为30B MoE模型（单token激活3B参数），对比三类预训练Checkpoint：CONSTANT（最后800B tokens保持恒定LR）、COOLDOWN（最后800B tokens LR降至最高值的10%）、MERGE（20个连续CONSTANT Checkpoint线性加权合并）
- 所有Checkpoint走完全相同的后续训练流程：100B token中训练、100B token长上下文适配、10B token对话SFT
- 引入**solution density（解密度）**指标：对Checkpoint施加高斯权重扰动，统计性能保留在指定阈值以上的比例，衡量参数空间局部鲁棒性

### 关键结果
- COOLDOWN的预训练loss、预训练评测得分均优于CONSTANT，但SFT后总得分低0.113，还出现严重的生成重复、不停机问题，调整SFT学习率完全无法修复该缺陷
- 中训练阶段得分与SFT后得分相关系数仅0.473，长上下文适配后相关系数升至0.884，同一学习率sweep内的Checkpoint排序完全稳定
- GSM8K任务τ=0.9阈值下，CONSTANT解密度为27%、MERGE为13%，COOLDOWN为0%，解密度排序完全匹配后续SFT的性能排序

**最值得记住的一句话**：Checkpoint的价值不取决于当前的评测指标，而取决于它在后续完整训练流水线后的最终表现。
