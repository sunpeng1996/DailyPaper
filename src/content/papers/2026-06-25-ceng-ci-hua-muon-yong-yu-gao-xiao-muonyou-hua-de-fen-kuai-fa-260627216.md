---
title: 'Hierarchical Muon: Tiled Newton-Schulz Updates for Efficient Muon Optimization'
title_zh: 层次化Muon：用于高效Muon优化的分块Newton-Schulz更新方法
authors:
- Ziyuan Tang
- Tianshi Xu
- Yousef Saad
- Yuanzhe Xi
arxiv_id: '2606.27216'
url: https://arxiv.org/abs/2606.27216
pdf_url: https://arxiv.org/pdf/2606.27216
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: LLM训练 · 高效优化器设计
tags:
- Optimizer
- LLM Training
- Newton-Schulz
- GPU Acceleration
- Matrix Operation
one_liner: 提出分块Newton-Schulz更新的HiMuon优化器，降低大矩阵更新开销同时匹配原版Muon训练效果
practical_value: '- 推荐/Agent场景下微调LLM4Rec、Agent基座时，可直接替换Muon优化器为HiMuon，在不损失训练效果的前提下降低单步训练开销，提升模型迭代效率

  - 大矩阵运算优化思路可复用：对大梯度/物品/用户嵌入矩阵做固定尺寸分块独立运算，适配GPU小核并行特性，同时可实现跨层批量计算、内存分块调度，缓解大模型训练显存压力

  - 分块矩阵的谱交互保留策略可迁移到其他矩阵类优化算子设计，在计算效率和近似精度之间做可控权衡'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Muon类优化器通过对动量梯度矩阵做有限步Newton-Schulz映射生成权重更新方向，可提升Transformer预训练效率，但全矩阵更新时间复杂度达O(r²sK)，大矩阵场景下计算开销极高，行列耦合特性也导致并行难度大。
### 方法关键点
HiMuon将动量梯度矩阵切分为T×T的独立分块，对每个分块单独执行Newton-Schulz映射后重组结果，仅保留分块内谱交互、丢弃分块间交互，时间复杂度降至O(HWTK)，天然支持分块尺寸适配的GPU kernel、跨层批量、内存分块调度、运行时分块尺寸动态调整。
### 关键结果
Transformer训练实验验证，HiMuon可显著提升优化器单步执行效率，同时训练收敛表现与全矩阵Muon基本一致。
