---
title: A Unified Detection Framework for AI-Related Content and Artifacts
title_zh: AI相关内容与生成产物的统一检测框架
authors:
- Xifeng Zhang
- Tao Hu
- Yijie Peng
- Wan Tian
affiliations:
- 首都师范大学数学科学学院
- 南京大学管理与工程学院
- 北京大学前沿信息技术研究院
- 北京大学王选计算机研究所
arxiv_id: '2607.07527'
url: https://arxiv.org/abs/2607.07527
pdf_url: https://arxiv.org/pdf/2607.07527
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM内容检测 · 统一多场景框架
tags:
- LLM Detection
- Mahalanobis Distance
- Robust Covariance Estimation
- AI Oversight
- MCD Estimator
one_liner: 提出基于马氏距离得分的统一检测框架，支持LLM生成文本、幻觉、水印、对抗样本多场景检测
practical_value: '- 可复用该框架马氏距离+鲁棒协方差估计思路，检测LLM生成的商品文案、用户评论中的幻觉内容，降低虚假信息风险

  - 针对多类正样本的联合MCD估计方法，可直接迁移到电商风控场景的异常内容识别任务

  - 框架的多场景适配特性，可复用搭建统一AIGC内容审核管线，同时覆盖生成文本识别、水印检测、对抗样本拦截需求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前AIGC技术大规模落地，缺乏低成本的统一监管方案，现有检测方法多针对单一场景，泛用性差，无法覆盖LLM生成内容识别、幻觉检测、水印校验、对抗样本拦截等多元监管需求。

### 方法关键点
提出基于Mahalanobis距离得分（MDS）的统一检测框架，适配4类核心AI监管场景；针对正样本（如人类生成文本、事实性内容、无水印样本）多分类、同质性异质性共存的特点，开发casewise和cellwise两类最小协方差行列式（MCD）的联合估计算法，证明了算法的收敛性和高崩溃点特性，保障正样本表征的鲁棒性。

### 关键结果
多场景实证评估验证了框架的检测有效性，暂未公开细分场景下的量化精度指标。
