---
title: Is Personalized Modality Weighting Actually Personalized? A Controlled Audit
  of Per-User Weighting Claims in Multimodal Recommenders
title_zh: 多模态推荐系统用户个性化模态加权机制的对照审计研究
authors:
- Jingyuan Zheng
- Xin Zhang
- Yang Gu
- Dongjing Wang
- Yuxiang Wang
- Xudong Shen
- Haiping Zhang
- Youhuizi Li
- Dongjin Yu
affiliations:
- Hangzhou Dianzi University
- Hangzhou Normal University
- Fuxi AI Lab, NetEase Inc.
arxiv_id: '2608.05655'
url: https://arxiv.org/abs/2608.05655
pdf_url: https://arxiv.org/pdf/2608.05655
published: '2026-08-06'
collected: '2026-08-07'
category: RecSys
direction: 多模态推荐 · 个性化机制审计
tags:
- Multimodal Recommendation
- Personalization Audit
- Controlled Experiment
- Modality Weighting
- Recommendation System
one_liner: 通过双对照审计证实多模态推荐中全局模态权重几乎覆盖全部收益，个性化加权无一致增益
practical_value: '- 多模态推荐落地优先上全局模态加权即可，无需投入算力研发用户个性化模态加权模块，实测其最高增益不到0.9pp且跨场景不稳定，多数场景为负收益

  - 验证个性化模块有效性时，不能仅做shuffle对照，必须增加与最强全局非个性化基线的效用对比，避免把模型容量增益错当成个性化收益

  - 若需探索模态相关个性化，不要用共享协同用户embedding生成权重，避免架构混淆导致误判模块有效，改用独立的模态偏好embedding作为输入

  - 新个性化模块上线前可复用论文的双对照审计框架做离线验证，过滤无效伪个性化设计，减少上线试错成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态推荐在十亿级用户规模场景广泛部署用户级个性化模态加权，宣称通过捕捉用户专属模态偏好带来排序增益，但过往评估未隔离用户专属信号、全局模态权重、模型容量三者的增益贡献，大量复杂个性化模块可能实际为无价值的伪增益。

### 方法关键点
- 设计双对照审计原则：效用差（real-GM）对比个性化加权与全局模态加权的效果差，可识别性差（real-shuf）在评估时打乱用户与权重的绑定，对比原始效果的差值
- 固定统一的协同过滤骨干，仅替换6种主流个性化模态加权头（自由查表、注意力门、超网络、低秩引导、解耦输入变体等），排除骨干结构、训练流程差异的干扰
- 加入信号植入校准实验，验证审计框架可有效检测真实存在的用户个性化信号，排除测量误差导致的假阴性

### 关键结果数字
- 覆盖3个短视频数据集+1个电商数据集，全局模态权重对比无模态基线的PairAcc增益达1.9~6.97pp，覆盖几乎全部模态相关收益
- 所有个性化加权头无一致增益，少量正增益不超过0.9pp，跨数据集/指标波动大，大部分场景增益为负
- 可识别性差存在架构混淆：用共享用户embedding生成权重的头，shuffle掉差可达128%的模态总收益，但实际效用仍低于全局权重，解耦输入后该虚高差值降到0.6%

最值得记住的结论：仅通过shuffle对照证明用户-模块绑定有效不能作为个性化收益的证据，必须同时跑赢最强非个性化基线才算有效个性化。
