---
title: Scaling Verifiable Environments for Long-horizon Work Agents
title_zh: 面向长周期工作Agent的可验证环境规模化构建框架
authors:
- Jiazheng Zhang
- Long Ma
- Yunxian Yang
- Zhiheng Xi
- Zhikai Lei
- Yajie Yang
- Chenyang Liao
- Enyu Zhou
- Yang Nan
- Yuchen Tian
affiliations:
- Tencent
- Fudan University
arxiv_id: '2610.04906'
url: https://arxiv.org/abs/2610.04906
pdf_url: https://arxiv.org/pdf/2610.04906
published: '2026-10-07'
collected: '2026-10-15'
category: Agent
direction: 工作Agent · 长周期训练环境构建
tags:
- Work Agent
- Long-horizon Agent
- Environment Synthesis
- Verifiable Evaluation
- Agent Training
one_liner: 提出WORKFORGE框架，基于真实资源规模化构建可验证的长周期工作Agent训练环境
practical_value: '- 电商/广告领域Agent训练可借鉴该框架范式：先将业务专家的运营/投放/客服 workflow 抽象为场景蓝图，再匹配真实业务数据（商品库、投放报告、用户行为数据等）构建真实工作空间，避免合成训练数据脱离业务实际。

  - 效果验证可复用混合校验机制：业务Agent的输出验证结合程序式校验（ROI达标、文案合规等可量化指标）+ LLM语义校验（文案调性匹配、推荐理由合理性），比单一校验准确率更高，可大幅降低人工标注成本。

  - 训练数据选型可复用结论：优先选择交互轮次20+的长轨迹数据训练Agent，能显著提升其多步决策、跨数据源信息整合能力，尤其适配电商运营、投放优化等需要多环节操作的业务场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长周期工作Agent训练存在明显瓶颈：人工构建训练环境成本极高无法规模化，合成环境则真实性不足、复杂度低，验证规则脱离实际，导致训练出的Agent无法落地真实业务场景，亟需兼顾真实性、可验证性、可扩展性的环境构建方案。

### 方法关键点
- 先将领域专家的工作流抽象为场景蓝图，明确任务流程、输出要求、依赖资源、决策节点四大核心要素；
- 基于场景蓝图检索匹配真实资源池构建工作空间，同时抽取空间内可观测事实作为锚点，保障任务和验证的可追溯性；
- 基于事实锚点生成任务指令、隐藏解决方案，配套双验证器：程序式验证器校验确定性要求，语义验证器评估开放性输出；
- 用Solver Agent执行任务生成带标注的长交互轨迹，可直接用于Agent微调。

### 关键实验
构建覆盖40个专业领域（含电商、广告、营销）的16.7K可验证环境，支持60种文件类型，平均每个工作空间含42.3个文件。微调Qwen3.5-35B-A3B-Base后，GDPval从45.5提升至73.6，APEX Score从5.0提升至21.3；微调Qwen3.5-27B后GDPval达82.4，超过参数大15倍的Qwen3.5-397B-A17B，性能追平头部闭源模型。数据量越大、训练轨迹越长，Agent性能提升越显著，混合验证策略比单一验证效果高30%以上。

### 核心结论
Agent的任务设计和验证规则必须锚定真实工作空间的可观测事实，才能保证训练出的能力可迁移到真实业务场景。
