---
title: 'UI-MOPD: Multi-Platform On-Policy Distillation for Continual GUI Agent Learning'
title_zh: UI-MOPD：面向持续GUI Agent学习的多平台在线策略蒸馏方法
authors:
- Niu Lian
- Alan Chen
- Zhehao Yu
- Chengzhen Duan
- Fazhan Liu
- Hui Liu
- Pei Fu
- Jian Luan
- Yaowei Wang
- Shu-Tao Xia
affiliations:
- 清华大学深圳国际研究生院
- 小米
- 哈尔滨工业大学（深圳）
- 浙江大学
- 鹏城实验室
arxiv_id: '2607.04425'
url: https://arxiv.org/abs/2607.04425
pdf_url: https://arxiv.org/pdf/2607.04425
published: '2026-07-04'
collected: '2026-07-07'
category: Agent
direction: GUI Agent · 跨平台持续学习
tags:
- GUI Agent
- On-Policy Distillation
- Continual Learning
- Multi-Teacher Distillation
- Cross-Platform Learning
one_liner: 基于平台感知路由的多教师在线策略蒸馏，解决跨平台GUI Agent持续学习的灾难性遗忘问题
practical_value: '- 做跨端（APP/PC/小程序）导购/交互Agent时，可复用分场景多教师蒸馏+路由的架构，避免不同端交互逻辑混叠，防止旧场景能力退化

  - 在线蒸馏工程实现中，可直接复用K3估计器降低KL计算开销，无需计算全词表logits，大幅降低蒸馏阶段算力消耗

  - 跨场景持续训练时，可引入自适应KL掩码：高reward样本关闭KL约束放开探索，低reward样本保留教师指导，平衡新场景适配与旧能力保留'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GUI Agent正从单平台任务执行向跨平台交互演进，现有方案存在两大痛点：一是高质量跨平台交互轨迹稀缺，数据集平台覆盖有限；二是不同平台交互规则差异大，混合SFT、模型合并等常规训练方式易导致行为模式混叠、平台专属能力退化、灾难性遗忘，得到劣化的平均策略。
### 方法关键点
- 构建Uni-GUI数据集：通过统一采集流水线产出11.5K条高质量跨平台（桌面/移动端）交互轨迹，覆盖160K步有效交互，格式标准化适配多模态模型训练
- 两阶段训练架构：第一阶段分平台SFT得到桌面、移动端两个专属专家教师；第二阶段通过多教师在线策略蒸馏训练共享学生模型，根据当前环境动态路由到对应平台教师，迁移平台专属行为先验
- 效率与效果优化：采用K3估计器仅用采样token的师生log概率计算KL，无需全词表计算，大幅降低开销；新增自适应KL掩码，高reward样本关闭KL约束放开探索，低reward样本保留教师指导
- 结构化奖励设计：区分完全正确、部分正确、无效动作的奖励梯度，提升RL阶段优化效率
### 关键结果
在OSWorld（桌面GUI基准）和MobileWorld（移动端GUI基准）上评测，对比混合SFT、权重平均/TIES合并等基线，UI-MOPD在OSWorld任务成功率达38.2%，相对基线提升12.7%；MobileWorld任务成功率达12.0%，相对基线提升55.8%，同时静态GUI理解、UI元素grounding能力无损失。
### 核心结论
跨场景持续学习的核心不是简单混合多源数据，而是给每个场景保留独立的行为锚点，通过条件约束避免不同场景的信号互相覆盖。
