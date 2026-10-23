---
title: 'UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping
  Agents'
title_zh: UserArena：面向长序列购物Agent的交互式用户模拟基准
authors:
- Jujia Zhao
- Jiakai Tang
- Jing Yu
- Wen Chen
- Jian Wu
- Han Zhu
- Fei Sun
- Suzan Verberne
- Zhaochun Ren
affiliations:
- Leiden University
- Renmin University of China
- Alibaba Group
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2610.30932'
url: https://arxiv.org/abs/2610.30932
pdf_url: https://arxiv.org/pdf/2610.30932
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 电商长序列用户仿真基准构建
tags:
- User Simulation
- E-commerce Agent
- Benchmark
- Long-Horizon Recommendation
- Trajectory Distillation
one_liner: 推出首个支持生产A/B验证的长序列电商用户模拟基准及高保真模拟器训练方法OPTD
practical_value: '- 构建内部用户模拟器时可复用OPTD训练范式：用轨迹级意图做蒸馏+信任域约束，既解决长序列仿真的曝光偏差，又避免意图引导偏离真实行为

  - 自建仿真评测体系可参考USERARENA的5级评估框架（L0-L4），尤其是可对接线上A/B结果做离线仿真效度校验，降低新策略上线试错成本

  - 长序列用户行为建模可参考轨迹级意图抽取思路：排除具体动作、商品ID等泄露信息，仅保留全局偏好/需求，提升跨session行为预测的一致性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent化推荐的训练与评估依赖高保真的用户行为仿真环境，但现有基准缺乏跨session的长序列真实用户轨迹，也无法验证仿真得到的策略效果是否和线上A/B结果一致，导致长序列用户模拟器的保真度评估缺乏可信依据，仿真结论的业务有效性不足。

### 方法关键点
- 构建USERARENA基准：包含阿里电商平台11010位用户的64729条session轨迹，覆盖56万+商品、13种用户动作，对齐每一步的用户画像、视觉上下文、商品信息与行为，支持跨session长序列评估，内置真实生产A/B测试结果作为仿真效度校验ground truth
- 提出5级评估体系：从环境合规性（L0）、局部行为保真（L1）、序列行为保真（L2）、个性化群体保真（L3）、结果保真（L4）逐层校验模拟器质量
- 提出OPTD训练方法：基于轨迹级全局意图做在线策略蒸馏，在学生模型自生成的rollout上提供稠密token级监督，配合信任域约束避免意图引导偏离可观测的真实行为，同时解决SFT的曝光偏差与RL的稀疏奖励问题

### 关键结果数字
对比SFT、GRPO等训练方法及8款主流用户模拟器，OPTD在单session场景下L1-L4的8项指标全部第一，跨session场景下5项指标第一；生产A/B验证中，OPTD模拟的PV-CTR政策效果是线上真实值的71.3%，远优于其他基线（最高仅29.7%），通用大模型如GPT-6反而出现效果高估。

**最值得记住的一句话**：通用大模型的能力不直接等价于电商用户行为仿真的保真度，基于真实轨迹的轨迹级蒸馏+线上A/B校验是构建业务可用用户模拟器的核心路径。
