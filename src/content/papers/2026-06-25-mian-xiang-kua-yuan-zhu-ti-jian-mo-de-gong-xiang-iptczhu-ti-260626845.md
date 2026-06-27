---
title: A Shared IPTC Topic Space for Cross-Source Topic Modelling
title_zh: 面向跨源主题建模的共享IPTC主题空间构建方法
authors:
- Din Iskakov
- Sebastian Gonçalves
- Marco Idiat
- Mendeli Vainstein
- Aline Villavicencio
- Ronaldo Menezes
- Rodrigo Wilkens
affiliations:
- University of Exeter, UK
- Federal University of Rio Grande do Sul, Brazil
arxiv_id: '2606.26845'
url: https://arxiv.org/abs/2606.26845
pdf_url: https://arxiv.org/pdf/2606.26845
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 跨源主题建模 · 分类体系对齐
tags:
- BERTopic
- Topic Modelling
- IPTC Taxonomy
- Cross-corpus Alignment
- Content Tagging
one_liner: 提出基于IPTC分类体系的跨语料共享主题空间框架，解决不同语料主题无法直接对齐问题
practical_value: '- 跨源内容（如站外种草笔记、站内商品内容、舆情内容）的主题对齐可复用「外部分类体系锚定+最大相似度规则聚合」的思路，解决各语料单独训练主题模型无法对齐的痛点

  - 内容标签体系统一落地时，可借鉴guided BERTopic+分类体系分层映射的方案，相比零样本分类在高阈值下覆盖率提升更显著，适配电商内容打标、合规审核、信息流召回等场景

  - 主题映射的阈值校准可参考文中渐进式调优流程，避免阈值收紧时覆盖率骤降，可灵活平衡标签准确率和覆盖度的业务需求'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
跨源（如社交媒体、主流媒体）主题关注度对比的核心痛点是：各语料单独训练的主题模型生成的语料专属主题空间无法直接对齐，缺乏可复现的跨源主题统一建模方案。

### 方法关键点
提出基于IPTC媒体主题分类体系锚定的共享主题空间框架：
1. 用guided BERTopic生成候选主题；
2. 基于加权关键词、目标质心两个维度，与94个IPTC一级子主题匹配打分；
3. 按最大相似度规则向上聚合到17个IPTC父主题；
4. 通过宽筛模型、映射优化、候选对比、目标构建消融、阈值校准5步完成模型选型。

### 关键结果
在纽约时报2011语料上，guided系列模型在严格分配阈值下的映射覆盖率显著高于零样本基准；加入父类信息的目标构建方案同时提升覆盖率和父类一致性；阈值收紧时覆盖率呈渐进式下降而非骤降。
