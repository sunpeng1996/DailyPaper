---
title: 'Recovering Expert Critic-Sourced Network Adjacency between Musical Artists
  from Acoustic Distributions: A Construct-Validity Approach'
title_zh: 基于声学分布与构念效度恢复乐评专家标注的音乐人邻接关系
authors:
- Elena Badillo-Goicoechea
- Fengfeng He
affiliations:
- The University of Chicago
arxiv_id: '2608.27291'
url: https://arxiv.org/abs/2608.27291
pdf_url: https://arxiv.org/pdf/2608.27291
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 音乐推荐 · 冷启动内容建模
tags:
- ColdStart
- ContentBasedRec
- OptimalTransport
- MusicRec
- ConstructValidity
one_liner: 利用声学特征与最优传输距离恢复乐评标注的音乐人邻接关系，冷启动场景AUC达0.767
practical_value: '- 冷启动推荐场景可引入第三方专家/专业文本标注的实体关联关系，补充交互数据不足的缺陷

  - 计算实体（商品/内容）相似度时，可采用Wasserstein距离建模多维度特征分布匹配度，效果优于单特征均值匹配

  - 多源交叉验证的标注关系置信度更高，可优先作为召回/排序特征，能显著提升模型效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有音乐推荐依赖用户交互数据（冷启动场景失效）和声学内容信号，未充分挖掘乐评专家在长文本中明确标注的音乐人关联信号，此前仅验证该信号的内部有效性，缺乏与声学特征对齐的外部验证。
### 方法关键点
将音乐人表示为80维Essentia底层声学特征的经验分布，采用边际最优传输（Wasserstein）距离建模成对音乐人相似度，在冷启动、音乐人不重叠的数据集划分下评估乐评邻接关系的声学可恢复性。
### 关键结果数字
集成模型样本外AUC达0.767（95%置信区间0.761-0.775）；可恢复性随乐评共识单调提升，多源共同标注的边AUC达0.865；边界清晰的场景化细分流派可恢复性显著高于宽泛的行业通用流派分类。
