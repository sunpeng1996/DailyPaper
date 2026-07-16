---
title: 'SPyCE: Skill-Policy Co-evolution for Multimodal Agents'
title_zh: SPyCE：面向多模态智能体的技能-策略协同进化框架
authors:
- Ru Zhang
- Weijie Qiu
affiliations:
- Zhejiang University
- Beijing University of Posts and Telecommunications
arxiv_id: '2607.13854'
url: https://arxiv.org/abs/2607.13854
pdf_url: https://arxiv.org/pdf/2607.13854
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: 多模态Agent · 技能-策略协同优化
tags:
- Multimodal Agent
- Reinforcement Learning
- Skill Library
- Co-evolution
- GRPO
- Tool Use
one_liner: 提出分层技能库与策略的闭环进化机制，大幅提升多模态Agent工具使用效率与任务效果
practical_value: '- 电商多模态导购/商品理解Agent可直接复用分层技能库设计：将高频局部操作（商品图旋转、裁剪放大、OCR提取）封装为条件-动作-效果三元组的执行技能，将流程类逻辑（品类识别→参数提取→规格匹配）封装为工作流技能，减少重复探索

  - Agent训练阶段可复用技能-策略闭环机制：定期将高价值（GRPO相对优势靠前）交互轨迹蒸馏更新到技能库，再用技能引导策略采样，相比纯GRPO训练任务成功率提升约4%，同时降低工具调用次数，压缩推理成本

  - 奖励设计可直接落地：仅对成功轨迹施加工具调用惩罚，既不会抑制前期必要探索，又能避免冗余操作，平衡任务效果与推理效率

  - 技能库运维规则可复用：采用余弦相似度去重+按调用成功率冷启动淘汰的合并-添加-剪枝规则，控制技能库规模，避免检索噪声'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态Agent强化学习方法仅将交互轨迹转化为标量奖励，工具使用模式需要每个新任务从零探索，样本效率低；记忆类方法仅依赖测试时检索静态经验，没有将可复用模式更新到策略中，长序列工具调度不稳定，在视觉搜索、图表分析、商品参数识别等多模态交互任务上效果瓶颈明显。

### 方法关键点
- 构建双层分层技能库：执行技能封装局部视觉操作的「条件-动作-效果」三元组，解决具体视觉瓶颈；工作流技能封装「瓶颈描述-流程框架」对，指导全局多步工具编排
- 实现技能-策略协同进化闭环：策略基于检索到的分层技能生成rollout，定期筛选GRPO相对优势靠前的高价值成功轨迹，蒸馏更新到技能库，通过合并/去重/低质淘汰规则控制技能库质量，形成「更好的策略产出更高质量轨迹→更好的技能引导策略优化」的正循环
- 定制奖励函数：仅对成功轨迹施加工具调用惩罚，避免过度抑制探索的同时减少冗余操作

### 关键结果
在8个基准（覆盖视觉搜索、多模态推理、Agent思考类任务）上测试，基于Qwen3-VL-8B backbone，相比纯GRPO基线，TIR-Bench任务成功率提升4.3pp，工具调用数减少0.3次；视觉搜索V*基准准确率提升2.1pp，MathVerse数学推理准确率提升2.2pp，所有基准均达到SOTA。

**最值得记住的结论**：多模态Agent优化不要仅聚焦奖励设计，将交互轨迹蒸馏为可复用的分层技能、与策略形成闭环进化，是同时提升效果、训练效率、推理效率的核心路径。
