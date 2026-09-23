---
title: 'The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks'
title_zh: 长周期任务下Agent决策品味的自动化测量与蒸馏优化
authors:
- Wenbo Pan
- Zhichao Liu
- Shujie Liu
- Jingying Zeng
- Chin-Yew Lin
- Xianfeng Tang
- Yan Lu
- Qi He
- Xiaohua Jia
affiliations:
- City University of Hong Kong
- Microsoft
- Independent Researcher
arxiv_id: '2609.25804'
url: https://arxiv.org/abs/2609.25804
pdf_url: https://arxiv.org/pdf/2609.25804
published: '2026-09-21'
collected: '2026-09-23'
category: Agent
direction: Agent长周期决策能力评测与优化
tags:
- LLM Agent
- Long-Horizon Task
- Agent Evaluation
- Knowledge Distillation
- Decision Making
one_liner: 提出无人工标注的Agent长周期决策品味基准Taste-Bench与可迁移的品味蒸馏方案
practical_value: '- 长周期导购/推荐Agent的决策点挖掘：可复用平行轨迹+单轨迹回退的决策分叉挖掘方法，从用户浏览转化路径、Agent服务日志中自动标注好坏决策，无需人工标注，可用于优化多轮推荐、用户留存运营等场景的Agent策略。

  - Agent决策能力蒸馏落地trick：不要直接拟合二进制决策标签，蒸馏带全局信息的教师模型的完整推理过程，用LoRA微调小模型作为独立决策顾问，和执行Agent解耦，可降低大模型调用成本，适配推荐/广告系统的低延迟要求。

  - Agent评测体系优化：现有推荐/导购Agent仅看端到端转化指标，可加入中间决策点准确率评估，更精准定位Agent能力短板，比如长周期复购推荐任务中单独评估商品选择、触达时机的决策质量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期Agent评测仅关注端到端任务成功率，无法衡量中间决策的质量（即「决策品味」）；而长周期任务中关键中间决策直接决定最终结果，错误决策的成本往往在后期才显现，人工标注决策质量成本高、跨域扩展性差，缺少自动化评测方案。

### 方法关键点
- 定义决策分叉（decision fork）概念：从Agent执行轨迹中自动挖掘相同前缀下的多方向选择点，用后续轨迹的实际结果自动标注最优选择，无需人工标注。
- 构建Taste-Bench基准：包含502个来自软件工程、机器学习研究领域的决策分叉问题，来源分两类：同任务的平行轨迹分叉、单轨迹内的自我修正回退分叉，经过去简单题、去歧义过滤，人工标注一致性达98.8%。
- 品味蒸馏方案：用带结果特权信息的教师模型生成完整推理过程，蒸馏到仅能看到决策点前上下文的学生模型（LoRA微调），训练后的学生模型可作为独立顾问为执行Agent提供决策建议。

### 关键结果
评测14款前沿大模型，最优GPT-5.6 Sol准确率仅59.7%；决策证据出现越晚的分叉难度越高，最长时间 horizon 的分叉平均准确率仅21%，接近随机猜测，且增加推理预算无法提升准确率。蒸馏后的学生模型在unseen任务上决策准确率比基线提升17.9个百分点，给执行Agent注入建议后，SWE-bench Pro任务成功率从14.6%提升到33.7%，接近最优决策上限39%。

**最值得记住的一句话**：长周期任务的核心瓶颈不是即时推理能力，而是对长期后果的预判能力，这种能力可通过轨迹蒸馏迁移，无需昂贵人工标注。
