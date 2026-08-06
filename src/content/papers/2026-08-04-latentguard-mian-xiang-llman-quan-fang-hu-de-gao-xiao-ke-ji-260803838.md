---
title: 'LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards'
title_zh: LatentGuard：面向LLM安全防护的高效可审计隐式推理框架
authors:
- Zhinan Liu
- Jie Li
- Mingyu Kang
- Jiayi Ji
affiliations:
- Xiamen University
- University of Science and Technology of China
arxiv_id: '2608.03838'
url: https://arxiv.org/abs/2608.03838
pdf_url: https://arxiv.org/pdf/2608.03838
published: '2026-08-04'
collected: '2026-08-06'
category: LLM
direction: LLM安全 · 隐式推理与按需审计
tags:
- LLM-Safety
- Latent-Reasoning
- Chain-of-Thought
- Auditability
- Efficient-Inference
one_liner: 将显式推理压缩为连续隐式状态，兼顾LLM安全防护的低延迟推理与按需审计能力
practical_value: '- 做Agent/生成式推荐的内容安全审核时，可直接复用该架构：常规流量走隐式推理低延迟链路，仅对抽检/申诉场景调用审计解码器生成解释，兼顾大流量下的性能与合规要求

  - 分阶段隐式蒸馏的训练策略可迁移到所有基于CoT的LLM优化场景：比如搜索推荐的Query改写、LLM排序，可先训显式CoT版本，再分阶段压缩成隐式推理，在不损失效果的前提下大幅降低推理延迟

  - 自适应隐式预算的动态推理设计可复用：根据样本难度动态分配计算资源，简单样本少用隐式token、难样本多用，相比固定预算的方案可进一步降低平均延迟，适配电商流量峰谷波动场景

  - 隔离式解释生成的设计可直接用到推荐可解释性场景：主推荐/排序链路不生成解释，单独训练轻量解释解码器，仅在用户申诉/运营排查时按需生成解释，不影响主链路性能'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
推理型LLM安全守卫通过生成显式CoT提升审核准确率与可解释性，但每次调用都生成数百token的推理过程，延迟过高无法适配大流量部署场景；现有隐式推理方法仅面向数学/逻辑推理任务，不支持安全场景必需的审计能力，无法满足工业化部署要求。

### 方法关键点
- 分阶段隐式推理课程：逐步将任务对齐的显式CoT片段替换为连续隐式状态，实现从显式推理监督到隐式计算的平滑训练过渡
- 自适应隐式预算推理：常规调用时动态生成隐式token，当<eor>概率超过阈值即停止推理，直接输出安全标签，无显式文本生成开销
- 隔离式按需审计解码器：采用stop-gradient机制训练独立的轻量解码器，仅在审计需求触发时将隐式状态转换为紧凑的审核证据，不占用主链路计算资源

### 关键实验结果
在GuardReasoner公开数据集上训练，对比GuardReasoner、LlamaGuard3/4、RobloxGuard等基线：
- LatentGuard-8B平均加权F1从GuardReasoner-8B的83.95提升至84.91
- 关键路径推理token从268.56个显式CoT token降至1.6个隐式token，单样本 latency 从0.792s降至0.089s，延迟降低8.9倍
- 按需审计解码器AUS（审计效用得分）达85.75，可生成符合审核要求的解释文本

### 核心洞见
将任务的常规执行链路与可解释/审计链路解耦，是兼顾高准确率、低延迟、可审计性的通用设计思路
