---
title: 'Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI
  Research and Development'
title_zh: 长周期AI研发Agent系统化评估：突破仅看最终得分的局限
authors:
- Yiwei Li
- Wanli Yang
- Hexiang Tan
- Xiangzhou Huang
- Zhengyu Chen
- Ziran Li
- Borun Chen
- Shanglin Lei
- Huaisheng Zhu
- Hao Tian
affiliations:
- Meituan
- University of Chinese Academy of Sciences
arxiv_id: '2608.13417'
url: https://arxiv.org/abs/2608.13417
pdf_url: https://arxiv.org/pdf/2608.13417
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: Agent 长周期研发能力评估
tags:
- Autonomous Agent
- Long-Horizon Task
- Agent Evaluation
- Experience Reuse
- Harness Optimization
one_liner: 提出覆盖过程能力、经验复用、工具链影响的长周期AI研发Agent细粒度评估框架
practical_value: '- 做推荐/广告调优类长周期Agent时，可复用这套C1/C2/C3过程指标做瓶颈诊断，不用仅靠最终AUC/GMV判断能力，精准定位是策略方向错、代码实现bug还是反馈迭代效率低的问题

  - 跨任务复用Agent经验时，优先选择Agent自生成的提炼式lesson而非全量历史上下文，可降低负迁移概率，比如跨不同类目推荐调优、不同广告位创意优化的经验迁移

  - Agent工具链（harness）优先落地版本控制、最优状态保护、停滞期跳出三个核心机制，无需改模型即可提升运行稳定性，缩小平均表现与峰值表现的差距

  - 业务场景下不要期待研发类Agent产出全新算法，将其限定在已知技术组合、超参调优、特征工程类场景，投入产出比更高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有长周期自主研发Agent的评估仅依赖最终任务得分，既无法定位迭代过程中的能力瓶颈，也无法衡量经验复用的实际效果，更忽略工具链对表现的影响，难以针对性指导Agent系统的迭代优化。
### 方法关键点
- 将长周期研发过程拆解为3个无LLM判别、可复现的规则化指标：**Solution Framing (C1)** 衡量方向选择的质量与效率，**Execution (C2)** 衡量方案实现的可靠性，**Feedback Control (C3)** 衡量最优结果保留与错误恢复能力
- 新增经验复用能力量化：通过反事实实验分别评估单任务内（Intra-task）、跨任务（Inter-task）经验的增益/负向影响
- 覆盖工具链（harness）影响评估：对比通用、模型原生、开源、自动演化四类工具链对表现的影响
- 补充创新性分析，区分现有技术组合、评测漏洞利用、真正方法论创新三类输出
### 关键结果
- 实验基于AutoLab的36个长周期任务，覆盖模型开发、系统优化、逻辑挑战、CUDA优化四类，评估7款前沿大模型，单任务重复3次实验，总成本约10万美元
- 7款模型Execution能力普遍达标（C2得分0.88~0.967），但Solution Framing（0.473~0.612）和Feedback Control（0.772~0.928）差异极大；模型间avg@3差距达0.237，远高于best@3的0.122，稳定性差异远大于峰值能力差异
- 仅1.2%的输出为真正创新，6.3%是利用评测漏洞；自动演化的harness可在系统优化类任务上提升avg@3达0.12
### 核心结论
当前长周期研发Agent本质是工程优化器而非自主研究者，平均表现的提升空间远大于峰值表现，优化优先级远高于模型本身的是过程瓶颈诊断、经验复用机制、工具链设计
