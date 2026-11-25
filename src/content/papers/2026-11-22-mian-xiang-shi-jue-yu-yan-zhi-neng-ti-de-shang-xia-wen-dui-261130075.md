---
title: Context-Grounded Skill Internalization for Vision-Language Agents
title_zh: 面向视觉语言智能体的上下文对齐技能内化方法
authors:
- Jinlin Liu
- Yumeng He
- Qihan Huang
- Kevin Qinghong Lin
- Han Peng
affiliations:
- Ant Group
- The University of Hong Kong
- Shanghai Jiao Tong University
- University of Oxford
arxiv_id: '2611.30075'
url: https://arxiv.org/abs/2611.30075
pdf_url: https://arxiv.org/pdf/2611.30075
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: 多模态Agent · 技能内化优化
tags:
- Vision-Language Agent
- Skill Internalization
- Context Misalignment
- SFT
- Hallucination
one_liner: 提出CGSI框架解决智能体技能内化时的上下文错位问题，降幻觉同时保性能
practical_value: '- 做Agent技能内化时可直接复用CGSI的loss mask策略：无需修改原始轨迹内容，仅屏蔽错位句子的损失监督，即可在不损失任务效果的前提下大幅降低无依据引用类幻觉，适合将RAG沉淀的领域技能内化到模型权重，减少推理时context长度，降低KV
  cache开销

  - 错位句子检测的特征构造方案可迁移：用有/无技能上下文的token生成概率差（mean gap、peak4 gap）+ 无技能上下文隐层语义特征训轻量分类器，相比全量VLM审计降本90%以上，适合业务侧大规模清洗Agent交互轨迹数据

  - 业务中Agent训练链路需前置CoMi治理：技能内化SFT阶段引入的CoMi不会被后续RL阶段消除，若未治理会导致上线后Agent出现无依据引用（如电商导购Agent提及不存在的活动规则），严重影响用户信任'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent主流技能内化方案为「带技能生成示范轨迹→移除技能后做SFT」，会引发上下文错位（CoMi）问题：模型输出会引用已被移除的技能，测试阶段12.2~46.0%的轨迹存在该问题，既损害可解释性，还可能导致模型违背当前指令，现有RL类内化方案训练成本高，全量VLM审计修正方案数据处理成本高。
### 方法关键点
- 提出CGSI框架，分两步落地：先训练轻量句子级错位检测器，再基于检测结果做上下文对齐SFT
- 检测器结合两类特征：① 有/无技能上下文下的句子token生成概率差（全局均值、4 token连续窗口峰值），捕捉句子对技能的依赖度；② 无技能上下文下的句子隐层语义表征，区分引用类表述和正常规划表述，用逻辑回归即可完成训练
- 对齐SFT支持两种策略：优先用loss mask，仅屏蔽错位句子的损失监督，保留上下文前缀不影响后续动作生成；可选VLM改写错位句子后再训练
### 关键实验
在ALFWorld、WebShop、ARC-AGI三个基准上测试Qwen3.5-4B/9B：
- 全参数SFT下，CGSI-Mask相对直接移除技能SFT基线，降低72.5~94.6%的CoMi，同时任务成功率无损失，例如WebShop-4B场景CoMi从46.0%降至3.4%
- 相比RL类技能内化基线Skill0，CGSI仅用1/15的训练时间就达到更高成功率（85.0% vs 81.0%）
- 相比全量VLM审计修正，CGSI降低91.0~96.1%的API成本，ARC数据集2281条轨迹处理成本从$1378降至$165（改写版）或0（mask版）
### 核心结论
技能内化SFT阶段的上下文错位不会被后续RL消除，必须在SFT阶段就确保监督信号与模型可见上下文对齐。
