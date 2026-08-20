---
title: 'ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube
  Videos'
title_zh: 2026 ChildSafeAds共享任务：儿童向YouTube视频商业内容检测
authors:
- Thales Bertaglia
- Catalina Goanta
- Gerasimos Spanakis
- Gunes Acar
affiliations:
- Utrecht University
- Maastricht University
- Radboud University
arxiv_id: '2608.19165'
url: https://arxiv.org/abs/2608.19165
pdf_url: https://arxiv.org/pdf/2608.19165
published: '2026-08-19'
collected: '2026-08-20'
category: Eval
direction: UGC内容儿童友好广告合规检测评测
tags:
- AdCompliance
- ContentModeration
- SharedTask
- Dataset
- LLMAnnotation
- UGC
one_liner: 发布儿童向YouTube视频植入广告识别的多子任务共享评测数据集与基准
practical_value: '- 做内容平台广告合规检测时，可复用SponsorBlock众包标记的广告片段作为无偏候选集，降低对平台自带广告披露标签的依赖

  - 多模态广告内容分类/风险识别任务，可按数据获取成本分层（转录文本→视频属性→外链页）设计基线，平衡推理效果与运行成本

  - 构建垂直领域标注数据集时，可采用「专家迭代分类体系+prompt调优+大模型预标注+少量人工校验」的范式，大幅提升标注效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
儿童难以识别YouTube UGC内容中植入的原生广告，现有平台广告披露合规率极低，监管侧与平台均缺乏大规模自动化检测的标准化基准与数据集。
### 方法关键点
构建ChildSafeAds 2026共享任务，基于SponsorBlock众包标记的广告片段，匹配对应转录文本、视频/频道属性、描述页外链，设置3个子任务：广告推广类型识别（ST1）、产品分类（ST2）、法律风险标记（ST3）；同时设置4级数据访问权限梯度，可对比不同数据获取成本下的模型效果。采用专家迭代分类体系+prompt调优+大模型预标注+少量人工校验的范式完成标注。
### 关键结果
数据集覆盖939个频道的3360条视频，其中45.5%的视频未正确使用平台自带的「包含付费推广」披露标签。
