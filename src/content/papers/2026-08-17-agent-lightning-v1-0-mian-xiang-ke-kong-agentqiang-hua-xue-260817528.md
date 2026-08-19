---
title: 'Agent Lightning v1.0: Towards Harnessed Agentic RL'
title_zh: Agent Lightning v1.0：面向可控Agent强化学习的轻量框架
authors:
- Zhiyuan He
- Siwei Zhang
- Zhiwen Zhou
- Yuqing Yang
- Yu Kang
- Yuge Zhang
- Luna K. Qiu
- Tin Yan Tsui
- Jiahang Xu
- Chong Luo
affiliations:
- Microsoft
- Fudan University
- Zhejiang University
- University of Edinburgh
arxiv_id: '2608.17528'
url: https://arxiv.org/abs/2608.17528
pdf_url: https://arxiv.org/pdf/2608.17528
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent 强化学习训练框架优化
tags:
- Agentic RL
- Reinforcement Learning
- LLM Agent
- Training Framework
- Harnessed Agent
one_liner: 提出仅3500行代码的Harnessed Agent RL轻量框架，解决训练部署gap与四大工程挑战
practical_value: '- 电商导购/搜索Agent做RL训练时，可直接复用其rollout级advantage计算、loss归一化方案，避免动态样本导致的训练不稳定

  - 自研Agent训练框架可参考其collocated async调度策略，在不增加GPU资源的前提下实现约2倍端到端训练提速

  - 可借鉴其K8S原生Agent执行调度方案，替代商用沙箱服务，大幅降低大规模Agent训练的算力成本

  - 针对Agent奖励黑客问题，可复用其网络限制、操作权限管控的通用防护思路，避免训练过程中Agent作弊'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent强化学习训练框架要求将Agent执行逻辑嵌入训练侧，无法复用线上已成熟的Agent Harness（工具调度、上下文管理、控制流逻辑），导致训练与部署存在显著gap；同时新兴的Harnessed Agent RL范式面临重tokenization、advantage计算、loss归一化、后端调度四大未被系统性解决的挑战，易引发训练失效或不稳定。

### 方法关键点
- 采用解耦架构，通过LLM API Proxy连接任意Agent Harness与RL训练流程，无需修改原有Agent代码
- 针对四大挑战给出工程最优解：采用最佳努力样本合并策略避免重tokenization偏差，选择rollout级advantage计算消除动态样本数的影响，优先采用rollout级token-mean loss保障训练稳定，设计collocated async调度策略实现GPU时分复用提速
- 框架总代码量仅约3500行，支持K8S原生调度Agent执行任务，无需依赖商用沙箱服务，内置监控模块可自动识别奖励黑客等异常行为

### 关键实验
在三类Agent上验证效果：搜索Agent在HotpotQA等6个数据集上EM从25.1%提升到41.7%，绝对提升16.6%；通用指令跟随Agent验证集准确率从51.9%提升到70.2%，绝对提升18.3%；编码Agent仅用6K训练样本，将Qwen3.5-9B在SWE-bench Verified上的得分从41.8%提升到56.4%，绝对提升14.6%，训练效率比同步RL提升2倍。

### 核心结论
Harnessed Agent RL范式下，训练和部署使用同一套Agent Harness是消除训练部署gap、提升Agent落地效果的核心路径
