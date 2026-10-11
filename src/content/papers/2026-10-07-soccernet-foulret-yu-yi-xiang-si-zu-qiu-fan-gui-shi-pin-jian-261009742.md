---
title: 'SoccerNet-FoulRet: Retrieving Semantically Similar Soccer Foul Videos'
title_zh: SoccerNet-FoulRet：语义相似足球犯规视频检索基准
authors:
- Jacobus Arthur
- Ahmad Sait
- Batool Hani
- Merey Ramazanova
- Jan Held
- Marc Van Droogenbroeck
- Bernard Ghanem
- Anthony Cioppa
- Silvio Giancola
affiliations:
- University of Liège
- KAUST
- SpAItial
arxiv_id: '2610.09742'
url: https://arxiv.org/abs/2610.09742
pdf_url: https://arxiv.org/pdf/2610.09742
published: '2026-10-07'
collected: '2026-10-11'
category: Multimodal
direction: 多模态视频语义检索 · 基准构建
tags:
- Video Retrieval
- Multimodal Embedding
- Benchmark Dataset
- Zero-shot Learning
- Fine-tuning
one_liner: 发布首个对齐裁判判罚语义的足球犯规视频检索基准，完成多类模型基线评测
practical_value: '- 做垂域跨模态检索业务（如电商商品视频搜同款、违规素材检索）时，可参考其「对齐业务语义定义相关性、脱离表层视觉特征」的评估逻辑，避免仅用通用视觉相似度做检索指标

  - 零样本检索效果不达标的场景，可先做低成本的类别级监督微调，再适配下游精确检索任务，平衡标注成本和检索效果

  - 构建行业垂域检索基准时，可复用其从现有标注数据集二次加工、人工校验query+相关性标签的流程，降低基准构建成本'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
职业足球裁判判罚缺乏可快速查询的相似历史案例，导致判罚标准不一致；现有视频检索仅匹配视觉相似度或通用事件标签，无法对齐裁判判罚逻辑层面的语义相关性。
### 方法关键点
基于SoccerNet-MVFoul数据集构建首个语义犯规检索基准SoccerNet-FoulRet，定义任务为给定查询犯规片段，返回裁判判罚规则下的相关先例，不受拍摄角度、参赛队伍等表层特征干扰；数据集包含693条人工校验的查询及类别相关性标签，评测零样本视频/视觉语言嵌入器、任务专属微调基线的检索性能。
### 关键结果数字
- 最强零样本模型在人工校验先例检索任务上HitRate@10 < 5%
- 类别监督微调可提升类别相关性表现，但对先例检索的迁移效果有限
