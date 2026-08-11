---
title: 'Intent Speaks Louder: Controllable User Simulation Beyond Response Imitation'
title_zh: 脱离响应模仿：基于显式意图对齐的可控用户模拟框架UserIDA
authors:
- Bo Wang
- Ruixing Zhang
- Yunqi Liu
- Yang Zhang
- Liangzhe Han
- Tongyu Zhu
- Leilei Sun
affiliations:
- Beihang University
arxiv_id: '2608.09420'
url: https://arxiv.org/abs/2608.09420
pdf_url: https://arxiv.org/pdf/2608.09420
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: 可控用户模拟 · 意图对齐
tags:
- User Simulation
- Controllable Generation
- Intent Alignment
- SFT
- GRPO
one_liner: 将交互意图作为轮次显式控制变量，提出UserIDA框架大幅提升用户模拟器意图准确性与可控性
practical_value: '- 做电商导购/客服Agent的仿真评估时，可复用本文6类交互意图标签体系，构造可控多轮用户行为轨迹，替代部分真人测试降低成本

  - 训练可控生成模型时，可借鉴意图校准的GRPO优化思路：先对符合控制目标的候选做奖励保底排序，再在合规候选内部优化语义/风格质量，避免高质量但不符合控制要求的输出占优

  - 电商搜索/推荐的多轮用户行为仿真，可借鉴用户全局画像+轮次局部意图解耦的框架，提升模拟轨迹的可控性与多样性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM用户模拟器多基于响应模仿，相同对话上下文可生成多种语义通顺但意图不符合预期的回复，无法支撑可控的多轮交互评估与Agent训练，缺少轮次级的显式意图控制变量。
### 方法关键点
- 定义6类轮次级交互意图指令集（Initiate/Amend/Supply/Repair/SetRegister/GroundAccept）作为显式控制输入，不约束具体表达形式
- 第一阶段做Intent-SFT：基于标注的意图-上下文-用户回复三元组做指令微调，学习同一上下文下不同意图的生成逻辑
- 第二阶段做意图校准的GRPO优化：混合候选组内将所有不符合目标意图的候选奖励调低至低于所有合规候选，再在合规候选内优化语义、风格相似度与真人相似度，避免高质量违规样本占优
### 关键结果
基于LMSYS-USP数据集，对比USP、UserLM等专用用户模拟器和GPT-4o、Gemini等通用大模型，UserIDA实现86.6%的轮次意图准确率，比最强专用baseline USP高24.3个百分点；上下文内干预实验中，91.7%的对话状态可实现至少4种目标意图，远高于baseline的22.9%；多轮轨迹全轮次意图成功率从13%提升到58%，同时保留语义、风格一致性。
### 核心结论
用户模拟需要将轮次局部交互意图控制和响应保真度作为两个互补的优化维度，仅优化响应相似度可能反而降低意图合规性。
