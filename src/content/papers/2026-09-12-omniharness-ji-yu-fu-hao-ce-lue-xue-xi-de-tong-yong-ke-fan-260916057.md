---
title: 'OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy
  Learning'
title_zh: OmniHarness：基于符号策略学习的通用可泛化视觉生成框架
authors:
- Xu Xu
- Jinxiu Liu
- Zhangbo Qiao
- Jiaxing Lu
- Xiangyu Zhang
- Yubin Gu
- Fangwei Ning
- Yan Shi
affiliations:
- Beihang University
- The Chinese University of Hong Kong
- National University of Singapore
arxiv_id: '2609.16057'
url: https://arxiv.org/abs/2609.16057
pdf_url: https://arxiv.org/pdf/2609.16057
published: '2026-09-12'
collected: '2026-09-17'
category: Agent
direction: Agent 符号策略学习 视觉生成泛化
tags:
- Symbolic Policy
- Multi-Agent
- Visual Generation
- Self-Exploration
- Zero-Finetune
one_liner: 提出符号策略学习框架OmniHarness，无需微调即可大幅提升多场景视觉生成效果
practical_value: '- 可借鉴符号策略蒸馏思路，将电商推荐/广告场景下成功的工具调用、流程抽象为可复用模板，去掉实例特定参数，大幅提升跨任务泛化性，无需频繁微调LLM

  - 自定向探索的任务选择方法可直接复用：优先选择能力边界附近（预估成功率约50%）的未充分探索任务做训练，用最少样本快速扩充Agent能力边界，适合电商新品类、新活动的策略冷启动

  - 中间步骤验证+局部故障恢复机制可迁移到推荐系统多步生成场景（如文案+海报+落地页全链路生成），避免错误累积，降低生成失败率

  - 冻结策略快照的即插即用设计可降低业务迭代成本：把成熟策略封装为独立模块，新业务场景直接复用，无需重新训练整套系统'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）和多Agent视觉生成方案存在三个核心痛点：1）蒸馏的经验多为任务特定，泛化性差；2）仅在任务完成后复盘，中间错误易累积传播；3）仅被动响应下游任务需求，能力缺口无法提前填补，复杂生成任务成功率难以提升。

### 方法关键点
- 符号策略学习：将验证通过的执行流程蒸馏为视觉生成任务族的符号策略，保留共享流程和适用条件，移除实例特定输入，支持跨任务复用
- 反馈引导执行：执行过程中验证中间输出，定位失败步骤后做局部修复，避免错误累积，无需重跑全流程
- 自定向探索：在下游任务未明确前，自主生成能力边界附近的练习任务执行，基于反馈迭代优化策略库，全程不修改模型参数
- 策略库支持导出为冻结快照，可即插即用到其他视觉Agent系统

### 关键实验
在ComfyBench、GenEval、GenEval2、WISE、Reason-Edit共6个基准，3个MLLM骨干、3个视觉Agent框架上验证：ComfyBench创意任务解决率达95.0%，超出SOTA基线27.5个百分点；GenEval总体得分0.997，5个类别得分达1.0；移除自定向探索后创意任务解决率下降22.5个百分点，移除中间验证后复杂任务通过率下降25个百分点。

### 最值得记住的一句话
无需微调模型，仅通过可复用的符号策略库积累和动态优化，即可实现跨任务的视觉生成能力跃升，大幅降低Agent系统迭代成本。
