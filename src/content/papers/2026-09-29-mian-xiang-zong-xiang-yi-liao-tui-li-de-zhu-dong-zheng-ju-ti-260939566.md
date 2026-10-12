---
title: 'From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical
  Reasoning'
title_zh: 面向纵向医疗推理的主动证据搜索智能体学习框架CASE
authors:
- Minye Shao
- Chaohui Yu
- Yixuan Wu
- Fan Wang
- Ling Shao
- Yang Long
affiliations:
- Durham University
- DAMO Academy, Alibaba Group
- Hupan Laboratory
- University of the Chinese Academy of Sciences
arxiv_id: '2609.39566'
url: https://arxiv.org/abs/2609.39566
pdf_url: https://arxiv.org/pdf/2609.39566
published: '2026-09-29'
collected: '2026-10-12'
category: Agent
direction: Agent · 多模态纵向推理训练优化
tags:
- Agent
- Medical Reasoning
- Multimodal
- Reinforcement Learning
- RLAIF
- Distillation
one_liner: 提出分角色医疗证据搜索智能体与训练范式，在自建基准上超越前沿通用多模态大模型
practical_value: '- 两阶段Agent训练范式可复用：先用SFT对齐顶流大模型的工具调用轨迹冷启动，再用GRPO+RLAIF+自蒸馏做agentic
  RL优化，无需硬编码工具调用逻辑，适合电商导购Agent、搜索多轮query理解Agent的训练

  - 特权自蒸馏（OPSD）trick可直接复用：训练后期用带答案的特权视图对齐普通视图的分布，解决Agent生成重复无意义内容、无法收敛到结论的问题，适配所有长路径Agent训练

  - 预计算工具返回结果的工程优化值得参考：Agent训练时提前预计算所有可能的工具返回结果，避免每次调用工具的GPU等待开销，大幅提升RL训练效率，适合所有工具增强Agent的训练

  - 证据优先的评估逻辑可迁移：推荐/搜索场景可效仿将「信息获取完整性」而非仅「最终结果准确率」作为评估指标，提升生成式推荐、多轮搜索的结果可信度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有医疗推理基准均基于预设给定的证据做QA，不要求智能体主动从分散的跨时间临床记录、多模态影像中搜索证据，无法模拟真实临床场景的纵向推理需求；同时小参数多模态模型如何脱离对顶流大模型的轨迹模仿，通过自主交互提升推理能力也缺乏成熟方案。
### 方法关键点
- 提出CASE框架：单共享Qwen3-VL-8B策略通过角色提示实例化放射科医生、解剖学家、顾问3个分角色Agent，共享工具调用交互逻辑，仅角色提示和工具集存在差异
- 两阶段训练：第一阶段用拒绝采样SFT（RSFT）过滤14k+顶流大模型的交互轨迹做冷启动，仅学习工具调用格式和基础交互逻辑；第二阶段用agentic RL做自主交互优化，融合结果准确率奖励、rubric规则的RLAIF洞察评分奖励、特权在路自蒸馏（OPSD）惩罚重复推理三类信号，加权后输入GRPO做策略更新
- 自建基准：基于UK Biobank构建包含4739名受试者、50401个ICD-10编码真实临床问题的纵向多模态基准，每个问题关联受试者基线+随访的多序列MRI、临床记录，要求Agent自主选择访问的随访批次、器官、模态、工具完成推理
### 关键结果
- 基于Qwen3-VL-8B的CASE Agent在匹配评估条件下，答案准确率相对GPT-5.4提升16%+，相对Claude Opus 4.8提升10%+
- 消融实验显示单独添加RLAIF可提升准确率~4.9%，单独添加OPSD可提升~8.1%，二者结合提升~10.4%，OPSD可有效解决RL训练后期模型重复输出、奖励崩溃的问题

**最值得记住的结论**：Agent训练的核心增益并非来自对顶流大模型轨迹的模仿，而是来自自主交互过程中对证据获取和推理逻辑的端到端优化
