---
title: 'As the Story Unfolds: Watching a Film and Identifying Characters as a Human
  Does'
title_zh: 《随剧情推进：像人类一样观看电影并识别角色》
authors:
- Zhongrui Gui
- Junyu Xie
- Tengda Han
- Weidi Xie
- Andrew Zisserman
affiliations:
- University of Oxford, UK
- Shanghai Jiao Tong University, China
arxiv_id: '2610.37579'
url: https://arxiv.org/abs/2610.37579
pdf_url: https://arxiv.org/pdf/2610.37579
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态视频理解 · 角色身份推理
tags:
- Multimodal LLM
- Video Understanding
- Entity Resolution
- Dataset
- Incremental Learning
one_liner: 提出无需外部演员表的电影角色命名任务，配套数据集、多模态模型及渐进式角色库构建框架
practical_value: '- 渐进式实体库构建思路可复用在电商直播场景的实时商品/主播识别任务，无需提前预制全量实体库，随直播流增量更新即可

  - 多模态cue融合（语音文本+视觉特征+时序逻辑）的方法可迁移到短视频信息流的人物/商品关联打标任务，提升标签准确率

  - 无外部知识库的实体推理范式可用于Agent实时理解用户上传的音视频内容，降低对预构建知识库的依赖'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有电影角色识别依赖外部演员表、演员照片等预构建知识库，无法模仿人类随剧情推进逐步识别角色的在线理解能力，且需要融合镜头结构、对话、视线、时序连续性等多类电影特有提示信息，落地难度高。

### 方法关键点
1. 定义全新角色命名任务，仅基于对话提到的姓名和对应视频上下文匹配对应可见角色；
2. 发布配套的角色命名、角色首次出场标注数据集；
3. 提出融合视频与对话特征的多模态模型，搭配随剧情推进增量构建角色库的渐进式框架。

### 关键结果
所提模型性能优于主流闭源多模态大模型，可实现无需外部知识库的类人在线电影角色理解
