---
title: 'MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training
  across Mobile and Computer Environments'
title_zh: MAI-Gym：跨多端的GUI Agent评估与RL训练一站式开源平台
authors:
- Panrong Tong
- Quyu Kong
- Pengxiang Li
- Tianyu Xia
- Hanzhang Zhou
- Lei Wang
- Chenglin Cai
- Long Li
- Long Chen
- Jianan Zhang
affiliations:
- Alibaba Group
arxiv_id: '2610.20939'
url: https://arxiv.org/abs/2610.20939
pdf_url: https://arxiv.org/pdf/2610.20939
published: '2026-10-13'
collected: '2026-10-16'
category: Agent
direction: GUI Agent · RL训练与评测平台
tags:
- GUI_Agent
- RL_Training
- Evaluation_Platform
- Open_Source
- Sim2Real
one_liner: 开源多端统一GUI Agent平台，支持2万并行环境，训出10B参数以下SOTA多端GUI Agent
practical_value: '- 可复用平台的2万并行环境管控、窗口式KV cache复用优化逻辑，降低大批次Agent在线推理/训练的算力成本

  - 做电商端侧交互Agent（如自动操作商家后台、用户导购助手）时，可先用仿真Mock App做RL预训练，再迁移到真实App，降低线上训练的风险与成本

  - 跨域Agent训练可参考联合RL方案，比分开训专家再参数融合效果更优，适合同时覆盖PC/移动端多场景的业务Agent

  - 任务生成可借鉴失败驱动的合成逻辑，针对Agent薄弱点自动生成训练任务，提升训练效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GUI Agent的RL训练面临两大核心痛点：一是多端（移动端/PC/WEB）环境难统一、并行扩展性差，评估和训练的Agent实现易漂移导致结果不可信；二是真实GUI任务（尤其是交易类）训练有操作风险，现有任务多为孤立设计无连贯上下文，多样性不足，难以支撑大规模RL训练。

### 方法关键点
- 架构设计：统一评估、数据采集、RL训练的rollout路径与Agent harness，避免训练/评估实现漂移，环境管理器封装多端差异，对外暴露统一接口
- 效率优化：支持2万并行环境实例，窗口式历史上下文设计大幅提升KV cache命中率，训练token量降低84.7%，训练速度提升62.6%
- 任务合成：支持自动生成可重置Mock App（真实App克隆/全新App），先构建跨App连贯世界再生成任务，配套可执行验证器，支持失败驱动的针对性任务生成
- 训练支持：内置GRPO、SAO等6种RL算法，策略自适应任务采样，优先给模型半掌握的任务分配资源，提升RL效率

### 关键结果
- 基于平台训出的MAI-Gym-9B是10B参数以下开源SOTA多端GUI Agent，MobileWorld准确率78.4%，OSWorld-Verified准确率76.2%，超过同尺寸基线最高3.2/5.4个百分点，性能优于部分更大参数的模型
- 仿真Mock App训练的能力可迁移到真实App：12306仿真App训练后，真实App上的任务成功率从28.8%提升到48.1%
- 跨端联合RL比分开训专家再融合效果更优，两个核心基准分别高2/1.4个百分点

**最值得记住的结论**：GUI Agent训练中，仿真环境低成本预训练+小样本真实环境微调的路径完全可行，统一训练/评估管线是大规模落地的核心前提。
