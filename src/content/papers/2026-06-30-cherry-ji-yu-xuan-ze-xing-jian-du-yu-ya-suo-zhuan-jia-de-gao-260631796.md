---
title: 'CHERRY: Compressed Hierarchical Experts with Recurrent Representational Yield'
title_zh: CHERRY：基于选择性监督与压缩专家的高效大模型训练框架
authors:
- Dohyeon Kwon
- Youngjin Park
affiliations:
- AXOps Team, TeamSparta Inc.
arxiv_id: '2606.31796'
url: https://arxiv.org/abs/2606.31796
pdf_url: https://arxiv.org/pdf/2606.31796
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 大模型训练效率优化 · 高效专家融合
tags:
- SGT
- MoE
- Model Compression
- Selective Training
- Recurrent Transformer
one_liner: 提出选择性监督、深度压缩、高效专家融合三项技术，大幅降低大模型训练与部署算力成本
practical_value: '- 微调LLM4Rec/业务Agent时，可仅对15%左右的高语义token（商品ID、决策关键词、属性值等）做SGT训练，配合α=0.7的混合损失，减少85%监督计算量，非监督token效果通过梯度耦合同步提升

  - 大推荐模型/Agent压缩部署时，采用相邻层平均+循环展开方案，可实现2.5倍参数量缩减，效果与原大模型处于噪声误差范围内，适合低资源/端侧部署场景

  - 模型对齐阶段，仅监督少量元认知pivot token（纠错触发词、合规拒绝词、验证标记等），用不到0.5%的训练token即可实现3.9倍自纠错率提升、83%
  jailbreak成功率下降，大幅降低对齐标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大模型训练依赖海量算力，普通团队难以负担，且常规训练对所有输出token均匀加权，大量算力浪费在低语义价值的句法类token上，同时大模型部署的参数量门槛较高，亟需低成本的训练、压缩、部署全链路效率方案。

### 方法关键点
- 选择性真值token训练（SGT）：仅对占比~15%的高语义token（实体、推理支点、元认知触发词等）做重点监督，用α=0.7的混合损失平衡重点监督和全序列锚定，依托Transformer位置共享权重的梯度耦合效应，非监督token也能同步获得效果提升
- 循环深度压缩：通过相邻层参数平均将48层模型压缩到6层，再循环展开核心层获得34层有效深度，参数量降至227M
- 高效专家融合（MoEE）：将多个压缩模型作为MoE专家，配合SGT蒸馏和多token预测头，在相同活参数量下效果优于单压缩模型，还可实现1.6~2.1倍推理提速

### 关键结果
在1.8B参数韩语底座模型上验证，训练集为12800条韩语指令数据：
1. SGT仅监督15% token即可获得全序列监督67%的损失下降，单监督token效率提升4.5倍
2. 压缩后的6层227M模型效果与566M稠密模型损失几乎一致（2.934 vs 2.926），参数量缩减2.5倍
3. 双专家MoEE在活参512M下比最优单压缩模型损失降低4.7%，仅监督2~5个元认知token即可让自纠错率从12%升至47%，jailbreak成功率从23%降至4%

最值得记住的结论：大模型效果不直接等于算力投入，通过选择性聚焦高价值信号、参数复用、多专家融合，完全可以在有限算力下拿到适配业务需求的效果。
