---
title: 'Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents'
title_zh: Mid-Harness：在模型与执行框架层实现终端Agent动作规模扩展
authors:
- Minki Kang
- Ryo Hachiuma
- Shaokun Zhang
- Subhashree Radhakrishnan
- Yonggan Fu
- Jindong Jiang
- Mingjie Liu
- Ehsan Hosseini-Asl
- Yi Dong
- Yu-Chiang Frank Wang
affiliations:
- NVIDIA
- KAIST
arxiv_id: '2609.39982'
url: https://arxiv.org/abs/2609.39982
pdf_url: https://arxiv.org/pdf/2609.39982
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: 终端Agent · 测试时动作验证优化
tags:
- Agent
- Test-Time Scaling
- Verification
- Action Selection
- Distillation
- LoRA
one_liner: 在模型与执行框架间新增动作采样验证层，无需改动原有组件即可提升终端Agent任务成功率
practical_value: '- 电商Agent系统迭代可复用无侵入式中间层设计：无需修改基座模型、业务执行逻辑，仅在模型调用接口层新增动作采样验证逻辑即可快速提升任务成功率，适配智能客服、订单处理、售后工单等长流程Agent场景

  - 验证机制优先选择pairwise对比方案：效果优于listwise、pointwise，可通过强teacher模型的pairwise标注数据用LoRA微调小模型作为verifier，完全不影响原有动作生成器的性能

  - 长流程任务可复用动作+轨迹混合缩放策略：动作层验证搭配Best-of-T、Sequential Refine等轨迹层缩放方法，比单纯增加轨迹生成量的token成本降低50%以上，可有效平衡业务效果与推理成本

  - 成本敏感场景可采用decision-only verifier：无需生成推理过程仅输出偏好标签，可降低20%+的token成本，中小模型下精度损失可控'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
终端Agent执行的每个动作都会改变环境状态，单次生成的错误动作（如错误命令、无效操作）会导致后续全流程失败，即使模型本身有能力生成正确动作。现有测试时计算缩放多聚焦轨迹层面的优化，动作层面采样与验证的有效性边界尚未被系统研究，产业界迫切需要无需改动原有基座模型、执行框架即可提升Agent效果的方案。

### 方法关键点
- 无侵入式Mid-Harness层：封装在模型调用接口内部，对原有动作生成器、执行框架完全透明；每步基于相同上下文采样N个候选动作，经过验证器筛选最优动作后再送入执行框架
- 三类验证机制对比：listwise（全候选集一次性排序）、pointwise（单个候选独立打分）、pairwise（两两组队对比后聚合排序），其中pairwise验证效果最优
- 蒸馏优化方案：用强模型（GPT-5.6 Sol）的pairwise标注数据，通过LoRA微调轻量verifier，全程不改动原动作生成器的权重
- 兼容现有轨迹层缩放方法：可与Best-of-T、Sequential Refine等轨迹优化方案无缝结合，无需增加环境执行次数

### 关键实验
在TerminalBench-Lite、SWE-bench-Verified、FeatureBench-Mini等数据集上验证，对比base agent、Best-of-T、Sequential Refine等baseline：
1. 固定TMAX-9B生成器，搭配GPT-5.6 Sol作为verifier，N=8时Pass@1从base的50.00%提升至68.03%
2. 自验证场景下，pairwise验证比listwise高3.74个百分点，蒸馏后进一步提升2.38个百分点
3. 搭配Sequential Refine（R=1）时Pass@1达60.20%，优于Best-of-T（T=7）的59.18%，token成本仅为后者的一半不到

### 核心结论
测试时计算资源投入到动作层面的精准验证，比单纯增加生成轨迹数的投入产出比更高。
