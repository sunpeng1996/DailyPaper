---
title: 'MTL-MHOL: Predicting Online Conversions under Delayed Feedback and Data Sparsity'
title_zh: MTL-MHOL：解决延迟反馈与数据稀疏问题的在线转化预测框架
authors:
- Mario Tejera Vicente
- Eva Hagen
- Emma van Breukelen
- Quinten van de Vijver
- Kathrin Gruber
affiliations:
- Erasmus University Rotterdam
- Erasmus School of Economics
arxiv_id: '2611.30648'
url: https://arxiv.org/abs/2611.30648
pdf_url: https://arxiv.org/pdf/2611.30648
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 转化预估 · 延迟反馈与稀疏性优化
tags:
- CVR-Prediction
- Delayed-Feedback
- Data-Sparsity
- Multi-Task-Learning
- Multi-Head-Learning
one_liner: 结合多任务学习与多头在线学习，同时解决CVR预测的延迟反馈与数据稀疏痛点
practical_value: '- 延迟反馈建模可直接复用「时间分桶+风险集mask+生存分析聚合」的设计，无需等全量转化标签成熟即可用部分成熟数据训练，适配电商大促等需要快速迭代模型的场景

  - 稀疏场景下可引入多类型辅助任务做硬参数共享，连续型辅助目标优先采用多分位数回归加软单调性约束，比单值回归提供更丰富的监督信号，有效缓解CVR样本少的问题

  - 框架为模型无关设计，可快速替换MLP/DeepFM等任意可微backbone：高基数稀疏特征场景选DeepFM，高阶交互多的场景选MLP，改造成本极低

  - 现有采用ESMM多任务架构的业务可直接叠加多头分桶方案，实测RCE可提升21.5%，无需重构现有架构即可获得收益'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
CVR预测是电商推荐、在线广告的核心建模环节，长期存在两大未被同时解决的痛点：一是转化延迟导致训练时出现大量假负样本，用全成熟标签训练损失时效性，用新鲜标签训练存在偏置；二是转化样本稀疏，仅用点击样本训练存在选择偏差，现有方案大多单独优化某一问题，无法兼顾线上部署灵活性与效果。
### 方法关键点
- 多头延迟反馈建模：将最长转化周期拆分为多个互斥时间桶，每个桶对应一个预测头，仅用该桶成熟且未发生前序转化的风险集样本训练，通过生存分析公式聚合各头输出得到整体CVR，无需后处理校准即可保证概率合理性
- 多任务稀疏缓解：引入点击、页面访问量等密集信号作为辅助任务，与主任务硬参数共享；连续型辅助目标采用多分位数回归加软单调性惩罚，提供更丰富的监督信号，缓解主任务样本稀疏问题
- 模型无关设计：支持替换MLP、DeepFM等任意可微backbone，适配不同特征场景
### 关键实验
在Criteo公开数据集和两家电商私有数据集上测试，对比LR、RF、ESMM、FSIW等基线：MLP版MTL-MHOL在Criteo上RCE比ESMM高21.5%，比经典LR高81%，与最优延迟反馈方案FSIW性能持平；DeepFM版在高稀疏私有数据集上RCE比MLP版高10%，各场景下均优于所有消融变体。
### 核心结论
延迟反馈和数据稀疏的优化是互补而非互斥的，「时间分桶多头方案+低代价辅助任务」的组合改造成本极低，尤其适合转化周期长的电商/广告场景
