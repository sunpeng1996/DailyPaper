---
title: 'ARMOR: Adaptive Retriever Optimization for Low-Resource Telecom Question Answering'
title_zh: ARMOR：面向低资源电信问答的自适应检索器优化方法
authors:
- Heshan Fernando
- Quan Xiao
- Yan Xin
- Tianyi Chen
affiliations:
- Rensselaer Polytechnic Institute
- Cornell University
- Samsung Research America
arxiv_id: '2606.29706'
url: https://arxiv.org/abs/2606.29706
pdf_url: https://arxiv.org/pdf/2606.29706
published: '2026-06-29'
collected: '2026-06-30'
category: RAG
direction: RAG检索优化 · 低资源域适配
tags:
- RAG
- Retriever Tuning
- Low-Resource Adaptation
- InfoNCE
- Query Distillation
one_liner: 低资源RAG场景下仅优化查询编码器，自适应融合双目标加正则实现优于生成器微调的QA效果
practical_value: '- 低资源垂类RAG适配优先选择仅微调查询编码器而非生成器，既节省标注数据、避免生成器通用能力退化，还无需重新构建文档索引，适合电商垂类客服、商品问答、广告咨询等场景快速落地

  - 检索器训练可融合RAG生成似然（下游效用导向）和InfoNCE对比损失（语义区分导向），通过可学习温度自动平衡两目标权重，省掉人工调参成本

  - 仅调查询编码器时必须加入与预训练base查询编码器的余弦蒸馏正则，避免查询嵌入漂移出固定文档嵌入空间，解决低数据场景过拟合问题，可直接复用进现有RAG系统

  - 生成器能力越强，检索优化带来的增益越明显，垂类场景下若已用上7B+量级大模型，优先优化检索侧的投入产出比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
低资源垂直域QA场景下，直接微调生成器容易过拟合、泛化性差，还会遗忘通用能力；RAG系统中优化检索侧（仅查询编码器）更轻量，但现有检索优化目标要么仅关注下游生成效用、要么仅优化语义空间，静态权重融合难以适配训练动态，还容易出现查询嵌入与固定文档索引不兼容的漂移问题。

### 方法关键点
- 固定生成器和文档编码器/索引，仅微调查询编码器，大幅降低域适配成本
- 对RAG似然和InfoNCE两个互补目标分别设置可学习温度，动态调整两目标的梯度贡献，无需人工设置混合权重
- 新增查询蒸馏正则，约束微调后查询嵌入与预训练base查询嵌入的余弦相似度，避免嵌入漂移

### 关键结果
在电信3个垂类（ISAC/JCC/SAGIN）的Tele-Eval基准测试中，对比base RAG、单目标微调、静态混合等基线：ARMOR在ISAC域QA得分从0.6893提升到0.7119，全域Recall@3/Recall@5均为最优，且无生成器微调带来的效果退化问题；8B量级生成器下ARMOR增益比小模型更明显。

### 核心结论
低资源垂类RAG适配优先优化检索侧而非生成侧，双目标动态融合加嵌入正则是兼顾效果和泛化性的高性价比路径
