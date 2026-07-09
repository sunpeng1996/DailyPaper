---
title: 'PIPBench: A Profile-Inclusive Framework for Personalized Image Generation
  Evaluation'
title_zh: PIPBench：面向个性化图像生成的含用户画像评估框架
authors:
- Yuhang Wu
- Shuxiang Zhang
- Wee Hian Ching
- Chi Zhang
- Miao Liu
affiliations:
- College of AI, Tsinghua University
- Sun Yat-sen University
- Shanghai Qi Zhi Institute
arxiv_id: '2607.06440'
url: https://arxiv.org/abs/2607.06440
pdf_url: https://arxiv.org/pdf/2607.06440
published: '2026-07-07'
collected: '2026-07-09'
category: Eval
direction: 多模态个性化生成 · 评估基准构建
tags:
- Personalized Generation
- Text-to-Image
- Benchmark
- User Profile
- Evaluation
one_liner: 提出首个融合用户画像的个性化图像生成基准PIPBench，配套可扩展数据构建流水线
practical_value: '- 电商个性化营销素材生成（如商品图、海报）场景可复用该框架的「用户属性画像+历史偏好样本」双重评估逻辑，解决千人千面生成效果难量化的问题

  - 需要大规模构造个性化生成评估数据集时，可复用「小批量真实用户采集+Agent模拟批量生成」的混合流水线，大幅降低标注和用户调研成本

  - 落地个性化AIGC业务时，可直接引入PIPBench测试集验证模型对用户隐式偏好的对齐效果，减少线上AB测试的试错成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文生图模型（如DALLE-3）仅能遵循用户显式prompt指令，无法对齐个体隐式审美偏好，当前缺乏融合用户画像维度的个性化图像生成标准化评估体系。
### 方法关键点
1. 提出PIPBench，是首个纳入用户画像的个性化图像生成评估基准，覆盖用户历史偏好图像、短prompt、显/隐式审美标签、人口/心理属性画像多维度数据；
2. 设计新型数据构建流水线，融合心理学、人口统计学画像维度，同时支持真实用户小样本采集和可扩展Agent模拟数据生成，大幅降低数据集构建成本；
3. 基于该基准对主流个性化文生图方法开展系统性评测。
### 关键结果
评测发现现有个性化生成方法普遍存在用户隐式偏好对齐能力不足的核心缺陷，为后续个性化文生图优化明确了核心方向。
