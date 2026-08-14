---
title: 'DrEM: Dual-Side Robust Ensemble Ranking from Noisy User Preference Predictions
  in Video Recommendation'
title_zh: DrEM：面向噪声用户偏好预测的视频推荐双边鲁棒集成排序
authors:
- Canwei Huang
- Tiantian He
- Xiaoxiao Xu
- Jun Zhang
- Ziran Deng
- Weike Pan
- Chunjie Chen
- Kaiqiao Zhan
affiliations:
- Shenzhen University
- Kuaishou Technology
arxiv_id: '2608.12778'
url: https://arxiv.org/abs/2608.12778
pdf_url: https://arxiv.org/pdf/2608.12778
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: 推荐系统·集成排序鲁棒优化
tags:
- Ensemble Ranking
- Robust Learning
- Noisy Prediction
- Video Recommendation
- Multi-Task Fusion
one_liner: 针对工业推荐集成排序pxtr的双边噪声问题，提出共享噪声模型的双端去噪框架，上线获显著业务收益
practical_value: '- 集成排序场景可复用双端去噪思路：监督侧用pair级翻转概率加权修正BPR类损失，特征侧加任务自适应扰动做一致性正则，不需要改推理逻辑，无线上耗时开销

  - pxtr噪声方差可通过分桶统计预测值与后验真实行为的偏差离线预计算，不需要额外特征或模型训练，落地成本低；稀疏任务（评论/关注/转发）的增益远高于dense任务（点击/播放），可优先在高噪声任务落地

  - 双端校正共享同一噪声分布参数，避免两边优化目标冲突，可直接作为插件接入现有EMER/EASQ等主流集成排序模型，适配性强'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级短视频推荐多采用多阶段架构，集成排序阶段需要将上游多任务模型输出的多维pxtr融合为统一排序分，pxtr同时承担输入特征和代理监督信号的双重角色。但上游模型输出的pxtr天然存在预测噪声，会同时从两方面传导到下游：监督侧噪声会翻转代理偏好引入错误梯度，特征侧噪声会导致排序分输出不稳定，现有方法默认pxtr为可信信号，未针对这种双边噪声做适配，存在明显优化空间。

### 方法关键点
- 共享logit空间加性高斯噪声模型，通过分桶聚合pxtr预测值与真实后验行为的偏差，预计算每个item的噪声方差，为双端校正提供统一参数
- 监督侧设计风险去噪鲁棒损失：基于噪声方差和pair的pxtr margin计算偏好翻转概率，对pairwise损失做自适应加权，修正噪声导致的梯度偏移，理论证明即使翻转概率存在估计误差，损失效果仍优于基础BPR损失
- 特征侧设计偏好保留排序一致性正则：基于item级噪声方差采样扰动注入pxtr输入，仅对扰动前后偏好顺序一致的pair做一致性约束，避免扰动破坏原生排序信号，同时提升模型对输入噪声的鲁棒性

### 关键实验
离线实验基于快手亿级DAU的工业真实数据集，以GAUC为核心指标，对比SSM/PSL/GaussAug/LSPR等单端鲁棒基线，在EMER/EASQ两个主流集成排序骨干上，各pxtr任务GAUC平均提升0.2~1.2个千分点；线上A/B测试7天覆盖5.1%主流量，相比生产基线，关注/评论等稀疏互动指标提升最高达1.388%，APP停留时长提升0.124%，7日留存提升0.02%，所有指标p值均<0.005。

### 核心结论
工业集成排序场景中，pxtr的双重角色导致的双边噪声是不可忽视的优化点，基于统一噪声模型的双端自适应校正，是投入低、收益高、兼容现有架构的有效优化路径
