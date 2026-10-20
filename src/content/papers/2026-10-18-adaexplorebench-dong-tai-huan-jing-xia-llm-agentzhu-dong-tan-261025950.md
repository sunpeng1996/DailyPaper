---
title: 'AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time
  Adaptation in Evolving Environments'
title_zh: AdaExploreBench：动态环境下LLM Agent主动探索与测试时适配评测基准
authors:
- Rui Wang
- Zishen Lai
- Jiayu Liu
- Cheng Qian
- Jeonghwan Kim
- Heng Wang
- Xuejun Zhang
- Jiateng Liu
- Bingxuan Li
- Shujin Wu
affiliations:
- HKUST
- HKUST(GZ)
- UIUC
- CUHK
- CMU
arxiv_id: '2610.25950'
url: https://arxiv.org/abs/2610.25950
pdf_url: https://arxiv.org/pdf/2610.25950
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: Agent 动态环境探索与适配评测
tags:
- LLM Agent
- Benchmark
- Proactive Exploration
- Test-time Adaptation
- Dynamic Environment
one_liner: 推出首个覆盖主动探索、无通知规则漂移的动态环境LLM Agent能力评测基准
practical_value: '- 电商/推荐场景的概念漂移检测可借鉴规则漂移探测思路：当线上推荐/广告效果下跌时，优先复用原有探针样本重探验证规则有效性，而非全量重训，可大幅降低适配成本

  - 做主动探索类Agent（如冷启动选品、新流量场探索）无需盲目增加探测量，优先选择能区分不同假设的高信息价值探针，可在提升探索效率的同时降低流量损耗

  - 上线LLM Agent前可复用本基准的评测范式：构造模拟业务规则变化的测试集，提前验证Agent主动感知环境变化、更新策略的能力，避免上线后因规则漂移出现效果暴跌'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent已逐步落地到动态变化的真实场景（如电商平台规则迭代、广告投放策略调整、用户偏好漂移），但现有评测基准多假设环境静止、证据直接提供，无法衡量Agent主动探索环境隐式规则、感知无通知的规则漂移并快速适配的能力，这是Agent落地的核心痛点。
### 方法关键点
- 将环境动态抽象为4类常见决策逻辑的隐式规则：加性加权、合取（需满足所有条件）、析取（满足任意条件即可）、优先级排序，规则漂移无通知触发，包含因子替换、影响方向反转两种典型变化
- 评测协议要求Agent自主决定探索时机、探针内容、探索量，仅能通过自身探针和效用反馈获取信息，避免环境信息泄露
- 支持可扩展无标注数据生成pipeline，共产出256个评测样例、1000个训练样例，覆盖金融、医疗、制造、网络安全4个领域
### 关键实验结果
评测8款主流LLM，默认动态环境下最强的Gemini-3.8-Flash的Calibrated Accuracy仅67.25%；移除规则漂移后所有模型平均准确率提升6.2%，直接提供充足证据平均提升9.4%，强制增加探测量反而使平均准确率下降2.0%。
### 核心结论
当前LLM Agent在动态环境的核心瓶颈不是探索量不足或基础规则学习能力弱，而是主动探索的质量差、对已习得规则存在假设固化，无法及时识别规则失效并更新。
