---
title: Harnessing Domain Specialists in Multimodal Mixture-of-Experts for Efficient
  Adaptation
title_zh: 利用多模态MoE的领域专家特性实现高效适配
authors:
- Damiano Marsili
- Raphi Kang
- Aditya Mehta
- Pietro Perona
- Georgia Gkioxari
affiliations:
- California Institute of Technology
arxiv_id: '2610.02123'
url: https://arxiv.org/abs/2610.02123
pdf_url: https://arxiv.org/pdf/2610.02123
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: 多模态MoE · 高效微调方法
tags:
- MoE
- Multimodal LLM
- Parameter Efficient Fine-Tuning
- Expert Specialization
- LoRA
one_liner: 提出无数据的ExpertLens方法识别多模态MoE领域专家，选择性微调实现超4倍训练加速效果超LoRA
practical_value: '- 业务侧若使用多模态MoE做商品理解、搜广推多模态特征建模，可复用ExpertLens无数据识别领域专家的逻辑，无需标注数据即可筛选垂类（美妆/3C/医药等）相关专家，仅微调该部分专家即可降低适配成本

  - 垂类多模态任务适配优先选择「领域专家微调+少量共享参数更新」的方案，相比LoRA最高可获2.9倍训练加速，同时效果更优，适配成本远低于全微调

  - 多垂类搜广推系统可利用MoE专家的天然语义独立性，不同垂类迭代仅微调对应专家，避免跨垂类适配的互相干扰，降低增量更新的成本和风险'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
MoE架构通过稀疏计算大幅提升模型容量，但现有适配方案要么全微调计算成本极高，要么LoRA等参数高效方法效果受限；多模态MoE中是否存在天然的语义专属专家、如何无需领域数据即可利用该特性降低适配成本，是待解决的实际问题。

### 方法关键点
- 先验证多模态MoE存在天然分层语义专业化：专家呈现模态偏好（图像/文本）、领域偏好（医疗/数学/遥感等）、细粒度语义偏好，且和低阶视觉特征无关
- 提出**ExpertLens**无数据专家筛选方法：将专家的router权重通过LM头解码为词汇token，计算和目标领域的匹配度，筛选得分≥0.9的领域专属专家
- 适配策略：仅微调筛选出的领域专家MLP，同时更新router权重、QKV投影、LM头少量共享参数，其余参数全部冻结

### 关键结果
- 在数学、医疗、遥感三类多模态任务上测试，对比全微调（FFT）、LoRA（r=32）、随机选专家等baseline
- ExpertLens仅更新21.7%-47%的参数，效果和全微调持平甚至略优（数学64.6% vs 63.8%，医疗53.7% vs 53.6%，遥感51.9% vs 51.6%），平均训练速度是全微调的4倍，比LoRA快2.9倍，效果显著超过LoRA
- 适配效果不受领域训练顺序影响，泛化到Qwen3-VL、Kimi-VL等不同多模态MoE模型均有效

**最值得记住的一句话**：多模态MoE为效率引入的稀疏性，会天然形成语义对齐的模块化结构，无需额外设计就能直接用于高效垂类适配
