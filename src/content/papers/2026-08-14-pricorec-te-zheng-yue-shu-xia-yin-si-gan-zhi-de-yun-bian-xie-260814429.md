---
title: 'PriCoRec: A Privacy-Aware Cloud-Device Collaborative Framework for Ad Recommendation
  under Feature Constraints'
title_zh: PriCoRec：特征约束下隐私感知的云边协同广告推荐框架
authors:
- Dairui Liu
- Zhongyi Lu
- Jitao Lu
- Aghiles Salah
- Mete Sertkan
- Roger Zhe Li
- Changhong Jin
- Barry Smyth
- Xingsheng Guo
- Ruihai Dong
affiliations:
- University College Dublin
- Huawei Ireland Research Center
arxiv_id: '2608.14429'
url: https://arxiv.org/abs/2608.14429
pdf_url: https://arxiv.org/pdf/2608.14429
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 隐私保护 · 云边协同广告推荐
tags:
- Ad Recommendation
- Privacy Preserving
- Cloud-Device Collaboration
- CTR Prediction
- Pre-ranking
- On-device Recommendation
one_liner: 拆分云侧预排序与端侧排序，敏感特征端侧留存，兼顾隐私、推荐效果与低延迟
practical_value: '- 云边拆分架构可直接复用，敏感用户特征（年龄、性别、本地行为）完全端侧计算不上传，大幅降低隐私合规成本，适配电商/广告推荐的监管要求

  - 云侧预排序新增DPP启发的多样性正则，无需修改端侧逻辑即可提升候选集召回率，λ在1e-3~1e-2区间调优性价比最高

  - 端侧模型直接复用云侧预排序logit作为辅助特征，配合4维小embedding、FP16存储可将模型压缩至7.7~15MB，推理延迟<1ms，完全符合端侧算力约束

  - 云导辅助训练思路可迁移到其他端小模型场景，避免端侧重复学习云侧已掌握的通用特征，大幅降低端侧模型训练和推理成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
隐私法规对用户敏感数据（年龄、性别、精细行为）的云端传输限制越来越严格，传统纯云推荐模型因特征缺失效果显著下滑；联邦学习、差分隐私等现有隐私保护方案算力开销大、部署门槛高，无法适配工业级级联推荐流水线的低延迟要求，亟需平衡隐私、效果、部署成本的新架构。

### 方法关键点
1. 特征与架构拆分：将特征分为云可访问特征（物品属性、粗粒度上下文）和端侧独有特征（敏感用户属性、精细行为），云侧仅完成预排序，端侧执行最终排序，敏感特征完全不出端
2. 云侧预排序优化：引入DPP启发的多样性正则作为辅助损失，基于item embedding的相似度矩阵计算多样性损失，加权到原有BPR排序损失中，解决云侧特征不足导致的候选集质量下降问题
3. 端侧轻量化优化：端侧小模型直接复用云侧预排序输出的relevance logit作为辅助特征，无需重复学习云侧已掌握的通用规律；配合小维度embedding、FP16存储、词汇表压缩实现极低部署开销

### 关键实验结果
在OpenMCC、TaobaoAd、Ali-CCP三个工业公开数据集上，对比DP-SGD、联邦学习等基线：云侧预排序R@100最高提升1.7%，端侧排序R@10最高提升25%；全链路延迟约10ms，端侧推理仅0.5ms，最小模型体积仅7.7MB，完全符合工业部署预算。

### 核心结论
云边协同推荐的核心不是简单拆分模型部署位置，而是让云侧聚焦算力密集的通用特征学习，端侧聚焦隐私敏感的个性化增强，可在不牺牲隐私的前提下拿到接近甚至超过纯云方案的效果。
