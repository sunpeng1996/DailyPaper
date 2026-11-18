---
title: 'ExRel: Learning Directed Reuse Relevance between Rich-Text K-12 Question Images
  with Executable Relation Contracts'
title_zh: ExRel：基于可执行契约的K12试题图像有向复用相关性学习
authors:
- Xuexin Liu
- Zengyi Wo
- Shiyu Zhang
- Suqi Cheng
- Daiting Shi
- Xiuyi Chen
affiliations:
- 中国科学院自动化研究所
- 南京大学
- 百度
arxiv_id: '2611.21461'
url: https://arxiv.org/abs/2611.21461
pdf_url: https://arxiv.org/pdf/2611.21461
published: '2026-11-16'
collected: '2026-11-18'
category: RecSys
direction: 多模态数据合成 · 相关性排序优化
tags:
- DataSynthesis
- MultimodalLearning
- RelevanceRanking
- LowResourceTraining
- CostOptimization
one_liner: 提出基于可执行契约的可控数据合成框架ExRel，解决K12试题图像复用相关性标注稀缺粒度粗问题
practical_value: '- 电商场景下商品/素材的细粒度相似度匹配任务，可借鉴可执行契约机制：明确定义允许修改的属性、需保留的核心特征，自动化生成符合标签分布的合成样本，降低人工标注成本

  - 合成训练数据的质量校验可复用分层校验逻辑：先做结构化规则校验（如属性一致性校验）再做小比例人工抽检，结合有限自动修复流程，大幅提升合成样本有效率

  - 稀缺小粒度样本的训练数据增强，可参考「结构化模板编辑+规则校验+轻度噪声注入」的合成范式，平衡数据多样性和标注准确率，提升小样本下的模型效果'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
K12富文本试题图像包含文本、公式、图表等多模态信息，通用相似度无法满足试题复用的细粒度相关性要求，自然标注样本以强相关性为主，缺乏中/弱相关性的细粒度覆盖，人工标注成本高。
### 方法关键点
提出ExRel代码基座智能框架：首先将真实试题重构为可编辑的HTML/CSS模板，将15种子关系编译为可执行契约，明确允许编辑项、保护不变量和查询-候选对方向；合成样本对经过DOM/渲染确定性校验、证据辅助审核、有限修复后添加轻度拍照退化，仅使用渲染后的图像做下游训练。
### 关键结果
ExRel合成数据的监督效果优于同规模自然数据，中相关性识别效果提升尤其明显；人工审核样本有效性达98.0%，单样本成本仅0.7元，较外包标注低36%；下游试题路由场景的实用性得到验证。
