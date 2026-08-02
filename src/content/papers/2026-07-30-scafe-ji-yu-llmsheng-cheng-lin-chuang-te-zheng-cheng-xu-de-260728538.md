---
title: 'ScaFE: Data-Efficient Scar Classification with LLM-Generated Clinical Feature
  Programs'
title_zh: ScaFE：基于LLM生成临床特征程序的数据高效瘢痕分类方法
authors:
- Ruman Wang
- Hangting Ye
affiliations:
- Liaoning University of Traditional Chinese Medicine
- Jilin University
arxiv_id: '2607.28538'
url: https://arxiv.org/abs/2607.28538
pdf_url: https://arxiv.org/pdf/2607.28538
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: LLM领域知识落地 · 隐私合规小样本分类
tags:
- LLM
- Feature Engineering
- Data Efficiency
- Privacy-preserving AI
- Knowledge Distillation
one_liner: 将LLM领域知识转化为本地可执行特征程序，实现数据高效、可审计的跨院图像分类
practical_value: '- 涉及用户隐私的电商/广告场景，可参考将LLM领域知识转化为本地可执行特征脚本的范式，避免原始用户/行为数据外传，满足合规要求

  - 小样本标注场景（比如新品冷启动推荐、小众类目分类）可复用「LLM生成候选特征+本地轻量模型拟合+聚合统计回传迭代」的流程，降低标注依赖

  - 需要可解释性的推荐/广告排序场景，可借鉴特征级SHAP校验迭代的思路，提升模型决策的可审计性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
临床瘢痕图像分类面临专家标注数据少、跨院采集差异大的问题，端到端图像模型数据依赖度高，调用云端VLM又存在数据合规风险，决策不可复现、难以审计。

### 方法关键点
提出ScaFE框架：联网LLM检索临床证据，合成可测量视觉瘢痕属性的可执行特征程序；候选程序在本地受限环境运行，仅回传聚合验证统计量和特征级SHAP摘要用于迭代优化，原始图像与患者数据完全留存在本地；最后用轻量随机森林基于生成的结构化特征完成分类。

### 关键结果
3家医院600张图像留一站点验证下，平衡准确率达81.0%，比最优基线BiomedCLIP高10.0个百分点；仅用10%开发数据时仍保持72.0%平衡准确率，领先基线11.8个百分点；迭代优化后特征程序可执行率从66.7%提升至95.0%，91.7%的最终特征有临床证据支撑。
