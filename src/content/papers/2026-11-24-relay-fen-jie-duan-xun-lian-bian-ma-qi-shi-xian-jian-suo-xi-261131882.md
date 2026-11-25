---
title: 'RELAY: Learning Compatible Representations One Encoder at a Time'
title_zh: RELAY：分阶段训练编码器实现检索系统嵌入表示兼容升级
authors:
- Yu Wang
- Chuan Qin
- Qiang Zhang
affiliations:
- Alibaba Qwen Business Unit
arxiv_id: '2611.31882'
url: https://arxiv.org/abs/2611.31882
pdf_url: https://arxiv.org/pdf/2611.31882
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: 检索系统嵌入兼容升级 · 增量重编码
tags:
- Compatible Representation
- Retrieval System
- LoRA
- Model Upgrade
- Embedding
one_liner: 分阶段先训兼容旧向量库的新查询编码器再训新文档编码器，大幅降低检索升级的效果掉点
practical_value: '- 检索系统升级时可复用该分阶段训练范式：先适配新Query编码器兼容旧文档向量库，上线提升效果后再逐步重编码文档，避免全量切换的风险

  - 混合新旧向量的召回阶段，可加入按文档版本的isotonic回归分数校准，能在不改变版本内排序的前提下解决跨版本分数偏置问题，实测33/39场景下AUC提升

  - 新文档编码器可只训LoRA，配合固定前缀取embedding的设计，降低训练成本的同时保证与冻结Query编码器的兼容性，比联合训练少用15%-34%的GPU小时

  - 全量重编码完成后可选择移除临时Query投影层，再微调Query编码器的LoRA，最终效果和联合训练差距小于1pp，无需重新编码全量文档'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
检索系统升级嵌入模型时，全量重编码千万/亿级文档库耗时极长，过渡阶段新旧向量共存会出现跨版本分数偏置，导致召回效果骤降（如CLIP升Qwen时重编码10%文档Recall@1从61.27%掉到13.81%），现有兼容方案要么效果损失大，要么无法在过渡阶段持续提升效果。

### 方法关键点
- 三阶段训练范式：1）Query适配：用LoRA训新Query编码器+临时投影层，对齐旧文档向量空间，可直接上线服务旧库；2）文档适配：冻结训好的Query编码器，用LoRA训新文档编码器，输出固定前缀维度的embedding与Query对齐，上线后逐步重编码替换旧向量；3）可选Query优化：全量重编码完成后移除临时投影层，微调Query的LoRA，无需重新编码文档
- 混合库分数校准：给新旧文档版本各训一个单调isotonic回归映射修正分数，保留版本内排序的同时解决跨版本分数偏置
- 全程只用标准检索对比损失，无需额外兼容正则项

### 关键实验
在COCO、Flickr30K的3个跨模型升级场景（Qwen2B→2B、CLIP→Qwen2B、Qwen2B→8B）对比13种SOTA兼容方案：
- 过渡阶段未重编码任何文档时，Recall@1比原系统提升8.66~10.23pp；直接重编码AUC在两个Qwen升级场景排第一，CLIP→Qwen场景排第二
- 混合库加分数校准后，33/39的方法-升级组合的重编码AUC提升，CLIP→Qwen场景下RELAY的最低Recall@1从36.6%提升到58.99%，高于原系统的50.09%
- 最终Query优化后，Recall@1和联合训练的差距小于0.97pp，训练GPU小时比联合训练低15%~34%

**最值得记住的一句话**：检索系统嵌入升级不需要一次性全量切换，先把新Query对齐旧库上线拿收益，再慢慢重编码文档，全程用同一个Query打分就能把过渡阶段的效果掉点降到几乎可忽略。
