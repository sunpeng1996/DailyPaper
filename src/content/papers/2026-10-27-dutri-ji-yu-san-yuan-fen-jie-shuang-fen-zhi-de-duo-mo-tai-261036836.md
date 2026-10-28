---
title: 'DuTri: Dual-Branch Modeling with Triadic Factorization for Multimodal Multi-Scenario
  Recommendation'
title_zh: DuTri：基于三元分解双分支的多模态多场景推荐框架
authors:
- Jintao Huang
- Chaohua Yang
- Kailiang Hao
- Dugang Liu
- Xing Tang
- Zhong Ming
affiliations:
- Shenzhen University
- Shenzhen Technology University
arxiv_id: '2610.36836'
url: https://arxiv.org/abs/2610.36836
pdf_url: https://arxiv.org/pdf/2610.36836
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 多场景推荐 · 多模态融合 · CTR预测
tags:
- Multi-scenario Recommendation
- Multimodal Fusion
- CTR Prediction
- Tensor Factorization
- Contrastive Learning
one_liner: 提出三元分解双分支架构，解耦协同与多模态建模，提升多场景推荐效果
practical_value: '- 现有多场景模型直接拼接多模态特征的范式存在性能缺陷，可参考双分支拆分设计，将跨场景协同偏好学习和多模态融合解耦，避免参数共享机制对多模态表征的干扰

  - 协同分支可采用CP分解对用户-场景-Item三元交互做结构化建模，配合残差量化压缩，既捕获跨场景共性与场景特性，又控制存储与推理成本

  - 多模态分支的模态权重可由用户+场景偏好联合生成门控控制，实现不同用户/场景下模态重要度自适应调整，无需人工定义规则

  - 可引入Item级对比学习对齐协同分支与多模态分支的Item表征，打通两个分支的信息传递，无需复杂特征交互即可实现协同信号与内容语义的融合'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前电商平台多业务入口需要统一多场景推荐建模，同时商品图文等多模态特征是优化推荐效果的重要信号，但现有多场景推荐模型引入多模态特征时，通常直接将图文特征与ID特征拼接后输入原有参数共享架构，忽略了协同信号与多模态语义的表征空间差异，对照实验证明这类方案在加入多模态特征后性能反而不如场景独立MLP，存在明显的范式缺陷。

### 方法关键点
- 双分支架构设计：拆分协同分支与多模态分支，前者负责学习跨场景用户偏好，后者负责自适应多模态融合
- 协同分支：对用户-场景-Item三元交互做CP分解，配合残差量化生成结构化偏好表征，共享用户/Item因子、用场景因子做调制，同时捕获跨场景共性与场景差异
- 多模态分支：用协同分支输出的用户+场景偏好生成门控权重，自适应融合Item的ID、文本、视觉特征
- 对齐机制：用Item级对比学习对齐两个分支的Item表征，实现信息互通，最终拼接两个分支输出接入场景专属预测头

### 关键实验
在AntM2C（支付宝5个工业场景）、Amazon（3个品类场景）两个公开数据集上，对比STAR、HMoE、AMS等16个SOTA基线：AntM2C上加权AUC达0.8632，比次优基线AMS提升0.34个千分点；Amazon上加权AUC达0.7437，比次优基线提升0.37个千分点，所有场景AUC均为最优，推理效率与AMS相当。

### 核心结论
多模态多场景推荐不要直接把多模态特征喂给传统多场景ID模型的参数共享架构，双分支解耦协同学习和多模态融合的范式收益更显著
