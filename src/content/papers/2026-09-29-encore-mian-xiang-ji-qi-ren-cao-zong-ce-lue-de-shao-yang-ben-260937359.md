---
title: 'Encore: Few-Shot Agentic Discovery of Manipulation Strategies'
title_zh: ENCORE：面向机器人操纵策略的少样本智能体发现方法
authors:
- Yifan Kang
- Zihan Wang
- Zhiwen Fan
- Bangya Liu
affiliations:
- Massachusetts Institute of Technology
- 2077AI Open Source Foundation
- Texas A&M University
- University of Wisconsin–Madison
arxiv_id: '2609.37359'
url: https://arxiv.org/abs/2609.37359
pdf_url: https://arxiv.org/pdf/2609.37359
published: '2026-09-29'
collected: '2026-10-13'
category: Agent
direction: 少样本编码智能体 · 操纵策略生成
tags:
- CodingAgent
- FewShotLearning
- DemonstrationDistillation
- PolicyGeneration
- Robotics
one_liner: 提出少样本编码智能体框架ENCORE，通过演示蒸馏生成可泛化的机器人操纵策略程序
practical_value: '- 少样本场景可借鉴「将演示样本蒸馏为多模态结构化特征包而非训练数据」的思路，降低电商新类目推荐、少样本商品文案生成的冷启动成本

  - 可复用「固定API接口+编码智能体迭代优化策略程序+无成功信号验证」的架构，用于推荐系统规则自动生成、电商导购Agent执行流程调优

  - 落地Agent系统时可参考「仿真环境迭代优化→冻结策略→真实环境部署」的流程，降低线上试错风险'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前编码智能体已能自主完成代码编写、运行、调试，但机器人任务的自然语言指令通常缺失抓取方式、接触顺序、结果形态等关键细节，仅给定指令的智能体需大量试错才能完成策略探索，效率极低。
### 方法关键点
1. 确定性演示蒸馏模块将少量演示样本提炼为包含多视角关键帧、夹爪事件、帧片段、完整轨迹的结构化演示包，无需作为训练数据微调模型；
2. 编码智能体基于演示包、固定感知与动作API编写策略程序，通过少量开发轮次迭代优化，冻结后在无成功信号反馈的封闭环境完成评估。
### 关键结果
- LIBERO-PRO数据集上首版程序即可在50%含扰动的演示任务、1个无演示任务上成功，冻结后策略准确率达96.3%，优于同基座LLM的SOTA智能体系统（89.3%）；
- 可落地到真实双臂机器人，仅需5次演示即可学会立方体交接、杯子翻转任务；无演示时RoboDojo未声明目标的任务成功率为0。
