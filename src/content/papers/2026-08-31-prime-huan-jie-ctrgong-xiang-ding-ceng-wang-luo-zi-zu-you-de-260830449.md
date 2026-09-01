---
title: 'PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks
  with Plug-in Residual Input-Conditioned Mixture of Expert'
title_zh: PRIME：缓解CTR共享顶层网络子组优化竞争的即插即用MoE方法
authors:
- Heng Yao
- Siyun Hou
- Tianying Liu
- Yulou Shu
- Yong He
- Chuan Yuan
- Kaibin Qiu
- Guowei Chen
- Jiayu Zhao
- Chao Yu
affiliations:
- Ant Group
- Henan Polytechnic University
- Independent Researcher
- Alibaba Inc.
arxiv_id: '2608.30449'
url: https://arxiv.org/abs/2608.30449
pdf_url: https://arxiv.org/pdf/2608.30449
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: CTR排序 · 共享顶层网络优化
tags:
- CTR Prediction
- Mixture of Experts
- Low-Rank Residual
- Recommendation Ranking
- Plug-in Module
one_liner: 提出即插即用低秩残差MoE组件PRIME，缓解CTR共享顶层网络子组梯度竞争，适配多架构提效
practical_value: '- 存量CTR模型迭代无需修改backbone，零残差初始化保证初始效果不跌，可冻住原有参数仅训PRIME组件，上线风险极低

  - 低秩残差专家+无辅助损失EMA负载均衡的设计可直接复用，参数量仅增加0.6%-0.8%，推理延迟普遍低于10%，满足线上高吞吐要求

  - 业务上线前可先做梯度诊断：计算不同语义子群（流量端、品类、时段）的顶层网络梯度余弦相似度，若低于同规模随机分组0.2以上，PRIME收益更明确

  - 多Bag专家聚合的设计可迁移到其他单/多任务模型顶层，降低预测方差提升训练稳定性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有CTR模型顶层普遍采用共享MLP结构，不同语义子群（用户、物品、场景）的梯度方向对齐度比同规模随机子群低0.23-0.37，导致优化方向被迫妥协，单纯加宽MLP无法解决底层共享约束问题；而直接替换顶层为MoE会破坏原有训练好的权重，效果波动大上线风险高。

### 方法关键点
- 锚定原有Dense预测路径，低秩残差专家仅做logit修正，零残差初始化保证训练初始完全对齐基线效果
- 输入依赖软路由分配专家权重，4个专家Bag聚合多组条件估计降低方差，采用EMA负载偏置调整专家利用率，无需额外辅助损失
- 完全即插即用，仅Hook原有模型的embedding输出和预测概率，不修改任何backbone逻辑

### 关键实验
在Avazu、Criteo两个公开数据集测试13种主流CTR架构，对比原生Dense基线、APG等同类方法：
- Avazu上11/13架构AUC提升，中位数AUC+0.0022，LogLoss降0.0011；Criteo上11/13架构AUC提升，中位数AUC+0.0066，LogLoss降0.0081
- 对比APG，在FiBiNET、DCNv2上所有10次种子实验AUC均更高，参数量少0.7%-5.2%，推理延迟低1.8%-15.9%
- 语义子组竞争gap平均降低34.3%，验证优化方向对齐度明显提升

**最值得记住的一句话**：CTR模型效果瓶颈很多时候不是特征交互不够，而是顶层共享参数的子组优化竞争没解决，低开销的即插即用条件适配比盲目堆参更有效
