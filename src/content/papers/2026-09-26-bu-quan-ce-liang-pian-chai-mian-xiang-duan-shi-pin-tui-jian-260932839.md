---
title: 'Mend the Measurement Gap: Latent User Preference Modeling for Short-Form Video
  Recommendation'
title_zh: 补全测量偏差：面向短视频推荐的隐式用户偏好建模
authors:
- Shuo Chang
- Yueqi Wang
- Zihuan Diao
- Ali Montazer
- Jiangguo Zhang
- Joyneel Misra
- Dapeng Hong
- Tomer Margolin
- Sourabh Bansod
- Ningren Han
affiliations:
- Google
- YouTube
arxiv_id: '2609.32839'
url: https://arxiv.org/abs/2609.32839
pdf_url: https://arxiv.org/pdf/2609.32839
published: '2026-09-26'
collected: '2026-09-29'
category: RecSys
direction: 短视频推荐 · 隐式偏好去噪
tags:
- Recommendation
- Debiasing
- Latent Variable
- Multi-task Learning
- Short-video
one_liner: 提出因子化隐价值模型FLVM解耦行为混杂因素，在YouTube Shorts提升用户愉悦度2.67%
practical_value: '- 可复用「受限基线路径+残差隐式路径」架构：将时长、用户倾向性、会话上下文等混杂特征单独放入基线路径，用stop-gradient阻断主损失回传，避免偏好信号被干扰，可解决观看时长、点击等信号的归因偏差问题

  - 多任务建模可引入硬稀疏路由掩码：让不同任务仅关联语义匹配的隐因子（如消费类信号关联消费隐因子、点赞差评关联valence隐因子），提升隐向量语义稳定性与可解释性

  - FLVM输出的标量化隐价值得分可直接替换现有多任务预打分模块，无需大幅改动现有排序链路即可落地，适合工业级推荐系统快速迭代

  - 冷启场景可直接复用该结构，通过解耦历史统计噪声和真实偏好提升新内容分发准确率，实验验证冷启组仍有>2%的正向增益'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
短视频推荐高度依赖观看时长、完成率等隐式反馈，但这类信号存在严重测量偏差：相同观看时长对不同时长视频的偏好指示性完全不同，完成率指标天然偏向短内容，普通多任务模型直接优化观测标签会放大统计噪声而非提升用户价值，现有去偏方法大多针对单信号，无法协同利用多源异构反馈的互补信息。

### 方法关键点
- 提出因子化隐价值模型（FLVM），将观测行为视为低维因子化隐价值状态的噪声测量值，包含消费$z_p$、主动参与$z_a$、正负向valence $z_s$三个独立隐因子
- 架构拆分为双路径：受限基线路径仅输入时长、用户倾向性、会话上下文三类混杂特征，用stop-gradient阻断主损失回传，专门拟合信号中的非偏好相关波动；隐式路径基于全量特征生成隐价值状态，通过硬稀疏路由掩码让每个反馈任务仅关联语义匹配的隐因子，预测基线无法解释的残差偏好
- 训练目标由多反馈预测主损失、基线路径单独训练的辅助损失、隐变量分布对齐的KL正则项三部分组成，推理时将$z_p$和$z_s$标量化为排序得分直接接入现有链路

### 关键实验
在YouTube Shorts百亿级用户场景验证，对比生产级多任务预打分基线：离线端观看时长RMSE从24.47降至23.35，点赞PR-AUC提升26.5%，差评PR-AUC提升42.1%；在线A/B测试核心用户愉悦度指标提升2.67%，冷启新内容场景仍保持>2%的正向增益，长视频表现提升尤为显著。

**最值得记住的一句话**：不要直接把观测行为等价于用户偏好，通过结构化路径拆分把混杂因素的影响从行为信号中剥离，才能得到更贴近用户真实意愿的偏好度量。
