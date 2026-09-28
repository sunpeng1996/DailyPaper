---
title: 'Causal Retention in Interactive Agents: Interface Factorization and Selective
  Adaptation'
title_zh: 交互式智能体的因果保留：接口分解与选择性适配
authors:
- Shengjun Zhang
- Tingyi Liu
- Dong Xie
- Yunlong Dong
- Xiang Wang
- Cheng Zeng
affiliations:
- Hubei University
- Wuhan University
- Baidu Inc.
- Independent Researcher
arxiv_id: '2609.30650'
url: https://arxiv.org/abs/2609.30650
pdf_url: https://arxiv.org/pdf/2609.30650
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 因果机制记忆与迁移
tags:
- Causal Retention
- Interactive Agent
- Mechanism Memory
- Selective Adaptation
- Structural Causal Model
one_liner: 提出Causal Core机制记忆模块，实现交互式Agent因果机制留存与跨域选择性适配且不降低任务性能
practical_value: '- 搭建LLM驱动的推荐/电商Agent时，可借鉴证据门控写入逻辑，仅保留经过干预验证的用户-物品交互因果机制，过滤虚假关联，减少推荐误判

  - 跨场景迁移推荐/广告策略时，可复用「诊断定位偏移+局部更新」的适配框架，仅修改发生偏移的规则条目，不破坏稳定交互逻辑，降低迁移后的效果波动

  - 识别推荐系统混淆变量（如同步观测的proxy特征）时，可参考readout过滤方法，通过对比干预分离直接因果目标和间接观测变量，提升特征归因准确性'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有交互式Agent的训练目标仅保障任务性能，无法保留完整的干预因果机制信息，跨域迁移时容易破坏原有稳定机制，且无法回答训练目标外的因果查询，导致模型可解释性、迁移性差。
### 方法关键点
- 定义因果保留指标，要求冻结的模型状态可独立回答动作、上下文、目标、值、延迟五类因果探针查询，且与训练过程无关
- 提出Causal Core记忆模块，通过目标门、时间门、读出门、上下文门四类证据门控机制，仅写入经过干预对比验证的因果元组(a,c,y,v,δ)
- 跨域适配时采用诊断惊奇信号定位偏移的机制条目，仅对偏移条目做局部重训练，不修改稳定条目
### 关键实验结果
在有限SCM、连续模拟器、TD-MPC2世界模型、Qwen2.5-7B-Instruct上测试，对比奖励优化、排名损失、世界模型等baseline：
- 冻结Qwen最后层探针源域平衡准确率0.958，延迟偏移子集仅0.583，加门控后延迟准确率达1.0，readout假阳率降至0.056
- TD-MPC2迁移时偏移执行器符号准确率从0.057提升至0.948，稳定响应误差无上升
- 选择性适配任务AdaptScore达1.0，所有baseline均为0
### 核心结论
任务性能充足不代表因果机制信息完整，保留可验证的因果元组记忆是提升Agent可解释性、迁移鲁棒性的核心路径
